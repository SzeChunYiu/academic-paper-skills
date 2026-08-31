# Venue-constrained manuscript budgeting evidence note — 2026-08-31

## Question

When a target venue/article type is known, should manuscript length, section allocation, figures/tables, references, captions, appendices, and revision reserve be treated as an explicit scientific planning problem rather than a late formatting step?

## Expert lenses

1. **Scientific-writing editor** — which reader functions deserve scarce main-text space?
2. **Venue-policy analyst** — what exactly counts toward a current target's limit?
3. **ML/computing reviewer** — how do page limits and reviewer burden alter manuscript design?
4. **Reproducibility/integrity engineer** — what must remain visible despite compression, and what can move to support?

## Current official evidence

### Nature / Nature Portfolio

Nature's current formatting guidance ties paper length directly to display use. A typical six-page Article is described as about 2,500 words plus four modest display items; a typical eight-page Article as about 4,300 words plus five to six display items. The guide explicitly notes that a larger composite figure may require reducing the text. It also states that essential but technical detail can move to Methods or Supplementary Information. The guide separately constrains title length, recommends up to roughly 50 main references, and gives a Methods guideline of about 3,000 words.

Transfer: manuscript space is multi-currency; figures and text compete for publication area. Technical completeness and main-narrative completeness should be separated.

Source: Nature, `Formatting guide`, accessed 2026-08-31.

### Nature Computational Science

The current content-type page states for an Article:

- main text up to 3,500 words, excluding abstract, Methods, references, and figure legends;
- abstract up to 150 words;
- up to six display items;
- Introduction, Results, Discussion, Online Methods structure;
- guideline of up to about 50 references.

Brief Communications have a much smaller 1,000–1,500 word main-text envelope and up to two display items. Perspectives allow up to 4,000 words and up to 100 references.

Transfer: the exact article/content type must be resolved before allocation. One venue name does not imply one budget.

Source: Nature Computational Science, `Content Types`, accessed 2026-08-31.

### NeurIPS 2026

The current Main Track Handbook limits submitted main paper content to nine pages **including figures and tables**. References, optional technical appendices, and the checklist do not count as content pages. The official template is mandatory and authors may not change layout to create space.

Transfer: for a page-constrained venue, rendered page area is the binding resource; source word count is only a planning proxy. Figure/table/equation decisions must be budgeted together with prose.

Source: NeurIPS 2026, `Main Track Handbook`, accessed 2026-08-31.

### TMLR

TMLR's current author guide says submissions may be any length but length should be justified by content and unusually long papers may delay review. The current FAQ/reviewer guidance states that main bodies over 12 pages use longer review timescales.

Transfer: absence of a hard page limit does not mean length is costless. Reviewer cognitive/time burden is a legitimate planning constraint, but it should not be converted into an invented hard maximum.

Sources: TMLR `Author Guide`, `FAQ`, and reviewer guidance, accessed 2026-08-31.

### Nature Portfolio general writing guidance

Nature Portfolio's writing guidance emphasizes a focused, concise message, making each figure earn its place, defining technical terms only when needed, and using Supplementary Information for technical material that supports conclusions without being crucial to the main narrative.

Transfer: main-text allocation should prioritize message/evidence/reader understanding rather than repository completeness.

Source: Nature Portfolio, `How to write your paper`, accessed 2026-08-31.

## Derived design requirements

The evidence supports these general rules:

1. Resolve the exact target/article type/stage/date before applying length rules.
2. Track multiple budget currencies separately when the venue does: words, pages, figures/tables, references, legends, Methods, etc.
3. For page-constrained venues, inspect the rendered official template; do not infer final compliance from words.
4. Do not encode universal section percentages.
5. Use close analogue section proportions only as descriptive priors.
6. Protect reader prerequisites, decisive evidence/formal spine, and claim-changing interpretation/boundaries before secondary positioning or provenance detail.
7. Treat nearest-work/claim-subtraction analysis as broader internally than its manuscript footprint.
8. Treat every substantial revision addition as consuming finite budget; prefer replacement/reallocation over append-only growth.
9. Keep a deliberate but manuscript-specific revision reserve when hard limits apply.
10. Use appendix/SI/Methods as allocation valves, never to hide claim-changing evidence or definitions required to understand the main result.

## Transfer limits / unresolved points

- No universal Introduction/Methods/Results/Discussion percentage is supported.
- No universal reserve percentage is supported.
- TMLR's 12-page threshold is a review-timing boundary, not a publication-quality cutoff.
- A Nature print-equivalent word/display trade-off must not be copied to other journals.
- Page cost of equations, algorithms, tables and captions depends on the exact template and cannot be accurately converted from source text without rendering.
- Some fields/venues intentionally publish long theory, review, methods, or resource papers; brevity is not intrinsically better.
- Exact target rules can change and should be live-resolved when submission-critical.
