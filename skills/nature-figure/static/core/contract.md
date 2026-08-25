# Figure contract before plotting

A publication-quality scientific figure is a visual argument, not an isolated pretty plot. Every figure starts from a **claim, reader question, evidence/estimand, data structure, and uncertainty/alternative-explanation check** before code or aesthetics. For serious manuscript figure design/redesign, first resolve the paper's scientific archetype and then study close analogue papers when useful.

When the user asks **what figures or plots should be made**, load `../../../nature-shared/core/figure-evidence-planning.md` before choosing a backend or chart type. When deciding whether a candidate figure belongs in main text/support or should be omitted, also load `../../../nature-shared/core/manuscript-content-selection.md`. When the paper class matters, load `../../../nature-shared/core/paper-archetype-atlas.md` so a trial, mechanism paper, benchmark, resource paper, theory paper, qualitative study, review, and hybrid paper are not forced into one visual sequence.

## Backend selection uses a saved preference

For plotting tasks, first honor an explicit Python/R choice in the current request or a clearly language-specific input file/workflow. Save that backend as the user's default with `scripts/nature_figure_backend.py set python` or `scripts/nature_figure_backend.py set r`.

If the current request does not specify a backend, check the saved preference with `scripts/nature_figure_backend.py get`. If it returns `python` or `r`, use that backend without asking again.

If no saved preference exists, ask one concise question: **Python or R? I will remember this as your default.** Then stop and wait for the user's answer. Do not generate mock data, write scripts, create figures, or choose Python/R by default before this first preference is established. After the user answers, save it and proceed.

Only recommend a backend when the user explicitly asks you to choose or recommend one. In that case, use `references/backend-selection.md`, state the reason, save the selected backend, and then proceed with the recommended backend.

**Planning-only exception:** deciding which figures/plots the paper needs does not require selecting Python/R. Complete scientific figure planning first; choose a backend only when rendering/code is requested.

## The selected backend is exclusive

Once Python or R is selected, every plotting script, preview image, SVG/PDF/TIFF/PNG export, QA render, and visual workaround must be produced by that same backend. Do not use Python to draw a preview for an R figure, and do not use R to draw a preview for a Python figure, even if the selected runtime or packages are missing locally. The non-selected language may only be used for non-visual file inspection or data conversion when it does not open a graphics device, import plotting libraries, create image/vector files, or change the final visual appearance.

## Missing runtime/package rule

After the backend is selected, check the selected runtime early (`Rscript`/R for R; Python and required plotting packages for Python). If the selected runtime or required packages are unavailable, stop before rendering and report the exact blocker. You may provide a selected-backend script and installation commands, or ask permission to install dependencies, but you must not fall back to the other language to make a substitute figure.

## Data-integrity gate

Use all user-provided observations and requested variables unless an exclusion has a scientific or statistical justification or the user explicitly requests a subset. Never reduce data merely to make a plot easier or faster to render. For large point clouds, prefer rasterized marks, hexbin/density representations, aggregation with a stated rule, or another backend-native rendering strategy.

If any row, column, replicate, image, or category is excluded, record the before/after counts, the exact rule, and the reason in the QA notes. Preserve the unmodified source data and never silently select convenient columns to satisfy a template.

Plan figures by scientific claims, not by source tables. Do not turn each table into a separate figure when several tables answer the same question. If an effect is defined within matched datasets, subjects, seeds, or tasks, inspect and visualize paired differences rather than relying only on overlapping marginal distributions; large between-unit heterogeneity can hide a strong paired effect.

## Paper-archetype calibration gate

Before planning a serious manuscript figure sequence, use `../../../nature-shared/core/paper-archetype-atlas.md` to classify the dominant epistemic job.

Examples:

- **mechanism/discovery** — phenomenon, dependency/perturbation, mechanism discrimination, orthogonal/model support, boundary;
- **randomized intervention** — participant/design orientation, primary outcome/effect with uncertainty, safety/secondary evidence;
- **observational** — population/estimand, adjusted association, identification/confounding, heterogeneity/sensitivity, generalizability;
- **computational/ML** — evaluation regime, fair comparison, heterogeneity, component evidence, OOD/generalization, calibration/failure;
- **method/tool** — principle/capability, technical validation, benchmark, operating regime, real application, limitation;
- **resource/dataset** — coverage, construction/processing, quality/validation, reuse/access;
- **theory/proof** — figures only when they clarify geometry/regimes, illustrate consequences, or test numerical behavior; proof remains the decisive evidence for theorem claims;
- **qualitative** — a paper may legitimately need no main figure; use conceptual/thematic displays only when they improve interpretation;
- **review/synthesis** — figures encode taxonomy, evidence maps, mechanisms, study-selection/meta-analytic structure, or conceptual relationships rather than pretending to be original empirical results.

Hybrid papers combine only the roles required by their actual publication promises. Do not duplicate orientation/validation simply because two archetypes are present.

There is no universal main-figure count or sequence.

## Claim-driven plot planning gate

When planning a manuscript figure set, load `../../../nature-shared/core/figure-evidence-planning.md` and, for every major claim, record:

```text
Claim
Reader question
Why a figure is or is not needed
Scientific/statistical unit
Estimand
Data structure
Alternative explanation / risk to reveal
Recommended plot family
Uncertainty/comparator to show
Main vs support
```

