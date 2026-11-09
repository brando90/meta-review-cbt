#!/usr/bin/env python3
"""Retrieve DOI metadata and reading copies; metadata is not content verification.

Usage: python3 scripts/retrieve_sources.py
Run from any directory. Copyrighted reading copies stay in gitignored _build/.
Public receipts contain metadata, source URLs, retrieval times and hashes only.
Requires beautifulsoup4 for reading public PMC HTML when XML is unavailable.
"""

import argparse
import hashlib
import json
from pathlib import Path
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "meta-review-cbt/1.0 (literature verification; mailto:brando9@stanford.edu)"


def retrieve(url, path):
    if path.exists():
        return path.read_bytes()
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=60) as response:
                content = response.read()
            path.write_bytes(content)
            return content
        except (HTTPError, URLError, TimeoutError) as exc:
            if isinstance(exc, HTTPError) and exc.code not in (429, 500, 502, 503, 504):
                raise
            if attempt == 2:
                raise
            time.sleep(3 * (attempt + 1))
    raise RuntimeError("Unreachable retry state")


def plain_xml(text):
    return " ".join(BeautifulSoup(text, "html.parser").get_text(" ").split())


def retrieve_public_html(key, pmcid, receipt, cache):
    url = "https://pmc.ncbi.nlm.nih.gov/articles/" + pmcid + "/"
    try:
        raw = retrieve(url, cache / (key + ".html"))
        article = BeautifulSoup(raw, "html.parser").find("article")
        if article is None:
            raise ValueError("No article body in public HTML response")
        paragraphs = [node.get_text(" ", strip=True) for node in article.find_all(["h1", "h2", "h3", "h4", "p", "table"])]
        (cache / (key + ".fulltext.txt")).write_text("\n\n".join(paragraphs) + "\n")
        receipt["fulltext_url"] = url
        receipt["fulltext_sha256"] = hashlib.sha256(raw).hexdigest()
        receipt["fulltext_format"] = "public PMC HTML"
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        receipt["fulltext_html_error"] = str(exc)


def retrieve_one(source, cache):
    key, doi = source["key"], source["doi"]
    crossref_url = "https://api.crossref.org/works/" + quote(doi, safe="")
    raw = retrieve(crossref_url, cache / (key + ".crossref.json"))
    metadata = json.loads(raw)["message"]
    if metadata["DOI"].casefold() != doi.casefold():
        raise ValueError(f"Crossref DOI mismatch for {key}")
    receipt = {
        "key": key,
        "doi": metadata["DOI"],
        "crossref_url": crossref_url,
        "crossref_sha256": hashlib.sha256(raw).hexdigest(),
        "title": metadata.get("title", []),
        "authors": [{field: author[field] for field in ("given", "family") if field in author}
                    for author in metadata.get("author", [])],
        "journal": metadata.get("container-title", []),
        "published": metadata.get("published", {}).get("date-parts"),
        "published_print": metadata.get("published-print", {}).get("date-parts"),
        "published_online": metadata.get("published-online", {}).get("date-parts"),
        "volume": metadata.get("volume"),
        "issue": metadata.get("issue"),
        "pages": metadata.get("page"),
        "crossref_retrieved_at_utc": datetime.fromtimestamp(
            (cache / (key + ".crossref.json")).stat().st_mtime, timezone.utc
        ).isoformat(),
        "content_read_status": "NOT_ESTABLISHED_BY_RETRIEVAL",
    }
    query = 'DOI:"' + doi + '"'
    if source.get("europepmc_query"):
        query = source["europepmc_query"]
    epmc_url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode({
        "query": query, "format": "json", "resultType": "core", "pageSize": 5,
    })
    epmc_raw = retrieve(epmc_url, cache / (key + ".epmc.json"))
    records = json.loads(epmc_raw).get("resultList", {}).get("result", [])
    receipt["europepmc_url"] = epmc_url
    receipt["europepmc_sha256"] = hashlib.sha256(epmc_raw).hexdigest()
    receipt["europepmc_matches"] = len(records)
    abstract = plain_xml(metadata.get("abstract", ""))
    if len(records) == 1:
        record = records[0]
        if record.get("doi") and record["doi"].casefold() != doi.casefold():
            raise ValueError(f"Europe PMC DOI mismatch for {key}")
        receipt["pmid"] = record.get("pmid")
        receipt["pmcid"] = record.get("pmcid")
        receipt["europepmc_title"] = record.get("title")
        abstract = plain_xml(record.get("abstractText", "")) or abstract
        if record.get("pmcid"):
            full_url = "https://www.ebi.ac.uk/europepmc/webservices/rest/" + record["pmcid"] + "/fullTextXML"
            try:
                full_raw = retrieve(full_url, cache / (key + ".xml"))
                root = ET.fromstring(full_raw)
                if root.find(".//body") is None:
                    raise ValueError("XML response has no article body")
                paragraphs = [" ".join("".join(node.itertext()).split())
                              for node in root.iter() if node.tag in ("article-title", "title", "p", "caption")]
                (cache / (key + ".fulltext.txt")).write_text("\n\n".join(paragraphs) + "\n")
                receipt["fulltext_url"] = full_url
                receipt["fulltext_sha256"] = hashlib.sha256(full_raw).hexdigest()
            except (HTTPError, URLError, TimeoutError, ET.ParseError, ValueError) as exc:
                receipt["fulltext_xml_error"] = str(exc)
                retrieve_public_html(key, record["pmcid"], receipt, cache)
    (cache / (key + ".abstract.txt")).write_text(
        "\n".join(receipt["title"]) + "\nhttps://doi.org/" + doi + "\n\n" + abstract + "\n"
    )
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Folder containing sources/source_manifest.json")
    root = parser.parse_args().root.resolve()
    cache = root / "_build" / "sources"
    cache.mkdir(parents=True, exist_ok=True)
    sources = json.loads((root / "sources" / "source_manifest.json").read_text())
    receipts = []
    for source in sources:
        try:
            receipt = retrieve_one(source, cache)
            receipts.append(receipt)
            print(source["key"], "metadata retrieved; full text:", bool(receipt.get("fulltext_url")), flush=True)
        except (HTTPError, URLError, TimeoutError, KeyError, ValueError) as exc:
            receipts.append({"key": source["key"], "doi": source["doi"], "error": str(exc)})
            print(source["key"], "ERROR", exc, flush=True)
        (cache / "retrieval_receipts.json").write_text(json.dumps(receipts, indent=2, ensure_ascii=False) + "\n")
        time.sleep(1)
    if any("error" in receipt for receipt in receipts):
        raise SystemExit("Some metadata requests failed; see _build/sources/retrieval_receipts.json")


if __name__ == "__main__":
    main()
