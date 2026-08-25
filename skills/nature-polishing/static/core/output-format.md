# Output format

## Final release gate

Before returning polished manuscript-facing prose, apply `../../../nature-shared/core/manuscript-surface-qa.md`.

For a full-paper polish, formal/theory claim, public-posting/submission-ready
deliverable, or any rewrite that changes scientific scope/strength, also apply
`../../../nature-shared/core/atomic-claim-verification.md`. Polishing cannot turn
an internally supported but unverified, unresolved, contradicted, blocked, or
unassessable assertion into verified content.

The final text must be checked for:

- leaked file/directory paths;
- script/notebook/config/output filenames;
- helper/class/function/module identifiers that should be scientific terms;
- CLI/developer/branch/PR/commit/CI residue;
- raw repository links outside designated availability/artifact text;
- punctuation/spacing defects;
- bracket/parenthesis balance;
- malformed figure references;
- range/minus/hyphen and unit-spacing issues that require target-aware review.

When plain-text/Markdown input is available, the conservative shared `audit_manuscript_surface.py` scanner may be used for mechanical warnings. Review findings in context; do not auto-delete legitimate accessions, gene/protein/variant identifiers, package names central to the method, equations or exact target-required text.

A polish is not complete when grammar is improved but project-artifact residue or obvious punctuation defects remain.

## Default output

1. The polished text as plain prose, not in a code block, **after the release gate**.
2. `Revision notes:` with `3-5` short bullets on major scientific-clarity/logic/style changes.
3. If the rewrite changed section logic, explanation depth, content placement or archetype-level evidence flow, say so explicitly.

If the user asks for side-by-side revision, provide:

- `Original`
- `Polished`
- `Why changed`

If any paragraph's structural/explanatory problem could not be fixed without inventing content, say so under `Revision notes:` instead of papering over it.

When the main-text discipline is triggered, add a compact
`Main-text discipline audit:` that identifies material kept, replaced,
compressed, relocated to SI/caption, or deleted; states which descriptive and
primary inferential quantities remain in the main text; and reports the
before/after word count. Do not bury the polished prose under the audit.

When artifact leakage was materially present, a short revision note may say that operational identifiers were translated/relocated, but do **not** reprint internal filenames/paths in the user-facing polished manuscript merely to document their removal unless the user explicitly requests an audit trail.
