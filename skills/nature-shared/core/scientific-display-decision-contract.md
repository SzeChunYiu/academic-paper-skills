# Scientific display decision contract

> Canonical evidence-to-representation contract for plots, figures, tables,
> image plates, diagrams, and mixed displays. Use it after deciding that a
> display is needed and before rendering or treating the display as support for
> manuscript prose.

Last reviewed: 2026-08-28.

## Principle

A display is an evidence transformation, not decoration. Resolve it in this
order:

```text
reader question
-> scientific object / estimand
-> evidence and dependence structure
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

This contract complements `figure-evidence-planning.md`:

- figure planning decides whether a display is needed and its evidence role;
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
- Resolver/evaluator: `../scripts/resolve_scientific_display.py`

The first evidence registry contains 39 reconciled sources: 20 read in full,
18 read at abstract level, and one official accessibility standard read
directly. Search queries, screening counts, inclusion/exclusion criteria,
stopping rule, source-specific support, transfer limits, and update triggers are
recorded rather than hidden behind a bibliography.

The maintained catalog is intentionally incomplete. If no adapter matches, the
resolver returns an unresolved research requirement rather than forcing a
generic plot. Domain-specific adapters may be added only with evidence,
provenance, and behavioral fixtures.

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

The first maintained adapters cover paired change, distribution inspection,
classification decisions, high-dimensional embeddings, workflow semantics, and
exact-value lookup. They are starting points, not an exhaustive chart taxonomy.

## Perceptual and statistical checks

Before rendering, resolve:

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
- whether the main/support placement matches claim importance rather than visual
  attractiveness.

### High-risk inference boundaries

- A visual association does not establish causation.
- An embedding alone does not establish quantitative separation, discrete
  natural clusters, mechanism, or causality.
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

The reader question, scientific object, claim link, candidate family, and
unresolved evidence needs may remain provisional. Unknowns must be explicit.

### Draft/review

Data/analysis/render lineage, denominator, unit, uncertainty, transformations,
group coverage, and inference boundaries must be checkable. Review should attack
the contract, not merely aesthetics.

### Final/production

No display-contract blocker may remain. Alt text is required; color cannot be
the only information channel; captions and source data must match the bound
snapshot; every display must be inspected at final physical size and in the
assembled manuscript.

### Post-publication

Preserve the released contract and artifact hashes. A correction adds a new
version and relation to the old object; it does not erase the prior state.

## Blocking failure classes and valid repair

| Failure | Minimum valid repair |
|---|---|
| hidden paired/repeated structure | expose within-unit structure or narrow/change the estimand |
| denominator/unit drift | reconcile against source data and version affected claims/captions |
| snapshot/receipt mismatch | re-run or re-render from the declared immutable upstream object |
| undefined uncertainty | name kind, level/method, and inferential unit, or remove unsupported bars |
| undisclosed transformation/scale | disclose and justify it or re-render without it |
| omitted adverse/null/group evidence | restore it or provide a traceable, justified companion placement |
| embedding/workflow overclaim | add independent evidence or narrow the claim to what the representation supports |
| color-only or missing alternative text | add redundant encoding and semantic text, then visually re-check |

Repairs must never invent data, analyses, sample sizes, groups, uncertainty, or
mechanisms merely to make the contract pass.

## Exit condition

A display is closed only when:

1. the schema-valid contract is bound to current artifacts;
2. the resolver has either matched an evidence-informed adapter or recorded a
   completed domain-specific representation rationale;
3. all semantic/provenance/accessibility blockers are closed;
4. visual inspection at final size is complete;
5. the manuscript claim stays within the declared inference boundary;
6. exact venue packaging is independently resolved for the current stage.

## Research basis

- Cleveland & McGill (1984), graphical perception experiments and perceptual
  tasks: <https://doi.org/10.1080/01621459.1984.10478080>
- Weissgerber et al. (2015), raw-data and paired/distribution visibility:
  <https://doi.org/10.1371/journal.pbio.1002128>
- Rougier, Droettboom & Bourne (2014), audience/message-led figure design:
  <https://doi.org/10.1371/journal.pcbi.1003833>
- Nature Methods, *Points of View, anew*:
  <https://www.nature.com/articles/s41592-026-03143-5>
- W3C WCAG 2.2, use of color:
  <https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html>

These sources support maintained starting points. Plot-specific statistical and
domain decisions still require the actual study design, evidence, reporting
standard, and current specialist guidance.
