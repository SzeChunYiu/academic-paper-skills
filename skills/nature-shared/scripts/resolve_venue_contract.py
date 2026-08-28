#!/usr/bin/env python3
"""Resolve a time-versioned venue decision contract without inventing policy.

The resolver selects only an exact venue + article type + stage snapshot that is
active on the requested date. Maintained snapshots are useful local knowledge;
live official-source records outrank them. If no exact contract is available,
the result is an explicitly non-exact fallback plus a live-resolution request.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT_ROOT = HERE / "journal-formats" / "decision-contracts"

TOP_LEVEL_REQUIRED = {
    "contract_schema_version",
    "contract_id",
    "venue",
    "article_type",
    "stages",
    "policy_validity",
    "provenance",
    "fallback_profile_id",
    "decision_contract",
}
DECISION_REQUIRED = {
    "acceptance_objective",
    "scientific_gates",
    "novelty_gate",
    "impact_gate",
    "breadth_gate",
    "audience_interest_gate",
    "burden_of_doubt",
    "allowed_repair_routes",
    "review_model",
    "ai_confidentiality_policy",
    "acceptance_states",
    "certification_layer",
}
STAGE_ALIASES = {
    "planning": "planning",
    "drafting": "planning",
    "pre_submission": "initial_submission",
    "presubmission": "initial_submission",
    "initial_submission": "initial_submission",
    "submission": "initial_submission",
    "peer_review": "peer_review",
    "review": "peer_review",
    "revision": "revision",
    "revisions": "revision",
    "accepted": "accepted",
    "accepted_in_principle": "accepted",
    "production": "production",
    "proof": "production",
    "post_publication": "post_publication",
}


def _token(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.casefold()).strip("_")


def _parse_date(value: str | None, field: str) -> date | None:
    if value is None:
        return None
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be YYYY-MM-DD or null: {value!r}") from exc


def normalize_stage(value: str) -> str:
    token = _token(value)
    return STAGE_ALIASES.get(token, token)


def load_contracts(path: str | Path) -> list[dict[str, Any]]:
    """Load JSON contracts from one file or all JSON files in a directory."""

    source = Path(path)
    paths = [source] if source.is_file() else sorted(source.glob("*.json"))
    contracts: list[dict[str, Any]] = []
    for contract_path in paths:
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        errors = validate_contract(contract)
        if errors:
            joined = "; ".join(errors)
            raise ValueError(f"invalid venue contract {contract_path}: {joined}")
        contracts.append(contract)
    return contracts


def load_fallback_profiles(path: str | Path | None = None) -> dict[str, Any]:
    source = Path(path) if path else DEFAULT_CONTRACT_ROOT / "fallback-profiles.json"
    payload = json.loads(source.read_text(encoding="utf-8"))
    return {profile["profile_id"]: profile for profile in payload["profiles"]}


def validate_contract(contract: dict[str, Any]) -> list[str]:
    """Return structural errors; full normative shape lives in the JSON Schema."""

    errors: list[str] = []
    missing = sorted(TOP_LEVEL_REQUIRED - contract.keys())
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))
        return errors

    decision = contract.get("decision_contract")
    if not isinstance(decision, dict):
        return ["decision_contract must be an object"]
    missing_decision = sorted(DECISION_REQUIRED - decision.keys())
    if missing_decision:
        errors.append("missing decision fields: " + ", ".join(missing_decision))

    for identity_field in ("venue", "article_type"):
        identity = contract.get(identity_field)
        if not isinstance(identity, dict) or not identity.get("id") or not identity.get("name"):
            errors.append(f"{identity_field} requires id and name")

    if not isinstance(contract.get("stages"), list) or not contract["stages"]:
        errors.append("stages must be a non-empty list")

    validity = contract.get("policy_validity", {})
    for field in ("effective_from", "effective_until", "observed_active_at", "reviewed_at"):
        try:
            _parse_date(validity.get(field), f"policy_validity.{field}")
        except ValueError as exc:
            errors.append(str(exc))
    if "effective_date_basis" not in validity:
        errors.append("policy_validity.effective_date_basis is required")

    provenance = contract.get("provenance", {})
    if provenance.get("resolution_mode") not in {
        "maintained_exact_profile",
        "live_official_resolution",
        "test_fixture",
    }:
        errors.append("provenance.resolution_mode is invalid")
    sources = provenance.get("sources")
    source_ids: set[str] = set()
    if not isinstance(sources, list) or not sources:
        errors.append("provenance.sources must be non-empty")
    else:
        for index, source in enumerate(sources):
            for key in ("source_id", "authority", "title", "url", "accessed_at", "supports"):
                if key not in source:
                    errors.append(f"provenance.sources[{index}].{key} is required")
            source_id = source.get("source_id")
            if source_id in source_ids:
                errors.append(f"duplicate source_id {source_id}")
            elif source_id:
                source_ids.add(source_id)

    def check_source_refs(value: Any, path: str = "decision_contract") -> None:
        if isinstance(value, dict):
            refs = value.get("source_refs")
            if isinstance(refs, list):
                for source_ref in refs:
                    if source_ref not in source_ids:
                        errors.append(f"{path}: unknown source_ref {source_ref}")
            for key, child in value.items():
                check_source_refs(child, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                check_source_refs(child, f"{path}[{index}]")

    check_source_refs(decision)

    objective = decision.get("acceptance_objective", {})
    if objective.get("scope") != "non_universal":
        errors.append("acceptance_objective.scope must be non_universal")

    gates = decision.get("scientific_gates")
    if not isinstance(gates, list) or not gates:
        errors.append("scientific_gates must be a non-empty list")
    else:
        for index, gate in enumerate(gates):
            for key in ("id", "observation_key", "required", "rule"):
                if key not in gate:
                    errors.append(f"scientific_gates[{index}].{key} is required")

    for gate_name in ("novelty_gate", "impact_gate", "breadth_gate", "audience_interest_gate"):
        gate = decision.get(gate_name, {})
        for key in ("required", "observation_key", "rule"):
            if key not in gate:
                errors.append(f"{gate_name}.{key} is required")

    certification = decision.get("certification_layer", {})
    if certification.get("separate_from_acceptance") is not True:
        errors.append("certification_layer.separate_from_acceptance must be true")
    return errors


def _identity_tokens(identity: dict[str, Any]) -> set[str]:
    values = [identity["id"], identity["name"], *identity.get("aliases", [])]
    return {_token(value) for value in values}


def _matches_tuple(
    contract: dict[str, Any], venue: str, article_type: str, stage: str
) -> bool:
    requested_stage = normalize_stage(stage)
    stages = {normalize_stage(value) for value in contract["stages"]}
    return (
        _token(venue) in _identity_tokens(contract["venue"])
        and _token(article_type) in _identity_tokens(contract["article_type"])
        and requested_stage in stages
    )


def _date_state(contract: dict[str, Any], as_of: date) -> str:
    validity = contract["policy_validity"]
    effective_from = _parse_date(validity.get("effective_from"), "effective_from")
    effective_until = _parse_date(validity.get("effective_until"), "effective_until")
    observed_active = _parse_date(validity.get("observed_active_at"), "observed_active_at")
    if effective_from and as_of < effective_from:
        return "future"
    if effective_until and as_of > effective_until:
        return "expired"
    # An observation made on a date cannot be back-cast as historical policy.
    if effective_from is None and observed_active and as_of < observed_active:
        return "historically_unresolved"
    return "active"


def _rank(contract: dict[str, Any]) -> tuple[int, str, str]:
    provenance = contract["provenance"]["resolution_mode"]
    live = 1 if provenance == "live_official_resolution" else 0
    validity = contract["policy_validity"]
    active_date = validity.get("effective_from") or validity.get("observed_active_at") or "0001-01-01"
    return live, active_date, validity.get("reviewed_at") or "0001-01-01"


def _resolution_certification(contract: dict[str, Any], as_of: str) -> dict[str, Any]:
    live = contract["provenance"]["resolution_mode"] == "live_official_resolution"
    return {
        "level": "live_official" if live else "maintained_snapshot",
        "tuple_verified": True,
        "as_of": as_of,
        "source_count": len(contract["provenance"]["sources"]),
        "does_not_certify": [
            "real_journal_acceptance",
            "manuscript_scientific_validity",
            "policy_before_the_supported_validity_window",
            "unstated_or_unresolved_policy",
        ],
    }


def resolve_contract(
    *,
    venue: str,
    article_type: str,
    stage: str,
    as_of: str,
    contracts: Iterable[dict[str, Any]],
    fallback_profile_id: str | None = None,
    fallback_profiles_path: str | Path | None = None,
) -> dict[str, Any]:
    """Resolve the exact tuple, or fail explicitly to a non-policy fallback."""

    as_of_date = _parse_date(as_of, "as_of")
    assert as_of_date is not None
    tuple_matches = [
        contract
        for contract in contracts
        if _matches_tuple(contract, venue, article_type, stage)
    ]
    by_state: dict[str, list[dict[str, Any]]] = {
        "active": [],
        "future": [],
        "expired": [],
        "historically_unresolved": [],
    }
    for contract in tuple_matches:
        by_state[_date_state(contract, as_of_date)].append(contract)

    if by_state["active"]:
        contract = max(by_state["active"], key=_rank)
        is_live = contract["provenance"]["resolution_mode"] == "live_official_resolution"
        return {
            "request": {
                "venue": venue,
                "article_type": article_type,
                "stage": normalize_stage(stage),
                "as_of": as_of,
            },
            "resolution_mode": "exact_live_official" if is_live else "exact_contract_snapshot",
            "contract": contract,
            "live_official_resolution_required": False,
            "live_official_resolution_recommended": not is_live,
            "not_yet_effective_contract_ids": [
                item["contract_id"] for item in by_state["future"]
            ],
            "resolution_certification": _resolution_certification(contract, as_of),
            "warnings": [
                "A maintained snapshot is not immutable truth; re-check official sources for submission-critical use."
            ]
            if not is_live
            else [],
        }

    fallbacks = load_fallback_profiles(fallback_profiles_path)
    inferred = next(
        (item.get("fallback_profile_id") for item in tuple_matches if item.get("fallback_profile_id")),
        None,
    )
    selected_id = fallback_profile_id or inferred or "generic-scholarly"
    if selected_id not in fallbacks:
        raise ValueError(f"unknown fallback profile: {selected_id}")
    fallback = dict(fallbacks[selected_id])
    fallback["profile_is_not_venue_policy"] = True
    warnings = [
        "No active exact contract supports this venue, article type, stage, and date.",
        "The fallback is a planning aid only and must not be attributed to the journal.",
    ]
    if by_state["historically_unresolved"]:
        warnings.append("The local snapshot cannot be back-cast before its observed-active date.")
    return {
        "request": {
            "venue": venue,
            "article_type": article_type,
            "stage": normalize_stage(stage),
            "as_of": as_of,
        },
        "resolution_mode": "fallback_with_live_resolution_required",
        "contract": None,
        "fallback": fallback,
        "live_official_resolution_required": True,
        "live_resolution_checklist": [
            "confirm exact venue identity and official domain",
            "confirm exact article/content type",
            "confirm current stage",
            "open current official author, editor, reviewer, ethics, AI, and confidentiality pages",
            "record page title, URL, access date, stated effective date or explicit not-stated status",
            "capture conflicts and unresolved fields without guessing",
            "materialize a schema-valid contract with provenance.resolution_mode=live_official_resolution",
        ],
        "not_yet_effective_contract_ids": [
            item["contract_id"] for item in by_state["future"]
        ],
        "expired_contract_ids": [item["contract_id"] for item in by_state["expired"]],
        "historically_unresolved_contract_ids": [
            item["contract_id"] for item in by_state["historically_unresolved"]
        ],
        "resolution_certification": {
            "level": "fallback_not_exact",
            "tuple_verified": False,
            "as_of": as_of,
            "does_not_certify": ["any_exact_journal_policy", "real_journal_acceptance"],
        },
        "warnings": warnings,
    }


def evaluate_acceptance(
    contract: dict[str, Any], observations: dict[str, Any]
) -> dict[str, Any]:
    """Evaluate stated gates only; this is not a prediction or journal decision."""

    decision = contract["decision_contract"]
    scientific_failures: list[str] = []
    target_failures: list[str] = []
    doubt_defaults: list[str] = []

    for gate in decision["scientific_gates"]:
        if gate.get("required") and observations.get(gate["observation_key"]) is not True:
            scientific_failures.append(gate["id"])

    for gate_name in ("novelty_gate", "impact_gate", "breadth_gate"):
        gate = decision[gate_name]
        if gate.get("required") and observations.get(gate["observation_key"]) is not True:
            target_failures.append(gate_name)

    interest = decision["audience_interest_gate"]
    if interest.get("required"):
        value = observations.get(interest["observation_key"])
        if value is None:
            doubt_rule = decision["burden_of_doubt"].get("overrides", {}).get(
                "audience_interest"
            )
            if doubt_rule == "assume_satisfied":
                doubt_defaults.append("audience_interest")
            else:
                target_failures.append("audience_interest_gate")
        elif value not in interest.get("accepted_values", []):
            target_failures.append("audience_interest_gate")

    states = decision["acceptance_states"]
    if scientific_failures:
        state = states["scientific_failure"]
    elif target_failures:
        state = states["target_failure"]
    else:
        state = states["criteria_satisfied"]
    return {
        "state": state,
        "objective_id": decision["acceptance_objective"]["id"],
        "objective_scope": decision["acceptance_objective"]["scope"],
        "scientific_failures": scientific_failures,
        "target_failures": target_failures,
        "doubt_defaults_applied": doubt_defaults,
        "actual_journal_decision": False,
        "certification_layer_evaluated": False,
    }


def assess_repair_route(contract: dict[str, Any], route: str) -> dict[str, Any]:
    for item in contract["decision_contract"]["allowed_repair_routes"]:
        if item["route"] == route:
            return {
                "route": route,
                "allowed": item["policy_status"] in {
                    "explicitly_allowed",
                    "conditionally_allowed",
                },
                "policy_status": item["policy_status"],
                "source_refs": item.get("source_refs", []),
                "constraint": item.get("constraint"),
            }
    return {
        "route": route,
        "allowed": False,
        "policy_status": "not_resolved",
        "source_refs": [],
        "constraint": "Absence from a contract is not evidence that the journal forbids the route.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venue", required=True)
    parser.add_argument("--article-type", required=True)
    parser.add_argument("--stage", required=True)
    parser.add_argument("--as-of", required=True)
    parser.add_argument("--contracts-dir", type=Path, default=DEFAULT_CONTRACT_ROOT / "profiles")
    parser.add_argument(
        "--live-contract",
        action="append",
        type=Path,
        default=[],
        help="Schema-valid contract materialized from a current official-source check.",
    )
    parser.add_argument("--fallback-profile")
    args = parser.parse_args(argv)

    contracts = load_contracts(args.contracts_dir)
    for live_path in args.live_contract:
        contracts.extend(load_contracts(live_path))
    result = resolve_contract(
        venue=args.venue,
        article_type=args.article_type,
        stage=args.stage,
        as_of=args.as_of,
        contracts=contracts,
        fallback_profile_id=args.fallback_profile,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
