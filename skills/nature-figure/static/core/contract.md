# Figure contract before plotting

A publication-quality scientific figure is a visual argument, not an isolated pretty plot. Every figure starts from a claim, an evidence hierarchy, and a review-risk check before code or aesthetics. For serious manuscript figure design/redesign, a focused analogue-paper pass may also be needed to learn what visual evidence comparable claims normally require without copying another paper's visual identity.

## Backend selection uses a saved preference

For plotting tasks, first honor an explicit Python/R choice in the current request or a clearly language-specific input file/workflow. Save that backend as the user's default with `scripts/nature_figure_backend.py set python` or `scripts/nature_figure_backend.py set r`.

If the current request does not specify a backend, check the saved preference with `scripts/nature_figure_backend.py get`. If it returns `python` or `r`, use that backend without asking again.

If no saved preference exists, ask one concise question: **Python or R? I will remember this as your default.** Then stop and wait for the user's answer. Do not generate mock data, write scripts, create figures, or choose Python/R by default before this first preference is established. After the user answers, save it and proceed.

Only recommend a backend when the user explicitly asks you to choose or recommend one. In that case, use `references/backend-selection.md`, state the reason, save the selected backend, and then proceed with the recommended backend.

## The selected backend is exclusive

Once Python or R is selected, every plotting script, preview image, SVG/PDF/TIFF/PNG export, QA render, and visual workaround must be produced by that same backend. Do not use Python to draw a preview for an R figure, and do not use R to draw a preview for a Python figure, even if the selected runtime or packages are missing locally. The non-selected language may only be used for non-visual file inspection or data conversion when it does not open a graphics device, import plotting libraries, create image/vector files, or change the final visual appearance.

## Missing runtime/package rule

After the backend is selected, check the selected runtime early (`Rscript`/R for R; Python and required plotting packages for Python). If the selected runtime or required packages are unavailable, stop before rendering and report the exact blocker. You may provide a selected-backend script and installation commands, or ask permission to install dependencies, but you must not fall back to the other language to make a substitute figure.

## Data-integrity gate

Use all user-provided observations and requested variables unless an exclusion has a scientific or statistical justification or the user explicitly requests a subset. Never reduce data merely to make a plot easier or faster to render. For large point clouds, prefer rasterized marks, hexbin/density representations, aggregation with a stated rule, or another backend-native rendering strategy.

If any row, column, replicate, image, or category is excluded, record the before/after counts, the exact rule, and the reason in the QA notes. Preserve the unmodified source data and never silently select convenient columns to satisfy a template.

Plan figures by scientific claims, not by source tables. Do not turn each table into a separate figure when several tables answer the same question. If an effect is defined within matched datasets, subjects, seeds, or tasks, inspect and visualize paired differences rather than relying only on overlapping marginal distributions; large between-unit heterogeneity can hide a strong paired effect.

## Analogue-paper calibration gate

When the task is a serious paper-figure redesign and the field/contribution class is known, load:

- `../../nature-shared/core/analogue-paper-calibration.md`;
- `../../nature-figure/references/analogue-figure-calibration.md` (or the routed equivalent from `SKILL.md`).

Study a few close comparator papers to understand:

- what scientific role each main figure performs;
- which controls/comparators/uncertainty are visible;
- whether raw observations, distributions, pairing, validation, mechanism, generalization, or failure boundaries are shown;
- how figure roles are sequenced;
- what is delegated to SI/Extended Data.

Then choose the final representation from the user's actual estimand/data structure. A chart's popularity in analogue papers is never sufficient justification for using it.

Preserve a coherent project visual identity: semantic colors, typography hierarchy, panel labels, line/marker logic, notation, spacing rhythm, and annotation style. Do not copy a comparator paper's distinctive layout or palette.

Skip this gate for small mechanical export/layout fixes or when no reliable analogue set exists.

## The six-point contract

1. **Core conclusion**: write the one-sentence claim the figure must defend.
2. **Evidence chain**: map each planned panel to one unique claim question, and drop or merge panels that only redraw another panel's evidence.
3. **Analogue evidence prior**: when applicable, record what comparable papers make visible for claims of this type, plus at least one pattern we deliberately reject if it does not fit our data.
4. **Archetype**: classify the figure as `quantitative grid`, `schematic-led composite`, `image plate + quant`, or `asymmetric mixed-modality figure`.
5. **Backend**: use the explicit or saved Python/R track exclusively for all figure drawing, previewing, exporting, and visual QA. Do not cross-render with the other language.
6. **Journal/export contract**: set final dimensions, a 5 pt floor for every rendered glyph, editable text, source data, statistics, image-integrity notes, and export formats before styling.

The highest-priority rule is: **the chart serves the scientific logic**. Aesthetic polish, template matching, analogue similarity, and complex layout are subordinate to making the core conclusion clear, defensible, reviewable, and faithful to the data.

For the full method to convert a request into core conclusion, evidence hierarchy, panel map, and review-risk checks, open `references/figure-contract.md`.
