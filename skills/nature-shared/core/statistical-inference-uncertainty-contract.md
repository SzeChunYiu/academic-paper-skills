# Statistical Inference and Uncertainty Engineering Contract

Use this contract after a study/protocol record and immutable analysis-ready
data snapshot exist, and before quantitative Results, tables, displays,
captions, claims, or readiness statements are treated as current.

The contract is a **decision and provenance layer**, not a universal statistics
recipe. It composes obligations for the recorded context and checks bounded
contradictions. It never selects a universal best test, model, prior, interval,
threshold, visualization, or acceptance strategy.

## Authority chain

```text
question / bounded claim
-> estimand or target quantity
-> analysis population and independent unit
-> dependence, missingness, multiplicity, and decision plan
-> immutable analysis input
-> executed estimator/model/test
-> diagnostics and sensitivity
-> estimate + typed uncertainty
-> table/display/caption/prose bindings
-> bounded claim
```

Statistics owns numerical and inferential semantics across manuscript
surfaces. The scientific-display contract still owns reader task,
representation choice, rendering, accessibility, caption completeness, and
visual lineage. A chart cannot repair an invalid analysis; a valid analysis
does not choose the chart automatically.

## Load only what is needed

- schema: `../analysis-contracts/statistical-inference-uncertainty-contract.schema.json`
- maintained adapters: `../analysis-contracts/maintained-analysis-adapters.json`
- evaluator: `../scripts/resolve_statistical_inference.py`
- evidence ledger, when a rule or transfer boundary needs inspection:
  `../research/statistical-inference-uncertainty-evidence-ledger-2026-08.md`

## 1. Resolve context without forcing a method

Resolve:

```text
analysis family
× study archetype
× design/dependence tags
× inference mode
× exact domain/regulator/venue policy
× as-of date
```

The maintained catalog currently covers general estimation, randomized and
observational work, diagnostic and prediction studies, evidence synthesis,
animal/preclinical work, omics/high-dimensional testing, simulation and
benchmarks, hierarchical/repeated/clustered designs, time-to-event analysis,
Bayesian analysis, equivalence/noninferiority, and an explicit
non-quantitative boundary.

Adapters are composable. They return obligations, hard-check classes, source
references, and transfer limits. They are not proof that the selected method is
correct. When no adapter matches, keep `unmatched_analysis_domain` unresolved
and research current methodological and official sources. Do not invent a
universal fallback.

## 2. Define the scientific target first

For every important result record:

- question and linked claim identity;
- population;
- conditions/exposure/comparator;
- outcome or target;
- time horizon;
- intercurrent-event handling when relevant;
- summary/effect measure and scale;
- direction of benefit/harm;
- analysis population;
- intended decision: descriptive, estimation, superiority, equivalence,
  noninferiority, prediction, calibration, utility, or another explicit class.

Keep estimand, estimator, estimate, test, and decision separate. A P value is
not an effect; a model coefficient is not automatically the scientific target;
a metric name does not define its deployment meaning.

## 3. Identify the actual independent unit and dependence

Record observation, assignment, analysis, cluster, and independent units
separately. Record observation count, independent-unit count, reported `n`, and
cluster count where applicable.

Subsamples, fields, wells, sections, repeated time points, augmentations, CV
folds, patches, prompts, seeds, and simulation replicates are not automatically
independent scientific units. If dependence exists, record how it was modeled,
aggregated, randomized, resampled, or otherwise handled and bind that decision
to an execution receipt.

Do not let a larger row count create false precision.

## 4. Bind plan, data, and execution

Preserve:

- protocol and analysis-plan identity and freeze time;
- immutable analysis-ready snapshot identity/hash;
- executed code and environment receipts;
- estimator, model/test, analysis population, independent unit, dependence
  handling, missing-data strategy, and multiplicity method;
- convergence and diagnostic records;
- produced result identities.

A plan, execution, result, or manuscript surface that names an absent upstream
object is not partially verified: its identity chain is broken. The execution's
result manifest and every result's execution identity must agree in both
directions before result-level or cross-surface checks can pass.

A changed estimator, population, missing-data strategy, outcome, hypothesis
family, or decision rule is a versioned deviation—not a prose edit. Preserve
reason, consequence, affected results/claims, classification, and disclosure
status.

Claim narrowing can repair overreach. It cannot create an execution receipt,
valid input snapshot, convergence, independent observations, or
prespecification.

## 5. Resolve multiplicity by objective

For a confirmatory family, record:

- family and hypothesis identities;
- primary/secondary/exploratory hierarchy;
- error criterion;
- method and threshold, if applicable;
- plan and execution receipt.

Do not apply one correction universally. Family-wise error, false discovery,
gatekeeping, hierarchical decisions, selective inference, and exploratory
ranking answer different questions. A transparent exploratory family can
remain uncorrected if its status and inferential boundary are visible; it must
not silently support confirmatory claims.

## 6. Resolve missingness, exclusions, and analysis populations

Record planned, entered, analyzed, missing-outcome, excluded, and group-specific
counts. Bind planned and realized missing-data strategies, assumptions,
receipts, and required sensitivity results. Preserve participant/unit-level
exclusion decisions and denominator changes.

