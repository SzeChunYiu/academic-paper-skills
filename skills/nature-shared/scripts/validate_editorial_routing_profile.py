#!/usr/bin/env python3
"""Validate a target-specific editorial-routing profile.

This validator checks bounded professional routing semantics. It does not rank
editors, predict acceptance, or infer private editorial preferences.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import jsonschema


HERE = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = HERE / "editorial-contracts" / "editorial-routing-profile.schema.json"

PROHIBITED_KEYS = {
    "acceptance_probability",
    "acceptance_rate",
    "leniency",
    "leniency_score",
    "harshness",
    "personality",
    "political_views",
    "religion",
    "demographic_targeting",
    "citation_preference",
    "friendliness_score",
    "favorable_editor_score",
    "reviewer_friendliness",
}


def _walk_keys(value: Any, path: str = "$") -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            found.append((key, child_path))
            found.extend(_walk_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(_walk_keys(child, f"{path}[{index}]"))
    return found


def _permission_errors(profile: dict[str, Any], field: str) -> list[str]:
    policy = profile.get(field, {})
    state = policy.get("state")
    source_url = policy.get("source_url")
    if state in {"permitted", "not_permitted"} and not source_url:
        return [f"{field}.source_url: resolved permission state requires a current policy source"]
    return []


def validate_profile(profile: dict[str, Any], schema_path: Path = DEFAULT_SCHEMA) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = [
        f"{'.'.join(str(p) for p in error.path) or '$'}: {error.message}"
        for error in sorted(validator.iter_errors(profile), key=lambda item: list(item.path))
    ]

    for key, path in _walk_keys(profile):
        if key.lower() in PROHIBITED_KEYS:
            errors.append(f"{path}: prohibited editor-targeting field")

    errors.extend(_permission_errors(profile, "suggestion_policy"))
    errors.extend(_permission_errors(profile, "exclusion_policy"))

    suggestion_state = profile.get("suggestion_policy", {}).get("state")
    exclusion_state = profile.get("exclusion_policy", {}).get("state")

    sources = profile.get("editor_sources", [])
    source_urls = {source.get("url") for source in sources}
    has_official_editor_source = any(
        source.get("official")
        and source.get("source_type") in {"official_editor_page", "official_board_page"}
        for source in sources
    )

    for index, candidate in enumerate(profile.get("candidates", [])):
        intended = candidate.get("intended_use")
        conflict = candidate.get("conflict_status")

        if intended == "suggest_if_permitted" and suggestion_state != "permitted":
            errors.append(
                f"candidates.{index}.intended_use: editor suggestion is not permitted by the resolved target policy"
            )
        if intended == "suggest_if_permitted" and conflict != "clear":
            errors.append(
                f"candidates.{index}.conflict_status: only conflict-clear candidates may be suggested"
            )
        if intended == "exclude_if_permitted" and exclusion_state != "permitted":
            errors.append(
                f"candidates.{index}.intended_use: editor exclusion is not permitted by the resolved target policy"
            )
        if intended == "exclude_if_permitted" and conflict not in {"possible_conflict", "conflict"}:
            errors.append(
                f"candidates.{index}.intended_use: exclusion needs a conflict-based rationale"
            )
        if candidate.get("routing_fit") == "conflict" and intended == "suggest_if_permitted":
            errors.append(
                f"candidates.{index}: conflicted editor cannot be a suggestion candidate"
            )

        candidate_sources = set(candidate.get("source_urls", []))
        unknown_sources = sorted(candidate_sources - source_urls)
        if unknown_sources:
            errors.append(
                f"candidates.{index}.source_urls: candidate cites sources not present in editor_sources: "
                + ", ".join(unknown_sources)
            )

    if profile.get("candidates") and not has_official_editor_source:
        errors.append(
            "editor_sources: named editor candidates require an official editor or editorial-board source"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    errors = validate_profile(profile, args.schema)
    if errors:
        print("Editorial routing profile validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Editorial routing profile validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
