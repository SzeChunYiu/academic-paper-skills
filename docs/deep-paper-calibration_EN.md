# Deep Paper Calibration: Learn the Scientific Job, Not the Prestige Surface

[中文](deep-paper-calibration.md)

The academic-paper skills now use two complementary research layers:

1. a **broad stratified corpus** to learn descriptive tendencies across many papers;
2. a **small near-neighbor set** to understand the exact reasoning/evidence dependencies of the current manuscript.

The goal is not to make every paper look like Nature, Science, Cell, IEEE, JAMA, or NeurIPS. It is to learn how different paper classes solve different reader problems.

## Why one universal paper template fails

Different papers make different epistemic promises.

A mechanism paper asks what produces a phenomenon. A randomized trial asks whether an intervention changes a prespecified outcome. A benchmark asks whether methods work under fair, relevant evaluation regimes. A resource paper must establish coverage, quality and reuse. A theory paper may establish its central claim by proof. A qualitative paper may need no figure at all.

The working tuple is:

```text
contribution archetype
× study design
× evidence modality
× intended reader
× publication model
```

Journal/venue conventions are applied after this scientific classification.

## Archetypes currently modeled

The shared atlas distinguishes at least:

- experimental discovery / mechanism;
- randomized trial / intervention;
- observational / epidemiological / clinical association;
- computational / machine-learning empirical;
- method / tool / software / instrument;
- dataset / resource / benchmark-resource;
- theory / proof / mathematical;
- qualitative / interpretive;
- review / systematic review / perspective / synthesis;
- hybrid papers combining several promises.

These are priors, not boxes. A methods paper can also make a biological discovery; a clinical trial can contain a mechanistic sub-study; a dataset paper can also benchmark methods.

## What direct reading teaches

Recent public-paper reading was deliberately stratified across contrasting paper classes.

### Computational benchmark

A 2026 Nature Methods single-cell perturbation benchmark publicly sequences its main figures as:

```text
workflow + datasets
→ OOD benchmark
→ explicit limitation of current methods
→ second generalization regime
→ broader benchmark
```

The important lesson is not the number five. It is that **an explicit limitation can deserve a main figure** when it changes the headline interpretation.

### Experimental mechanism

A 2025 Nature Cell Biology mechanism paper progresses from:

```text
curvature-dependent phenotype
→ dynamics
→ force/dependency evidence
→ mathematical model
```

Each figure removes a different uncertainty about the same phenomenon.

### Randomized trial

A 2025 Nature Medicine phase 2a trial begins with:

```text
participant flow
→ primary outcome with 95% CI
→ pharmacokinetics
```

That is trial decision logic. An architecture diagram or benchmark heatmap would not be the natural opening simply because the intervention was AI-discovered.

### Resource paper

A 2025 Scientific Data resource paper starts with sampling geography plus richness distributions, then shows the processing workflow. Its key trust questions are **what is covered?** and **how was the resource produced?**

### Qualitative paper

A 2025 PLOS ONE endometriosis interview study uses a participant table but no main figure. Another 2025 interview study includes a simple themes figure.

Therefore:

> `qualitative study → thematic diagram` is not a rule.

The figure must earn its place.

### Theory + numerics

JMLR 2025 papers show theory-heavy workflows where theorem/proof and numerical evidence have separate epistemic roles. Numerical plots can illustrate or test practical behavior, but they cannot substitute for a proof when the claim is mathematical.

## Broad empirical evidence

The direct-reading layer is paired with larger corpus research.

Examples include:

- 500 published research-article introductions across five social-science disciplines, showing substantial disciplinary variation in rhetorical realization;
- a 600-introduction social-science corpus mapping phrase frames to rhetorical moves;
- cross-disciplinary syntactic-complexity studies covering hundreds of science, engineering and social-science introductions;
- cross-disciplinary engagement studies across applied linguistics, education, electrical engineering and biology;
- Viziometrics, which classified **more than eight million PubMed figures** and found substantial field/topic variation in visual types.

The implication is not "learn the average paper." The implication is **stratify before generalizing**.

## Broad corpus versus close analogues

### Broad corpus: 30–100+ papers

Use to estimate tendencies such as:

- section presence/order;
- paragraph/sentence distributions;
- figure/table counts;
- caption lengths;
- figure-call locations;
- common evidence roles;
- common plot families;
- main-versus-support allocation;
- rhetorical move prevalence after semantic annotation.

