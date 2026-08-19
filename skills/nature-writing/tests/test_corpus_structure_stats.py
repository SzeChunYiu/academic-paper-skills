from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "corpus_structure_stats.py"
SPEC = importlib.util.spec_from_file_location("corpus_structure_stats_under_test", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CorpusStructureStatsTests(unittest.TestCase):
    def test_markdown_sections_are_detected_and_back_matter_excluded(self) -> None:
        text = """# Introduction
We study a difficult problem. However, prior work leaves one question open.

# Methods
We collected data and fit the model.

# Results
The estimate increased by 12%. Therefore, we tested a second condition (Fig. 2).

# Discussion
These results suggest a bounded interpretation.

# References
Reference one.
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "paper.md"
            path.write_text(text, encoding="utf-8")
            result = MODULE.analyze_paper(path)
        self.assertEqual(
            result["section_sequence"],
            ["introduction", "methods", "results", "discussion"],
        )
        self.assertGreater(result["overall"]["words"], 0)
        self.assertEqual(result["overall"]["figure_table_calls"], 1)

    def test_surface_markers_are_descriptive(self) -> None:
        result = MODULE.summarize_text(
            "However, the estimate may vary. Therefore, we tested another sample. "
            "Here we show the bounded result."
        )
        self.assertGreater(result["marker_counts"]["contrast"], 0)
        self.assertGreater(result["marker_counts"]["hedge"], 0)
        self.assertGreater(result["marker_counts"]["cause_consequence"], 0)
        self.assertGreater(result["marker_counts"]["contribution_signal"], 0)

    def test_aggregate_has_no_quality_score(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.md").write_text("# Results\nA result was observed.", encoding="utf-8")
            (root / "b.md").write_text("# Discussion\nThe result may reflect a local effect.", encoding="utf-8")
            payload = MODULE.build_payload(MODULE.iter_files([directory]), include_back_matter=False)
        corpus = payload["corpus"]
        self.assertEqual(corpus["paper_count"], 2)
        self.assertNotIn("quality_score", corpus)
        self.assertTrue(any("not writing-quality scores" in note for note in corpus["notes"]))

    def test_numbered_common_headings_are_normalized(self) -> None:
        sections = MODULE.split_sections(
            "1. Introduction\nContext.\n\n2. Materials and Methods\nProcedure.\n\n3. Conclusions\nAnswer."
        )
        self.assertEqual([name for name, _ in sections], ["introduction", "methods", "conclusion"])


if __name__ == "__main__":
    unittest.main()
