# Study protocol and conduct evidence ledger — 2026-08

**Purpose:** research basis for the versioned study protocol/conduct contract,
its maintained study-type adapters, and its automatic blockers. This is not a
universal checklist and not a substitute for domain expertise, ethics authority,
or scientific review.

**Frozen search date:** 2026-08-28  
**Machine-readable registry:**
`../study-contracts/study-protocol-evidence-registry.json`  
**Frozen broad-search log:**
`study-protocol-conduct-search-log-2026-08-28.json`  
**Current included corpus:** 39 sources: 19 read in full text and 20 read at
abstract level.

## Search and screening protocol

Broad discovery used OpenAlex, with DOI/title reconciliation through Crossref.
Abstracts and open full text were read through Europe PMC, publisher
versions-of-record, and JMLR. Twelve query families produced 84 frozen records:

1. preregistration and Registered Reports;
2. protocol-publication outcome switching;
3. randomization, allocation concealment, and blinding;
4. stopping flexibility, power, and sample-size rationale;
5. deviations, intervention fidelity, and adherence;
6. observational target-trial design;
7. computational leakage and benchmark reproducibility;
8. animal-study design rigor;
9. systematic-review protocols and exact search provenance;
10. qualitative reflexivity, saturation, and data adequacy;
11. FAIR data, raw-result provenance, and analytic reproducibility;
12. reporting-guideline adherence and limitations.

Targeted reference-chain and standards follow-up produced the included set.
Included sources had to support a specific contract field or blocker through
empirical/meta-research, a bounded methods evaluation/framework, or a major
reporting standard with explicit scope. Citation count, venue prestige, and
checklist popularity were not evidence of quality. DOI/title mismatches were
excluded; read depth is recorded rather than implied.

This iteration stopped after every maintained adapter had multiple relevant
sources, every automatic blocker had empirical or methodological support, and
new searches mainly produced domain refinements rather than missing universal
fields. It is not an exhaustive systematic review.

## Governing synthesis

The protocol/conduct object must preserve:

```text
question and estimand
-> protocol version and freeze timing
-> analysis-plan version
-> executed conduct and raw-data receipt
-> deviations and amendments
-> analysis execution
-> bounded claim status
```

No single indicator collapses this chain. In particular:

- registration is not design validity;
- checklist completion is not verified execution;
- reproducible rerun is not independent replication;
- randomization named in prose is not proof the sequence was executed;
- preregistration does not turn weak measurement into strong evidence;
- exploration is not defective when labeled honestly;
- a deviation is not erased by a clean final Methods section.

## Evidence by decision family

### 1. Timing controls whether a claim is predictive or postdictive

Nosek et al. define preregistration around specifying questions and analysis
before observing outcomes, distinguishing prediction from postdiction. Munafò et
al. explain how data-contingent choices in outcomes, exclusions, covariates,
models, and stopping can inflate findings. Simmons et al. demonstrate through
simulation and experiments that undisclosed flexibility can sharply increase
false-positive results. Registered Reports move review before results; Chambers
and Tzavella explicitly caution that this model is not a universal solution.

**Contract consequence:** record actual protocol/SAP freeze time relative to
data and outcome access. A false prospective label blocks. Existing-data work
can remain valuable but must be labeled according to what was knowable when the
plan was frozen.

**Transfer limit:** not all science is confirmatory, and not every qualitative,
descriptive, discovery, theory, or emergency study should be forced through the
same registration mechanism.

### 2. Outcome switching and selective reporting require version comparison

Chan et al.'s protocol-publication cohort found incomplete efficacy and harm
reporting and at least one changed, introduced, or omitted primary outcome in
62% of trials. Dwan et al.'s updated systematic review found direct evidence of
publication and outcome-reporting bias; across included protocol comparisons,
40–62% of studies had a changed, introduced, or omitted primary outcome.

**Contract consequence:** protocol, analysis plan, collected outcomes, reported
primary outcomes, and claims are separate linked objects. A difference is not
silently normalized. It needs a dated deviation, reason, affected claims,
inference consequence, and visible manuscript locations.

**Allowed repair:** restore the prespecified outcome; disclose and version the
change; reclassify/narrow the claim; add sensitivity analysis; or conduct a new
prospective study. Backdating or retroactive renaming is never a repair.

### 3. Planned randomized-trial safeguards must be checked as executed

Wood et al.'s meta-epidemiological analysis found larger average effects with
inadequate/unclear concealment or lack of blinding for subjective outcomes, but
little evidence of the same average bias for objective outcomes. Savović et al.
also found average exaggeration and increased heterogeneity associated with
unclear/inadequate sequence generation, concealment, or blinding, mainly for
subjective outcomes. The evidence therefore supports execution-specific fields
and outcome-sensitive interpretation—not a universal numerical penalty.

