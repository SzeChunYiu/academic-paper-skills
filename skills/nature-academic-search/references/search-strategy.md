# Search Strategy Guide

The legacy skill name does not imply a Nature or prestige-journal search. Start from the research question, the source type the question requires, and the field's actual publication ecology.

## 1. Convert the question into atomic concepts

1. Write the research question or claim in one sentence.
2. Separate population/system, intervention/exposure/input, comparator/baseline, outcome/phenomenon, method, and boundary when those concepts apply.
3. Split compound questions whose clauses could require different source sets.
4. Generate synonyms, abbreviations, historical terms, spelling variants, and controlled vocabulary.
5. Add study/source-type terms only when they improve precision rather than prematurely excluding evidence.

For biomedical topics, map concepts to MeSH where useful, but combine controlled vocabulary with title/abstract synonyms so new/unindexed terminology is not lost.

## 2. Select sources by discipline and evidence type

Do not force all scholarship through a journal-article/DOI model.

| Need | Strong starting sources | Important additions |
|---|---|---|
| Clinical/biomedical | PubMed/NCBI | systematic-review/guideline databases, registries, publisher full text |
| Molecular/life science | PubMed + Crossref/OpenAlex | bioRxiv for discovery/preprints, domain repositories |
| Engineering | Crossref/OpenAlex + IEEE/other field indexes | conference proceedings, standards, arXiv when relevant |
| Computer science | ACM/DBLP-like proceedings indexes, Crossref/OpenAlex | arXiv, Semantic Scholar, journal databases |
| Physics/math | arXiv + Crossref/OpenAlex | INSPIRE or discipline indexes where relevant |
| Social science | Crossref/OpenAlex + discipline databases | SSRN/OSF/preprints where appropriate, books/chapters |
| Humanities | library/book/article indexes | monographs, chapters, archives, primary editions |
| Law/policy | legal databases + official primary sources | cases, statutes, regulations, reports, scholarship |
| Chinese scholarship | CNKI/万方 and discipline sources | Crossref/PubMed where indexed |

A conference paper can be the primary archival source in computer science/engineering. A book can be primary scholarship in humanities. A guideline can be more appropriate than a high-impact experimental paper for a practice recommendation.

## 3. Construct queries

### General pattern

`(concept A synonyms) AND (concept B synonyms) AND optional boundary/source-type terms`

Use field qualifiers only where the database supports them. Start broad enough to discover terminology, then tighten.

### Biomedical example

`("disease"[MeSH Terms] OR disease[Title/Abstract]) AND ("intervention"[MeSH Terms] OR intervention[Title/Abstract])`

### Methods/benchmark example

`(method OR model-name) AND (benchmark OR dataset OR validation OR comparison)`

### Mechanism example

`(entity A synonyms) AND (entity B synonyms) AND (mechanism OR regulates OR mediates)`

### Humanities/source example

Search both the interpretive concept and the primary-source corpus/author/work; do not add biomedical-style study filters.

## 4. Search in layers

A robust search often uses three layers rather than one provider:

1. **Discovery** — broad database/index search to learn terminology and candidate records.
2. **Verification** — DOI/PMID/publisher/library/official primary record to confirm metadata and status.
3. **Evidence reading** — abstract/full text/primary source to establish what the work actually supports.

Search results and metadata are not evidence by themselves.

## 5. Result ranking

Do not use journal reputation as the default ranking function.

### Default ranking dimensions

Evaluate candidates on:

- direct relevance to the exact question/claim
- appropriate source/study design
- match to population/system, setting, method, outcome, and boundary
- methodological transparency/quality signals visible from the paper
- primary versus secondary evidence role
- recency when the field is time-sensitive
- correction/retraction/status signals
- accessibility of enough content to evaluate support

Citation count may be useful for identifying influential or foundational work, but it is not a support grade and disadvantages recent or niche work.

### Do not use arbitrary universal scores for systematic reviews

There is no defensible universal formula such as `0.5 relevance + 0.3 recency + 0.2 citations` for evidence synthesis. For systematic/scoping reviews, follow a protocol with reproducible inclusion/exclusion criteria and database-specific searches; do not replace screening/risk-of-bias assessment with a convenience score.

### Useful sort modes

- `relevance` — discovery default
- `recent` — when user asks for current literature; still screen relevance
- `influential` — citation-weighted only when impact/history is the question
- `foundational` — older seminal sources plus later validation/reassessment
- `evidence-fit` — preferred for claim support; manual/multi-factor screening rather than raw citation prestige

## 6. Journal scope awareness

A journal filter is a user constraint, not a quality heuristic.

Use an exact journal/publisher filter only for requests such as:

- “find papers in Nature Communications”
- “show prior work from this target journal”
- “build a journal corpus to study style/topic coverage”
- “CNS only”

Do not restrict a general literature review or citation-support task to Nature/Science/Cell merely because the manuscript targets a selective journal.

When the target journal matters for writing/submission style rather than evidence scope, use the shared journal resolver in `../../nature-shared/journal-formats/journal-resolution.md` instead of filtering literature.

## 7. Query quality checks

Before accepting the search:

- Can the query retrieve a known relevant paper/source?
- Are key synonyms/abbreviations represented?
- Are source-type filters excluding legitimate field outputs?
- Are date/language filters justified?
- Is the result set dominated by a neighboring concept because the query is underspecified?
- For a review, can another person reproduce the database, query, date, and filters?
- For claim support, did you inspect contradictory/limiting evidence as well as confirming papers?

## 8. Deduplication and provenance

See [Dedup Engine](dedup-engine.md) for cross-source deduplication. Preserve:

- source database
- exact query
- search date
- filters
- stable identifiers
- duplicate/merged provenance
- screening reason when a candidate is excluded from a formal review

This makes the result transferable across journals and auditable later.
