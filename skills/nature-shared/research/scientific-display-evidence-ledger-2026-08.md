# Scientific display evidence ledger — 2026-08

**Purpose:** research basis for the scientific display decision contract and its
maintained adapters. This is an evidence ledger, not a style guide and not a
catalogue of fashionable plots.

**Frozen search date:** 2026-08-28  
**Machine-readable registry:**
`../display-contracts/display-evidence-registry.json`  
**Frozen broad-search log:**
`scientific-display-search-log-2026-08-28.json`  
**Current corpus:** 39 included sources: 20 read in full text, 18 read at
abstract level, and one official accessibility standard read directly.

## Search and screening protocol

### Sources searched

- OpenAlex for broad multi-disciplinary discovery;
- Crossref for DOI/title reconciliation;
- Europe PMC full-text XML for open biomedical and methodological articles;
- publisher article pages for current editorials and articles not represented
  correctly in aggregators;
- W3C for the current official accessibility standard.

### Query families

The first search pass used 12 query families:

1. graphical perception and visual encoding;
2. task- and data-dependent chart effectiveness;
3. uncertainty, confidence intervals, and decision quality;
4. raw data, distributions, pairing, and repeated measures;
5. misleading visualization and ethical duties;
6. scientific color maps and color-vision accessibility;
7. ROC, precision–recall, calibration, and decision thresholds;
8. survival and time-to-event plots;
9. DAG and workflow diagram reporting;
10. t-SNE, UMAP, and embedding interpretation;
11. scientific image integrity and image-based figures;
12. alt text and natural-language visualization descriptions.

This produced 84 top-ranked records for title/metadata screening. Targeted DOI,
reference-chain, and official-source follow-up produced the 39-source included
set. DOI metadata were reconciled before inclusion; one initially retrieved
Nature collection URL returned 404 and was replaced by the verified current
*Points of View, anew* article. Incorrect DOI matches were rejected rather than
silently attributed to the intended title.

### Inclusion criteria

At least one of:

- controlled graphical-perception, comprehension, or decision experiment;
- systematic/meta-research audit of published display practices;
- methods evaluation with a direct and bounded display implication;
- current official reporting or accessibility standard;
- specialist display/integrity guidance with clear assumptions and limits.

Excluded:

- visual galleries or templates without evidence;
- journal prestige, citation count, or publication frequency as a quality rule;
- purely aesthetic advice without a reader task;
- tertiary summaries whose primary source could not be verified;
- sources whose DOI/title identity could not be reconciled.

### Stopping rule

This iteration stopped after:

- every maintained adapter had at least two relevant sources;
- all current top-level display-risk families had evidence coverage;
- the candidate-selection and contract fields stopped changing under additional
  searches;
- new results were predominantly domain refinements suitable for later adapters
  rather than missing top-level architecture.

This is not a claim of exhaustive or systematic-review completeness. It is a
versioned engineering evidence base with an update date and explicit gaps.

## Governing synthesis

The stable conclusion across the literature is not “plot X is best.” It is:

```text
reader task × data distribution × dependence structure × estimand
× audience × medium × uncertainty × inference claim
```

controls representation choice.

**Descriptive frequency is not a normative rule.** A chart that is common in
published papers, or common in a prestigious venue, may remain poorly matched
to the task and evidence.

## Evidence by decision family

### 1. Perceptual encodings are not equally accurate—but rankings are bounded

**Evidence:** Cleveland & McGill identified elementary graphical-perception
tasks and experimentally compared decoding accuracy. Heer & Bostock replicated
parts of this programme through crowdsourcing and extended it to area, size,
contrast, and gridline questions. Harrison et al. found correlation-judgment
precision differed across nine visualizations and even differed between
positive and negative correlations. Kim & Heer showed encoding effectiveness
changed with task and data distribution. Saket et al. showed tables, lines,
bars, scatterplots, and pies changed rank across ten reader tasks.

**Contract consequence:** record the reader task and data structure before the
representation. Return candidates, not a universal winner. Preserve a table
candidate when exact lookup—not pattern detection—is the task.

**Transfer limit:** these experiments use bounded stimuli, tasks, populations,
and media. Perceptual accuracy alone does not establish scientific inferential
validity.

### 2. Raw data and dependence structure must not disappear behind summaries

**Evidence:** Weissgerber et al.'s review of 703 physiology articles showed that
bar/line summaries dominated small-n continuous-data displays and could conceal
distribution, outliers, and pairing. Their full-text recommendations are
explicitly conditioned on sample size and design. The later *Reveal, Don't
Conceal* primer likewise conditions dot, box, and violin choices on study
design, sample size, and variable type. Raincloud plots demonstrate one way to
combine observations, density, and summaries.

**Contract consequence:** record statistical unit, pairing/repeated structure,
sample denominator, and the reason for aggregation. Reject an independent mean
bar when the estimand is paired change.

