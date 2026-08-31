from __future__ import annotations

import importlib.util
from datetime import datetime, timezone
from pathlib import Path


SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
CONTRACT = SHARED / "core" / "venue-constrained-manuscript-budget.md"
EXCELLENCE = SHARED / "core" / "manuscript-excellence-release-gate.md"
SCHEMA = SHARED / "analysis-contracts" / "manuscript-budget.schema.json"
VERIFIER = SHARED / "scripts" / "verify_manuscript_budget.py"
WRITING = SKILLS / "academic-writing" / "manifest.yaml"
PIPELINE = SKILLS / "academic-paper-pipeline" / "manifest.yaml"
REVIEWER = SKILLS / "nature-reviewer" / "manifest.yaml"


def _version(text: str) -> tuple[int, ...]:
    for line in text.splitlines():
        if line.startswith("version:"):
            return tuple(int(part) for part in line.split(":", 1)[1].strip().split("."))
    raise AssertionError("manifest version missing")


def _load_verifier():
    spec = importlib.util.spec_from_file_location("verify_manuscript_budget", VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _base_ledger() -> dict:
    return {
        "schema_version": "1.0.0",
        "manuscript_id": "paper-demo",
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
                "limit": 3500,
                "actual": 3200,
                "count_rule": "abstract, methods, references and legends excluded",
                "source_ref": "official-content-type",
                "status": "within",
            },
            {
                "constraint_id": "display_items",
                "surface": "figures and tables",
                "unit": "display_items",
                "strength": "hard",
                "limit": 6,
                "actual": 5,
                "count_rule": "figures and tables combined",
                "source_ref": "official-content-type",
                "status": "within",
            },
        ],
        "sections": [
            {
                "section_id": "intro",
                "title": "Introduction",
                "reader_question": "What problem remains unresolved?",
                "scientific_function": "problem, gap and bounded contribution",
                "priority": "P1",
                "unit": "words",
                "soft_min": 450,
                "soft_max": 700,
                "actual": 600,
                "status": "within_budget",
                "claim_ids": ["C1"],
                "overflow_route": "compress background before cutting gap definition",
            },
            {
                "section_id": "results",
                "title": "Results",
                "reader_question": "What evidence establishes the headline claim?",
                "scientific_function": "decisive evidence chain",
                "priority": "P2",
                "unit": "words",
                "soft_min": 1500,
                "soft_max": 2100,
                "actual": 1850,
                "status": "within_budget",
                "claim_ids": ["C1"],
                "overflow_route": "move secondary robustness to support",
            },
            {
                "section_id": "discussion",
                "title": "Discussion",
                "reader_question": "What do the findings mean and where do they stop?",
                "scientific_function": "interpretation, alternative, boundary and implication",
                "priority": "P3",
                "unit": "words",
                "soft_min": 500,
                "soft_max": 850,
                "actual": 650,
                "status": "within_budget",
                "claim_ids": ["C1"],
                "overflow_route": "remove repeated positioning before claim-changing boundary",
            },
        ],
        "reserve": {
            "unit": "words",
            "planned": 100,
            "actual": 300,
            "expected_revision": False,
            "rationale": "leave room for production clarification",
        },
        "sources": [],
        "release": {
            "decision": "PASS",
            "reviewed_at": datetime.now(timezone.utc).isoformat(),
            "notes": [],
        },
    }


def test_contract_treats_space_as_target_specific_scientific_resource() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "a manuscript budget is not a late copy-editing problem",
        "build a publication-surface inventory",
        "allocate by scientific function, not conventional section name",
        "no universal section percentages",
        "closest / nearest work receives a function-limited budget",
        "displays have an opportunity cost",
        "abstract and title are separate micro-budgets",
        "captions and legends are not free storage",
        "references are selected under a relevance budget",
        "every addition must be funded",
        "maintain a deliberate reserve",
        "page-limited manuscripts were measured in the official rendered template",
    ):
        assert marker in text, marker

    # Lock the actual anti-quota examples and derivation rule rather than exact
    # Markdown emphasis around the word "not".
    assert "introduction must be 15%" in text
    assert "related work must be 20%" in text
    assert "official target constraints" in text
    assert "the current paper's argument/claim dependency graph" in text
    assert "analogue proportions are descriptive priors, not quotas" in text


def test_contract_protects_core_science_from_positioning_overweight() -> None:
    text = CONTRACT.read_text(encoding="utf-8").lower()
    for marker in (
        "p4–p6 should not crowd out an underdeveloped p1–p3 function",
        "claim-subtraction ledger",
        "a long related work section is followed by a one-paragraph formulation",
        "discussion spends more effort restating nearest work than interpreting the paper's findings",
        "evidence that changes the headline claim",
        "a definition required to understand the main result",
        "the contribution-defining formal spine",
    ):
        assert marker in text, marker


def test_schema_is_versioned_and_covers_mixed_budget_units() -> None:
    text = SCHEMA.read_text(encoding="utf-8")
    assert '"const": "1.0.0"' in text
    for marker in ('"words"', '"pages"', '"characters"', '"references"', '"display_items"'):
        assert marker in text
    for marker in ('"underdeveloped"', '"overweight"', '"needs_render_measurement"', '"unresolved_target_rule"'):
        assert marker in text


