# Methods writing guide

The Methods section explains **how the evidence was generated and why the procedure is credible enough to support the paper's inferences**. A computational pipeline is one subtype, not the universal model.

## Contents

- [Core reader questions](#core-reader-questions)
- [Build the method map](#build-the-method-map)
- [Credibility moves](#credibility-moves)
- [Rationale: explain consequential choices](#rationale-explain-consequential-choices)
- [Common organizing principles](#common-organizing-principles)
- [Experimental science](#experimental-science)
- [Clinical / epidemiological](#clinical--epidemiological)
- [Computational / algorithmic](#computational--algorithmic)
- [Qualitative / social science](#qualitative--social-science)
- [Theory / simulation](#theory--simulation)
- [Paragraph and sentence logic](#paragraph-and-sentence-logic)
- [Reproducibility boundary](#reproducibility-boundary)
- [Audit](#audit)

## Core reader questions

Methods should let a competent reader determine:

1. What was studied, measured, modeled, sampled, constructed, or analyzed?
2. How were observations/evidence generated?
3. Which choices materially affect interpretation?
4. What controls, comparisons, validation, or checks support credibility?
5. How were uncertainty, bias, confounding, error, or alternative explanations handled?
6. Can the work be understood, reproduced, or independently evaluated at the level expected in this field?
7. Were ethics, registration, consent, data/code, or reporting obligations satisfied where applicable?

Do not use one generic `motivation -> design -> technical advantage` template to answer all seven.

## Build the method map

Before prose, map the evidence pipeline:

```text
research question
  -> study material / data / population / formal objects
  -> design or sampling
  -> measurement / intervention / representation
  -> processing / procedure
  -> analysis / inference
  -> controls / validation / sensitivity
  -> outputs used by Results
```

For each node record:

- what was done;
- inputs and outputs;
- parameters/conditions that matter;
- rationale if a reasonable alternative would change interpretation;
- source/reference if established procedure is reused;
- reproducibility artifact if relevant.

Organize subsections around reader recovery of this pipeline, not around arbitrary module counts.

## Credibility moves

Large cross-disciplinary Methods corpora show that Methods rhetorically **demonstrate rigour and credibility**, not merely chronology. Common credibility functions include:

### Contextualize the design

- study setting;
- system/material/population;
- data provenance;
- assumptions;
- design type.

### Establish selection/sampling logic

- inclusion/exclusion;
- recruitment;
- sample construction;
- case/source selection;
- train/validation/test split;
- simulation regime.

### Establish measurement/representation validity

- instrument/calibration;
- operational definitions;
- validated scales;
- labels/annotation;
- feature/variable construction;
- source authentication/coding scheme where applicable.

### Describe procedure

- chronological steps when order matters;
- intervention/experimental conditions;
- preprocessing;
- algorithm/training/inference;
- coding/analysis workflow.

### Establish analysis/inference

- statistical model/test;
- estimator;
- error/uncertainty;
- assumptions;
- multiple comparisons;
- causal identification strategy;
- qualitative analytic approach;
- proof/simulation procedure.

### Establish controls/validation

- negative/positive controls;
- baselines;
- ablations;
- sensitivity/robustness;
- external validation;
- inter-rater agreement;
- triangulation/negative cases;
- convergence or numerical checks.

### Establish ethical/reproducible practice

- ethics/consent/registration;
- software/version/environment;
- data/code/material availability;
- preregistration/protocol deviation;
- randomization/blinding where relevant.

Select only moves needed by the study design and reporting standard.

## Rationale: explain consequential choices

A rationale is useful when the reader could reasonably ask **why this choice rather than another?**

Good targets:

- sampling frame;
- outcome/endpoint;
- model class;
- baseline/comparator;
- preprocessing transformation;
- threshold/cutoff;
- hyperparameter search strategy;
- instrument/assay;
- time window;
- exclusion rule;
- coding framework;
- statistical procedure.

Do not justify routine steps with generic claims such as `to improve accuracy`. State the scientific/inferential reason and, when possible, cite validation or show it empirically later.

Methods should not assert a `technical advantage` that only the Results can establish. Methods can explain a **design intention or expected property**; Results establish whether it worked.

## Common organizing principles

### Chronological

Best when procedural order matters: recruitment -> intervention -> measurement -> analysis.

### Evidence-source based

Best when different experiments/datasets/sources generate distinct evidence chains.

### Conceptual component based

Best for complex models/instruments with meaningful independent components.

### Analysis-question based

Best when one dataset supports several distinct inferential questions.

### Nested overview -> detail

Useful for complex systems: overview first, then components, then implementation/analysis.

Choose organization to reduce backtracking. A method figure can help when spatial/data-flow relationships are hard to describe linearly, but it is not mandatory.

## Experimental science

Typical needs:

- materials/specimens/organisms;
- preparation;
- apparatus/instrumentation;
- experimental conditions;
- controls;
- biological vs technical replicates;
- randomization/blinding if applicable;
- measurement and calibration;
- analysis/statistics;
- source data/image integrity where relevant.

Write sequence precisely enough that results can be interpreted. Do not hide a condition needed to understand a figure in Supplementary Methods only.

## Clinical / epidemiological

Typical needs:

- design and setting;
- participants/population;
- eligibility;
- exposure/intervention;
- comparator;
- outcomes and timing;
- sample-size/power logic;
- confounders/covariates;
- missing data;
- statistical analysis;
- sensitivity/subgroups;
- ethics/consent/registration;
- reporting guideline as applicable.

The Methods language must preserve the inference boundary. An observational design should not be narrated as if treatment assignment were randomized.

## Computational / algorithmic

For a real pipeline/model paper, a useful map is:

`problem/formalization -> representation/data -> components -> objective -> training/optimization -> inference -> complexity/resources -> implementation -> evaluation protocol`

### Component subsection

A component may use:

`local problem/design requirement -> component definition -> data/information flow -> expected consequence`

Only claim performance or superiority when evidence supports it.

### Evaluation is part of methodological credibility

Specify:

- datasets/splits and leakage controls;
- baselines and why they are fair;
- metrics;
- hyperparameter selection;
- compute/resources;
- repeated runs/seeds where relevant;
- ablation design;
- statistical comparisons/uncertainty;
- external/stress-test protocol.

A clean pipeline diagram cannot substitute for a fair evaluation design.

## Qualitative / social science

Depending on paradigm, Methods may need:

- research setting/context;
- participant/case/source sampling rationale;
- researcher position/reflexivity where relevant;
- data collection;
- interview/observation/document procedures;
- coding/analytic approach;
- theme/category construction;
- triangulation/negative cases/member checking where appropriate to the methodology;
- ethics/consent;
- saturation/information-power or other adequacy rationale when used.

Do not force quantitative words such as `validation` or `accuracy` onto an interpretive methodology that uses different credibility criteria.

## Theory / simulation

Formal/computational theory Methods may instead foreground:

- assumptions/definitions;
- model equations;
- parameter regimes;
- initial/boundary conditions;
- numerical methods;
- discretization/convergence;
- theorem/proof strategy where separated from Results;
- simulation repetitions/uncertainty;
- benchmark/analytic checks.

The reader needs to know which conclusions follow mathematically from assumptions and which are observed only numerically.

## Paragraph and sentence logic

Methods paragraphs often use one of these nuclei:

- define a design/material/data object;
- explain a selection rule;
- describe a procedure;
- justify a consequential choice;
- define analysis/inference;
- establish a validation/control.

Satellites add parameters, references, rationale, exceptions, or outputs.

### Tense and voice

Use tense/voice to make agency and status clear:

- past tense often describes what was done in this study;
- present tense can define equations, general procedures, software behavior, or figure structure;
- active voice is useful when author choice matters (`we excluded...`, `we fit...`);
- passive voice is useful when the operation/object deserves focus and agency is unimportant.

Do not switch to passive solely to sound academic.

### Sequence

When procedural order matters, use explicit chronological syntax. When order does not matter, group by conceptual dependency rather than filling prose with `first/then/next`.

## Reproducibility boundary

Reproducibility is field-specific. Before finalizing, determine what a competent independent researcher needs:

- raw/processed data;
- source code;
- software/environment/version;
- trained weights;
- materials/reagents;
- protocols;
- random seeds/configuration;
- case/source corpus;
- codebook/annotation instructions;
- analysis scripts;
- proprietary restrictions and access route.

If an artifact cannot be shared, explain the constraint and preserve enough methodological description to evaluate the evidence.

## Audit

1. Can every major Results claim be traced to a method/analysis path?
2. Are all interpretation-changing choices visible?
3. Are sampling/data provenance and exclusions recoverable?
4. Are controls/baselines/comparators appropriate to the claim?
5. Is uncertainty/bias/confounding handled at the level expected by the design?
6. Does rationale explain consequential choices without advertising untested advantages?
7. Can an independent reader reconstruct the sequence/data flow?
8. Are ethics, reporting and availability obligations addressed?
9. Is Methods detail allocated appropriately between main text, supplement and repository?
10. Does the section fit the research paradigm rather than an inherited computational template?

Fix credibility gaps before polishing wording.