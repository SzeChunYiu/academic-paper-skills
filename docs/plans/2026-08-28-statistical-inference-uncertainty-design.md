# Statistical Inference and Uncertainty Engineering Contract Design

## Objective and boundary

Model the layer between an analysis-ready data snapshot and every quantitative
result, table cell, plot interval, caption, statistical sentence, and
claim-strength decision. The contract must detect recorded contradictions and
unsafe inference shortcuts without pretending that a schema, test name, small
P value, confidence interval, posterior, diagnostic, reporting checklist, or
software receipt proves that a model is correct or a scientific claim is true.

This iteration complements rather than replaces the study-protocol, data-
integrity, scientific-display, atomic-claim, and exact-venue contracts.

## Approaches considered

1. **Expand the prose-only statistics checklist.** Backward compatible, but it
   cannot bind estimates or uncertainty to immutable analyses and manuscript
   surfaces.
2. **Mandate one universal statistical workflow.** Easy to automate, but wrong
   for descriptive, frequentist, Bayesian, design-based, prediction, survival,
   meta-analytic, high-dimensional, simulation, and non-quantitative work.
3. **Invariant analysis core plus maintained study/analysis adapters and live
   exact-domain resolution.** Selected. Machine-checkable contradictions are
   common; inferential obligations activate only through matching adapters and
   current official/methodological sources.

## Architecture

The authoritative chain is:

```text
question and claim class
-> estimand / target quantity
-> analysis population and independent unit
-> dependence, missingness, multiplicity, and decision plan
-> immutable data snapshot
-> executed estimator/model/test receipt
-> diagnostics and sensitivity analyses
-> estimate plus correctly typed uncertainty
-> table/display/caption/prose bindings
-> bounded claim
```

A strict JSON Schema stores identity, stage, policy as-of date, adapter and
source provenance, upstream protocol/data bindings, estimand, units and
dependence, analysis population, planned and executed analyses, multiplicity,
missingness, sample-size rationale, diagnostics, estimates, uncertainty,
sensitivity analyses, deviations, and cross-surface bindings. A resolver uses:

`analysis family × study archetype × design tags × inference mode × as-of date`

It returns applicable obligations, hard-check classes, source provenance,
transfer limits, and unresolved live-research needs. It never selects a
universal best test, model, threshold, interval, or chart.

## Maintained adapters and live resolution

The first catalog covers general estimation/reporting, randomized intervention,
observational association/causal analysis, hierarchical/repeated/clustered
data, diagnostic/prediction/ML evaluation, high-dimensional multiplicity,
time-to-event analysis, evidence synthesis/meta-analysis, simulation and
computational benchmarking, Bayesian workflow, and equivalence/non-inferiority.
A non-quantitative/formal boundary prevents the system from fabricating
statistics for qualitative, interpretive, or proof-based papers.

These are maintained starting points, not a claim to encode every discipline,
estimator, regulator, journal, data-generating process, software ecosystem, or
community standard. Unmatched analysis families and consequential exact rules
remain explicit live official/methodological-source research obligations.
Time-versioned provenance prevents future-effective standards from being
backcast and prevents observed-current pages from establishing historical
requirements.

## Bounded automatic checks

The evaluator fails closed on structural invalidity and recorded contradictions,
including analysis-input hash drift, duplicate identities, independent-unit or
dependence mismatch, false use of subsamples as independent `n`, unlogged
plan/execution changes, omitted primary/adverse/null results, unaccounted
confirmatory multiplicity, post-hoc observed power used as evidence, failed
model convergence, required diagnostics represented as complete without a
receipt, missingness handling that contradicts the plan, and cross-surface
estimate/denominator/interval/P-value drift.

Inference-boundary checks reject several high-risk shortcuts: separate
significance tests cannot establish a between-group difference; `P > alpha`
cannot establish equivalence or absence of a meaningful effect; equivalence or
non-inferiority requires a justified, prospectively fixed margin; confidence,
credible, prediction, bootstrap, and compatibility intervals are not
interchangeable; and a sensitivity analysis targeting a different quantity
cannot silently be called robustness of the original estimand.

Exploratory multiplicity, Bayesian analyses, descriptive studies, and
non-quantitative work are not forced into a frequentist confirmatory template.
Unknown or scientifically judgment-dependent items remain unresolved rather
than being converted into invented facts.

## Repairs and certification boundary

Valid repairs preserve provenance: resolve the true independent unit; refit an
appropriate model; rerun from the bound snapshot; disclose and version a
deviation; add justified multiplicity, missing-data, diagnostic, calibration,
or sensitivity work; correct every dependent surface; reclassify an analysis
as exploratory; or narrow/remove the affected claim. Invalid repairs include
inventing sample sizes, P values, intervals, priors, margins, diagnostics,
analysis receipts, or prespecification.

Claim narrowing can repair an inference that outruns an executed analysis. It
cannot create an analysis execution, independent observations, convergence,
missing data, a prespecified margin, or a valid data snapshot.

Passing certifies only the recorded bounded invariants. It does not certify
model adequacy, assumption truth, causal identification, absence of bias,
measurement validity, adequate power/precision, reproducibility, external
validity, scientific truth, reporting-guideline completion, or journal
acceptance.

## Research and test strategy

The evidence registry separates peer-reviewed full-text readings,
abstract/metadata-only readings, reporting guidelines, regulatory/technical
standards, and current official policies. Each source records read depth,
supported decisions, limits, contradictions, dates, and update triggers. A
frozen multi-query discovery log documents breadth without claiming a
systematic review.

Behavior fixtures must demonstrate at least: valid bounded frequentist and
Bayesian routes; pseudoreplication detection; direct-interaction versus
separate-significance logic; non-significance versus equivalence; multiplicity
and missingness deviations; confidence-versus-prediction interval drift;
future-effective policy handling; claim narrowing as a valid but limited repair;
and explicit non-universal/no-statistics objectives. Canonical academic-writing,
academic-paper-pipeline, nature-statistics, and additive project-state
integration are required.
