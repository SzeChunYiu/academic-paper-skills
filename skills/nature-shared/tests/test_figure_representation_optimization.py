from __future__ import annotations

import importlib.util
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "figure-purpose-representation-optimization.md"
RESEARCH = SHARED / "research" / "figure-purpose-representation-evidence-2026-09-01.md"
SCHEMA = SHARED / "display-contracts" / "figure-representation-decision.schema.json"
VERIFIER = SHARED / "scripts" / "verify_figure_representation_decision.py"
WRITING = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER = SKILLS / "nature-reviewer" / "manifest.yaml"
FIGURE = SKILLS / "nature-figure" / "manifest.yaml"


def _load_verifier():
    spec = importlib.util.spec_from_file_location("verify_figure_representation_decision", VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _version(text: str) -> tuple[int, ...]:
    for line in text.splitlines():
        if line.startswith("version:"):
            return tuple(int(part) for part in line.split(":", 1)[1].strip().split("."))
    raise AssertionError("manifest version missing")


def _candidate(family: str, decision: str) -> dict:
    return {
        "family": family,
        "reader_task_fit": "supports direct comparison of paired task-level differences",
        "information_preserved": ["task-level variation", "direction of paired differences"],
        "information_hidden": ["exact lookup requires companion table"],
        "perceptual_task": "position on a common scale",
        "dependence_visibility": "pairing is explicit",
        "uncertainty_visibility": "intervals shown for the claim-bearing contrast",
        "heterogeneity_failure_visibility": "task failures remain visible",
        "exact_value_recovery": "companion table/source data",
        "transformations": [],
        "inference_risks": ["visual difference does not establish causal mechanism"],
        "space_attention_cost": "moderate main-text area",
        "accessibility_risks": ["critical groups also use shape/labels, not color alone"],
        "decision": decision,
        "rationale": "chosen for direct contrast" if decision == "chosen" else "rejected because it hides task-level heterogeneity",
    }


def _record(*, mandated: bool = False, final: bool = True) -> dict:
    candidates = [_candidate("paired difference plot", "chosen")]
    if not mandated:
        candidates.append(_candidate("grand-mean bar chart", "rejected"))
    return {
        "schema_version": "1.0.0",
        "display_id": "fig2",
        "stage": "final" if final else "draft",
        "reader_question": "Does the method improve performance consistently across tasks?",
        "reader_state_transition": {
            "before": "reader knows the aggregate benchmark question",
            "after": "reader can inspect direction and heterogeneity of paired task-level effects",
            "remaining_uncertainty": "external-domain generalization remains unresolved",
        },
        "claim_ids": ["C1"],
        "scientific_object": "paired task-level performance difference",
        "statistical_unit": "held-out task",
        "dependence_structure": "methods are evaluated on the same held-out tasks",
        "alternative_explanation": "a grand mean improvement could be driven by a few tasks",
        "representation_mandate": {
            "status": "mandated" if mandated else "not_mandated",
            "reason": "target reporting standard requires this representation" if mandated else "",
        },
        "candidates": candidates,
        "chosen_representation": "paired difference plot",
        "chosen_reason": "It exposes the claim-bearing within-task contrast and failure heterogeneity more directly than a pooled mean bar.",
        "information_loss": ["exact multi-metric lookup is delegated to a companion table"],
        "uncertainty_encoding": "95% interval for the paired effect where inferentially defined",
        "exact_value_companion": "main results table and source data",
        "placement": "main",
        "inference_boundary": "supports paired benchmark improvement; does not establish mechanism or unseen-domain generalization",
        "clean_reader_status": "pass" if final else "pending",
        "final_size_status": "pass" if final else "pending",
        "release": {"decision": "PASS", "notes": []},
    }


def test_contract_requires_purpose_counterfactual_choice_and_loss_audit() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "every main figure needs a scientific purpose",
        "reader-state transition test",
        "representation tournament is mandatory",
        "representation dominance",
        "information-loss audit",
        "same-summary-different-data test",
        "alternative-explanation visibility test",
        "dependence visibility test",
        "uncertainty visibility test",
        "transformation sensitivity test",
        "multi-panel figures need one scientific thesis",
        "figure sequence is part of the paper's argument",
        "real-paper evidence is calibration, not imitation",
        "broad corpus layer",
        "controlled evidence layer",
        "deep-paper layer",
        "clean-reader figure test",
        "final-size and accessibility test",
    ):
        assert marker in text, marker

    assert "there is no universal best plot" in text
    assert "do not turn this conceptual expression into a fake numerical score" in text
    assert "why this representation is better" in text


