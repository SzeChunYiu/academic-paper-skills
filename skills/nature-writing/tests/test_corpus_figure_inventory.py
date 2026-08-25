from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "corpus_figure_inventory.py"
spec = importlib.util.spec_from_file_location("corpus_figure_inventory", SCRIPT)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class CorpusFigureInventoryTests(unittest.TestCase):
    def test_extracts_caption_and_candidate_roles(self) -> None:
        text = """# Results
Figure 1 | Overview of the benchmark workflow and datasets.
Figure 2. Out-of-distribution generalization across unseen cell contexts.
Figure 3: Limitations of current methods under sparse perturbations.
Table 1 | Participant characteristics.
"""
        path = Path("paper.md")
        records = mod.extract_displays(path, text)
        self.assertEqual(len(records), 4)
        roles = {(r.kind, r.number): set(r.candidate_roles) for r in records}
        self.assertIn("orientation_workflow", roles[("figure", "1")])
        self.assertIn("generalization_ood", roles[("figure", "2")])
        self.assertIn("failure_limitation", roles[("figure", "3")])
        self.assertEqual(records[3].kind, "table")

    def test_aggregate_has_explicit_non_scoring_warning(self) -> None:
        summary = mod.DocumentSummary("x.md", 1, 0, 1, 0, 1, 0, {"unclassified": 1})
        display = mod.DisplayRecord("x.md", "figure", "1", "Result", "Results", ("unclassified",))
        aggregate = mod.aggregate([summary], [display])
        warning = aggregate["methodological_warning"]
        self.assertIn("keyword heuristics", warning)
        self.assertIn("not semantic ground truth", warning)
        self.assertIn("writing-quality scores", warning)
        self.assertIn("acceptance predictors", warning)
        self.assertIn("instructions to copy frequent plot types", warning)

    def test_iter_paths_recurses_only_text_like_files(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "a.md").write_text("Figure 1. A", encoding="utf-8")
            (root / "b.txt").write_text("Figure 1. B", encoding="utf-8")
            (root / "c.pdf").write_bytes(b"pdf")
            paths = mod.iter_paths([root])
            self.assertEqual({p.suffix for p in paths}, {".md", ".txt"})

    def test_qualitative_caption_is_not_forced_into_quantitative_role(self) -> None:
        roles = mod.classify_roles("Themes generated from participant interviews")
        self.assertIn("qualitative_synthesis", roles)
        self.assertNotIn("primary_effect_finding", roles)

    def test_display_calls_are_counted_descriptively(self) -> None:
        text = "As shown in Fig. 1 and Figure 2, results differ. Table 1 summarizes the cohort."
        summary = mod.summarize_document(Path("paper.md"), text, [])
        self.assertEqual(summary.figure_call_count, 2)
        self.assertEqual(summary.table_call_count, 1)
        self.assertEqual(summary.unique_figure_calls, 2)


if __name__ == "__main__":
    unittest.main()
