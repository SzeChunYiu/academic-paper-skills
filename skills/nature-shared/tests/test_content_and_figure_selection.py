from __future__ import annotations

import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ContentAndFigureSelectionTests(unittest.TestCase):
    def test_shared_manifest_routes_content_and_figure_planning(self) -> None:
        manifest = read(SHARED / "manifest.yaml")
        self.assertIn("core/manuscript-content-selection.md", manifest)
        self.assertIn("core/figure-evidence-planning.md", manifest)

    def test_repository_leakage_is_explicitly_blocked(self) -> None:
        text = read(SHARED / "core" / "manuscript-content-selection.md")
        self.assertIn("implementation-detail leakage", text)
        self.assertIn("repository-to-manuscript leakage", text)
        self.assertIn("If the implementation were rewritten from scratch", text)
        for marker in (
            "file paths",
            "script filenames",
            "helper-function/class names",
            "branch, PR, issue",
            "installation steps",
        ):
            self.assertIn(marker, text)

    def test_content_admission_has_scientific_functions_and_destinations(self) -> None:
        text = read(SHARED / "core" / "manuscript-content-selection.md")
        for marker in (
            "F1 — inference-critical",
            "F2 — interpretation-critical",
            "F3 — reproducibility-critical",
            "F4 — compliance/provenance-critical",
            "F5 — orientation-critical",
            "Data / Code / Resource Availability",
            "Repository / artifact documentation",
            "Omit",
        ):
            self.assertIn(marker, text)

    def test_content_selection_is_contribution_type_aware(self) -> None:
        text = read(SHARED / "core" / "manuscript-content-selection.md")
        for marker in (
            "Experimental discovery / mechanism",
            "Clinical / epidemiological / observational",
            "Computational / machine learning",
            "Method / instrument / tool",
            "Dataset / resource / benchmark",
            "Theory / mathematical",
            "Qualitative / interpretive / humanities",
        ):
            self.assertIn(marker, text)

    def test_main_text_discipline_has_artifact_and_plot_ledgers(self) -> None:
        text = read(SHARED / "core" / "main-text-discipline.md")
        self.assertIn("artifact_operation", text)
        self.assertIn("Repository-leakage list", text)
        self.assertIn("Figure/plot suggestion ledger", text)
        self.assertIn("one-stop shop", text)

    def test_figure_planning_is_claim_and_estimand_driven(self) -> None:
        text = read(SHARED / "core" / "figure-evidence-planning.md")
        self.assertIn("claim -> reader question -> evidence/estimand", text)
        self.assertIn("Figure necessity test", text)
        self.assertIn("Scientific unit", text)
        self.assertIn("Alternative explanation", text)
        self.assertIn("Can prose/table do this better?", text)

    def test_plot_atlas_covers_decision_relevant_families(self) -> None:
        text = read(SHARED / "core" / "figure-evidence-planning.md")
        for marker in (
            "Paired/matched change",
            "Calibration / probabilistic prediction",
            "Survival / time-to-event",
            "Heterogeneity / subgroup effects",
            "Many methods / benchmarks",
            "Ablation / component contribution",
            "Imaging / microscopy / morphology",
            "Null / negative result",
        ):
            self.assertIn(marker, text)

    def test_plot_choice_is_not_top_journal_cargo_cult(self) -> None:
        text = read(SHARED / "core" / "figure-evidence-planning.md")
        self.assertIn("top paper used plot X", text)
        self.assertIn("comparable papers often contain it", text)
        figure_contract = read(SKILLS / "nature-figure" / "static" / "core" / "contract.md")
        self.assertIn("A chart's popularity in analogue papers is never sufficient justification", figure_contract)

    def test_writing_routes_content_and_plot_planning(self) -> None:
        manifest = read(SKILLS / "nature-writing" / "manifest.yaml")
        workflow = read(SKILLS / "nature-writing" / "static" / "core" / "workflow.md")
        self.assertIn("manuscript-content-selection.md", manifest)
        self.assertIn("figure-evidence-planning.md", manifest)
        self.assertIn("Repository-to-manuscript leakage gate", workflow)
        self.assertIn("figure/plot suggestion ledger", workflow)

    def test_figure_skill_routes_planning_without_rendering_gate(self) -> None:
        manifest = read(SKILLS / "nature-figure" / "manifest.yaml")
        contract = read(SKILLS / "nature-figure" / "static" / "core" / "contract.md")
        self.assertIn("figure-evidence-planning.md", manifest)
        self.assertIn("manuscript-content-selection.md", manifest)
        self.assertIn("Planning-only exception", contract)
        self.assertIn("deciding which figures/plots the paper needs does not require selecting Python/R", contract)

    def test_reviewer_can_audit_content_and_figure_adequacy(self) -> None:
        manifest = read(SKILLS / "nature-reviewer" / "manifest.yaml")
        self.assertIn("manuscript-content-selection.md", manifest)
        self.assertIn("figure-evidence-planning.md", manifest)
        self.assertIn("not publication policy", manifest)


if __name__ == "__main__":
    unittest.main()
