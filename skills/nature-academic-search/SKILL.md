---
name: nature-academic-search
description: >-
  Venue-agnostic multi-source literature search, evidence discovery, citation verification,
  strict independent other-citation audits, article-level citation metric tables, influential
  citer profiling with citation-context extraction, MeSH search strategy, citation file
  management (.nbib/.ris/.bib conversion), and reference management (BibTeX, related articles,
  ID conversion) via scholarly sources such as PubMed, CrossRef/OpenAlex, arXiv, Scopus,
  ScienceDirect, proceedings indexes, and discipline-specific sources. The legacy skill name is
  retained for compatibility and does not imply a Nature-only search. Use for coordinated
  literature workflows beyond one API/MCP call, including 文献检索、查文献、找文献、文献综述检索、
  查论文、引文核对、参考文献管理、文献去重、严格他引、他引判定、排除自引、谁引用了我的文章、
  引用我的文章的人有没有大牛、院士引用、校长引用、院长引用、杰青引用、长江学者引用、
  Fellow引用、文章引用表、指定文章引用数、严格他引数、整理成表格.
---

# Venue-Agnostic Academic Search — Router

`nature-academic-search` is a legacy entry-point name. Do not infer a Nature, CNS, journal-only, or prestige-journal search constraint from it.

This skill is split into two layers:

- A **static layer** under `static/` holding the tool inventory and shared source-routing/operational rules.
- A **dynamic layer** (this file plus `manifest.yaml`) that detects the workflow and loads only that workflow, reaching for shared modules/scripts as needed.

## Routing protocol

### 1. Load the manifest and core layer

Read [manifest.yaml](manifest.yaml), then every file listed under `always_load`:

- `static/core/tools.md`
- `static/core/routing-and-ops.md`

### 2. Detect workflow(s)

Map the request to one or more values:

- `multi-source-search` — find literature across appropriate sources.
- `citation-verification` — verify citations extracted from a document.
- `mesh-strategy` — build a MeSH/PubMed search strategy.
- `citation-file-mgmt` — convert/manage `.nbib`/`.ris`/`.bib` files.
- `reference-mgmt` — BibTeX, related-article discovery, identifier conversion.
- `strict-other-citation-impact-audit` — determine strict independent other-citations, build article-level citation metric tables, identify high-profile citers, and extract citation context.

A combined request may need several workflows. State material scope/filter assumptions when they affect what gets retrieved.

### 3. Resolve the publication ecology before source selection

Do not assume every discipline's primary scholarship is a DOI journal article.

- biomedical/clinical -> journals, systematic reviews/guidelines, registries where relevant
- engineering/computer science -> journals **and proceedings/conferences**; standards/software/data may also matter
- physics/math -> journals plus preprints/discipline indexes where appropriate
- social science -> journal articles, working papers/preprints, books/chapters depending field
- humanities -> monographs, chapters, archives, primary editions and journal scholarship
- law/policy -> cases, statutes/regulations, official reports and scholarship
- Chinese scholarship -> CNKI/万方 and field-specific sources where needed

If the task is about evidence for a claim, journal prestige is not a ranking criterion. If the user explicitly asks for an exact journal/family corpus, apply that filter and report it.

### 4. Load only the matching workflow fragment(s)

Read the mapped workflow files under `references/workflows/`. Do **not** read all workflows. Each workflow links to shared modules it needs.

For query construction, source selection, and evidence ranking, load `references/search-strategy.md`. Its default is evidence/fit-aware and explicitly separates a journal filter from evidence quality.

### 5. Run the workflow

Apply:

1. Core tools/source routing — choose sources appropriate to field and source type; continue after individual provider failures.
2. Workflow-specific steps.
3. Search strategy — atomic concepts, synonyms, layered discovery/verification/evidence reading.
4. Shared modules/scripts on demand — deduplication, citation parser, format conversion, BibTeX/RIS handling.
5. Evidence or impact ranking appropriate to the user's question.

Do not use citation count as a universal evidence score. Use citation weighting only when influence/history/impact is itself part of the question.

For systematic/scoping reviews, preserve reproducible database/query/date/filter provenance and use explicit inclusion/exclusion criteria rather than an arbitrary relevance/recency/citation formula.

For claim-support searches, inspect the paper/abstract/primary source before calling it support and actively surface contradictory or limiting literature when material.

### 6. Reach for references only when needed

Use `manifest.yaml`'s `references.on_demand`, including:

- `references/source-tiers.md` — detailed source reliability/fallback notes
- `references/search-strategy.md` — domain/source selection and evidence-fit ranking
- `references/dedup-engine.md` — deduplication across sources
- `references/citation-parser.md` — extracting references from documents
- `references/ris-bibtex-format.md` — reference formats
- `scripts/academic_search.py` — no-MCP OpenAlex discovery fallback
- `scripts/format-converter.py` — DOI/PMID/arXiv export/conversion
- `scripts/preflight.py` — endpoint preflight

If a named target journal matters for **submission formatting** rather than literature scope, route that question to the shared journal resolver (`../nature-shared/journal-formats/journal-resolution.md`) instead of filtering the search.

## Output principles

Always make the search auditable enough for the task:

- sources searched
- queries/filters/date when reproducibility matters
- explicit journal/family restrictions, if any
- identifiers and duplicate handling
- source type (primary study/review/guideline/proceeding/book/etc.)
- whether support was actually read/verified or is metadata-only
- important gaps, contradictions, or provider failures

## Generalization rules

Never:

- treat Nature/CNS membership as evidence quality
- discard conference proceedings solely because they are not journals
- force humanities/legal scholarship into a biomedical source model
- use a target journal as an automatic evidence-source filter
- replace systematic-review screening/risk-of-bias logic with citation counts

Existing `nature-*` naming remains for compatibility; behavior is venue-agnostic unless the user supplies a venue restriction.
