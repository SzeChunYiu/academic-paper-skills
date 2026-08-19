# Journal-specific bibliography style audit

Use this reference when the user asks whether references are formatted correctly for a named journal/style, or when transferring a bibliography between journals.

Metadata verification and rendered-style verification are different tasks.

## Layer 1 — bibliographic identity

Run the normal `nature-ref-verifier` workflow first:

- DOI/PMID/ISBN/other identifier identity
- title
- ordered authors/editors
- venue/container
- year/date
- volume/issue
- pages/article number
- publication type/status
- correction/retraction signals when relevant

Do not “fix style” around incorrect metadata.

## Layer 2 — target rendering

Read:

- `../../nature-shared/journal-formats/journal-resolution.md`
- exact current target-journal author/reference instructions or an official/trusted CSL/BibTeX/reference-manager style when available

Resolve:

`exact journal -> article/content type -> stage -> reference component`

Then audit only the rendering rules actually supported by that target, such as:

- numeric versus author-date versus notes/bibliography
- in-text numbering/order or author-date syntax
- bibliography ordering
- author-name order and truncation / `et al.` threshold
- article-title capitalization and inclusion/omission
- journal full name versus approved abbreviation
- volume/issue/page/article-number punctuation
- year placement
- DOI/URL/PMID display
- preprint, dataset, software, conference, book/chapter, standard, patent, thesis, and web-reference forms
- access dates where applicable

Do not assume a publisher has one reference style across every journal.

## Source hierarchy for style

1. Exact current journal author guide or official journal template/style file.
2. Official publisher/society style linked from the exact journal.
3. Trusted current CSL/reference-manager style for the exact journal.
4. Family profile only to identify what to verify, never to invent punctuation.

If the journal says references may be submitted in any consistent style at initial submission, report that flexibility rather than reformatting unnecessarily.

## Journal transfer

When moving from journal A to B:

1. Preserve verified structured metadata.
2. Remove A-specific numbering/punctuation/abbreviations from the rendering layer.
3. Resolve B's exact current style.
4. Re-render from structured metadata rather than editing every reference string by hand when possible.
5. Re-check in-text citation/reference correspondence after renumbering or author-date conversion.
6. Verify special source types separately; journal articles are not the only reference class.

## Audit output

Separate:

- `metadata errors` — factually incorrect reference identity/fields
- `style errors` — correct metadata rendered against target rules
- `cross-link errors` — in-text citation missing from bibliography, uncited bibliography item, duplicate numbering, author-year ambiguity
- `unresolved` — target rule or source metadata cannot be verified

A bibliography can be metadata-correct but style-wrong, or style-consistent but metadata-wrong. Never collapse these categories.
