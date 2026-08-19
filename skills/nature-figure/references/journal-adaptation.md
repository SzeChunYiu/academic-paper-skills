# Cross-journal figure adaptation

Use this reference whenever a scientific figure has a named target journal/venue outside the exact Nature and Nature Machine Intelligence profiles, or when a figure is being transferred between journals.

First read:

- `../../nature-shared/journal-formats/journal-resolution.md`
- `../../nature-shared/journal-formats/journal-family-profiles.md` when family context is useful

Then resolve:

`exact journal -> article/content type -> stage -> figure component`

Do not infer technical requirements from the legacy `nature-figure` skill name.

## 1. Keep scientific design separate from submission mechanics

The figure's scientific job is target-independent:

- one clear conclusion or question per figure
- explicit evidence hierarchy and panel logic
- correct data transformations and statistics
- visible uncertainty and sample-size definitions where relevant
- consistent terminology/units
- no misleading axis, crop, normalization, or selective omission
- accessible encoding that does not rely on color alone

Journal adaptation changes the packaging and sometimes the amount of material, not the underlying data or strength of the conclusion.

## 2. Resolve the stage

Use the shared stage labels:

- `planning`
- `initial-submission`
- `revision`
- `accepted`
- `production`

A production raster/vector requirement must not be presented as mandatory for initial submission unless the exact journal says so.

## 3. Verify the exact figure contract

For a submission-critical named target, check the current official author/figure instructions and record the source/access date in working notes.

Check independently:

### Geometry and layout

- allowed display-item count, if any
- one-column/two-column/page-width targets
- maximum physical dimensions
- portrait/landscape restrictions
- whether multi-panel figures should be assembled or uploaded panel-by-panel
- panel-label convention

### File and rendering requirements

- accepted formats (PDF/EPS/SVG/TIFF/JPEG/PNG/source files, etc.)
- vector versus raster preference
- required/minimum resolution by artwork type
- color mode requirements
- font embedding or typeface rules
- line-weight and text-size constraints
- transparency/layer restrictions

### Legends and in-figure text

- legend location and any length constraints
- abbreviation definitions
- statistical notation requirements
- whether titles belong in the graphic or only in the legend
- scale-bar requirements for microscopy/imaging

### Data integrity and source data

- underlying/source-data submission
- uncropped/unprocessed image requirements
- blot/gel/source-image rules
- error-bar/sample-size/statistical-test disclosure
- image manipulation policies

### Accessibility

- color-vision-safe design
- contrast and legibility at final size
- alt text or long-description requirements
- patterns/shapes/direct labels when color alone would be ambiguous

### Special visual products

Resolve separately for:

- graphical abstracts
- TOC graphics
- highlights/image teasers
- cover-art submissions
- video/interactive/supplementary figures

These are not implied by the main-figure rules.

### AI-assisted/generated imagery

Check the exact journal/publisher policy current at submission time for:

- eligibility of generated images in scientific figures
- required disclosure
- provenance/documentation
- restrictions on logos, identifiable people, copyrighted material, or manipulated scientific images

Practitioner advice or another journal's policy is not submission clearance.

## 4. Family-specific fallback questions

These are prompts for what to verify, not exact requirements.

### IEEE

- publication-specific template and column geometry
- grayscale/color reproducibility and print legibility
- vector/raster export and lettering at final column size
- whether graphical abstracts are used by the exact periodical

### ACM

- venue template/TAPS pipeline
- one-column review versus final publication layout
- accessibility/alt-text expectations
- anonymity implications for screenshots, datasets, or acknowledgments

### Cell Press

- exact journal's graphical-abstract/front-matter expectations
- STAR Methods/source-data relevance where applicable
- figure count/legend/file rules for the exact content type

### PLOS

- exact journal figure upload/placement workflow
- data availability and underlying data linkage
- file/resolution/legend rules from the current journal guide

### Elsevier

- exact Guide for Authors artwork rules
- journal-specific graphical abstract/highlights requirements
- initial-format flexibility versus final artwork requirements

### Springer/BMC

- journal-specific artwork and supplementary rules
- structured data/availability expectations
- initial versus production source-file needs

### Wiley/society journals

- exact society journal artwork guide
- online-only color versus print constraints where relevant
- reference/legend/style variations owned by the society journal

## 5. Journal transfer workflow

When moving an existing figure from journal A to journal B:

1. Preserve the source data, analysis code, panel logic, statistics, and scientific labels.
2. Remove A-only dimensions, label conventions, legend boilerplate, source-data wording, or graphical-abstract assumptions.
3. Resolve B's exact content type and stage.
4. Reflow panels for B's physical dimensions without changing scales/normalization deceptively.
5. Re-render text at final physical size; do not merely resize a raster screenshot.
6. Rewrite the legend only where B's conventions require it, preserving the same scientific information.
7. Re-run automated and visual QA at B's final size.
8. Archive a reproducible export configuration for the new target.

## 6. Compliance report

For final journal adaptation, report:

- `verified`: exact current requirements checked
- `applied`: changes made
- `unresolved`: rules/source conflicts or unknown article type/stage
- `not applicable`: checked but irrelevant

For every numeric or mechanical requirement, distinguish verified rules from design preferences.

## Anti-patterns

Never:

- copy flagship Nature dimensions or legend limits into another journal
- infer production requirements from published PDF appearance alone
- shrink a completed raster figure until labels become unreadable
- change data limits, cropping, uncertainty, or statistical annotations merely to fit a layout
- treat a graphical abstract requirement as universal across a publisher
- declare AI-generated scientific imagery acceptable because another journal permits it
