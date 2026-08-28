# Statistical Inference and Uncertainty Evidence Ledger

**Registry:** `statistical-inference-evidence-registry-2026-08-28`  
**Reviewed:** 2026-08-28  
**Scope:** evidence for the bounded statistical-inference and uncertainty
contract, maintained analysis adapters, automatic contradiction checks, repair
routes, and certification exclusions.

This is a targeted, reconciled evidence review, **not** a systematic review and
not a claim that every statistical discipline or method has been encoded. The
frozen discovery log contains 16 Europe PMC queries and 128 query-level
metadata records. OpenAlex and Crossref returned HTTP 429 during discovery;
that limitation and the biomedical weighting of Europe PMC are preserved in
the log. Metadata screening discovered candidates. It did not count as reading
evidence for a contract rule.

The separate machine-readable registry contains 65 reconciled sources: 46
full-text readings, 9 abstract-level readings, 3 metadata-only boundary
records, and 7 official guideline/policy readings. One additional issuing-body
technical report was read in full. Every source records its supported decisions,
limits, read depth, URL, access date, and metadata-verification statement.

## Governing synthesis

The evidence does not support a universal best statistical test, model, prior,
interval, threshold, chart, or workflow. It does support a common authority
chain:

```text
question / bounded claim
-> estimand or target quantity
-> population and independent unit
-> dependence, missingness, multiplicity, and decision plan
-> immutable analysis input
-> executed estimator/model/test and diagnostics
-> estimate plus typed uncertainty
-> table/display/caption/prose bindings
-> bounded claim
```

The evaluator therefore automates only recorded identity and contradiction
checks. Analysis-specific obligations are composed from maintained adapters.
An unmatched domain, consequential regulator rule, or exact venue policy stays
an explicit live-research task.

## Decision ledger

| Contract decision | Main evidence | Supported behavior | Transfer boundary |
|---|---|---|---|
| Separate estimand, estimator, and estimate | ICH E9(R1); ICH E9 | Bind population, condition, outcome, time, intercurrent-event handling, summary measure, analysis, and estimate | Regulatory clinical-trial vocabulary must be adapted, not imposed unchanged, outside its scope |
| Report magnitude and uncertainty, not a threshold alone | ASA statement; Wasserstein et al.; Greenland et al.; SAMPL | Preserve estimates, interval semantics, exact method, denominators, context, and transparent decisions | None of these sources makes one inferential framework universal |
| Do not infer truth, importance, or absence from a P value | ASA statement; Greenland et al.; McShane et al.; Altman and Bland | Block `P > alpha -> no effect` and threshold-only scientific conclusions | Equivalence, precision, Bayesian, and decision-theoretic objectives require their own rules |
| A difference between significance decisions is not a tested difference | Gelman and Stern | Require a direct contrast/interaction for a between-condition claim | Exact contrast and model depend on the estimand and dependence structure |
| Independent `n` is not the observation count | Lazic 2010/2018; ARRIVE 2.0; SuperPlots | Record assignment, analysis, observation, cluster, and independent units separately; block pseudoreplication | Detecting hierarchy does not choose a mixed model, aggregation rule, or degrees-of-freedom method |
| Diagnostics require target, outcome, and receipt | Hoekstra et al.; BARG; Vehtari et al.; Gabry et al. | Record what was checked, how, with what result, and the consequence; block represented completion without a receipt | A diagnostic receipt cannot prove the model or assumptions are true |
| Confirmatory multiplicity requires a declared family and objective | FDA multiple-endpoints guidance; ICH E9; Noble; Benjamini-Hochberg | Preserve the hypothesis family, FWER/FDR or other objective, method, timing, and receipt | Exploratory analysis can remain unadjusted when honestly labeled; no correction is universal |
| Missing data need a plan, executed handling, assumptions, and sensitivity | Little et al.; Sterne et al.; TARMOS | Bind counts/patterns, planned and realized strategy, imputation/model receipts, deviations, and MNAR sensitivity where relevant | No universal missingness mechanism or imputation model can be inferred from observed data |
| Observed post-result power adds no independent inferential evidence | Greenland et al.; Lakens sample-size justification; Gelman and Carlin | Preserve prospective sample-size reasoning; use observed estimate and uncertainty after analysis | Feasibility, precision, assurance, and power are different prospective objectives |
| Equivalence/noninferiority require a justified bound | Lakens 2017/2018; FDA noninferiority; ICH E9 | Require prospective margin provenance and interval-based decision; nonsignificance is insufficient | Margin, population, interval direction, and regulatory convention are domain-specific |
| Sensitivity labeled robustness must preserve the target estimand | ICH E9(R1); Thabane et al.; Steegen et al. | Record the assumption varied, scenario, plausibility, target, receipt, and decision change | A different estimand is informative but cannot silently certify robustness of the original target |
| Confirmatory/exploratory timing and deviations must remain visible | Nosek et al.; Dwan et al.; CONSORT 2025 | Bind plan freeze, execution, visible deviations, selection status, and affected claims | Preregistration is not validity; legitimate exploration remains valuable when labeled |
| Planned adverse, harmful, null, and failed results cannot disappear | CONSORT 2025; CONSORT Harms; Dwan et al. | Preserve planned-result identities, denominators, harms, failures, exclusions, and non-supportive outcomes | This is a visibility rule, not proof that outcome ascertainment was complete |
| Interval kinds are not interchangeable | Cumming et al.; Hoekstra et al.; meta-analysis prediction-interval sources; BARG | Type confidence, credible, prediction, bootstrap, or compatibility intervals and keep that type consistent across surfaces | Interpretation remains conditional on the relevant model and target |
| Cross-surface values need one result authority | Cole et al.; Dwan et al.; SAMPL | Bind tables, displays, captions, and prose to result and analysis receipts with declared rounding tolerance | Matching values do not establish that the underlying analysis is correct |
| Future-setting meta-claims need prediction uncertainty | Cochrane Handbook; Guddat et al.; Inthout et al. | Distinguish pooled-mean confidence from a future-setting prediction interval and expose heterogeneity | Prediction intervals also depend on model adequacy, study exchangeability, and enough studies |
| AUC/discrimination alone cannot establish calibration or utility | TRIPOD+AI; Van Calster et al.; Vickers and Elkin | Separate discrimination, calibration, clinical utility, validation context, and uncertainty | Clinical prediction guidance does not define universal deployment, fairness, or benefit thresholds |
| Survival displays and inference must preserve risk/censoring semantics | KMunicate; Austin et al.; Pocock et al. | Record time origin, endpoint, risk sets, censoring, competing risks, uncertainty, and late-follow-up limits | Kaplan-Meier, cumulative incidence, cause-specific, and subdistribution targets are not interchangeable |
| Simulation and benchmark results need execution and variance receipts | Morris et al.; Koehler et al.; Bouthillier et al.; Pineau et al. | Record design factors, data-generating mechanisms, Monte Carlo error, failures, seeds/splits/trials, budgets, and environment | Reproducibility and low Monte Carlo error do not prove realistic scenarios or external validity |
| Bayesian work must not be forced into a frequentist template | BARG; Vehtari et al.; Gabry et al. | Record priors, likelihood, computation, convergence/ESS, posterior and predictive checks, sensitivity, and typed posterior uncertainty | No universal prior, Bayes-factor threshold, interval, or convergence cutoff follows |
| Non-quantitative work must not receive invented statistics | SRQR; COREQ; NASEM terminology boundary | Route to the relevant interpretive, qualitative, historical, or formal standards; do not fabricate P values or intervals | SRQR/COREQ cover selected qualitative traditions, not proof papers or every interpretive method |

