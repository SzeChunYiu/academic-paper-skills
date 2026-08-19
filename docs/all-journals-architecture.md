# All-journals architecture

The repository keeps the historical `nature-*` skill names for compatibility, but the core academic workflows should not infer the target journal from those names.

## Design goal

Support arbitrary academic journals and venues without maintaining a brittle hard-coded list of thousands of titles.

The architecture separates:

1. scientific/evidence logic that should survive journal transfer
2. discipline/reporting obligations
3. journal-specific house style
4. submission/production mechanics

Exact journal rules are resolved at use time when needed.

## Shared journal resolver

`skills/nature-shared/journal-formats/journal-resolution.md` defines the common resolution tuple:

`exact journal -> article/content type -> submission stage -> output component`

Resolution priority:

1. current exact official journal instructions
2. exact versioned local profile when available
3. publisher/venue family fallback profile
4. discipline/reporting profile
5. generic scholarly default

The live exact guide is required for submission-critical numeric/mechanical rules.

## Family profiles

`skills/nature-shared/journal-formats/journal-family-profiles.md` provides fallback questions and writing/workflow context for:

- Nature Portfolio
- Science / AAAS
- Cell Press
- IEEE
- ACM
- PLOS
- Springer/BMC/SpringerOpen
- Elsevier
- Wiley and society journals
- APA-style social/behavioral venues
- medical/clinical reporting
- humanities/law

Family profiles are deliberately not universal submission contracts.

## Function changes

### Writing

`nature-writing` adds a `profiled` journal route for any named non-Nature target or journal transfer. It preserves exact Nature/Nature Communications/NMI profiles for compatibility while routing other journals through the shared resolver.

### Polishing

`nature-polishing` uses a two-pass model:

1. target-independent scientific edit
2. verified target-dependent adaptation

This prevents polishing from changing evidentiary strength merely to imitate a prestigious journal.

### Citation discovery

General citation requests now default to `best-evidence` instead of CNS-family filtering.

`scripts/academic_citation_search.py` reuses the legacy citation script's Crossref metadata parsing, author-integrity checks, deduplication, and RIS/ENW/Zotero export helpers but does not apply a prestige whitelist by default.

Explicit `nature`, `science`, `cell`, `cns`, and `flagship` scopes remain available.

Evidence selection and final bibliography rendering are separate. A manuscript targeting Journal X does not imply its citations should come only from Journal X.

### Academic search

The search strategy is publication-ecology aware: conference proceedings can be primary literature in computing/engineering; books and archives can be primary scholarship in humanities; guidelines can be appropriate evidence in clinical contexts. Citation count is not a universal evidence score.

### Figures

`nature-figure/references/journal-adaptation.md` resolves target/stage-specific figure mechanics independently from scientific design, including dimensions, formats/resolution, legends, source data, accessibility, graphical abstracts, and AI-image policy.

### Reference verification

Reference verification now distinguishes:

- bibliographic identity/metadata correctness
- target-journal rendering style
- in-text/reference cross-link correctness

Journal transfer should re-render from verified metadata instead of manually editing already-formatted strings when possible.

## Backward compatibility

This refactor does not rename the `nature-*` skill directories or entry-point names. Existing exact Nature-family profiles and legacy explicit CNS citation behavior remain available.

The compatibility rule is:

> legacy name does not imply legacy scope.

## Adding an exact journal profile later

Add an exact profile only when repeated use justifies maintaining it.

A profile should record:

- exact journal title
- reviewed date
- official source URLs/titles
- article/content types covered
- stage distinctions
- verified limits/mechanics
- known unresolved/conflicting rules

Then add a precise router value or exact-target branch without changing the generic resolver.

## Research basis reviewed 2026-08-19

The refactor was calibrated against current official author resources and journal examples from Nature Portfolio, AAAS/Science family, Cell Press, IEEE, ACM, PLOS, Springer/BMC, Elsevier, and Wiley. The common finding is that publisher family alone is not a sufficient submission contract: exact journal, article type, and stage matter.

Because publisher instructions change, the files in this repository are routing knowledge rather than permanent substitutes for the official target-journal guide.
