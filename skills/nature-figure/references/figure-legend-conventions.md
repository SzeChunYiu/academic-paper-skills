# Figure and table legend/caption conventions

Use this file when **writing or auditing manuscript-facing figure legends, table captions, panel descriptions, or display notes**.

The core rule is target-aware:

> A legend must help the reader identify **what is shown and how to read it**. Its exact title syntax, punctuation, panel grammar, statistics placement, source-data boilerplate, attribution wording, and length are determined by the exact journal/venue, article type, and stage.

Do not infer a universal caption skeleton from one journal corpus.

## Contents

- [Scientific job](#scientific-job)
- [Main text versus legend](#main-text-versus-legend)
- [Target-aware structure](#target-aware-structure)
- [Panel descriptions](#panel-descriptions)
- [Statistics and uncertainty](#statistics-and-uncertainty)
- [Artifact-leakage boundary](#artifact-leakage-boundary)
- [Punctuation and typography](#punctuation-and-typography)
- [Tense](#tense)
- [Self-containment](#self-containment)
- [Attribution and reused material](#attribution-and-reused-material)
- [Table captions](#table-captions)
- [Local Nature Communications CS/AI observational profile](#local-nature-communications-csai-observational-profile)
- [Length and exact-journal gate](#length-and-exact-journal-gate)
- [Final legend audit](#final-legend-audit)

## Scientific job

A legend is neither a plotting log nor a miniature paper.

Its first responsibility is to let the intended reader recover:

- what each display/panel contains;
- groups, conditions and comparators;
- axes/units or scale bars where needed;
- the scientific/statistical unit and `n` definition where relevant;
- uncertainty/error-bar meaning;
- statistical annotation definitions when needed;
- concise panel-specific experimental or analytical context required to interpret the display;
- attribution/source-data statements required by the exact target.

A legend may include a tightly bounded inference when the target and local writing convention permit it and the visual evidence directly supports that inference. Do not use the legend to make a stronger claim than the main text/evidence warrants.

## Main text versus legend

Use the division of labor:

**Main text**

- tells the reader **why the figure is being shown**;
- identifies the pattern/comparison that matters;
- explains the scientific inference and boundary;
- connects the figure to the next evidence block.

**Legend/caption**

- tells the reader **what is shown**;
- explains how to decode it;
- provides display-specific definitions, conditions and statistics needed to read it.

Do not make the body merely say `see Fig. 3` while forcing the legend to carry the whole scientific argument.

Do not repeat the entire Results paragraph in the legend either.

## Target-aware structure

Before writing the legend, resolve:

`exact journal/venue -> article/content type -> stage -> display component`

Then apply the verified target rule.

Possible target conventions include:

- title after `Fig. N |`;
- bold or plain title;
- sentence-style or noun-phrase title;
- panel letters in bold, italic, parentheses, or prose;
- full sentences versus compact telegraphic panel descriptions;
- statistics embedded in panel descriptions versus a final statistics sentence;
- explicit source-data boilerplate;
- different rules for initial submission versus production.

These conventions are **not interchangeable across journals**.

If the target is unknown, use a generic readable form:

1. concise informative figure title;
2. panel-by-panel decoding in panel order;
3. statistical/sample-size/uncertainty definitions where necessary;
4. attribution/source statements only when applicable.

Do not invent a journal-specific `Fig. N |` style when no target has been resolved.

## Panel descriptions

Write panel text in the same order the reader encounters the panels unless another order is scientifically clearer and the target permits it.

For each panel, include only what is needed to decode and evaluate it:

- data/entity/population;
- condition/comparator;
- measurement/quantity;
- plot/image encoding;
- key scale/unit;
- uncertainty/statistics as required.

Do not narrate the plotting pipeline.

Bad:

`b, Plot generated from outputs/site_metrics.csv using scripts/plot_auc.py.`

Better:

`b, Site-level discrimination in three external validation cohorts; points show cohort estimates and bars show 95% confidence intervals.`

The second version describes the **science**, not the repository.

## Statistics and uncertainty

Statistics placement is target- and display-dependent.

When necessary to interpret the figure, identify:

- sample/statistical unit and `n`;
- what error bars/intervals represent;
- whether values are mean/median/model estimate/etc.;
- statistical test/model;
- multiplicity correction when relevant;
- sidedness when required;
- exact/threshold P-value convention according to the target;
- repeated-measures/paired structure when relevant.

Do not add statistics merely because a local corpus often did. Do not duplicate a full numerical report in both Results and legend when one authoritative location plus a concise cross-reference is clearer and target-compliant.

## Artifact-leakage boundary

Before final delivery, load `../../nature-shared/core/manuscript-surface-qa.md`.

A manuscript-facing legend should normally **not** expose:

- plot script names;
- notebook names;
- source/output image filenames;
- CSV/TSV/XLSX filenames;
- local or repository paths;
- helper function/class names;
- configuration keys or config filenames;
- command-line flags/invocations;
- branch/PR/issue/commit/CI details;
- temporary run/checkpoint identifiers;
- repository navigation instructions;
- export filenames such as `fig3_final_v8.svg`.

Translate to scientific language or move the operational detail to source-data/artifact metadata.

### Legitimate literal identifiers

Retain only when scientifically/access-wise necessary, for example:

- canonical accession/registry IDs;
- protein/gene/variant identifiers;
- a named public dataset/resource;
- a software package name central to the method;
- a PDB accession;
- a target-required source-data identifier;
- required permission/attribution wording.

Even legitimate identifiers should not be repeated simply because the plotting code knows them.

## Punctuation and typography

A legend is manuscript prose. Run normal copy-editing after the scientific content is stable.

Check:

- no doubled punctuation;
- no accidental spaces before commas/periods/semicolons;
- spaces after punctuation where prose requires them;
- balanced parentheses/brackets;
- consistent panel-letter punctuation;
- consistent punctuation of parallel panel descriptions;
- correct figure reference form for the target;
- correct range dash/minus/hyphen usage;
- correct spacing around values and units according to the target;
- correct capitalization of display labels versus prose;
- canonical spelling of scientific/model/product names.

Do not apply automatic `.title()` transformations to labels such as `XGBoost`, `DeepSeek`, `GPT-5.2`, gene symbols, chemical names, or formal abbreviations.

### Title punctuation

Whether a short figure title takes a terminal period is **target-specific**. Do not hard-code `no full stop` from a Nature Communications corpus into other venues.

### Panel punctuation

Some journals/corpora favor compact panel fragments; others favor complete sentences. Use the exact target convention when known. For an unknown target, prefer grammatically coherent concise prose over forced telegram style.

## Tense

Tense follows the semantic job, not a universal figure-caption formula.

Useful defaults:

- present tense for what the display **shows/contains**;
- past tense for what the authors **did** to generate/measure/analyse something;
- present/perfect/past for interpretation/prior-work attribution according to normal academic grammar and target convention.

Do not rewrite all panel text into present tense when doing so obscures the procedural relation.

## Self-containment

A legend should be interpretable without forcing the reader to hunt through the manuscript for basic decoding information.

Include enough to recover:

- symbols/colors/line styles;
- sample unit and essential conditions;
- axes/units/scale bars;
- abbreviations not already safely established or target-exempt;
- statistical notation;
- important image-processing/normalization facts **only when they affect interpretation**.

Self-containment does **not** mean reproducing the full Methods section or repository instructions.

## Attribution and reused material

For adapted/reproduced third-party material, follow exact copyright/licensing/journal requirements.

A permission/attribution line is publication provenance and should remain when required. It is not repository leakage.

Do not copy another paper's legend wording except for unavoidable required attribution/legal language.

## Table captions

Table captions follow the same scientific principles:

- identify the table's purpose/content;
- define columns/abbreviations/statistical summaries necessary to interpret it;
- avoid repeating every numerical result in prose;
- send detailed procedure to Methods when appropriate;
- follow exact target punctuation/title/note conventions.

A benchmark or resource paper may legitimately lean more heavily on tables than figures when exact multi-metric or metadata comparison is the reader task.

## Local Nature Communications CS/AI observational profile

This subsection records a **local observed profile**, not a universal contract.

A 2025 set of 20 open-access Nature Communications computer-science/AI research articles frequently used:

- `Fig. N |` followed by a short overall title;
- panel letters followed by compact present-tense descriptions;
- sample size/error/test information in the legend;
- Source Data wording at the end when applicable;
- display labels with stable canonical model/product capitalization.

This pattern can help when the exact target is a comparable Nature Communications research article and current author instructions do not conflict.

It must **not** be imposed on:

- flagship Nature;
- Nature Machine Intelligence;
- PLOS/IEEE/ACM/Cell/Science/etc.;
- clinical trial captions;
- qualitative figures;
- theory papers;
- tables whose target style differs;
- any unknown target.

Observed frequency is not evidence that the pattern is intrinsically better.

## Length and exact-journal gate

Do not use one numeric legend limit for all journals.

- Flagship **Nature**: load `nature-article-requirements.md` and use its current verified complete-legend limit.
- **Nature Machine Intelligence**: load the shared NMI contract and distinguish current live instructions from historical advisory guidance.
- **Nature Communications** or another title: verify current exact instructions before enforcing a number.
- Other venues: resolve exact current requirements.

For an unknown target, optimize for sufficient decoding and no redundant Results/Methods repetition rather than a fabricated word ceiling.

## Final legend audit

Before release ask:

1. Does the title/panel syntax match the exact target, or a neutral generic form if unresolved?
2. Can the reader decode every panel without opening the project repository?
3. Did any filename, path, script/helper, CLI flag, notebook, output artifact or developer-history token leak into the legend?
4. Are `n`, units, uncertainty and statistics defined sufficiently for the display?
5. Does the body text still explain what scientific pattern matters and why?
6. Does the legend avoid duplicating the whole Results/Methods narrative?
7. Are punctuation, brackets, spacing and figure-reference forms mechanically clean?
8. Did punctuation/copy-editing alter any scientific identifier, mathematical expression, range, chemical/biological name or citation?
9. Is required attribution/source-data language present and exact?
10. Does every retained literal identifier perform a scientific, access, or publication-provenance function?

A polished figure is not complete until its **manuscript-facing text** passes the same artifact-leakage and copy-editing standard as the body.