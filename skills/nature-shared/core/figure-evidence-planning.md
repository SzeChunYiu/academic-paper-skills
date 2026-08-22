# Claim-driven figure and plot planning

> Shared scientific contract for deciding **which figures a paper needs and what each plot should show before visual styling begins**. Detailed rendering remains the job of `nature-figure`; writing/reviewer skills may use this file to plan evidence roles.

Last reviewed: 2026-08-22.

## Contents

- [Principle](#principle)
- [From claim to figure](#from-claim-to-figure)
- [Figure necessity test](#figure-necessity-test)
- [Figure-role atlas](#figure-role-atlas)
- [Plot-selection variables](#plot-selection-variables)
- [Question-to-plot atlas](#question-to-plot-atlas)
- [Contribution-type figure sequences](#contribution-type-figure-sequences)
- [Main figure versus support figure](#main-figure-versus-support-figure)
- [What not to plot](#what-not-to-plot)
- [Output contract](#output-contract)
- [Research basis](#research-basis)

## Principle

A figure is a **visual evidence unit**. It should exist because a reader/reviewer needs to inspect a scientific pattern, comparison, relationship, uncertainty, or system structure that prose or a small table cannot communicate as well.

Use this order:

`claim -> reader question -> evidence/estimand -> data structure -> uncertainty/alternative explanation -> visual representation -> panel sequence -> main/support placement -> target mechanics`

Never start with:

`top paper used plot X -> make plot X`.

Nature Portfolio explicitly advises authors to make each figure earn its place. Nature Methods' visualization guidance similarly emphasizes matching visual representation to the data/task and identifying the figure's message before design.

## From claim to figure

For every major claim, write:

```text
Claim
Reader question
Decisive evidence
Strongest plausible alternative explanation
Data/statistical unit
Estimand or quantity of interest
Variation/heterogeneity that matters
Uncertainty to expose
Candidate visual representation
Can prose/table do this better?
Main vs support
```

A figure is strongest when it closes a **decision-relevant uncertainty**.

### Example

Claim: method generalizes across hospitals.

Reader questions:

- does performance remain acceptable at each site?
- is average performance hiding site failures?
- does calibration drift?

Possible visual package:

- per-site paired/interval performance plot;
- calibration curves for representative/all sites if calibration is part of the claim;
- site-level covariate/performance relationship only if it tests a relevant explanation.

A single pooled mean bar is usually insufficient for this generalization claim.

## Figure necessity test

Include a figure/panel only if at least one applies:

1. **pattern** — the shape/distribution/relationship matters;
2. **comparison** — readers need direct visual comparison among conditions/methods/groups;
3. **heterogeneity** — variation across units changes interpretation;
4. **uncertainty** — uncertainty itself is decision-relevant;
5. **mechanism/sequence** — process/causal/experimental architecture is difficult to understand from prose;
6. **high-dimensional structure** — a matrix/spatial/network pattern is the evidence;
7. **failure boundary** — where the method/effect stops is central;
8. **orientation** — a schematic/flow materially lowers comprehension cost;
9. **evidence density** — the figure communicates much more useful information than equivalent prose/table.

If a panel contains two values, repeats a sentence, or does not change interpretation, consider prose or omission.

## Figure-role atlas

Do not force every paper to use all roles.

### R1 — orientation / study system

Purpose: explain design, workflow, cohort flow, apparatus, method concept, or experimental timeline.

Useful when the system is complex enough that readers would otherwise spend working memory reconstructing it.

### R2 — phenomenon / primary finding

Purpose: make the core effect or observation inspectable.

### R3 — mechanism / explanation

Purpose: distinguish a proposed mechanism/explanation from plausible alternatives.

Should contain discriminating evidence, not merely an illustrative schematic.

### R4 — validation / replication

Purpose: show the result persists under an independent measurement, cohort, assay, dataset, experiment, or source.

### R5 — generalization / external validity

Purpose: show breadth across populations, regimes, tasks, sites, materials, environments, scales, or assumptions.

### R6 — robustness / sensitivity

Purpose: show dependence on analytical/experimental choices.

Usually support unless robustness itself is the scientific claim or a specific sensitivity changes interpretation.

### R7 — heterogeneity / subgroup structure

Purpose: show variation hidden by an average.

### R8 — failure boundary / negative case

Purpose: show where the claim stops, a null/negative regime, or an adverse trade-off.

Main-text priority rises when this changes the headline claim.

### R9 — benchmark / comparative performance

Purpose: compare against meaningful baselines, existing methods, standards, or controls.

### R10 — resource / coverage / quality

Purpose: explain what a dataset/resource contains, its quality, bias/coverage, and what it enables.

### R11 — model/process interpretation

Purpose: expose a scientifically relevant internal relationship or predictive/causal mechanism. Do not treat generic model-interpretability graphics as mechanistic evidence by default.

### R12 — synthesis / conceptual model

Purpose: integrate findings into a bounded model. A synthesis schematic should distinguish established from speculative relations.

## Plot-selection variables

Before recommending a plot, determine:

### Scientific question

- distribution?
- difference?
- paired change?
- trend/time/dose?
- association?
- prediction/discrimination?
- calibration/agreement?
- survival/event time?
- composition?
- spatial structure?
- high-dimensional matrix?
- ranking/benchmark?
- heterogeneity?
- robustness/sensitivity?
- mechanism/mediation?
- uncertainty/posterior?
- image morphology?

### Data structure

- categorical / continuous / count / ordinal;
- independent / paired / repeated;
- cross-sectional / longitudinal;
- hierarchical / clustered;
- censored / competing-risk;
- compositional;
- spatial;
- network/relational;
- matrix/high-dimensional;
- image/spectrum/signal;
- deterministic simulation / stochastic runs;
- task/site/seed-level benchmark observations.

### Estimand

What is the actual quantity being compared?

- mean/median difference;
- paired difference;
- slope/rate;
- risk/risk difference/risk ratio/hazard;
- probability/calibration;
- AUC/precision/recall;
- error/accuracy;
- effect size;
- distribution/quantile;
- resource cost;
- sensitivity/specificity;
- correlation/association parameter;
- posterior/credible interval;
- uncertainty band;
- rank only if rank is truly the question.

### Scientific unit

Participants, animals, samples, cells, technical replicates, sites, tasks, seeds, datasets, images, simulations, timepoints, papers, sources, etc.

Do not visually treat technical replicates as independent biological/statistical units.

### Alternative explanation

What pattern would be visible if the competing explanation were true?

The best plot often makes that alternative visually testable.

## Question-to-plot atlas

These are starting points, not universal rules.

### Distribution of continuous observations

Good candidates:

- dot/strip/swarm plot;
- ECDF;
- histogram/density when sample size supports shape estimation;
- box/violin combined with points when appropriate.

For small sample sizes, show individual observations rather than hiding them behind mean bars. Weissgerber et al. found bar/line summaries can conceal outliers, bimodality, overlap, and pairing; PLOS Biology now recommends displays that let readers evaluate individual-point distributions.

### Independent group difference

Good candidates:

- raw points + summary/interval;
- estimation/effect-size plot;
- box/violin + points when distribution matters.

Avoid a bar of mean ± error when the underlying observations are decision-relevant.

### Paired/matched change

Good candidates:

- connected paired points;
- paired-difference distribution;
- slopegraph;
- repeated-measure trajectory.

Do not visually imply independence when pairing is the estimand.

### Longitudinal/time course

Good candidates:

- individual trajectories when unit-level variation matters;
- summary line + uncertainty band/interval;
- small multiples if groups/traces become entangled.

Lines imply meaningful order/continuity; do not connect unordered categories by default.

### Dose-response / scaling / ordered parameter

Good candidates:

- scatter/line with fit and interval if justified;
- log axes when scientifically meaningful and clearly labelled;
- saturation/phase/regime transitions made visible rather than compressed into one endpoint.

### Association / relationship

Good candidates:

- scatter;
- hexbin/density for heavy overplotting;
- fitted curve/interval only with an explicit model/assumption;
- residual/partial-effect diagnostic when the inferential claim depends on adjustment/model form.

A visual association does not establish causality.

### Agreement / measurement method comparison

Good candidates:

- identity-line scatter for correspondence;
- difference-versus-average (Bland–Altman style) when agreement/bias across range is the question;
- replicate/reliability displays as appropriate.

Correlation alone is not agreement.

### Classification discrimination

Candidates:

- ROC curve when sensitivity/specificity trade-off across thresholds is relevant;
- precision–recall when positive-class retrieval under class imbalance is more decision-relevant;
- threshold-specific operating points with confidence intervals when deployment decisions matter.

Do not present AUC alone when clinically/operationally relevant thresholds or calibration matter.

### Calibration / probabilistic prediction

Candidates:

- calibration/reliability curve;
- observed versus predicted risk by bins/smoothers with uncertainty;
- calibration intercept/slope or score in accompanying table/text;
- prediction distribution to show where calibration is being assessed.

Discrimination and calibration answer different questions.

### Survival / time-to-event

Candidates:

- Kaplan–Meier curves with numbers at risk for survival-function comparisons when appropriate;
- cumulative-incidence plots for competing-risk settings;
- forest/interval plots for model effect estimates.

Do not use a generic line chart that ignores censoring.

### Heterogeneity / subgroup effects

Candidates:

- forest plot with estimates + intervals;
- stratified raw/summary plots when subgroup sample structure matters;
- site/task-level paired performance plots;
- interaction visualization if the interaction claim is central.

Avoid declaring subgroup differences from one significant and one nonsignificant within-group test without an interaction/comparison of effects.

### Robustness / sensitivity

Candidates:

- sensitivity curve across thresholds/assumptions;
- forest/interval plot across specifications;
- small multiples;
- heatmap when a true 2D parameter surface is the object of interest.

Usually Extended Data/SI unless the dependence defines the main boundary.

### Many methods / benchmarks

Candidates:

- paired per-dataset/task differences;
- interval plots with common baseline;
- rank plot only when rank is the decision target;
- performance-versus-compute/memory/latency frontier if efficiency is claimed;
- table for exact values when there are many metrics and visual pattern is secondary.

Do not show only grand means when task heterogeneity matters.

### Ablation / component contribution

Ask what the ablation claim is.

- incremental component effect -> paired difference/interval across tasks/runs;
- factorial contribution/interactions -> effect plot/model estimates;
- architecture variants -> benchmark/interval table/plot;
- ordered component addition -> line only if the order is scientifically meaningful.

An ablation does not automatically establish mechanism; it establishes dependence of performance/output on a component under the tested intervention.

### High-dimensional matrix / omics / condition-by-feature structure

Candidates:

- heatmap when matrix pattern/clustering is the scientific object;
- clustered heatmap with annotation only when clustering choices are justified;
- dimensionality reduction for exploration/orientation, accompanied by quantitative/statistical evidence for claims inferred from the embedding.

A UMAP/t-SNE visualization alone is weak evidence for quantitative separation or mechanism.

### Composition / proportions

Candidates:

- stacked bars/areas for a small number of meaningful parts and totals;
- dot/interval plots for precise category comparison;
- compositional-data-aware representations when inference concerns relative composition.

Pie/donut charts are poor choices when precise comparison among many categories matters.

### Imaging / microscopy / morphology

A strong evidence figure often combines:

- representative images with non-deceptive selection/cropping;
- scale bars;
- consistent processing;
- independent quantitative summary across the correct experimental unit;
- localization/intensity/morphology measurements as relevant;
- blinded selection/analysis information in Methods when relevant.

A representative image alone rarely establishes a population-level quantitative claim.

### Spatial / geographic

Candidates:

- map for spatial pattern;
- distribution/interval companion for quantitative comparison;
- spatial residual/autocorrelation display when model validity depends on spatial structure.

### Network / relational

Network diagrams are useful when topology is the evidence. For comparison/inference, accompany them with quantitative network measures or model results when appropriate; avoid hairball networks used only decoratively.

### Uncertainty / posterior distributions

Candidates:

- interval/forest plots;
- posterior density/ridge plots;
- credible bands;
- probability-of-effect displays when interpretable.

Show the uncertainty quantity the inference actually uses.

### Null / negative result

Candidates:

- effect estimate + confidence/credible interval;
- equivalence/non-inferiority interval relative to prespecified margin when appropriate;
- sensitivity/power/precision information as relevant;
- raw data/distribution when sample size is small.

`P > 0.05` and a short bar are not sufficient evidence for equivalence/no effect.

### Qualitative / interpretive evidence

Do not force quantitative plotting. Possible displays include:

- conceptual framework;
- process/model diagram;
- theme/source map;
- timeline;
- evidence table/matrix.

The display must preserve provenance and not convert interpretive evidence into fake quantitative precision.

## Contribution-type figure sequences

These are **role menus**, not templates.

### Experimental discovery

Possible sequence:

- orientation/system;
- primary phenomenon;
- decisive controls/mechanism;
- validation/generalization;
- failure/boundary if central.

### Mechanism paper

Possible sequence:

- phenomenon;
- perturbation establishes dependency;
- competing mechanism discrimination;
- rescue/orthogonal evidence;
- boundary/generalization.

### Clinical / epidemiological

Possible roles:

- cohort/participant flow and baseline orientation when needed;
- primary outcome/effect estimate;
- time-to-event or absolute-risk display when relevant;
- adjusted/identification result;
- heterogeneity/safety/generalization if central;
- sensitivity in support unless decision-changing.

### Computational / ML

Possible roles:

- problem/method overview;
- primary benchmark with task/site/run structure visible;
- ablation/component evidence if claimed;
- external/OOD/generalization;
- calibration/failure cases;
- compute/performance trade-off if claimed.

Do not default to one `architecture diagram + giant benchmark table + UMAP` sequence.

### Methods / tool / instrument

Nature Methods' Article criteria suggest a particularly useful role inventory:

- method/tool concept;
- performance/accuracy/sensitivity or relevant technical validation;
- reproducibility;
- comparison to established methods;
- general applicability;
- demonstration of useful new scientific inference when part of the claim.

### Resource / dataset

Possible roles:

- composition/coverage;
- quality/provenance/bias;
- access/workflow orientation;
- benchmark/validation;
- scientific utility/use case.

### Theory / modeling

Possible roles:

- conceptual geometry/system definition;
- theorem/regime/phase diagram;
- simulation/numerical verification if relevant;
- comparison with data;
- counterexample/boundary.

### Review / synthesis

Possible roles:

- taxonomy;
- conceptual framework;
- evidence landscape;
- unresolved questions;
- process/model schematic.

Do not invent quantitative data for a review figure.

## Main figure versus support figure

### Main figure priority rises when

- the evidence is necessary for the central claim;
- omission would cause a reasonable reviewer to question the central inference;
- the pattern cannot be understood from prose alone;
- the figure shows a conclusion-changing boundary/negative result;
- the figure is a decisive comparator/control;
- the figure establishes generalization that the title/abstract claims.

### Support placement is usually appropriate when

- it repeats the same conclusion under another seed/specification/threshold;
- it is a non-central control;
- it is a full parameter sweep supporting a concise main result;
- it expands a benchmark table without changing the interpretation;
- it documents provenance/diagnostics useful for specialist scrutiny.

Load `manuscript-content-selection.md` and exact target rules for final placement.

## What not to plot

Do not create/display a plot merely because:

- the analysis software generated it;
- comparable papers often contain it;
- it looks sophisticated;
- it uses an attractive embedding;
- it can fill an empty figure panel;
- it repeats exact values already in a table without adding visual insight;
- it hides unfavorable variance/outliers/negative cases;
- it changes axis/crop/normalization to exaggerate an effect;
- it gives a false impression of independence, causality, continuity, or precision.

## Output contract

When the skill has enough information, it may proactively return a **figure/plot suggestion ledger**:

```text
Claim / reader question
Why a figure is or is not needed
Scientific/statistical unit
Estimand
Data structure
Alternative explanation / risk to reveal
Recommended plot
Alternative representation
What uncertainty must be shown
Main vs support
Panels needed
What not to include
```

Then build a figure sequence:

```text
Fig. 1 — role / claim / panels
Fig. 2 — role / claim / panels
...
Extended/SI — supporting roles
```

The recommendations must remain revisable when the actual data are inspected.

## Research basis

- Nature Portfolio, *How to write your paper*: figures should earn their place and support the main message.
- Rougier, Droettboom & Bourne (2014), *Ten Simple Rules for Better Figures*: identify audience and message before design; message/readability outrank beauty; literature can inspire but should be adapted, not copied.
- Nature Methods, *Points of View* and the 2026 relaunch editorial: visualization should match data types/tasks, expose uncertainty, reveal structure/artifacts, and be treated as part of reproducibility.
- Weissgerber et al. (2015), PLOS Biology: systematic review of 703 physiology papers showed common bar/line summaries can conceal continuous-data distributions and paired structure; recommends fuller data displays.
- PLOS Biology current submission guidance: for continuous data, particularly small `n`, use displays that allow readers to evaluate the distribution of individual points.
- Nature Methods, *Kick the bar chart habit*: statistical samples should use representations suited to their distribution rather than bars that overweight the zero baseline.
- Nature Methods, *Unentangling complex plots*: small multiples can outperform one overloaded complex plot.
- Nature Methods, *The overview figure*: overview schematics can reduce cognitive load for complex experimental designs/findings.
- Nature research figure guide: data presentation, axes, accessibility, and figure readability are integral to interpretation.

Plot-specific statistical decisions must still follow field methods/reporting standards and the actual design.
