from __future__ import annotations

import unittest
from pathlib import Path


PIPELINE = Path(__file__).parents[1]
SKILLS = PIPELINE.parent
SHARED = SKILLS / "nature-shared"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class AcademicPaperPipelineTests(unittest.TestCase):
    def test_pipeline_core_has_full_iteration_lifecycle(self) -> None:
        text = read(SHARED / "core" / "academic-paper-iteration-pipeline.md")
        for marker in (
            "editorial triage simulation",
            "independent reviewer round",
            "editor synthesis + decision letter",
            "targeted re-review",
            "editor closure check",
            "simulated_publication_ready_for_target",
        ):
            self.assertIn(marker, text)

    def test_editor_not_votes_controls_convergence(self) -> None:
        text = read(SHARED / "core" / "academic-paper-iteration-pipeline.md")
        self.assertIn("does **not** count votes", text)
        self.assertIn("must address", text)
        self.assertIn("non-essential", text)

    def test_reviewer_continuity_and_moving_goalposts_are_controlled(self) -> None:
        text = read(SHARED / "core" / "academic-paper-iteration-pipeline.md")
        self.assertIn("Use **reviewer continuity** by default", text)
        self.assertIn("Moving-goalpost protection", text)
        self.assertIn("new_evidence_created_new_issue", text)
        self.assertIn("revision_introduced_regression", text)
        self.assertIn("late optional enrichment", text)

    def test_pipeline_never_invents_new_experiment(self) -> None:
        text = read(SHARED / "core" / "academic-paper-iteration-pipeline.md")
        self.assertIn("Never fabricate the last route", text)
        self.assertIn("blocked_on_author_evidence", text)
        self.assertIn("request_real_new_experiment_or_data_from_author", text)

    def test_unknown_paper_researches_instead_of_forcing_template(self) -> None:
        text = read(SHARED / "core" / "unknown-paper-research-protocol.md")
        self.assertIn("research the publication ecology before inventing a rule", text)
        self.assertIn("8–15 recent comparable papers", text)
        self.assertIn("3–6 closest papers", text)
        self.assertIn("Counterexample search", text)
        self.assertIn("temporary archetype profile", text)

    def test_sentence_logic_contract_is_dependency_first(self) -> None:
        text = read(SHARED / "core" / "sentence-logic-and-cohesion.md")
        for marker in ("inherits X", "relation R", "adds Y", "enables Z"):
            self.assertIn(marker, text)
        self.assertIn("Identity-chain audit", text)
        self.assertIn("Subject-verb distance audit", text)
        self.assertIn("Stress/emphasis audit", text)
        self.assertIn("Analysis-to-analysis handoff", text)
        self.assertIn("A connective labels a relation; it does not create one", text)

    def test_skill_manifest_loads_hardening_contracts(self) -> None:
        manifest = read(PIPELINE / "manifest.yaml")
        for marker in (
            "academic-paper-iteration-pipeline.md",
            "unknown-paper-research-protocol.md",
            "sentence-logic-and-cohesion.md",
            "explanatory-sufficiency.md",
            "atomic-claim-verification.md",
            "manuscript-content-selection.md",
            "figure-evidence-planning.md",
            "manuscript-surface-qa.md",
        ):
            self.assertIn(marker, manifest)

    def test_pipeline_closes_every_atomic_content_item_before_readiness(self) -> None:
        skill = read(PIPELINE / "SKILL.md")
        workflow = read(SHARED / "core" / "academic-paper-iteration-pipeline.md")
        contract = read(SHARED / "core" / "atomic-claim-verification.md")
        self.assertIn("one row per atomic content item", skill)
        self.assertIn("Atomic scientific-content ledger", workflow)
        self.assertIn("independent coverage pass", workflow)
        for marker in ("SUPPORTED_INTERNAL", "UNRESOLVED", "CONTRADICTED", "BLOCKED", "NOT_ASSESSABLE"):
            self.assertIn(marker, skill)
            self.assertIn(marker, workflow)
            self.assertIn(marker, contract)

    def test_skill_is_journal_agnostic(self) -> None:
        skill = read(PIPELINE / "SKILL.md")
        self.assertIn("Nature is only one optional target adapter", skill)
        self.assertIn("The editor, not reviewer vote count, controls convergence", read(PIPELINE / "README_EN.md"))

    def test_pipeline_keeps_science_target_objective_and_certification_separate(self) -> None:
        skill = read(PIPELINE / "SKILL.md")
        manifest = read(PIPELINE / "manifest.yaml")
        state = read(PIPELINE.parents[1] / "docs" / "academic-paper-project-state.template.yaml")
        self.assertIn("venue-decision-contract.md", manifest)
        for marker in (
            "venue_decision_contract",
            "acceptance_objective",
            "scientific_gate_status",
            "target_gate_status",
            "resolution_certification",
            "journal_certification_layer",
            "effective_date_basis",
        ):
            self.assertIn(marker, state)
        self.assertIn("no universal acceptance objective", skill)
        self.assertIn("certification is separate from acceptance", skill)


if __name__ == "__main__":
    unittest.main()
