# Literature version and source quality contract

> Shared contract for choosing the right scholarly source and the right publication version for each manuscript claim. Last reviewed: 2026-08-31.

## Purpose

A literature search can be topically relevant yet still produce a weak scholarly reference set when it over-selects recent preprints, cites a preprint after a peer-reviewed version of record exists, relies on project-internal documents for external positioning, or lists many loosely related papers instead of the few sources needed to understand and evaluate the contribution.

The core invariant is:

> **Select sources by evidentiary role and publication state, and prefer the appropriate version of record when the same work has subsequently been peer reviewed and formally published.**

This is not a journal-prestige rule and it is not an open-access penalty.

Open-access journal articles, peer-reviewed conference proceedings, books, standards, datasets, software papers, and authoritative primary records may all be the best source for a claim. The problem is publication-state and evidence-role mismatch, not access model.

## 1. Separate relevance, authority, maturity, and version

For every candidate source, evaluate four independent dimensions:

```text
claim relevance
source/evidence authority for that claim
publication maturity / review state
version identity
```

A source can be highly relevant but still be a non-peer-reviewed preprint. A journal article can be peer reviewed but irrelevant to the exact claim. A famous venue does not repair a support mismatch.

## 2. Publication-state classes

Classify each manuscript-facing source as one of:

- `version_of_record` — formally published journal article or other canonical publisher version;
- `peer_reviewed_proceedings` — peer-reviewed conference/workshop paper where proceedings are a primary publication venue for the field;
- `accepted_or_in_press` — accepted by a named scholarly venue but final publication metadata may be incomplete;
- `preprint_only` — recognized preprint/repository version with no located peer-reviewed publication;
- `review_or_synthesis` — peer-reviewed review, meta-analysis, systematic review, consensus synthesis, or scholarly review article;
- `book_or_chapter` — scholarly monograph/chapter appropriate to the claim;
- `standard_or_official_primary_record` — standard, guideline, regulation, official technical specification, dataset record, trial registry, or other primary authority;
- `software_or_dataset_publication` — citable release/paper/record when the scientific claim is about the software/data object;
- `unpublished_or_internal` — project note, internal report, private manuscript, internal companion paper, or unaccepted submission;
- `other` — with an explicit justification.

Do not infer peer review from DOI presence alone.

## 3. Version-of-record preference

When a preprint has subsequently become a peer-reviewed published article, cite the published version whenever appropriate.

Use relationship metadata and primary records where available:

- Crossref `isPreprintOf` / `hasPreprint` relationships;
- Crossref/DOI title and author matching when relationship metadata is absent;
- DataCite related identifiers when relevant;
- PubMed/publisher pages in biomedical literature;
- conference/publisher proceedings pages for computing fields;
- the article's publisher page and DOI metadata.

### Why

The peer-reviewed version may contain:

- corrections;
- revised claims;
- changed analyses;
- additional limitations;
- different title/author metadata;
- final pagination/article number;
- post-publication corrections or retractions.

The preprint remains part of the scholarly history but is not automatically the best citation target once a later formal version exists.

### Legitimate exceptions

Keep/cite the preprint instead of, or alongside, the published version when the citation is specifically about:

- the historical timing/content of the preprint;
- content present in the preprint but removed or materially changed in the published article;
- a priority/history question for which the preprint date is scientifically relevant;
- a version comparison itself;
- a field-specific reason that is explicitly stated.

Record the reason.

## 4. Preprints are allowed, but must remain visibly preprints

A preprint is legitimate when:

- the work is genuinely recent and no peer-reviewed version was located;
- the claim specifically concerns a frontier result not yet formally published;
- the field commonly disseminates important results first through recognized preprint servers;
- no mature substitute supports the exact proposition.

When citing a preprint:

- label it as a preprint in the bibliography/output metadata;
- verify that no later peer-reviewed version is available at the time of manuscript release;
- avoid letting a preprint carry more authority than its content/review state permits;
- pair it with mature literature when the underlying principle is established and the preprint supplies only a recent extension.

