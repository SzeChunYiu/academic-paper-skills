# Public review-history calibration

> Use public editorial/reviewer histories to learn **concern-to-repair patterns** for comparable papers. This is a calibration layer, not an acceptance predictor. Accepted/public cases are selected and incomplete; never infer that a visible revision caused acceptance.
>
> Last reviewed: 2026-08-29.

## 1. Why this exists

Published papers show the final scientific object but often hide the path that made the work reviewable.

Transparent peer-review systems can reveal:

```text
initial claim/evidence state
-> editor/reviewer concern
-> author repair
-> changed manuscript/evidence
-> re-review / decision state
```

That sequence can teach the package how real scientific concerns are phrased and closed.

But public histories have strong selection effects:

- many archives contain only accepted/published papers;
- desk-rejected manuscripts are often absent;
- confidential editor comments are frequently missing;
- some authors opt out or journals publish only parts of the record;
- fields differ in review culture and revision burden.

Therefore use public histories to learn **repair grammar**, not causal acceptance rules.

## 2. Evidence class

All patterns learned from public review histories start as `Grade H` in `acceptance-optimization-protocol.md`.

They can be promoted only when independently supported by:

- official target criteria;
- broader rejection-report evidence;
- multi-journal meta-research;
- methodological/statistical evidence;
- repeated cross-venue cases with clear transfer limits.

Never promote frequency alone to a hard blocker.

## 3. Preferred public sources

### Nature Communications

For original research papers submitted from 1 November 2022, accepted papers have a public peer-review file containing reviewer comments to authors and author rebuttal letters.

Important limitation: internal editorial discussions, decision letters and confidential comments are not necessarily included.

Use for:

- reviewer concern classes;
- response/revision structure;
- evidence additions;
- claim recalibration;
- figure/table changes;
- field-specific expectations.

### PLOS journals

Where authors opt in or the journal exposes a history, packages may include decision letters, reviewer reports, responses and attachments.

Use for:

- explicit editor synthesis;
- revision instructions;
- reviewer-to-editor disagreement;
- point-by-point closure patterns;
- reporting/data-availability issues.

### eLife

Reviewed Preprints and Versions of Record may expose public reviews, editor assessments, author responses and version histories.

Use for:

- evidence-strength changes;
- significance versus evidence distinction;
- multiple revision rounds;
- claim/interpretation changes;
- persistent concerns.

Do not treat eLife's current publication model as equivalent to a conventional accept/reject journal.

### TMLR / OpenReview

TMLR uses public open review after initial reviews are submitted, including reviewer discussion, author responses and final decisions for non-desk-rejected submissions.

Use for:

- claim/evidence negotiation;
- open rebuttal dynamics;
- claim narrowing instead of forced experiments;
- technical-correctness publication models;
- resubmission/decision patterns.

Desk-rejected TMLR submissions are not public, so pair TMLR accepted/rejected public cases with official desk criteria and other rejection evidence.

## 4. Sampling strategy

Do not sample only famous papers.

For a manuscript-specific calibration, prefer:

1. same dominant paper archetype;
2. similar scientific question or evidence class;
3. similar methods/data structure;
4. same or closely comparable target venue/article type;
5. recent cases under the current review model;
6. a mix of easy and difficult revision histories;
7. at least one counterexample where a common requested repair was not necessary or the authors narrowed the claim instead.

### Quick calibration

Use roughly 3–6 close histories.

### Research tranche

Use roughly 15–30 stratified histories across several venues/archetypes before proposing a reusable cross-paper rule.

### Corpus-scale work

For dozens/hundreds of cases, use a structured annotation schema and aggregate only within compatible strata.

## 5. Case annotation schema

For every history record:

```text
case_id
venue
article_type
review_model
submission/review dates
paper archetype
domain
methods/evidence tags

initial headline claims
initial evidence package
initial main figures/tables

editor concern ids, if public
reviewer concern ids
concern class
concern severity
challenged claim
why the concern matters
requested repair

actual author repair
new evidence added?
reanalysis performed?
figure/table changed?
method/reporting detail added?
explanation added?
claim narrowed/removed?
limitation added?
prior-work positioning changed?

re-review response
concern closed / partly closed / disputed / unknown
final claim delta
final evidence delta
final figure/table delta
final manuscript delta

what can transfer to our paper
what cannot transfer
survivorship/selection warning
source urls
```

## 6. Concern taxonomy

Start with these classes:

- `scope_or_target_fit`;
- `contribution_or_novelty`;
- `study_rationale`;
- `design_or_identification`;
- `measurement_validity`;
- `sample_or_information_size`;
- `statistical_inference`;
- `missing_control_or_comparator`;
- `alternative_explanation`;
- `generalization_external_validity`;
- `robustness_sensitivity`;
- `mechanism_evidence`;
- `benchmark_fairness`;
- `calibration_or_utility`;
- `data_or_code_availability`;
- `reporting_compliance`;
- `figure_or_table_evidence`;
- `under_explanation`;
- `writing_or_structure`;
- `prior_work_fairness`;
- `claim_overreach`;
- `limitation_or_boundary`;
- `integrity_or_ethics`;
- `surface_or_copyedit`;
- `optional_enrichment`.

