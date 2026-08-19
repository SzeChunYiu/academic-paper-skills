# Workflow

Run these seven steps for any citation job. The default evidence scope is `best-evidence`; Nature/Science/Cell restrictions are opt-in. For runs with more than about 10 segments, batch the work while preserving one final mapping.

## 1. Segment the text

- Split long text into citable segments. Prefer paragraph boundaries first, then sentence boundaries.
- Keep each segment focused on one citable idea when possible.
- Preserve original order and stable segment IDs such as `S001`, `S002`, `S003`.
- Skip obvious non-citable connective sentences unless the user asks to cite every sentence.
- Split compound claims when different clauses need different evidence.

Default segmentation rules: use blank lines as paragraph boundaries; if a paragraph is long or contains multiple claims, split into sentences or atomic claims; merge very short fragments into neighboring text unless they contain a distinct claim; keep section headings as labels rather than citable segments.

## 2. Parse each segment

For each citable segment:

- Extract the core claim in one sentence.
- Identify claim type: `mechanism`, `association`, `method`, `clinical`, `epidemiology`, `background`, `definition`, `benchmark`, `theory`, or `review-context`.
- Identify entities, intervention/exposure, comparator, outcome, population/model, directionality, and boundary where applicable.
- Decide what source type is appropriate: primary experiment, systematic review/meta-analysis, guideline, methods paper, conference paper, dataset/software paper, book/chapter, archival/primary source, etc.
- Convert the claim into 2-4 search queries: precise concept query, synonym query, broader context query, and a source-type/method query when useful.

If the claim is too broad, split it into citable subclaims rather than searching the whole sentence. For deeper help, open `references/search-strategy.md`.

## 3. Resolve evidence scope and search candidates

### Default — best evidence across appropriate scholarly venues

Unless the user explicitly asks for a journal/family restriction, use the journal-agnostic route:

```bash
python scripts/academic_citation_search.py \
  --text "PASTE MANUSCRIPT TEXT HERE" \
  --scope best-evidence \
  --per-query 8 \
  --pretty
```

The script searches Crossref journal metadata without applying a Nature/Science/Cell prestige filter and can export RIS/ENW/Zotero RDF. Its candidates still require abstract/full-text screening.

Use additional discipline-appropriate sources when needed. Examples:

- biomedical/clinical: PubMed/NCBI and evidence-synthesis databases
- engineering/computing: IEEE/ACM proceedings, Crossref, arXiv as discovery/preprint context, field indexes
- social science: Crossref, discipline databases, preprint/repository sources when appropriate
- humanities/law: books, chapters, archives, primary texts, cases/statutes, and specialized indexes; the Crossref journal script is not sufficient by itself

### Explicit restricted scope

If the user explicitly asks for Nature-series, Science-family, Cell Press, CNS, or flagship-only literature, use the legacy family route or the new wrapper with that scope:

```bash
python scripts/nature_citation.py \
  --text "PASTE MANUSCRIPT TEXT HERE" \
  --scope cns \
  --outdir /tmp/nature-citation \
  --format ris \
  --with-artifacts
```

or:

```bash
python scripts/academic_citation_search.py \
  --text "PASTE MANUSCRIPT TEXT HERE" \
  --scope cns \
  --pretty
```

Do not infer a restricted scope merely because the manuscript targets a prestigious journal.

### Named target journal

A target journal controls **rendering/compliance**, not normal evidence selection. Search only that journal when the user specifically asks for same-journal precedent, a journal corpus, or references from that journal.

## 4. Evaluate whether each paper supports the segment

Use a conservative support scale:

- `strong support`: the paper directly tests or establishes the same relationship/mechanism/method under sufficiently matching conditions.
- `partial support`: the paper supports part of the segment, a related model, or a narrower condition.
- `background support`: the paper supports field context, not the specific claim.
- `contradictory/limiting`: the paper conflicts with or narrows the claim.
- `metadata-only candidate`: title/metadata suggest relevance, but abstract/full text has not been checked.

Never cite a `metadata-only candidate` as support without checking the abstract, full text, or primary record. If a paper is a review, label it as review/context and avoid using it as the sole primary evidence for a specific experimental claim when direct studies are available.

For high-stakes or contested claims, actively search for contradictory and limiting evidence rather than only confirming papers.

## 5. Export complete reference metadata, then render style separately

Default reference-manager export may be RIS. ENW and Zotero RDF are also supported. Do not invent missing fields. If DOI, pages, volume, issue, or publication date are absent in verified metadata, leave them absent and flag the gap when it matters.

Before writing a reference-manager file, run the author-integrity gate:

- Use the complete ordered author list from structured Crossref, PubMed, or publisher metadata. Never derive `AU` fields from a display citation, an `et al.` string, or a surname-only list.
- Write one `AU` line per person in complete structured form and retain initials, suffixes, particles, and ordering supplied by the source.
- Encode consortium/institutional authors correctly for the selected export format.
- If any personal author lacks required structured metadata, refetch by DOI/PMID or compare against the publisher record before calling the export reference-manager-ready.
- Permit `--allow-incomplete-authors` only as an explicit override and retain warnings.

A metadata export is not the same as the final journal bibliography style.

If the user asks for submission-ready reference rendering, resolve the exact target journal/style using `../../../nature-shared/journal-formats/journal-resolution.md` and the current official journal guide or trusted CSL/BibTeX/reference-manager style. Keep evidence selection unchanged while transforming punctuation, numbering, abbreviation, author truncation, and ordering.

## 6. Optional review artifacts

For long or ambiguous runs, provide review artifacts that let the user inspect the claim-to-source mapping, queries, identifiers, support grades, contradictions, and unresolved evidence gaps. The legacy Nature/CNS script can generate HTML/TSV/JSON/report artifacts with `--with-artifacts`; general workflows may use its metadata/export helpers or equivalent review tables.

Do not hide source restrictions. A report should state whether the search used `best-evidence`, a family restriction, an exact-journal filter, or another constraint.

## 7. Report results

Unless the user asks for a different format, return a compact structure such as:

```text
检索范围
- evidence scope: best-evidence / explicit family / exact journal
- date/study-type/open-access filters: [...]
- searched sources: [...]

分段引用对应关系
S001: [source segment]
  - [Author, year, title, venue, DOI/PMID/URL]
  - source type: [primary/review/guideline/etc.]
  - 支撑等级: [strong/partial/background/limiting/metadata-only]
  - 插入建议: [after sentence / after clause]

导出/引用格式
- metadata export: [RIS/ENW/RDF if requested]
- target style: [resolved journal/style, or unresolved]

风险和缺口
- [missing full-text check, contradictory evidence, weak population match, no direct primary evidence, metadata gaps, etc.]
```

If no suitable paper exists under an explicit restricted scope, say so plainly and offer the best broader evidence separately rather than pretending the restriction produced adequate support.

If the default `best-evidence` search finds only weak or indirect support, recommend narrowing or rewriting the claim instead of upgrading the support grade because the papers are prestigious.