SPIRIT 2025 and CONSORT 2025 provide current protocol/report fields for
randomized trials, including outcomes, harms, participant flow, protocol/SAP
access, and open-science records. TIDieR separates planned from actual
intervention delivery. Carroll et al. define fidelity through adherence in
content, frequency, duration, and coverage, moderated by delivery quality,
responsiveness, facilitation, and complexity.

**Contract consequence:** assignment sequence, concealment, blinding roles,
fidelity, harms, stopping, exclusions, and participant flow need conduct
receipts. Methods prose is not an execution receipt.

### 4. Reporting standards expose records but do not certify quality

STROBE explicitly says it guides reporting, is not a design/conduct
prescription, and is not a quality-assessment instrument. PRISMA-S explicitly
says it guides reporting rather than conduct. The same boundary applies to
SPIRIT, CONSORT, ARRIVE, COREQ, and SRQR: the fields help readers see the record;
they do not prove the record is unbiased or correct. Samaan et al.'s scoping
review also found reporting-guideline adherence remained widely suboptimal.

**Contract consequence:** `reporting_complete`, `protocol_traceable`,
`conduct_traceable`, `scientifically_valid`, and `journal_accepted` are separate
states. The automatic evaluator returns only bounded traceability results.

### 5. Observational causal work needs a target design, not randomized language

Hernán and Robins frame observational causal analysis as emulation of an
explicit target trial. Their related time-zero paper shows how aligning
eligibility, treatment assignment, and start of follow-up prevents avoidable
immortal-time errors. STROBE requires readers to be able to distinguish what was
planned, done, found, and inferred.

**Contract consequence:** causal observational adapters ask for target
population, strategies, eligibility, time zero, follow-up, estimand,
confounders, identification assumptions, missingness, and sensitivity analyses.

**Transfer limit:** target-trial framing does not remove unmeasured confounding,
prove positivity, or apply to every descriptive/associational study.

### 6. Computational studies need leakage and execution provenance

Kapoor and Narayanan document cross-disciplinary machine-learning leakage:
train/test non-independence, preprocessing on held-out data, and reuse of test
feedback can produce irreproducible scientific performance. Their review is a
documented lower bound, not a prevalence meta-analysis. Pineau et al. connect
machine-learning reproducibility to code, data, hyperparameters, seeds,
resources, and result variability. Sandve et al. require raw-to-result workflow,
versions, parameters, intermediates, seeds, and source data behind displays.

Baggerly and Coombes show that weak provenance can hide simple indexing and
labeling errors with clinical consequences. Stodden et al. obtained artifacts
for 44% and reproduced findings for 26% of a random sample governed by an
availability-on-request policy. Hardwicke et al. show that availability,
reusability, and analytic reproducibility are distinct states.

**Contract consequence:** bind data snapshot, unit/group/time split,
preprocessing fit scope, labels, code/environment, seeds, selection budget, and
evaluation receipt. Overlap or all-data preprocessing blocks a held-out claim.

**Transfer limit:** exact rerun does not establish independent replication,
generalization, fairness, or conceptual correctness.

### 7. Animal/preclinical records need unit, bias-reduction, exclusions, and welfare

ARRIVE 2.0 exposes experimental unit, sample-size rationale, inclusion/exclusion,
randomization, blinding, outcomes, statistics, procedures, and welfare. Kilkenny
et al.'s survey found widespread omission of core design and analysis details.
Macleod et al. found limited reporting of bias-reduction measures and lower
reported randomization in higher-impact journals, directly refuting prestige as
a conduct proxy. Landis et al. prioritize sample-size estimation, randomization,
blinding, and data handling.

**Contract consequence:** the animal adapter records actual execution and
distinguishes `unknown`, `not done`, and `not applicable`. It also requires the
true experimental unit and relevant hierarchy such as cage, litter, batch, or
operator.

### 8. Systematic reviews need exact search and amendment provenance

PRISMA-P defines protocol fields; PRISMA 2020 connects final reporting to
registration, protocol, amendments, selection, extraction, risk of bias,
synthesis, certainty, and availability. PRISMA-S requires database and platform,
exact copied search strings, dates, limits, supplementary routes,
deduplication, and any search peer review.

**Contract consequence:** review searches are executable/versioned study
conduct, not a prose summary. Later search changes remain amendments.

**Transfer limit:** PRISMA completion does not prove exhaustiveness, correct
eligibility decisions, low bias, or valid synthesis. Specialized reviews need
extensions.

### 9. Qualitative adequacy is study-specific