def test_research_ledger_separates_practice_perception_and_deep_reading() -> None:
    text = RESEARCH.read_text(encoding="utf-8").lower()
    for marker in (
        "broad published-practice corpora",
        "controlled visualization/perception/statistical-cognition research",
        "deep contextual paper reading",
        "more than 8 million",
        "8,834 figures",
        "580 papers",
        "cleveland & mcgill",
        "brehmer & munzner",
        "franconeri",
        "hypothetical outcome plots",
        "published-paper frequency is not a quality score",
        "representation-tournament engineering consequence",
        "research scaling strategy",
    ):
        assert marker in text, marker


def test_schema_contains_counterfactual_and_reader_state_fields() -> None:
    text = SCHEMA.read_text(encoding="utf-8")
    for marker in (
        '"reader_state_transition"',
        '"representation_mandate"',
        '"candidates"',
        '"information_preserved"',
        '"information_hidden"',
        '"perceptual_task"',
        '"dependence_visibility"',
        '"uncertainty_visibility"',
        '"inference_risks"',
        '"clean_reader_status"',
        '"final_size_status"',
    ):
        assert marker in text


def test_valid_counterfactual_representation_decision_passes() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_record())
    assert result["decision"] == "PASS"
    assert result["counts"] == {"error": 0, "unresolved": 0, "review": 0}


def test_nonmandated_display_without_alternative_blocks() -> None:
    verifier = _load_verifier()
    record = _record()
    record["candidates"] = [record["candidates"][0]]
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "counterfactual_representation_missing" for item in result["findings"])


def test_genuinely_mandated_representation_can_have_one_candidate() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_record(mandated=True))
    assert result["decision"] == "PASS"
    assert not any(item["code"] == "counterfactual_representation_missing" for item in result["findings"])


def test_mandate_without_reason_blocks() -> None:
    verifier = _load_verifier()
    record = _record(mandated=True)
    record["representation_mandate"]["reason"] = ""
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "mandate_reason_missing" for item in result["findings"])


def test_chosen_candidate_must_match_chosen_representation() -> None:
    verifier = _load_verifier()
    record = _record()
    record["chosen_representation"] = "grand-mean bar chart"
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "chosen_family_mismatch" for item in result["findings"])


def test_final_display_requires_clean_reader_and_final_size_closure() -> None:
    verifier = _load_verifier()
    record = _record()
    record["clean_reader_status"] = "pending"
    record["final_size_status"] = "pending"
    record["release"]["decision"] = "UNRESOLVED"
    result = verifier.validate(record)
    assert result["decision"] == "UNRESOLVED"
    codes = {item["code"] for item in result["findings"]}
    assert "clean_reader_closure_incomplete" in codes
    assert "final_size_closure_incomplete" in codes


def test_main_figure_without_reader_state_change_is_review_signal() -> None:
    verifier = _load_verifier()
    record = _record()
    record["reader_state_transition"]["after"] = record["reader_state_transition"]["before"]
    record["release"]["decision"] = "REVIEW"
    result = verifier.validate(record)
    assert result["decision"] == "REVIEW"
    assert any(item["code"] == "no_reader_state_transition" for item in result["findings"])


def test_public_skills_route_representation_optimization_without_bloating_always_load() -> None:
    contract_path = "figure-purpose-representation-optimization.md"
    schema_path = "figure-representation-decision.schema.json"
    verifier_path = "verify_figure_representation_decision.py"
    research_path = "figure-purpose-representation-evidence-2026-09-01.md"

    writing = WRITING.read_text(encoding="utf-8")
    pipeline = PIPELINE.read_text(encoding="utf-8")
    reviewer = REVIEWER.read_text(encoding="utf-8")
    figure = FIGURE.read_text(encoding="utf-8")

    for text in (writing, pipeline, reviewer, figure):
        assert contract_path in text
        assert schema_path in text
        assert verifier_path in text
        assert research_path in text

    assert _version(writing) >= (1, 18, 0)
    assert _version(pipeline) >= (1, 20, 0)
    assert _version(reviewer) >= (3, 5, 0)
    assert _version(figure) >= (3, 7, 0)

    # Progressive disclosure from PR #26 remains intact: the new representation
    # contract must not be added to the global always-loaded kernels.
    for text in (writing, pipeline, reviewer):
        always = text.split("references:", 1)[0]
        assert contract_path not in always
