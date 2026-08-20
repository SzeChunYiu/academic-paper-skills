# Analogue figure calibration

Use this reference when a figure set is being created/rebuilt for a known research community, or when the user asks what figures, data, panels, or plot types comparable papers use.

## Contents

- [Principle](#principle)
- [Select the analogue set](#select-the-analogue-set)
- [Build a figure-evidence inventory](#build-a-figure-evidence-inventory)
- [Learn figure roles before chart types](#learn-figure-roles-before-chart-types)
- [Choose what data must be visible](#choose-what-data-must-be-visible)
- [Choose how to plot it](#choose-how-to-plot-it)
- [Build our figure sequence](#build-our-figure-sequence)
- [Main text versus supplementary](#main-text-versus-supplementary)
- [Visual identity boundary](#visual-identity-boundary)
- [Anti-copying and anti-cargo-cult rules](#anti-copying-and-anti-cargo-cult-rules)
- [Output contract](#output-contract)

## Principle

A comparable paper is useful because it reveals **which visual evidence readers in this research class need to evaluate a claim**. It is not a design template.

Always load `../../nature-shared/core/analogue-paper-calibration.md` first. Then use this file to deepen the visual/evidence analysis.

The workflow is:

`claim/evidence needs -> analogue figure roles -> user's actual data -> plot choice -> panel sequence -> target-journal mechanics`

Never reverse it into:

`paper used heatmap -> we need heatmap`.

## Select the analogue set

For a normal figure redesign, inspect a few closest papers rather than a broad random journal sample. Prefer matching:

- contribution type;
- study design / experiment family;
- data modality;
- evaluation structure;
- target venue/article type;
- intended audience.

A paper with the same evidence architecture in a neighboring journal can be more useful than an unrelated paper in the exact target.

## Build a figure-evidence inventory

For every main figure in each analogue, record:

| Field | What to record |
|---|---|
| Figure role | orientation / main effect / mechanism / validation / generalization / failure boundary / resource / synthesis |
| Reader question | what uncertainty does this figure resolve? |
| Claim | what narrow conclusion does the figure license? |
| Data unit | participants / samples / cells / tasks / seeds / timepoints / cases / sources / simulations / etc. |
| Evidence modality | scatter / distribution / trajectory / image / spectrum / heatmap / table / schematic / network / map / diagnostic |
| Comparator | control / baseline / reference / null / subgroup / previous method |
| Raw-data visibility | individual observations / aggregates / both / not applicable |
| Uncertainty | CI / SD / SE / posterior / replicate spread / none / not applicable |
| Statistical cue | test/effect size/model/interval where relevant |
| Panel logic | why A -> B -> C? |
| Main vs SI | which supporting evidence was moved out of the main figure? |
| Caption role | decoding only / interpretation / stats/protocol detail |

Do not judge a figure only by appearance. Ask what scientific work it performs.

## Learn figure roles before chart types

Across the analogue set, look for recurrent **roles** such as:

1. **orientation / system definition** — what is being studied and how;
2. **primary evidence** — the central effect/finding;
3. **mechanism / explanation** — why the effect occurs;
4. **validation / external replication** — whether it persists outside the initial setting;
5. **generalization / scaling** — breadth across data/tasks/populations/conditions;
6. **robustness / sensitivity** — dependence on analysis choices or perturbations;
7. **failure boundary / negative case** — where the claim stops;
8. **resource utility** — what the dataset/tool enables.

The useful transferable pattern is often the **role sequence**, not the visual encoding.

## Choose what data must be visible

For each planned claim ask:

- What is the actual statistical/experimental unit?
- What variation matters to interpretation?
- Is the estimand paired, marginal, longitudinal, hierarchical, compositional, spatial, or relational?
- What alternative explanation must the reader be able to inspect?
- Would an aggregate hide distribution, heterogeneity, outliers, or pairing?
- Does a representative image need quantitative corroboration?
- Does a performance mean require run/task/site uncertainty?

Examples:

- small-sample continuous data often benefit from individual observations or distribution displays rather than bars of means alone;
- paired data should expose within-pair changes when the paired contrast is central;
- microscopy/image claims commonly need both representative images and quantitative summaries when the conclusion is not purely illustrative;
- generalization claims need evidence across the stated regimes, not a decorative collection of examples;
- model superiority claims should show fair common baselines/scales and variability when stochasticity/task variation matters.

## Choose how to plot it

Select plot form by **reader task + data structure**.

### Distribution / group difference

Prefer forms that expose the relevant distribution and sample unit: dot/strip/swarm, box/violin with points where appropriate, interval/estimation plots, or other field-appropriate distribution displays.

### Paired / repeated data

Use connected pairs, paired differences, slope graphs, repeated-measure trajectories, or model-based interval displays when those reveal the estimand.

### Ordered progression / time

Use line/trajectory displays when order is meaningful. Show uncertainty/replicates as appropriate rather than hiding them behind a single smooth line.

### Relationship / association

Use scatter/hexbin/density depending scale, with an explicitly justified fitted relation if needed. Do not imply causality from the visual alone.

### Composition

Use part-to-whole encodings only when parts form a meaningful total. Avoid pie/donut forms when precise comparison among many categories matters.

### Many conditions / matrix structure

Heatmaps are useful when the matrix pattern itself matters. If the key question is a small number of pairwise differences, a heatmap may hide the important estimand.

### Ranking / method comparison

Use common axes and clear uncertainty. Avoid ranking methods by tiny visual differences when uncertainty overlaps materially.

### Images / spatial fields

Keep scale bars, consistent processing, crop integrity, representative-selection rationale, and quantitative linkage visible.

### Diagnostic / calibration claims

Use a diagnostic plot that directly shows calibration/error/failure behavior rather than reporting only a headline aggregate metric.

## Build our figure sequence

After studying analogues, create an **our-figure plan** independent of any one paper.

For each planned figure:

```text
Figure N
Decision-relevant question
Claim supported
Data required
Panel roles
Preferred representation(s)
Why this representation fits the data
Key uncertainty / comparator
Main-text sentence that calls the figure
What moves to SI
Analogue pattern used (function only)
Analogue pattern rejected and why
```

The sequence should reduce reader/reviewer uncertainty in the same way the Results narrative does.

## Main text versus supplementary

Use analogues as priors only. Final placement follows scientific function and target requirements.

Main figures should contain the shortest sufficient visual evidence chain for the headline claims. Supporting parameter sweeps, secondary baselines, provenance detail, repeated robustness checks, and non-central edge cases usually belong in SI unless they materially change the interpretation.

Load `../../nature-shared/core/main-text-discipline.md` for the final allocation decision.

## Visual identity boundary

Preserve a coherent **project visual identity** rather than mimicking analogue-paper aesthetics.

Keep stable across the manuscript where appropriate:

- typography hierarchy;
- panel-label logic;
- line/marker conventions;
- semantic color meaning;
- spacing/grid rhythm;
- annotation style;
- terminology and variable notation.

Adapt these only when exact target rules or accessibility require it.

Analogue papers can influence **which comparisons are made visible** and **how much information a panel carries**. They should not determine distinctive colors, layout motifs, or decorative style.

## Anti-copying and anti-cargo-cult rules

Never:

- reproduce a distinctive multi-panel composition just because it looks successful;
- inherit another paper's normalization, smoothing, axis limits, exclusions, statistical test, or sample aggregation without justification;
- use a chart because it is popular in the target journal;
- infer journal production dimensions from a published PDF;
- hide raw variability merely because analogue papers did;
- add panels that do not close a claim/evidence dependency;
- force every paper into a `schematic -> main result -> mechanism -> generalization` sequence when the evidence does not support it.

## Output contract

Return a compact visual calibration brief:

```text
Analogue visual evidence patterns
- recurrent figure roles
- recurrent evidence/data displays
- legitimate alternatives

Our data-to-plot decisions
- claim/question -> data -> plot -> uncertainty/comparator

Our figure sequence
- Fig. 1 ...
- Fig. 2 ...

Main vs SI allocation
- ...

Project visual identity to preserve
- ...

Patterns explicitly rejected
- ...
```

The final figures must remain scientifically defensible without reference to the analogue papers.