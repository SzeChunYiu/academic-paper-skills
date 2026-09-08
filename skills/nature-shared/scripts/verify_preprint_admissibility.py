#!/usr/bin/env python3
"""Fail-closed admissibility gate for depositing a manuscript in a preprint repository.

Preprint servers are moderated venues. They decline manuscripts on *content
type* and on *format* independently of scientific quality, and a decline is
expensive: arXiv's computer-science practice for review and position papers
tells rejected authors they may not simply resubmit, and that an appeal is
entertained only once peer review has completed elsewhere. A pipeline that
treats deposit as an upload step rather than as a gated venue has no place to
catch that, which is exactly how a manuscript reaches a moderator carrying a
label that decides its fate.

This gate answers one question: **would this deposit be refused for what it is,
rather than for what it says?**

Design commitments
------------------
*Policy is data, not code.* Every rule comes from a versioned rules file
carrying a source URL, a retrieval date and the operative quotation. The
verifier itself asserts no policy. When the rules file is older than a declared
staleness horizon the gate refuses to certify rather than applying rules that
may have moved.

*Evidence, not vocabulary.* Content type arrives from
``detect_manuscript_content_type.py``, which reads what the manuscript displays.
A rule of this kind must fire on positive evidence that a manuscript IS a
review or position piece, never on a manuscript's failure to prove it is not.

*Relabelling is not a remedy.* Where the declared label overstates the content,
the gate says so and refuses to offer a wording fix. The manuscript changes or
the route changes.

*Not a prediction.* A PASS means no rule in the ruleset is triggered by the
evidence supplied. It is not a forecast of a moderator's decision, and it
confers no authority.

Exit codes
    0  PASS            no rule triggered on the evidence supplied
    1  BLOCK           at least one rule triggered
    2  CANNOT_EVALUATE missing inputs, unreadable rules, or stale policy

Exit 2 is distinct on purpose. A deposit the gate could not assess must never
be recorded as a deposit the gate assessed and cleared.
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "preprint.admissibility-verdict.v1"
RULES_SCHEMA = "preprint.repository-admissibility-rules.v1"
DECLARATION_SCHEMA = "preprint.deposit-declaration.v1"

# A ruleset older than this is refused rather than trusted. Repository practice
# changed substantively in October 2025 with no migration period, and a gate
# quietly applying superseded rules is worse than no gate.
DEFAULT_MAX_POLICY_AGE_DAYS = 120

SYNTHESIS_CONTENT_TYPES = {
    "review",
    "survey",
    "position",
    "perspective",
    "programme",
}


def _fail(msg: str, code: int = 2) -> int:
    print(json.dumps({"verdict": "CANNOT_EVALUATE", "error": msg}, indent=2))
    return code


def _load_json(path: Path, label: str) -> Any:
    if not path.is_file():
        raise FileNotFoundError("%s not found: %s" % (label, path))
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError("%s is not valid JSON: %s" % (label, exc)) from exc


def _parse_date(value: str, field: str) -> datetime.date:
    try:
        return datetime.date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("%s must be an ISO date, got %r" % (field, value)) from exc


def archive_of(category: str) -> str:
    """Return the top-level archive of a category: 'cs.AI' -> 'cs'."""
    return (category or "").split(".", 1)[0].strip().lower()


def rule_applies(rule: dict[str, Any], primary: str, cross_list: list[str]) -> bool:
    """Does this rule's scope cover the declared categories?

    Cross-lists are included deliberately. Choosing a non-cs primary for a
    manuscript whose real home is cs, while cross-listing it into cs, does not
    escape a cs practice; it also is not something this gate will help anyone
    do, because the same rule is evaluated against the cross-list.
    """
    scope = rule.get("applies_to", {})
    archives = [a.lower() for a in scope.get("archives", [])]
    if not archives:
        return False

    categories = [primary] + list(cross_list)
    for cat in categories:
        cat_l = (cat or "").strip().lower()
        if not cat_l:
            continue
        # An excluded category wins over the archive match.
        if cat_l in [e.lower() for e in rule.get("excludes", {}).get("categories", [])]:
            continue
        if archive_of(cat_l) in archives or cat_l in archives:
            return True
    return False


def evaluate(
    rules_doc: dict[str, Any],
    declaration: dict[str, Any],
    detection: dict[str, Any] | None,
    as_of: datetime.date,
    max_age_days: int,
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    blocked = False
    unevaluable: list[str] = []

    policy_as_of = _parse_date(rules_doc.get("policy_as_of", ""), "policy_as_of")
    age = (as_of - policy_as_of).days
    if age > max_age_days:
        unevaluable.append(
            "ruleset for %s is %d days old (limit %d); re-verify the live policy "
            "before depositing" % (rules_doc.get("repository"), age, max_age_days)
        )

    primary = declaration.get("primary_category") or ""
    cross_list = declaration.get("cross_list") or []
    if not primary or primary.upper().startswith("AUTHOR_TO_SET"):
        unevaluable.append(
            "primary_category is unset; category is what decides whether an "
            "archive-scoped rule applies at all, so nothing can be checked without it"
        )

    # Content type: the author declares it, and the detector corroborates or
    # contradicts. Disagreement is itself reportable.
    declared_type = (declaration.get("declared_content_type") or "").strip().lower()
    detected_indicators: list[str] = []
    detected_declared: str | None = None
    mismatch = None
    if detection:
        detected_indicators = detection.get("synthesis_indicators", []) or []
        detected_declared = (detection.get("declared", {}) or {}).get("type")
        mismatch = detection.get("mismatch")
    else:
        unevaluable.append(
            "no content-type detection supplied; run detect_manuscript_content_type.py "
            "and pass it with --detection"
        )

    if not declared_type:
        unevaluable.append(
            "declared_content_type is unset; the gate will not infer the author's "
            "own claim about what the manuscript is"
        )

    # The effective content type errs toward the synthesis reading whenever
    # either the author or the evidence says so, because that is the reading a
    # moderator can act on.
    effective_types = set()
    if declared_type:
        effective_types.add(declared_type)
    if detected_declared:
        effective_types.add(detected_declared)
    synthesis_evidence = bool(detected_indicators)

    for idx, rule in enumerate(rules_doc.get("rules", [])):
        rid = rule.get("id", "rule[%d]" % idx)
        if not rule_applies(rule, primary, cross_list):
            continue
        triggers = {t.lower() for t in rule.get("triggers_on_content_types", [])}
        hit_types = sorted(effective_types & triggers)
        triggered = bool(hit_types) or (
            synthesis_evidence and bool(triggers & SYNTHESIS_CONTENT_TYPES)
        )
        if not triggered:
            continue

        satisfied = []
        missing = []
        for req in rule.get("requires", []):
            if declaration.get(req):
                satisfied.append(req)
            else:
                missing.append(req)

        finding = {
            "rule_id": rid,
            "repository": rules_doc.get("repository"),
            "matched_categories": [primary] + list(cross_list),
            "matched_content_types": hit_types,
            "matched_evidence": detected_indicators,
            "requirements_satisfied": satisfied,
            "requirements_missing": missing,
            "consequence": rule.get("consequence"),
            "source": (rules_doc.get("sources") or [{}])[rule.get("source_ref", 0)]
            if rules_doc.get("sources")
            else None,
        }
        if missing and rule.get("effect", "BLOCK").upper() == "BLOCK":
            blocked = True
            finding["verdict"] = "BLOCK"
        else:
            finding["verdict"] = "SATISFIED"
        findings.append(finding)

    integrity: list[str] = []
    if mismatch == "LABEL_OVERSTATES_CONTENT":
        blocked = True
        integrity.append(
            "The manuscript displays no primary research while nothing declares it a "
            "review or position piece. Changing the label is not an available remedy. "
            "Either the manuscript gains primary research, or the route changes to one "
            "that accepts synthesis."
        )
    if mismatch == "LABEL_UNDERSTATES_CONTENT":
        integrity.append(
            "The manuscript displays primary research while its declared surfaces call "
            "it a review or position piece. Correcting the declared label to match the "
            "body is legitimate and makes the submission more accurate."
        )
    if detection and detection.get("structural", {}).get(
        "negation_conflicts_with_structure"
    ):
        integrity.append(
            "A statement in the manuscript denies reporting primary research while the "
            "body displays it. One of the two is wrong, and a moderator reads the "
            "statement. Resolve before depositing."
        )

    if unevaluable:
        verdict = "CANNOT_EVALUATE"
    elif blocked:
        verdict = "BLOCK"
    else:
        verdict = "PASS"

    return {
        "schema_version": SCHEMA_VERSION,
        "verdict": verdict,
        "repository": rules_doc.get("repository"),
        "policy_as_of": rules_doc.get("policy_as_of"),
        "policy_age_days": age,
        "evaluated_on": as_of.isoformat(),
        "declared": {
            "primary_category": primary,
            "cross_list": cross_list,
            "declared_content_type": declared_type or None,
            "peer_review_doi": declaration.get("peer_review_doi"),
        },
        "rules_evaluated": len(rules_doc.get("rules", [])),
        "findings": findings,
        "integrity_notes": integrity,
        "not_evaluable_because": unevaluable,
        "meaning": (
            "PASS means no rule in this ruleset was triggered by the evidence supplied. "
            "It is not a prediction of a moderation decision and confers no authority."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rules", required=True, help="repository admissibility rules JSON")
    ap.add_argument("--declaration", required=True, help="deposit declaration JSON")
    ap.add_argument("--detection", default=None, help="detect_manuscript_content_type.py output")
    ap.add_argument("--as-of", default=None, help="evaluation date (ISO); defaults to today")
    ap.add_argument("--max-policy-age-days", type=int, default=DEFAULT_MAX_POLICY_AGE_DAYS)
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args(argv)

    try:
        rules_doc = _load_json(Path(args.rules), "rules")
        declaration = _load_json(Path(args.declaration), "declaration")
        detection = _load_json(Path(args.detection), "detection") if args.detection else None
    except (FileNotFoundError, ValueError) as exc:
        return _fail(str(exc))

    if rules_doc.get("schema_version") != RULES_SCHEMA:
        return _fail(
            "rules schema_version must be %r, got %r"
            % (RULES_SCHEMA, rules_doc.get("schema_version"))
        )
    if declaration.get("schema_version") != DECLARATION_SCHEMA:
        return _fail(
            "declaration schema_version must be %r, got %r"
            % (DECLARATION_SCHEMA, declaration.get("schema_version"))
        )
    if not rules_doc.get("sources"):
        return _fail("rules file carries no sources; policy without a citation is not usable")

    try:
        as_of = (
            _parse_date(args.as_of, "--as-of") if args.as_of else datetime.date.today()
        )
        result = evaluate(
            rules_doc, declaration, detection, as_of, args.max_policy_age_days
        )
    except ValueError as exc:
        return _fail(str(exc))

    payload = json.dumps(result, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return {"PASS": 0, "BLOCK": 1, "CANNOT_EVALUATE": 2}[result["verdict"]]


if __name__ == "__main__":
    raise SystemExit(main())
