from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

SHARED = Path(__file__).parents[1]
SKILLS = SHARED.parent
SCRIPT = SHARED / "scripts" / "verify_research_integrity.py"
SCHEMA = SHARED / "analysis-contracts" / "research-integrity-ledger.schema.json"
CONTRACT = SHARED / "core" / "research-integrity-verification.md"

spec = importlib.util.spec_from_file_location("verify_research_integrity", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def args() -> argparse.Namespace:
    return argparse.Namespace(timeout=1.0, user_agent="test", mailto=None)


def valid_ledger() -> dict:
    return {
        "schema_version": "1.0",
        "manuscript_id": "paper-1",
        "authoring_agent_id": "writer-agent",
        "verification_scope": "full_manuscript",
        "sources": [
            {
                "source_id": "S1",
                "source_type": "journal_article",
                "identifiers": [{"scheme": "doi", "value": "10.0000/example"}],
                "bibliographic": {
                    "title": "Verified example",
                    "authors": ["Ada Smith"],
                    "year": 2024,
                    "venue": "Journal",
                },
                "declared_publication_status": "ACTIVE",
                "identity_checks": [
                    {
                        "provider": "crossref",
                        "status": "MATCH",
                        "checked_at": "2026-08-30T12:00:00Z",
                        "verification_method": "registry_lookup",
                        "verifier_id": "registry-tool",
                    }
                ],
                "status_checks": [
                    {
                        "provider": "crossref",
                        "status": "ACTIVE",
                        "checked_at": "2026-08-30T12:00:00Z",
                        "verification_method": "registry_lookup",
                        "verifier_id": "registry-tool",
                    }
                ],
            }
        ],
        "claims": [
            {
                "claim_id": "C1",
                "location": "Introduction:1",
                "text": "The verified example reports the stated result.",
                "claim_class": "literature_fact",
                "risk": "normal",
                "release_status": "VERIFIED",
                "independent_check": {"status": "PASS", "verifier_id": "reviewer-agent"},
            }
        ],
        "evidence_receipts": [
            {
                "receipt_id": "E1",
                "claim_id": "C1",
                "warrant_type": "source",
                "source_id": "S1",
                "locator": "Results, paragraph 2",
                "evidence_fingerprint": "sha256:" + "0" * 64,
                "verification_method": "fulltext_span_check",
                "support_status": "ENTAILS",
                "scope_match": "MATCH",
                "verifier_id": "evidence-reader",
            }
        ],
        "citation_usages": [
            {
                "citation_id": "R1",
                "source_id": "S1",
                "location": "Introduction:1",
                "claim_ids": ["C1"],
            }
        ],
        "release": {"requested_state": "submission_ready"},
    }


def validate(ledger: dict) -> dict:
    return module.validate_ledger(ledger, live=False, args=args())


def test_valid_release_ledger_passes() -> None:
    report = validate(valid_ledger())
    assert report["decision"] == "PASS", report
    assert report["error_count"] == 0


def test_model_self_report_is_not_verification() -> None:
    ledger = valid_ledger()
    ledger["evidence_receipts"][0]["verification_method"] = "model_self_report"
    report = validate(ledger)
    assert report["decision"] == "BLOCKED"
    assert any("untrusted verification_method" in x for x in report["errors"])


def test_authoring_agent_cannot_self_certify_independent_check() -> None:
    ledger = valid_ledger()
    ledger["claims"][0]["independent_check"]["verifier_id"] = "writer-agent"
    report = validate(ledger)
    assert any("independent verifier must differ" in x for x in report["errors"])


def test_release_requires_identity_and_status_receipts() -> None:
    ledger = valid_ledger()
    ledger["sources"][0].pop("identity_checks")
    ledger["sources"][0].pop("status_checks")
    report = validate(ledger)
    assert any("release requires a resolved identity check" in x for x in report["errors"])
    assert any("release requires a current publication-status check" in x for x in report["errors"])


def test_retracted_source_blocks_release() -> None:
    ledger = valid_ledger()
    ledger["sources"][0]["declared_publication_status"] = "RETRACTED"
    ledger["sources"][0]["status_checks"][0]["status"] = "RETRACTED"
    report = validate(ledger)
    assert any("publication status is RETRACTED" in x for x in report["errors"])


def test_citation_must_map_to_source_receipt_for_same_claim() -> None:
    ledger = valid_ledger()
    ledger["evidence_receipts"][0]["source_id"] = "S_OTHER"
    report = validate(ledger)
    assert any("no evidence receipt for claim C1" in x for x in report["errors"])


def test_high_risk_claim_requires_counterevidence_search() -> None:
    ledger = valid_ledger()
    ledger["claims"][0]["claim_class"] = "causal"
    ledger["claims"][0]["risk"] = "high"
    report = validate(ledger)
    assert any("requires counterevidence_search" in x for x in report["errors"])


def test_metadata_identity_comparison_rejects_wrong_source() -> None:
    source = valid_ledger()["sources"][0]
    ok, problems = module.compare_identity(
        source,
        {"title": "Completely unrelated paper", "authors": ["Other Person"], "year": 2020},
    )
    assert not ok
    assert any("title mismatch" in x for x in problems)
    assert any("year mismatch" in x for x in problems)
    assert any("first-author mismatch" in x for x in problems)


def test_contract_schema_and_pipeline_routing_are_present() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert schema["title"] == "Research Integrity Verification Ledger"
    contract = CONTRACT.read_text(encoding="utf-8")
    for marker in (
        "phantom source",
        "semantic citation hallucination",
        "retrieval prompt injection",
        "evidence fingerprint",
        "independent verifier",
        "counterevidence",
    ):
        assert marker in contract.lower()

    for path in (
        SKILLS / "academic-paper-pipeline" / "manifest.yaml",
        SKILLS / "nature-citation" / "manifest.yaml",
    ):
        assert "research-integrity-verification.md" in path.read_text(encoding="utf-8"), str(path)