def test_valid_budget_passes() -> None:
    verifier = _load_verifier()
    result = verifier.validate(_base_ledger())
    assert result["decision"] == "PASS"
    assert result["counts"] == {"error": 0, "unresolved": 0, "review": 0}


def test_hard_word_limit_blocks_release() -> None:
    verifier = _load_verifier()
    ledger = _base_ledger()
    ledger["constraints"][0]["actual"] = 3600
    ledger["constraints"][0]["status"] = "over"
    ledger["release"]["decision"] = "BLOCKED"
    result = verifier.validate(ledger)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "hard_limit_exceeded" for item in result["findings"])


def test_page_limited_target_requires_rendered_measurement() -> None:
    verifier = _load_verifier()
    ledger = _base_ledger()
    ledger["target"]["budget_basis"] = "pages"
    ledger["constraints"] = [
        {
            "constraint_id": "content_pages",
            "surface": "main content",
            "unit": "pages",
            "strength": "hard",
            "limit": 9,
            "actual": None,
            "count_rule": "figures and tables included; references and appendix excluded",
            "source_ref": "official-handbook",
            "status": "unmeasured",
        }
    ]
    ledger["reserve"] = {
        "unit": "pages",
        "planned": 0.25,
        "actual": None,
        "expected_revision": False,
        "rationale": "render after figure layout stabilizes",
    }
    ledger["release"]["decision"] = "UNRESOLVED"
    result = verifier.validate(ledger)
    assert result["decision"] == "UNRESOLVED"
    codes = {item["code"] for item in result["findings"]}
    assert "rendered_page_measurement_required" in codes
    assert "hard_constraint_unmeasured" in codes


def test_underdeveloped_decisive_section_blocks_even_under_total_limit() -> None:
    verifier = _load_verifier()
    ledger = _base_ledger()
    ledger["sections"][1]["status"] = "underdeveloped"
    ledger["release"]["decision"] = "BLOCKED"
    result = verifier.validate(ledger)
    assert result["decision"] == "BLOCKED"
    assert any(
        item["code"] == "section_underdeveloped" and item["severity"] == "error"
        for item in result["findings"]
    )


def test_overweight_related_work_is_review_not_universal_error() -> None:
    verifier = _load_verifier()
    ledger = _base_ledger()
    ledger["sections"].append(
        {
            "section_id": "related",
            "title": "Related Work",
            "reader_question": "What is the closest prior work and exact gap?",
            "scientific_function": "selective positioning",
            "priority": "P4",
            "unit": "words",
            "soft_min": 150,
            "soft_max": 350,
            "actual": 700,
            "status": "overweight",
            "claim_ids": [],
            "overflow_route": "compress to closest origins/comparator/gap only",
        }
    )
    ledger["release"]["decision"] = "REVIEW"
    result = verifier.validate(ledger)
    assert result["decision"] == "REVIEW"
    codes = {item["code"] for item in result["findings"]}
    assert "above_soft_budget" in codes
    assert "section_reallocation_needed" in codes


def test_zero_reserve_is_review_signal_when_revision_expected() -> None:
    verifier = _load_verifier()
    ledger = _base_ledger()
    ledger["reserve"]["planned"] = 100
    ledger["reserve"]["actual"] = 0
    ledger["reserve"]["expected_revision"] = True
    ledger["release"]["decision"] = "REVIEW"
    result = verifier.validate(ledger)
    assert result["decision"] == "REVIEW"
    codes = {item["code"] for item in result["findings"]}
    assert "reserve_below_plan" in codes
    assert "zero_revision_reserve" in codes


def test_unstated_limit_cannot_be_invented() -> None:
    verifier = _load_verifier()
    ledger = _base_ledger()
    ledger["constraints"][0]["strength"] = "none_stated"
    ledger["constraints"][0]["limit"] = 3000
    ledger["release"]["decision"] = "BLOCKED"
    result = verifier.validate(ledger)
    assert result["decision"] == "BLOCKED"
    assert any(item["code"] == "invented_unstated_limit" for item in result["findings"])


def test_excellence_gate_makes_target_budget_a_release_requirement() -> None:
    text = EXCELLENCE.read_text(encoding="utf-8").lower()
    for marker in (
        "target manuscript budget ledger",
        "e8 — venue-constrained allocation",
        "nearest-work/related work is selective rather than exhaustive",
        "page-limited targets have been measured in the official rendered template",
        "every substantive manuscript addition must be funded",
        "no universal section percentage is required",
    ):
        assert marker in text, marker


def test_writing_pipeline_and_reviewer_always_load_budget_contract() -> None:
    writing = WRITING.read_text(encoding="utf-8")
    pipeline = PIPELINE.read_text(encoding="utf-8")
    reviewer = REVIEWER.read_text(encoding="utf-8")
    contract_path = "../nature-shared/core/venue-constrained-manuscript-budget.md"
    schema_path = "../nature-shared/analysis-contracts/manuscript-budget.schema.json"
    verifier_path = "../nature-shared/scripts/verify_manuscript_budget.py"
    for text in (writing, pipeline, reviewer):
        assert contract_path in text
        assert schema_path in text
        assert verifier_path in text
    assert _version(writing) >= (1, 14, 0)
    assert _version(pipeline) >= (1, 16, 0)
    assert _version(reviewer) >= (3, 1, 0)
