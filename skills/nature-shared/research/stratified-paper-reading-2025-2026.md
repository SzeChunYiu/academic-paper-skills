# Stratified recent-paper reading notes, 2025–2026

> Descriptive research layer for calibrating writing, evidence allocation and figures across paper classes. Reviewed 2026-08-25. Do not treat published-paper patterns as causal acceptance evidence or as templates to copy.

## Method

The corpus is intentionally **stratified by epistemic job**, not only by journal prestige.

For each case, record only reusable abstractions:

- contribution archetype;
- study/evidence type;
- argument/evidence sequence recoverable from the public article;
- main-display roles visible from public figure titles/captions when available;
- main-versus-support behavior;
- explanation/writing observation;
- pattern to adopt/adapt/reject.

Do not store full copyrighted article text or reusable sentence templates.

## 1. Computational benchmark / generalization

### Wei et al., Nature Methods, 2026

**Paper:** *Benchmarking algorithms for generalizable single-cell perturbation response prediction*  
**DOI:** 10.1038/s41592-025-02980-0

Public main-figure sequence:

1. workflow and datasets for the benchmark;
2. OOD benchmark in a cellular-context generalization scenario;
3. explicit limitation of current methods in that scenario;
4. genetic-perturbation benchmark in a second generalization scenario;
5. broader perturbation-generalization benchmarking.

Extended Data then carries metric correlations, covariate effects, heterogeneity and fine-tuning-set-size analyses.

**Transferable lesson:** benchmark papers can make a failure/limitation a main figure when it changes the scientific conclusion. Supporting metric/covariate sweeps can remain Extended Data.

### Fu et al., Nature Methods, 2025

**Paper:** *Benchmarking single-cell multi-modal data integrations*  
**DOI:** 10.1038/s41592-025-02737-9

Public article metadata show multiple main benchmark figures with large Extended Data/Supplementary support and source-data files per figure.

**Transferable lesson:** a benchmark should organize comparisons around decision-relevant evaluation scenarios, not expose every metric as equal-priority prose.

### FusionBench, JMLR, 2025

**Paper:** *FusionBench: A Unified Library and Comprehensive Benchmark for Deep Model Fusion*  
**JMLR:** 26(307):1–38.

The abstract makes two promises: a reusable library and a benchmark across multiple tasks/model/dataset settings.

**Transferable lesson:** software-resource and benchmark promises must both be evaluated. Repository usability belongs in the artifact layer; manuscript space should emphasize benchmark design, validity, breadth and scientific/technical conclusions.

## 2. Computational explanation / data-design paper

### Ursu et al., Nature Machine Intelligence, 2025

**Paper:** *Training data composition determines machine learning generalization and biological rule discovery*  
**DOI:** 10.1038/s42256-025-01089-5

Public figure titles show an explanatory progression:

1. training-data composition determines generalization/rule discovery;
2. classification performance varies across antigens/tasks and positive-negative similarity;
3. negative-dataset choice can enhance learning of biological rules.

**Transferable lesson:** the figure sequence is not `architecture -> leaderboard -> ablation`; it moves from phenomenon to explanatory variable to scientific consequence.

### Graber et al., Nature Machine Intelligence, 2025

**Paper:** *Resolving data bias improves generalization in binding affinity prediction*  
**DOI:** 10.1038/s42256-025-01124-5.

**Transferable lesson:** when bias/data construction is itself the causal explanation for model behavior, dataset composition/selection deserves main-text explanation rather than being buried as implementation detail.

## 3. Experimental/mechanistic biology

### Rawal et al., Nature Cell Biology, 2025

**Paper:** *Edge curvature drives endoplasmic reticulum reorganization and dictates epithelial migration mode*  
**DOI:** 10.1038/s41556-025-01729-3.

Public early figure sequence:

1. edge-curvature-dependent ER morphologies;
2. differential ER dynamics at convex versus concave edges;
3. protrusive/contractile forces regulating those morphologies;
4. mathematical model of curvature-dependent ER morphologies.

