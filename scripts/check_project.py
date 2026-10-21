#!/usr/bin/env python3
"""Offline consistency checks for the protocol, source archive and search receipts."""
import csv
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((ROOT / "sources/manifest.json").read_text())
    for name, record in manifest["files"].items():
        path = ROOT / "sources" / name
        assert path.stat().st_size == record["bytes"], name
        assert sha(path) == record["sha256"], name
    queries = json.loads((ROOT / "search/queries.json").read_text())
    protocol = (ROOT / "protocol.md").read_text()
    for query in queries["slices"]:
        assert query["europe_pmc"] in protocol, query["id"]
    metadata = json.loads((ROOT / "data/citation-metadata.json").read_text())
    keys = {r["citation_key"] for r in metadata}
    bib = (ROOT / "references.bib").read_text()
    bibkeys = set(re.findall(r"@\w+\{([^,]+),", bib))
    assert keys == bibkeys
    for record in metadata:
        assert record["doi"] in bib
    cited = set()
    for path in (ROOT / "sections").glob("*.tex"):
        for group in re.findall(r"\\cite\w*\{([^}]+)\}", path.read_text()):
            cited.update(group.split(","))
    assert cited <= keys, cited - keys
    with (ROOT / "data/citation-evidence.csv").open(newline="") as stream:
        evidence = list(csv.DictReader(stream))
    assert cited <= {row["citation_key"] for row in evidence}
    with (ROOT / "data/search-counts.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        run_dir = ROOT / "data/search-runs" / row["run_id"]
        run_receipt = json.loads((run_dir / "receipt.json").read_text())
        assert sha(run_dir / "search_europe_pmc.py") == run_receipt["script_sha256"]
        assert sha(run_dir / "queries.json") == run_receipt["query_manifest_sha256"]
        frozen = json.loads((run_dir / "queries.json").read_text())
        spec = next(q for q in frozen["slices"] if q["id"] == row["slice_id"])
        assert spec["europe_pmc"] == row["query"]
        assert hashlib.sha256(row["query"].encode()).hexdigest() == row["query_sha256"]
        if row["status"] == "ok":
            receipt = ROOT / "data" / row["response_file"]
            assert sha(receipt) == row["response_sha256"]
            data = json.loads(receipt.read_text())
            assert data["request"]["queryString"] == row["query"]
            assert data["hitCount"] == int(row["hit_count"])
        else:
            assert row["hit_count"] == ""
    baseline = [r for r in rows if r["run_id"] == "baseline-10-21-2026"]
    assert len(baseline) == 10
    report = (ROOT / "data/search-report.md").read_text()
    tex = (ROOT / "sections/results.tex").read_text()
    for row in baseline:
        assert f"| {row['slice_id']} | {row['label']} | {row['hit_count']} |" in report
        assert f"{row['slice_id']} & {row['label']} & {row['hit_count']}" in tex
    print(f"Verified {len(manifest['files'])} source hashes, {len(keys)} bibliography records, "
          f"{len(cited)} cited keys and {len(rows)} search receipts; protocol/results agree.")


if __name__ == "__main__":
    main()
