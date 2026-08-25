# Target-corpus calibration

Use this protocol when the user asks to learn how a field/venue writes, what evidence/figures comparable papers show, why a manuscript does not resemble the relevant literature, or to build/update a maintained paper corpus.

This is a **rhetorical and evidence-architecture learning** workflow, not a sentence-copying or chart-copying workflow.

## Contents

- [Core separation](#core-separation)
- [Stratify before counting](#stratify-before-counting)
- [Corpus design](#corpus-design)
- [Pass A — scalable descriptive profiling](#pass-a--scalable-descriptive-profiling)
- [Pass B — semantic rhetorical/evidence reading](#pass-b--semantic-rhetoricalevidence-reading)
- [Pass C — close analogue reading](#pass-c--close-analogue-reading)
- [Whole-paper logic reduction](#whole-paper-logic-reduction)
- [Study transitions between analyses](#study-transitions-between-analyses)
- [Study claim calibration](#study-claim-calibration)
- [Separate invariant from variable](#separate-invariant-from-variable)
- [Profile output](#profile-output)
- [How to use the profile](#how-to-use-the-profile)
- [Anti-copying and anti-overfitting](#anti-copying-and-anti-overfitting)
- [Update protocol](#update-protocol)

## Core separation

Use three scales for different purposes:

1. **Broad stratified corpus** — dozens/hundreds of papers for descriptive tendencies.
2. **Quick target profile** — **8–15 comparable recent papers** when a fast venue/article-type profile is needed.
3. **Close analogues** — 3–6 nearest neighbors for deep claim/evidence/explanation/figure reasoning.

For a maintained repository profile, aim for **30–100 papers** and stratify them before generalizing. For research-grade studies, use larger reproducible samples with explicit inclusion/exclusion.

Frequency is not quality. Published frequency is not an acceptance rule.

## Stratify before counting

The most important improvement over a journal-only corpus is **paper-archetype stratification**.

Before aggregating, record:

- exact journal/venue;
- article/content type;
- year;
- discipline/subfield;
- study design;
- dominant paper archetype from `../nature-shared/core/paper-archetype-atlas.md`;
- secondary archetype(s);
- evidence modality;
- target reader/publication model.

Do not average a randomized trial, a benchmark, a qualitative interview study and a resource paper into one `journal style` merely because they share a venue/publisher.

## Corpus design

Prefer matching, in order:

1. scientific/epistemic archetype and contribution promise;
2. study design/evidence type;
3. article/content type;
4. discipline/subfield/audience;
5. exact journal/venue when useful;
6. recent publication period.

Comparability outranks prestige.

Retain counterexamples deliberately. A rigorous outlier can reveal that a supposed `rule` is actually an archetype, field, author or article-type preference.

## Pass A — scalable descriptive profiling

When dozens or hundreds of papers have been extracted to `.md`, `.markdown`, or `.txt`, use two complementary tools.

### A1. Text/rhetoric surface inventory

```bash
python scripts/corpus_structure_stats.py CORPUS_DIR --pretty --output corpus-structure.json
```

Use for descriptive signals such as:

- section/heading presence/order;
- paragraph/sentence length distributions;
- figure/table call density;
- selected contrast/consequence/example markers;
- selected hedge/booster/self-reference/contribution signals.

These are not writing-quality scores and do not identify rhetorical moves reliably.

### A2. Figure/caption/evidence-role inventory

```bash
python scripts/corpus_figure_inventory.py CORPUS_DIR \
  --json corpus-figures.json \
  --csv corpus-displays.csv
```

Use for:

- figure/table caption counts;
- in-text display calls;
- section context of captions;
- caption text for later semantic annotation;
- transparent **candidate** evidence roles such as orientation/workflow, primary finding, mechanism, validation, OOD/generalization, robustness, failure/limitation, heterogeneity, calibration/diagnostic, resource coverage, theory/model and qualitative synthesis.

The role labels are keyword heuristics for triage. They are **not semantic ground truth, writing-quality scores, acceptance predictors, or instructions to copy frequent plot types**.

### A3. Stratified descriptive summaries

Aggregate only within meaningful strata, for example:

`computational benchmark × biology × 2024–2026`

rather than:

`all Nature Portfolio papers`.

Useful descriptive measures include:

- median/quantiles of main-figure count;
- table usage;
- figure-call location;
- caption length;
- candidate figure roles;
- location of validation/failure/heterogeneity evidence;
- main-versus-support patterns when support text is available;
- section/move/sentence statistics.

Do not turn medians into mandatory budgets.

## Pass B — semantic rhetorical/evidence reading

Surface statistics cannot explain **why** a paper works.

Read complete papers or complete rhetorical/evidence units to recover:

- question/tension and bounded contribution;
- why evidence block B becomes necessary after A;
- paragraph nucleus and satellites;
- observation versus interpretation;
- alternatives/counterevidence;
- hidden assumptions;
- explanation depth;
- claim calibration;
- why a figure is necessary;
- what reader question each figure resolves;
- what is placed in main versus support;
- why a structural outlier is sensible for its study design.

When resources are limited, prioritize semantic reading over collecting more superficial counts.

## Pass C — close analogue reading

For 3–6 nearest-neighbor papers, annotate more deeply:

### Paper-level

- dominant/secondary archetype;
- central question/tension;
- central answer/contribution;
- evidence sequence;
- decision-changing boundaries/limitations;
- main-display sequence and roles;
- support-material roles.

### Section-level

For each major section:

- reader question;
- rhetorical moves/order;
- opening/handoff strategy;
- location of interpretation/limitations;
- explanation-depth hotspots.

### Paragraph-level

- nucleus;
- evidence/explanation/comparison/qualification/counterargument/implication/bridge;
- figure/table integration;
- local reader handoff.

### Sentence-level

Sample by rhetorical function, not randomly:

- sentence function;
- dependency and given/new progression;
- identity/reference chains;
- active/passive and agency;
- tense/aspect;
- hedge/booster strength;
- clausal versus phrasal realization;
- citation integration.

### Figure-level

For each main/support display:

- figure role;
- reader question;
- claim licensed;
- statistical/scientific unit;
- estimand/quantity;
- comparator/control;
- raw-data visibility;
- uncertainty;
- alternative explanation exposed;
- plot/image/table/schematic family;
- why this figure follows the previous evidence block;
- why it is main/support.

Do **not** retain reusable full-sentence templates or distinctive figure layouts from copyrighted papers. Abstract the function.

## Whole-paper logic reduction

For every close paper, reduce the manuscript to:

```text
question/tension
-> response/contribution
-> evidence progression
-> interpretation
-> boundary
-> meaning
```

Then separately reduce the main visual argument:

```text
reader uncertainty 1 -> figure/evidence role 1
-> next uncertainty -> figure/evidence role 2
-> ... -> bounded conclusion
```

This lets us compare papers with different visible structures without assuming one skeleton.

## Study transitions between analyses

The most reusable lesson is often the dependency, not the wording or chart.

Examples:

- baseline failure -> limitation analysis;
- discovery -> mechanism question;
- mechanism claim -> discriminating perturbation/control;
- initial benchmark -> OOD validation;
- inconsistent effect -> heterogeneity analysis;
- probability claim -> calibration diagnostic;
- theorem -> corollary/numerical illustration;
- qualitative theme -> contrasting/negative case;
- resource construction -> quality/coverage validation.

Record `evidence block A -> reason for block B`.

## Study claim calibration

For each major claim record:

- claim type;
- evidence type;
- uncertainty/boundary;
- alternative interpretation;
- hedge/booster;
- whether causal/generalization language is warranted;
- figure/table/source supporting it.

This is more useful than counting `clearly`, `significantly` or `therefore` in isolation.

## Separate invariant from variable

Classify observed patterns as:

- **scientific/evidence dependency** — justified by the claim/design;
- **archetype tendency** — common for this epistemic paper class;
- **discipline tendency**;
- **journal/content-type tendency**;
- **house/submission rule** — must be verified officially;
- **author-level variation** — do not generalize.

This classification is required before promoting an observed pattern into a writing/figure rule.

## Profile output

Produce a temporary profile containing:

### Corpus definition

- target/field/archetype;
- date window;
- number of papers;
- inclusion logic;
- important coverage gaps.

### Whole-paper architecture

- common argument spines;
- evidence sequences;
- legitimate alternative architectures.

### Section/paragraph/sentence tendencies

- move maps;
- paragraph nuclei/satellites;
- sentence information structure/stance;
- meaningful variants.

### Figure/evidence architecture

- main-figure role sequences;
- recurrent plot families by reader task;
- uncertainty/comparator patterns;
- support allocation;
- legitimate `no-figure` or table-heavy variants;
- failure/limitation visibility.

### Transferable rules

Only patterns that make scientific/rhetorical sense and survive counterexamples.

### Local tendencies

Useful defaults only for this stratum.

### Unresolved variation

Conflicting patterns that should not become rules.

### Counterexamples

Papers that violate the common pattern and why.

## How to use the profile

Apply in this order:

1. scientific accuracy/evidence boundary;
2. exact reporting/reproducibility obligations;
3. paper-archetype evidence logic;
4. rhetorical engine;
5. intended-reader explanation need;
6. close-analogue reasoning;
7. broader corpus tendencies;
8. exact journal house/submission rules.

If corpus practice conflicts with evidence integrity, evidence integrity wins. If it conflicts with current official submission mechanics, the official requirement wins.

## Anti-copying and anti-overfitting

Never:

- copy distinctive sentences/phrases;
- build reusable phrase banks from copyrighted prose;
- copy a distinctive multi-panel composition;
- infer effectiveness from prestige/citation count;
- infer acceptance probability from figure count/type;
- mix paper archetypes and report the average as one style;
- convert caption keyword heuristics into semantic truth;
- treat corpus frequency as an exact submission rule;
- hide limitations because published main texts appear compressed;
- force a plot because it is common in the stratum;
- force a figure when a qualitative/theory paper does not need one.

Learn **moves, dependencies, explanation depth, evidence roles, information structure and claim calibration**, not surface imitation.

For backward-compatible writing-contract language: Learn **moves, relations, sequencing, information structure, and claim calibration**, not wording.

## Update protocol

For maintained corpora:

- record sampling date and paper identifiers;
- retain selection/exclusion criteria and extraction provenance;
- add papers incrementally rather than silently replacing the corpus;
- compare old/new distributions before changing a rule;
- keep previous profiles when venue practice shifts;
- deliberately preserve counterexamples;
- promote a local rule into cross-disciplinary core only after validation outside the source corpus;
- add a regression test whenever the profile changes a hard drafting/figure contract.

The local `nat-comms-2025-corpus.md` remains one useful stratum. It is not a universal academic-writing/legend/figure template.