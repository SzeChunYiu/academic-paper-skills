from __future__ import annotations

import importlib.util
from copy import deepcopy
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "scientific-rhetorical-act-and-result-state.md"
RESEARCH = SHARED / "research" / "atomic-result-rhetoric-and-writing-quality-evidence-2026-09-02.md"
SCHEMA = SHARED / "analysis-contracts" / "scientific-rhetorical-act.schema.json"
VERIFIER = SHARED / "scripts" / "verify_scientific_rhetorical_act.py"
KERNEL = SHARED / "core" / "ai-session-execution-kernel.md"
WRITING = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER = SKILLS / "nature-reviewer" / "manifest.yaml"


def _load_verifier():
    spec = importlib.util.spec_from_file_location("verify_scientific_rhetorical_act", VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _version(text: str) -> tuple[int, ...]:
    for line in text.splitlines():
        if line.startswith("version:"):
            return tuple(int(part) for part in line.split(":", 1)[1].strip().split("."))
    raise AssertionError("manifest version missing")


def _act(
    *,
    act_id: str = "A1",
    result_id: str = "R1",
    evidence_state: str = "directional_supported",
    claimed_state: str = "directional_effect",
    role: str = "primary_confirmatory",
    prespecification: str = "prespecified",
    placement: str = "main_text",
) -> dict:
    return {
        "act_id": act_id,
        "result_id": result_id,
        "claim_ids": ["C1"],
        "section": "Results",
        "rhetorical_act": "estimate",
        "evidence_state": evidence_state,
        "claimed_state": claimed_state,
        "analysis_role": role,
        "prespecification": prespecification,
        "scientific_direction": "increase",
        "target": "paired held-out task performance difference",
        "observation": "method A had a larger estimated score than method B",
        "uncertainty": "95% interval for the paired effect is reported",
        "scientific_consequence": "the comparison supports a bounded improvement on the tested tasks",
        "allowed_inference": ["bounded directional improvement on the tested tasks"],
        "forbidden_inference": ["universal superiority or causal mechanism"],
        "reader_job": "understand the direction, magnitude, uncertainty, and local consequence",
        "wording_plan": {
            "lead_message": "Method A outperformed method B on the paired held-out tasks.",
            "quantitative_anchor": "paired effect and 95% interval",
            "qualification": "limited to the tested tasks",
            "handoff": "the next analysis tests whether the gain is consistent across domains",
        },
        "display_binding": "fig2/table1",
        "placement": placement,
        "status": "retained",
    }


def _record(*acts: dict) -> dict:
    if not acts:
        acts = (_act(),)
    return {
        "schema_version": "1.0.0",
        "record_id": "result-rhetoric-1",
        "manuscript_scope": "headline Results and abstract",
        "acts": list(acts),
        "cross_surface_consistency": {
            "checked": True,
            "surfaces": ["abstract", "results", "figure", "discussion"],
            "optimism_drift_detected": False,
            "notes": [],
        },
        "release": {"decision": "PASS", "notes": []},
    }


def test_contract_atomizes_result_states_and_writing_quality() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "result polarity is not enough",
        "ordinary non-significant result / failure to reject",
        "inconclusive / imprecise result",
        "evidence of absence / practically negligible effect",
        "equivalence",
        "non-inferiority",
        "supported adverse / harmful effect",
        "failed prespecified hypothesis",
        "failed replication / non-replication",
        "contradictory evidence",
        "heterogeneous / interaction result",
        "robustness / sensitivity result",
        "positive control",
        "negative control",
        "unexpected / anomalous result",
        "exploratory / post hoc result",
        "threshold / criterion result",
        "boundary / failure-mode result",
        "secondary-outcome rescue",
        "trend laundering",
        "null-to-equivalence laundering",
        "significance-to-importance laundering",
        "abstract optimism drift",
        "what distinguishes a well-written scientific article from a poorly written one",
        "positive/negative symmetry",
        "cross-surface consistency",
    ):
        assert marker in text, marker

    assert "non-significant\n!= no effect" in text
    assert "write the evidence state you actually have" in text


