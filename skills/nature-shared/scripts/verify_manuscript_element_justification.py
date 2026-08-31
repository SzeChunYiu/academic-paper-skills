#!/usr/bin/env python3
"""Validate a manuscript element-justification ledger.

The verifier checks structural completeness of hierarchical justification,
parent links, functional roles, placement/status consistency, redundancy signals,
and final-stage coverage declarations. It does not decide whether prose is good
or whether a scientific argument is true; those remain scholarly judgments.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


VALID_STAGES = {"planning", "draft", "review", "final", "production"}
FINAL_STAGES = {"final", "production"}
RETAINED = {"keep", "compress", "merge", "move", "replace", "unresolved"}
VALID_STATUS = RETAINED | {"delete"}
VALID_COVERAGE = {"targeted", "all_sections", "all_paragraphs", "all_sentences", "full_manuscript_mixed"}
SCAFFOLDING_FUNCTIONS = {"orient", "define", "connect", "navigate", "reproduce", "comply"}


def finding(code: str, severity: str, message: str, pointer: str | None = None) -> dict[str, Any]:
    return {"code": code, "severity": severity, "message": message, "pointer": pointer}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _decision(findings: list[dict[str, Any]]) -> str:
    severities = {item["severity"] for item in findings}
    if "error" in severities:
        return "BLOCKED"
    if "unresolved" in severities:
        return "UNRESOLVED"
    if "review" in severities:
        return "REVIEW"
    return "PASS"


def _has_cycle(parent_of: dict[str, str | None]) -> str | None:
    for start in parent_of:
        seen: set[str] = set()
        current: str | None = start
        while current is not None:
            if current in seen:
                return current
            seen.add(current)
            current = parent_of.get(current)
    return None


def validate(ledger: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    required_top = ("schema_version", "manuscript_id", "stage", "scope", "elements", "release")
    for key in required_top:
        if key not in ledger:
            findings.append(finding("missing_top_level", "error", f"Missing required field: {key}", key))
    if findings:
        return summarize(findings, ledger)

    if ledger.get("schema_version") != "1.0.0":
        findings.append(finding("unsupported_schema_version", "error", "schema_version must be 1.0.0", "schema_version"))

    stage = ledger.get("stage")
    if stage not in VALID_STAGES:
        findings.append(finding("invalid_stage", "error", f"Unsupported stage: {stage}", "stage"))

    scope = ledger.get("scope") or {}
    coverage = scope.get("coverage")
    if coverage not in VALID_COVERAGE:
        findings.append(finding("invalid_coverage", "error", f"Unsupported coverage: {coverage}", "scope.coverage"))
    if not _nonempty(scope.get("surface")):
        findings.append(finding("scope_surface_missing", "error", "scope.surface must be non-empty", "scope.surface"))
    if stage in FINAL_STAGES and coverage in {"targeted", "all_sections"}:
        findings.append(
            finding(
                "final_paragraph_coverage_incomplete",
                "unresolved",
                "Final full-manuscript justification should declare at least all-paragraph or full-manuscript-mixed coverage; targeted/section-only review is insufficient for a universal element-justification release claim.",
                "scope.coverage",
            )
        )

    elements = ledger.get("elements") or []
    if not isinstance(elements, list) or not elements:
        findings.append(finding("elements_missing", "error", "elements must contain at least one audited element", "elements"))
        return summarize(findings, ledger)

    ids: set[str] = set()
    parent_of: dict[str, str | None] = {}
    for index, element in enumerate(elements):
        ptr = f"elements[{index}]"
        eid = str(element.get("element_id") or "").strip()
        if not eid:
            findings.append(finding("element_id_missing", "error", "element_id must be non-empty", f"{ptr}.element_id"))
            continue
        if eid in ids:
            findings.append(finding("duplicate_element_id", "error", f"Duplicate element_id: {eid}", f"{ptr}.element_id"))
        ids.add(eid)
        parent = element.get("parent_id")
        parent_of[eid] = parent if isinstance(parent, str) and parent else None

    for index, element in enumerate(elements):
        ptr = f"elements[{index}]"
        eid = str(element.get("element_id") or "").strip()
        parent = parent_of.get(eid)
        if parent is not None and parent not in ids:
            findings.append(finding("parent_missing", "error", f"Parent element {parent} is not present in the ledger", f"{ptr}.parent_id"))
        if parent == eid and eid:
            findings.append(finding("self_parent", "error", "An element cannot be its own parent", f"{ptr}.parent_id"))

        status = element.get("status")
        if status not in VALID_STATUS:
            findings.append(finding("invalid_element_status", "error", f"Unsupported status: {status}", f"{ptr}.status"))

        functions = element.get("functions")
        if not isinstance(functions, list):
            findings.append(finding("functions_invalid", "error", "functions must be a list", f"{ptr}.functions"))
            functions = []
        if status in RETAINED and not functions:
            findings.append(finding("retained_without_function", "error", "Retained element must perform at least one declared function", f"{ptr}.functions"))

        for key in (
            "location",
            "reader_question",
            "incoming_dependency",
            "contribution",
            "outgoing_dependency",
            "deletion_consequence",
            "placement_reason",
            "representation_reason",
        ):
            if status in RETAINED and not _nonempty(element.get(key)):
                findings.append(finding("retained_reason_missing", "error", f"Retained element requires non-empty {key}", f"{ptr}.{key}"))

        redundancy = element.get("redundancy") or {}
        redundancy_status = redundancy.get("status")
        redundancy_reason = redundancy.get("reason")
        if redundancy_status not in {"unique", "partially_redundant", "redundant", "unresolved"}:
            findings.append(finding("invalid_redundancy_status", "error", f"Unsupported redundancy status: {redundancy_status}", f"{ptr}.redundancy.status"))
        if not _nonempty(redundancy_reason):
            findings.append(finding("redundancy_reason_missing", "error", "Redundancy audit requires a reason", f"{ptr}.redundancy.reason"))
        if status == "keep" and redundancy_status == "redundant":
            findings.append(finding("redundant_element_kept", "review", "Element is marked redundant but retained unchanged; merge/delete or justify a distinct function", ptr))
        if status == "unresolved" or redundancy_status == "unresolved":
            severity = "unresolved" if element.get("importance") in {"central", "mandatory"} or stage in FINAL_STAGES else "review"
            findings.append(finding("element_justification_unresolved", severity, "Element justification remains unresolved", ptr))

        placement = element.get("placement")
        if status == "delete" and placement != "omit":
            findings.append(finding("deleted_element_destination", "review", "Deleted element should normally have placement=omit; use move/replace when the content survives elsewhere", f"{ptr}.placement"))
        if status in RETAINED and placement == "omit":
            findings.append(finding("retained_element_omitted", "error", "Retained element cannot have placement=omit", f"{ptr}.placement"))

        protected_by = element.get("protected_by") or []
        if status == "delete" and protected_by:
            findings.append(
                finding(
                    "protected_element_deleted",
                    "error",
                    "Element marked for deletion is protected by a scientific/reporting/reproducibility/compliance requirement",
                    f"{ptr}.protected_by",
                )
            )

        state = element.get("reader_state")
        if state:
            before = state.get("before")
            after = state.get("after")
            remaining = state.get("remaining_uncertainty")
            for key, value in (("before", before), ("after", after), ("remaining_uncertainty", remaining)):
                if not _nonempty(value):
                    findings.append(finding("reader_state_incomplete", "error", f"reader_state.{key} must be non-empty", f"{ptr}.reader_state.{key}"))
            if status == "keep" and before == after and not (set(functions) & SCAFFOLDING_FUNCTIONS):
                findings.append(
                    finding(
                        "no_reader_state_change",
                        "review",
                        "Kept element records no reader-state change and no explicit scaffolding/reproducibility/compliance function; test deletion/compression.",
                        f"{ptr}.reader_state",
                    )
                )

        if element.get("importance") == "central" and status == "delete":
            findings.append(finding("central_element_deleted", "review", "A central element is marked delete; confirm the central function is preserved elsewhere rather than lost", ptr))

    cycle = _has_cycle(parent_of)
    if cycle is not None:
        findings.append(finding("parent_cycle", "error", f"Parent hierarchy contains a cycle involving {cycle}", "elements"))

    computed = _decision(findings)
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
        computed = _decision(findings)

    return summarize(findings, ledger, forced_decision=computed)


def summarize(findings: list[dict[str, Any]], ledger: dict[str, Any], forced_decision: str | None = None) -> dict[str, Any]:
    counts = Counter(item["severity"] for item in findings)
    return {
        "decision": forced_decision or _decision(findings),
        "counts": {
            "error": counts["error"],
            "unresolved": counts["unresolved"],
            "review": counts["review"],
        },
        "manuscript_id": ledger.get("manuscript_id"),
        "stage": ledger.get("stage"),
        "scope": ledger.get("scope"),
        "findings": findings,
        "notes": [
            "Element justification is hierarchical: a sentence cannot rescue an unnecessary paragraph, and a useful paragraph cannot rescue an unnecessary section.",
            "The invariant applies universally, but audit granularity should be proportional to scientific/rhetorical risk rather than creating clause-level bureaucracy everywhere.",
            "A passing ledger verifies decision completeness, not manuscript quality or scientific truth.",
        ],
    }


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Validate a manuscript element-justification ledger.")
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