Do not silently style a preprint as though it were a published journal article.

## 5. Mature-claim anchor rule

For an established or mature scientific principle, method family, or background claim, prefer at least one mature primary or authoritative scholarly anchor when available.

Examples:

- a foundational theorem -> original/canonical scholarly source or authoritative book;
- a mature methodology -> peer-reviewed methods paper/review/standard;
- a well-established field concept -> authoritative review, textbook/monograph, or key original work;
- a standard reporting/clinical practice claim -> current official guideline/consensus statement;
- a current benchmark/system result -> the actual benchmark/system publication, which may legitimately be a peer-reviewed conference paper.

A bibliography dominated by very recent preprints can still be correct for a frontier topic, but it should trigger a maturity audit when mature background claims are also being made.

Do not impose a numeric journal quota. Audit claim by claim.

## 6. Computing/ML conference boundary

In computer science and machine learning, top peer-reviewed conference proceedings can be primary literature and must not be downgraded merely because they are not journal articles.

The hierarchy is therefore **not**:

```text
journal > conference > preprint
```

in every field.

Use:

```text
peer-reviewed version appropriate to the field
> corresponding unreviewed preprint of the same work
```

when all else is equal.

If an arXiv posting corresponds to a peer-reviewed NeurIPS/ICML/ICLR/ACL/EMNLP/ACM/IEEE proceedings paper, prefer the proceedings version for ordinary scholarly citation unless the preprint-specific exception applies.

## 7. Open access is not a quality class

Do not treat `open source`, `open access`, or repository availability as evidence that a source is weak.

These are separate properties:

```text
accessibility / licence
publication state
peer-review state
evidence quality
claim relevance
```

A fully open Nature/Science/PLOS/ACM/IEEE article may be a strong version of record. A closed journal article may be weak evidence for the claim. A public repository record may be the authoritative source for a dataset or software release.

## 8. Internal project documents cannot substitute for external prior work

Project-internal papers, notes, claim ledgers, novelty audits, unpublished companion manuscripts, repository documents, and private reports may support provenance or internal reasoning.

They do **not** by themselves establish:

- field novelty;
- external priority;
- broad prior-art boundaries;
- a public scientific definition the reader is expected to know;
- independent replication;
- consensus.

If a companion work is unpublished/internal, the current paper must remain intelligible without it and external claims must be supported by citable public evidence or explicitly marked as unresolved.

If a companion paper is publicly available/accepted and directly relevant, cite it normally and restate the minimum context needed locally.

## 9. Reference lists should be selective but complete for interpretation

The goal is neither minimum citation count nor exhaustive citation inventory.

For each literature role ask:

- Which source is necessary to establish the research need?
- Which source is the closest conceptual or methodological parent/comparator?
- Which source establishes a mature background principle?
- Which contradictory/limiting source changes interpretation?
- Which source documents the exact method/system/data object used?

Do not add references merely because they were encountered during search.

Do not list every work in a neighboring family when a synthesis sentence plus a few representative/key sources communicates the relationship more clearly.

For dedicated Related Work sections, prefer conceptual synthesis over citation catalogues.

## 10. Original work versus reviews

Use review articles judiciously.

- Reviews/surveys are useful for broad context, field history, and efficient orientation.
- For a specific experimental result, algorithm, theorem, or method introduced by identifiable original work, cite the original work when available.
- A review may supplement but should not obscure credit to the primary source.
- Do not copy a review's reference list without inspecting the cited source that carries the manuscript claim.

## 11. Evidence-role ledger

For substantial literature work, maintain:

```text
claim_id
source_id
source_role: primary / review / background / standard / contradiction / comparator / data / software
publication_state
preprint_identifier_if_any
version_of_record_identifier_if_any
version_relation_status: verified / probable / not_found / not_applicable
full_text_or_primary_record_checked: yes / no
support_grade
status/correction/retraction_check
reason_if_preprint_retained
```

The ledger may remain internal unless the user requests it.

## 12. Version resolution procedure