def test_research_ledger_contains_methodology_spin_editorial_and_real_paper_layers() -> None:
    text = RESEARCH.read_text(encoding="utf-8").lower()
    for marker in (
        "consort 2025",
        "nature human behaviour",
        "communications psychology 2025",
        "consort harms 2022",
        "subgroup and heterogeneity interpretation",
        "systematic review of spin",
        "secondary-outcome rescue",
        "nature computational science 2026",
        "nature cancer",
        "cognitive control training",
        "audio-based ai classifiers",
        "oral semaglutide",
        "tenecteplase",
        "online searches to evaluate misinformation",
        "paraspeckle condensation",
        "climate interventions",
        "non-significant is not absence",
        "a null/negative result can be the narrative hinge",
    ):
        assert marker in text, marker


def test_schema_records_fine_grained_result_state() -> None:
    text = SCHEMA.read_text(encoding="utf-8")
    for marker in (
        '"evidence_state"',
        '"claimed_state"',
        '"analysis_role"',
        '"prespecification"',
        '"scientific_direction"',
        '"allowed_inference"',
        '"forbidden_inference"',
        '"absence_basis"',
        '"heterogeneity_basis"',
        '"control_basis"',
        '"wording_plan"',
        '"optimism_drift_detected"',
    ):
        assert marker in text


def test_valid_directional_result_passes() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_record())
    assert result["decision"] == "PASS"
    assert result["counts"] == {"error": 0, "review": 0}


def test_ordinary_non_significance_cannot_claim_equivalence() -> None:
    verifier = _load_verifier()
    act = _act(evidence_state="ordinary_non_significant", claimed_state="equivalence")
    act["scientific_direction"] = "near_zero"
    act["wording_plan"]["lead_message"] = "The two methods were equivalent."
    record = _record(act)
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    codes = {item["code"] for item in result["findings"]}
    assert result["decision"] == "BLOCKED"
    assert "evidence_claim_mismatch" in codes


def test_evidence_of_absence_requires_explicit_basis() -> None:
    verifier = _load_verifier()
    act = _act(evidence_state="evidence_of_absence", claimed_state="bounded_absence")
    act["scientific_direction"] = "near_zero"
    act["wording_plan"]["lead_message"] = "The data exclude effects of the prespecified meaningful magnitude."
    record = _record(act)
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "absence_basis_missing" for item in result["findings"])


def test_equivalence_requires_margin() -> None:
    verifier = _load_verifier()
    act = _act(evidence_state="equivalence_supported", claimed_state="equivalence")
    act["scientific_direction"] = "near_zero"
    act["absence_basis"] = {
        "method": "TOST",
        "meaningful_region": "differences smaller than the smallest effect size of interest",
        "margin": "",
        "status": "prespecified",
    }
    record = _record(act)
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "margin_missing" for item in result["findings"])


def test_failed_prespecified_hypothesis_must_actually_be_prespecified() -> None:
    verifier = _load_verifier()
    act = _act(
        evidence_state="failed_prespecified_hypothesis",
        claimed_state="failed_hypothesis",
        role="primary_confirmatory",
        prespecification="post_hoc",
    )
    act["wording_plan"]["lead_message"] = "The scaling prediction was not supported."
    record = _record(act)
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "failed_hypothesis_not_prespecified" for item in result["findings"])


def test_failed_hypothesis_does_not_automatically_rule_out_alternative() -> None:
    verifier = _load_verifier()
    act = _act(
        evidence_state="failed_prespecified_hypothesis",
        claimed_state="failed_hypothesis",
        role="primary_confirmatory",
        prespecification="prespecified",
    )
    act["wording_plan"]["lead_message"] = "The prediction was not supported, which rules out model scale as an explanation."
    record = _record(act)
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "failed_hypothesis_proves_alternative" for item in result["findings"])


def test_heterogeneity_claim_requires_interaction_basis() -> None:
    verifier = _load_verifier()
    act = _act(evidence_state="heterogeneity_supported", claimed_state="heterogeneity")
    act["scientific_direction"] = "mixed"
    act["wording_plan"]["lead_message"] = "The treatment effect differed across age groups."
    record = _record(act)
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "heterogeneity_basis_missing" for item in result["findings"])


def test_exploratory_post_hoc_must_remain_exploratory() -> None:
    verifier = _load_verifier()
    act = _act(
        evidence_state="exploratory_post_hoc",
        claimed_state="exploratory_pattern",
        role="primary_confirmatory",
        prespecification="prespecified",
    )
    act["wording_plan"]["lead_message"] = "An exploratory pattern emerged."
    record = _record(act)
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    codes = {item["code"] for item in result["findings"]}
    assert result["decision"] == "BLOCKED"
    assert "exploratory_role_mismatch" in codes
    assert "post_hoc_status_missing" in codes


