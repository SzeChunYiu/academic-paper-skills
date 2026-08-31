# Figure purpose and representation evidence — 2026-09-01

**Purpose:** research basis for choosing what scientific figures should show, when a figure is necessary, why one representation is preferable to alternatives, how visual encodings change reader judgments, and how real papers allocate visual evidence across a manuscript.

This ledger deliberately separates **published-practice evidence**, **controlled perceptual/cognitive evidence**, and **deep paper-reading evidence**. They answer different questions and must not be conflated.

## Research architecture

### Layer A — broad published-practice corpora

Question:

> What visual forms do scientists actually publish, and how does prevalence vary by field, topic, venue, and time?

Use this layer to discover conventions and candidate representations, **not** to infer that the most frequent chart is best.

### Layer B — controlled visualization/perception/statistical-cognition research

Question:

> Under studied tasks and audiences, which visual encodings help or hurt accurate perception, comparison, uncertainty reasoning, memory, or interpretation?

Use this layer to reason about reader tasks and known failure modes.

### Layer C — deep contextual paper reading

Question:

> Why did a particular figure exist in this scientific argument, what question did it answer, why were its panels grouped, and what did it replace or leave to support material?

Use this layer for figure-role and sequence calibration. Do not copy visual identity.

## 1. Broad-corpus evidence: prevalence is conditional, not normative

### Viziometrics — >8 million scientific figures

Lee, West & Howe, *Viziometrics: Analyzing Visual Information in the Scientific Literature* (2016).

Public record:
<https://arxiv.org/abs/1605.04951>

The study classified more than 8 million PubMed figures into broad types and reported substantial variation by field/topic. It also found associations between visual-information use and citation impact.

**Supported lesson:** scientific visual practice is heterogeneous and large-scale corpus mining can estimate conditional prevalence.

**Not supported:** more figures cause higher impact; diagrams/plots used by highly cited papers are automatically better; prevalence is a quality score.

**Engineering consequence:** large-corpus evidence feeds candidate-generation and anomaly detection only.

### Biology figure-practice corpus — 8,834 figures, 2,930 studies

Freeman et al., *“Showing the data” in published biology research*, mBio (2026).

DOI: <https://doi.org/10.1128/mbio.00572-26>

The study analyzed 8,834 figures from 2,930 studies in 18 journals and five biology fields (2021–2025). Summary-bar/dynamite plots remained common but declined over time, with strong field variation.

**Supported lesson:** common plot families can remain suboptimal and practice changes over time; field prevalence is descriptive context rather than validation.

**Engineering consequence:** never choose a plot merely because it is locally conventional; compare the information visible to the reader.

### Image-based publication audit — 580 papers

Jambor et al., *Creating clear and informative image-based figures for scientific publications*, PLOS Biology (2021).

DOI: <https://doi.org/10.1371/journal.pbio.3001161>

Across top journals in plant science, cell biology, and physiology, common problems included missing scale bars, unclear inset labels, inaccessible colors, and insufficient explanation. Very few papers met all audited good-practice criteria for all image figures.

**Supported lesson:** publication in a strong journal is not proof that every visual choice is good. Real-paper learning needs critical audit, not imitation.

## 2. Controlled graphical perception and task models

### Cleveland & McGill — graphical perception as a scientific problem

Cleveland & McGill, *Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods*, JASA 79, 531–554 (1984).

DOI: <https://doi.org/10.1080/01621459.1984.10478080>

The work established a controlled-experiment foundation for studying how readers decode quantitative graphical encodings.

**Supported lesson:** chart choice can be evaluated through the perceptual operation the reader must perform; visual encoding is not merely aesthetic.

**Transfer boundary:** perceptual ranking depends on task/context and should not become a universal chart hierarchy detached from the scientific question.

### Brehmer & Munzner — why / how / what visualization tasks

Brehmer & Munzner, *A Multi-Level Typology of Abstract Visualization Tasks*, IEEE TVCG 19, 2376–2385 (2013).

DOI: <https://doi.org/10.1109/TVCG.2013.124>

The typology distinguishes **why** a visualization is used, **how** the reader acts on it, and **what** the data/input/output are.

