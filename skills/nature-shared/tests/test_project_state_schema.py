from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

SHARED = Path(__file__).parents[1]
ROOT = SHARED.parents[1]
SCHEMA_PATH = SHARED / "project-contracts" / "academic-paper-project-state.schema.json"
TEMPLATE_PATH = ROOT / "docs" / "academic-paper-project-state.template.yaml"
VALIDATOR_PATH = SHARED / "scripts" / "validate_project_state.py"
MUTATIONS_PATH = (
    Path(__file__).parent / "fixtures" / "project-state" / "invalid-mutations.json"
)


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_project_state", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import validator from {VALIDATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run_cli(argv: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), *[str(a) for a in argv]],
        capture_output=True,
        text=True,
    )


def apply_mutation(doc: dict, mutation: dict) -> dict:
    node = doc
    for key in mutation["path"][:-1]:
        node = node[key]
    if mutation["op"] == "set":
        node[mutation["path"][-1]] = mutation["value"]
    elif mutation["op"] == "del":
        del node[mutation["path"][-1]]
    else:
        raise ValueError(f"unknown op: {mutation['op']}")
    return doc


class ProjectStateSchemaTests(unittest.TestCase):
    def setUp(self) -> None:
        required = [SCHEMA_PATH, TEMPLATE_PATH, VALIDATOR_PATH, MUTATIONS_PATH]
        if self._testMethodName == "test_required_project_state_artifacts_exist":
            return
        if not all(path.exists() for path in required):
            self.skipTest("project-state enforcement artifacts not present yet")
        self.validator = load_validator()
        self.schema = self.validator.load_schema(SCHEMA_PATH)
        self.template = yaml.safe_load(TEMPLATE_PATH.read_text(encoding="utf-8"))
        self.mutations = json.loads(MUTATIONS_PATH.read_text(encoding="utf-8"))

    def test_required_project_state_artifacts_exist(self) -> None:
        for path in (SCHEMA_PATH, TEMPLATE_PATH, VALIDATOR_PATH, MUTATIONS_PATH):
            self.assertTrue(path.exists(), path)

    def test_untouched_template_validates_with_zero_errors(self) -> None:
        errors = self.validator.iter_validation_errors(self.template, self.schema)
        self.assertEqual(errors, [], "the untouched template must be structurally valid")

    def test_schema_is_draft_2020_12_and_self_checking(self) -> None:
        import jsonschema

        self.assertEqual(self.schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        jsonschema.Draft202012Validator.check_schema(self.schema)

    def test_every_invalid_mutation_fails_for_the_expected_reason(self) -> None:
        for mutation in self.mutations["mutations"]:
            with self.subTest(mutation=mutation["name"]):
                doc = apply_mutation(copy.deepcopy(self.template), mutation)
                errors = self.validator.iter_validation_errors(doc, self.schema)
                self.assertTrue(errors, "mutation must produce at least one schema error")
                matches = [
                    error
                    for error in errors
                    if error["path"] == mutation["expected_pointer"]
                    and mutation["expected_fragment"] in error["message"]
                ]
                self.assertTrue(
                    matches,
                    f"expected an error at {mutation['expected_pointer']} containing "
                    f"{mutation['expected_fragment']!r}; got "
                    f"{[(e['path'], e['message']) for e in errors]}",
                )

    def test_cli_valid_template_exits_zero(self) -> None:
        proc = run_cli([TEMPLATE_PATH, "--schema", SCHEMA_PATH])
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("VALID", proc.stdout)

    def test_cli_invalid_state_exits_one(self) -> None:
        doc = copy.deepcopy(self.template)
        doc["schema_version"] = "0.0.1"
        with tempfile.NamedTemporaryFile(
            "w", suffix=".yaml", delete=False
        ) as handle:
            yaml.safe_dump(doc, handle)
            state_path = Path(handle.name)
        try:
            proc = run_cli([state_path, "--schema", SCHEMA_PATH])
            self.assertEqual(proc.returncode, 1, proc.stdout + proc.stderr)
            self.assertIn("INVALID", proc.stdout)
        finally:
            state_path.unlink(missing_ok=True)

    def test_cli_missing_state_exits_two(self) -> None:
        proc = run_cli([ROOT / "docs" / "does-not-exist.yaml"])
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)
        self.assertIn("CANNOT-CHECK", proc.stdout)


if __name__ == "__main__":
    unittest.main()
