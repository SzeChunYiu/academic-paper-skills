# Statistical Inference and Uncertainty Engineering Implementation Plan

> **For Codex:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add an evidence-backed, non-universal statistical inference and uncertainty decision contract to the canonical paper lifecycle.

**Architecture:** A strict JSON Schema and Python resolver/evaluator enforce bounded analysis, uncertainty, and cross-surface invariants. Maintained analysis adapters add context-specific obligations; unmatched methods and exact rules remain explicit live-research tasks.

**Tech Stack:** JSON Schema 2020-12, Python 3.11 plus `jsonschema`, JSON/YAML/Markdown, `unittest`.

---

### Task 1: Freeze and reconcile the research base

**Files:**
- Create: `skills/nature-shared/research/statistical-inference-uncertainty-search-log-2026-08-28.json`
- Create: `skills/nature-shared/research/statistical-inference-uncertainty-evidence-ledger-2026-08.md`
- Create: `skills/nature-shared/analysis-contracts/statistical-inference-evidence-registry.json`

1. Execute and freeze broad bibliographic queries across the main analysis and uncertainty failure classes.
2. Read peer-reviewed full text and official standards directly where available; label abstract-level use narrowly.
3. Record supported behaviors, contradictions, transfer limits, effective dates, and update triggers.
4. Reconcile every adapter source reference and preserve the non-exhaustive boundary.

### Task 2: Specify behavior before implementation

**Files:**
- Create: `skills/nature-shared/tests/test_statistical_inference_contracts.py`
- Create: `skills/nature-shared/tests/fixtures/statistical-inference/valid-randomized.json`

1. Write behavior tests for schema, evidence breadth, non-universal resolution, upstream bindings, unit/dependence, multiplicity, missingness, diagnostics, interval semantics, inference shortcuts, surface consistency, policy dates, repairs, and certification.
2. Run the module and verify failure because the schema, catalog, registry, and resolver do not exist.
3. Keep each test focused on an observable decision and verify structural failure returns before semantic arithmetic.

### Task 3: Implement schema and maintained adapters

**Files:**
- Create: `skills/nature-shared/analysis-contracts/statistical-inference-uncertainty-contract.schema.json`
- Create: `skills/nature-shared/analysis-contracts/maintained-analysis-adapters.json`

1. Define strict, additive object shapes and explicit unknown/not-checked/not-applicable states.
2. Add evidence-linked, non-universal adapters with transfer limits and live exact-domain research boundaries.
3. Run behavior tests and verify only resolver/evaluator behaviors remain red.

### Task 4: Implement resolver and evaluator test-first

**Files:**
- Create: `skills/nature-shared/scripts/resolve_statistical_inference.py`
- Modify: `skills/nature-shared/tests/test_statistical_inference_contracts.py`

For each behavior, run the single failing test, add the minimum check and repair route, then rerun the full module. Schema-invalid objects must stop before semantic operations. Results must separate blockers, unresolved research, warnings, visible deviations, repair routes, obligations, source provenance, transfer limits, and bounded certification.

### Task 5: Document and integrate the contract

**Files:**
- Create: `skills/nature-shared/core/statistical-inference-uncertainty-contract.md`
- Modify: `skills/academic-writing/{SKILL.md,README.md,README_EN.md,manifest.yaml}`
- Modify: `skills/academic-paper-pipeline/{SKILL.md,README.md,README_EN.md,manifest.yaml}`
- Modify: `skills/nature-statistics/{SKILL.md,README.md,README_EN.md,manifest.yaml}`
- Modify: `skills/nature-shared/{README.md,README_EN.md,manifest.yaml}`
- Modify: `docs/academic-paper-project-state.template.yaml`

1. Insert analysis resolution after data integrity and before quantitative Results, displays, captions, or claims.
2. Route the evidence ledger on demand and bump affected manifests additively.
3. Add project-state analysis, result, surface-binding, unresolved, blocker, and assurance fields without removing or renaming existing keys.
4. Add integration tests for every canonical consumer.

### Task 6: Verify, review, and integrate

1. Run the new module, all focused shared/writing/pipeline/statistics/figure suites, Python/JSON/YAML parsing, and repository/README/index/metadata/workflow validators.
2. Run `git diff --check`; inspect status and `origin/main...HEAD` diff.
3. Commit, push, open a dedicated PR, and inspect all hosted checks plus independent review findings.
4. Fix valid findings test-first and repeat verification.
5. Squash-merge only when the PR is clean and all required checks succeed; then verify local `main` matches `origin/main` and report the merged commit.
