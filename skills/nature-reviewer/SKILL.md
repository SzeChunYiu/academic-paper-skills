---
name: nature-reviewer
description: >-
  Simulate journal-aware pre-submission editorial triage, mutually blind peer review,
  post-review editor synthesis, and an author-facing decision-engineering map. The legacy
  skill name is retained for compatibility but the workflow is not Nature-only. Resolve the
  exact journal/venue and publication model before assessing novelty, priority, breadth,
  advancement, rigor, clinical relevance, or other target-specific criteria. Use for mock peer
  review, desk-review risk, editor perspective, reviewer perspective, acceptance-readiness,
  manuscript critique, novelty/significance/technical-soundness assessment, 投稿前自审、编辑视角、
  审稿人视角、模拟审稿、拒稿风险、接收概率相关风险分析. Produce evidence-grounded Major Concerns,
  Minor Comments, blocking flags, and minimum-sufficient repair tests without gaming reviewers.
---

# Journal-Aware Editor + Reviewer Decision Simulation

`nature-reviewer` is a legacy entry-point name. Do **not** infer flagship Nature criteria from the skill name.

The workflow models the publication funnel as separate stages:

`target criteria -> editorial triage -> independent external review -> editor synthesis -> author-facing decision engineering`

The goal is not to predict or manipulate acceptance. The goal is to make the scientific case correctly scoped, easy to evaluate, and strong against the decision-relevant objections used by the exact target.

## Core stance

- Load `manifest.yaml` and every `always_load` file.
- Resolve exact target journal/venue, article type and current publication model before applying target-specific axes.
- Keep universal scientific validity separate from target-specific priority, significance, readership, novelty, advancement, clinical impact or other editorial criteria.
- Do not use one `novelty + rigor + impact` formula across journals.
- Build a **decision proof** for each headline claim: claim, importance under target criteria, decisive evidence, strongest alternative explanation, boundary, and resolution test.
- For full manuscripts and formal/theory claims, load
  `../nature-shared/core/atomic-claim-verification.md`. Each blind reviewer builds
  or coverage-checks the atomic inventory independently; do not place a shared
  pre-adjudicated ledger or concern list in the reviewer packet.
- Simulate editor triage before reviewers, using only the manuscript and verified target criteria. Do not contaminate reviewers with triage conclusions.
- Return exactly `3 mutually blind reviewer reports + 1 post-review synthesis` by default, while also adding the separate editorial-triage and author-facing decision-engineering layers. The user may request another reviewer count.
- Give every reviewer the same immutable manuscript/source packet, target criteria and report skeleton, plus only that reviewer's preassigned emphasis.
- Run each reviewer in a **genuinely separate context**, subagent, process, or invocation. If the environment cannot isolate contexts, generate one reviewer report per invocation or explicitly state that mutual blindness cannot be guaranteed.
- **Freeze each individual report before comparing** them. Natural duplication/disagreement is evidence, not a defect to edit away.
- Generate synthesis only afterward as `Editor synthesis (post-review; simulated)` and keep it **not shown to reviewers**.
- **Do not let one reviewer read** another review, the editorial-triage conclusion, a shared concern ledger, consensus hints, or the author-facing repair plan.
- Give every substantive concern a stable ID, faithful `claim_pointer`, verifiable `evidence_pointer`, decision consequence and resolution test.
- Separate user-visible concerns into `Major Concerns` and `Minor Comments`.
- Mark a Major Concern `Blocking Yes` only when the current manuscript cannot establish a central case or satisfy a hard target criterion until the issue is resolved.
- **Minor Comments are never blocking**.
- **Do not impose a concern quota**. Use `None identified from the supplied material` instead of manufacturing issues.
- Prefer the minimum scientifically sufficient closure: add decisive evidence, reanalyse, correct, clarify/restructure, narrow claim, remove claim, or change target/article type.
- Treat reviewer requests as optional unless they close a real scientific or publication-criteria gap.
- Do not claim the real editor's final decision or numeric acceptance probability.

## Target/publication-model gate

When the target is named, load:

