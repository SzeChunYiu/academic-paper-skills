# Evidence note: standalone manuscripts and literature-version quality

Date: 2026-08-31

## Triggering failure class

Three full-paper outputs exposed a recurring boundary failure despite existing terminology, explanatory-sufficiency, artifact-leakage, and scholarly-surface contracts:

- paper-private experiment/version IDs were used as primary reader-facing nouns before adequate local definition;
- project-series and research-management vocabulary leaked into titles, Related Work, Results, limitations, and conclusions;
- claim-subtraction/donor/parent/ownership reasoning was surfaced instead of being translated into ordinary scholarly positioning;
- development histories were narrated as version chains even when only a smaller set of scientifically distinct studies mattered;
- data/code availability sections expanded into file manifests, hashes, internal paths, and reproduction commands;
- reference lists in fast-moving ML/AI areas were heavily preprint-weighted even where mature or formally published anchors could support background claims.

The repair is generalized as two distinct contracts: standalone-paper reader independence and literature version/source maturity.

## Reader-independence transfer logic

Existing repository rules already say that a paper is not a compressed repository, that internal labels require reader-facing scientific identities, and that central concepts require minimum sufficient explanation. The observed manuscripts show that these rules need an explicit reading-order and zero-context invariant.

The new contract therefore treats each manuscript as an independent public object. A qualified reader may be assumed to know the field, but not the project repository, paper-series chronology, experiment ledger, private codenames, terminal strings, claim-subtraction notes, or unpublished companion-paper ontology.

## Literature source evidence

### Crossref

Crossref's posted-content and versioning documentation explicitly distinguishes preprints from formal published versions and supports `isPreprintOf` / `hasPreprint` relationships. Crossref recommends associating a posted preprint with the later accepted/version-of-record DOI and records corrections/retractions as post-publication updates.

Relevant official documentation reviewed:

- `https://www.crossref.org/documentation/schema-library/markup-guide-record-types/posted-content-includes-preprints/`
- `https://www.crossref.org/documentation/principles-practices/best-practices/versioning/`
- `https://www.crossref.org/documentation/principles-practices/best-practices/relationships/`

### ICMJE

Current ICMJE recommendations state that when a preprint has subsequently been published in a peer-reviewed journal, authors should cite the subsequent published article whenever appropriate. ICMJE also recommends direct/original references where possible and notes that fewer key original papers can serve better than exhaustive reference lists.

Reviewed:

- `https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/overlapping-publications.html`
- `https://icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html`

This is biomedical guidance and is not transferred as a universal journal rule. Its version-of-record and anti-exhaustive-list principles are used as evidence for a broader source-quality contract, not as a mandate to force biomedical citation norms onto computing.

### ACM / computing boundary

Current ACM venue guidance reviewed for UIST explicitly recommends thoughtful related-work discussion rather than vague citation lists and prefers peer-reviewed citations, using arXiv sparingly for genuinely cutting-edge work not published elsewhere. Other ACM review criteria emphasize that prior work should be sufficient to interpret and assess the contribution rather than a list of work in the area.

Reviewed:

- `https://uist.acm.org/2026/author-guide/`
- `https://ci.acm.org/2025/review_criteria/`
- `https://icer2026.acm.org/track/icer-2026-papers`

Transfer limit: computer science conference proceedings are often primary peer-reviewed literature. The new contract therefore does not impose a journal-over-conference hierarchy.

### Nature / selective reference lists

Nature's formatting guidance uses a bounded reference budget for Articles, and Nature Methods has argued for thoughtful, streamlined reference lists that cite the most appropriate/original sources rather than prestige-driven or copied reference lists.

Reviewed:

- `https://www.nature.com/nature/for-authors/formatting-guide`
- `https://www.nature.com/articles/nmeth.4219`

Transfer limit: exact reference counts are venue-specific and are not generalized.

## Generalized conclusions

1. A manuscript can be globally consistent yet still fail local first-use comprehension.
2. A private experiment ID is not a scientific definition.
3. A research-management ontology should normally disappear during publication projection.
4. Claim subtraction is an internal novelty-control operation; the paper should present the resulting scholarly contrast.
5. Related Work is a rhetorical/scientific function, not a mandatory section or exhaustive inventory.
6. Search breadth and manuscript citation breadth are different. Internal search can be exhaustive while the manuscript is selective.
7. Open access/open source is not a weakness. Publication state, evidence role, version identity, and claim support are the relevant axes.
8. When the same work has a later formal peer-reviewed version, that version should normally become the canonical citation.
9. Preprints remain valid for genuinely frontier work and must be visibly labeled as preprints.
10. Internal/unpublished companion papers cannot be the hidden prerequisite for understanding an independently submitted paper.

## Guarantee boundary

These contracts reduce project-context leakage and publication-state bias. They cannot guarantee that every field-specific term is obvious to every reader or that every preprint-to-publication relationship is discoverable: relationship metadata can be incomplete, venues differ, and some fields use proceedings/books/standards as primary authorities. Contextual expert review remains necessary.
