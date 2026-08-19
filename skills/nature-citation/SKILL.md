---
name: nature-citation
description: >-
  Add defensible citations to academic manuscript text by splitting long passages into citable
  claims, searching the best relevant scholarly evidence by default, evaluating support
  conservatively, validating structured bibliographic metadata, and exporting reference-manager
  files. The legacy skill name is retained for compatibility: general citation requests are NOT
  restricted to Nature/Science/Cell. Explicit Nature Portfolio, Science-family, Cell Press, CNS,
  or flagship-only filters remain available when requested. Target-journal bibliography style is
  resolved separately from evidence selection. Use whenever the user asks to add references to a
  paragraph/manuscript, find sources/literature for a claim, build text-to-reference correspondence,
  create a reference list, search Nature-series/CNS support explicitly, or export EndNote/RIS/Zotero
  RDF. Trigger on academic-writing citation needs, 支撑文献、补引用、找引用、自动给出引用、分段引用、
  学术写作引用、写论文加引用、写paper找文献、加参考文献、配文献、引用文献、文献支撑.
metadata:
  author: Yuan1z skill, refactored into static/dynamic layers
---

# Evidence-First Academic Citation — Router

`nature-citation` is a legacy entry-point name. Do not infer a Nature/CNS search restriction from the skill name.

This skill is split into two layers:

- A **static layer** under `static/` that holds versioned core principles, Chinese-user behavior, and the claim-to-citation workflow.
- A **dynamic layer** (this file plus `manifest.yaml`) that chooses the runtime search route and reaches for heavier references only when needed.

## Routing protocol

Follow these five steps every time the skill is invoked.

### 1. Load the manifest and core layer

Read [manifest.yaml](manifest.yaml). Then read every file listed under `always_load`:

- `static/core/principles.md` — evidence scope versus rendering style, source hierarchy, support grading, metadata integrity.
- `static/core/chinese-mode.md` — Chinese-language operating behavior.
- `static/core/workflow.md` — the end-to-end citation workflow.

### 2. Resolve evidence scope independently from citation style

Decide **evidence scope** first.

Default to `best-evidence` for general requests such as:

- add references/citations to this paragraph
- find literature supporting this claim
- write a paper and add citations
- `支撑文献` / `补引用` / `找引用` / `加参考文献`

`best-evidence` means: search appropriate scholarly venues without a Nature/Science/Cell prestige filter and rank by direct evidentiary fit, source type, methods/study quality, claim boundary, and recency where relevant.

Use an explicit restricted scope only when the user asks for it:

- `nature` — Nature Portfolio
- `science` — AAAS Science family
- `cell` — Cell Press
- `cns` — Nature Portfolio + AAAS Science family + Cell Press
- `flagship` — Nature + Science + Cell only
- exact journal(s) — only when the user specifically requests same-journal or journal-filtered sources

A manuscript targeting a particular journal does **not** imply that supporting literature should come only from that journal.

Then resolve **citation rendering style** separately when needed. A target journal may require numeric, superscript, author-date, notes/bibliography, or a specific reference-manager/CSL style. If submission-ready formatting matters, load `../nature-shared/journal-formats/journal-resolution.md` and check the exact current target-journal guide/style.

State material search restrictions to the user; do not hide them.

### 3. Choose the search route

#### General/default citation request

Use `scripts/academic_citation_search.py` with `--scope best-evidence`.

This route reuses the legacy script's mature Crossref, structured-author, deduplication, and RIS/ENW/Zotero RDF helpers without applying its CNS-family whitelist.

When Crossref journal metadata is insufficient, expand to discipline-appropriate sources. Examples include PubMed/NCBI for biomedical work, conference/proceedings indexes for engineering and computer science, and books/archives/primary legal or humanities sources where those are the right evidence types.

#### Explicit Nature/Science/Cell-family request

Use `scripts/nature_citation.py` or the new wrapper with the requested restricted `--scope`. The legacy script remains useful for its family whitelist, DOI/PMID enrichment, batch checkpoints, exports, and optional HTML browser.

#### Long input

For more than about 10 citable segments, process in batches while preserving stable segment IDs and one final mapping. Use the legacy long-article artifact workflow when HTML/TSV/JSON browsing is useful; otherwise batch the general route.

### 4. Run the claim-to-evidence workflow

Follow `static/core/workflow.md`:

1. segment into atomic citable claims
2. parse claim type, entities, population/model, direction, and boundary
3. select appropriate source types and search queries
4. discover candidates under the resolved evidence scope
5. inspect abstract/full text or primary records and assign support grades conservatively
6. validate complete structured author/bibliographic metadata
7. export metadata and, if requested, render the exact target citation style separately

Never present a paper as support merely because the title looks related. Never promote a `metadata-only candidate` to evidence without checking its abstract/full text or equivalent primary record.

Actively surface contradictory or limiting evidence for high-stakes, contested, or overbroad claims.

### 5. Reach for references only when needed

Open on demand per `manifest.yaml`:

- general journal-agnostic script -> `scripts/academic_citation_search.py`
- legacy family scope/full flag list/HTML artifacts -> `references/script-usage.md` and `scripts/nature_citation.py`
- search-query design and support grading -> `references/search-strategy.md`
- explicit Nature/CNS family boundaries -> `references/journal-scope.md`
- RIS/EndNote/Zotero RDF details -> `references/ris-endnote.md`
- named target journal/style -> `../nature-shared/journal-formats/journal-resolution.md`; add `journal-family-profiles.md` only as fallback context

## Output contract

A normal report should make four things distinguishable:

1. **Search scope and sources** — `best-evidence` or explicit restrictions, date/study-type filters, databases searched.
2. **Claim-to-source mapping** — each source segment, candidate, source type, identifier, support grade, and insertion point.
3. **Metadata/export** — RIS/ENW/Zotero RDF if requested, with author-integrity warnings surfaced.
4. **Target rendering/compliance** — exact journal/style used, or `unresolved` if the final bibliography style was not requested/verified.

If a restricted family search produces weak or no direct evidence, say so and keep stronger broader evidence in a separate optional set rather than lowering the support threshold.

## Why this split

- Evidence quality and journal prestige are no longer conflated.
- Existing CNS/Nature workflows remain backward-compatible when explicitly requested.
- General academic users can cite the strongest field-appropriate work rather than only three publisher families.
- Reference-manager metadata stays complete and reusable across journal transfers; final house style can be regenerated for a new target without repeating evidence discovery.
