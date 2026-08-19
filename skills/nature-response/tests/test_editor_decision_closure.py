from __future__ import annotations

import unittest
from pathlib import Path


RESPONSE = Path(__file__).parents[1]


def read(relative: str) -> str:
    return (RESPONSE / relative).read_text(encoding="utf-8")


class EditorDecisionClosureTests(unittest.TestCase):
    def test_manifest_routes_shared_decision_engine(self) -> None:
        manifest = read("manifest.yaml")
        self.assertIn("editor-reviewer-decision-engine.md", manifest)
        self.assertIn("editor-decision-closure.md", manifest)
        self.assertIn("editorial-decision-profiles.md", manifest)

    def test_closure_routes_are_not_experiment_only(self) -> None:
        closure = read("references/editor-decision-closure.md")
        for marker in (
            "add_decisive_evidence",
            "reanalyse_existing_evidence",
            "clarify_or_restructure",
            "narrow_claim",
            "remove_claim",
            "optional_enrichment",
        ):
            self.assertIn(marker, closure)
        self.assertIn("do unnecessary experiments simply to signal effort", closure)

    def test_editor_instructions_precede_reviewer_preferences(self) -> None:
        closure = read("references/editor-decision-closure.md")
        self.assertIn("explicit editor instructions/decision conditions", closure)
        self.assertIn("optional enrichment/preferences", closure)


if __name__ == "__main__":
    unittest.main()
