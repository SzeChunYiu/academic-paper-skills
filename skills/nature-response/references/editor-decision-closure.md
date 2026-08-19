# Editor-decision closure for revision packages

Use this reference after a real editor/reviewer decision has been parsed and before committing to experiments or manuscript expansion.

## Contents

- [Principle](#principle)
- [Authority order](#authority-order)
- [Build the decision ledger](#build-the-decision-ledger)
- [Classify reviewer requests](#classify-reviewer-requests)
- [Choose the closure route](#choose-the-closure-route)
- [Major revision strategy](#major-revision-strategy)
- [Minor revision strategy](#minor-revision-strategy)
- [Conflicting or excessive requests](#conflicting-or-excessive-requests)
- [Cover-letter synthesis](#cover-letter-synthesis)
- [Anti-gaming and honesty](#anti-gaming-and-honesty)

## Principle

A revision succeeds when decision-relevant concerns are **closed in the manuscript and evidence state**, not when every reviewer request produces new prose or a new experiment.

Load `../../nature-shared/core/editor-reviewer-decision-engine.md` and resolve the exact target journal/publication model if needed.

## Authority order

For strategy, use:

1. explicit editor instructions/decision conditions;
2. hard journal/publication criteria;
3. technically blocking reviewer concerns;
4. major reviewer concerns that materially affect the case;
5. clarity/reporting concerns;
6. optional enrichment/preferences.

A reviewer preference does not automatically outrank an editor instruction or the manuscript's scientific scope.

## Build the decision ledger

For every editor/reviewer item record:

```yaml
id: R1.3
source: reviewer_1
claim_affected: value
criterion_affected: value or not_applicable
scientific_consequence: value
editor_decision_relevance: direct | indirect | optional | unresolved
work_status: not_started | in_progress | done | author_input_needed
closure_route: value
closure_evidence: manuscript/analysis location
residual_risk: value
```

Keep editor items (`E.*`) separate from reviewer items.

## Classify reviewer requests

Use:

- `publication_criteria_blocker`;
- `technical_blocker`;
- `major_repairable`;
- `claim_recalibration`;
- `clarity_or_reporting`;
- `optional_enrichment`.

Do not classify by politeness, length, difficulty or experiment cost.

## Choose the closure route

### `add_decisive_evidence`

Use only when new evidence genuinely discriminates among important interpretations or is explicitly required by a criterion/editor condition.

### `reanalyse_existing_evidence`

Use when current data can answer the concern with a better/appropriate analysis.

### `correct_error`

Use for factual, statistical, computational, figure, citation or reporting errors.

### `clarify_or_restructure`

Use when the evidence already exists but reviewers could not recover it. Change the manuscript as well as the response.

### `narrow_claim`

Use when the evidence supports a bounded claim and preserving the broader wording would require disproportionate new work.

### `remove_claim`

Use for unsupported secondary claims that are not necessary to the central contribution.

### `explain_nonimplementation`

Use only when a request is technically inappropriate, impossible, outside scope, incompatible with another instruction, or optional. Give evidence/reasoning and, when possible, an alternative repair.

## Major revision strategy

1. Identify explicit editor conditions first.
2. Resolve all blocking central-case items.
3. Rebuild the headline claim ledger after any new evidence or narrowing.
4. Re-check whether target-specific significance/priority still holds after narrowing.
5. Resolve major repairable concerns.
6. Repair clarity/reporting issues that caused reviewers to miss existing evidence.
7. Treat optional enrichment as optional; do not let it crowd out the central revision.
8. Re-run consistency and main-text discipline so the paper does not grow into a reviewer-comment archive.

## Minor revision strategy

Minor revision does not mean every request is minor scientifically. Verify each item.

- Correct all explicit editor conditions.
- Do not introduce new claims that create new evidence dependencies.
- Prefer precise local edits.
- Escalate immediately if a reviewer request reveals a hidden central validity problem rather than disguising it as a minor wording change.

## Conflicting or excessive requests

When reviewers conflict:

1. identify the underlying claim/criterion;
2. determine whether both can be satisfied scientifically;
3. follow explicit editor direction when provided;
4. explain the conflict in the editor-facing cover letter if a choice is necessary;
5. do not show one mutually blind reviewer another reviewer's content.

When a reviewer requests excessive work:

- ask whether the work changes acceptance of the central claim;
- ask whether a target criterion requires it;
- if not, consider claim narrowing, clarification, SI placement, or a reasoned nonimplementation response.

## Cover-letter synthesis

The revision cover letter should help the editor audit closure. Summarize:

- editor conditions and where each was closed;
- central technical blockers and their closure evidence;
- any headline claim that was narrowed/removed;
- conflicts/nonimplemented requests that need editor adjudication;
- remaining limitations disclosed in the manuscript.

Do not use the cover letter to create new significance claims absent from the revised manuscript.

## Anti-gaming and honesty

Never:

- call a request `addressed` when only the response prose changed;
- add irrelevant reviewer citations to influence recommendation;
- hide negative new results obtained during revision;
- move a decision-changing limitation out of sight;
- claim an experiment was performed when it was not;
- invent page/line locations;
- overstate agreement with a reviewer when the authors actually disagree;
- do unnecessary experiments simply to signal effort.

The strongest response makes the editor's closure check easy and honest.