**Transfer limit:** “show every point” is not universal. Large, spatial,
privacy-sensitive, hierarchical, or heavily overplotted datasets require
aggregation, density, sampling, small multiples, or other truthful reduction.
Raincloud plots can themselves become redundant or crowded.

### 3. Uncertainty displays change judgments

**Evidence:** Belia et al. found severe researcher misunderstanding of CI and SE
bars and of independent versus repeated-measures interpretation. Cumming &
Finch's overlap rules are explicitly design- and interval-dependent. Correll &
Gleicher found the encoding of mean/error changed decisions. Hullman et al.
found hypothetical outcome plots substantially improved selected multi-variable
probability judgments but performed worse for some high-variance univariate
tasks. Fernandes et al. found quantile dotplots improved an incentivized transit
decision. Krzywinski & Altman distinguish SD, SE, and CI meanings.

**Contract consequence:** every uncertainty mark declares kind, construction or
level, inferential unit, and caption meaning. Selection follows the reader's
judgment or decision task.

**Contradiction resolved:** animated outcomes are not always superior. The
evidence supports a task-conditioned candidate, not replacing every interval
with animation.

### 4. Color is a quantitative encoding and an accessibility risk

**Evidence:** Crameri et al. document artificial gradients, false boundaries,
grayscale failures, and color-vision exclusion from non-uniform rainbow-like
maps. Nuñez et al. optimize continuous maps for common color-vision
deficiencies. WCAG 2.2 requires that color not be the sole carrier of
information. Rougier et al. distinguish sequential, diverging, and qualitative
roles.

**Contract consequence:** match sequential/diverging/cyclic/categorical
semantics to the data; require redundant non-color cues for critical
distinctions; record the chosen channel and rationale.

**Transfer limit:** “always use viridis” would be another universal-rule error.
Diverging and cyclic quantities, categorical identities, diagnostic images, and
domain conventions require different palettes and validation.

### 5. Classifier plots answer different scientific questions

**Evidence:** Saito & Rehmsmeier show that ROC plots can conceal practical
false-positive burden under class imbalance, whereas precision–recall changes
with class prevalence. Van Calster et al. show why calibration must be assessed
separately from discrimination. Niculescu-Mizil & Caruana show algorithm-specific
probability distortion and calibration behavior.

**Contract consequence:** record prevalence, positive class, decision threshold,
and whether the claim concerns ranking, probability accuracy, operating-point
performance, or utility. AUC alone cannot support a deployment or calibrated-risk
claim.

**Transfer limit:** PR is not universally superior. Costs, prevalence shifts,
thresholds, calibration, and decision consequences control the appropriate
display package.

### 6. Time-to-event data are not ordinary line data

**Evidence:** Pocock et al. identify survival-plot pitfalls involving scale,
follow-up, censoring, and risk sets. KMunicate's 1,274-respondent stakeholder
survey favored extended risk tables and confidence bands.

**Contract consequence:** time-to-event adapters require changing risk sets,
censoring semantics, follow-up horizon, and uncertainty; competing-risk
settings need the correct estimand/display rather than a generic survival line.

**Transfer limit:** KMunicate measured preference, not objective comprehension,
and respondents were mostly statisticians and clinicians.

### 7. Embeddings are method-dependent views, not mechanism receipts

**Evidence:** Wattenberg et al. demonstrate strong dependence of t-SNE appearance
on perplexity, initialization, iteration, and geometry. Kobak & Berens show how
settings affect global structure in single-cell data. Chari & Pachter document
inevitable distortion, contradictory visual stories, and confirmatory-bias
risks from extreme dimension reduction.

**Contract consequence:** record preprocessing, distance, algorithm, parameters,
seed, stability checks, and the narrow reader task. Require independent evidence
for separation, natural-cluster, causal, or mechanistic claims.

**Transfer limit:** these critiques do not prohibit embeddings for bounded
orientation, diagnostics, or post-analysis communication.

### 8. Diagram type controls permissible semantics

**Evidence:** Tennant et al.'s review found target estimands, DAG availability,
construction, and implied adjustment sets were often underreported. CONSORT and
PRISMA flow diagrams expose participant/record flow, exclusions, and
denominators. STROBE emphasizes what was planned, done, found, and inferred.

**Contract consequence:** distinguish workflow, causal DAG, mechanism,
architecture, state, timeline, and evidence graph. A workflow edge means
sequence/operation, not causality. A DAG edge is an assumption to scrutinize,
not a fact created by drawing it.

**Transfer limit:** reporting standards improve transparency; they do not certify
study conduct or causal validity and do not impose one rigid manuscript format.

### 9. Image-based figures need acquisition-to-display integrity

**Evidence:** Rossner & Yamada require preservation of originals, consistent
global adjustments, disclosure, and honest composites. Cromey provides ethical
image-processing boundaries. Jambor et al.'s meta-research across 580 biology
papers found widespread missing scale information, inaccessible colors,
ambiguous annotations, and incomplete object/context explanation.

