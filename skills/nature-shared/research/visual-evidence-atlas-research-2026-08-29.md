# Visual evidence atlas research — 2026-08-29

**Purpose:** targeted follow-up research for practical scientific visual
representation: figure-vs-table decisions, data presentation, plot selection,
longitudinal displays, meta-analysis, prediction, heatmaps/clustering,
compositional data, spatial maps, qualitative evidence, color, and current
journal/reporting guidance.

This is a research ledger. It does not define a universal chart hierarchy.

## Search scope

Targeted source families:

1. current journal/reporting guidance on figures and tables;
2. continuous-data presentation and raw-data visibility;
3. effect-size/estimation graphics;
4. repeated-measures and longitudinal displays;
5. meta-analysis forest/funnel plots;
6. classification, calibration, and clinical utility;
7. heatmaps and clustering interpretation;
8. compositional data;
9. geospatial maps and spatial uncertainty;
10. qualitative data displays;
11. color and accessibility.

Priority was given to current official guidance, primary methods articles,
meta-research, and direct specialist tutorials with explicit transfer limits.

## Stable conclusions

### A. Figure vs table vs text is a reader-task decision

Current ICMJE guidance says results should be presented in logical sequence,
important findings first, without repeating all data across text, tables, and
figures. Tables support efficient exact-detail lookup; graphs can replace dense
tables when patterns matter.

**Engineering consequence:** every display plan first declares whether the
reader needs exact values, pattern recognition, or interpretation. Do not make a
figure merely because figures look more publication-like.

Source:
<https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html>

### B. Exact primary results cannot disappear into pictures

Current JAMA Network Open guidance requires exact primary-outcome values with
uncertainty in text/table rather than only in a figure, discourages duplication,
reserves bar graphs for frequency data, rejects pie/3D graphs, recommends point
estimates rather than bars for summary statistics, uses log scales for ratio
measures, and requires numbers at risk for survival plots.

**Engineering consequence:** the atlas separates visual pattern from exact-value
recovery and treats some journal rules as useful evidence about scientific
semantics without universalizing JAMA house style.

Source:
<https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors>

### C. Small continuous datasets should expose observations/distributions

PLOS Biology's current author guidance discourages bar/line graphs for continuous
data, especially small independent sample sizes, and recommends plots that let
readers inspect individual-point distributions.

Weissgerber et al. systematically reviewed 703 physiology papers and showed why
summary bars can hide outliers, skew, multimodality, unequal variance, sample
size, and pairing.

**Engineering consequence:** small-n continuous data route to points/paired
points/distribution-aware displays rather than default mean bars.

Sources:
<https://journals.plos.org/plosbiology/s/submission-guidelines>
<https://doi.org/10.1371/journal.pbio.1002128>

### D. Effect magnitude and precision deserve direct visual attention

The 2026 Nature Methods paper on multi-group estimation graphics argues that
multi-group interpretation is often better centered on relevant effect sizes and
precision rather than an omnibus null test plus a web of post-hoc comparisons.

**Engineering consequence:** independent-group and multi-group effect claims
should consider estimation/dot-whisker graphics that expose the actual contrast
and interval.

Source:
<https://www.nature.com/articles/s41592-026-03187-7>

### E. Multilevel biological data need both observation-level variability and replicate-level reproducibility

Lord et al.'s SuperPlots work shows that displaying many cells/technical
observations without the independent experimental replicates can suggest false
precision. Their proposed visual layering exposes both within-experiment spread
and between-experiment reproducibility.

**Engineering consequence:** plotting every point does not fix pseudoreplication.
The atlas requires the independent/statistical unit and dependence structure
before choosing point layers and intervals.

Source:
<https://doi.org/10.1083/jcb.202001064>

### F. Longitudinal data need linked units, raw trajectories, and overplotting control

Howard (2021) recommends combining model-implied trajectories, confidence bands,
and raw repeated-measures data so readers can see nonlinearity, outliers, and the
relationship between data and fitted trends.

Lasagna-plot research demonstrates that classical spaghetti plots become
unreadable at large subject counts because trajectories overlap.

**Engineering consequence:** modest-n longitudinal studies may use individual
trajectories; dense studies need small multiples, raw-data overlays, lasagna/
heatmap-style encodings, or other truthful reductions.

Sources:
<https://doi.org/10.1177/25152459211047228>
<https://pmc.ncbi.nlm.nih.gov/articles/PMC2937254/>

### G. Forest plots are graphical + numeric evidence; funnel plots diagnose small-study effects, not automatically publication bias

Cochrane guidance describes forest plots as displays of study-level effect
estimates, confidence intervals, weights, summary effects, participant/event
information, direction, heterogeneity, and related synthesis metadata.

Cochrane's missing-evidence chapter recommends standard error/precision on the
funnel axis and emphasizes that asymmetry can arise from many mechanisms beyond
selective publication.

**Engineering consequence:** a pooled diamond without study effects/uncertainty
is not a sufficient synthesis display, and funnel asymmetry must not be labelled
`publication bias` by appearance alone.

Sources:
<https://training.cochrane.org/handbook/current/chapter-iii>
<https://training.cochrane.org/handbook/current/chapter-13>

### H. ROC, precision-recall, calibration, and decision curves answer different questions

Saito & Rehmsmeier show why ROC displays can look reassuring under severe class
imbalance while precision-recall more directly exposes positive-prediction
performance. Existing display-registry evidence separately supports calibration
curves for probability accuracy.