Later main/source-data structure continues through seven figures with extensive Extended Data.

**Transferable lesson:** a mechanism paper often deepens the same phenomenon through increasingly discriminating evidence. Explanation must make clear why dynamics/forces/modeling are needed after the initial morphology result.

### Moghe et al., Nature Cell Biology, 2025

**Paper:** *Coupling of cell shape, matrix and tissue dynamics ensures embryonic patterning robustness*  
**DOI:** 10.1038/s41556-025-01618-9.

The public article exposes source data for seven main figures and seven Extended Data figures.

**Transferable lesson:** multi-modal mechanistic studies may need multiple evidence modalities; the correct compression is not fewer figures by default, but a clear dependency structure and support allocation.

### Zhang et al., Nature Cell Biology, 2025

**Paper:** *TMEM65 functions as the mitochondrial Na+/Ca2+ exchanger*  
**DOI:** 10.1038/s41556-025-01721-x.

Public metadata show source data across six main figures plus multiple Extended Data figures, including uncropped blot/gel source files.

**Transferable lesson:** molecular-function claims commonly require biochemical/functional orthogonality and source-data integrity, while raw-image provenance belongs in source-data infrastructure rather than narrative prose.

## 4. Randomized/interventional clinical papers

### Xu et al., Nature Medicine, 2025

**Paper:** *A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial*  
**DOI:** 10.1038/s41591-025-03743-2.

Public figure sequence:

1. participant randomization and follow-up;
2. change in FVC with 95% CI and an ANCOVA/missing-data analysis panel;
3. pharmacokinetic properties.

Extended Data includes treatment-stratified/sensitivity material.

**Transferable lesson:** trial figures follow decision logic: who was analyzed, what happened to the primary endpoint, then clinically/pharmacologically relevant support. Confidence intervals carry interpretation.

### Yang et al., Nature Medicine, 2025

**Paper:** *Neoadjuvant chemoradiation with or without PD-1 blockade in locally advanced rectal cancer: a randomized phase 2 trial*  
**DOI:** 10.1038/s41591-024-03360-5.

Public metadata show main statistical source data and subgroup analysis in Extended Data.

**Transferable lesson:** subgroup analysis is not automatically main text; its placement depends on prespecification and whether heterogeneity changes the treatment conclusion.

### Artificial-intelligence individualized atrial-fibrillation trial, Nature Medicine, 2025

**Paper:** *Artificial intelligence for individualized treatment of persistent atrial fibrillation: a randomized controlled trial*  
**DOI:** 10.1038/s41591-025-03517-w.

Public text uses Fig. 1 as participant flow and orients the reader to multicenter randomization before outcome interpretation.

**Transferable lesson:** clinical readers need population/design orientation before algorithmic details.

## 5. Observational / population / burden papers

### Orcutt et al., Nature Medicine, 2025

**Paper:** *Evaluating generalizability of oncology trial results to real-world patients using machine learning-based trial emulations*  
**DOI:** 10.1038/s41591-024-03352-5.

**Transferable lesson:** an ML component in an observational/clinical paper does not turn it into an ML benchmark paper. The primary reader question is generalizability/causal transport, so population, emulation assumptions and clinical effect interpretation outrank architecture details.

### Global research effort versus disease burden, Nature Medicine, 2025

**Paper:** *Global distribution of research efforts, disease burden, and impact of US public funding withdrawal*  
**DOI:** 10.1038/s41591-025-03923-0.

Fig. 1 combines:

- bars comparing disease burden versus research share;
- a country-level map of research-to-burden ratios;
- a scatter plot relating geographic production imbalance to disease-specific research imbalance.

**Transferable lesson:** one figure can legitimately use different plot families when panels answer linked levels of the same scientific question. Panel diversity should follow reasoning, not visual uniformity.

### Argentieri et al., Nature Medicine, 2025

**Paper:** *Integrating the environmental and genetic architectures of aging and mortality*  
**DOI:** 10.1038/s41591-024-03483-9.

The article uses extensive Supplementary/Extended Data for multivariable model detail.