1. `../nature-shared/journal-formats/journal-resolution.md`;
2. current official target editor/reviewer/publication criteria when decision-critical;
3. `../nature-shared/journal-formats/editorial-decision-profiles.md` as a fallback model only.

Common profiles include:

- selective broad-interest;
- selective field-advancement;
- rigor-first scholarly record;
- clinical/policy priority;
- evidence-assessment without conventional post-review gatekeeping;
- deadline-constrained conference selection.

### Important contrasts

- Flagship Nature can screen on importance/broad readership independently from technical validity.
- PLOS ONE explicitly emphasizes technical rigor/scientific and ethical eligibility rather than perceived importance as a publication threshold.
- IEEE exposes scope, novelty, validity, data, clarity, compliance and advancement as separate assessment axes.
- eLife's current assessment model separates significance of findings from strength of evidence and should not be converted into a fake acceptance score.

Always verify the exact target at use time.

## Accepted inputs

- full manuscript;
- title/abstract/summary;
- selected sections;
- figures/tables/legends;
- supplementary material;
- author claim/evidence notes;
- target journal/venue and article type;
- cover letter/initial-submission positioning;
- constraints on additional experiments/analysis.

If material is partial, perform a bounded review and state the assessment boundary.

## Workflow

### 1. Build target criteria card

Record:

- exact journal/venue;
- article/content type;
- publication model;
- editorial-triage axes;
- reviewer axes;
- acceptance/assessment condition;
- verified sources;
- unresolved criteria.

### 2. Run editorial triage simulation

Without future reviewer concerns, evaluate:

- scope/article-type fit;
- contribution clarity;
- decisive evidence class;
- target-specific priority/breadth/advancement only if applicable;
- maturity/readiness for external review;
- readability/evaluability;
- obvious integrity/compliance/central-evidence blockers.

Allowed posture labels include:

- `send_to_review_case_clear`;
- `send_to_review_but_positioning_risk`;
- `technical_case_not_review_ready`;
- `target_fit_or_priority_risk`;
- `scope_or_article_type_mismatch`;
- `integrity_or_compliance_blocker`;
- `not_assessable_from_supplied_material`.

These are simulation labels, not predictions of the real editor.

### 3. Build immutable reviewer packet

Include only supplied manuscript facts, verified anchors, assessment boundary, target criteria, report skeleton and reviewer-specific emphasis.

Do not include triage conclusions or pre-generated concerns.

### 4. Run independent reviewers

Use `references/review-axes.md`.

Default emphases:

- Reviewer 1: validity, methods, data, inference and blocking technical concerns;
- Reviewer 2: prior work, contribution/originality and target-specific significance/priority;
- Reviewer 3: reproducibility/reporting, clarity/readership and generalization/boundaries.

Modify these lenses for the article type when needed without inventing biographies.

Each reviewer independently builds its own concern ledger and output.
For full/formal scope, each reviewer also checks atomic coverage, immediate
definition consequences, proof dependencies, counterexamples, source entailment,
and fail-closed statuses before reports are frozen.

### 5. Construct concerns

For each Major Concern include:

- concern ID;
- severity;
- `Blocking Yes / No`;
- target criterion affected;
- `claim_pointer`;
- `evidence_pointer`;
- concern;
- alternative interpretation when relevant;
- why it matters;
- resolution test.

The resolution test may legitimately be **claim narrowing or removal**, not always a new experiment.

### 6. Freeze reports

Do not rewrite independent reports after comparison to manufacture agreement or diversity.

### 7. Run editor synthesis

After all reports are frozen, classify issues as:

- `publication_criteria_blocker`;
- `technical_blocker`;
- `major_repairable`;
- `claim_recalibration`;
- `clarity_or_reporting`;
- `optional_enrichment`.

Editors are simulated as weighing arguments and relevant lenses, not counting votes.

Allowed simulated decision postures:

- `strong_case_after_minor_closure`;
- `promising_major_revision_case`;
- `central_case_requires_new_decisive_evidence`;
- `scientifically_valid_but_target_fit_or_priority_problem`;
- `current_claims_not_established`;
- `transfer_or_repositioning_may_be_better_than_more_experiments`;
- `not_assessable`.

