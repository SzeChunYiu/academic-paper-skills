# Evidence-Graded Publication Optimization

[中文](acceptance-optimization.md)

This guide describes how the academic-paper system tries to maximize **legitimate publication opportunity** without pretending that journal acceptance is controllable or reducible to a score.

The central idea is simple:

> Improve every preventable failure point in the scientific and editorial path, starting as early as the research-question/design stage, while keeping irreducible editorial uncertainty explicit.

## The lifecycle

Publication opportunity is treated as a lifecycle:

```text
question value / scientific utility
-> study design capable of the intended claim
-> evidence maturity
-> analysis / uncertainty / reporting
-> figures and tables
-> exact target and article type
-> desk-rejection stress test
-> editorial routing
-> expert peer review
-> editor synthesis
-> revision closure
-> transfer / retargeting when appropriate
```

This is deliberately broader than manuscript polishing.

A weak design cannot be rescued by elegant writing, and a strong specialist paper should not be distorted merely to imitate a broad-interest journal.

## Evidence grades

Acceptance advice is labeled by the kind of evidence supporting it:

| Grade | Meaning | How it may be used |
|---|---|---|
| A | direct experimental or quasi-experimental publication-process evidence | support the outcome actually tested |
| B | large-scale or multi-journal observational meta-research | strong prior, not causal proof |
| C | single-journal or narrow-domain observational evidence | define likely failure modes with transfer limits |
| D | current official target policy/reviewer criteria | exact target gate when applicable |
| E | expert editorial/practice guidance | workflow guidance, not acceptance proof |
| H | public peer-review-history heuristic | learn concern-to-repair patterns only |
| MANUSCRIPT_INTERNAL | the project's own scientific evidence/state | scientific hard gate where appropriate |

A public review history cannot become a hard acceptance rule just because the paper was accepted.

## Start before the manuscript

For a prospective project, the system asks:

- Is the research question useful or important under a plausible publication model regardless of outcome direction?
- Can the proposed design actually support the intended headline claim?
- What comparator, control, uncertainty, validation or failure-boundary evidence would be required?
- What would make the study informative if the result is null, negative or heterogeneous?
- Is there an eligible Registered Report route that would allow methods and analysis to be peer reviewed before results are known?

The purpose is not to design a study to obtain a publishable positive result. It is to design a study whose answer is scientifically interpretable and publication-worthy regardless of result direction where possible.

## Registered Reports

For eligible prospective research, the system checks current official target policy before outcome access.

A Registered Report may allow Stage 1 peer review of the question, design and analysis before results are known, followed by in-principle acceptance when the protocol satisfies the venue's criteria. Stage 2 publication then depends on faithful execution and defensible interpretation rather than whether the result happens to be positive or statistically significant.

This is not a universal shortcut. Stage 1 can be rejected, eligibility varies by venue and field, and retrospective projects cannot manufacture prospective status.

## Build the evidence package backward from the claim

For every headline claim:

```text
claim
-> estimand / scientific object
-> independent unit
-> design / identification
-> measurement validity
-> comparator / control
-> sample or information size
-> uncertainty
-> strongest alternative explanation
-> discriminating evidence
-> robustness / sensitivity
-> failure boundary
```

The target is the **shortest sufficient evidence set**, not the largest number of experiments.

## Pre-submission red teams

Before submission, the pipeline independently attacks the manuscript from several directions:

- domain science and prior-work positioning;
- design/identification;
- measurement and controls;
- statistics and uncertainty;
- reporting-standard completeness;
- figure/table/data visibility;
- explanatory sufficiency and sentence logic;
- target scope/article type;
- editorial routing and reviewer-expertise coverage.

For quantitatively central papers, specialist statistical review is treated as a high-value quality intervention. Evidence supports improvements in manuscript statistical/reporting quality, but the package does not relabel that evidence as a proven acceptance-rate increase.

## Desk-rejection stress test

The system explicitly tries to desk-reject the manuscript for common preventable reasons:

1. wrong target or article type;
2. weak/unclear question, rationale or contribution;
3. design cannot support the central claim;
4. methods or analysis are under-described/weak;
5. decisive evidence is hidden or badly represented;
6. writing/explanation blocks evaluation;
7. policy/compliance requirements are unresolved.

Each identified problem needs a concrete closure test.

## Fit-first target ladder

When the goal is successful publication rather than one fixed venue, the system builds a ladder such as:

```text
stretch_but_compatible
best_fit
robust_fit
specialist_fallback
alternative_article_type
Registered Report route where prospective and eligible
```

Targets are compared by scientific scope, contribution class, evidence expectations, readership, article type, reporting compatibility, review model and practical constraints—not impact factor alone.

## Learn from public review histories, carefully

Transparent review archives from venues such as Nature Communications, PLOS, eLife and TMLR/OpenReview can reveal how real objections were handled.

The system annotates:

```text
initial claim/evidence
-> reviewer/editor concern
-> actual author repair
-> changed evidence/analysis/figure/text/claim
-> re-review / final state
```

It learns patterns such as:

- when a new control really discriminated an alternative explanation;
- when reanalysis was enough;
- when a figure redesign exposed evidence already present;
- when a claim was narrowed rather than adding an experiment;
- when a reviewer request was not actually required by the editor.

But accepted histories are survivorship-selected. Therefore they are Grade H heuristics, must carry a survivorship warning, and should be paired with rejection-report or rejected-case evidence.

The package never treats “this change appeared before acceptance” as proof that the change caused acceptance.

## Revision is about scientific delta

A revision is tracked by what actually changed:

- new evidence/control/validation;
- reanalysis or sensitivity analysis;
- corrected statistics;
- redesigned figure/table;
- expanded methods/explanation;
- limitation made visible;
- claim narrowed or removed;
- target/article type changed.

A long response letter is not a substitute for a changed scientific object.

## Rejection triage

After rejection, the pipeline first classifies the reason:

- scientific blocker;
- target mismatch;
- manuscript/evidence visibility failure;
- policy/compliance problem;
- unresolved review disagreement;
- uncontrollable editorial context;
- appeal candidate under an exact appeal policy.

Only then does it decide whether the right action is new evidence, reanalysis, writing/figure repair, claim narrowing, appeal, transfer or retargeting.

## What cannot be engineered away

Even a decision-ready manuscript may encounter:

- overlapping work that authors could not know about;
- competition among several strong submissions;
- reviewer availability;
- legitimate disagreement about soft priority criteria;
- confidential editorial information;
- editorial discretion not reducible to public rules.

These factors are kept in a separate `uncontrollable editorial context` bucket so the system does not respond to every rejection with unnecessary experiments or hype.

## Hard boundaries

The system must never optimize through:

- editor leniency/harshness profiles;
- reviewer friendliness scores;
- individual acceptance-propensity estimates;
- strategic citations to likely editors/reviewers;
- personal, demographic, political or religious profiling;
- hidden negative evidence;
- inflated novelty/significance;
- fabricated experiments/results;
- prestige-only target ranking;
- AI-detector gaming;
- accepted-paper survivorship patterns presented as causal acceptance rules.

## Strongest allowed readiness label

The acceptance-optimization layer may return:

`acceptance_optimized_decision_ready_for_target`

This means the preventable scientific, target, presentation and reviewability blockers have been systematically attacked under current evidence and policy.

It does **not** mean “likely accepted,” and it never comes with a numeric acceptance probability.
