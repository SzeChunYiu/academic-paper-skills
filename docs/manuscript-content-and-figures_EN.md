# What Belongs in a Paper — and What Figures Should It Show?

[中文](manuscript-content-and-figures.md)

A strong paper is not an exhaustive dump of everything in the project. It is a carefully allocated publication package: the main text carries the shortest sufficient scientific argument, figures make decisive evidence inspectable, Methods make the work interpretable and reproducible, supplementary material supports deeper scrutiny, and repositories hold operational details.

This guide explains how the repository now decides **what to include, where to put it, what to omit, and what plots to suggest**.

Last reviewed: 2026-08-22.

## 1. The problem: repository-to-manuscript leakage

When an AI writes from a codebase, it often copies implementation artifacts directly into prose:

- filenames and directory paths;
- helper-function/class names;
- CLI commands;
- configuration files;
- package/setup instructions;
- branch/PR/issue history;
- unit-test names;
- internal modules;
- repeated GitHub links;
- developer workflow.

This is **implementation-detail leakage** or **repository-to-manuscript leakage**.

The problem is not that these details are false. The problem is that they often do not perform a useful scientific function at the point where they are written.

### Scientific-abstraction test

Ask:

> If the implementation were rewritten from scratch, but the scientific method and results stayed identical, would this detail still matter to the paper?

If no, it is probably artifact/documentation detail rather than scientific narrative.

Examples:

| Source artifact | Better publication treatment |
|---|---|
| `scripts/preprocess.py` | Describe consequential preprocessing in Methods; filename usually stays in repository docs. |
| `src/model.py::fit()` | Describe the algorithm/model fitting operation scientifically. |
| YAML config | Report consequential parameters in Methods/SI; archive full config with code. |
| GitHub URL | Put authoritative access in Code/Resource Availability. |
| installation command | Repository README/artifact appendix. |
| unit tests / CI | Repository QA unless software reliability itself is evaluated scientifically. |
| internal module hierarchy | Usually developer docs; include only if architecture is itself a contribution. |

## 2. The five-function admission test

Every candidate detail should perform at least one function.

### F1 — inference-critical

Needed to believe/evaluate a scientific claim.

### F2 — interpretation-critical

Needed to understand meaning, scope, alternative explanation, or boundary.

### F3 — reproducibility-critical

Needed to recreate or verify the experiment/analysis.

### F4 — compliance/provenance-critical

Required for ethics, reporting, data/code/material access, registration, attribution, or auditability.

### F5 — orientation-critical

Substantially reduces the cognitive cost of understanding a complex system, design, cohort, workflow, or evidence sequence.

If none applies, the content normally should not occupy manuscript space.

But even F1–F5 information is not automatically main-text content. It must go to the right destination.

## 3. Destination: main text, Methods, SI, repository — or nowhere?

### Main text

Use for the information a target reader must see during the first-pass scientific argument:

- research question/tension;
- bounded contribution;
- central findings;
- decisive comparisons/controls;
- primary uncertainty;
- central mechanism evidence when mechanism is claimed;
- central validation/generalization when claimed;
- negative/failure evidence that changes interpretation;
- limitations/boundaries that prevent overgeneralization.

### Main figures/tables

Use when the **pattern** should be inspected rather than described:

- distribution;
- pairing;
- heterogeneity;
- relationship;
- uncertainty;
- comparative performance;
- mechanism/sequence;
- generalization/failure boundary;
- high-dimensional/spatial/network structure.

A display must earn its place.

### Figure legends

Decode the display:

- what each panel shows;
- groups/conditions;
- axes and units;
- `n` and statistical unit;
- uncertainty/error representation;
- test/annotation definitions;
- scale bars and panel-specific details.

Do not make the legend a duplicate Results paragraph plus full Methods section.

### Methods

Use for details needed for interpretation and replication:

- design;
- provenance/sampling;
- procedure;
- measurements;
- preprocessing;
- algorithms/models;
- fitting/training;
- statistics;
- controls;
- software/hardware when consequential;
- ethics/registration;
- reproducibility details.

For computational papers, detailed derivations, training strategies and exhaustive architecture descriptions often belong here when they would distract from Results.

### Extended Data / Supplementary Information

Use for important support that is not necessary for first-pass argument reconstruction:

- secondary controls;
- robustness/sensitivity;
- alternative specifications;
- parameter sweeps;
- full benchmark tables;
- extended diagnostics;
- secondary endpoints;
- large derivations/calculations;
- specialist details;
- non-central edge cases.

Do **not** bury a failed external validation, subgroup reversal, adverse effect, or important failure boundary when it changes the headline interpretation.

### Data / Code / Resource Availability

Use as the authoritative access point for:

- persistent repository/DOI/accession;
- release/version/commit when needed;
- license;
- access restrictions;
- archived data/code/material identifiers;
- central protocols.