COREQ structures interview/focus-group reporting around research team and
reflexivity, study design, and analysis/reporting. SRQR deliberately preserves
flexibility across paradigms. Guest et al. operationalized saturation in one
study but cannot supply a universal count. Malterud et al. instead frame sample
adequacy through information power: aim, specificity, theory, dialogue quality,
and analysis strategy. Vasileiou et al. found sample-size justification was
often absent and recommended study-specific data-adequacy reasoning.

**Contract consequence:** record orientation, researcher position, context,
sampling rationale, consent, data generation, coding/interpretation, negative
cases, and evidence excerpts. Ask for saturation only when the method uses it.

**Transfer limit:** neither “12 interviews” nor universal preregistration is a
valid qualitative hard gate.

### 10. Data stewardship and sensitivity are independent dimensions

The FAIR principles support findability, governed accessibility,
interoperability, and reuse for data and workflows, while explicitly preceding
implementation and not constituting one technical standard. Sensitive data can
remain governed rather than open. Lakens distinguishes several legitimate
sample-size rationales and requires alignment with inferential goals. Cro et al.
define sensitivity analysis as testing conclusions against changes in
assumptions, models, values, and analytic choices.

**Contract consequence:** openness is not universal, but asset identity,
governance, versions, transformations, known defects, and access conditions are.
Sample-size and sensitivity fields preserve rationale without imposing one
calculation on every design.

## Automatic-blocker justification

| Blocker | Evidence basis | Boundary |
|---|---|---|
| false prospective status | `nosek-2018`, `simmons-2011`, `munafo-2017` | timing classification only; not a validity score |
| undisclosed primary-outcome change | `chan-2004`, `dwan-2013`, `spirit-2025`, `consort-2025` | a disclosed change can remain usable with a changed claim status |
| randomization execution unverified | `wood-2008`, `savovic-2012`, `consort-2025` | bias impact varies by outcome and context |
| undisclosed blinding deviation | `wood-2008`, `savovic-2012`, `munafo-2017` | not every role/design can be blinded |
| stopping/exclusion lineage incomplete | `simmons-2011`, `arrive-2020`, `consort-2025` | deviations may be legitimate but must remain visible |
| adverse-event omission | `chan-2004`, `consort-2025` | field-specific harms definitions still apply |
| evaluation leakage | `kapoor-2023`, `pineau-2021`, `sandve-2013` | split unit and deployment target determine leakage |
| confirmatory label unsupported | `nosek-2018`, `chambers-2021`, `munafo-2017` | honest exploratory work remains valid research |
| required ethics authority missing | reporting and governance standards plus non-invention rule | no prose-only or claim-only repair creates retrospective authority |

## Contradictions and transfer limits

1. **Preregistration versus exploration:** preregistration clarifies prediction;
   it must not stigmatize transparent exploration.
2. **Blinding versus feasibility:** blinding reduces some biases, especially for
   subjective outcomes, but some interventions/roles cannot be blinded.
3. **Reporting versus conduct:** absence of a report can mean unknown, while a
   report can still be inaccurate. Preserve planned, executed, and verified as
   separate states.
4. **FAIR versus open:** accessible under governed conditions can be FAIR;
   sensitive data must not be exposed merely to satisfy an openness slogan.
5. **Reproducibility versus replication:** rerunning code is not an independent
   test of the scientific claim.
6. **Saturation versus information power:** qualitative adequacy has no universal
   numerical threshold.
7. **Target-trial design versus causal proof:** explicit emulation improves
   design clarity but does not eliminate confounding or measurement error.
8. **Checklist adherence versus certification:** no maintained adapter may turn
   reporting completion into a scientific-quality or acceptance certificate.

## Remaining research gaps

- laboratory assay calibration, measurement-system analysis, and metrology;
- multi-omics batch effects and preprocessing provenance;
- spatial, longitudinal, clustered, stepped-wedge, adaptive, platform, and
  non-inferiority designs;
- diagnostic/prognostic studies and current STARD/TRIPOD+AI extensions;
- implementation, economic, mixed-methods, participatory, Indigenous, and
  community-governed research;
- formal proof development, theorem dependency, and computer-assisted proof
  conduct records;
- software engineering experiments, human-computer interaction, and simulation
  validation;
- lab notebooks, instruments, calibration files, chain of custody, and operator
  competence;
- protocol-deviation taxonomies outside clinical trials;
- prospective evidence on whether automated contract warnings improve conduct;
- field-specific ethics, biosafety, dual-use, privacy, and data-sovereignty law.

These should become separate researched adapters. Unknown domains must stay
unresolved rather than inheriting a convenient checklist.

