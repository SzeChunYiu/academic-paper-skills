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

    def test_sentence_logic_and_content_richness_are_explicit(self) -> None:
        skill = read(SKILL / "SKILL.md")
        for marker in ("inherits X", "relation R", "adds Y", "enables Z"):
            self.assertIn(marker, skill)
        self.assertIn("scientifically sufficient, not verbose", skill)
        self.assertIn("minimum sufficient scientific explanation", skill.lower())

    def test_legacy_nature_writing_is_explicitly_support_only(self) -> None:
        agent = read(LEGACY / "agents" / "openai.yaml")
        self.assertIn("allow_implicit_invocation: false", agent)
        self.assertIn("use academic-writing", agent.lower())

    def test_pipeline_is_recommended_for_closed_loop_work(self) -> None:
        skill = read(SKILL / "SKILL.md")
        readme = read(SKILL / "README_EN.md")
        self.assertIn("$academic-paper-pipeline", skill)
        self.assertIn("academic-paper-pipeline", readme)


if __name__ == "__main__":
    unittest.main()
