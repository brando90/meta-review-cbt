#!/usr/bin/env python3
"""Retrieve reproducible Europe PMC match counts; no credentials required."""
import argparse
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
FIELDS = ["run_id", "retrieved_utc", "protocol_version", "as_of", "slice_id",
          "label", "query", "query_sha256", "status", "hit_count", "attempts",
          "response_file", "response_sha256", "request_url", "error"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def validate_count(body, query):
    data = json.loads(body)
    if not isinstance(data, dict) or "error" in data or "errMsg" in data:
        raise ValueError("API returned an error or non-object response")
    count = data.get("hitCount")
    if type(count) is not int or count < 0:
        raise ValueError("Missing or invalid hitCount; not a zero-result search")
    if data.get("request", {}).get("queryString") != query:
        raise ValueError("API did not echo the requested query exactly")
    if not isinstance(data.get("resultList", {}).get("result"), list):
        raise ValueError("Missing result list")
    return count


def request_url(query):
    return ENDPOINT + "?" + urllib.parse.urlencode({
        "query": query, "format": "json", "resultType": "idlist", "pageSize": 1})


def fetch(url):
    request = urllib.request.Request(url, headers={
        "User-Agent": "meta-review-cbt/0.1 (research search counts)",
        "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def validate_queries(config):
    dt.date.fromisoformat(config["as_of"])
    if not config.get("protocol_version"):
        raise ValueError("Missing protocol version")
    queries = config["slices"]
    ids = [q["id"] for q in queries]
    if len(queries) != 10 or len(set(ids)) != 10:
        raise ValueError("Expected ten distinct search slices")
    for query in queries:
        if not re.fullmatch(r"S[0-9]{2}", query["id"]):
            raise ValueError("Unsafe slice identifier")
        for field in ("label", "europe_pmc", "pubmed", "psycinfo_ovid"):
            if not isinstance(query.get(field), str) or not query[field].strip():
                raise ValueError("Missing query field: " + field)
    return config


def run(config, output, label, fetcher=fetch, pause=time.sleep):
    validate_queries(config)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}", label):
        raise ValueError("Run label must be a safe, unique filename")
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    # One writer: retain the lock after a crash for explicit inspection/recovery.
    lock = output / ".search-counts.lock"
    with lock.open("x") as stream:
        stream.write(label + "\n")
    try:
        log = output / "search-counts.csv"
        if log.exists():
            with log.open(newline="") as stream:
                if next(csv.reader(stream), None) != FIELDS:
                    raise ValueError("Existing CSV schema differs; preserve it")
        folder = output / "search-runs" / label
        folder.mkdir(parents=True, exist_ok=False)
        (folder / "queries.json").write_text(json.dumps(config, indent=2) + "\n")
        rows = []
        for spec in config["slices"]:
            query = spec["europe_pmc"]
            url = request_url(query)
            row = dict.fromkeys(FIELDS, "")
            row.update(run_id=label, protocol_version=config["protocol_version"],
                       as_of=config["as_of"], slice_id=spec["id"], label=spec["label"],
                       query=query, query_sha256=digest(query.encode()), request_url=url)
            for attempt in (1, 2):
                row.update(attempts=attempt, retrieved_utc=dt.datetime.now(dt.timezone.utc).isoformat())
                try:
                    body = fetcher(url)
                    receipt = folder / (spec["id"] + f"-attempt-{attempt}.json")
                    receipt.write_bytes(body)
                    row.update(response_file=str(receipt.relative_to(output)), response_sha256=digest(body))
                    row.update(hit_count=validate_count(body, query), status="ok", error="")
                    break
                except (urllib.error.URLError, TimeoutError, ValueError) as error:
                    row.update(status="error", hit_count="", error=str(error))
                    if attempt == 1:
                        pause(2)
            new_file = not log.exists()
            with log.open("a", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                if new_file:
                    writer.writeheader()
                writer.writerow(row)
                stream.flush()
            rows.append(row)
            print(f"{row['slice_id']} {row['status']}: {row['hit_count'] if row['status'] == 'ok' else row['error']}", flush=True)
            pause(0.35)
        (folder / "receipt.json").write_text(json.dumps({
            "run_id": label, "endpoint": ENDPOINT,
            "script_sha256": digest(Path(__file__).read_bytes()),
            "query_manifest_sha256": digest((folder / "queries.json").read_bytes()),
            "successful_slices": sum(r["status"] == "ok" for r in rows),
            "total_slices": len(rows), "counts_are_eligible_studies": False,
        }, indent=2) + "\n")
        return rows
    finally:
        lock.unlink()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queries", type=Path, default=ROOT / "search/queries.json")
    parser.add_argument("--output", type=Path, default=ROOT / "data")
    parser.add_argument("--run-label", default=dt.datetime.now(dt.timezone.utc).strftime("search-%Y%m%dT%H%M%S%fZ"))
    parser.add_argument("--dry-run", action="store_true", help="Print all queries; no requests or file writes")
    args = parser.parse_args(argv)
    config = validate_queries(json.loads(args.queries.read_text()))
    if args.dry_run:
        for spec in config["slices"]:
            print(spec["id"] + " " + spec["label"] + "\n" + request_url(spec["europe_pmc"]))
        return 0
    rows = run(config, args.output, args.run_label)
    return 0 if all(row["status"] == "ok" for row in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