Never state these as the journal's real decision.

### 8. Build decision engineering map

This is author-facing and generated after frozen reviews.

For each decision-relevant risk identify:

- stage where it matters;
- target criterion;
- claim affected;
- why it can change a decision;
- cheapest valid closure route;
- minimum sufficient manuscript/evidence change;
- residual risk.

Also list **Do not waste effort on** items for reviewer requests classified as optional enrichment.

### 9. Run QA

Load `references/qa-checklist.md` and audit:

- target-criteria fidelity;
- reviewer isolation;
- traceability;
- severity/blocking calibration;
- resolution-test validity;
- editor/reviewer role boundaries;
- anti-gaming;
- non-invention.

## Output contract

Unless the user asks otherwise:

```text
Review setup
Editorial triage simulation
Reviewer 1
Reviewer 2
Reviewer 3
Editor synthesis (post-review; simulated)
Decision engineering map (author-facing)
Risk / unsupported claims
```

Each reviewer retains both `Major Concerns` and `Minor Comments` headings even when one tier is empty.

## Acceptance-engineering red lines

Do not optimize acceptance by:

- hiding negative/contradictory evidence;
- selectively omitting close competitors;
- inflating novelty or broad impact;
- citing likely reviewers to influence them;
- choosing suggested reviewers because they are expected to be favorable;
- agreeing to irrelevant reviewer self-citations merely for recommendation benefit;
- burying limitations that change the headline interpretation;
- adding cosmetic experiments that do not discriminate between plausible explanations;
- writing a cover letter that claims significance the manuscript does not establish.

Peer-review research on author-suggested reviewers and reviewer citation requests is treated here as an anti-gaming warning, not a tactic.

## Red lines and legacy integrity contracts

- Do not invent reviewer identities, specialties, institutions, selection history, hidden editor knowledge, competing submissions, experiments, validations, controls, citations, figure details, or line numbers.
- **Do not invent experiments** or manuscript changes.
- Do not present an editor simulation as a real decision letter.
- Do not silently turn reviewer assessment into author rebuttal drafting; real post-decision response work belongs to `nature-response`.
- **Avoid em dashes, en dashes, and colons** as routine prose connectors in the reviewer-report style contract where a clearer sentence boundary works.
- **Do not use dash punctuation or colons** habitually when clearer prose is available. Preserve punctuation required by titles, quotations, formulas, identifiers, URLs, times and machine-readable syntax.
- Do not downgrade core validity, ethics or integrity problems because their prose explanation is short.
- Do not upgrade local presentation preferences merely to sound severe.

## Related files

- `../nature-shared/core/editor-reviewer-decision-engine.md` — shared decision stages, claim decision proof, closure routes and anti-gaming rules.
- `../nature-shared/journal-formats/editorial-decision-profiles.md` — cross-journal publication-model fallbacks.
- `references/source-basis.md` — researched public editor/reviewer source basis.
- `references/reviewer-workflow.md` — exact simulation execution order.
- `references/review-axes.md` — universal and target-conditional axes.
- `references/technical-concern-taxonomy.md` — concern coverage/traceability.
- `references/domain-specific-review-gates.md` — claim-dependent domain checks.
- `references/report-structure.md` — output anatomy.
- `references/role-boundaries.md` — editor/reviewer/author-facing separation.
- `references/qa-checklist.md` — final release gate.
- `../nature-writing/references/paper-review.md` — full manuscript claim/argument audit.
- `../nature-shared/core/atomic-claim-verification.md` — coverage-complete,
  fail-closed scientific-content verification.
- `../nature-shared/core/consistency-sweep.md` — internal manuscript contradiction scan.

## Source hierarchy

1. exact current target journal/venue editor/reviewer/publication criteria;
2. manuscript facts supplied by the user;
3. shared decision engine and publication-model profile;
4. `references/source-basis.md`;
5. exact Nature local source only when flagship Nature is the target;
6. domain-specific supporting gates when applicable.

If target-policy certainty is unavailable, mark it unresolved instead of improvising a criterion.
