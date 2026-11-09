#!/usr/bin/env python3
"""Check manuscript citations and the targeted revision's public source records.

No network calls or model calls. This checks consistency, not the truth of a
paper's findings or whether a person actually read it. The BibTeX parser targets
this repository's one-field-per-line, brace-delimited bibliography format.
"""

import collections
import hashlib
import html
import json
from pathlib import Path
import re
import unicodedata

REPO = Path(__file__).resolve().parents[3]


def normalize(text):
    text = html.unescape(re.sub(r"<[^>]+>", "", text))
    text = unicodedata.normalize("NFKD", text)
    return "".join(c.lower() for c in text if c.isalnum())


def bibliography():
    text = (REPO / "deep-research/references.bib").read_text()
    entries = {}
    for match in re.finditer(r"^@\w+\{([^,]+),\n(.*?)^\}\s*$", text, re.M | re.S):
        key, body = match.groups()
        assert key not in entries, f"Duplicate bibliography key: {key}"
        entries[key] = dict(re.findall(r"^\s+(\w+)\s*=\s*\{(.*)\},?\s*$", body, re.M))
    assert len(entries) == len(re.findall(r"^@\w+\{", text, re.M)), "Unparsed bibliography entry"
    return entries


def authors_match(author_field, source_authors):
    actual = [normalize(author.split(",")[0]) for author in author_field.split(" and ")]
    expected = [normalize(author["family"]) for author in source_authors]
    if actual[-1:] == ["others"]:  # BibTeX's explicit truncated-author marker.
        prefix = actual[:-1]
        return 0 < len(prefix) < len(expected) and prefix == expected[:len(prefix)]
    return actual == expected


def citation_keys(tex):
    cited = set()
    for group in re.findall(r"\\cite(?!gap\b)\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}", tex):
        cited.update(key.strip() for key in group.split(","))
    return cited


def main():
    entries = bibliography()
    tex = "\n".join(p.read_text() for p in sorted((REPO / "latex").rglob("*.tex")))
    cited = citation_keys(tex)
    gaps = re.findall(r"\\citegap\{([^}]+)\}", tex)
    assert not gaps, f"Unresolved citation-gap markers: {gaps}"
    assert not (cited - entries.keys()), f"Undefined citations: {cited - entries.keys()}"
    labels = re.findall(r"\\label\{([^}]+)\}", tex)
    assert len(labels) == len(set(labels)), "Duplicate LaTeX labels"
    refs = set(re.findall(r"\\(?:ref|pageref|autoref)\{([^}]+)\}", tex))
    assert not refs.difference(labels), f"Undefined labels: {refs.difference(labels)}"
    statuses = collections.Counter()
    checked_keys = set()
    for root in sorted((REPO / "experiments").glob("0[123]_*")):
        metadata = {x["key"]: x for x in json.loads((root / "sources/metadata_receipts.json").read_text())}
        manifest = json.loads((root / "sources/source_manifest.json").read_text())
        if isinstance(manifest, dict):
            manifest = manifest["sources"]
        assert set(metadata) == {x["key"] for x in manifest}, root
        readings = json.loads((root / "sources/reading_receipts.json").read_text())
        assert {x["key"] for x in readings} == set(metadata), root
        for row in readings:
            key = row["key"]
            assert key not in checked_keys, f"Duplicate candidate: {key}"
            checked_keys.add(key)
            statuses[row["status"]] += 1
            assert row["manuscript_cited"] == (key in cited), f"Stale citation inventory: {key}"
            if row["status"] == "METADATA_ONLY_EXCLUDED":
                assert key not in cited, key
            for file in row["files"]:
                path = root / file["path"]
                if path.exists():
                    assert hashlib.sha256(path.read_bytes()).hexdigest() == file["sha256"], path
            if key not in entries:
                continue  # Read but unused candidates need not enter the bibliography.
            entry, source = entries[key], metadata[key]
            assert entry["doi"].lower() == source["doi"].lower(), f"DOI mismatch: {key}"
            assert normalize(entry["title"]) == normalize(source["title"][0]), f"Title mismatch: {key}"
            assert authors_match(entry["author"], source["authors"]), f"Author mismatch: {key}"
            years = {dates[0][0] for field in ("published", "published_print", "published_online") if (dates := source.get(field))}
            assert int(entry["year"]) in years, f"Year mismatch: {key}"
    report = {
        "bibliography_entries": len(entries),
        "unique_cited_keys": len(cited),
        "undefined_citations": 0,
        "unresolved_citation_gaps": 0,
        "unique_labels": len(labels),
        "undefined_references": 0,
        "candidate_records": len(checked_keys),
        "reading_status_counts": dict(sorted(statuses.items())),
        "note": "Consistency checks only; content-reading decisions remain explicit human/agent records.",
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