BMJ clinical-prediction guidance explains decision curves as net-benefit displays
across meaningful threshold probabilities; they address utility, not merely
statistical discrimination.

**Engineering consequence:** classifier figures become a package chosen from the
claim: ranking/discrimination, positive retrieval, probability calibration,
operating point, and utility are separate reader questions.

Sources:
<https://doi.org/10.1371/journal.pone.0118432>
<https://www.bmj.com/content/386/bmj-2023-078276>
<https://www.bmj.com/content/352/bmj.i6>

### I. Heatmap structure depends strongly on transformation, clustering, and ordering

Gehlenborg & Wong describe heatmaps as useful multivariate displays that require
careful application.

`Unboxing cluster heatmaps` demonstrates an important perceptual trap: rotating
dendrogram children leaves the hierarchy unchanged but can dramatically change
which rows/cells appear adjacent, altering perceived clusters.

Heatmap implementation literature emphasizes that scaling, transformation,
distance, linkage, ordering, and annotations are analytic decisions, not
cosmetic parameters.

**Engineering consequence:** every inferential heatmap declares scaling,
normalization, color center, distance/linkage, row/column ordering, and cluster
stability/validation when clusters are claimed. Dendrogram adjacency is not
independent evidence of natural clusters.

Sources:
<https://doi.org/10.1038/nmeth.1902>
<https://doi.org/10.1186/s12859-016-1442-6>
<https://pmc.ncbi.nlm.nih.gov/articles/PMC10989952/>

### J. Composition is not absolute abundance

Microbiome compositional-data literature shows that changes in relative
abundance can be induced by changes in other components; a relative decrease
need not be an absolute decrease.

**Engineering consequence:** stacked relative-abundance plots are orientation
views, not receipts for absolute-change claims. The display must declare the
composition denominator and use compositional/log-ratio-aware analysis when
that is the inferential target.

Sources:
<https://doi.org/10.3389/fmicb.2017.02224>
<https://onlinelibrary.wiley.com/doi/10.1111/1755-0998.13730>

### K. Choropleth maps need denominators and uncertainty

The CDC Field Epidemiology Manual recommends rates rather than raw counts for
area/choropleth maps and emphasizes population distribution, no-data states,
legends, and rate semantics.

Health-cartography research shows that mapped rates can still mislead when
population denominators vary widely and that uncertainty/reliability should be
communicated for unstable small-area estimates.

**Engineering consequence:** map contracts record numerator, denominator,
spatial unit, rate stabilization/smoothing, no-data/zero distinction, and
uncertainty. Raw case-count choropleths are blocked for risk claims.

Sources:
<https://www.cdc.gov/field-epi-manual/php/chapters/describing-epi-data.html>
<https://pmc.ncbi.nlm.nih.gov/articles/PMC2760860/>
<https://doi.org/10.1002/sta4.150>

### L. Qualitative papers can use matrices/networks without pretending the data are quantitative

Verdinelli & Scagnoli reviewed visual displays in qualitative research and found
matrices especially adaptable for themes, participant characteristics,
experiences, phases, definitions, excerpts, and cross-case comparison.

**Engineering consequence:** qualitative evidence can be visually rich through
matrices, networks, timelines, process models, and theme/source maps. The atlas
forbids converting theme salience into fake numerical precision merely to create
a chart.

Source:
<https://doi.org/10.1177/160940691301200117>

### M. Color is data encoding, not decoration

Crameri, Shephard & Heron document how perceptually non-uniform rainbow-like
maps can invent apparent boundaries or distort magnitude and how red-green
choices create accessibility failures.

**Engineering consequence:** palette topology follows sequential/diverging/
cyclic/categorical data semantics, and critical distinctions use redundant
non-color encoding.

Source:
<https://doi.org/10.1038/s41467-020-19160-7>

## Transfer limits

1. A journal's figure rule is not automatically a universal scientific law.
2. A visualization that is good for one reader task may be poor for another.
3. Raw-data visibility does not justify treating nested/technical observations as independent.
4. Showing more marks can reduce comprehension through overplotting.
5. A sophisticated chart does not repair a wrong estimand or invalid analysis.
6. A published visual convention is evidence about practice, not proof of effectiveness.
7. Exact target author instructions still control file format, dimensions,
   panel limits, legend limits, and production mechanics.
8. Machine-generated visual suggestions still require final-size visual and
   scientific inspection.

## Resulting skill changes

The 2026-08-29 tranche adds a shared `visual-evidence-atlas.md` and routes it
through academic writing, the academic-paper pipeline, and scientific figure
planning.

The atlas adds explicit contracts for:

- text vs table vs figure vs mixed display;
- scientific table design;
- small/large continuous data;
- paired and longitudinal data;
- effect/forest/funnel displays;
- survival;
- prediction/classification/calibration/decision utility;
- heatmaps/clustering;
- compositional data;
- geospatial maps;
- qualitative evidence matrices;
- image evidence and diagrams;
- main-vs-support display allocation;
- figure sequence as manuscript argument;
- final visual integrity/accessibility.

This tranche deliberately does not convert every newly researched family into a
hard machine blocker. The maintained machine adapters require reconciled source
registry entries and dedicated behavioral fixtures. The atlas can provide
candidate families and review questions immediately while preserving the
existing fail-closed rule: unsupported display families trigger domain-specific
research rather than a guessed universal chart.