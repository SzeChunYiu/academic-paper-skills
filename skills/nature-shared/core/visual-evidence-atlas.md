# Visual evidence atlas

> Research-grounded decision guide for deciding whether evidence belongs in text,
> a table, a quantitative plot, an image plate, a diagram, or a mixed display.
> This atlas is journal-agnostic. Exact venue rules are applied only after the
> scientific display is honest and fit for the reader task.

Last reviewed: 2026-08-29.

## Contents

- [Core rule](#core-rule)
- [Text vs table vs figure vs mixed display](#text-vs-table-vs-figure-vs-mixed-display)
- [Universal evidence packet](#universal-evidence-packet)
- [Table architecture](#table-architecture)
- [Plot and display atlas](#plot-and-display-atlas)
- [Figure sequence as argument](#figure-sequence-as-argument)
- [Panel and caption discipline](#panel-and-caption-discipline)
- [Main paper vs supplement](#main-paper-vs-supplement)
- [Visual integrity and accessibility](#visual-integrity-and-accessibility)
- [Unknown display fallback](#unknown-display-fallback)
- [Research basis](#research-basis)

## Core rule

The visual representation of a paper is part of the scientific argument.

Do not ask:

`What plot looks good?`

Ask:

```text
What must the reader decide or inspect?
-> what scientific quantity or structure answers that question?
-> what unit and dependence structure generated the evidence?
-> what uncertainty/heterogeneity/alternative explanation matters?
-> which representation exposes those features with the least distortion?
-> what exact values or metadata must remain recoverable elsewhere?
```

There is no universal best chart, no universal figure count, and no rule that
figures are inherently better than tables.

## Text vs table vs figure vs mixed display

Choose the display medium from the reader task.

### Prefer text when

- there are only one or two decisive values;
- the exact numeric result is simple and the visual pattern adds no information;
- a sentence can communicate the result without forcing the reader to decode a display;
- a proposed panel merely repeats a sentence.

Text should summarize the scientific observation, not duplicate every table or
figure value.

### Prefer a table when

- exact lookup is the primary reader task;
- many related values must be compared precisely;
- readers need denominators, units, confidence intervals, reference groups,
  model variants, or multiple outcomes in a compact structure;
- a dense graph would hide labels or require the reader to estimate values from marks;
- exact primary-outcome values need to remain recoverable even when a figure
  shows the pattern.

Tables are evidence objects, not screenshots of spreadsheet output.

### Prefer a figure when

- shape, distribution, trajectory, association, spatial structure, heterogeneity,
  uncertainty, mechanism, flow, or a high-dimensional pattern is the scientific object;
- the reader must compare many observations or estimates rapidly;
- the scientific conclusion depends on a pattern that would be difficult to
  reconstruct from a table;
- a failure boundary, subgroup difference, outlier structure, calibration
  defect, or uncertainty pattern is central.

### Prefer a mixed display when

- the figure communicates pattern while a compact table gives exact values;
- a representative scientific image needs population-level quantification;
- a forest plot benefits from aligned study/effect columns;
- a model-performance figure needs both visual curves and a compact metric table;
- a qualitative matrix needs short evidence excerpts plus a conceptual relation;
- a resource paper needs a coverage graphic plus exact inventory/count metadata.

### Duplication rule

Do not repeat the same information in text, table, and figure without a distinct
reader function.

Use:

`figure = pattern`

`table = exactness/detail`

`text = interpretation and the most important observations`

This aligns with current ICMJE guidance to avoid repeating all data across text,
tables, and figures and to keep only displays needed to explain the argument and
assess supporting data.

## Universal evidence packet

Before choosing any plot or table, record:

```text
Reader question
Claim ID
Scientific object / estimand
Population or denominator
Independent/statistical unit
Dependence structure
Observed vs fitted/simulated/imputed/derived status
Candidate display family
Uncertainty quantity and inferential unit
Important heterogeneity or subgroup structure
Alternative explanation the display should expose
Missingness/exclusion/attrition relevant to interpretation
Exact values that must remain recoverable
Main/support placement
Allowed inference
Prohibited inference
```

A display that cannot state its scientific object and allowed inference is not
ready to render.

## Table architecture

### General table contract

Every scientific table should make recoverable:

- table purpose in a short self-contained title;
- compared groups/conditions/models in a reader-friendly order;
- statistical unit and denominator where relevant;
- units of measure;
- exact values at justified precision;
- uncertainty for estimates when it matters;
- reference category/baseline for ratios or model coefficients;
- missing/not-applicable states explicitly rather than ambiguous blank cells;
- nonstandard abbreviations in notes;
- transformations/standardization where they change interpretation;
- source/provenance when the table synthesizes external evidence.

Primary comparisons should usually be easy to read across rows or columns
without repeatedly searching the table.

### Baseline / sample-characteristics table

Use when readers need to understand the analyzed population, groups, exposures,
or data coverage.

Show only scientifically relevant characteristics. Report counts together with
percentages where useful, and make denominators recoverable. Do not automatically
add significance tests to baseline tables; whether they are meaningful depends
on the design and exact reporting standard.

### Outcome / effect table

Useful for multiple outcomes, time points, subgroups, or estimands where exact
values matter.

Prefer columns such as:

```text
Outcome / group
Estimate
Uncertainty interval
Unit / scale
N or events / denominator
Adjusted/unadjusted label when relevant
```

Do not present p-values without the corresponding effect/quantity when the
scientific claim concerns magnitude or uncertainty.

### Regression / model table

For the primary model, expose:

- coefficient/effect estimate;
- interval/uncertainty;
- reference category and units;
- model population and number of observations/events when relevant;
- what adjustment/model variant the column represents;
- prespecified primary exposure/comparison prominently;
- goodness-of-fit or diagnostic metrics only when they answer a reader question.

Dense secondary coefficients can move to supplementary tables rather than
burying the primary comparison.

### Benchmark table

For computational/method papers, exact metric tables are useful when readers
need many task/model values.

Also expose:

- metric direction and units;
- task/site/dataset structure;
- number of runs/seeds/folds or uncertainty unit;
- compute/memory/latency when efficiency is claimed;
- missing/non-comparable entries explicitly;
- whether bolding/highlighting follows a declared rule.

A benchmark table should not hide task heterogeneity behind one grand mean.

### Qualitative evidence matrix

Use to compare themes, cases, participant groups, phases, sources, or competing
interpretations.

Possible columns:

```text
Theme / construct
Source or participant group
Evidence summary / short excerpt pointer
Contradictory or deviant case
Interpretation
Boundary / context
```

Do not turn qualitative evidence into pseudo-quantitative counts unless frequency
is methodologically meaningful and transparently defined.

### Exhaustive/support table

Use supplementary tables for dense robustness specifications, complete regression
outputs, exhaustive benchmark grids, parameter inventories, or detailed source
metadata that support auditability but would interrupt the main argument.

## Plot and display atlas

These are research-informed candidate families, not universal defaults.

### 1. Categorical counts, frequencies, proportions, rates

Use when the scientific object is genuinely categorical.

Candidates:

- bar chart with a zero baseline for counts/frequencies;
- dot/interval plot for rates or proportions when uncertainty/comparison matters;
- ordered horizontal bars for many categories;
- table when exact category values dominate the task.

Show numerator and denominator when proportions could otherwise be ambiguous.

Avoid:

- bars of means for continuous outcomes merely because the software defaults to bars;
- 3D bars;
- pie/donut charts when precise comparison across several categories matters.

Current JAMA guidance is an especially strict example: bar graphs are reserved
for frequency data, pie/3D graphs are rejected, and point estimates rather than
bars are preferred for summary statistics. Treat this as evidence about a sound
scientific distinction, while still resolving each target venue independently.

### 2. Small-n continuous observations

Candidates:

- dot/strip/swarm plot;
- paired points when dependent;
- raw observations plus an appropriate center/interval;
- estimation plot when the scientific question is an effect/difference.

Required:

- show observations when aggregation would hide outliers, skew, multimodality,
  pairing, or sample size;
- name the independent unit.

Avoid mean bars that conceal the distribution. Weissgerber et al. showed that
very different datasets can produce essentially the same bar/line summary, and
PLOS Biology now explicitly recommends showing distributions for small
continuous datasets.

### 3. Larger continuous distributions

Candidates:

- ECDF;
- histogram with justified bins;
- density with declared smoothing;
- box plot;
- violin/raincloud plus observations or quantiles when this improves the reader task.

Do not assume a violin or raincloud is better merely because it is information
dense. Binning and smoothing are transformations and can create or hide shape.
For very small samples, a box/violin summary may imply more distributional
knowledge than the data support.

### 4. Independent group effects

Candidates:

- raw data + effect estimate/interval;
- dot-whisker / estimation graphics;
- distribution display plus explicit contrast.

When the claim is about a difference, make the difference visually recoverable;
do not force readers to mentally subtract two summary bars.

Recent Nature Methods work on multi-group estimation graphics reinforces the
value of showing effect magnitudes and precision for the comparisons that
actually matter instead of centering the visual narrative on an omnibus test.

### 5. Paired / matched change

Candidates:

- connected paired points;
- paired difference distribution;
- slopegraph;
- before/after points plus effect interval.

Required: preserve pairing. A chart that visually separates paired observations
into independent groups misstates the design.

### 6. Repeated / longitudinal trajectories

For modest numbers of units:

- individual trajectories/spaghetti plot;
- group/model trajectory + uncertainty band with raw trajectories visible when
  unit-level variation matters;
- small multiples for heterogeneous groups.

For dense longitudinal data:

- summarized trajectories plus transparent raw-data layer;
- heatmap/lasagna-style display;
- representative trajectories only if the sampling rule is explicit and the
  complete distribution remains available elsewhere.

Do not let overplotting turn hundreds of trajectories into an opaque mass.
Howard (2021) recommends combining model-implied trajectories, confidence bands,
and raw longitudinal observations; lasagna-plot research shows why dense
spaghetti plots can fail through overplotting.

### 7. Association / regression

Candidates:

- scatterplot;
- hexbin/density when overplotted;
- fitted line/curve with uncertainty only when a declared model supports it;
- residual/partial-effect diagnostics when adjustment/model form is part of the claim.

Required:

- expose influential ranges/outliers where relevant;
- distinguish observed points from fitted values;
- label transformations/scales.

A visual association does not establish causality.

### 8. Effect estimates / ratios / subgroup effects

Candidates:

- dot-whisker / forest-style interval plot;
- aligned effect table + interval plot;
- small multiples when outcomes/scales differ.

For odds ratios, risk ratios, hazard ratios, and similar ratio measures, a log
axis often gives a scientifically meaningful symmetric treatment around the
null value of 1. Plot the actual ratio values on the log scale rather than
silently transforming labels.

Avoid comparing subgroups through separate significance labels; a subgroup
claim requires a comparison of effects/interaction appropriate to the analysis.

### 9. Meta-analysis / evidence synthesis

Forest plot should make recoverable, as applicable:

- study identifier;
- study-level effect estimate;
- confidence interval;
- study weight when relevant;
- summary effect/interval;
- direction of effect;
- participant/event totals;
- heterogeneity/inconsistency information appropriate to the model;
- risk-of-bias information or a traceable companion display when decision-relevant.

Cochrane guidance treats forest plots as combined graphical + numeric evidence
rather than decoration around a pooled diamond.

Funnel plots:

- display effect estimate against precision/standard error when evaluating
  small-study effects;
- do not equate asymmetry with publication bias;
- inspect alternative causes such as heterogeneity, methodological differences,
  and chance;
- use appropriate tests only when their assumptions/sample of studies support them.

### 10. Survival / time-to-event

Candidates:

- Kaplan–Meier with numbers at risk and censoring semantics for survival-function comparisons;
- cumulative-incidence curves for competing-risk questions;
- effect interval/forest plot for model-based hazard or time effects;
- restricted-mean survival-time display when that estimand is primary.

Required:

- risk set over time;
- follow-up horizon;
- censoring definition;
- uncertainty;
- no visual extrapolation past useful support.

A generic line chart ignores the changing denominator and is not an acceptable
substitute.

### 11. Classification, probability prediction, calibration, utility

Different plots answer different questions.

Discrimination:

- ROC for sensitivity/specificity trade-offs;
- precision–recall when positive-class performance under imbalance is central.

Probability accuracy:

- calibration/reliability curve;
- calibration intercept/slope or score in table/text;
- prediction distribution to show where calibration is assessed.

Operating decision:

- threshold-specific sensitivity/specificity/PPV/NPV or cost/utility display;
- decision curve when a real threshold-dependent net-benefit question exists.

Required:

- positive class;
- prevalence/base rate;
- threshold semantics;
- uncertainty where relevant.

AUC alone does not establish calibration, utility, fairness, or deployability.

### 12. Heatmaps and clustered matrices

Use when the matrix pattern itself is the scientific object.

Record:

- what each cell encodes;
- normalization/transformation and whether it is row-wise, column-wise, or global;
- missing-value treatment;
- color scale and center/reference;
- row/column ordering;
- distance metric;
- clustering algorithm/linkage;
- number/definition of clusters if interpreted;
- annotation tracks and their source.

Inference boundary:

- adjacency in a heatmap is partly a consequence of ordering;
- dendrogram leaf order can change apparent neighboring patterns without changing
  the hierarchy;
- a dendrogram/heatmap is not proof that discrete natural clusters exist;
- cluster stability or independent evidence is needed for stronger cluster claims.

Use exact-value tables or interactive/source-data companions when readers need
precise cell values from a large matrix.

### 13. Compositional / relative-abundance data

Use stacked bars/areas only when the reader task is composition/orientation and
there are a manageable number of meaningful parts.

Required:

- declare that the parts are relative/compositional;
- state the denominator/normalization;
- avoid interpreting relative decrease as absolute decrease unless absolute data support it;
- consider log-ratio/compositional analysis displays when inference concerns
  relative changes between components;
- provide absolute quantities or counts as a companion when measured and
  scientifically necessary.

Microbiome-methods research demonstrates why a component's relative abundance
can fall even when its absolute abundance is unchanged.

### 14. Geospatial / areal data

Choose the map from the spatial estimand.

Candidates:

- point map for event/location pattern;
- choropleth for rates/ratios/proportions over areas;
- density/smoothed map when the model and bandwidth are explicit;
- cartogram or companion plot when area size badly distorts visual emphasis;
- uncertainty overlay/bivariate map or companion interval plot when estimate
  precision varies geographically.

Required:

- numerator and denominator semantics;
- no-data/zero distinction;
- geographic unit and projection where relevant;
- rate stabilization/smoothing disclosure;
- uncertainty for unstable small-area estimates when it changes interpretation.

Do not use a choropleth of raw case counts when the scientific claim concerns
risk; CDC guidance explicitly recommends rates for area maps and warns that raw
counts lose denominator information.

### 15. Images / microscopy / morphology / blots

A population-level quantitative claim should usually combine:

- representative image(s) with traceable selection;
- scale and acquisition context;
- disclosed processing/cropping/compositing;
- quantitative evidence across the correct experimental unit;
- uncertainty/distribution where relevant.

Do not let a visually striking representative field stand in for population
quantification.

### 16. Qualitative / interpretive evidence

Possible displays:

- case/theme matrix;
- concept/network map;
- process model;
- timeline;
- participant/source map;
- evidence/contradiction matrix.

Use visuals to organize and expose relationships, not to manufacture numeric
precision. Qualitative-display research shows matrices are particularly useful
for comparing experiences, phases, themes, groups, definitions, and excerpts.

### 17. Workflows, mechanisms, causal models, architectures

Declare the semantic type before drawing.

- workflow arrow = sequence/operation;
- causal DAG edge = explicit causal assumption;
- mechanism arrow = bounded observed/inferred/assumed relationship;
- architecture connection = interface/data flow;
- timeline link = temporal order.

Do not use a visually causal arrow when only sequence or association is known.

## Figure sequence as argument

A paper's figures should form an evidence progression rather than a gallery.

For every main figure state:

```text
Figure role
Headline claim/question
What uncertainty remains before the figure
What the figure resolves
What new uncertainty/question it creates
Why this belongs in main text
```

A useful sequence often resembles:

`orientation -> decisive phenomenon -> discrimination/validation -> generalization -> boundary`

but paper archetype controls the actual order.

Examples:

- randomized trial: participant flow -> primary effect -> time-to-event/safety/heterogeneity as scientifically required;
- mechanism paper: phenomenon -> perturbation -> discriminating mechanism -> rescue/orthogonal evidence -> boundary;
- ML paper: problem/method -> benchmark heterogeneity -> calibration/OOD/failure -> efficiency if claimed;
- resource paper: coverage -> quality/bias -> validation -> use case;
- qualitative paper: study/context orientation -> thematic/evidence matrix -> process/conceptual synthesis when useful.

Do not create a universal `Figure 1 schematic + Figure 2 main effect + Figure 3 UMAP`
recipe.

## Panel and caption discipline

Every panel must contribute to one coherent figure-level evidence story.

A multi-panel figure should not be a storage container for unrelated analyses.

For every panel, make recoverable:

- what was measured/compared;
- independent/statistical unit;
- sample/denominator information;
- central tendency/estimate definition when shown;
- uncertainty/error-bar definition;
- statistical test/model pointer when needed;
- transformation/normalization relevant to interpretation;
- symbol/color/line semantics;
- scale bars/image processing where relevant;
- source-data availability.

The caption should teach the reader how to read the scientific evidence without
becoming a dump of implementation details.

## Main paper vs supplement

Main-text priority rises when the display:

- supports a headline claim;
- contains the decisive comparator/control;
- shows a conclusion-changing limitation or adverse result;
- establishes generalization claimed in title/abstract;
- exposes heterogeneity that changes the average interpretation;
- is necessary to understand the paper's method or study population.

Supplement priority rises when the display:

- repeats the same conclusion under many secondary specifications;
- is a detailed diagnostic/audit trail;
- expands a full parameter sweep whose main pattern is already shown;
- contains exhaustive secondary model coefficients/benchmark values;
- preserves reproducibility detail without changing the central interpretation.

Do not hide a result in the supplement merely because it is unfavorable.

## Visual integrity and accessibility

### Scales and axes

- use a zero baseline when length-from-zero is the encoding, especially bars;
- do not truncate axes to exaggerate differences without clear scientific reason and disclosure;
- label log/symlog transformations and units;
- avoid broken axes when they obscure magnitude comparisons;
- keep comparable panels on compatible scales when the scientific task is direct comparison;
- show reference/null lines when they materially aid interpretation.

### Uncertainty

Every interval/error bar names its meaning and inferential unit.

Do not use a generic `error` label. SD, SE, CI, credible interval, prediction
interval, bootstrap interval, and between-replicate variability answer different
questions.

### Color

- sequential values -> perceptually ordered sequential palette;
- deviation around a meaningful center -> diverging palette;
- cyclic quantities -> cyclic palette;
- categories -> distinguishable qualitative palette;
- critical meaning must not depend on color alone;
- avoid rainbow-like maps that create false visual boundaries;
- check grayscale and color-vision accessibility.

### Decoration

Avoid 3D effects, shadows, gradients, pictorial volume, or area encodings that
make value judgment less accurate without serving a scientific task.

### Final-size inspection

A figure that works on a large monitor can fail in the assembled manuscript.
Inspect:

- smallest text;
- line/marker visibility;
- panel-label hierarchy;
- color contrast;
- overplotting;
- axis readability;
- legend/caption handoff;
- cross-panel consistency;
- grayscale/CVD behavior;
- raster/vector export quality.

## Unknown display fallback

If the requested visual object is not covered here or by the maintained display
adapters, do not improvise a fashionable chart.

Research in this order:

1. exact reporting/disciplinary standards for the scientific object;
2. specialist methods literature about the relevant representation and known failure modes;
3. 3–6 genuinely comparable recent papers to learn local evidence roles and display grammar;
4. counterexamples where the common display fails;
5. alternative text/table/display forms that answer the reader task.

Create a temporary manuscript-specific display profile recording:

```text
What comparable papers do
Why they may do it
What evidence supports/contradicts the convention
What our data/estimand require
What we adopt/adapt/reject
What remains unresolved
```

Learn representation logic, not another paper's palette, layout, iconography, or
visual identity.

## Research basis

This atlas operationalizes the existing 39-source scientific-display evidence
registry and extends it with targeted research performed on 2026-08-29.
Source-specific notes and transfer limits are recorded in:

`../research/visual-evidence-atlas-research-2026-08-29.md`

Key sources include:

- ICMJE, *Recommendations for Preparing a Manuscript for Submission to a Medical Journal* (current January 2026):
  <https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html>
- JAMA Network Open, current Instructions for Authors, Tables and Figures:
  <https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors>
- PLOS Biology, current submission guidance on presentation of continuous data:
  <https://journals.plos.org/plosbiology/s/submission-guidelines>
- Weissgerber et al. (2015), *Beyond Bar and Line Graphs*:
  <https://doi.org/10.1371/journal.pbio.1002128>
- Rougier, Droettboom & Bourne (2014), *Ten Simple Rules for Better Figures*:
  <https://doi.org/10.1371/journal.pcbi.1003833>
- Choi et al. (2026), *Getting over ANOVA: estimation graphics for multi-group comparisons*:
  <https://www.nature.com/articles/s41592-026-03187-7>
- Lord et al. (2020), *SuperPlots: Communicating reproducibility and variability in cell biology*:
  <https://doi.org/10.1083/jcb.202001064>
- Howard (2021), longitudinal trajectories with confidence bands and raw data:
  <https://doi.org/10.1177/25152459211047228>
- Cochrane Handbook, reporting/meta-analysis and missing-evidence chapters:
  <https://training.cochrane.org/handbook/current/chapter-iii>
  <https://training.cochrane.org/handbook/current/chapter-13>
- Saito & Rehmsmeier (2015), ROC vs precision–recall under imbalance:
  <https://doi.org/10.1371/journal.pone.0118432>
- Gehlenborg & Wong (2012), *Heat maps*:
  <https://doi.org/10.1038/nmeth.1902>
- Behrisch et al. (2017), *Unboxing cluster heatmaps*:
  <https://doi.org/10.1186/s12859-016-1442-6>
- Gloor et al. (2017), microbiome data are compositional:
  <https://doi.org/10.3389/fmicb.2017.02224>
- CDC Field Epidemiology Manual, current mapping guidance:
  <https://www.cdc.gov/field-epi-manual/php/chapters/describing-epi-data.html>
- Verdinelli & Scagnoli (2013), qualitative data displays:
  <https://doi.org/10.1177/160940691301200117>
- Crameri, Shephard & Heron (2020), scientific colour maps:
  <https://doi.org/10.1038/s41467-020-19160-7>

These sources inform candidate representations and failure modes. They do not
replace the actual study design, statistical analysis, exact reporting standard,
or target-journal requirements.