Before finalizing a preprint citation:

1. Normalize title and author metadata.
2. Search Crossref/DOI/publisher metadata for the title and authors.
3. Inspect explicit `isPreprintOf` / `hasPreprint` relationships when available.
4. Check field-specific bibliographic sources when needed.
5. If a peer-reviewed version is found, compare whether it is the same scholarly work.
6. Replace the preprint citation with the formal version unless a documented exception applies.
7. Refresh correction/retraction/update status on the selected published record.

Do not assume that absence of relationship metadata proves no published version exists; metadata links can be incomplete.

## 13. Frontier-source audit

When a manuscript cites many recent preprints, classify why each is needed:

- exact recent system/method under discussion;
- closest unpublished competitor;
- current empirical observation with no published substitute;
- convenience citation for a mature principle.

The fourth category should normally be replaced by a mature source.

A preprint-heavy bibliography is therefore a **review signal**, not an automatic failure.

## 14. Journal/proceedings source diversity is role-driven

A healthy reference set may legitimately include:

- original peer-reviewed studies;
- conference proceedings;
- authoritative reviews;
- books/monographs;
- standards/guidelines;
- data/software publications;
- a small number of necessary preprints.

Do not diversify merely for appearance. Diversify when different source types are the appropriate authorities for different claims.

## 15. Search and ranking implications

Citation discovery should prefer candidates with:

- direct semantic relevance;
- appropriate study/source type;
- complete stable identifiers;
- peer-reviewed/formal publication state when a matching version exists;
- current non-retracted/non-withdrawn status;
- enough accessible evidence to verify support.

Metadata relevance is still discovery only. Publication maturity does not prove entailment.

When candidate A is a preprint and candidate B is the peer-reviewed version of the same work, candidate B should normally be the canonical bibliography entry.

## 16. Related-work writing implications

The literature search may be broad; the manuscript should be selective.

Internal search can examine dozens or hundreds of papers. The public Related Work/Introduction should contain only the subset needed to:

```text
orient the reader
locate the closest prior work
establish the unresolved question
credit key origins
expose important alternatives/limitations
```

Do not surface the search inventory as prose.

## 17. Release blockers

Do not call a manuscript reference set submission/publication ready while any of these remains true:

- a cited preprint has a located corresponding peer-reviewed version but the preprint is used without a reason;
- a preprint is presented as though it were peer reviewed;
- a mature claim is supported only by a recent preprint when an appropriate established source is readily available;
- project-internal unpublished material is the only authority for an external novelty/background claim;
- metadata-only candidates are cited as evidence without inspecting support;
- corrections/retractions that materially affect a cited claim remain unchecked;
- a reference catalogue overwhelms the paper without adding interpretive value;
- a close prior work that would materially change the novelty or interpretation is omitted.

## 18. Boundaries

This contract does not require:

- a minimum number of journal articles;
- replacing valid peer-reviewed conference papers with journals;
- avoiding arXiv entirely;
- closed-access sources;
- citing prestigious journals;
- exhaustive citation lists;
- replacing an authoritative standard/book/data record with an unrelated journal paper merely to satisfy a format preference.

It requires the right source, at the right scholarly version, for the right claim.

## Source basis

The maintained evidence basis includes:

- Crossref documentation on posted content, preprint relationships (`isPreprintOf` / `hasPreprint`), versioning, and post-publication updates;
- ICMJE recommendations that, when a preprint is subsequently published in a peer-reviewed journal, authors should cite the published article whenever appropriate, and that key original sources are often preferable to exhaustive reference lists;
- current ACM author/reviewer guidance emphasizing relevant prior work rather than vague citation lists and, in some venues, preference for peer-reviewed citations with arXiv used sparingly for genuinely cutting-edge unpublished work;
- Nature/Nature Methods guidance encouraging thoughtful, streamlined reference lists and citation of the most appropriate/original sources rather than prestige-driven or copied references.

Exact venue-specific requirements override generic presentation rules, but not source identity or claim-support integrity.