**Contract consequence:** bind images to originals/acquisition, processing,
crop/composite history, scale, selection logic, and the correct quantitative
unit. An unquantified representative image cannot establish a population-level
effect.

**Transfer limit:** imaging modalities have additional acquisition and integrity
standards; a generic contract cannot replace modality-specific guidance.

### 10. Accessibility requires semantic—not merely textual—equivalence

**Evidence:** Lee et al. found distinctive problems and workflows for alt text in
computing publications. Lundgard & Satyanarayan identify four description levels:
construction, statistical relations, perceptual patterns, and domain insight,
and evaluate them with blind and sighted readers. WCAG prohibits color-only
meaning.

**Contract consequence:** final displays require semantic alt text; complex
displays may require a long description and structured source-data companion.
Alt text must not merely repeat a filename, chart type, or caption.

**Transfer limit:** no single prose template fits all scientific displays.
Description depth depends on display complexity, user task, and what information
is available elsewhere.

## Contract-field justification

| Contract field | Why it exists | Principal evidence IDs |
|---|---|---|
| reader task | chart effectiveness changes by task | `cleveland-mcgill-1984`, `kim-heer-2018`, `saket-2018` |
| estimand/statistical unit | the display must expose the quantity and dependence actually analyzed | `weissgerber-2015`, `belia-2005`, `tennant-2020` |
| representation rationale | no family is universally best | `harrison-2014`, `kim-heer-2018`, `hullman-2015` |
| allowed/prohibited inference | embeddings, workflows, images, and metrics invite predictable overreach | `chari-2023`, `tennant-2020`, `jambor-2021`, `vancalster-2019` |
| transformations/scales | binning, smoothing, axes, reduction, and color can create or hide structure | `crameri-2020`, `wattenberg-2016`, `kobak-2019` |
| uncertainty definition | viewer judgments depend on meaning and encoding | `belia-2005`, `correll-gleicher-2014`, `fernandes-2018` |
| denominator/group coverage | selection and attrition change interpretation | `consort-2010`, `prisma-2020`, `weissgerber-2015` |
| data→analysis→render lineage | stale or selectively altered outputs are not the declared evidence | `rossner-2004`, `jambor-2021`, `rougier-2014` |
| alt text/redundant channels | visual access cannot depend on color or sight alone | `wcag-color-2023`, `lee-2022`, `lundgard-2021` |

## Contradictions and transfer limits

1. **Raw points versus aggregation:** points improve transparency in small data;
   dense or sensitive data may require truthful aggregation. The contract asks
   why and records transformations rather than enforcing one threshold.
2. **Static intervals versus animated/frequency displays:** HOPs and quantile
   dotplots improve some decisions, but not all judgments and not all media.
3. **ROC versus precision–recall:** imbalance can make ROC visually optimistic,
   but PR alone still omits calibration, costs, and deployment thresholds.
4. **Color accessibility versus domain meaning:** perceptual uniformity and CVD
   safety are required, but palette family must still match data topology.
5. **Embedding usefulness versus distortion:** embeddings can orient and
   diagnose; they cannot independently carry quantitative or mechanistic claims.
6. **Reporting standards versus quality:** CONSORT, PRISMA, and STROBE specify
   transparent reporting. Passing them is not proof of correct conduct or low
   bias.
7. **Stakeholder preference versus comprehension:** preferred Kaplan–Meier
   additions are not automatically those with best measured decision accuracy.
8. **Published prevalence versus quality:** the frequency of a display in a
   corpus is never converted into a required or accepted display.

## Evidence-strength policy

Adapters may be maintained when they have:

- at least two relevant sources;
- at least one empirical, systematic/meta-research, specialist methods
  evaluation, or official-standard source appropriate to the rule;
- a stated transfer boundary;
- no claim of universal optimality;
- a behavioral test for any automatically blocking rule.

Expert/editorial guidance may inform candidate families and review questions,
but cannot by itself create a hard scientific blocker unless the blocker follows
from a separately established integrity/accessibility requirement.

## Remaining research gaps

This iteration does **not** claim closure on all display engineering. Priority
follow-up research includes:

- forest/funnel plots, meta-analytic heterogeneity, and small-study effects;
- geospatial maps, projections, spatial uncertainty, and areal normalization;
- heatmaps, clustering stability, normalization, and dendrogram semantics;
- network layout stability, edge uncertainty, and hairball alternatives;
- compositional data and part-to-whole displays;
- diagnostic-test and clinical decision-curve communication;
- dose-response and nonlinear model diagnostics;
- qualitative evidence matrices, timelines, and thematic maps;
- mathematical diagrams, commutative diagrams, proof dependency graphs, and
  notation-heavy tables;
- audio/tactile and genuinely nonvisual access to complex scientific objects;
- interaction between figure sequence, caption design, memory, and reader
  expertise;
- empirical tests of machine-generated alt text and automated visual-integrity
  warnings;
- domain-specific imaging standards beyond the general image contract.

These gaps should become separate, researched adapter iterations—not guessed
rules added to the universal core.