**Engineering consequence:** figure planning starts from the reader's scientific task rather than chart family.

### Munzner — nested visualization-design model

Munzner, *A Nested Model for Visualization Design and Validation*, IEEE TVCG 15, 921–928 (2009).

DOI: <https://doi.org/10.1109/TVCG.2009.111>

The model separates domain problem characterization, abstraction into data/tasks, visual encoding/interaction, and algorithms. Errors at an upstream level propagate downstream.

**Engineering consequence:** a beautifully rendered plot cannot repair a wrong scientific question, estimand, or data abstraction.

### Franconeri et al. — cognitive/perceptual review

Franconeri, Padilla, Shah, Zacks & Hullman, *The Science of Visual Data Communication: What Works*, Psychological Science in the Public Interest 22, 110–161 (2021).

DOI: <https://doi.org/10.1177/15291006211051956>

The review synthesizes evidence that viewers can rapidly extract some broad visual statistics, while repeated subset comparisons tax attention/working memory. Effective graphics guide attention and match audience expectations without creating misleading mappings.

**Engineering consequence:** when a figure requires repeated legend lookup, mental subtraction, or memory of values across panels, consider a more direct encoding or a table.

### Hullman, Resnick & Adar — uncertainty representation depends on the task

Hullman, Resnick & Adar, *Hypothetical Outcome Plots Outperform Error Bars and Violin Plots for Inferences about Reliability of Variable Ordering*, PLOS ONE 10, e0142444 (2015).

DOI: <https://doi.org/10.1371/journal.pone.0142444>

In controlled experiments, hypothetical outcome plots improved accuracy for some multi-quantity uncertainty judgments relative to error bars and violin plots, while performance differences were smaller for other tasks.

**Supported lesson:** there is no representation that dominates for every uncertainty question; the reader judgment determines the appropriate encoding.

## 3. Contemporary scientific-figure design guidance

### Fujii — effective scientific figures

Fujii, *How to design effective scientific figures*, Nature Human Behaviour 10, 825–827 (2026).

DOI: <https://doi.org/10.1038/s41562-026-02466-9>

The Comment emphasizes designing figures around effective communication across audiences/scientific contexts rather than treating figure preparation as a final technical formatting step.

### Jambor — visualization checklist

Jambor, *A checklist for designing and improving the visualization of scientific data*, Nature Cell Biology 27, 879–883 (2025).

DOI: <https://doi.org/10.1038/s41556-025-01684-z>

The checklist synthesizes design, perception, accessibility and visualization principles for clearer scientific figures.

**Engineering consequence for both:** final visual QA is necessary but comes after scientific representation choice. Typography/color cannot rescue a figure that answers the wrong question.

## 4. Existing specialist evidence retained from the visual-evidence atlas

The prior 2026-08-29 tranche already established task-specific evidence for:

- text versus table versus figure versus mixed display;
- raw-data visibility for continuous data;
- estimation/effect-size plots;
- multilevel/technical-replicate structure;
- longitudinal displays and overplotting;
- forest/funnel plots;
- ROC versus precision-recall versus calibration versus decision utility;
- heatmaps/clustering;
- compositional data;
- spatial maps and denominators;
- qualitative matrices/networks;
- color/accessibility;
- image evidence.

See:
`visual-evidence-atlas-research-2026-08-29.md` and `scientific-display-evidence-ledger-2026-08.md`.

This new tranche does not duplicate those rules. It adds **counterfactual representation selection and figure-purpose/sequence reasoning**.

## 5. Deep real-paper reading: figure role and sequence

The examples below are descriptive case studies from public article pages, captions, and/or full text. Their value is the **relationship between the scientific question and figure function**, not visual imitation.

### 5.1 Computational method/generalization — Nature Methods

**μSAM: automated and interactive segmentation for microscopy** (Nature Methods, 2025).

Observed main-display progression from public article/captions:

1. method/workflow orientation plus qualitative examples;
2. focused benchmark and interaction/fine-tuning behavior;
3. generalist model comparison with quantitative and qualitative evidence;
4. extension to a second microscopy modality/problem.

