from __future__ import annotations

import importlib.util
from datetime import datetime, timezone
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "manuscript-budget-utilization.md"
VERIFIER = SHARED / "scripts" / "verify_manuscript_budget.py"
WRITING = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER = SKILLS / "nature-reviewer" / "manifest.yaml"


def _load_verifier():
    spec = importlib.util.spec_from_file_location("verify_manuscript_budget", VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _ledger(actual: int, limit: int = 4000, expected_revision: bool = False, release: str = "PASS") -> dict:
    return {
        "schema_version": "1.0.0",
        "manuscript_id": "budget-demo",
        "target": {
            "venue": "Example Journal",
            "article_type": "Article",
            "stage": "initial_submission",
            "as_of": "2026-08-31",
            "budget_basis": "words",
        },
        "constraints": [
            {
                "constraint_id": "main_words",
                "surface": "main text",
                "unit": "words",
                "strength": "hard",
                "limit": limit,
                "actual": actual,
                "count_rule": "main text only",
                "source_ref": "official-rule",
                "status": "within",
            }
        ],
        "sections": [
            {
                "section_id": "setup",
                "title": "Problem formulation",
                "reader_question": "What is the scientific problem?",
                "scientific_function": "activate the central object and assumptions",
                "priority": "P1",
                "unit": "words",
                "soft_min": 500,
                "soft_max": 900,
                "actual": 700,
                "status": "within_budget",
                "claim_ids": ["C1"],
                "overflow_route": "compress background first",
            },
            {
                "section_id": "results",
                "title": "Results",
                "reader_question": "What establishes the claim?",
                "scientific_function": "decisive evidence",
                "priority": "P2",
                "unit": "words",
                "soft_min": 1200,
                "soft_max": 2200,
                "actual": 1600,
                "status": "within_budget",
                "claim_ids": ["C1"],
                "overflow_route": "move non-claim-changing robustness to support",
            },
            {
                "section_id": "discussion",
                "title": "Discussion",
                "reader_question": "What do the findings mean?",
                "scientific_function": "interpretation and boundaries",
                "priority": "P3",
                "unit": "words",
                "soft_min": 500,
                "soft_max": 900,
                "actual": 650,
                "status": "within_budget",
                "claim_ids": ["C1"],
                "overflow_route": "remove repeated positioning first",
            },
        ],
        "reserve": {
            "unit": "words",
            "planned": 200,
            "actual": max(limit - actual, 0),
            "expected_revision": expected_revision,
            "rationale": "preserve room for scientifically necessary clarification",
        },
        "sources": [],
        "release": {
            "decision": release,
            "reviewed_at": datetime.now(timezone.utc).isoformat(),
            "notes": [],
        },
    }


def test_contract_rejects_filling_to_a_percentage() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "do not maximize words used",
        "85–95% utilization often deserves no special concern",
        "diagnostic band, not a quota",
        "under-utilization is a diagnostic question, not a padding trigger",
        "allocate from the contribution outward",
        "marginal scientific value per unit of space",
        "final available space should deepen before it broadens",
        "compression is asymmetric",
        "information density is not sentence stuffing",
        "figures, tables and equations share the attention budget",
    ):
        assert marker in text, marker


def test_low_utilization_is_info_not_failure_or_padding_order() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_ledger(actual=3000, limit=4000))
    assert result["decision"] == "PASS"
    finding = next(item for item in result["findings"] if item["code"] == "main_text_low_utilization_diagnostic")
    assert finding["severity"] == "info"
    assert "do not pad" in finding["message"].lower()
    assert result["utilization"]["percent"] == 75.0


def test_healthy_mid_band_does_not_create_utilization_finding() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_ledger(actual=3600, limit=4000))
    assert result["decision"] == "PASS"
    codes = {item["code"] for item in result["findings"]}
    assert "main_text_low_utilization_diagnostic" not in codes
    assert "main_text_high_utilization_diagnostic" not in codes


def test_high_utilization_with_expected_revision_requires_headroom_review() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_ledger(actual=3880, limit=4000, expected_revision=True, release="REVIEW"))
    assert result["decision"] == "REVIEW"
    codes = {item["code"] for item in result["findings"]}
    assert "main_text_high_utilization_diagnostic" in codes
    assert "thin_revision_headroom" in codes


def test_high_utilization_without_expected_revision_is_not_automatic_failure() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_ledger(actual=3880, limit=4000, expected_revision=False))
    assert result["decision"] == "PASS"
    codes = {item["code"] for item in result["findings"]}
    assert "main_text_high_utilization_diagnostic" in codes
    assert "thin_revision_headroom" not in codes


def test_public_skills_route_utilization_contract() -> None:
    for path in (WRITING, PIPELINE, REVIEWER):
        text = path.read_text(encoding="utf-8")
        assert "manuscript-budget-utilization.md" in text, path
        assert "verify_manuscript_budget.py" in text, path
