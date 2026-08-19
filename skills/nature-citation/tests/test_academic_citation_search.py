from __future__ import annotations

import argparse
import importlib.util
import sys
import unittest
from pathlib import Path
from unittest import mock


SCRIPTS = Path(__file__).parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

SCRIPT = SCRIPTS / "academic_citation_search.py"
SPEC = importlib.util.spec_from_file_location("academic_citation_search_under_test", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def crossref_item(journal: str, doi: str, score: float = 10.0) -> dict[str, object]:
    return {
        "title": [f"Evidence from {journal}"],
        "container-title": [journal],
        "published": {"date-parts": [[2025, 1, 2]]},
        "DOI": doi,
        "URL": f"https://doi.org/{doi}",
        "author": [{"family": "Smith", "given": "Alex"}],
        "type": "journal-article",
        "score": score,
    }


def args(**overrides: object) -> argparse.Namespace:
    values: dict[str, object] = {
        "scope": "best-evidence",
        "journal": [],
        "rows": 30,
        "mailto": None,
        "from_year": None,
        "to_year": None,
        "max_retries": 0,
        "per_query": 8,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class AcademicCitationSearchTests(unittest.TestCase):
    def test_default_scope_is_best_evidence(self) -> None:
        parser = MODULE.parser()
        parsed = parser.parse_args(["--query", "test query"])
        self.assertEqual(parsed.scope, "best-evidence")

    def test_best_evidence_does_not_filter_non_cns_journal(self) -> None:
        items = [crossref_item("Journal of Field-Specific Evidence", "10.1000/field")]
        with mock.patch.object(MODULE.legacy, "fetch_crossref", return_value=items):
            results, errors = MODULE.search_query("specific evidence", args())
        self.assertEqual(errors, [])
        self.assertEqual([item.journal for item in results], ["Journal of Field-Specific Evidence"])

    def test_explicit_cns_scope_still_filters(self) -> None:
        items = [
            crossref_item("Journal of Field-Specific Evidence", "10.1000/field", score=30),
            crossref_item("Nature Medicine", "10.1000/nature", score=20),
        ]
        with mock.patch.object(MODULE.legacy, "fetch_crossref", return_value=items):
            results, errors = MODULE.search_query("specific evidence", args(scope="cns"))
        self.assertEqual(errors, [])
        self.assertEqual([item.journal for item in results], ["Nature Medicine"])

    def test_target_journal_filter_is_explicit_and_independent(self) -> None:
        items = [
            crossref_item("IEEE Transactions on Pattern Analysis and Machine Intelligence", "10.1000/ieee"),
            crossref_item("Pattern Recognition", "10.1000/pr"),
        ]
        with mock.patch.object(MODULE.legacy, "fetch_crossref", return_value=items):
            results, _ = MODULE.search_query("vision model", args(journal=["Pattern Recognition"]))
        self.assertEqual([item.journal for item in results], ["Pattern Recognition"])

    def test_metadata_rank_is_not_journal_prestige_rank(self) -> None:
        field = MODULE.legacy.candidate_from_crossref(
            crossref_item("Journal of Field-Specific Evidence", "10.1000/field", score=40),
            "query",
        )
        nature = MODULE.legacy.candidate_from_crossref(
            crossref_item("Nature", "10.1000/nature", score=10),
            "query",
        )
        assert field and nature
        ranked = sorted([nature, field], key=MODULE.candidate_rank, reverse=True)
        self.assertEqual(ranked[0].journal, "Journal of Field-Specific Evidence")


if __name__ == "__main__":
    unittest.main()
