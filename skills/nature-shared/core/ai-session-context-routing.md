# AI session context routing for academic-paper work

> Progressive-disclosure map for deciding which detailed contracts enter an AI session at each stage.

This contract is mandatory whenever the writing/review pipeline performs substantial work. It complements `ai-session-execution-kernel.md`.

## 1. Routing principle

Do not preload every writing/research/review rule.

Use:

```text
small always-loaded kernel
+ current manuscript checkpoint
+ one stage bundle
+ zero or more task-specific bundles
+ only the manuscript/evidence excerpts needed for the active decision
```

Detailed contracts remain mandatory when their trigger is active.

## 2. Stage bundles

### BOOTSTRAP bundle

Use when starting a paper/session, retargeting, or resuming without a reliable checkpoint.

Load the minimum needed subset of:

- `paper-type-taxonomy.md`
- `paper-archetype-atlas.md`
- `reader-workflow.md`
- `standalone-manuscript-reader-contract.md`
- `journal-formats/journal-resolution.md` when target-specific rules matter
- `unknown-paper-research-protocol.md` when the paper type is not covered confidently

Produce/freeze:

- central question;
- bounded answer candidate;
- intended reader;
- paper archetype;
- target/article type/stage if known;
- current evidence boundary;
- next primary operation.

Do not load sentence-level polishing, release packaging, or full reviewer rules here.

### RESEARCH bundle

Use when finding/validating external scientific evidence, literature position, novelty boundaries, or venue/reporting norms.

Load as applicable:

- `literature-version-and-source-quality.md`
- `research-integrity-verification.md`
- `atomic-claim-verification.md` for claim-level support decisions
- `analogue-paper-calibration.md` for close-paper structure/evidence calibration
- `unknown-paper-research-protocol.md` for uncovered genres
- target/reporting-standard references only when they affect the active research question

Return structured source/evidence cards rather than raw search dumps.

Do not carry the entire search corpus into COMPOSE.

### ARCHITECT bundle

Use when designing or substantially restructuring the scientific argument.

Load as applicable:

- `manuscript-narrative-architecture.md`
- `manuscript-section-craftsmanship.md`
- `explanatory-sufficiency.md`
- `terminology-ledger.md`
- `manuscript-content-selection.md`
- `venue-constrained-manuscript-budget.md` when target/length is known
- `formal-spine-preservation.md` when the contribution has formal content
- `figure-evidence-planning.md` / `scientific-display-decision-contract.md` when displays are part of the evidence architecture

Produce/freeze:

- question -> bounded answer -> evidence progression -> alternative/boundary -> meaning;
- section-function map;
- reader-state activation map;
- main-versus-support allocation;
- target budget snapshot if applicable.

### COMPOSE bundle

Use for drafting one section/subsection/display at a time.

Always provide:

- section contract;
- relevant claims/evidence cards;
- active terminology;
- immediate upstream/downstream handoff;
- target-space budget for that surface when applicable.

Load only relevant detailed contracts, for example:

- `abstract-information-budget.md` for abstract;
- `manuscript-section-craftsmanship.md` for the active section;
- `sentence-logic-and-cohesion.md` only when local flow is difficult;
- `natural-scholarly-prose.md` / `author-voice-profile.md` during prose realization after scientific logic is fixed;
- `numerical-reporting-precision.md` when rendering claim-bearing numbers;
- `epistemic-rhetoric-and-qualification.md` when claim scope/stance is active;
- `formal-spine-preservation.md` when composing formal contribution text;
- statistics/reporting/figure contracts only when the section actually uses them.

Do **not** preload full reviewer, acceptance-optimization, release-integrity, or package-verification contracts during ordinary prose generation.

### AUDIT bundle

Use for a specific quality check after composition.

Load the contract(s) corresponding to the question being audited, plus the smallest affected manuscript scope.

Examples:

- abstract density -> `abstract-information-budget.md` + `audit_abstract_information.py`;
- reader independence -> `standalone-manuscript-reader-contract.md` + `audit_standalone_manuscript.py`;
- surface leakage -> `scholarly-surface-semantics.md` + scanner;
- narrative/precision -> relevant contract + `audit_narrative_precision.py`;
- citation integrity -> research-integrity ledger/verifier;
- budget -> manuscript-budget ledger/verifier.

Return findings as stable concern IDs, severity, evidence, and resolution tests. Do not rewrite the whole manuscript automatically.

### REVISE bundle

Use after an audit/review identifies finite concerns.

Load:

- current affected surface;
- concern IDs and resolution tests;
- changed evidence/results;
- local section craftsmanship/narrative contract;
- any scientific contract directly implicated by the concern.

Avoid loading unrelated closed concerns and full historical reviewer prose.

After repair, update the checkpoint and revision delta.

### REVIEW bundle

Use for editor/reviewer simulation.

Load:

- current full manuscript when global evaluation is required;
- `editor-reviewer-decision-engine.md`;
- `adversarial-review-bias-control.md`;
- `paper-archetype-atlas.md` so evidence, explanation and display expectations are judged against the actual paper class;
- `standalone-manuscript-reader-contract.md` for zero-context reader judgment;
- `manuscript-section-craftsmanship.md` when section-function quality is in scope;
- target decision contract/publication model;
- `manuscript-excellence-release-gate.md` for global communication/readiness checks;
- atomic/integrity/statistics/formal contracts when the reviewer is actually evaluating those claims.

Reviewer-specific task packets should remain mutually blind where required. Do not give every reviewer all prior reviews, author responses, or internal author ledgers unless the review stage explicitly needs them.

### RELEASE bundle

Use only when the current manuscript is being considered final/submission/publication ready.

Load all applicable final gates, including:

- `manuscript-excellence-release-gate.md`;
- `atomic-claim-verification.md`;
- `research-integrity-verification.md`;
- `consistency-sweep.md`;
- `scholarly-surface-semantics.md`;
- `manuscript-surface-qa.md`;
- exact target/reporting rules;
- `publication-release-integrity.md` and package verifier when releasing files;
- formal/statistical/data/protocol contracts if those domains apply.

This is intentionally the widest context mode.

## 3. Task-specific bundles

### FORMAL task

Trigger when the manuscript makes contribution-defining formal claims, proofs, bounds, definitions, invariants, or non-implications.

Load:

- `formal-spine-preservation.md`
- `atomic-claim-verification.md`
- theory/proof archetype guidance

### QUANTITATIVE task

Trigger when claim-bearing numerical/statistical inference is being designed, rendered, audited, or revised.

Load:

- `statistical-inference-uncertainty-contract.md`
- `numerical-reporting-precision.md`
- relevant reporting guideline/target requirements

### FIGURE/TABLE task

Trigger for evidence representation or display planning.

Load:

- `figure-evidence-planning.md`
- `scientific-display-decision-contract.md`
- `visual-evidence-atlas.md` only when a representation choice requires it

### SOURCE/CITATION task

Trigger for manuscript-facing external claims/citations.

Load:

- `literature-version-and-source-quality.md`
- `research-integrity-verification.md`
- `atomic-claim-verification.md` when entailment/claim granularity matters

### TARGET task

Trigger when exact venue/article-type compliance or editorial fit matters.

Load:

- `journal-formats/journal-resolution.md`
- `journal-formats/venue-decision-contract.md`
- `venue-constrained-manuscript-budget.md`
- target-specific evidence only as needed

## 4. Context eviction rule

When changing primary operation, explicitly evict detailed contracts that no longer govern the next action unless they contain a still-active hard constraint.

Example:

```text
RESEARCH -> ARCHITECT
```

Keep:

- verified source/evidence cards;
- unresolved novelty boundary;
- target constraints.

Evict:

- raw search results;
- duplicate abstracts;
- search-query history;
- irrelevant source metadata.

Example:

```text
REVIEW -> REVISE
```

Keep:

- must-address concern IDs;
- exact resolution tests;
- affected claim/evidence references;
- editor decision conditions.

Evict:

- reviewer prose that does not affect a live concern;
- resolved concerns;
- redundant reviewer agreement.

## 5. Full manuscript policy

The full manuscript is justified for:

- macro-argument architecture;
- clean-reader self-containment review;
- terminology/number/claim consistency;
- global section allocation;
- editor/reviewer simulation;
- release QA.

For local drafting/revision, prefer:

```text
active section
+ preceding/following handoff
+ relevant abstract/introduction claim if needed
+ active evidence cards
+ current terminology state
```

Do not repeatedly inject the full paper merely because it is available.

## 6. Context packet quality test

Before a substantial model step, ask:

1. Does every included item affect the current decision?
2. Is a missing item capable of changing correctness or scientific interpretation?
3. Is any long source/review/history block replaceable by a structured card/checkpoint row?
4. Are duplicate instructions stated in more than one loaded contract?
5. Is the session attempting more than one primary operation?
6. Can deterministic work be moved to a script/validator first?

If 1 is no for large portions of the packet, shrink it.
If 2 is yes, load the missing contract/evidence.

## 7. Resume protocol

When starting a new AI session on an existing paper:

1. load the compact checkpoint;
2. load the current manuscript version or only the active section according to mode;
3. load relevant claim/evidence/source rows;
4. load the stage bundle;
5. verify unresolved blockers and next action;
6. continue from the checkpoint rather than reconstructing project history from memory.

If the checkpoint conflicts with the current manuscript/evidence artifacts, the artifacts win and the checkpoint is refreshed.

## 8. Anti-overengineering boundary

Do not turn context routing into a bureaucracy that costs more than it saves.

- Short one-off edits can use a minimal local packet without creating every ledger.
- Machine-checkable checkpoints are most useful for long, multi-session, multi-review manuscripts.
- Do not create a new bundle for every minor prose issue.
- Do not load a contract solely because its name sounds related; use its trigger.

The optimization target is **scientific correctness per unit of active context and session effort**, not minimum token count in isolation.
