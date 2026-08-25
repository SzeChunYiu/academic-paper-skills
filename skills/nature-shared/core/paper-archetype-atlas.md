# Paper archetype atlas

> Shared cross-disciplinary calibration for deciding how different kinds of papers build arguments, allocate evidence, elaborate ideas, and sequence figures. This is not a journal template. Last reviewed: 2026-08-25.

## Why this exists

A package cannot fit "all papers" by learning one prestigious style. Papers differ because their **epistemic jobs differ**.

A randomized trial asks whether an intervention changes an outcome under a prespecified design. A mechanism paper asks what process produces a phenomenon. A benchmark paper asks whether methods perform under fair, decision-relevant regimes. A resource paper asks whether a dataset/tool is trustworthy, reusable and sufficiently characterized. A theory paper may establish its main result through proof rather than visual evidence. A qualitative paper may need no quantitative plot at all.

Use this tuple before choosing prose or figures:

`contribution archetype × study design × evidence modality × intended reader × publication model`

The archetype is a **prior**. The manuscript's actual claims and evidence remain decisive.

## Cross-archetype invariants

Strong papers usually make it possible to recover:

1. the question or unresolved tension;
2. the bounded contribution/answer;
3. the evidence or reasoning that warrants it;
4. the strongest relevant alternative/uncertainty;
5. the boundary of the conclusion;
6. why the next evidence block is necessary.

What differs is **which evidence closes those dependencies** and **how much explanation the reader needs**.

## A. Experimental discovery / mechanism paper

### Core reader question

`What phenomenon exists, what causes or controls it, and how convincingly are alternatives excluded?`

### Common reasoning sequence

A useful starting pattern is:

`phenomenon -> dependency/perturbation -> mechanism discrimination -> quantitative/model support -> orthogonal/rescue validation -> scope/failure boundary`

Not every mechanism paper needs every stage. Do not invent rescue experiments or molecular mechanisms merely because other papers have them.

### Main-text content

Prioritize:

- the phenomenon or effect;
- decisive perturbations/controls;
- evidence that distinguishes the claimed mechanism from plausible alternatives;
- orthogonal measurement when one assay could be misleading;
- causal/temporal ordering when mechanism depends on it;
- a boundary or context that changes the claim.

### Common main-figure roles

- morphology/phenomenon plus quantification;
- time/dynamics or dose response;
- perturbation/dependency;
- mechanistic intermediate;
- mathematical/physical model when it tests/explains the mechanism;
- rescue/orthogonal validation;
- generalization to another system/condition.

### Plot families

- representative image + population-level quantification;
- paired/group distribution displays;
- trajectories/time course;
- dose-response curves;
- perturbation effect sizes with uncertainty;
- correlation/association only when the claim is relational, not as a substitute for causal evidence;
- model prediction versus observed data;
- spatial maps/fields when spatial structure is mechanistic.

### Direct-reading calibration

A 2025 Nature Cell Biology paper on edge curvature and ER organization publicly sequences its early main figures as:

`curvature-dependent morphology -> differential dynamics -> force regulation -> mathematical model`.

This is useful because each figure removes a different uncertainty. It is **not** a universal four-figure skeleton.

### Over-compression risk

Mechanism papers are especially vulnerable to one-sentence jumps such as `X changed, indicating mechanism Y`. Use `explanatory-sufficiency.md` to expose the discriminating logic.

## B. Randomized trial / intervention paper

### Core reader question

`Who was assigned to what, what happened on the prespecified outcomes, with what uncertainty and safety, and how should the effect be interpreted?`

### Common reasoning sequence

`participant flow -> baseline/design orientation -> primary outcome -> uncertainty/clinical scale -> key secondary/safety outcomes -> subgroup/heterogeneity if prespecified/decision-relevant -> sensitivity/robustness`

### Main-text content

Prioritize:

- eligibility/randomization/analysis population;
- intervention/control and primary endpoint;
- effect estimate and uncertainty, not P value alone;
- absolute quantities when clinically meaningful;
- missingness/censoring/analysis-set facts that change interpretation;
- harms/safety;
- prespecified subgroup or effect-modification evidence only when scientifically justified;
- limitations of duration/sample/generalizability.

### Common main figures/tables

- CONSORT-style participant flow;
- primary endpoint over time or effect estimate;
- survival/cumulative incidence when appropriate;
- forest plot for prespecified heterogeneity;
- safety table rather than decorative plots when counts are the reader task;
- PK/PD when exposure-response is part of the contribution.

### Direct-reading calibration