**Lesson:** mixed qualitative/quantitative panels are useful when they answer linked parts of the same reader question. The sequence moves from orientation to primary evidence to generalization, not from whatever analysis script ran first.

### 5.2 LLM confidence/calibration — Nature Machine Intelligence

**What large language models know and what people think they know** (Nature Machine Intelligence, 2025; public figure captions inspected).

Observed roles:

1. evaluation methodology schematic;
2. calibration/discrimination comparison;
3. calibration diagrams plus confidence distributions/uncertainty;
4. human-confidence response to explanation styles.

**Lesson:** calibration claims require calibration-oriented representations. A generic accuracy bar cannot substitute for a reliability/calibration diagram because the reader task is different.

### 5.3 Biodiversity / spatial ecology — Nature Ecology & Evolution

Public figure sequence inspected in a 2025 butterfly-diversity paper included:

- maps and trend surfaces for diversity gradients;
- hotspot maps plus compact comparative summaries;
- cross-taxon overlap/correlation matrix;
- spatial mismatch maps.

**Lesson:** different chart families can coexist in one paper because each is adapted to a different spatial/comparative reader task. Visual uniformity is not a goal.

### 5.4 Materials / multimodal mechanism evidence — Nature Communications

A 2025 materials paper inspected through public figure captions combined, across the main sequence:

- energy/lattice curves and atomic structures;
- XRD and AFM;
- PFM microscopy;
- reciprocal-space maps;
- switching/hysteresis measurements.

**Lesson:** a multi-modal figure can be scientifically coherent when different representations converge on the same structural/mechanistic question. Panel heterogeneity is acceptable when the **scientific thesis is unified**.

### 5.5 Clinical machine learning — Nature Communications

A 2025 clinical-ML paper inspected through public figure captions used:

- cohort/data/model workflow;
- UMAP orientation;
- Kaplan–Meier survival displays;
- medication-composition summaries.

**Critical lesson:** representation validity must be assessed independently of publication. UMAP can orient readers to projected structure but does not establish natural clusters. Kaplan–Meier is appropriate to censored survival questions in a way a generic line plot is not. A visually elaborate composition chart may still be inferior when precise category comparison is the actual task.

### 5.6 Benchmark / generalization papers — Nature Methods

The existing stratified corpus includes a 2026 Nature Methods perturbation-response benchmark whose main sequence explicitly promoted a **failure/limitation** to a main figure when it changed the scientific conclusion.

**Lesson:** main figures are not a showcase of positive findings. If failure changes the headline claim, hiding it in supplementary material is a visual-integrity failure.

### 5.7 Mechanistic cell biology — Nature Cell Biology

Existing direct-reading notes include a 2025 mechanism paper whose early figure sequence moved from:

1. phenomenon/morphology;
2. dynamics;
3. forces/perturbation;
4. mathematical model.

**Lesson:** a mechanism paper often deepens one phenomenon with increasingly discriminating evidence. Each figure earns its place by closing another alternative, not by supplying a new modality for its own sake.

### 5.8 Randomized clinical trials — Nature Medicine

Existing direct-reading notes include trials where:

1. participant flow/population orientation precedes outcome interpretation;
2. primary outcome/effect with uncertainty is the central display;
3. pharmacokinetic/safety/supporting evidence follows as scientifically relevant.

**Lesson:** figure sequence follows clinical decision logic. Design/population orientation may be essential even though it is not the scientific novelty.

### 5.9 Resource/data papers — Scientific Data

Existing examples combine sampling geography/coverage, distributions, processing workflows, validation, and quality/bias characterization.

**Lesson:** resource figures answer `what exists?`, `what is covered?`, `how was it produced?`, and `can it be trusted/reused?`; they should not imitate a mechanism-paper figure sequence.

### 5.10 Qualitative papers — PLOS ONE

Existing direct-reading examples include rigorous qualitative papers with **no main figure** or only a simple thematic synthesis display.

**Lesson:** the correct number of figures can be zero. A chart is not a marker of rigor.

### 5.11 Theory / theory+numerics — JMLR

Existing direct-reading examples separate theorem/proof claims from numerical illustrations.

