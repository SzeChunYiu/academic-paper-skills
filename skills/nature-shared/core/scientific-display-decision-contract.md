# Scientific display decision contract

> Canonical evidence-to-representation contract for plots, figures, tables,
> image plates, diagrams, and mixed displays. Use it after deciding that a
> display is needed and before rendering or treating the display as support for
> manuscript prose.

Last reviewed: 2026-08-29.

## Principle

A display is an evidence transformation, not decoration. Resolve it in this
order:

```text
reader question
-> scientific object / estimand
-> evidence and dependence structure
-> text vs table vs figure vs mixed display
-> candidate representations
-> perceptual and inferential risks
-> allowed and prohibited inferences
-> data/analysis/render/source-data lineage
-> caption and accessibility
-> stage-specific exit tests
```

There is **no universal best chart**. A maintained adapter returns a candidate
set and obligations. The actual design, estimand, scientific unit, data,
uncertainty, alternative explanation, audience task, and medium determine the
final choice. Frequency in published papers is descriptive evidence, not a
quality rule.

## Authority and boundaries

This contract complements `figure-evidence-planning.md` and
`visual-evidence-atlas.md`:

- figure planning decides whether a display is needed and its evidence role;
- the visual evidence atlas decides whether the reader task is best served by
  text, a table, a figure, or a mixed display and provides researched plot/table
  families and failure modes;
- this contract binds one display to the scientific object, representation,
  inference boundary, and immutable provenance chain;
- `nature-figure` renders and visually inspects it;
- exact venue guidance controls packaging only after scientific integrity;
- the project-state object records lifecycle status.

A passing automated check does **not** certify the truth of the data, validity
of the analysis, truth of the claim, visual legibility at final size, or journal
acceptance.

## Machine-readable assets

- Schema: `../display-contracts/scientific-display-contract.schema.json`
- Maintained adapters: `../display-contracts/maintained-adapters.json`
- Evidence registry: `../display-contracts/display-evidence-registry.json`
- Research synthesis: `../research/scientific-display-evidence-ledger-2026-08.md`
- Practical visual atlas: `visual-evidence-atlas.md`
- Targeted visual-evidence research tranche:
  `../research/visual-evidence-atlas-research-2026-08-29.md`
- Resolver/evaluator: `../scripts/resolve_scientific_display.py`

The first evidence registry contains 39 reconciled sources: 20 read in full,
18 read at abstract level, and one official accessibility standard read
directly. Search queries, screening counts, inclusion/exclusion criteria,
stopping rule, source-specific support, transfer limits, and update triggers are
recorded rather than hidden behind a bibliography.

The 2026-08-29 visual-evidence tranche adds targeted research on table-vs-figure
selection, effect/forest/funnel displays, longitudinal data, prediction utility,
heatmaps/clustering, compositional data, geospatial maps, and qualitative
displays. These additions expand the human/agent decision atlas immediately;
they become hard machine adapters only after source-registry reconciliation and
behavioral fixtures.

The maintained catalog is intentionally incomplete. If no adapter matches, the
resolver returns an unresolved research requirement rather than forcing a
generic plot. Domain-specific adapters may be added only with evidence,
provenance, and behavioral fixtures.

## Figure vs table vs text gate

Before selecting a chart family, state what the reader must do.

### Text

Use when one or two values or observations are sufficient and a display adds no
new pattern, structure, or decision value.

### Table

Use when exact lookup, many related estimates, denominators, units, reference
levels, multiple outcomes, model variants, or precise cross-comparison is the
primary task.

A table must preserve exact values, units, denominators, missingness, and
uncertainty where relevant. It should not be a rasterized spreadsheet.

### Figure

Use when shape, distribution, trajectory, association, uncertainty,
heterogeneity, spatial structure, mechanism, flow, or another visual pattern is
the scientific object.

### Mixed display

Use when a figure exposes the pattern but exact values or metadata must remain
recoverable—for example a forest plot with aligned study/effect values, a
representative image plus quantitative evidence, or a prediction curve plus a
compact metric table.

### Non-duplication rule

Do not repeat the same evidence in text, table, and figure without a distinct
reader function.

Use:

```text
figure = pattern
 table = exactness/detail
  text = interpretation + the most important observations
```