A 2025 Nature Medicine randomized phase 2a trial uses participant randomization/follow-up as Fig. 1, the primary FVC change with 95% CI as Fig. 2, and pharmacokinetics as Fig. 3, with subgroup/sensitivity material in Extended Data. The sequence mirrors trial decision logic rather than a generic `schematic -> mechanism -> validation` pattern.

## C. Observational / epidemiological / clinical association paper

### Core reader question

`What is associated with what, in whom, under what identification/confounding assumptions, and how robust/generalizable is the association?`

### Common reasoning sequence

`population/data orientation -> exposure/outcome definition -> primary association/effect estimate -> adjustment/identification -> heterogeneity/nonlinearity -> sensitivity/negative controls -> external/temporal validation or generalizability -> limitations`

### Main figures

- cohort flow only if selection is nontrivial;
- distribution/burden maps or descriptive structure when they establish the research object;
- adjusted effect/forest plots;
- dose-response/nonlinearity curves;
- survival curves when time-to-event is central;
- calibration/discrimination only for prediction claims;
- sensitivity or negative-control result in main text if it materially changes credibility.

### Plot warning

A giant correlation heatmap is rarely sufficient evidence for an observational claim. The plot should expose the estimand and uncertainty, not merely the availability of many variables.

## D. Computational / machine-learning empirical paper

### Core reader question

`Does the method/model solve the stated scientific/technical problem under fair and relevant evaluation regimes, why, and where does it fail?`

### Common reasoning sequence

`task/problem + evaluation regime -> comparator fairness -> primary performance -> variability/heterogeneity -> component/mechanism evidence -> OOD/external/generalization -> calibration/robustness/efficiency -> failure boundary`

### Main-text content

Prioritize:

- task and evaluation regime;
- dataset splits and leakage prevention when consequential;
- fair baseline/comparator setup;
- primary metrics tied to the real decision problem;
- uncertainty across seeds/tasks/sites/subjects when stochasticity/heterogeneity matters;
- ablation only when it addresses a causal/component claim;
- OOD/external validation when generalization is claimed;
- calibration when probabilities/decisions are claimed;
- computational cost when efficiency is part of the contribution;
- explicit failure cases/biases when they bound use.

### Common main-figure roles

- task/data/evaluation schematic;
- benchmark across regimes rather than one pooled score;
- heterogeneity by task/site/class;
- ablation/component contribution;
- generalization/OOD;
- explicit limitation/failure analysis;
- calibration/decision curve where relevant;
- qualitative examples only when they diagnose behavior rather than decorate.

### Direct-reading calibration

A 2026 Nature Methods benchmark of single-cell perturbation prediction publicly sequences:

`workflow/datasets -> OOD benchmark -> explicit limitation of current methods -> second generalization scenario -> broader benchmark`.

The presence of a **main limitation figure** is important: a failure boundary can deserve main-display space when it changes the headline interpretation.

A 2025 Nature Machine Intelligence paper on training-data composition uses early figures to connect data composition to generalization, then shows performance variation across tasks/data geometry, then tests how negative-data choice changes learned biological rules. The figure sequence moves from phenomenon to explanatory factor rather than merely ranking models.

### Plot families

- per-task/site/run dot/interval distributions;
- paired method comparisons when evaluated on the same units;
- critical-difference/rank plots only when ranking is the actual reader task and assumptions are met;
- scatter/relationship plots for scaling/error analyses;
- ROC/PR only when threshold-free discrimination is relevant;
- operating-point/confusion/cost plots when deployment decisions matter;
- reliability/calibration curves for probabilistic prediction;
- ablation effect plots with uncertainty;
- learning/scaling curves;
- failure-stratified plots.

### Anti-patterns

- giant metric tables with no reader hierarchy;
- bars of grand means hiding task/site variation;
- UMAP/t-SNE used as quantitative proof;
- cherry-picked qualitative examples;
- architecture diagram occupying a main figure when architecture itself is not the contribution;
- repository/module details in Results.

## E. Method / tool / software / instrument paper

### Core reader question

`What new capability does this method enable, is it valid, better/different under the relevant conditions, usable/reproducible, and what are its limits?`

### Common reasoning sequence

`capability/problem -> method principle -> technical validation -> benchmark against alternatives -> sensitivity/operating regime -> real application -> reproducibility/usability -> limitation`

### Main figures

- principle/workflow schematic when orientation is genuinely necessary;
- technical validation against ground truth/reference standard;
- accuracy/precision/sensitivity across relevant operating range;
- benchmark against existing methods;
- real-use application demonstrating new scientific capability;
- failure/operating boundary;
- resource/workflow utility only if evaluated.

### Software-specific boundary