**Lesson:** a plot can test/illustrate empirical or numerical behavior but cannot replace proof of a theorem; conversely, a proof cannot substitute for empirical performance evidence.

## 6. Cross-case deductions

### Main figure = scientific decision unit

Across archetypes, strong main displays answer a decision-relevant uncertainty such as:

```text
does the phenomenon exist?
what controls it?
does the intervention work?
does the method generalize?
where does it fail?
what does the resource cover?
how uncertain is the estimate?
what synthesis organizes the evidence?
```

The planning unit is the reader question, not the chart name.

### Figure purpose is paper-archetype dependent

- clinical trial: population/design + effect + uncertainty;
- mechanism: phenomenon + discriminator + orthogonal validation;
- benchmark: evaluation scenario + heterogeneity + failure/generalization;
- resource: coverage + quality + provenance + utility;
- theory: formal object/regime + proof status + numerical illustration when relevant;
- qualitative: prose/table may dominate and no figure may be necessary.

### Same chart family can support different epistemic jobs

A scatter plot may show association, calibration, scaling, resource coverage, or mechanism-related covariation. Calling something a “scatter plot” therefore says little about whether it is scientifically appropriate.

### Negative/failure evidence can deserve main-display status

Main/support placement follows claim importance, not positivity or attractiveness.

### Published-paper frequency is not a quality score

A common chart can persist because of software defaults, field habit, reviewer expectations, or historical inertia. Corpus prevalence is one input to candidate generation, not a release criterion.

## 7. Representation-tournament engineering consequence

For each claim-bearing display, the pipeline should compare plausible candidates on:

```text
reader task
scientific object / estimand
unit / dependence
information preserved
information hidden
uncertainty / heterogeneity / failure visibility
perceptual decoding burden
inferential risk
exact-value recovery
space / attention cost
accessibility
```

The chosen display records why plausible alternatives lost.

This is stronger than “pick from a chart atlas” because the decision is counterfactual.

## 8. Information-loss principle

Every aggregation, projection, smoothing, normalization, sorting, stacking, binning, color mapping, representative-image selection, or pooling operation discards or deemphasizes information.

The right question is not whether information is lost—some loss is necessary—but whether the lost information is irrelevant to the claim and its alternatives.

A representation is unsafe when the hidden information could change the scientific interpretation.

## 9. Research scaling strategy

It is neither feasible nor scientifically sound to “read billions of papers” manually. The scalable design is a three-tier programme:

1. **corpus mining** over millions of available figures/captions/metadata to estimate field-conditional practices and discover candidate families;
2. **controlled evidence synthesis** to establish task-specific perceptual/statistical strengths and failure modes;
3. **stratified deep reading** of complete papers to understand figure purpose, sequence, main/support allocation, and counterexamples.

Future corpus expansion should be stratified by:

- paper archetype;
- discipline;
- evidence modality;
- article type;
- venue family;
- year;
- figure role;
- open/full-text availability;
- counterexamples to current rules.

Do not optimize the training corpus for prestige alone.

## 10. Remaining research gaps

Current hard adapters remain incomplete for:

- very high-dimensional uncertainty displays;
- Bayesian posterior decision displays across specialist domains;
- tensor/network visualizations;
- spectroscopy/signal-processing representations;
- materials phase maps and crystallographic plots;
- electrophysiology/waveform displays;
- causal mediation and longitudinal causal inference graphics;
- complex mixed-effects diagnostic visualization;
- geoscience transects/sections;
- chemistry structure–property display conventions;
- domain-specific imaging modalities;
- interactive/supplementary web figures.

When a manuscript depends on an uncovered specialist family, invoke domain-specific research rather than forcing a generic chart.

## 11. Stable conclusion

The figure system should optimize for:

```text
scientific question
× reader task
× estimand / unit / dependence
× uncertainty / alternative
× information retained
× perceptual accuracy
× inferential safety
× manuscript space
× accessibility
```

not for:

```text
software default
+ field habit
+ visual sophistication
+ imitation of a famous paper
```

The correct representation is the one that lets the intended reader inspect the scientifically relevant distinction with the least material loss or distortion under the actual manuscript constraints.
