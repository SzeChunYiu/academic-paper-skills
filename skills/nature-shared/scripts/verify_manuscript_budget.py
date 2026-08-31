#!/usr/bin/env python3
"""Validate a venue-constrained manuscript budget ledger.

The verifier is intentionally conservative. It does not invent section budgets
or convert words to pages. It checks the budget decisions already resolved by
the writing pipeline and fails closed when a binding target measurement is
missing or a central section is explicitly marked underdeveloped.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


REQUIRED_TOP = ("schema_version", "manuscript_id", "target", "constraints", "sections", "reserve", "release")
POST_PLANNING_STAGES = {"initial_submission", "peer_review", "revision", "accepted", "production"}
CENTRAL_PRIORITIES = {"P0", "P1", "P2", "P3"}


def finding(code: str, severity: str, message: str, pointer: str | None = None) -> dict[str, Any]:
    return {"code": code, "severity": severity, "message": message, "pointer": pointer}


def validate(ledger: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []

    for key in REQUIRED_TOP:
        if key not in ledger:
            findings.append(finding("missing_top_level", "error", f"Missing required top-level field: {key}", key))

    if findings:
        return summarize(findings, ledger)

    if ledger.get("schema_version") != "1.0.0":
        findings.append(finding("unsupported_schema_version", "error", "schema_version must be 1.0.0", "schema_version"))

    target = ledger.get("target") or {}
    stage = target.get("stage")
    budget_basis = target.get("budget_basis")
    if stage not in {"planning", "initial_submission", "peer_review", "revision", "accepted", "production"}:
        findings.append(finding("invalid_stage", "error", f"Unsupported target stage: {stage}", "target.stage"))
    if budget_basis not in {"words", "pages", "mixed", "advisory_length"}:
        findings.append(finding("invalid_budget_basis", "error", f"Unsupported budget_basis: {budget_basis}", "target.budget_basis"))

    constraints = ledger.get("constraints") or []
    seen_constraints: set[str] = set()
    has_hard_constraint = False
    has_measured_page_constraint = False
    has_unmeasured_page_constraint = False

    for index, item in enumerate(constraints):
        ptr = f"constraints[{index}]"
        cid = str(item.get("constraint_id") or "")
        if not cid:
            findings.append(finding("missing_constraint_id", "error", "Constraint is missing constraint_id", ptr))
        elif cid in seen_constraints:
            findings.append(finding("duplicate_constraint_id", "error", f"Duplicate constraint_id: {cid}", ptr))
        else:
            seen_constraints.add(cid)

        strength = item.get("strength")
        unit = item.get("unit")
        limit = item.get("limit")
        actual = item.get("actual")
        status = item.get("status")

        if strength == "hard":
            has_hard_constraint = True
            if limit is None:
                findings.append(finding("hard_limit_missing", "error", "Hard constraint requires a numeric limit", ptr))
            if unit == "pages":
                if actual is None:
                    has_unmeasured_page_constraint = True
                else:
                    has_measured_page_constraint = True
            if actual is None:
                severity = "unresolved" if stage in POST_PLANNING_STAGES else "review"
                findings.append(
                    finding(
                        "hard_constraint_unmeasured",
                        severity,
                        f"Hard {unit} constraint is not measured for surface {item.get('surface')}",
                        ptr,
                    )
                )
            elif limit is not None and actual > limit:
                findings.append(
                    finding(
                        "hard_limit_exceeded",
                        "error",
                        f"{item.get('surface')} uses {actual:g} {unit}, exceeding hard limit {limit:g}",
                        ptr,
                    )
                )
            elif limit is not None and status == "over":
                findings.append(finding("constraint_status_inconsistent", "error", "Constraint status says over although actual does not exceed limit", ptr))
        elif strength == "guideline":
            if limit is None:
                findings.append(finding("guideline_limit_missing", "error", "Guideline constraint requires a numeric guideline value", ptr))
            elif actual is not None and actual > limit:
                findings.append(
                    finding(
                        "guideline_exceeded",
                        "review",
                        f"{item.get('surface')} uses {actual:g} {unit}, above guideline {limit:g}; justify or reallocate",
                        ptr,
                    )
                )
        elif strength == "none_stated":
            if limit is not None:
                findings.append(finding("invented_unstated_limit", "error", "none_stated constraint must not contain an invented numeric limit", ptr))
        else:
            findings.append(finding("invalid_constraint_strength", "error", f"Unsupported constraint strength: {strength}", ptr))

        if status == "unresolved_rule":
            findings.append(finding("target_rule_unresolved", "unresolved", "Target count rule remains unresolved", ptr))
        elif status == "unmeasured" and strength == "hard" and stage in POST_PLANNING_STAGES:
            findings.append(finding("binding_measurement_missing", "unresolved", "Binding target surface remains unmeasured", ptr))

    if budget_basis in {"pages", "mixed"} and stage in POST_PLANNING_STAGES and has_hard_constraint:
        page_hard = [c for c in constraints if c.get("strength") == "hard" and c.get("unit") == "pages"]
        if page_hard and not has_measured_page_constraint:
            findings.append(
                finding(
                    "rendered_page_measurement_required",
                    "unresolved",
                    "Page-constrained target requires a rendered page measurement; word counts are not a substitute",
                    "constraints",
                )
            )
        if page_hard and has_unmeasured_page_constraint:
            findings.append(
                finding(
                    "page_constraint_partially_unmeasured",
                    "unresolved",
                    "At least one hard page constraint remains unmeasured",
                    "constraints",
                )
            )

    sections = ledger.get("sections") or []
    seen_sections: set[str] = set()
    for index, section in enumerate(sections):
        ptr = f"sections[{index}]"
        sid = str(section.get("section_id") or "")
        if not sid:
            findings.append(finding("missing_section_id", "error", "Section budget row is missing section_id", ptr))
        elif sid in seen_sections:
            findings.append(finding("duplicate_section_id", "error", f"Duplicate section_id: {sid}", ptr))
        else:
            seen_sections.add(sid)

        soft_min = section.get("soft_min")
        soft_max = section.get("soft_max")
        actual = section.get("actual")
        status = section.get("status")
        priority = section.get("priority")
        unit = section.get("unit")

        if soft_min is not None and soft_max is not None and soft_min > soft_max:
            findings.append(finding("invalid_soft_range", "error", "soft_min cannot exceed soft_max", ptr))

        if actual is not None and unit != "not_measured":
            if soft_min is not None and actual < soft_min:
                findings.append(
                    finding(
                        "below_soft_budget",
                        "review",
                        f"Section {section.get('title')} is below its manuscript-specific soft allocation; check functional sufficiency rather than padding",
                        ptr,
                    )
                )
            if soft_max is not None and actual > soft_max:
                findings.append(
                    finding(
                        "above_soft_budget",
                        "review",
                        f"Section {section.get('title')} is above its manuscript-specific soft allocation; justify the displaced space or reallocate",
                        ptr,
                    )
                )

        if status == "underdeveloped":
            severity = "error" if priority in CENTRAL_PRIORITIES else "review"
            findings.append(
                finding(
                    "section_underdeveloped",
                    severity,
                    f"Section {section.get('title')} is explicitly underdeveloped at priority {priority}",
                    ptr,
                )
            )
        elif status == "over_limit":
            findings.append(finding("section_over_limit", "error", f"Section {section.get('title')} is over a binding limit", ptr))
        elif status in {"overweight", "reallocate"}:
            findings.append(
                finding(
                    "section_reallocation_needed",
                    "review",
                    f"Section {section.get('title')} is marked {status}; confirm its scientific value justifies the opportunity cost",
                    ptr,
                )
            )
        elif status == "needs_render_measurement":
            severity = "unresolved" if stage in POST_PLANNING_STAGES else "review"
            findings.append(finding("section_render_measurement_needed", severity, f"Section {section.get('title')} still needs rendered-space measurement", ptr))
        elif status == "unresolved_target_rule":
            findings.append(finding("section_target_rule_unresolved", "unresolved", f"Target allocation rule is unresolved for section {section.get('title')}", ptr))
        elif status != "within_budget":
            findings.append(finding("invalid_section_status", "error", f"Unsupported section status: {status}", ptr))

    reserve = ledger.get("reserve") or {}
    reserve_actual = reserve.get("actual")
    reserve_planned = reserve.get("planned")
    expected_revision = bool(reserve.get("expected_revision"))
    if reserve_actual is not None and reserve_actual < 0:
        findings.append(finding("negative_reserve", "error", "Budget reserve cannot be negative", "reserve.actual"))
    if reserve_planned is not None and reserve_actual is not None and reserve_actual < reserve_planned:
        findings.append(finding("reserve_below_plan", "review", "Remaining reserve is below the manuscript-specific planned reserve", "reserve"))
    if expected_revision and has_hard_constraint and reserve_actual == 0:
        findings.append(
            finding(
                "zero_revision_reserve",
                "review",
                "Hard-constrained manuscript has zero reserve while substantive revision is still expected; every addition now requires explicit reallocation",
                "reserve",
            )
        )
    if expected_revision and has_hard_constraint and reserve_actual is None:
        findings.append(finding("reserve_unmeasured", "review", "Revision reserve is not measured for a hard-constrained manuscript", "reserve"))

    computed = decision(findings)
    recorded = (ledger.get("release") or {}).get("decision")
    if recorded and recorded != computed:
        findings.append(
            finding(
                "stale_release_decision",
                "error",
                f"Recorded release decision {recorded} does not match computed decision {computed}",
                "release.decision",
            )
        )
        computed = decision(findings)

    return summarize(findings, ledger, forced_decision=computed)


def decision(findings: list[dict[str, Any]]) -> str:
    severities = {item["severity"] for item in findings}
    if "error" in severities:
        return "BLOCKED"
    if "unresolved" in severities:
        return "UNRESOLVED"
    if "review" in severities:
        return "REVIEW"
    return "PASS"


def summarize(
    findings: list[dict[str, Any]], ledger: dict[str, Any], forced_decision: str | None = None
) -> dict[str, Any]:
    counts = Counter(item["severity"] for item in findings)
    return {
        "decision": forced_decision or decision(findings),
        "counts": {
            "error": counts["error"],
            "unresolved": counts["unresolved"],
            "review": counts["review"],
        },
        "target": ledger.get("target"),
        "findings": findings,
        "notes": [
            "Soft section ranges are manuscript-specific planning constraints, not universal section quotas.",
            "Page-constrained targets require rendered measurement; the verifier never converts words to pages.",
            "A central section explicitly marked underdeveloped blocks readiness even when total length is compliant.",
        ],
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Validate a venue-constrained manuscript budget ledger.")
    p.add_argument("ledger", type=Path)
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--report", type=Path)
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 2

    payload = validate(ledger)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if payload["decision"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