### Figure necessity

A figure/panel should normally perform at least one of these jobs:

- reveal a pattern/distribution;
- enable a central comparison;
- expose pairing/heterogeneity;
- show uncertainty that changes interpretation;
- explain a complex mechanism/workflow/system;
- reveal high-dimensional/spatial/network structure;
- show validation/generalization/failure boundary;
- compress evidence more effectively than prose/table.

If two numbers can be stated more clearly in one sentence, do not create a decorative panel just to fill a figure.

### Plot form follows reader task + data structure

Examples of starting points:

- small-sample continuous groups -> show individual observations/distribution rather than only mean bars;
- paired change -> connected pairs or paired-difference display;
- time/dose/ordered parameter -> trajectory/line only when order is meaningful;
- association -> scatter/hexbin/density with justified fit if needed;
- calibration -> calibration/reliability display, not AUC alone;
- classification -> ROC/precision–recall/operating-point displays according to the decision problem;
- survival -> censoring-aware survival/cumulative-incidence representation;
- heterogeneity -> forest/stratified effect display;
- benchmark -> per-task/site/run paired or interval comparisons rather than only grand means when variation matters;
- robustness -> sensitivity curves/intervals/small multiples, usually support;
- imaging -> representative image + quantitative evidence when a population-level claim is made;
- high-dimensional data -> heatmap/embedding only when the pattern is the object of interest, with quantitative evidence for inferred claims;
- null result -> effect estimate + uncertainty/equivalence logic rather than `P > 0.05` alone.

These are scientific starting points, not universal style rules.

## Analogue-paper calibration gate

When the task is a serious paper-figure redesign and the field/contribution class is known, load:

- `../../../nature-shared/core/analogue-paper-calibration.md`;
- `../../references/analogue-figure-calibration.md`.

Study a few close comparator papers to understand:

- what scientific role each main figure performs;
- which controls/comparators/uncertainty are visible;
- whether raw observations, distributions, pairing, validation, mechanism, generalization, or failure boundaries are shown;
- how figure roles are sequenced;
- what is delegated to SI/Extended Data.

Then choose the final representation from the user's actual estimand/data structure. A chart's popularity in analogue papers is never sufficient justification for using it.

Preserve a coherent project visual identity: semantic colors, typography hierarchy, panel labels, line/marker logic, notation, spacing rhythm, and annotation style. Do not copy a comparator paper's distinctive layout or palette.

Skip this gate for small mechanical export/layout fixes or when no reliable analogue set exists.

## Content-allocation gate

Load `../../../nature-shared/core/manuscript-content-selection.md` before finalizing main/support placement.

Main figures carry the **shortest sufficient visual evidence chain** for headline claims. Extended Data/SI can carry repeated robustness, parameter sweeps, non-central controls, extended benchmarks, specialist diagnostics, and provenance details unless they change the headline interpretation.

Do not bury a failed external validation, subgroup reversal, adverse effect, or failure boundary in support material if the abstract/title/general claim would otherwise become misleading.

## Legend/caption and manuscript-surface gate

Before delivering figure titles, legends, captions, table notes, alt text or body callouts, load:

- `../../references/figure-legend-conventions.md`;
- `../../../nature-shared/core/manuscript-surface-qa.md`.

This is a **hard last-mile gate**. Manuscript-facing text must not expose internal plotting or repository artifacts merely because the figure pipeline knows them.

Remove, translate or relocate as appropriate:

- plot-script/notebook/config names;
- local/repository paths;
- source/output image filenames;
- helper/class/function names;
- CLI commands/flags;
- branch/PR/issue/commit/CI details;
- temporary run/checkpoint/output identifiers;
- raw repository links outside the designated availability/artifact location.

A legend should describe the scientific display, not how the project tree generated it.

Then run punctuation/typography QA for doubled punctuation, spacing, bracket balance, figure-reference forms, panel punctuation, units, ranges/minus signs, and target-specific citation/equation/title conventions. Do not mechanically alter scientific identifiers or chemical/biological names.

## The nine-point contract

1. **Core conclusion**: write the one-sentence claim the figure must defend.
2. **Reader question**: state what uncertainty/comparison the reader should resolve by inspecting the figure.
3. **Paper archetype**: identify the relevant epistemic job so figure roles match the scientific promise.
4. **Evidence/estimand**: identify the data/statistical unit, quantity of interest, and alternative explanation.
5. **Representation**: choose the plot/image/table/schematic family from the data/question, not journal popularity.
6. **Evidence chain**: map each planned panel to one unique claim question, and drop or merge panels that only redraw another panel's evidence.
7. **Analogue evidence prior**: when applicable, record what comparable papers make visible for claims of this type, plus patterns deliberately rejected if they do not fit our data.
8. **Backend**: use the explicit or saved Python/R track exclusively once rendering begins.
9. **Journal/export + surface contract**: set physical/export requirements and ensure every manuscript-facing label/legend/caption is artifact-clean, punctuated correctly, and target-aware.

The highest-priority rule is: **the chart serves the scientific logic**. Aesthetic polish, template matching, analogue similarity, and complex layout are subordinate to making the core conclusion clear, defensible, reviewable, and faithful to the data.

For the full method to convert a request into core conclusion, evidence hierarchy, panel map, and review-risk checks, open `references/figure-contract.md`.
