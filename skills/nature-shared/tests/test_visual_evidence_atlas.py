from __future__ import annotations

import unittest
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
ROOT = SKILLS.parent
ATLAS = SHARED / "core" / "visual-evidence-atlas.md"
CONTRACT = SHARED / "core" / "scientific-display-decision-contract.md"
RESEARCH = SHARED / "research" / "visual-evidence-atlas-research-2026-08-29.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class VisualEvidenceAtlasTests(unittest.TestCase):
    def test_medium_is_chosen_before_chart_family(self) -> None:
        atlas = read(ATLAS).lower()
        contract = read(CONTRACT).lower()
        for marker in (
            "text vs table vs figure vs mixed display",
            "prefer text when",
            "prefer a table when",
            "prefer a figure when",
            "prefer a mixed display when",
        ):
            self.assertIn(marker, atlas)
        self.assertIn("text vs table vs figure vs mixed display", contract)
        self.assertIn("figure = pattern", contract)
        self.assertIn("table = exactness/detail", contract)

    def test_table_contract_covers_major_scientific_table_roles(self) -> None:
        atlas = read(ATLAS).lower()
        for marker in (
            "baseline / sample-characteristics table",
            "outcome / effect table",
            "regression / model table",
            "benchmark table",
            "qualitative evidence matrix",
            "exhaustive/support table",
            "denominator",
            "missing/not-applicable",
            "uncertainty",
        ):
            self.assertIn(marker, atlas)
        self.assertIn("do not present p-values without the corresponding effect", atlas)

    def test_continuous_paired_and_longitudinal_data_do_not_collapse_to_mean_bars(self) -> None:
        atlas = read(ATLAS).lower()
        self.assertIn("small-n continuous observations", atlas)
        self.assertIn("avoid mean bars that conceal the distribution", atlas)
        self.assertIn("paired / matched change", atlas)
        self.assertIn("preserve pairing", atlas)
        self.assertIn("repeated / longitudinal trajectories", atlas)
        self.assertIn("spaghetti plot", atlas)
        self.assertIn("lasagna", atlas)
        self.assertIn("overplotting", atlas)

    def test_specialist_visual_families_have_inference_boundaries(self) -> None:
        atlas = read(ATLAS).lower()
        required = (
            "meta-analysis / evidence synthesis",
            "funnel plots",
            "survival / time-to-event",
            "classification, probability prediction, calibration, utility",
            "heatmaps and clustered matrices",
            "compositional / relative-abundance data",
            "geospatial / areal data",
            "qualitative / interpretive evidence",
        )
        for marker in required:
            self.assertIn(marker, atlas)
        self.assertIn("do not equate asymmetry with publication bias", atlas)
        self.assertIn("a relative decrease as absolute decrease", atlas)
        self.assertIn("do not use a choropleth of raw case counts", atlas)
        self.assertIn("a dendrogram/heatmap is not proof", atlas)
        self.assertIn("auc alone does not establish calibration", atlas)

    def test_visual_sequence_and_main_support_allocation_are_scientific(self) -> None:
        atlas = read(ATLAS).lower()
        self.assertIn("figure sequence as argument", atlas)
        self.assertIn("what the figure resolves", atlas)
        self.assertIn("main paper vs supplement", atlas)
        self.assertIn("do not hide a result in the supplement merely because it is unfavorable", atlas)
        self.assertNotIn("universal `figure 1 schematic", atlas.replace("do not create a ", ""))

    def test_unknown_visual_problem_triggers_research_not_cargo_cult(self) -> None:
        atlas = read(ATLAS).lower()
        self.assertIn("unknown display fallback", atlas)
        self.assertIn("specialist methods literature", atlas)
        self.assertIn("3–6 genuinely comparable recent papers", atlas)
        self.assertIn("counterexamples", atlas)
        self.assertIn("learn representation logic", atlas)

    def test_research_ledger_records_current_and_specialist_sources(self) -> None:
        research = read(RESEARCH).lower()
        for marker in (
            "icmje",
            "jama network open",
            "plos biology",
            "getting over anova",
            "superplots",
            "cochrane",
            "precision–recall",
            "heatmap",
            "compositional",
            "choropleth",
            "qualitative",
            "color",
        ):
            self.assertIn(marker, research)
        self.assertIn("2026-08-29", research)
        self.assertIn("does not define a universal chart hierarchy", research)

    def test_top_level_writing_pipeline_and_figure_routes_load_atlas(self) -> None:
        files = (
            SKILLS / "academic-writing" / "manifest.yaml",
            SKILLS / "academic-paper-pipeline" / "manifest.yaml",
            SKILLS / "nature-figure" / "manifest.yaml",
        )
        for path in files:
            text = read(path)
            self.assertIn("visual-evidence-atlas.md", text, path)
            self.assertIn("visual-evidence-atlas-research-2026-08-29.md", text, path)

    def test_display_contract_includes_new_high_risk_boundaries(self) -> None:
        contract = read(CONTRACT).lower()
        for marker in (
            "funnel-plot asymmetry alone does not establish publication bias",
            "relative/compositional change does not establish an absolute abundance",
            "raw-count choropleth does not establish geographic risk",
            "clustered heatmap/dendrogram alone does not establish stable or natural clusters",
            "exact primary values must remain recoverable",
        ):
            self.assertIn(marker, contract)


if __name__ == "__main__":
    unittest.main()