Frequency is not quality.

### Close analogues: 3–6 papers

Use to understand:

- exact claim/evidence dependencies;
- why evidence block B follows A;
- explanation depth;
- what comparator/uncertainty is visually exposed;
- which negative/failure evidence is kept visible;
- local terminology and reader assumptions.

Close papers are read deeply. Broad corpora are summarized descriptively.

## Scalable figure/caption inventory

When extracted papers are available as `.md` / `.txt`, use:

```bash
python skills/nature-writing/scripts/corpus_figure_inventory.py CORPUS_DIR \
  --json corpus-figures.json \
  --csv corpus-displays.csv
```

The tool inventories:

- figure/table captions;
- in-text figure/table calls;
- current section context;
- transparent keyword-based **candidate** roles such as orientation/workflow, primary finding, mechanism, validation, OOD/generalization, robustness, failure/limitation, heterogeneity, calibration/diagnostic, resource coverage, theory/model, and qualitative synthesis.

These role labels are triage aids only. They are not semantic ground truth, quality scores, acceptance predictors, or instructions to copy common plot types.

Use `corpus_structure_stats.py` alongside it for section/paragraph/sentence surface statistics, then perform semantic reading.

## Figure planning after calibration

The final decision remains manuscript-specific:

```text
claim
→ reader question
→ statistical/scientific unit
→ estimand
→ data structure
→ uncertainty / alternative explanation
→ representation
→ main/support/omit
```

Examples:

- paired treatment effect → expose paired change;
- probabilistic prediction → show calibration if calibrated probabilities are claimed;
- generalization → expose performance across the regimes named by the claim;
- failure boundary → show it in main text if it changes the headline conclusion;
- small-sample continuous data → expose individual observations/distribution when useful;
- qualitative themes → use a conceptual display only when relationships are clearer visually than in prose.

Do not start from "top papers usually use a heatmap."

## Final manuscript-surface QA

Content planning alone is not sufficient to stop codebase leakage. Later rewrites and figure-generation pipelines can reintroduce internal artifacts.

Every manuscript-facing surface now receives a final check for:

- local/repository file paths;
- script/notebook/config filenames;
- output filenames;
- helper/class/function names;
- CLI commands/flags;
- branch/PR/issue/commit/CI/test history;
- raw repository links outside designated availability sections;
- plotting-pipeline language inside figure legends.

The rule is:

> **The audit trail may name the artifact; the paper should name the science.**

A conservative linter is available:

```bash
python skills/nature-shared/scripts/audit_manuscript_surface.py manuscript.md --strict
```

It also catches high-confidence punctuation defects such as doubled punctuation, punctuation spacing, malformed figure references and unmatched brackets. Meaning-sensitive punctuation still requires contextual editing.

## Punctuation is not "style"

The package now treats punctuation/copy-editing as its own final QA layer.

It distinguishes:

- simple mechanical defects that can be flagged safely;
- target-specific punctuation such as citation placement/equation punctuation;
- meaning-sensitive punctuation such as restrictive commas;
- scientific typography such as hyphen versus en dash versus minus sign.

No global punctuation transform is safe for all journals and disciplines.

## What we deliberately do not learn

We do not infer that:

- more figures are better;
- a prestigious journal's common layout is intrinsically superior;
- a visual type causes acceptance;
- a final published paper reveals why it was accepted;
- a correlation between figure types and impact is an acceptance recipe;
- one local caption style is universal;
- qualitative, theoretical, clinical and computational papers should share one figure grammar.

Published papers show **surviving solutions under a publication ecology**, not causal acceptance rules.

## Practical manuscript-specific output

For a serious paper rewrite, the package can maintain:

```text
Dominant paper archetype
Secondary archetype(s)
Core reader decision
Headline claims
Evidence dependencies
Explanation-depth hotspots
Main-figure roles
Supporting evidence roles
Content to relocate/omit
Close analogue set
Broad-corpus tendencies
Patterns adopted/adapted/rejected
Final manuscript-surface leakage findings
Punctuation/copy-editing findings
```

The actual prose and figures remain the deliverable. The research machinery exists to make those decisions better, not to bury the author under analytics.

## Research boundary

The corpus is continuously extendable. New papers should be added by a balanced matrix of archetype, field, article type, evidence modality and publication model, with explicit counterexamples retained.

The most important rule remains:

> Learn the **scientific function and reader problem** behind successful writing and figures; do not copy the visible surface.