Do not force a concern into the wrong class to make aggregation easier.

## 7. Closure-route taxonomy

Annotate the **actual** repair, not merely what the reviewer requested.

Possible routes:

- `new_evidence`;
- `new_control`;
- `external_validation`;
- `reanalysis`;
- `sensitivity_analysis`;
- `statistical_correction`;
- `figure_redesign`;
- `table_added_or_restructured`;
- `method_detail_added`;
- `reporting_compliance_added`;
- `explanation_expanded`;
- `prior_work_repositioned`;
- `limitation_made_explicit`;
- `claim_narrowed`;
- `claim_removed`;
- `no_change_with_evidence_based_rebuttal`;
- `target_or_article_type_changed`;
- `not_closed`;
- `unknown`.

## 8. Learn dependencies, not phrases

Extract patterns such as:

- reviewers repeatedly challenge pooled averages when task/site heterogeneity matters;
- mechanism claims trigger demands for discriminating evidence beyond association;
- a claim was saved by narrowing rather than an additional experiment;
- a figure redesign exposed an already-existing result more clearly;
- methods clarification closed a reproducibility concern without new data;
- a generalization claim required an external dataset;
- the editor overruled a nonessential reviewer request.

Do **not** copy:

- reviewer wording;
- author rebuttal wording;
- manuscript sentences;
- figure layouts/palettes;
- rhetorical flourishes.

## 9. Pair accepted histories with rejection evidence

To reduce survivorship bias, pair `Grade H` cases with at least one of:

- desk-rejection studies;
- post-review rejection studies;
- official rejection/triage criteria;
- public rejected OpenReview/TMLR submissions where available;
- target transfer guidance.

Ask:

> Could this repair pattern merely be common among published papers because only successful cases are visible?

If yes, keep it descriptive.

## 10. Reviewer request versus editor requirement

Public histories often show requests that were not actually necessary for publication.

Record separately:

```text
reviewer_requested
editor_required
scientifically_required
actually_performed
```

Do not convert every visible reviewer suggestion into a universal acceptance requirement.

This is particularly important for:

- extra experiments;
- expanded scope;
- reviewer-preferred citations;
- speculative analyses;
- stylistic preferences.

## 11. Revision-delta analysis

For every case, compare initial and final versions where possible.

Annotate:

```text
claims added / narrowed / removed
new results
new analyses
new controls
new datasets
new figures/tables
figure role changes
main vs supplement relocation
methods detail changes
limitations changes
sentence/paragraph restructuring
abstract/title changes
```

The goal is to identify which scientific object changed, not just count changed words.

## 12. Evidence-maturity trajectories

Use histories to distinguish:

### Evidence-strength repair

Examples:

- additional control;
- stronger uncertainty analysis;
- external validation;
- corrected statistical model;
- robustness/sensitivity;
- improved provenance.

### Claim calibration

Examples:

- causal -> associative;
- universal -> context-bound;
- mechanism -> dependence;
- clinical utility -> discrimination only;
- superiority -> noninferior / mixed / task-dependent.

### Presentation repair

Examples:

- decisive result promoted to main figure;
- paired data shown as paired;
- exact values added to table;
- Methods explanation expanded;
- figure caption made self-contained.

Keep these categories separate because they imply different work.

## 13. Public-history self-research fallback

When the package is unsure how a reviewer in a specific paper class may evaluate a claim:

1. inspect official criteria;
2. inspect the nearest methods/reporting guidance;
3. find 3–6 recent comparable public review histories;
4. annotate concern-to-repair patterns;
5. find at least one counterexample or rejected-case source;
6. compare those patterns with the actual evidence state of the user's paper;
7. adopt/adapt/reject each pattern explicitly.

Do not use public histories merely because they are from a prestigious journal.

## 14. Reusable rule promotion

A public-history pattern may become a reusable package rule only when:

- it has a clear scientific rationale;
- it is observed across multiple independent cases or supported by stronger evidence;
- the relevant paper archetype/field is explicit;
- counterexamples have been considered;
- the rule states what inference failure it prevents;
- the rule does not depend on copying a venue's cosmetic style.

Otherwise keep it as a manuscript-specific prior.

## 15. Output for a manuscript-specific calibration

Return a compact ledger:

| Concern pattern | Evidence/history basis | Applies here? | Our current state | Best valid repair | Transfer caveat |
|---|---|---|---|---|---|

Then update the manuscript's main concern/evidence/figure ledgers.

Do not return a list of "tricks used by accepted papers."

## 16. Hard boundary

Public peer-review data must never be used to:

- identify a "friendly" editor or reviewer;
- infer individual acceptance propensity;
- strategically cite a likely reviewer;
- reproduce distinctive rebuttal language;
- reverse-engineer hidden confidential editorial information;
- estimate a causal acceptance effect from accepted-only cases;
- encourage evidence suppression or reviewer gaming.

The package learns **how scientific objections get resolved**, not how people get manipulated.
