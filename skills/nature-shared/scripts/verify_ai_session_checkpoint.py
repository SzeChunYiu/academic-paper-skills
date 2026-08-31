#!/usr/bin/env python3
"""Validate compact academic-paper AI session checkpoints.

The verifier checks structural completeness plus a few execution invariants. It
is intentionally small: the checkpoint is a context-management aid, not a new
bureaucratic source of manuscript truth.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import jsonschema

SCHEMA = Path(__file__).parents[1] / "analysis-contracts" / "ai-session-checkpoint.schema.json"

MODE_SURFACE_REQUIRED = {"COMPOSE", "AUDIT", "REVISE"}


def validate(payload: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    try:
        jsonschema.validate(payload, schema)
    except jsonschema.ValidationError as exc:
        findings.append(
            {
                "code": "schema_invalid",
                "severity": "error",
                "message": exc.message,
            }
        )
        return _result(findings)

    mode = payload["session_mode"]
    surface = payload["active_scope"]["surface"]

    if mode in MODE_SURFACE_REQUIRED and not surface:
        findings.append(
            {
                "code": "active_surface_required",
                "severity": "error",
                "message": f"{mode} mode requires a concrete active manuscript surface.",
            }
        )

    required = set(payload["context"]["required_contracts"])
    loaded = set(payload["context"]["loaded_contracts"])
    missing = sorted(required - loaded)
    if missing:
        findings.append(
            {
                "code": "required_contract_not_loaded",
                "severity": "error",
                "message": "Required contract(s) missing from current context: " + ", ".join(missing),
            }
        )

    if mode == "RELEASE" and payload.get("target") is None:
        findings.append(
            {
                "code": "release_target_unresolved",
                "severity": "error",
                "message": "RELEASE mode requires a resolved target/article-type state rather than an absent target object.",
            }
        )

    if mode == "REVIEW" and not payload["open_blockers"] and "clean-room" not in payload["primary_operation"].lower():
        findings.append(
            {
                "code": "review_scope_check",
                "severity": "review",
                "message": "REVIEW mode has no open blocker/concern rows. Confirm this is an intentional first-pass or clean-room review rather than a lost review state.",
            }
        )

    if payload["next_action"].strip().lower() == payload["stop_condition"].strip().lower():
        findings.append(
            {
                "code": "next_action_equals_stop_condition",
                "severity": "review",
                "message": "Next action and stop condition are identical; clarify what the session should do versus what ends the operation.",
            }
        )

    return _result(findings)


def _result(findings: list[dict[str, str]]) -> dict[str, Any]:
    counts = Counter(item["severity"] for item in findings)
    if counts["error"]:
        decision = "BLOCKED"
    elif counts["unresolved"]:
        decision = "UNRESOLVED"
    elif counts["review"]:
        decision = "REVIEW"
    else:
        decision = "PASS"
    return {
        "decision": decision,
        "counts": {
            "error": counts["error"],
            "unresolved": counts["unresolved"],
            "review": counts["review"],
        },
        "findings": findings,
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Validate an academic-paper AI session checkpoint.")
    p.add_argument("checkpoint", type=Path)
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--fail-on-review", action="store_true")
    return p


def main() -> int:
    args = parser().parse_args()
    payload = json.loads(args.checkpoint.read_text(encoding="utf-8"))
    result = validate(payload)
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    if result["decision"] == "BLOCKED":
        return 1
    if args.fail_on_review and result["decision"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
