from __future__ import annotations

import unittest
from pathlib import Path


SKILL = Path(__file__).parents[1]
SKILLS = SKILL.parent
LEGACY = SKILLS / "nature-writing"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class AcademicWritingCanonicalTests(unittest.TestCase):
    def test_canonical_name_is_academic_writing(self) -> None:
        skill = read(SKILL / "SKILL.md")
        manifest = read(SKILL / "manifest.yaml")
        agent = read(SKILL / "agents" / "openai.yaml")
        self.assertIn("name: academic-writing", skill)
        self.assertIn("name: academic-writing", manifest)
        self.assertIn("$academic-writing", agent)
        self.assertIn("Nature is not the default", skill)

    def test_core_writing_hardening_is_always_loaded(self) -> None:
        manifest = read(SKILL / "manifest.yaml")
        for marker in (
            "paper-archetype-atlas.md",
            "sentence-logic-and-cohesion.md",
            "explanatory-sufficiency.md",
            "atomic-claim-verification.md",
            "manuscript-content-selection.md",
            "figure-evidence-planning.md",
            "manuscript-surface-qa.md",
        ):
            self.assertIn(marker, manifest)

    def test_unknown_paper_research_is_routed(self) -> None:
        manifest = read(SKILL / "manifest.yaml")
        skill = read(SKILL / "SKILL.md")
        self.assertIn("unknown-paper-research-protocol.md", manifest)
        self.assertIn("Self-research when uncertain", skill)
        self.assertIn("counterexamples", skill)

    def test_readiness_is_fail_closed_on_atomic_content(self) -> None:
        manifest = read(SKILL / "manifest.yaml")
        skill = read(SKILL / "SKILL.md")
        contract = read(SKILLS / "nature-shared" / "core" / "atomic-claim-verification.md")
        self.assertIn("atomic-claim-verification.md", manifest)
        for marker in ("SUPPORTED_INTERNAL", "UNRESOLVED", "CONTRADICTED", "BLOCKED", "NOT_ASSESSABLE"):
            self.assertIn(marker, skill)
            self.assertIn(marker, contract)

    def test_sentence_logic_and_content_richness_are_explicit(self) -> None:
        skill = read(SKILL / "SKILL.md")
        for marker in ("inherits X", "relation R", "adds Y", "enables Z"):
            self.assertIn(marker, skill)
        self.assertIn("scientifically sufficient, not verbose", skill)
        self.assertIn("Do not delete reasoning merely to make prose short", skill)
        self.assertIn("Do not add textbook filler merely to make prose long", skill)

    def test_legacy_nature_writing_is_explicitly_support_only(self) -> None:
        agent = read(LEGACY / "agents" / "openai.yaml")
        self.assertIn("allow_implicit_invocation: false", agent)
        self.assertIn("use academic-writing", agent.lower())

    def test_pipeline_is_recommended_for_closed_loop_work(self) -> None:
        skill = read(SKILL / "SKILL.md")
        readme = read(SKILL / "README_EN.md")
        self.assertIn("$academic-paper-pipeline", skill)
        self.assertIn("academic-paper-pipeline", readme)

    def test_exact_venue_decision_contract_is_routed_by_tuple_and_date(self) -> None:
        skill = read(SKILL / "SKILL.md")
        manifest = read(SKILL / "manifest.yaml")
        self.assertIn("venue-decision-contract.md", manifest)
        self.assertIn("exact venue × article type × stage × effective date", skill)
        self.assertIn("live official-source resolution", skill)
        self.assertIn("fallback profile is not exact journal policy", skill)

    def test_scientific_display_contract_is_canonical_not_cosmetic(self) -> None:
        skill = read(SKILL / "SKILL.md")
        manifest = read(SKILL / "manifest.yaml")
        self.assertIn("scientific-display-decision-contract.md", manifest)
        self.assertIn("scientific display decision contract", skill.lower())
        self.assertIn("reader question -> scientific object / estimand", skill)
        self.assertIn("no universal best chart", skill.lower())
        self.assertIn("data snapshot -> analysis receipt -> render receipt", skill)

    def test_study_protocol_and_conduct_precede_manuscript_projection(self) -> None:
        skill = read(SKILL / "SKILL.md")
        manifest = read(SKILL / "manifest.yaml")
        readme = read(SKILL / "README_EN.md")
        self.assertIn("study-protocol-conduct-contract.md", manifest)
        self.assertIn("protocol version -> analysis-plan version", skill)
        self.assertIn("conduct receipt -> deviation ledger", skill)
        self.assertIn("Methods prose is a projection", skill)
        self.assertIn("not a scientific-validity certificate", readme)


if __name__ == "__main__":
    unittest.main()