**Transferable lesson:** high-dimensional observational studies should keep the main narrative centered on the estimands and durable conclusions, while exhaustive model outputs/supporting variants remain in support material.

## 6. Dataset / resource papers

### Strickland et al., Scientific Data, 2025

**Paper:** *A beneficial arthropod dataset for agricultural landscapes in Western Canada, and adjacent mountain ecosystems*  
**DOI:** 10.1038/s41597-025-05133-2.

Fig. 1 combines sampling geography with histograms of raw species richness. Fig. 2 is a data-processing workflow.

**Transferable lesson:** resource-paper main displays answer trust/reuse questions such as `what is covered?` and `how was the resource produced?`, not a mechanism-story template.

### Dong et al., Scientific Data, 2025

**Paper:** *An Enhanced Phenology Dataset for Global Drylands from 2001 to 2019*  
**DOI:** 10.1038/s41597-025-05519-2.

**Transferable lesson:** spatiotemporal resource papers typically need coverage, derivation/processing, validation and uncertainty/quality characterization before example use.

### Koscova et al., Scientific Data, 2026

**Paper:** *The Harvard-Emory ECG Database*  
**DOI:** 10.1038/s41597-026-06861-9.

**Transferable lesson:** a clinical signal resource should describe population/source, acquisition, label/metadata structure, quality control, coverage and access. A model benchmark is optional unless fitness-for-use requires it.

### DynamicTHOR, Scientific Data, 2026

**Paper:** *DynamicTHOR: A Scalable Dataset of Human-Centric Dynamic Scenes for Embodied AI*  
**DOI:** 10.1038/s41597-026-07201-7.

**Transferable lesson:** AI datasets should make dataset construction, scale/diversity, annotation/ground truth, quality and reuse conditions visible; software directory structure is secondary artifact documentation.

## 7. Qualitative / interpretive papers

### Brauer et al., PLOS ONE, 2025

**Paper:** *Take me seriously: a qualitative interview study exploring healthcare experiences of endometriosis patients*  
**DOI:** 10.1371/journal.pone.0323883.

The public article lists a participant table but no main figure.

**Transferable lesson:** a rigorous qualitative paper may need **no figure**. Themes and interpretive reasoning can be clearer in prose/table form.

### Barnes et al., PLOS ONE, 2025

**Paper:** *Barriers and facilitators to conducting human subjects research at a safety net institution from the perspective of researchers*  
**DOI:** 10.1371/journal.pone.0313530.

The public article includes a participant table and a simple figure showing themes generated from interview transcripts.

**Transferable lesson:** thematic figures are optional orientation/synthesis tools, not evidence substitutes. The underlying qualitative evidence and interpretation remain in prose/cases/quotes.

### Nolan et al., PLOS ONE, 2025

**Paper:** *The challenges of transgender and nonbinary graduate students in chemistry...*  
**DOI:** 10.1371/journal.pone.0320493.

The public article lists one figure and two tables.

**Transferable lesson:** qualitative display choice depends on whether a visual relationship among themes improves reader understanding; frequency plots should not be forced when frequency is not the analytic claim.

### Johnston et al., PLOS ONE, 2025

**Paper:** *Conducting qualitative research on acute mental health inpatient wards: Lessons from the field*  
**DOI:** 10.1371/journal.pone.0319609.

**Transferable lesson:** methodological/reflexive qualitative papers may be organized around process decisions and lessons rather than conventional Results plots.

## 8. Theory / mathematical / theory+numerics

### Brugiapaglia et al., JMLR, 2025

**Paper:** *Physics-Informed Deep Learning and Compressive Collocation for High-Dimensional Diffusion-Reaction Equations: Practical Existence Theory and Numerics*  
**JMLR:** 26(275):1–51.

The abstract explicitly combines a practical existence theorem with numerical comparison.

**Transferable lesson:** theory+numerics papers need to keep epistemic status separate: theorem/proof establishes one class of claims; numerics illustrate/test practical behavior. Figures cannot substitute for proofs and proofs cannot substitute for empirical performance claims.

