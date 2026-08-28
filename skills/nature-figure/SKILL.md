---
name: nature-figure
description: >-
  Create, revise, audit, and export submission-grade scientific figures for any academic journal or conference in Python (matplotlib/seaborn) or R (ggplot2/patchwork/ComplexHeatmap), including multi-panel plots, figures4papers-style work, and journal-ready vector/raster outputs. The legacy skill name is retained for compatibility; target-journal compliance is resolved independently for Nature Portfolio, Science/AAAS, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, Wiley, society journals, and other venues. For serious manuscript figure design or redesign, study a few genuinely comparable papers to learn evidence roles, figure sequence, data visibility, plot grammar, and main-text-versus-SI allocation, while preserving an independent project visual identity and choosing the final representation from the user's actual data. Define the conclusion, evidence logic, data integrity, target journal/content type/stage, export needs, accessibility, and reviewer risks before plotting. Also use the separate OpenRouter GPT Image 2 route for explicit AI-generated graphical abstracts, mechanism diagrams, concept schematics, 论文示意图、机制示意图、图形摘要; treat those outputs as drafts and check the exact venue's current AI-image policy. Do not use for interactive dashboards, statistics-only analysis, data cleaning, literature review, code debugging, pure photo editing, or Illustrator/Figma-first infographics without manuscript-figure intent.
---

# Journal-Aware Scientific Figure Making — Router

`nature-figure` is a legacy entry-point name. Do not infer Nature production rules from the skill name.

This skill is split into:

- a **static layer** under `static/` for the figure contract, stance, and backend quick starts;
- a **dynamic layer** (`SKILL.md` + `manifest.yaml`) that resolves plotting route/backend and loads only the relevant design, analogue-study, QA, and journal-compliance references.

Scientific design and journal submission mechanics are separate. Build an honest, legible figure first; adapt packaging to the exact target second.

## Routing protocol

### 0. Resolve special AI/graphical-abstract routes first

For every AI-assisted graphical-abstract planning, generation, revision, or audit task, read `references/ai-graphical-abstract-workflow.md` first. It owns the message/audience brief, composition workflow, human scientific review, disclosure boundary, provenance, and policy gate.

If the user explicitly requests OpenRouter, GPT Image 2, an image-generation API, an AI-generated paper schematic, graphical abstract, mechanism diagram, or concept illustration:

1. Read [manifest.yaml](manifest.yaml) and the `always_load` files.
2. Read `references/ai-graphical-abstract-workflow.md`.
3. Read `references/openrouter-image-generation.md`.
4. Use `scripts/generate_openrouter_schematic.py` when a real API call or reproducible payload is requested.
5. Treat the result as a draft schematic rather than quantitative data. Do not invent measurements, unsupported mechanisms, author/institutional marks, or provenance.
6. If a target journal/venue is named, also load `references/journal-adaptation.md` and verify its current AI-generated/AI-assisted image policy. A different journal's permission is not clearance.

Planning/audit-only graphical-abstract work does not need the Python/R backend gate. Continue to the backend gate only for plotting, charting, data visualization, or manuscript figure assembly.

### 1. Load the manifest and core layer

Read [manifest.yaml](manifest.yaml) and every file under `always_load`:

- `static/core/contract.md`
- `static/core/stance.md`

The figure contract determines the scientific conclusion, evidence hierarchy, data-integrity checks, target/stage, and output contract before plotting.

### 1.5 Scientific display decision contract

For every evidence-bearing plot, figure, table, image plate, diagram, or mixed
display, load `../nature-shared/core/scientific-display-decision-contract.md`.
Resolve the reader task, scientific object/estimand, statistical unit and
dependence structure, candidate representation, allowed/prohibited inference,
data/analysis/render/source-data lineage, caption semantics, omitted groups,
accessibility, and placement before rendering.

The maintained adapters and `resolve_scientific_display.py` return candidate
families and obligations, never a universal best chart. An unmatched scientific
task triggers domain-specific research rather than a forced generic plot. A
passing automated contract remains bounded: final-size visual inspection and
human scientific judgment are still required.

### 2. Resolve the plotting backend — blocking only for plotting tasks

Determine backend in this order:

1. Explicit Python or R choice in the current request.
2. Clearly language-specific input/workflow.
3. Saved preference from `scripts/nature_figure_backend.py get`.
4. If none exists, ask once: **Python or R? I will remember this as your default.** Then save the answer before plotting.

- `python` — matplotlib / seaborn
- `r` — ggplot2 / patchwork / ComplexHeatmap

Do not choose a backend by aesthetics alone. If the user asks for a recommendation, load `references/backend-selection.md`, explain the reason, save the selected preference, and proceed. Once resolved, keep the backend exclusive for drawing, preview, export, and visual QA unless the user explicitly changes it.

Backend choice is independent of journal choice.

### 3. Resolve target journal/venue and stage

For every named target, classify:

`exact journal/venue -> article/content type -> stage -> figure component`

Use stages:

- `planning`
- `initial-submission`
- `revision`
- `accepted`
- `production`

Then route:

- **flagship Nature** -> `references/nature-article-requirements.md`
- **Nature Machine Intelligence** -> `../nature-shared/journal-formats/nature-machine-intelligence.md`
- **any other named journal/venue or journal transfer** -> `references/journal-adaptation.md`, plus shared `journal-resolution.md`; add `journal-family-profiles.md` only as fallback context
- **no target** -> generic accessible publication figure; do not invent dimensions, formats, legend limits, or source-data rules

When exact compliance matters, current official instructions for the exact target/content type/stage outrank local profiles.

### 4. Run an analogue-paper visual calibration when useful

For serious manuscript figure design/rewrite where the field, claim class, or target is known, load:

