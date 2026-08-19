from __future__ import annotations

import unittest
from pathlib import Path


WRITING = Path(__file__).parents[1]


def read(relative: str) -> str:
    return (WRITING / relative).read_text(encoding="utf-8")


class RhetoricalEngineContractTests(unittest.TestCase):
    def test_manifest_loads_rhetorical_engine(self) -> None:
        manifest = read("manifest.yaml")
        self.assertIn("static/core/rhetorical-engine.md", manifest)
        self.assertIn("references/section-move-atlas.md", manifest)
        self.assertIn("references/cross-disciplinary-writing-evidence.md", manifest)

    def test_workflow_uses_nucleus_not_single_function_paragraph_rule(self) -> None:
        workflow = read("static/core/workflow.md")
        self.assertIn("nucleus", workflow)
        self.assertIn("satellites", workflow)
        self.assertNotIn("Each paragraph must do exactly one job", workflow)
        self.assertIn("given", workflow)
        self.assertIn("reader-prediction", workflow)

    def test_introduction_does_not_hide_incrementality(self) -> None:
        intro = read("references/introduction.md")
        self.assertIn("Replication need", intro)
        self.assertIn("New opportunity", intro)
        self.assertIn("Do **not** hide the baseline", intro)
        self.assertNotIn("make the work look like a low-score incremental patch", intro)

    def test_methods_are_not_pipeline_only(self) -> None:
        method = read("references/method.md")
        self.assertIn("rigour and credibility", method.casefold())
        self.assertIn("Clinical / epidemiological", method)
        self.assertIn("Qualitative / social science", method)
        self.assertIn("Computational / algorithmic", method)

    def test_results_and_discussion_are_evidence_driven(self) -> None:
        results = read("static/fragments/section/experiments.md")
        discussion = read("static/fragments/section/discussion.md")
        self.assertIn("evidence dependency graph", results)
        self.assertIn("why the next analysis follows", results)
        self.assertIn("Finding-centered cycle", discussion)
        self.assertIn("alternative explanations", discussion)

    def test_corpus_calibration_forbids_sentence_copying(self) -> None:
        calibration = read("references/target-corpus-calibration.md")
        self.assertIn("8–15 comparable recent papers", calibration)
        self.assertIn("30–100 papers", calibration)
        self.assertIn("Do **not** retain reusable full-sentence templates", calibration)
        self.assertIn("Learn **moves, relations, sequencing, information structure, and claim calibration**, not wording.", calibration)

    def test_evidence_reference_records_large_corpus_basis(self) -> None:
        evidence = read("references/cross-disciplinary-writing-evidence.md")
        for marker in (
            "500 research-article introductions",
            "900 Methods sections across 30 academic fields",
            "5,910 research/conference abstracts",
            "more than 85,000 PLOS research articles",
            "more than one million research articles",
        ):
            self.assertIn(marker, evidence)


if __name__ == "__main__":
    unittest.main()
