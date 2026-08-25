from __future__ import annotations

import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class SurfaceArchetypeIntegrationTests(unittest.TestCase):
    def test_shared_manifest_routes_archetype_and_surface_qa(self) -> None:
        manifest = read(SHARED / "manifest.yaml")
        self.assertIn("core/paper-archetype-atlas.md", manifest)
        self.assertIn("core/manuscript-surface-qa.md", manifest)
        self.assertIn("scripts/audit_manuscript_surface.py", manifest)

    def test_writing_always_loads_surface_qa(self) -> None:
        manifest = read(SKILLS / "nature-writing" / "manifest.yaml")
        output = read(SKILLS / "nature-writing" / "static" / "core" / "output-format.md")
        self.assertIn("../nature-shared/core/manuscript-surface-qa.md", manifest)
        self.assertIn("Final release gate before returning manuscript prose", output)
        self.assertIn("manuscript prose must name the science", output)
        self.assertIn("audit_manuscript_surface.py", output)

    def test_polishing_always_loads_surface_qa(self) -> None:
        manifest = read(SKILLS / "nature-polishing" / "manifest.yaml")
        self.assertIn("../nature-shared/core/manuscript-surface-qa.md", manifest)
        self.assertIn("paper-archetype-atlas.md", manifest)

    def test_reviewer_can_distinguish_surface_from_science(self) -> None:
        manifest = read(SKILLS / "nature-reviewer" / "manifest.yaml")
        self.assertIn("paper-archetype-atlas.md", manifest)
        self.assertIn("manuscript-surface-qa.md", manifest)
        self.assertIn("ordinary copy-editing as clarity/reporting unless it changes meaning", manifest)

    def test_figure_contract_has_hard_surface_gate(self) -> None:
        contract = read(SKILLS / "nature-figure" / "static" / "core" / "contract.md")
        manifest = read(SKILLS / "nature-figure" / "manifest.yaml")
        self.assertIn("Paper-archetype calibration gate", contract)
        self.assertIn("Legend/caption and manuscript-surface gate", contract)
        self.assertIn("paper-archetype-atlas.md", manifest)
        self.assertIn("manuscript-surface-qa.md", manifest)

    def test_legend_contract_is_not_a_fixed_natcomms_skeleton(self) -> None:
        legend = read(SKILLS / "nature-figure" / "references" / "figure-legend-conventions.md")
        self.assertNotIn("Legend structure — the fixed skeleton", legend)
        self.assertIn("Do not infer a universal caption skeleton", legend)
        self.assertIn("Local Nature Communications CS/AI observational profile", legend)
        self.assertIn("plot script names", legend)
        self.assertIn("output image filenames", legend)
        self.assertIn("Punctuation and typography", legend)


if __name__ == "__main__":
    unittest.main()