- `../nature-shared/core/analogue-paper-calibration.md`;
- `references/analogue-figure-calibration.md`.

Inspect a few **near-neighbor papers** matched by contribution type, study design, data modality, article type, and audience. The goal is to learn:

- what scientific role each main figure performs;
- which data are visible in the main paper;
- how comparable claims expose controls, uncertainty, raw observations, validation, generalization, and failure boundaries;
- how figure roles are sequenced;
- what is relegated to Methods/SI/Extended Data;
- which plot forms are local conventions versus scientifically necessary choices.

Do **not** copy colors, distinctive panel compositions, visual motifs, normalization, statistics, axis choices, or production dimensions from published papers.

Use analogue papers as **visual/evidence priors**, then select the final plot from the user's actual data structure and reader task. A common plot that hides the estimand is the wrong plot.

Skip or bound this pass when there is no reliable analogue set, the user asks only for a mechanical export/layout fix, or the task is too small for literature calibration to add value.

### 5. Load the matching backend fragment

Read only the selected backend fragment:

- `static/fragments/backend/python.md`, or
- `static/fragments/backend/r.md`

Do not load the other backend fragment unless the user explicitly asks to compare backends.

### 6. Build the figure in the correct priority order

Apply:

1. **Scientific contract** — core conclusion, evidence chain, panel map, statistical/data-integrity risks.
2. **Analogue evidence calibration** — when applicable, use comparable papers to identify expected evidence roles, figure sequence, and local visual grammar without copying surface design.
3. **Project visual identity** — keep typography hierarchy, semantic colors, panel labels, markers/lines, annotation style, spacing rhythm, and variable notation coherent across the manuscript unless accessibility or exact target rules require a change.
4. **Default stance** — archetype-first composition, clear hierarchy, restrained encoding, accessible typography/color.
5. **Backend fragment** — executable plotting/export rules.
6. **Asset adaptation** — if reusing any bundled/user/licensed template, load `references/asset-adaptation.md` before remapping data.
7. **Journal adaptation** — apply only verified target/stage requirements. Do not change data or evidentiary strength to fit house style.
8. **Delivery QA** — load `references/qa-contract.md`, run available validators, inspect each panel and the complete figure at final physical size.

For a journal transfer, preserve source data, analysis code, scales, statistics, and panel meaning; remove the old journal's dimensions/legend boilerplate; reflow and re-render for the new verified contract rather than shrinking a raster screenshot.

### 7. What cross-journal adaptation must check

`references/journal-adaptation.md` owns the detailed checklist. At minimum resolve independently:

- display-item count and panel assembly rules
- column/page width and physical dimensions
- vector/raster formats and required resolution
- color mode, fonts, line weights, transparency/layers
- panel-label convention and in-figure titles
- legend placement/content/limits
- scale bars and imaging integrity
- statistical/sample-size definitions
- source/underlying-data requirements
- accessibility and alt-text/long-description requirements
- graphical abstract / TOC / cover-art rules
- AI-generated/AI-assisted image policy
- initial-review versus production differences

Published appearance is not a substitute for the author instructions.

### 8. Reach for references only when needed

Open on demand according to [manifest.yaml](manifest.yaml). Key routes include:

- analogue-paper evidence/figure study -> `../nature-shared/core/analogue-paper-calibration.md` + `references/analogue-figure-calibration.md`
- contract planning -> `references/figure-contract.md`
- backend recommendation -> `references/backend-selection.md`
- R workflow -> `references/r-workflow.md`
- template reuse -> `references/asset-adaptation.md`
- final QA -> `references/qa-contract.md`
- non-Nature target/journal transfer -> `references/journal-adaptation.md`
- exact flagship Nature -> `references/nature-article-requirements.md`
- exact NMI -> `../nature-shared/journal-formats/nature-machine-intelligence.md`
- design rationale -> `references/design-theory.md`
- Python helper API -> `references/api.md`
- patterns/chart recipes -> `references/common-patterns.md`, `references/chart-types.md`, `references/template-catalog.md`
- Nature visual examples -> `references/nature-2026-observations.md` as inspiration only, never as another journal's technical contract
- AI graphical abstract -> `references/ai-graphical-abstract-workflow.md`
- OpenRouter generation -> `references/openrouter-image-generation.md`
- legend writing -> `references/figure-legend-conventions.md` plus the exact target-journal rules

## Delivery contract

For journal-specific final delivery, distinguish:

- `verified` — exact current requirements checked
- `applied` — changes made to satisfy them
- `unresolved` — unknown article type/stage or conflicting/missing current rules
- `not applicable` — checked but irrelevant

For analogue calibration, distinguish:

- `observed` — pattern present in analogue papers;
- `adopted` — used because it fits our scientific question/data;
- `adapted` — function retained but representation/wording redesigned for our evidence;
- `rejected` — common pattern not suitable for our data/claim;
- `unresolved` — more evidence/comparators needed.

Automated checks do not replace visual inspection at final physical size.

## Generalization and integrity rules

Never:

- copy Nature/NMI dimensions, display budgets, or legend rules into another venue
- infer production requirements from a published PDF alone
- shrink a raster figure until labels become unreadable
- change axes, crops, normalization, uncertainty, sample size, or statistical annotations deceptively to fit a layout
- assume graphical abstracts or STAR-style elements are universal across a publisher
- assume an AI-image policy transfers between journals
- copy a distinctive figure composition, palette, or visual identity from an analogue paper
- use a chart solely because it is common in the target literature when another representation better exposes the user's estimand/data

The chart serves the scientific logic. Analogue papers provide evidence about community expectations and successful evidence architectures, but journal aesthetics and published examples remain subordinate to clarity, integrity, reproducibility, accessibility, the user's actual data, and exact verified target requirements.
