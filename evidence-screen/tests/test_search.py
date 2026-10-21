import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("search", ROOT / "scripts/search_europe_pmc.py")
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)


def response(query, count=0):
    return json.dumps({"hitCount": count, "request": {"queryString": query},
                       "resultList": {"result": []}}).encode()


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / "search/queries.json").read_text())

    def test_zero_is_a_valid_count(self):
        self.assertEqual(search.validate_count(response("q"), "q"), 0)

    def test_bad_responses_do_not_become_zero(self):
        for body in (b"{}", b"not json", b"[]", b'{"error":"invalid query"}',
                     response("q", -1), response("q", True), response("q", "5"),
                     response("other", 5), b'{"hitCount":5}',
                     b'{"hitCount":5,"request":null}',
                     b'{"hitCount":5,"request":{"queryString":"q"},"resultList":null}'):
            with self.subTest(body=body), self.assertRaises(ValueError):
                search.validate_count(body, "q")

    def test_failure_retries_once_preserves_blank_count_and_receipts(self):
        calls = []
        def fetch(url):
            calls.append(url)
            query = parse_qs(urlparse(url).query)["query"][0]
            if query == self.config["slices"][0]["europe_pmc"]:
                raise URLError("offline")
            return response(query, 7)
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()):
            rows = search.run(self.config, temp, "test", fetcher=fetch, pause=lambda _: None)
            self.assertEqual(len(calls), 11)
            self.assertEqual(rows[0]["status"], "error")
            self.assertEqual(rows[0]["hit_count"], "")
            self.assertEqual(rows[0]["attempts"], 2)
            self.assertEqual(rows[1]["hit_count"], 7)
            saved = Path(temp) / rows[1]["response_file"]
            self.assertEqual(search.digest(saved.read_bytes()), rows[1]["response_sha256"])
            with self.assertRaises(FileExistsError):
                search.run(self.config, temp, "test", fetcher=fetch)
            self.assertEqual(len(calls), 11)

    def test_dry_run_makes_no_requests_or_outputs(self):
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()), patch.object(search, "run", side_effect=AssertionError("network run")):
            self.assertEqual(search.main(["--dry-run", "--output", temp]), 0)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_existing_log_schema_and_writer_lock_are_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            (output / "search-counts.csv").write_text("wrong,header\n")
            with self.assertRaises(ValueError):
                search.run(self.config, temp, "test")
            self.assertEqual((output / "search-counts.csv").read_text(), "wrong,header\n")
            (output / ".search-counts.lock").write_text("another-writer")
            with self.assertRaises(FileExistsError):
                search.run(self.config, temp, "test")
            self.assertEqual((output / ".search-counts.lock").read_text(), "another-writer")

    def test_config_and_path_validation(self):
        self.assertEqual(len(search.validate_queries(self.config)["slices"]), 10)
        with self.assertRaises(ValueError):
            search.run(self.config, "/unused", "../escape")
        self.config["slices"][1]["id"] = self.config["slices"][0]["id"]
        with self.assertRaises(ValueError):
            search.validate_queries(self.config)


if __name__ == "__main__":
    unittest.main()