Current ICMJE guidance supports this separation: tables/figures should be
restricted to what is needed to explain the argument and assess the evidence,
and the text should not repeat all displayed data.

For the researched task-by-task rules, load `visual-evidence-atlas.md`.

## Required object model

Each display records:

| Object | Required decision |
|---|---|
| identity/stage | stable contract ID, display ID, display kind, lifecycle stage |
| reader task | the question a reader should answer by inspecting the display |
| scientific object | estimand/target quantity, statistical unit, dependence/data structure, population denominator |
| claim links | claim IDs/types plus allowed and prohibited inferences |
| evidence links | immutable data snapshot, analysis receipt, render receipt, and source-data object |
| representation | family, scientific rationale, variable-to-channel encodings, transformations, uncertainty, scales, included/omitted groups |
| caption | denominator, unit, uncertainty definition, transformation disclosures |
| accessibility | semantic alt text/long description and non-color-only encoding |
| placement | main, support, repository, or omitted, with a scientific reason |
| risks | known ways the display may invite overinterpretation |

The minimum provenance chain is:

```text
data snapshot SHA-256
-> analysis receipt bound to that snapshot
-> render receipt bound to that analysis
-> source-data object bound to the same snapshot
```

Changing any upstream object creates a new version. Do not silently keep an old
caption or plot after the denominator, group set, transformation, or analysis
changes.

## Representation resolution

Call the resolver with the reader task, data structure, and claim type. Its
output contains:

- matched adapter IDs;
- candidate representation families;
- disallowed families for the declared task/structure;
- obligations and inference boundaries;
- supporting source references;
- unresolved research needs.

Example:

```bash
python skills/nature-shared/scripts/resolve_scientific_display.py \
  path/to/display-contract.json --pretty
```

The maintained adapters cover paired change, distribution inspection,
uncertainty, classification decisions, time-to-event data, high-dimensional
embeddings, workflow/causal semantics, scientific color, image evidence,
accessibility, and exact-value lookup. They are starting points, not an
exhaustive chart taxonomy.

When a scientifically relevant family exists in `visual-evidence-atlas.md` but
not in the machine adapter catalog, record the manual representation rationale
and research basis rather than pretending the resolver certified it.

## Perceptual and statistical checks

Before rendering, resolve:

- whether text, table, figure, or mixed display best fits the reader task;
- position/length/area/color channel suitability for the reader task;
- axis type, domain, truncation, zero baseline relevance, and transformations;
- binning, smoothing, interpolation, normalization, aggregation, ordering, and
  parameter choices;
- overplotting and hidden density;
- independence, pairing, repeated measures, nesting, clustering, or censoring;
- the exact meaning and unit of every interval/error bar;
- observed versus fitted, simulated, imputed, or derived quantities;
- denominators, missingness, exclusions, attrition, and omitted groups;
- whether adverse, null, harmful, failure-boundary, or contradictory evidence is
  visible or traceably allocated elsewhere;
- whether a table better serves exact lookup than a plot;
- whether a figure needs a table/source-data companion for exact primary results;
- whether the main/support placement matches claim importance rather than visual
  attractiveness.

### High-risk inference boundaries

- A visual association does not establish causation.
- An embedding alone does not establish quantitative separation, discrete
  natural clusters, mechanism, or causality.
- A clustered heatmap/dendrogram alone does not establish stable or natural
  clusters; normalization, distance, linkage, ordering, and stability matter.
- A workflow diagram records operations/sequence; it is not a causal DAG or
  mechanism model.
- A mechanism diagram must distinguish observed, inferred, assumed, and
  speculative relations.
- A representative image does not establish a population-level quantitative
  claim without traceable sampling and quantification.
- An ablation establishes dependence under the tested intervention; it does not
  automatically establish mechanism.
- AUC alone does not establish calibration, threshold utility, or deployment
  value.
- Funnel-plot asymmetry alone does not establish publication bias.
- A relative/compositional change does not establish an absolute abundance
  change.
- A raw-count choropleth does not establish geographic risk when denominators
  differ.
- `P > 0.05` does not establish equivalence or absence of effect.

## Diagram semantic types

Declare one primary semantic type before choosing the drawing backend:

