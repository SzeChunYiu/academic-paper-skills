# Editor/reviewer simulation workflow

## Contents

- [Default execution order](#default-execution-order)
- [Target-resolution gate](#target-resolution-gate)
- [Editorial triage simulation](#editorial-triage-simulation)
- [Immutable reviewer packet](#immutable-reviewer-packet)
- [Independent reviewer pass](#independent-reviewer-pass)
- [Concern-ledger fields](#concern-ledger-fields)
- [Editor synthesis](#editor-synthesis)
- [Decision-engineering map](#decision-engineering-map)
- [Failure-safe behaviour](#failure-safe-behaviour)

## Default execution order

1. Identify the supplied manuscript package and assessment boundary.
2. Resolve exact target journal/venue, article type and publication model as far as possible.
3. Build the target criteria card from current official guidance or mark unresolved axes.
4. Run an **editorial triage simulation** without reading future reviewer concerns.
5. Build one immutable reviewer packet.
6. Define reviewer emphasis briefs before any report is generated.
7. Generate each reviewer report in a genuinely separate context.
8. Freeze all reports.
9. Run a separate **editor synthesis** that weighs decision-relevant arguments rather than reviewer votes.
10. Produce an author-facing **decision-engineering map** with the cheapest scientifically valid repair route for each risk.
11. Run QA for target-criteria fidelity, reviewer isolation, traceability, severity, anti-gaming and non-invention.

## Target-resolution gate

Before evaluating `significance`, `priority`, `breadth`, `novelty` or `fit`, determine whether the exact target actually uses that criterion.

Load:

- `../nature-shared/journal-formats/journal-resolution.md` for exact journal/article type/stage;
- `../nature-shared/journal-formats/editorial-decision-profiles.md` for fallback publication-model logic;
- exact live reviewer/editor guidance when submission-critical.

Create a target criteria card:

```yaml
journal: exact title or unresolved
article_type: value or unresolved
publication_model: selective-broad-interest | field-advancement | rigor-first | clinical-policy | evidence-assessment | conference-selection | custom
editorial_triage_axes: []
reviewer_axes: []
acceptance_or_assessment_condition: text
verified_sources: []
unresolved_criteria: []
```

Do not infer a `high-impact` criterion from reputation alone.

## Editorial triage simulation

This is a bounded simulation of likely **decision risks**, not a claim about what the real handling editor will decide.

### Editor packet

Use only:

- manuscript/title/abstract/figures/material supplied by the user;
- target criteria card;
- exact official criteria already verified.

Do not use future simulated reviewer concerns.

### Triage questions

1. Is the manuscript in scope and the article type plausible?
2. Can the central question/tension and contribution be stated faithfully in one compact block?
3. What is the decisive evidence class?
4. Does the current manuscript visibly meet target-specific priority/breadth/advancement criteria when those criteria exist?
5. Is the evidence package mature enough to justify full review?
6. Does readability/organization obstruct assessment of the contribution?
7. Is there an obvious integrity/compliance or central-evidence blocker?

### Triage output states

- `send_to_review_case_clear`;
- `send_to_review_but_positioning_risk`;
- `technical_case_not_review_ready`;
- `target_fit_or_priority_risk`;
- `scope_or_article_type_mismatch`;
- `integrity_or_compliance_blocker`;
- `not_assessable_from_supplied_material`.

Never output a numerical desk-rejection probability.

## Immutable reviewer packet

Give every isolated reviewer the same:

- supplied manuscript/source material;
- verified section/figure/table/equation anchors;
- assessment boundary and missing-file inventory;
- target criteria card;
- report skeleton;
- shared scientific grounding rules;
- that reviewer's preassigned emphasis brief.

Do **not** include:

- editorial triage conclusions;
- suspected concerns;
- shared claim/evidence criticism;
- another report/ledger;
- consensus hints;
- a desired recommendation.

The editorial triage pass must not contaminate reviewer independence.

## Independent reviewer pass

Inside each isolated context:

1. independently reconstruct the central claims and evidence;
2. apply universal scientific axes from `review-axes.md`;
3. apply only target-conditional axes actually present in the target criteria card;
4. load applicable domain-specific review gates;
5. build a private concern ledger;
6. render Major Concerns and Minor Comments;
7. give each Major Concern a resolution test;
8. finalize and freeze the report.

### Reviewer recommendation posture

Keep recommendation language conditional and criterion-based, for example:

- `central case could become publishable if the blocking validity issue is resolved`;
- `technically credible, but the verified target-specific priority criterion is not yet established`;
- `meets a rigor-first scientific-validity bar from the supplied material, subject to the listed reporting corrections`;
- `main claim is only partially supported and should be narrowed or strengthened`.

The reviewer does not decide the final outcome.

## Concern-ledger fields

Use this private shape:

```yaml
issue_key: generalization-external-validation
axis: claim_evidence_validity
applicability: applicable
severity: major
blocking: yes
severity_rationale: The manuscript claims cross-domain generalization but evaluates only one domain.
claim_pointer: The method is claimed to generalize across domains.
evidence_pointer: Results, External evaluation; location not provided if unavailable
evidence_status: located
concern: The visible evidence does not establish the stated scope.
alternative_interpretation: Performance may be domain-specific.
resolution_test: Provide an independent cross-domain test or narrow the generalization claim.
target_criterion: validity / advancement
reviewer_id: Reviewer 1
```

A concern without a resolution test is incomplete.

## Editor synthesis

Run only after all reviewer reports are frozen.

### Step 1 — map reviewer-local issues

Reconcile equivalent concerns to synthesis keys without rewriting the original reports.

### Step 2 — classify decision consequence

Use:

- `publication_criteria_blocker`;
- `technical_blocker`;
- `major_repairable`;
- `claim_recalibration`;
- `clarity_or_reporting`;
- `optional_enrichment`.

### Step 3 — weight arguments, not votes

- Consensus is useful evidence but not a voting rule.
- A single technically decisive objection may remain blocking.
- A reviewer request can be non-essential even if multiple reviewers like it.
- Give greater weight to a concern when the assigned reviewer lens directly covers that issue, but do not invent hidden expertise.

### Step 4 — compare with initial triage

Ask whether external review changed the picture:

- editor underestimated technical risk;
- editor overestimated/underestimated significance;
- target fit remains the main issue;
- manuscript is scientifically sound but needs claim recalibration;
- revision can plausibly close the blocking concerns.

### Step 5 — produce simulated decision posture

Allowed labels:

- `strong_case_after_minor_closure`;
- `promising_major_revision_case`;
- `central_case_requires_new_decisive_evidence`;
- `scientifically_valid_but_target_fit_or_priority_problem`;
- `current_claims_not_established`;
- `transfer_or_repositioning_may_be_better_than_more_experiments`;
- `not_assessable`.

These are **simulation postures**, never assertions of the journal's real decision.

## Decision-engineering map

After editor synthesis, switch to an author-facing repair pass. Do not alter frozen reviewer reports.

For each decision-relevant issue record:

```text
Risk
Stage where it matters
Journal criterion
Claim affected
Why the concern can change a decision
Resolution route
Minimum sufficient change
Evidence/manuscript locations to update
Residual risk after repair
```

Choose among:

1. add decisive evidence;
2. reanalyse existing evidence;
3. correct an error;
4. clarify/restructure the evidence already present;
5. narrow the claim;
6. remove the claim;
7. change target/article type when the scientific work is sound but the journal objective is mismatched.

Prefer the **minimum scientifically sufficient** repair, not the maximum amount of new work.

## Failure-safe behaviour

- If isolated contexts are unavailable, produce one reviewer report per invocation or disclose that mutual blindness cannot be guaranteed.
- If exact target criteria cannot be verified, mark target-specific editorial conclusions `unresolved`; keep the technical review usable.
- If input is partial, do a bounded review and identify what cannot be assessed.
- Do not infer absent validations, ethics approvals, data, figures or citations.
- Do not transform a true design limitation into a wording problem.
- Do not transform a true target-fit problem into a demand for unnecessary experiments.
- Do not recommend reviewer/citation gaming as an acceptance strategy.