A software paper can discuss interface/architecture when that interface/architecture is part of the **evaluated contribution**. File trees, helper names, installation commands and internal modules still belong in artifact docs.

### Main versus artifact

Paper:

- scientific purpose;
- method principle;
- validation;
- benchmark;
- capability/application;
- limits.

Artifact:

- install commands;
- exact directory structure;
- API reference;
- CLI options;
- file-by-file tutorial;
- developer architecture.

## F. Dataset / resource / benchmark-resource paper

### Core reader question

`What resource exists, how was it assembled, what does it cover, how was quality validated, what biases/limitations remain, and how can it be reused?`

### Common reasoning sequence

`need + scope -> collection/sampling -> processing/annotation -> coverage/distribution -> technical validation/quality -> usage/example -> access + limitations`

### Main figures

- geographical/temporal/sample coverage;
- cohort/specimen/data composition;
- acquisition/processing workflow;
- quality-control distributions;
- missingness/completeness;
- agreement/validation against reference data;
- example use or benchmark when it demonstrates fitness for reuse.

### Direct-reading calibration

A 2025 Scientific Data arthropod Data Descriptor uses a first display combining sampling geography and raw richness distributions, followed by a data-processing workflow. This reflects resource trust questions: **what is covered? how was it produced?** rather than a hypothesis-testing sequence.

### Anti-patterns

- pretending the data descriptor needs a dramatic mechanistic claim;
- filling main text with filenames/directories;
- showing only attractive example samples without coverage/QC;
- omitting bias/missingness/collection limitations.

## G. Theory / proof / mathematical paper

### Core reader question

`What is established under which assumptions, why is the result nontrivial, and what does the theorem imply?`

### Common reasoning sequence

`problem/definitions -> assumptions -> main theorem/result -> intuition -> proof structure -> consequences/corollaries -> illustrative numerics/examples -> limitations/open conditions`

The proof may be the decisive evidence. Do not force empirical-figure logic onto it.

### Figures

Use only when they reduce conceptual burden or test/illustrate consequences:

- geometric/conceptual diagram;
- phase/regime map;
- simulation illustrating theorem behavior;
- convergence/error curve;
- counterexample;
- real-data illustration when the paper claims practical relevance.

### Direct-reading calibration

JMLR 2025 papers span theorem-heavy work with later experiments/numerical illustrations and empirical-theoretical hybrids. The paper should make clear which statements are proved, which are simulated, and which are empirically observed.

### Explanation risk

A formula/theorem dump is not concise clarity. Define objects, state the scientific/mathematical role of assumptions, and give intuition at the level appropriate for the audience.

## H. Qualitative / interpretive paper

### Core reader question

`What experience/process/meaning/pattern was identified, how was interpretation developed and grounded, and how should it be bounded?`

### Common reasoning sequence

`phenomenon/context -> sampling/data generation -> analytic approach/reflexivity -> themes/process/model -> supporting excerpts/cases -> relationships/contradictions -> interpretation -> transferability/limitations`

### Main displays

A qualitative paper may legitimately have **no main figure**.

Potential displays when they improve understanding:

- participant/sample table;
- thematic/process map;
- conceptual model;
- coding/analytic workflow if method transparency is a contribution;
- timeline/context map;
- matrix of themes/cases when it reveals structure better than prose.

### Direct-reading calibration

Recent 2025 PLOS ONE qualitative studies show real variation: one endometriosis interview study uses only a participant table; other interview studies include a thematic figure. Therefore, `qualitative paper -> theme diagram` is not a rule.

### Anti-patterns

- forced bar charts of theme counts when frequency is not the analytic claim;
- decorative word clouds treated as evidence;
- decontextualized quotes;
- software-package names substituted for explanation of the analytic method;
- implying statistical generalization from purposive qualitative sampling.

## I. Review / systematic review / perspective / synthesis paper

### Core reader question

`What body of evidence or conceptual landscape is being synthesized, how is it organized, what disagreements/gaps/boundaries emerge, and what new synthesis follows?`

### Narrative review / perspective

Common displays:

- conceptual taxonomy;
- mechanism/framework schematic;
- evidence map;
- comparative table;
- timeline;
- decision tree.

Avoid decorative conceptual art that does not encode a real relationship.

### Systematic review / meta-analysis

Common displays:

- study-selection flow;
- risk-of-bias summary;
- forest plot;
- funnel/small-study diagnostic when justified;
- subgroup/meta-regression plot;
- evidence certainty tables.

Do not make a forest plot when pooling is scientifically inappropriate merely because meta-analyses usually contain one.

## Hybrid papers

Many strong papers combine archetypes.

Examples:

- method + biological discovery;
- dataset + benchmark;
- theory + empirical validation;
- clinical trial + biomarker/mechanistic sub-study;
- qualitative + quantitative mixed methods.

For hybrids:

1. identify the **dominant publication promise**;
2. identify secondary promises;
3. build a claim-dependency graph;
4. assign evidence/figure roles per promise;
5. remove duplicate orientation/validation;
6. ensure one archetype's conventions do not erase another's evidence needs.

A method + discovery paper may need to validate the method **before** using it to support the new biological finding, unless the evidence can be interleaved without circularity.

## Figure-count rule

There is no universal ideal number of figures.

Use a **figure necessity test**:

> If this display is removed, does the reader lose the ability to inspect a central pattern, evaluate a decisive comparison, understand an essential system/process, or see a claim-changing boundary?

If no, move it to support or omit it.

Large-scale Viziometrics research classified more than eight million PubMed figures and found figure-type distributions vary widely by field/topic. This supports learning field/archetype-specific visual grammar rather than a universal top-journal figure sequence.

## Writing-form rule

Do not copy syntax statistics from one field into another. Corpus research shows rhetorical moves, phraseology, engagement, and syntactic complexity vary by discipline and by rhetorical function.

Use the hierarchy:

`scientific function -> archetype -> reader/evidence need -> local analogue convention -> sentence/plot realization`

not:

`prestige paper surface -> imitation`.

## Broad-corpus versus close-analogue workflow

### Broad corpus

Use 30–100+ recent papers, stratified by archetype, to learn distributions/tendencies:

- section ordering;
- section/paragraph length;
- figure/table counts;
- figure-call locations;
- caption length/structure;
- recurring evidence roles;
- common plot families;
- what is usually placed in support material.

Frequency is not quality.

### Close analogues

Use 3–6 nearest neighbors to study:

- exact claim/evidence dependencies;
- explanation depth;
- figure role sequence;
- comparator/uncertainty choices;
- local terminology and audience assumptions.

Then build the current paper from its own evidence.

## Source basis

Large-corpus writing/visual evidence includes:

- Lu et al. (2021), 500 published social-science RA introductions across five disciplines, showing substantial rhetorical/phraseological variation. DOI: 10.1016/j.system.2021.102543.
- COSSRAI work on 600 social-science RA introductions and move-linked phrase frames.
- cross-disciplinary syntactic-complexity studies covering 400 social-science/engineering and 300 science introductions, showing function- and discipline-dependent sentence realization.
- 2024 engagement analysis of 200 introductions from applied linguistics, education, electrical engineering and biology.
- Lee, West & Howe, *Viziometrics*, classification of >8 million PubMed figures into visual types, showing strong field/topic variation. arXiv:1605.04951.

Recent direct-reading calibration includes public article pages/figure titles from:

- Wei et al., *Benchmarking algorithms for generalizable single-cell perturbation response prediction*, Nature Methods (2026), DOI 10.1038/s41592-025-02980-0.
- Rawal et al., *Edge curvature drives endoplasmic reticulum reorganization and dictates epithelial migration mode*, Nature Cell Biology (2025), DOI 10.1038/s41556-025-01729-3.
- Xu et al., *A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial*, Nature Medicine (2025), DOI 10.1038/s41591-025-03743-2.
- Ursu et al., *Training data composition determines machine learning generalization and biological rule discovery*, Nature Machine Intelligence (2025), DOI 10.1038/s42256-025-01089-5.
- Strickland et al., *A beneficial arthropod dataset for agricultural landscapes in Western Canada, and adjacent mountain ecosystems*, Scientific Data (2025), DOI 10.1038/s41597-025-05133-2.
- Brauer et al., *Take me seriously: a qualitative interview study exploring healthcare experiences of endometriosis patients*, PLOS ONE (2025), DOI 10.1371/journal.pone.0323883.
- Barnes et al., *Barriers and facilitators to conducting human subjects research at a safety net institution from the perspective of researchers*, PLOS ONE (2025), DOI 10.1371/journal.pone.0313530.
- current JMLR Volume 26 (2025) theory, algorithmic, benchmark and software papers, including FusionBench and physics-informed high-dimensional PDE work.

These cases are **descriptive calibration**, not evidence that a particular figure order caused publication.

## Output contract

When the paper archetype matters, maintain a compact manuscript-specific plan:

```text
Dominant archetype
Secondary archetype(s)
Core reader decision
Headline claims
Evidence dependencies
Expected main-figure roles
Likely support roles
Explanation-depth hotspots
Archetype anti-patterns to avoid
Close analogue set
Observed patterns adopted/adapted/rejected
```

The final manuscript must still be defensible if every analogue paper is removed from view.