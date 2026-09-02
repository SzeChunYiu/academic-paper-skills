#!/usr/bin/env python3
"""Structurally validate an academic-paper project-state YAML instance."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent
SHARED_DIR = SCRIPTS_DIR.parent
DEFAULT_SCHEMA = SHARED_DIR / "project-contracts" / "academic-paper-project-state.schema.json"

EXIT_OK = 0
EXIT_DEFECT = 1
EXIT_CANNOT_CHECK = 2


def load_schema(schema_path: Path) -> dict:
    return json.loads(schema_path.read_text(encoding="utf-8"))


def load_state(state_path: Path) -> tuple[dict | None, str | None]:
    """Load a YAML project-state file.

    Returns (document, error). A YAML parse error or a non-mapping document is
    a defect in the artifact itself, not a cannot-check condition.
    """
    try:
        text = state_path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, f"cannot read state file: {exc}"
    try:
        doc = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        return None, f"YAML parse error: {exc}"
    if not isinstance(doc, dict):
        return None, f"state file must contain a YAML mapping, got {type(doc).__name__}"
    return doc, None


def canonical_pointer(path: list[Any]) -> str:
    """Render an error location as a JSON pointer (RFC 6901)."""
    parts: list[str] = []
    for item in path:
        parts.append(str(item).replace("~", "~0").replace("/", "~1"))
    return "/" + "/".join(parts)


def iter_validation_errors(doc: dict, schema: dict) -> list[dict]:
    import jsonschema

    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path)):
        errors.append(
            {
                "path": canonical_pointer(list(error.absolute_path)),
                "schema_path": canonical_pointer(list(error.absolute_schema_path)),
                "message": error.message,
            }
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", type=Path, help="project-state YAML file to validate")
    parser.add_argument(
        "--schema",
        type=Path,
        default=DEFAULT_SCHEMA,
        help=f"structural schema (default: {DEFAULT_SCHEMA.name} beside the contract dir)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit a machine-readable result object instead of human prose",
    )
    args = parser.parse_args()

    if not args.state.is_file():
        report = {
            "status": "cannot_check",
            "reason": "missing_input",
            "state": str(args.state),
        }
    else:
        doc, load_error = load_state(args.state)
        if load_error and "cannot read" in load_error:
            report = {
                "status": "cannot_check",
                "reason": "unreadable_input",
                "state": str(args.state),
                "detail": load_error,
            }
        elif load_error:
            report = {
                "status": "invalid",
                "state": str(args.state),
                "error_count": 1,
                "errors": [{"path": "", "schema_path": "", "message": load_error}],
            }
        else:
            try:
                schema = load_schema(args.schema)
            except (OSError, json.JSONDecodeError) as exc:
                report = {
                    "status": "cannot_check",
                    "reason": "unreadable_schema",
                    "schema": str(args.schema),
                    "detail": str(exc),
                }
            else:
                errors = iter_validation_errors(doc, schema)
                report = {
                    "status": "valid" if not errors else "invalid",
                    "state": str(args.state),
                    "schema": str(args.schema),
                    "error_count": len(errors),
                    "errors": errors,
                }

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=False))
    else:
        status = report["status"]
        if status == "cannot_check":
            print(f"CANNOT-CHECK {report['state']}: {report['reason']} ({report.get('detail', '')})")
        elif status == "valid":
            print(f"VALID {report['state']} against {report.get('schema', 'schema')}")
        else:
            print(f"INVALID {report['state']}: {report['error_count']} structural error(s)")
            for error in report["errors"][:20]:
                print(f"  {error['path'] or '<root>'}: {error['message']}")
            if report["error_count"] > 20:
                print(f"  ... and {report['error_count'] - 20} more")

    if report["status"] == "valid":
        return EXIT_OK
    if report["status"] == "invalid":
        return EXIT_DEFECT
    return EXIT_CANNOT_CHECK


if __name__ == "__main__":
    sys.exit(main())
