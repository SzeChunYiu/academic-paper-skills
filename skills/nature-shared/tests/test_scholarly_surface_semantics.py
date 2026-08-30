from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
SCRIPT = SHARED / "scripts" / "audit_scholarly_surface_semantics.py"
CONTRACT = SHARED / "core" / "scholarly-surface-semantics.md"
WRITING_MANIFEST = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE_MANIFEST = SKILLS / "academic-paper-pipeline" / "manifest.yaml"

spec = importlib.util.spec_from_file_location("audit_scholarly_surface_semantics", SCRIPT)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


def kinds(text: str) -> set[str]:
    return {f.kind for f in mod.audit_text(text)}


def test_flags_chat_style_bold_and_monospace_semantic_leakage() -> None:
    text = r"""## Results
The result is **not** a universal guarantee.
Under \texttt{ANY_OPTIMAL_ACTION} semantics the rule is deterministic.
"""
    found = kinds(text)
    assert "inline_bold_review" in found
    assert "monospace_semantics_review" in found
    assert "internal_enum_token_review" in found


def test_flags_backticks_and_internal_ci_status_vocabulary() -> None:
    text = "The `CURRENT_STATE_OK` case is PASS, whereas the bounded search is CANNOT CHECK."
    found = kinds(text)
    assert "inline_code_semantics_review" in found
    assert "internal_enum_token_review" in found
    assert "internal_status_vocabulary_review" in found


def test_flags_raw_math_source_tokens_outside_math_mode() -> None:
    found = kinds("The premium C_dyn^* is compared with C_stat in the next section.")
    assert "raw_math_token" in found


def test_proper_math_mode_is_not_raw_math_leakage() -> None:
    found = kinds(r"The premium $C_{\mathrm{dyn}}^*-C_{\mathrm{stat}}^*$ is one bit.")
    assert "raw_math_token" not in found


def test_flags_dashboard_like_all_caps_labels() -> None:
    found = kinds("PRESENT-EQUIVALENCE GATE -> COMMON LATER EVIDENCE -> SCORE UPDATE")
    assert "all_caps_workflow_label_review" in found


def test_latex_table_without_caption_is_release_error() -> None:
    findings = mod.audit_text(r"""\begin{table}
\begin{tabular}{ll}
A & B \\
\end{tabular}
\end{table}
""")
    matches = [f for f in findings if f.kind == "latex_table_missing_caption"]
    assert len(matches) == 1
    assert matches[0].severity == "error"


def test_table_number_gaps_and_duplicates_are_detected() -> None:
    gap = kinds("Table 1: First\nTable 3: Third\n")
    duplicate = kinds("Table 1: First\nTable 1: Again\n")
    assert "table_number_gap" in gap
    assert "duplicate_table_number" in duplicate


def test_overfull_renderer_log_is_reviewed() -> None:
    found = kinds(r"Overfull \hbox (12.0pt too wide) in paragraph at lines 10--12")
    assert "overfull_box" in found


def test_normal_scholarly_prose_has_no_new_surface_findings() -> None:
    text = (
        "The current decision is unique. After the same later evidence, "
        "the two histories require different admissible actions."
    )
    assert not mod.audit_text(text)


def test_contract_covers_semantic_and_formal_failure_classes() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "manuscript semantics are not authoring, markdown, code, ci, or build semantics",
        "emphasis is a rhetorical decision",
        "code and monospace typography",
        "named scientific objects require explicit definitions",
        "derived quantities need type-compatible operands",
        "internal audit states must be translated",
        "registration language",
        "rendered-artifact correctness",
        "title, scope, and mathematical machinery must agree",
        "contribution mass and article-type fit",
        "novelty and search-frontier statements are time-bounded",
        "three-layer release audit",
    ):
        assert marker in text, marker


def test_writing_and_pipeline_route_semantics_gate_and_scanner() -> None:
    writing = WRITING_MANIFEST.read_text(encoding="utf-8")
    pipeline = PIPELINE_MANIFEST.read_text(encoding="utf-8")
    assert "../nature-shared/core/scholarly-surface-semantics.md" in writing
    assert "../nature-shared/core/scholarly-surface-semantics.md" in pipeline
    assert "../nature-shared/scripts/audit_scholarly_surface_semantics.py" in writing
    assert "../nature-shared/scripts/audit_scholarly_surface_semantics.py" in pipeline
