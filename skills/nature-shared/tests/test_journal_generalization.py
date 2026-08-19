from __future__ import annotations

import unittest
from pathlib import Path


SKILLS = Path(__file__).parents[2]


def read(relative: str) -> str:
    return (SKILLS / relative).read_text(encoding="utf-8")


class JournalGeneralizationContractTests(unittest.TestCase):
    def test_shared_resolver_separates_evidence_and_house_style(self) -> None:
        resolver = read("nature-shared/journal-formats/journal-resolution.md")
        self.assertIn("Evidence selection", resolver)
        self.assertIn("House style", resolver)
        self.assertIn("Submission mechanics", resolver)
        self.assertIn("exact journal -> article/content type -> submission stage -> output component", resolver)

    def test_writing_and_polishing_have_profiled_non_nature_route(self) -> None:
        writing = read("nature-writing/manifest.yaml")
        polishing = read("nature-polishing/manifest.yaml")
        self.assertIn("profiled:", writing)
        self.assertIn("journal-resolution.md", writing)
        self.assertIn("profiled:", polishing)
        self.assertIn("journal-resolution.md", polishing)

    def test_citation_default_is_best_evidence(self) -> None:
        manifest = read("nature-citation/manifest.yaml")
        principles = read("nature-citation/static/core/principles.md")
        self.assertIn("default_scope: best-evidence", manifest)
        self.assertIn("general_script: scripts/academic_citation_search.py", manifest)
        self.assertIn("Default: `best-evidence`", principles)
        self.assertIn("never silently restrict to CNS", principles)

    def test_figure_has_non_nature_journal_adapter(self) -> None:
        manifest = read("nature-figure/manifest.yaml")
        adapter = read("nature-figure/references/journal-adaptation.md")
        self.assertIn("references/journal-adaptation.md", manifest)
        self.assertIn("initial-submission", adapter)
        self.assertIn("production", adapter)
        self.assertIn("Accessibility", adapter)

    def test_reference_verifier_separates_metadata_and_style(self) -> None:
        manifest = read("nature-ref-verifier/manifest.yaml")
        audit = read("nature-ref-verifier/references/journal-style-audit.md")
        self.assertIn("journal-style-audit.md", manifest)
        self.assertIn("Layer 1 — bibliographic identity", audit)
        self.assertIn("Layer 2 — target rendering", audit)

    def test_family_profiles_cover_multiple_publication_ecologies(self) -> None:
        profiles = read("nature-shared/journal-formats/journal-family-profiles.md")
        for marker in (
            "Nature Portfolio",
            "Science / AAAS family",
            "Cell Press",
            "IEEE journals and transactions",
            "ACM journals and proceedings",
            "PLOS journals",
            "Elsevier journals",
            "Wiley journals",
            "Humanities and law journals",
        ):
            self.assertIn(marker, profiles)


if __name__ == "__main__":
    unittest.main()
