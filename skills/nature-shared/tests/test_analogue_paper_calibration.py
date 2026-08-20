from __future__ import annotations

import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class AnaloguePaperCalibrationTests(unittest.TestCase):
    def test_shared_manifest_routes_analogue_and_voice(self) -> None:
        manifest = read(SHARED / "manifest.yaml")
        self.assertIn("core/analogue-paper-calibration.md", manifest)
        self.assertIn("core/author-voice-profile.md", manifest)

    def test_analogue_contract_learns_structure_not_surface(self) -> None:
        text = read(SHARED / "core" / "analogue-paper-calibration.md")
        self.assertIn("3–6 very close analogues", text)
        self.assertIn("scientific necessity", text)
        self.assertIn("field convention", text)
        self.assertIn("author choice", text)
        self.assertIn("what the figure proves", text)
        self.assertIn("Learn **functions, relations, evidence architecture, and visual grammar**, not expressive surface.", text)
        self.assertIn("Survivorship bias", text)

    def test_author_voice_is_separate_from_analogue_style(self) -> None:
        text = read(SHARED / "core" / "author-voice-profile.md")
        self.assertIn("Voice invariants", text)
        self.assertIn("Flexible traits", text)
        self.assertIn("analogue papers = structural priors", text)
        self.assertIn("author voice = expression prior", text)
        self.assertIn("generic academic prose", text)

    def test_writing_router_runs_analogue_and_revoice_pass(self) -> None:
        router = read(SKILLS / "nature-writing" / "SKILL.md")
        manifest = read(SKILLS / "nature-writing" / "manifest.yaml")
        self.assertIn("Analogue-paper study + author voice", router)
        self.assertIn("re-voice pass", router)
        self.assertIn("figure/data choices", manifest)
        self.assertIn("author-voice-profile.md", manifest)

    def test_polishing_router_preserves_voice_and_skips_layout_only(self) -> None:
        router = read(SKILLS / "nature-polishing" / "SKILL.md")
        manifest = read(SKILLS / "nature-polishing" / "manifest.yaml")
        self.assertIn("analogue papers = structural/evidence priors", router)
        self.assertIn("author voice = expression prior", router)
        self.assertIn("Do not run prose rewriting, analogue-style calibration, or author-voice rewriting for a placement-only request.", router)
        self.assertIn("core/author-voice-profile.md", manifest)

    def test_figure_router_learns_figure_roles_not_visual_identity(self) -> None:
        router = read(SKILLS / "nature-figure" / "SKILL.md")
        manifest = read(SKILLS / "nature-figure" / "manifest.yaml")
        reference = read(SKILLS / "nature-figure" / "references" / "analogue-figure-calibration.md")
        contract = read(SKILLS / "nature-figure" / "static" / "core" / "contract.md")
        self.assertIn("Run an analogue-paper visual calibration", router)
        self.assertIn("analogue-figure-calibration.md", manifest)
        self.assertIn("Learn figure roles before chart types", reference)
        self.assertIn("Project visual identity to preserve", reference)
        self.assertIn("use a chart because it is popular in the target journal", reference)
        self.assertIn("../../../nature-shared/core/analogue-paper-calibration.md", contract)
        self.assertTrue((SHARED / "core" / "analogue-paper-calibration.md").exists())
        self.assertTrue((SKILLS / "nature-figure" / "references" / "analogue-figure-calibration.md").exists())


if __name__ == "__main__":
    unittest.main()
