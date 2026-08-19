# Editorial decision profiles

> Cross-journal decision-model fallbacks. Last reviewed: 2026-08-19.
>
> These are **publication-model profiles**, not publisher-wide policies. Resolve the exact journal and article type first; current official criteria outrank this file.

## Contents

- [How to use the profiles](#how-to-use-the-profiles)
- [Profile A — selective broad-interest](#profile-a--selective-broad-interest)
- [Profile B — selective field-advancement](#profile-b--selective-field-advancement)
- [Profile C — rigor-first scholarly record](#profile-c--rigor-first-scholarly-record)
- [Profile D — clinical / policy priority](#profile-d--clinical--policy-priority)
- [Profile E — evidence-assessment without post-review gatekeeping](#profile-e--evidence-assessment-without-post-review-gatekeeping)
- [Profile F — conference / deadline-constrained selection](#profile-f--conference--deadline-constrained-selection)
- [Profile selection procedure](#profile-selection-procedure)
- [Do not average incompatible profiles](#do-not-average-incompatible-profiles)
- [Source examples](#source-examples)

## How to use the profiles

The decision engine needs a target-specific objective function. Do not use `novelty + rigor + impact` as a universal acceptance formula.

Resolve:

`exact journal/venue -> article type -> review model -> editorial criteria -> current stage`

Then select the nearest profile only as a fallback. Override any axis with exact current journal guidance.

Every profile separates:

- **editorial triage axes**;
- **reviewer axes**;
- **acceptance/closure condition**;
- **wrong optimization to avoid**.

## Profile A — selective broad-interest

### Typical use

Flagship multidisciplinary or highly selective journals where editors screen for importance/readership in addition to technical merit.

### Editorial triage axes

- originality/advance;
- scientific importance;
- breadth of interest or implications beyond a narrow specialty;
- clarity/readability sufficient for editorial evaluation;
- maturity/completeness of the case;
- exact-journal fit.

### Reviewer axes

- technical soundness;
- strength of evidence for conclusions;
- originality/context;
- field significance;
- data/methodology;
- whether technical failings remain before the case is established.

### Closure condition

A technically sound revision can still fail if the **verified editorial priority/breadth criterion** is no longer met after necessary claim narrowing.

### Wrong optimization

Do not try to create breadth by writing generic societal-impact sentences. Show a real consequence of the finding for a wider scientific question/community.

### Example source models

- flagship Nature;
- PLOS Biology uses originality, field importance, interest outside the field, rigorous methodology and substantial evidence, although exact workflow differs from Nature.

## Profile B — selective field-advancement

### Typical use

Engineering, computing and society journals/venues where scope, novelty, validity and meaningful advancement within the field are explicit.

### Editorial triage axes

- exact publication scope;
- contribution and novelty;
- completeness/maturity;
- importance to the field/community;
- compliance with article/venue requirements.

### Reviewer axes

- sound methods/design;
- correct data analysis/interpretation;
- reproducibility;
- literature completeness and fair positioning;
- logical flow and supported conclusions;
- clarity/presentation;
- field advancement.

### Closure condition

The manuscript needs a credible field contribution with methods/results sufficient to support it. Broad interdisciplinary appeal is not automatically required unless the exact venue says so.

### Wrong optimization

Do not imitate flagship-general-science breadth at the expense of technical precision or community-specific value.

### Example source models

- IEEE Author Center exposes scope, novelty, validity, data, clarity, compliance and advancement as distinct checks.
- ACM review criteria vary by conference/journal and must be resolved per venue.

## Profile C — rigor-first scholarly record

### Typical use

Journals whose publication criterion emphasizes technical/scientific rigor and ethical validity rather than perceived novelty or importance.

### Editorial triage axes

- scope;
- basic scientific/ethical eligibility;
- completeness for review;
- obvious technical/integrity blockers.

### Reviewer axes

- technical rigor;
- valid methods/analysis;
- data support for claims;
- fair literature context;
- reproducibility/reporting;
- ethical/policy compliance.

### Closure condition

If the work is technically rigorous, ethically sound, correctly reported and the conclusions follow, lack of perceived high impact should not be converted into a rejection reason when the journal explicitly rejects impact-based gatekeeping.

### Wrong optimization

Do not inflate novelty, significance or general interest to satisfy criteria the journal intentionally does not use.

### Example source model

PLOS ONE states that peer review determines technical rigor and scientific/ethical eligibility rather than whether the work reaches a perceived importance threshold.

## Profile D — clinical / policy priority

### Typical use

Selective medical/public-health journals where technical validity is necessary but priority depends on importance of the clinical/public-health question and implications for care, policy or research agendas.

### Editorial triage axes

- importance of the research question;
- study-design credibility;
- potential clinical/public-health/policy relevance;
- sufficiency of the body of work;
- accessibility to relevant non-specialist clinicians/policymakers when required.

### Reviewer axes

- quality/priority;
- originality;
- validity of data/design;
- reasonableness of conclusions;
- reporting-guideline adherence;
- effect magnitude/uncertainty;
- clinical/generalizability implications and harms.

### Closure condition

A statistically correct result may still lack priority if it does not materially change knowledge/practice under the exact target's criteria. Conversely, priority language cannot rescue weak causal identification or inadequate data.

### Wrong optimization

Do not equate statistical significance with clinical importance, and do not convert observational association into intervention guidance.

### Example source models

- PLOS Medicine explicitly considers important questions, substantial advance and implications for care/policy/research agendas.
- JAMA Network reviewer guidance separates quality, priority, originality, data validity and reasonableness of conclusions.

## Profile E — evidence-assessment without post-review gatekeeping

### Typical use

Publication models where reviewed work receives a structured assessment rather than a conventional post-review accept/reject judgement.

### Editorial triage axes

- whether the work is appropriate to send for review under the journal's selection model;
- article/scope eligibility;
- whether review can produce a useful public assessment.

### Reviewer/editor assessment axes

Keep **significance of findings** separate from **strength of evidence**.

For example, a finding can be narrowly useful but supported by compelling evidence, or highly important but currently supported by incomplete evidence.

### Closure condition

Do not manufacture an `acceptance probability` where the publication model does not use conventional post-review acceptance. Optimize the manuscript to improve the accuracy/strength of its public assessment and evidentiary support.

### Wrong optimization

Do not collapse significance and evidence strength into one prestige score.

### Example source model

eLife Assessments use separate vocabularies for significance and strength of evidence and, under its reviewed-preprint model, do not use conventional accept/reject decisions after peer review.

## Profile F — conference / deadline-constrained selection

### Typical use

Competitive conference review where decisions are selection under a fixed program/deadline rather than indefinite journal-style revision.

### Editorial/program triage axes

- scope/relevance to attendees;
- contribution/novelty/significance;
- technical soundness/completeness;
- reproducibility/resources where expected;
- clarity;
- comparison against competing submissions under capacity constraints.

### Reviewer axes

- soundness/validity;
- novelty/significance;
- prior work;
- reproducibility/data/code;
- presentation;
- limitations/ethics;
- whether the work is sufficiently complete for the submitted version.

### Closure condition

A concern that might be repairable over months in a journal can be decision-critical under a conference deadline if the current version does not establish the claim.

### Wrong optimization

Do not assume a `major revision` path exists. Engineer the submitted paper to make the current evidence complete enough for the venue's decision cycle.

## Profile selection procedure

1. Open the exact current journal/venue criteria.
2. Identify whether perceived significance/priority is an explicit publication gate.
3. Identify whether broad readership is required or field-local value is enough.
4. Identify whether reviewers assess significance or mainly validity/rigor.
5. Identify whether revision is iterative, bounded, or absent.
6. Identify whether acceptance is conventional or replaced by an assessment/publication model.
7. Select the closest profile.
8. Record exact deviations from the profile.

A manuscript transfer may change the decision objective while the underlying science stays the same.

## Do not average incompatible profiles

Bad approach:

`acceptability = 20% novelty + 20% rigor + 20% impact + 20% breadth + 20% clarity`

This creates fake precision and contradicts journals with different missions.

Instead, model **gates plus target-specific priorities**. Examples:

- rigor-first journal: validity may be a hard gate while impact is not a gate;
- selective broad-interest journal: validity is a hard gate and breadth/priority is an additional editorial gate;
- evidence-assessment model: significance and evidence strength remain separate reported dimensions.

## Source examples

Current public pages reviewed 2026-08-19:

- Nature editorial criteria and peer-review policy.
- IEEE Author Center peer-review guidance.
- PLOS ONE reviewer guidelines and Academic Editor philosophy.
- PLOS Biology/PLOS Medicine reviewer/editorial criteria.
- JAMA Network reviewer guidance.
- eLife Assessment definitions and current reviewed-preprint model.
- ACM venue-specific review criteria; exact ACM venue rules must be checked at use time.

This file is a resolver aid, not a substitute for the exact journal's current author/editor/reviewer documentation.