### Álvarez et al., JMLR, 2025

**Paper:** *Supervised Learning with Evolving Tasks and Performance Guarantees*  
**JMLR:** 26(17):1–59.

The abstract combines a general methodology, analytical performance guarantees and benchmark experiments.

**Transferable lesson:** hybrid theorem/algorithm papers often need `definition/method -> guarantees -> empirical reliability`, not a standard experimental narrative.

### JMLR theory paper with ensemble monotonicity, 2025

A public JMLR PDF shows theorem statements on classification-error monotonicity followed by a separate experiments section providing simple real-data illustrations.

**Transferable lesson:** experiments can be explicitly illustrative rather than primary proof. The manuscript should say so.

## 9. Review / perspective / conceptual synthesis

### Ito et al., Nature Machine Intelligence, 2025

**Paper:** *Quantifying artificial intelligence through algorithmic generalization*  
**DOI:** 10.1038/s42256-025-01092-w.

The Perspective introduces algebraic circuit complexity as a conceptual framework for quantifying algorithmic generalization.

**Transferable lesson:** a perspective's key evidence can be conceptual/mathematical synthesis. It may need framework diagrams/taxonomies rather than benchmark-style plots.

### Ilievski et al., Nature Machine Intelligence, 2025

**Paper:** *Aligning generalization between humans and machines*  
**DOI:** 10.1038/s42256-025-01109-4.

The Perspective organizes AI and cognitive-science notions of generalization across conceptual dimensions.

**Transferable lesson:** review/perspective figures should encode the synthesis—dimensions, relationships, taxonomy, disagreements—not imitate empirical result panels.

### Liu et al., Nature Machine Intelligence, 2025

**Paper:** *Rethinking machine unlearning for large language models*  
**DOI:** 10.1038/s42256-025-00985-0.

**Transferable lesson:** review articles need explicit scope, taxonomy/comparison criteria, evidence boundaries and unresolved questions; they do not inherit the evidence sequence of original research.

## Cross-case deductions

### 1. A main figure is a scientific decision unit

Across archetypes, main figures repeatedly answer a decision-relevant uncertainty:

- `does the phenomenon exist?`
- `what controls it?`
- `does the intervention work?`
- `does the method generalize?`
- `where does it fail?`
- `what does the dataset cover?`
- `what conceptual synthesis organizes the field?`

The right unit of planning is the **reader question**, not the chart type.

### 2. Main-display failure evidence is legitimate

The Nature Methods benchmark puts an explicit limitation in Fig. 3. This is a strong counterexample to the common AI tendency to hide negative/failure results in SI. If failure changes the headline interpretation, it can be main-text evidence.

### 3. Orientation figures are archetype-dependent

- trials often need participant flow;
- resource papers often need coverage/workflow;
- benchmark papers often need task/dataset/evaluation orientation;
- mechanism papers may instead open directly with the phenomenon;
- qualitative papers may need no figure.

### 4. The same chart can serve different epistemic jobs

A scatter plot can be:

- a mechanism relation;
- an observational association;
- a calibration diagnostic;
- a scaling law;
- a resource coverage relationship.

Therefore chart labels such as `scatter`, `heatmap` or `forest` are too coarse for manuscript planning.

### 5. Published-paper frequency is not a quality score

Large corpus studies show real disciplinary variation in rhetorical moves and syntax. Viziometrics shows field/topic variation in figure types. A package should learn **conditional distributions** and then make manuscript-specific decisions.

## Corpus expansion protocol

For future updates, add papers by a balanced matrix rather than prestige-only sampling:

- archetype;
- field;
- article type;
- publication model;
- evidence modality;
- year;
- open/full-text availability;
- successful counterexample to a current rule.

Maintain two layers:

1. **broad corpus** — 30–100+ papers for descriptive tendencies;
2. **near-neighbor set** — 3–6 papers for deep manuscript-specific reasoning.

Do not use final published papers to infer which surface feature caused acceptance.