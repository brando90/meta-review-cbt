#!/usr/bin/env python3
"""Export public metadata and the explicitly recorded reading decisions.

This does not read papers on behalf of a reviewer. FULL_PASSAGES and
ABSTRACT_ONLY explicitly list the November 2026 reading decisions. Unknown keys
and changed previously recorded reading copies require a new manual check.
Run after retrieve_sources.py for the three experiment folders. Copyrighted
reading copies stay in ignored _build/. Hashes identify the copies inspected.
"""

import hashlib
import json
from pathlib import Path
import re

REPO = Path(__file__).resolve().parents[3]
FULL_PASSAGES = {
    "preuss2022evolution": "Abstract, evolutionary fundamentals, cortical organization",
    "dolan2013goals": "Instrumental/habit definitions, neural interactions, computational and Pavlovian sections",
    "taylor2021awareness": "Methods, results, discussion, limitations, competing interests",
    "richards2016cobra": "Methods and primary outcome results",
    "krause2022claustrophobia": "Methods, results, discussion passages",
    "sipka2025factorial": "Design, component descriptions and outcome passages",
    "driessen2015publicationbias": "Methods, Table 2, results, reasons for non-publication, discussion",
    "leichsenring2018plurality": "Abstract and relevant main-text argument",
    "hayes2006act": "Author-manuscript definitions of acceptance, defusion, values and committed action",
    "fluckiger2018alliance": "Abstract and full-text definition/causality passages",
    "craske2014maximizing": "Author-manuscript inhibitory-learning model, response-system divergence, expectancy-violation and consolidation passages",
}
EXCLUDED = {"mahoney1977prejudices": "Metadata only; no abstract; publisher routes returned challenge pages"}
ABSTRACT_ONLY = {
    "Delgadillo2018Feedback", "abramowitz2001suppression", "baldwin2007alliance", "berridge2016liking",
    "beutler2018reactance", "brembs2002operant", "burlingame2016group",
    "carlbring2018icbt", "cuijpers2010publicationbias",
    "cuijpers2017components", "dewit2018failures", "doll2009instruction",
    "emerson2010peerreview", "eubanks2018rupture", "fluckiger2020reciprocal",
    "grillner2016basal", "hofmann2008extinction", "jacobson1996component",
    "johnco2025restructuring", "krebs2018readiness", "li2011instructed",
    "longmore2007challenge", "ludwig2020selfregulation", "munder2013allegiance",
    "pittig2021intensified", "schultz1997reward", "stockton2019mediation",
    "tolin2010cbt", "truijens2019manual", "wood2016habit", "yin2004lesions", "yin2006habits",
    "zimmerman2024allegiance",
}
RECORDED_KEYS = set(FULL_PASSAGES) | ABSTRACT_ONLY | set(EXCLUDED)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_copy(path, root, previous):
    relative = str(path.relative_to(root))
    digest = sha256(path)
    prior = {entry["path"]: entry["sha256"] for entry in previous.get("files", [])}
    if relative in prior and prior[relative] != digest:
        raise ValueError(f"Copy changed since recorded reading; inspect it again: {relative}")
    return {"path": relative, "sha256": digest}


def export(root, cited):
    cache = root / "_build" / "sources"
    metadata = json.loads((cache / "retrieval_receipts.json").read_text())
    previous_path = root / "sources" / "reading_receipts.json"
    previous = {row["key"]: row for row in json.loads(previous_path.read_text())} if previous_path.exists() else {}
    readings = []
    for record in metadata:
        key = record["key"]
        if key not in RECORDED_KEYS:
            raise ValueError(f"No explicit reading decision recorded for: {key}")
        if "error" in record:
            raise ValueError(f"Unresolved metadata: {key}")
        crossref = cache / (key + ".crossref.json")
        if sha256(crossref) != record["crossref_sha256"]:
            raise ValueError(f"Metadata changed since retrieval: {key}")
        row = {
            "key": key,
            "doi": record["doi"],
            "identity_checked": "Crossref title, authors and publication year checked against intended citation",
            "reading_date": "2026-11-08",
            "manuscript_cited": key in cited,
            "status": "ABSTRACT_READ",
            "passages": "Abstract",
            "files": [],
        }
        if key in EXCLUDED:
            row.update(status="METADATA_ONLY_EXCLUDED", passages=EXCLUDED[key])
            if key in cited:
                raise ValueError(f"Excluded unread candidate is cited: {key}")
        else:
            abstract = cache / (key + ".abstract.txt")
            if not abstract.read_text().partition("\n\n")[2].strip():
                raise ValueError(f"Empty abstract: {key}")
            row["files"].append(checked_copy(abstract, root, previous.get(key, {})))
            if key in FULL_PASSAGES:
                text = cache / (key + ".fulltext.txt")
                row.update(status="ABSTRACT_AND_RELEVANT_FULLTEXT_PASSAGES_READ", passages=FULL_PASSAGES[key])
                row["files"].append(checked_copy(text, root, previous.get(key, {})))
        # Supplemental reading-copy provenance; the metadata receipt remains unchanged.
        pdf_receipt = cache / (key + ".pdf.receipt.json")
        if pdf_receipt.exists():
            row["additional_reading_source"] = json.loads(pdf_receipt.read_text())
        if key == "preuss2022evolution":
            raw = cache / "preuss_route_0.txt"
            row["additional_reading_source"] = {
                "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8617185/",
                "sha256": sha256(raw),
                "note": "Reading text recovered from the earlier successful public HTML response; later routes returned challenge pages",
            }
        readings.append(row)
    out = root / "sources"
    (out / "metadata_receipts.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
    (out / "reading_receipts.json").write_text(json.dumps(readings, ensure_ascii=False, indent=2) + "\n")
    print(root.name, len(readings), "candidate reading decisions exported")


def main():
    cited = set()
    for path in (REPO / "latex").rglob("*.tex"):
        for group in re.findall(r"\\cite(?!gap\b)\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}", path.read_text()):
            cited.update(key.strip() for key in group.split(","))
    for root in sorted((REPO / "experiments").glob("0[123]_*")):
        export(root, cited)


if __name__ == "__main__":
    main()
