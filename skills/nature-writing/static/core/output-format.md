# Output format (writing)

## Final release gate before returning manuscript prose

Before returning any manuscript-facing `Draft:` text, run the final surface contract in `../../../nature-shared/core/manuscript-surface-qa.md`.

For a full manuscript, formal/theory section, public-posting/submission-ready
claim, or decision-relevant rewrite, first run
`../../../nature-shared/core/atomic-claim-verification.md`. Do not label the work
verification-complete or ready while any in-scope assertion is merely internally
supported, unresolved, contradicted, blocked, or not assessable.

This applies to:

- title/abstract/body prose;
- headings;
- figure callouts;
- complete figure legends/captions;
- table titles/notes;
- Methods wording;
- equations plus explanatory prose;
- Extended Data/SI prose when it is paper-facing;
- availability/declaration text.

### Artifact-leakage release check

The delivered manuscript text must not expose internal project details merely because they exist in source material or were used to generate a figure/result.

Scrub or contextually justify:

- file and directory paths;
- script/notebook/config/output filenames;
- helper function/class/module names;
- CLI commands/flags;
- branch/PR/issue/commit/CI/test history;
- temporary run/checkpoint identifiers;
- raw repository URLs outside the designated availability/artifact section.

Translate retained material into the scientific operation/entity wherever possible. Put authoritative code/data/resource access in its designated availability section. The **audit note** may name an internal artifact; the **manuscript prose must name the science**.

### Punctuation/copy-editing release check

After scientific meaning is stable, check:

- doubled/missing punctuation;
- punctuation spacing;
- bracket/parenthesis balance;
- malformed figure references;
- list parallelism;
- range dash versus minus versus compound hyphen;
- number/unit spacing;
- target-aware citation/equation/title/legend punctuation;
- accidental changes to identifiers, chemical/biological names, mathematical expressions or statistics.

When plain-text or Markdown manuscript material is available, `../../../nature-shared/scripts/audit_manuscript_surface.py` can provide a conservative mechanical warning pass. Review all findings in context; it is not an auto-rewriter.

Do not deliver prose with a known high-confidence leakage or punctuation defect simply because the scientific reasoning is correct.

## Default output

1. `Draft:` — the requested prose, after the final release gate.
2. `Section outline:` — `3-7` compact bullets when the task involves a full section.
3. `Assumptions or missing inputs:` — only material issues; do not pad with style nits.
4. `Claim-evidence map:` — for major claims, in the form:
   `Claim: ... | Evidence: ... | Status: supported / needs evidence / inferred`
   For full/formal/readiness work, summarize the atomic verification counts and
   list every fail-closed item instead of presenting a major-claim sample as
   complete coverage.
5. `Why this structure:` — `2-4` short bullets on the structural choices made.
6. `To redirect me:` — one line inviting targeted feedback, e.g. "Name the paragraph or claim that is off and I will revise only that, keeping the rest." This sets up the targeted revision loop instead of a full rewrite.

For Chinese-author notes, provide polished English first, then brief Chinese notes explaining major structural choices.

For a Results or full-main-text restructuring task, also include a compact
`Main-text discipline audit:` after the prose:

- result allocation: core / necessary support / qualification / SI-bound detail
- relocated, replaced, compressed, or deleted material
- primary statistic retained in the main text and secondary analyses routed to SI
- before/after word count for each revised subsection

For substantial full-paper planning/rewrite, maintain internally or expose when useful:

- dominant/secondary paper archetype;
- explanation-depth hotspots;
- content-allocation ledger;
- figure/plot suggestion ledger;
- final artifact-leakage findings and their resolution.

Return the full allocation, archetype, explanation and claim-repetition tables only when the manuscript is being comprehensively restructured or the user asks for the audit trail.

If essential evidence or a boundary is missing, do not invent it. Put a
placeholder such as `[Evidence needed: comparator group accuracy on test set X]`
only in the author-facing `Assumptions or missing inputs:` audit note. Do not
leave it inside final manuscript-facing `Draft:` prose, and never label that
scope ready until it is resolved, qualified, removed, or explicitly blocked.

For `task=submission-package`, replace the default manuscript format with:

1. `Submission readiness:`
2. `Deliverable matrix:`
3. `Draft materials:`
4. `AUTHOR_INPUT_NEEDED:`
5. `Cross-file consistency checks:`
6. `Next actions:`

Submission-facing prose still passes the relevant punctuation/identifier QA. Availability sections are allowed to contain the exact durable access identifiers required for submission.
