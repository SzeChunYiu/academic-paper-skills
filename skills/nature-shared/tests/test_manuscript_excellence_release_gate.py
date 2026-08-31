from __future__ import annotations

import importlib.util
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
NARRATIVE = SHARED / "core" / "manuscript-narrative-architecture.md"
RHETORIC = SHARED / "core" / "epistemic-rhetoric-and-qualification.md"
PRECISION = SHARED / "core" / "numerical-reporting-precision.md"
EXCELLENCE = SHARED / "core" / "manuscript-excellence-release-gate.md"
SCANNER = SHARED / "scripts" / "audit_narrative_precision.py"
WRITING = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER = SKILLS / "nature-reviewer" / "manifest.yaml"


def _version(text: str) -> tuple[int, ...]:
    for line in text.splitlines():
        if line.startswith("version:"):
            return tuple(int(part) for part in line.split(":", 1)[1].strip().split("."))
    raise AssertionError("manifest version missing")


def _load_scanner():
    spec = importlib.util.spec_from_file_location("audit_narrative_precision", SCANNER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_narrative_contract_enforces_macro_argument_and_reader_activation() -> None:
    text = NARRATIVE.read_text(encoding="utf-8").lower()
    for marker in (
        "build the manuscript argument graph before polishing",
        "section-function contract",
        "functional sufficiency, not word-count sufficiency",
        "problem-formulation / theory-opening gate",
        "reader-state activation law",
        "meaning before use",
        "scientific name before project label",
        "no surprise-entity rule",
        "tables and figures do not get a terminology exemption",
        "results must be a question chain, not a run log",
        "discussion architecture",
        "reverse-outline audit",
        "zero-context reconstruction test",
    ):
        assert marker in text, marker


def test_narrative_contract_catches_surprise_entities_without_word_quota() -> None:
    text = NARRATIVE.read_text(encoding="utf-8").lower()
    assert "a model family suddenly appearing in results" in text
    assert "a dataset first appearing in a table row" in text
    assert "a hypothesis first appearing only when declared passed/failed" in text
    assert "impose universal minimum word counts" in text
    assert "a short section is sufficient when it discharges every downstream dependency" in text


def test_rhetoric_contract_preserves_honesty_without_self_erasure() -> None:
    text = RHETORIC.read_text(encoding="utf-8").lower()
    for marker in (
        "self-erasing rhetoric is not",
        "truthful does not mean maximally cautious",
        "defensive-phrase audit",
        "positive-claim visibility gate",
        "adverse and null results should be scientific, not ceremonial",
        "integrity language is not automatically manuscript language",
        "discussion should be willing to make an argument",
        "rhetorical-economy test",
        "calibrated scientific confidence",
    ):
        assert marker in text, marker
    assert "never use this contract to" in text
    assert "remove a limitation that changes the claim" in text
    assert "hide a failed preregistered primary outcome" in text


def test_precision_contract_rejects_formatter_precision_without_fixed_sigfig_rule() -> None:
    text = PRECISION.read_text(encoding="utf-8").lower()
    for marker in (
        "more digits are not more rigorous",
        "separate stored precision from displayed precision",
        "49/96 (51.0%)",
        "0.510417",
        "do not routinely render a perfect finite-sample score as `1.000000`",
        "significant figures should reflect uncertainty and resolution",
        "do not apply a universal `three significant figures everywhere` rule",
        "cross-surface consistency",
        "software formatter used `%.6f`",
    ):
        assert marker in text, marker


def test_excellence_gate_is_mandatory_before_review_and_release() -> None:
    text = EXCELLENCE.read_text(encoding="utf-8").lower()
    for marker in (
        "mandatory stage integration",
        "whole-paper argument graph",
        "section-function",
        "reader-state activation map",
        "headline result -> interpretation matrix",
        "pre-review excellence qa",
        "e1 — macro logic",
        "e2 — functional section sufficiency",
        "e3 — reader-state activation",
        "e4 — discussion depth",
        "e5 — rhetorical calibration",
        "e6 — numerical precision",
        "e7 — close-analogue plausibility",
        "clean-reader closure",
        "publication-ready terminal extension",
    ):
        assert marker in text, marker
    # The map can evolve from a section-function map into a richer
    # section-function-and-craftsmanship map without breaking the invariant.
    assert "craftsmanship map" in text


def test_scanner_flags_overprecision_defensiveness_and_deferred_reader_activation() -> None:
    scanner = _load_scanner()
    sample = """
# Problem formulation
We define x as the visible state and y as the target.

# Results
D1 reaches 1.000000 on the first arm and 0.510417 on the second. A control was 0.906250.
A second exact arm was 1.000000.
We do not claim universal superiority. This does not establish generality.
The result should not be read as population evidence. The wider question remains undetermined.
This does not authorize a causal conclusion.
"""
    result = scanner.audit(sample)
    by_code = {item["code"]: item for item in result["findings"]}
    assert result["decision"] == "REVIEW"
    assert "excessive_decimal_precision" in by_code
    assert "fixed_width_perfect_metric" in by_code
    assert "defensive_qualification_density" in by_code
    assert "short_setup_section_review" in by_code
    assert result["metrics"]["opaque_ids_first_seen_in_results"] == ["D1"]
    assert "repeated fixed-width" in (by_code["fixed_width_perfect_metric"]["detail"] or "")
    assert "matches" in (by_code["defensive_qualification_density"]["detail"] or "")
    assert "first-in-Results IDs: D1" in (by_code["short_setup_section_review"]["detail"] or "")


def test_scanner_does_not_turn_shortness_into_a_word_count_quota() -> None:
    scanner = _load_scanner()
    sample = """
# Problem formulation
We study whether a representation preserves the information needed for a later decision. The observable state, target action, and comparison rule are defined here before the experiment. The first experiment tests identifiability, and the second asks whether an explicit computation closes the residual.

# Results
The structured representation was correct on 49 of 96 cases (51.0%). The stronger representation reached 83.7%, and the difference motivated the explicit-computation control.

# Discussion
The result separates missing information from missing computation in this finite benchmark. It does not determine whether the same distinction dominates in open-world tasks, where the representation itself must be learned.
"""
    result = scanner.audit(sample)
    assert result["decision"] == "PASS"
    assert result["counts"] == {"error": 0, "review": 0}
    assert result["metrics"]["opaque_ids_first_seen_in_results"] == []


def test_setup_span_includes_child_subsections_before_judging_compactness() -> None:
    scanner = _load_scanner()
    subsection_body = " ".join(["definition"] * 150)
    sample = f"""
# Problem formulation
The main object is introduced here.

## Observable state
{subsection_body}

# Results
D1 reaches 0.75 on the held-out comparison.
"""
    result = scanner.audit(sample)
    codes = {item["code"] for item in result["findings"]}
    assert "short_setup_section_review" not in codes
    assert result["metrics"]["opaque_ids_first_seen_in_results"] == ["D1"]


def test_writing_pipeline_and_reviewer_always_load_excellence_contracts() -> None:
    writing = WRITING.read_text(encoding="utf-8")
    pipeline = PIPELINE.read_text(encoding="utf-8")
    reviewer = REVIEWER.read_text(encoding="utf-8")
    paths = (
        "../nature-shared/core/manuscript-excellence-release-gate.md",
        "../nature-shared/core/manuscript-narrative-architecture.md",
        "../nature-shared/core/epistemic-rhetoric-and-qualification.md",
        "../nature-shared/core/numerical-reporting-precision.md",
    )
    for path in paths:
        assert path in writing
        assert path in pipeline
        assert path in reviewer
    assert "../nature-shared/scripts/audit_narrative_precision.py" in writing
    assert "../nature-shared/scripts/audit_narrative_precision.py" in pipeline
    assert "../nature-shared/scripts/audit_narrative_precision.py" in reviewer
    assert _version(writing) >= (1, 13, 0)
    assert _version(pipeline) >= (1, 15, 0)
    assert _version(reviewer) >= (3, 0, 0)
