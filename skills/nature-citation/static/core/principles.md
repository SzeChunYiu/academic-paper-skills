# Core principles (citation)

Use this skill to turn manuscript text into a defensible citation workflow:

- segmented text with citation candidates for each citable claim
- conservative evidence notes explaining whether each candidate truly supports the claim
- complete structured metadata suitable for a reference manager
- optional journal/style-specific bibliography rendering after evidence selection

The legacy skill name is retained for compatibility. It does **not** imply a Nature-only evidence search.

## Separate two independent decisions

### 1. Evidence scope

Default: `best-evidence`.

Search the scholarly literature without a prestige/publisher filter and rank papers by direct support for the claim, study design, methodological quality, relevance to the population/model and outcome, recency when time sensitivity matters, and the role the source will play (primary evidence versus review/background).

Do not use journal prestige as a proxy for evidentiary strength.

Optional scopes are allowed only when the user requests them or the task itself makes them necessary:

- `Nature系列`: Nature Portfolio
- `Science系列`: AAAS Science family
- `Cell Press`: Cell Press
- `CNS` / `CNS及其子刊`: Nature Portfolio + AAAS Science family + Cell Press
- `只要Nature/Science/Cell正刊`: flagship-only
- exact named journal or set of journals
- explicit date range, study type, open-access requirement, primary-research-only, review-only, etc.

If the user asks generally for “references”, “supporting papers”, “citations for this paragraph”, or “文献支撑/补引用”, use `best-evidence`; never silently restrict to CNS.

### 2. Citation rendering style

Citation rendering is a later step. The target journal may require numeric, superscript, author-date, notes/bibliography, abbreviated journal names, a particular author truncation rule, or a reference-manager style.

Resolve exact formatting from the target journal/current style guide when the user asks for submission-ready references. Do not alter which papers count as good evidence merely to match the target journal.

Keep machine-readable metadata complete even when the rendered bibliography abbreviates it.

When a named target journal is involved, use `../../../nature-shared/journal-formats/journal-resolution.md` to distinguish evidence selection, reporting requirements, house style, and submission mechanics.

## Search routes

### General/default route

Use `scripts/academic_citation_search.py --scope best-evidence` for broad scholarly discovery. It reuses the mature Crossref/PubMed metadata/export helpers from the legacy script without applying the CNS-family filter.

### Explicit prestige/family route

Use `scripts/nature_citation.py` or `academic_citation_search.py` with an explicit `nature`, `science`, `cell`, `cns`, or `flagship` scope only when the user asks for that restriction.

A journal filter and a target citation style are different concepts. A manuscript targeting *Journal X* does not imply that all citations should come from *Journal X*.

## Source hierarchy

Use sources according to the information needed, not brand prestige:

1. Primary structured bibliographic metadata: Crossref, PubMed/NCBI E-utilities, DataCite when relevant, DOI metadata, and discipline-specific indexes.
2. Publisher/journal article pages for exact bibliographic facts, corrections/retractions, and accessible abstracts/full text.
3. Trusted full-text repositories and indexing databases appropriate to the field.
4. Discovery systems such as Google Scholar, Semantic Scholar, Web of Science, Scopus, arXiv, SSRN, or domain repositories as appropriate; verify critical metadata/evidence against primary records when possible.

For clinical/biomedical questions, prioritize databases and study designs appropriate to evidence synthesis rather than a general journal whitelist. For engineering/computing, conference proceedings may be primary literature and must not be discarded merely because they are not journal articles. For humanities/law, books, chapters, archival sources, cases/statutes, editions, or primary documents may be legitimate evidence even though the legacy Crossref journal script cannot retrieve all of them.

If metadata sources disagree, preserve stable identifiers and publisher/primary-record facts and flag the discrepancy.

## Search quality rules

- Prefer precision over volume. A useful answer is usually a small set of directly relevant sources plus explicit gaps.
- Split compound claims before searching; one paper rarely supports every clause of a long sentence.
- Use exact-phrase search only for distinctive terms; otherwise combine concepts and synonyms.
- Match source type to claim type. Reviews are useful for context; primary studies are preferable for specific experimental effects when available; guidelines or consensus statements may be appropriate for standards of care/practice.
- Check population/model, intervention/exposure, comparator, outcome, direction, and boundary before assigning support.
- Treat citation counts and journal reputation as tie-breakers at most, never as support evidence.
- Capture retractions, corrections, and expressions of concern when visible.
- Date-sensitive topics require current searching and an explicit search date.
- For medical, clinical, legal, or safety claims, use current authoritative evidence and state important uncertainty; a citation lookup is not a substitute for a systematic review or professional guidance.

## Support grading

Use these labels consistently:

- `strong support` — directly tests or establishes the relevant relationship under sufficiently matching conditions
- `partial support` — supports only part of the claim or a narrower/related setting
- `background support` — establishes context but not the specific asserted relationship
- `contradictory/limiting` — conflicts with or materially narrows the claim
- `metadata-only candidate` — title/metadata suggest relevance, but abstract/full text has not been checked

Never present a metadata-only candidate as evidentiary support.

## Metadata and export integrity

- Prefer DOI/PMID/other stable identifiers.
- Preserve complete ordered author metadata from structured sources.
- Do not invent missing volume, issue, pages, article number, publication date, or author names.
- Stop an “EndNote-ready” export when personal-author metadata is structurally incomplete unless the user deliberately accepts an override.
- RIS/ENW/Zotero RDF exports are metadata containers; they do not by themselves guarantee the final journal's bibliography punctuation/style.

## Source notes

This workflow uses public bibliographic APIs and official publisher/import documentation. Exact journal portfolios, submission rules, reference styles, and database behavior change over time; verify current official sources whenever coverage or submission compliance matters.