def test_harm_cannot_be_repaired_by_omission() -> None:
    verifier = _load_verifier()
    act = _act(
        evidence_state="harm_supported",
        claimed_state="harm",
        role="adverse_harm",
        prespecification="prespecified",
        placement="omitted",
    )
    act["scientific_direction"] = "harmful"
    act["status"] = "omit"
    act["wording_plan"]["lead_message"] = "Serious adverse events were more frequent in the intervention group."
    record = _record(act)
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "harm_omitted" for item in result["findings"])


def test_trend_toward_significance_is_review_signal() -> None:
    verifier = _load_verifier()
    act = _act(evidence_state="ordinary_non_significant", claimed_state="no_clear_difference")
    act["wording_plan"]["lead_message"] = "The effect showed a trend toward significance."
    record = _record(act)
    record["release"]["decision"] = "REVIEW"
    result = verifier.validate(record)
    assert result["decision"] == "REVIEW"
    assert any(item["code"] == "trend_toward_significance" for item in result["findings"])


def test_failed_primary_plus_favorable_secondary_triggers_rescue_review() -> None:
    verifier = _load_verifier()
    primary = _act(
        act_id="A1",
        result_id="primary",
        evidence_state="ordinary_non_significant",
        claimed_state="no_clear_difference",
        role="primary_confirmatory",
    )
    primary["wording_plan"]["lead_message"] = "The primary comparison did not provide clear evidence of a difference."
    secondary = _act(
        act_id="A2",
        result_id="secondary",
        evidence_state="superiority_supported",
        claimed_state="superiority",
        role="secondary_confirmatory",
    )
    secondary["wording_plan"]["lead_message"] = "A secondary outcome favored the intervention."
    record = _record(primary, secondary)
    record["release"]["decision"] = "REVIEW"
    result = verifier.validate(record)
    assert result["decision"] == "REVIEW"
    assert any(item["code"] == "secondary_rescue_risk" for item in result["findings"])


def test_optimism_drift_blocks_release() -> None:
    verifier = _load_verifier()
    record = _record()
    record["cross_surface_consistency"]["optimism_drift_detected"] = True
    record["release"]["decision"] = "BLOCKED"
    result = verifier.validate(record)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "optimism_drift" for item in result["findings"])


def test_valid_bounded_absence_with_basis_passes() -> None:
    verifier = _load_verifier()
    act = _act(evidence_state="evidence_of_absence", claimed_state="bounded_absence")
    act["scientific_direction"] = "near_zero"
    act["absence_basis"] = {
        "method": "Bayes factor with prespecified meaningful effect region",
        "meaningful_region": "effects at or above 0.20 standardized units",
        "margin": "0.20",
        "status": "prespecified",
    }
    act["wording_plan"]["lead_message"] = "The data provide evidence against effects of at least 0.20 standardized units under the tested conditions."
    result = verifier.validate(_record(act))
    assert result["decision"] == "PASS"


def test_public_skills_route_atomic_result_contract_progressively() -> None:
    contract = "scientific-rhetorical-act-and-result-state.md"
    evidence = "atomic-result-rhetoric-and-writing-quality-evidence-2026-09-02.md"
    schema = "scientific-rhetorical-act.schema.json"
    verifier = "verify_scientific_rhetorical_act.py"

    writing = WRITING.read_text(encoding="utf-8")
    pipeline = PIPELINE.read_text(encoding="utf-8")
    reviewer = REVIEWER.read_text(encoding="utf-8")

    for text in (writing, pipeline, reviewer):
        assert contract in text
        assert evidence in text
        assert schema in text
        assert verifier in text
        always = text.split("references:", 1)[0]
        assert contract not in always

    assert _version(writing) >= (1, 20, 0)
    assert _version(pipeline) >= (1, 23, 0)
    assert _version(reviewer) >= (3, 7, 0)


def test_kernel_keeps_compact_result_state_invariant() -> None:
    text = KERNEL.read_text(encoding="utf-8").lower()
    assert "evidence state before result rhetoric" in text
    assert "scientific-rhetorical-act-and-result-state.md" in text
