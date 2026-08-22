from __future__ import annotations

import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ExplanatorySufficiencyTests(unittest.TestCase):
    def test_shared_manifest_routes_explanatory_sufficiency(self) -> None:
        manifest = read(SHARED / "manifest.yaml")
        self.assertIn("core/explanatory-sufficiency.md", manifest)
        self.assertIn("hidden premises", manifest)

    def test_contract_defines_under_explanation_not_length(self) -> None:
        text = read(SHARED / "core" / "explanatory-sufficiency.md")
        self.assertIn("explanatory underspecification", text)
        self.assertIn("minimum sufficient explanation", text)
        self.assertIn("equate longer prose with better prose", text)
        self.assertIn("Over-explanation guard", text)

    def test_explanation_packet_and_reconstruction_are_explicit(self) -> None:
        text = read(SHARED / "core" / "explanatory-sufficiency.md")
        for marker in (
            "E1 — identity",
            "E2 — purpose",
            "E3 — mechanism or logic",
            "E4 — evidence/observable consequence",
            "E5 — boundary/assumption",
            "E6 — connection",
            "Reader reconstruction test",
            "Hidden-premise / conceptual-jump audit",
        ):
            self.assertIn(marker, text)

    def test_adaptive_elaboration_uses_reader_and_centrality(self) -> None:
        text = read(SHARED / "core" / "explanatory-sufficiency.md")
        self.assertIn("Audience model first", text)
        self.assertIn("importance × unfamiliarity × inferential-dependence", text)
        self.assertIn("High elaboration priority", text)
        self.assertIn("Low priority", text)
        self.assertIn("Do not allocate explanation by word-count quotas", text)

    def test_section_specific_contract_covers_methods_results_and_figures(self) -> None:
        text = read(SHARED / "core" / "explanatory-sufficiency.md")
        for marker in (
            "### Introduction",
            "### Methods",
            "### Results",
            "### Discussion",
            "### Figure callouts and legends",
            "### Equations and formal models",
        ):
            self.assertIn(marker, text)
        self.assertIn("what was done -> how -> why this choice", text)
        self.assertIn("what to notice and why it matters", text)

    def test_writing_workflow_has_explanation_gate_and_ledger(self) -> None:
        manifest = read(SKILLS / "nature-writing" / "manifest.yaml")
        workflow = read(SKILLS / "nature-writing" / "static" / "core" / "workflow.md")
        self.assertIn("explanatory-sufficiency.md", manifest)
        self.assertIn("Explanatory sufficiency gate", workflow)
        self.assertIn("Reader reconstruction test", workflow)
        self.assertIn("explanation ledger", workflow)
        self.assertIn("textbook over-explanation", workflow)

    def test_polishing_and_reviewer_can_diagnose_under_explanation(self) -> None:
        polishing = read(SKILLS / "nature-polishing" / "manifest.yaml")
        reviewer = read(SKILLS / "nature-reviewer" / "manifest.yaml")
        self.assertIn("explanatory-sufficiency.md", polishing)
        self.assertIn("under- and over-explanation", polishing)
        self.assertIn("explanatory-sufficiency.md", reviewer)
        self.assertIn("hidden premises", reviewer)
        self.assertIn("must guess rationale", reviewer)

    def test_citation_and_jargon_do_not_replace_local_explanation(self) -> None:
        text = read(SHARED / "core" / "explanatory-sufficiency.md")
        self.assertIn("Citation as explanation substitute", text)
        self.assertIn("Named method without scientific rationale", text)
        self.assertIn("Figure reference without visual interpretation", text)
        self.assertIn("Equation without semantic interpretation", text)


if __name__ == "__main__":
    unittest.main()
