# `nature-citation` Skill

[中文说明](README.md)

`nature-citation` splits manuscript passages or scientific claims into citable units and finds **best-fit supporting evidence without a prestige-journal whitelist by default**. Explicit Nature / Science / Cell / CNS / flagship scopes remain available when the user actually requests them.

## What To Use It For

- Add supporting references to Introduction, Discussion, Methods rationale, reviewer responses, or individual scientific claims.
- Split long passages into stable claim units such as `S001` and `S002`.
- Search broadly for the best evidence by default rather than silently restricting results to Nature/Science/Cell.
- Explicitly restrict to `nature`, `science`, `cell`, `cns`, `flagship`, or another target scope when that is the actual task.
- Keep **evidence selection** separate from the **target journal's bibliography rendering**.
- Explain what part of a claim each candidate source supports and where support is incomplete or only adjacent.
- Export inspectable RIS by default and block records with missing/incomplete personal-author metadata before export.
- Retrieve structured author metadata by DOI/PMID while preserving order, given names/initials, suffixes, and collective authors.

## Typical Requests

- "Find the strongest evidence for each claim in this Introduction; don't filter by journal prestige."
- "For this sentence, prefer primary studies over reviews where possible and explain the support match."
- "Use only CNS-family papers from the last five years for this special comparison."
- "I confirmed these DOIs; export a Zotero/EndNote-ready RIS file."

## What You Need To Provide

- Passage, claim list, DOI list, or PMID list.
- Desired evidence scope: default `best-evidence`, or an explicit journal/family scope.
- Year range, whether reviews/guidelines/preprints are allowed, and discipline-specific evidence constraints when relevant.
- Export format such as `RIS`, `ENW`, or Zotero `RDF`.

## Outputs

- Claim-segmentation table and candidate-reference table.
- Suggested insertion point, DOI, journal, year, source type, and support note for each claim.
- Explicit evidence-mismatch warnings when a paper supports only part of a claim.
- Optional JSON/TSV/Markdown/HTML review material.
- Reference-manager export; RIS is the default.

## Boundaries

- Citation count or journal prestige is not treated as a universal evidence-quality score.
- A manuscript targeting Journal X does not imply citations should come only from Journal X.
- Candidate papers are support options, not guarantees of final citation suitability.
- Blogs, press releases, and search snippets are not used as sole scientific evidence.
- The skill does not strengthen a manuscript claim merely because a source uses stronger wording.

## Related Skills

- `nature-academic-search`: broader multi-source literature discovery, verification, citation metrics, and influential-citer analysis.
- `nature-ref-verifier`: verify selected bibliographic metadata and target rendering.
- `nature-writing`: integrate evidence and citations into the manuscript argument.
