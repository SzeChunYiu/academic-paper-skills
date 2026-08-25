from __future__ import annotations

import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class PaperArchetypeAtlasTests(unittest.TestCase):
    def test_atlas_covers_major_epistemic_archetypes(self) -> None:
        text = read(SHARED / "core" / "paper-archetype-atlas.md")
        for marker in (
            "Experimental discovery / mechanism paper",
            "Randomized trial / intervention paper",
            "Observational / epidemiological / clinical association paper",
            "Computational / machine-learning empirical paper",
            "Method / tool / software / instrument paper",
            "Dataset / resource / benchmark-resource paper",
            "Theory / proof / mathematical paper",
            "Qualitative / interpretive paper",
            "Review / systematic review / perspective / synthesis paper",
        ):
            self.assertIn(marker, text)

    def test_atlas_rejects_universal_figure_count_and_prestige_imitation(self) -> None:
        text = read(SHARED / "core" / "paper-archetype-atlas.md")
        self.assertIn("There is no universal ideal number of figures", text)
        self.assertIn("prestige paper surface -> imitation", text)
        self.assertIn("Frequency is not quality", text)

    def test_recent_reading_corpus_contains_contrasting_cases(self) -> None:
        text = read(SHARED / "research" / "stratified-paper-reading-2025-2026.md")
        for marker in (
            "Nature Methods, 2026",
            "Nature Cell Biology, 2025",
            "Nature Medicine, 2025",
            "Scientific Data, 2025",
            "PLOS ONE, 2025",
            "JMLR, 2025",
        ):
            self.assertIn(marker, text)
        self.assertIn("may need **no figure**", text)
        self.assertIn("explicit limitation", text)


if __name__ == "__main__":
    unittest.main()
