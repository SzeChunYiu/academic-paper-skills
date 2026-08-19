# Direct-reading notes: cross-venue 2025–2026 papers

> Working research notes for the writing skill. Last reviewed: 2026-08-19.
>
> These notes abstract **rhetorical structure, evidence sequence, and claim calibration** from published papers. They are not sentence templates and should never be used to copy distinctive published prose.

## Contents

- [Purpose and sampling](#purpose-and-sampling)
- [Nature Communications local corpus](#nature-communications-local-corpus)
- [Nature Machine Intelligence](#nature-machine-intelligence)
- [npj Computational Materials](#npj-computational-materials)
- [PLOS ONE: clinical machine-learning proof of principle](#plos-one-clinical-machine-learning-proof-of-principle)
- [JAMA Network Open: observational cohort](#jama-network-open-observational-cohort)
- [IEEE Access: engineering benchmark/resource paper](#ieee-access-engineering-benchmarkresource-paper)
- [eLife: statistical/methodological paper](#elife-statisticalmethodological-paper)
- [PLOS ONE: qualitative-methods tutorial](#plos-one-qualitative-methods-tutorial)
- [JMLR: theory/method/software publication ecology](#jmlr-theorymethodsoftware-publication-ecology)
- [Cross-paper lessons](#cross-paper-lessons)
- [What stays local](#what-stays-local)

## Purpose and sampling

This direct-reading layer complements large move/syntax corpora in `cross-disciplinary-writing-evidence.md`.

Selection aims to create **contrast**, not a prestige ranking. Papers were chosen across:

- broad-audience and specialist science;
- experimental/computational/clinical/methodological work;
- engineering/computer science;
- quantitative observational research;
- qualitative/mixed-method methodological writing;
- theory/method/software publication ecologies.

When a local corpus is used for an actual target manuscript, follow `target-corpus-calibration.md` and sample more comparable papers of the exact article type.

## Nature Communications local corpus

The repository's `nat-comms-2025-corpus.md` already contains a manually curated set of **20 open-access 2025 CS/AI papers**.

Useful local tendencies include compact challenge framing, explicit contribution statements, strong figure-led Results, and recurring conclusion-first paragraph openings.

### Lesson

Those patterns are valuable **for that stratum**. They should not control clinical, qualitative, theoretical, or non-Nature writing.

## Nature Machine Intelligence

### Paper

*A multimodal large language model for materials science* (2026).

### Observed logic

The Results do not simply repeat one `claim -> number` paragraph form. The evidence progresses through several questions:

- overall evaluation/capability;
- ablation/component contribution;
- external/generalization behavior;
- interpretability/representation analysis.

Paragraphs frequently combine a result nucleus with evidence, comparison and a narrow interpretive satellite.

The Discussion then re-integrates those separate evidence streams into the paper-level contribution instead of walking through figures in order.

### Writing lesson

A good Results sequence is often a **dependency graph of questions**. `Main benchmark -> ablation -> generalization -> interpretation` is useful when each result creates the reason for the next; it is not a universal journal sequence.

## npj Computational Materials

### Paper

*Developing a complete AI-accelerated workflow for superconductor discovery* (2026).

### Observed logic

The paper combines computational and experimental evidence. Results move through:

- predictive/computational filtering;
- disorder/structural analysis;
- synthesis;
- diffraction/characterization;
- low-temperature measurements.

The evidence sequence matters because later experimental blocks validate or constrain earlier computational predictions.

The Discussion re-opens the broad discovery problem and reconstructs the contribution around **progressive filtering plus experimental confirmation**.

### Writing lesson

Interdisciplinary Results should follow **evidentiary dependence across modalities**, not force all computation into one section and all experiment into another if that separation obscures why one validates the other.

## PLOS ONE: clinical machine-learning proof of principle

### Paper

*Machine learning detects hidden treatment response patterns only in the presence of comprehensive clinical phenotyping* (2025).

### Observed logic

The Introduction spends meaningful space on:

- clinical phenotype definition;
- personalized-treatment motivation;
- concrete clinical examples;
- limitations of conventional analysis;
- study design and the simulated-RCT question.

This is much more context/inference heavy than a compact technical `task -> gap -> model` funnel.

The Results use a sequential inferential narrative, and the Discussion cycles through main finding, comparison/interpretation, qualification and recommendation.

### Writing lesson

Clinical/health-data papers often need to establish **what the clinical construct and inference mean** before technical novelty becomes interpretable. Shortening that context merely to resemble a selective ML journal can make the argument worse.

## JAMA Network Open: observational cohort

### Paper

Gurayah et al., *Barriers to Health Care and Cancer Screening* (2026), DOI `10.1001/jamanetworkopen.2026.7024`.

### Abstract architecture

The article uses an explicitly structured clinical abstract:

- Importance;
- Objective;
- Design, Setting, and Participants;
- Main Outcomes and Measures;
- Results;
- Conclusions and Relevance.

The Results move from cohort composition to barrier burden, latent factor structure and adjusted associations, with effect estimates and confidence intervals central to the summary.

### Introduction architecture

The Introduction establishes:

1. screening's clinical importance;
2. persistent disparities despite guidelines;
3. multifactorial barriers;
4. the opportunity afforded by a large diverse linked EHR/self-report cohort;
5. why correlated barriers motivate factor analysis.

The need is therefore partly **population/evidence coverage + multivariate structure**, not merely `no one has studied barriers`.

### Methods architecture

Methods open with ethics/data access/reporting-guideline status, then organize by:

- study population;
- barrier measurement;
- screening-adherence definition;
- inclusion/exclusion;
- covariates;
- statistical analysis;
- sensitivity analyses.

This is a strong example of Methods as inferential credibility: eligibility, ascertainment, covariates and selection-bias sensitivity are central to what the associations mean.

### Discussion architecture

The Discussion is recursive:

- headline association;
- possible explanation/context for low screening;
- financial-barrier interpretation and prior evidence;
- policy/practice implication;
- logistical-barrier interpretation;
- other psychosocial/competing obligations;
- future question;
- dedicated limitations with consequences for measurement, representativeness and selection.

### Writing lesson

For observational research, **design and inferential boundary are rhetoric**, not administrative Methods detail. The writing skill must not convert `associated with` into causal intervention language simply because the Discussion discusses policy relevance.

## IEEE Access: engineering benchmark/resource paper

### Paper

*Machine Learning for Online Transient Stability Assessment* (2026), IEEE Access, DOI `10.1109/ACCESS.2026.3686293`.

### Introduction architecture

The Introduction identifies inconsistent evaluation practice and reproducibility/cross-study comparability as the problem, then gives an explicit four-item contribution list:

- unified treatment/review of fundamentals;
- benchmark of many ML models under a common protocol;
- latency–accuracy trade-off analysis;
- an open-source package/resource.

It also ends with an explicit section roadmap.

### Whole-paper architecture

The paper uses a recognizable engineering structure:

- Introduction;
- ML/TSA background and method categories;
- experimental setup + comparative results;
- Discussion;
- Conclusion.

The Conclusion enumerates performance, model-family behavior, trade-offs and the software/resource contribution.

### Writing lesson

Explicit contribution lists and `remainder of paper` roadmaps can be useful **local engineering conventions**. The core skill should preserve them when a target venue/community benefits from them, not export them into all journals.

The evidence sequence also shows why a benchmark paper is not a simple method paper: evaluation protocol, comparator breadth, latency/accuracy trade-offs and reproducibility resource are separate contribution branches.

## eLife: statistical/methodological paper

### Paper

*Thrifty wide-context models of B cell receptor somatic hypermutation* (2025), eLife, DOI `10.7554/eLife.105471`.

### Observed abstract logic

The abstract moves through:

- why probabilistic modeling of the biological process matters;
- an identified representation/parameter-growth challenge;
- the proposed wide-context/thrifty modeling approach;
- comparative performance;
- negative results for some elaborations;
- disagreement between fitting approaches.

### Writing lesson

Method papers can communicate **negative comparative findings** as first-class scientific results. The skill should not force every methodological variant into an improvement narrative.

The current eLife publication model also pairs articles with an assessment of significance and strength of evidence, reinforcing the usefulness of keeping **importance** and **evidence strength** conceptually separate when drafting claims.

## PLOS ONE: qualitative-methods tutorial

### Paper

Leplaa et al., *Applying qualitative methods to experimental designs: A tutorial for the behavioral sciences* (2025), DOI `10.1371/journal.pone.0324936`.

### Observed logic

This is not an ordinary empirical IMRaD paper. Its contribution is methodological guidance plus an empirical worked example.

The paper:

- argues for the value of qualitative evaluation within experiments;
- identifies insufficient methodological guidance;
- walks through research stages and methodological choices;
- emphasizes qualitative rigour;
- uses a worked example to illustrate the framework;
- Discussion summarizes the practical framework and intended audience.

Within the Introduction/methodological discussion, alternative interview forms are presented with **advantages and limitations in context**, not as one baseline to defeat.

### Writing lesson

A tutorial/methodological synthesis may organize around **decisions and considerations**, not a Results ladder. `method = modules` and `related work = competitor limitations` are poor defaults here.

## JMLR: theory/method/software publication ecology

### Corpus snapshot

JMLR Volume 26 (2025) includes long papers spanning:

- optimization theory;
- PAC-Bayes/meta-learning;
- causal inference;
- uncertainty quantification;
- graph representation learning;
- random matrix theory;
- federated learning;
- theoretical convergence;
- statistical inference;
- open-source software papers.

Article lengths in the volume range from short software papers to formal papers approaching or exceeding many tens of pages.

### Writing lesson

`computer science / machine learning` is not one rhetorical genre. A theoretical convergence paper, causal-inference paper, benchmark, and software paper may share a venue while needing different Introduction, Methods/formalism, Results and Conclusion logic.

Target calibration should therefore match **contribution type and evidence architecture**, not only journal and field name.

## Cross-paper lessons

### 1. Reason for the next analysis is more reusable than paragraph wording

Across venues, strong evidence sequences often have the pattern:

`evidence A changes what is uncertain -> analysis B targets that uncertainty`.

This is the core rationale behind the writing engine's evidence-dependency graph.

### 2. Contribution lists are local tools

Explicit contribution bullets are common/useful in some engineering/CS papers, but clinical and broad-audience science often integrate the study response into prose.

### 3. Structured abstracts are article-type conventions

JAMA's detailed structured abstract is useful because observational/clinical readers need design, population, outcomes and uncertainty visible immediately. It should not become the default for theoretical or materials papers.

### 4. Methods are part of argument credibility

Across JAMA observational work, eLife methods work and computational papers, choices about samples/data, measurement, model/analysis and validation determine what readers can infer.

### 5. Negative evidence can be a contribution

Method comparisons and replication/validation work should be allowed to conclude that extra complexity does not help, an expected effect is absent, or a claim does not generalize.

### 6. Discussion architecture is often recursive

Finding -> interpretation -> prior work -> qualification/implication can recur several times. A single final limitations block is not sufficient when a boundary constrains a specific earlier interpretation.

### 7. Publication ecology matters below the journal level

Article type, research paradigm and evidence structure can explain more variation than publisher brand.

## What stays local

Do **not** promote these observations to universal rules:

- Nature-style contribution phrasing;
- JAMA structured abstract headings;
- IEEE contribution bullets/section roadmap;
- eLife assessment terminology;
- one exact Results subsection sequence;
- one paragraph length or sentence-density target.

Use them as evidence for a general rule only when the rule survives comparison across different publication ecologies.