| Type | What edges/nodes may mean | What it cannot silently claim |
|---|---|---|
| workflow | operation and sequence | causal identification or mechanism |
| causal DAG | explicit assumed causal relations | empirical truth of every edge |
| mechanism model | bounded observed/inferred interactions | established mechanism without discriminating evidence |
| architecture | components, boundaries, interfaces, flow | biological/causal mechanism |
| state diagram | states and allowed transitions | frequencies or causal effects unless encoded |
| timeline | temporal order | causation from temporal order |
| evidence graph | claims, supports, contradictions, unresolved links | quantitative effect strength without defined encoding |

## Stage gates

### Planning

The reader question, scientific object, claim link, display-medium choice,
candidate family, and unresolved evidence needs may remain provisional. Unknowns
must be explicit.

### Draft/review

Data/analysis/render lineage, denominator, unit, uncertainty, transformations,
group coverage, exact-value companion needs, and inference boundaries must be
checkable. Review should attack the contract, not merely aesthetics.

### Final/production

No display-contract blocker may remain. Alt text is required; color cannot be
the only information channel; captions and source data must match the bound
snapshot; exact primary values must remain recoverable when required by the
scientific/reporting contract; every display must be inspected at final physical
size and in the assembled manuscript.

### Post-publication

Preserve the released contract and artifact hashes. A correction adds a new
version and relation to the old object; it does not erase the prior state.

## Blocking failure classes and valid repair

| Failure | Minimum valid repair |
|---|---|
| wrong display medium for reader task | move to text/table/figure/mixed representation that exposes the needed pattern or exactness |
| hidden paired/repeated structure | expose within-unit structure or narrow/change the estimand |
| denominator/unit drift | reconcile against source data and version affected claims/captions |
| snapshot/receipt mismatch | re-run or re-render from the declared immutable upstream object |
| undefined uncertainty | name kind, level/method, and inferential unit, or remove unsupported bars |
| undisclosed transformation/scale | disclose and justify it or re-render without it |
| omitted adverse/null/group evidence | restore it or provide a traceable, justified companion placement |
| embedding/workflow/heatmap overclaim | add independent evidence or narrow the claim to what the representation supports |
| classifier metric overclaim | add calibration/threshold/utility evidence required by the claim or narrow the claim |
| compositional absolute-change overclaim | add absolute evidence or restate the claim as relative/compositional |
| map denominator/uncertainty omission | restore denominator/rate/uncertainty semantics or change the spatial display |
| color-only or missing alternative text | add redundant encoding and semantic text, then visually re-check |

Repairs must never invent data, analyses, sample sizes, groups, uncertainty, or
mechanisms merely to make the contract pass.

## Exit condition

A display is closed only when:

1. the schema-valid contract is bound to current artifacts;
2. the text/table/figure/mixed choice is justified by the reader task;
3. the resolver has either matched an evidence-informed adapter or recorded a
   completed domain-specific representation rationale using the visual atlas and
   specialist research;
4. all semantic/provenance/accessibility blockers are closed;
5. exact-value/table/source-data companions required by the scientific or
   reporting contract exist;
6. visual inspection at final size is complete;
7. the manuscript claim stays within the declared inference boundary;
8. exact venue packaging is independently resolved for the current stage.

## Research basis

- Cleveland & McGill (1984), graphical perception experiments and perceptual
  tasks: <https://doi.org/10.1080/01621459.1984.10478080>
- Weissgerber et al. (2015), raw-data and paired/distribution visibility:
  <https://doi.org/10.1371/journal.pbio.1002128>
- Rougier, Droettboom & Bourne (2014), audience/message-led figure design:
  <https://doi.org/10.1371/journal.pcbi.1003833>
- Nature Methods, *Points of View, anew*:
  <https://www.nature.com/articles/s41592-026-03143-5>
- ICMJE current manuscript-preparation recommendations:
  <https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html>
- JAMA Network Open current Tables and Figures instructions:
  <https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors>
- Cochrane Handbook, forest/funnel and synthesis display guidance:
  <https://training.cochrane.org/handbook/current/chapter-iii>
  <https://training.cochrane.org/handbook/current/chapter-13>
- W3C WCAG 2.2, use of color:
  <https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html>

These sources support maintained starting points. Plot-specific statistical and
domain decisions still require the actual study design, evidence, reporting
standard, and current specialist guidance. Load `visual-evidence-atlas.md` and
its dated research ledger for the expanded task-by-task visual rules.