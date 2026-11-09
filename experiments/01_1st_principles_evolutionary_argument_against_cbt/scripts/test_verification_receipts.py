#!/usr/bin/env python3
"""Offline safety checks for reading-receipt export, not tests of scientific truth."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


exporter = load_module("export_verification_receipts")
checker = load_module("check_revision")


class ReadingReceiptTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.cache = self.root / "_build" / "sources"
        self.cache.mkdir(parents=True)
        (self.root / "sources").mkdir()

    def fixture(self, key="baldwin2007alliance", abstract="Title\nDOI\n\nSynthetic test abstract.\n"):
        crossref = self.cache / (key + ".crossref.json")
        crossref.write_text("{}\n")
        (self.cache / (key + ".abstract.txt")).write_text(abstract)
        record = {"key": key, "doi": "10.example/test", "crossref_sha256": exporter.sha256(crossref)}
        (self.cache / "retrieval_receipts.json").write_text(json.dumps([record]))
        return key

    def export(self, cited=()):
        with contextlib.redirect_stdout(io.StringIO()):
            exporter.export(self.root, set(cited))
        return (self.root / "sources" / "reading_receipts.json").read_bytes()

    def test_unknown_candidate_requires_explicit_decision(self):
        self.fixture(key="unread_candidate")
        with self.assertRaisesRegex(ValueError, "No explicit reading decision"):
            self.export()

    def test_header_only_is_not_a_readable_abstract(self):
        self.fixture(abstract="Title\nDOI\n")
        with self.assertRaisesRegex(ValueError, "Empty abstract"):
            self.export()

    def test_excluded_candidate_cannot_be_cited(self):
        key = self.fixture(key="mahoney1977prejudices")
        with self.assertRaisesRegex(ValueError, "Excluded unread candidate is cited"):
            self.export([key])

    def test_changed_copy_requires_another_reading(self):
        key = self.fixture()
        self.export()
        (self.cache / (key + ".abstract.txt")).write_text("Title\nDOI\n\nChanged synthetic content.\n")
        with self.assertRaisesRegex(ValueError, "Copy changed since recorded reading"):
            self.export()

    def test_unchanged_export_is_reproducible(self):
        key = self.fixture()
        first = self.export([key])
        self.assertEqual(first, self.export([key]))
        self.assertEqual(json.loads(first)[0]["status"], "ABSTRACT_READ")

    def test_truncated_author_list_must_match_a_nonempty_prefix(self):
        source = [{"family": "Pittig"}, {"family": "Heinig"}, {"family": "Goerigk"}]
        self.assertTrue(checker.authors_match("Pittig, Andre and Heinig, Ingmar and others", source))
        self.assertFalse(checker.authors_match("Wrong, Name and others", source))
        self.assertFalse(checker.authors_match("others", source))

    def test_citation_gap_is_not_a_bibliography_key(self):
        tex = r"\citep[see][p. 2]{one,two} \citegap{source needed} \citet*{three}"
        self.assertEqual(checker.citation_keys(tex), {"one", "two", "three"})


if __name__ == "__main__":
    unittest.main()