## Maintained adapter coverage

The first catalog contains 14 composable adapters:

1. general estimation/reporting;
2. randomized intervention;
3. observational epidemiologic;
4. diagnostic accuracy;
5. prediction model/ML;
6. systematic review/meta-analysis;
7. animal/preclinical;
8. omics/high-dimensional;
9. simulation/computational benchmark;
10. hierarchical/repeated/clustered;
11. time-to-event;
12. Bayesian analysis;
13. equivalence/noninferiority;
14. qualitative/non-quantitative boundary.

Each profile cites at least two registry sources and declares transfer limits.
Profiles may compose: for example, a randomized repeated-measures study activates
general estimation, randomized-intervention, and hierarchical obligations. The
resolver returns obligations and hard-check classes, never a recommended
universal method.

## Contradictions and tensions retained

### Threshold decisions versus estimation

Regulatory confirmatory settings can require prespecified error control and
decision thresholds. ASA/meta-research sources warn that a threshold is not a
complete scientific interpretation. The contract preserves both: exact
confirmatory decision rules can be required, but they cannot be relabeled as
truth, magnitude, importance, or absence of bias.

### Error control versus exploratory discovery

Multiplicity guidance supports prospective family-wise or false-discovery
objectives where claims require them. Preregistration and transparency sources
also support exploration when honestly labeled. The evaluator therefore blocks
silent unaccounted confirmatory families but does not force confirmatory error
control onto a transparent exploratory objective.

### Confidence intervals versus Bayesian uncertainty

Frequentist sources warn against posterior-probability readings of confidence
intervals. Bayesian sources require priors, computation diagnostics, posterior
checks, and sensitivity. The schema permits a Bayesian result with no P value
and a credible interval; cross-surface checks preserve the interval's type.

### Reporting completion versus scientific validity

CONSORT, STROBE, STARD, PRISMA, ARRIVE, TRIPOD+AI, SAMPL, BARG, SRQR, and COREQ
can improve visibility and auditability. None makes checklist completion proof
of unbiased design, valid measurement, adequate assumptions, causal
identification, reproducibility, truth, or acceptance. Those exclusions are
part of the evaluator output.

## Repair boundaries

Evidence-supported repairs include:

- recover the true independent unit and refit/aggregate appropriately;
- rerun from the bound immutable snapshot;
- execute and preserve required diagnostics or sensitivity analyses;
- correct multiplicity, missing-data, calibration, survival, or prediction-
  interval work for the actual objective;
- disclose/version a deviation and reclassify confirmatory versus exploratory
  status;
- regenerate every table/display/caption/prose surface from the current result;
- narrow or remove a claim that outruns the executed evidence.

Claim narrowing is a valid scientific repair for overreach. It cannot create
independent observations, a missing analysis, convergence, a data snapshot,
prespecification, a noninferiority margin, a diagnostic, a missing-data
analysis, or an execution receipt. Inventing any of those is prohibited.

## Time-versioned policy rule

Official analysis, regulator, reporting, and venue sources are resolved as of
the contract date. A future-effective rule is not backcast. A page observed
active today without a historical effective date cannot establish an earlier
requirement. Superseded or conflicting rules remain versioned, and unresolved
historical authority stays unresolved until a dated official archive is found.

## Certification boundary

A passing contract certifies only the recorded bounded invariants that were
actually checked. It does **not** certify model adequacy or assumption truth,
causal identification, absence of bias, measurement validity, adequate power or
precision, analytic reproducibility, independent replication, external
validity, scientific truth, reporting-guideline completion, or journal
acceptance.

## Update triggers

Re-review the registry and affected adapters when:

- official guidance is superseded or corrected;
- a new analysis family or domain standard is encountered;
- a blocker or repair route is challenged by stronger evidence;
- an exact venue/regulatory requirement becomes consequential; or
- the scheduled review date, 2027-02-28, is reached.

