from __future__ import annotations

import argparse
import importlib.util
from datetime import datetime, timezone
from pathlib import Path

SHARED = Path(__file__).parents[1]
SCRIPT = SHARED / "scripts" / "verify_research_integrity.py"
EMPTY_SHA = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

spec = importlib.util.spec_from_file_location("verify_research_integrity_review_regressions", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def args() -> argparse.Namespace:
    return argparse.Namespace(
        timeout=1.0,
        user_agent="test",
        mailto=None,
        manuscript=None,
        max_status_age_days=30,
    )


def ledger_with_statuses(statuses: list[str]) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    return {
        "schema_version": "1.0",
        "manuscript_id": "paper-review-regression",
        "manuscript_fingerprint": EMPTY_SHA,
        "authoring_agent_id": "writer",
        "coverage_check": {
            "status": "PASS",
            "verifier_id": "coverage-reviewer",
            "verification_method": "human_review",
            "checked_at": now,
            "reviewed_manuscript_fingerprint": EMPTY_SHA,
        },
        "sources": [
            {
                "source_id": "S1",
                "source_type": "journal_article",
                "identifiers": [{"scheme": "doi", "value": "10.0000/example"}],
                "bibliographic": {
                    "title": "Verified example",
                    "authors": ["Ada Smith"],
                    "year": 2024,
                },
                "declared_publication_status": "ACTIVE",
                "identity_checks": [
                    {
                        "provider": "registry",
                        "status": "MATCH",
                        "checked_at": now,
                        "verification_method": "registry_lookup",
                        "verifier_id": "registry-tool",
                    }
                ],
                "status_checks": [
                    {
                        "provider": f"registry-{index}",
                        "status": status,
                        "checked_at": now,
                        "verification_method": "registry_lookup",
                        "verifier_id": "registry-tool",
                    }
                    for index, status in enumerate(statuses)
                ],
            }
        ],
        "claims": [
            {
                "claim_id": "C1",
                "location": "Introduction:1",
                "text": "The source reports the result.",
                "claim_class": "literature_fact",
                "risk": "normal",
                "release_status": "VERIFIED",
                "independent_check": {"status": "PASS", "verifier_id": "independent-reviewer"},
            }
        ],
        "evidence_receipts": [
            {
                "receipt_id": "E1",
                "claim_id": "C1",
                "warrant_type": "source",
                "source_id": "S1",
                "locator": "Results, paragraph 1",
                "evidence_fingerprint": "sha256:" + "0" * 64,
                "verification_method": "fulltext_span_check",
                "support_status": "ENTAILS",
                "scope_match": "MATCH",
                "verifier_id": "evidence-reviewer",
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
        "release": {"requested_state": "review"},
    }


def test_mixed_active_and_retracted_status_receipts_fail_closed() -> None:
    report = module.validate_ledger(ledger_with_statuses(["ACTIVE", "RETRACTED"]), live=False, args=args())
    assert report["decision"] == "BLOCKED"
    assert any("blocking status RETRACTED" in error for error in report["errors"])


def test_datacite_creator_names_preserve_family_identity() -> None:
    source = {
        "bibliographic": {
            "title": "Dataset title",
            "authors": ["Ada Smith"],
            "year": 2024,
        }
    }
    structured = module.datacite_creator_name({"givenName": "Ada", "familyName": "Smith", "name": "Smith, Ada"})
    fallback = module.datacite_creator_name({"name": "Smith, Ada"})
    assert structured == "Ada Smith"
    assert fallback == "Ada Smith"

    for author in (structured, fallback, "Smith, Ada"):
        matched, problems = module.compare_identity(
            source,
            {"title": "Dataset title", "authors": [author], "year": 2024},
        )
        assert matched, problems