This is where a repository link usually belongs — once, authoritatively — rather than repeatedly inside Results.

### Repository / artifact documentation

Use for:

- installation;
- dependencies;
- CLI usage;
- file structure;
- configs;
- APIs;
- scripts;
- reproduction commands;
- developer information;
- unit tests/CI;
- detailed operational examples.

### Omit

Omit information that does not contribute to inference, interpretation, reproducibility, compliance/provenance, or orientation.

`We did this analysis` is not a reason to publish the analysis.

## 4. What top-tier editorial guidance says

The strongest editorial guidance converges on the same principle.

Nature Portfolio advises authors to keep the paper focused and concise and to make every figure support the main message.

Nature Computational Science explicitly recommends organizing Results in a **logical narrative**, not laboratory chronology, and including only the most important results in the main text. Detailed mathematical derivations, training strategies, and exhaustive model-architecture/construction details should move to Methods when they distract from the Results narrative.

Nature Methods simultaneously demands detailed method description, algorithms, code, licensing and user guidance for reuse. This is not a contradiction: **reproducibility completeness and narrative selectivity belong in different layers of the publication package**.

Nature Methods also judges methods papers on validation, benchmarking, reproducibility, general applicability, and useful applications rather than on the amount of implementation prose in Results.

## 5. How to decide what figures the paper needs

Do not start with chart type.

Start with:

`claim -> reader question -> estimand -> data structure -> uncertainty / alternative explanation -> plot -> placement`

For every headline claim ask:

1. What must a skeptical reader inspect to evaluate this claim?
2. What is the experimental/statistical unit?
3. What quantity is actually being compared or estimated?
4. What variation matters?
5. What alternative explanation should the visual help test?
6. What uncertainty must remain visible?
7. Can prose/table communicate this better than a figure?
8. Is the evidence central enough for main text?

## 6. Figure roles: what scientific job does the figure perform?

A useful role atlas is:

- **orientation/system** — design, cohort flow, workflow, apparatus, method concept;
- **primary finding** — central effect/observation;
- **mechanism** — discriminates mechanism from alternatives;
- **validation/replication** — independent evidence;
- **generalization** — different sites/populations/tasks/regimes;
- **robustness/sensitivity** — analysis/parameter dependence;
- **heterogeneity** — variation hidden by an average;
- **failure/negative boundary** — where claim stops;
- **benchmark/comparison** — meaningful alternatives/baselines;
- **resource/quality/coverage** — resource composition, quality and utility;
- **model/process interpretation** — scientifically relevant internal relationship;
- **synthesis/conceptual model** — bounded integration of findings.

A paper does not need all of these.

The right sequence depends on contribution type.

## 7. Plot suggestions by scientific question

These are starting points, not templates.

### Small-sample continuous groups

Prefer individual observations / distribution-aware displays rather than a bar of mean ± error alone.

Possible choices:

- dot/strip/swarm;
- box/violin + points;
- ECDF;
- estimation/effect-size plot.

Weissgerber et al. showed that bar/line summaries can conceal outliers, bimodality, overlap, and paired structure. Nature and PLOS guidance increasingly encourages showing individual points when sample size permits.

### Paired / matched data

Show the pairing:

- connected pairs;
- paired-difference distribution;
- slopegraph;
- repeated-measure trajectories.

A two-group unpaired bar plot can erase the actual estimand.

### Time / dose / ordered parameter

Use trajectories/lines only when order/continuity is meaningful. Show individual trajectories or uncertainty when they matter.

### Association

Use scatter / hexbin / density depending data scale. Add fitted relations only with justified models. A visual association is not causality.

### Agreement between measurement methods

Correlation alone is not agreement.

Use correspondence plus difference-versus-average/other agreement diagnostics where appropriate.

### Classification

Use the display that matches the decision:

- ROC for sensitivity/specificity trade-off;
- precision–recall under relevant class imbalance;
- operating points for deployment decisions.

Do not report AUC as the complete evaluation if calibration or threshold behavior matters.

### Calibration

Use calibration/reliability curves plus appropriate quantitative calibration measures. Discrimination and calibration answer different questions.

### Survival / time-to-event

Use censoring-aware survival/cumulative-incidence displays and effect intervals as appropriate, not generic time lines.

### Heterogeneity / subgroup effects

Use forest/interval plots or stratified raw-data displays. Show the actual comparison of subgroup effects when heterogeneity is claimed.

### Robustness / sensitivity

Use sensitivity curves, interval plots, small multiples, or parameter surfaces. Usually supporting evidence unless the sensitivity defines the main scientific boundary.

### ML / algorithm benchmarking

When task/site/run heterogeneity matters, show per-unit performance or paired differences rather than only grand means.

Useful possibilities:

- per-task/site paired comparisons;
- interval plots;
- performance-versus-compute frontier;
- exact-value table for many metrics.

Do not use rank alone unless rank is the real decision target.

### Ablation

An ablation answers dependency of performance/output on a component under an intervention. It does not automatically prove mechanism.

Plot the actual component effect, interaction or per-task variation.

### Imaging / microscopy

For population-level claims, representative images should normally be connected to quantitative evidence using the correct experimental unit.

### High-dimensional / single-cell / omics

Heatmaps and embeddings are valuable when the matrix/manifold pattern is the object of interest. An attractive UMAP/t-SNE alone should not carry a quantitative separation/mechanism claim.

### Null / negative findings

Use effect estimates and uncertainty/equivalence/non-inferiority logic as appropriate. `P > 0.05` plus an empty-looking bar is not proof of no effect.

### Qualitative / theory / humanities

Do not force numerical graphics. A conceptual framework, evidence matrix, source map, process diagram or no figure at all may be more faithful.

## 8. Contribution type changes what belongs in the paper

### Experimental discovery / mechanism

High-priority evidence may include:

- phenomenon;
- decisive controls;
- perturbation/dependency;
- competing mechanism discrimination;
- rescue/orthogonal evidence;
- generalization/boundary.

### Clinical / epidemiological

High-priority evidence may include:

- cohort/design orientation;
- primary outcome/effect;
- uncertainty;
- confounding/identification logic;
- absolute clinical quantities when meaningful;
- central heterogeneity/safety/generalizability.

### Computational / ML

High-priority evidence may include:

- task/data regime;
- fair baseline comparison;
- primary benchmark;
- variation across tasks/sites/runs;
- ablation only when component dependence is claimed;
- external/OOD validation when generalization is claimed;
- failure/calibration/efficiency when central.

Implementation plumbing belongs in Methods/repository.

### Methods / tools

Nature Methods provides a particularly clear evidence model:

- detailed method description for reuse;
- strong performance validation;
- ground truth/gold standard when available;
- benchmarking against similar methods;
- real experimental data, not simulation alone;
- general applicability across distinct systems/datasets;
- useful challenging application when appropriate.

### Dataset / resource

A resource paper may legitimately include information that would be clutter in another paper — for example resource composition, file/data organization, quality controls and Usage Notes — because usability/provenance is itself part of the contribution.

This is why content rules must be **contribution-type aware**.

## 9. Direct-reading patterns from recent high-tier papers

These are examples of role sequences, not templates to copy.

### Nature Cell Biology method + discovery

The 2025 paper *Decoding heterogeneous single-cell perturbation responses* starts with a framework/benchmark figure, then uses later figures to establish dose-response/heterogeneity and biological applications. The transferable pattern is `method definition -> validation/benchmark -> new analysis capability -> biological discovery`, not its exact visual design.

### Nature Cell Biology large perturbation resource/method

*Systematic reconstruction of molecular pathway signatures using scalable single-cell perturbation screens* uses a sequence of `large-scale experimental system -> computational method -> cross-context signatures -> validation -> in vivo/in situ applications`.

### Nature Methods benchmark

The 2026 benchmark of 27 single-cell perturbation prediction methods across 29 datasets uses an overview/workflow figure followed by distinct generalization scenarios and a figure specifically focused on a limitation. That is a strong example of **failure-boundary evidence earning main-figure space**.

### Nature Medicine generalization

Recent oncology/generalization work uses site/trial/population-stratified effect/survival displays rather than only pooled headline metrics. Clinical generalization is shown as heterogeneity across contexts, not declared from one external dataset.

These examples should guide the questions we ask, not dictate panel count or aesthetics.

## 10. A practical content + figure planning output

For each important content item:

```text
Item
Function: inference / interpretation / reproducibility / compliance / orientation / none
Claim dependency
Decision-changing? yes/no
Destination
Reason
```

For each headline claim:

```text
Claim / reader question
Figure needed? why/why not
Statistical unit
Estimand
Data structure
Alternative explanation to expose
Recommended plot
Alternative representation
Required uncertainty/comparator
Main vs support
Panels
```

Then assemble:

```text
Main-text evidence chain
Fig. 1 — ...
Fig. 2 — ...
Fig. 3 — ...
Extended Data/SI — ...
Methods — ...
Data/Code/Resource Availability — ...
Repository/artifact docs — ...
Omit — ...
```

## 11. The goal

The ideal paper is not the paper with the most details or most figures.

It is the paper in which:

- every main-text paragraph advances or bounds the central reasoning;
- every main figure closes a real evidentiary question;
- reproducibility information is complete but correctly allocated;
- operational codebase detail stays in the artifact layer unless scientifically meaningful;
- negative and boundary evidence remains visible;
- the exact journal and contribution type determine local expectations;
- the reader never has to infer why a sentence, analysis or panel is present.