Observed data cannot prove an unverifiable missingness mechanism. When the
conclusion depends on such assumptions, vary plausible assumptions and show
whether the decision changes. A complete-case result cannot silently replace a
planned analysis.

## 7. Preserve magnitude, typed uncertainty, and decision semantics

Every result needs:

- stable identity and linked analysis/estimand/population;
- role and selection status;
- estimate, scale, and unit;
- interval kind, target, level, sidedness, method, bounds, unit, and transform;
- test record when the framework uses one;
- objective, decision state, comparison basis, and margin provenance when
  relevant;
- analyzed and independent `n`;
- adverse/harmful/null/failed status;
- current analysis-receipt hash.

Confidence, credible, posterior predictive, frequentist prediction, bootstrap,
and compatibility intervals are not interchangeable. Bayesian work need not
invent a P value. Descriptive or non-quantitative work must not be forced into
a frequentist confirmatory template.

## 8. Block unsafe inference shortcuts

At minimum, reject these recorded contradictions:

- separate within-group significance tests used to claim a group difference;
- `P > alpha` used to establish no effect or equivalence;
- equivalence/noninferiority without a prospectively justified margin and
  compatible interval decision;
- supported noninferiority without an explicit effect scale, favorable
  direction, required lower/upper interval bound, null value, margin-to-boundary
  relation, and boundary value;
- post-hoc observed power used as evidence after results are known;
- discrimination-only evidence used to claim calibration or clinical utility;
- a future-setting meta-analytic claim without prediction uncertainty;
- a sensitivity analysis targeting a different estimand silently labeled
  robustness of the primary estimand;
- a nonconverged model used for a model-based claim;
- a required diagnostic represented as complete without a receipt.

The valid repair may be a direct contrast, a different executed analysis,
additional diagnostic/sensitivity/calibration work, transparent exploratory
reclassification, or claim narrowing. Do not default to “more experiments”
when the supportable claim can be stated accurately.

## 9. Bind all statistical surfaces

Tables, plot data, figure labels, captions, abstracts, Results sentences,
Discussion restatements, supplements, and responses to reviewers must bind to
the same result identity and current analysis receipt.

Record for every surface:

- result and surface identity/type;
- analysis-receipt hash;
- reported estimate, interval kind/level/bounds, P value if any, and independent
  `n`;
- declared rounding method and tolerance.

Regenerate dependent surfaces when an analysis receipt changes. Do not allow a
table, plot, caption, and prose sentence to drift numerically or change interval
semantics. An orphan surface is blocking rather than exempt from numeric checks.
Preserve planned primary, adverse, harmful, null, inconclusive, and failed
results; omission is not a repair.

## 10. Resolve exact policies as of the scientific object

Resolve consequential domain, regulator, reporting, and exact-venue analysis
rules from current official sources using the contract `as_of_date`. Record
issuer, title, URL, review date, applicability, resolution state,
`effective_from`, `effective_until`, and the basis for those dates.

- Do not backcast a future-effective policy.
- A current page without a historical effective date cannot prove an older
  rule.
- Preserve superseded and conflicting policies as versioned provenance.
- If an exact required policy cannot be established, return `unresolved`; do
  not replace it with an adapter or remembered rule.

## 11. Evaluator states and outputs

The evaluator returns:

- `pass`: no recorded blocker or unresolved required research;
- `blocked`: a structural or semantic contradiction is recorded;
- `unresolved`: no blocker is recorded, but required live research/authority is
  unresolved.

It keeps separate:

- blockers and blocker codes;
- unresolved research and codes;
- repair routes;
- warnings;
- visible deviation classes;
- matched adapters;
- obligations and hard checks;
- source references and transfer limits;
- bounded certification and exclusions.

Run from the `nature-shared` package context or pass explicit paths:

```bash
python scripts/resolve_statistical_inference.py path/to/contract.json
```

Schema-invalid contracts stop before semantic arithmetic or referential work.
An empty receipt can remain schema-valid so the evaluator returns the specific
scientific blocker rather than hiding it behind a shape error.

## 12. Repair hierarchy

Prefer the smallest scientifically honest route:

1. correct an identity/binding/rounding error;
2. restore a missing record or receipt;
3. rerun from the bound input;
4. refit or use a design/estimand-appropriate analysis;
5. add missing diagnostics, sensitivity, multiplicity, calibration, or
   prediction work;
6. disclose/version a deviation and reclassify the analysis;
7. narrow or remove the affected claim;
8. conduct a new prospective study only when the scientific question still
   requires evidence that the current record cannot provide.

Never invent sample sizes, observations, P values, intervals, priors, margins,
diagnostics, policies, prespecification, or analysis receipts.

## Certification boundary

A passing contract certifies only the recorded bounded invariants checked by
this layer. It does **not** certify:

- model adequacy or assumption truth;
- causal identification or absence of bias;
- measurement validity;
- adequate power or precision;
- analytic reproducibility or independent replication;
- external validity or generalization;
- scientific truth;
- reporting-guideline completion;
- journal acceptance.

Those questions require their own evidence, review, and exact decision
contracts.
