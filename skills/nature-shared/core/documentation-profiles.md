# Maintained documentation profiles

Profile version: 1.1.0.

- [Resolve the document](#resolve-the-document-before-drafting)
- [Apply the existing loop](#apply-the-existing-loop-with-the-right-reader-contract)
- [Coordinate updates and review](#coordinate-updates-and-review)
- [Version and release binding](#version-and-release-binding)
- [Figures and homepage projections](#figures-mathematics-and-homepage-projections)
- [Sources and transfer limits](#sources-and-transfer-limits)

Use this contract for a research-operations manual, theory reference, or code/API manual.
It adapts the existing academic-paper pipeline to a non-journal reader task.
It does not create a second writing pipeline, a scientific acceptance authority,
or a new machine-verifiable readiness terminal.

## Resolve the document before drafting

Freeze document ID, reader, purpose, profile, owner, source authority and exact
dependency versions. Use one primary profile per volume and explicit chapter
roles when a volume combines explanation, reference, how-to guidance and tutorials.
Do not impose IMRaD, novelty, editorial prestige or journal word limits on a manual.
If a chapter makes a new scientific contribution or is prepared as a journal paper,
apply the ordinary scientific-mass and exact-venue gates to that claim/surface.

| Profile | Reader question and required content | Decisive checks |
|---|---|---|
| operations-manual | How does research enter, proceed, stop, recover and improve? Mission, lifecycle, authorities, roles, allocation, handoff, budgets, incident recovery, metascience and management principles | Trace each normative rule to its owner/version; distinguish proposed policy, implemented interface and witnessed operation; exercise documented procedures and failure paths |
| theory-reference | What mathematical objects, assumptions and evidence justify the method? Definitions, notation, derivations, theorem status, rival models, ML, simulator assumptions, strategies and empirical boundaries | Atomic proof/source checks, counterexamples and independent scrutiny; retain conjecture/exploratory/negative states; distinguish model validity, simulation verification and economic evidence |
| technical-reference | What does this code expose, require and guarantee at this version? Architecture, interfaces, schemas, commands, deployment, dependencies, invariants, tests and troubleshooting | Derive names/signatures from pinned source; execute safe examples; test errors, defaults, units, compatibility and actual integration boundaries |

These are writing profiles, not repository shelves or scientific verdicts.
A theory chapter cannot be promoted to accepted theory merely because its prose
is reviewed. An accurate description of an unimplemented protocol does not prove
deployment. Library, research and release decisions remain separate.

## Apply the existing loop with the right reader contract

1. Intake and freeze the actual source tree, governance rules, claims, references,
   evidence and exclusions. Reuse canonical material instead of duplicating proofs
   or creating a parallel current manual.
2. Create an atomic content/claim map: definitions, scientific claims, normative
   rules, implementation facts, numerical statements and availability claims.
   Validate warrants at their stated scope. Normative claims need an authority;
   observed claims need observations, not a policy document.
3. Plan chapter functions and prerequisites. Keep conceptual explanation separate
   from exact interface reference and goal-directed procedures where that helps
   the reader. Define terms before use and preserve formal assumptions.
4. Compose using the existing writing, explanation, source, formal and display
   contracts when applicable. Mark genuinely inapplicable journal-only criteria
   with a reason; do not relabel an unresolved criterion as inapplicable.
5. Audit with the profile-specific checks above and the ordinary atomic/source,
   terminology, numerical, cross-surface and rendered-artifact checks.
6. Obtain independent initial review from relevant scientific/operations/software
   expertise plus a fresh reader who attempts the documented task. Use mutually
   blind initial concerns where the existing review contract requires it.
7. Synthesize arguments, repair concrete concerns, preserve revision deltas and
   re-review affected claims. A positive reviewer vote or polished writing is
   never sufficient. Keep scientific and operational blockers separate.
8. Release only the exact reviewed source/PDF package under the binding below.
   If release evidence is unavailable, retain a clearly marked draft and next
   resolution test; do not claim the writing pipeline passed.

For technical and operations documentation, repository-relative paths, API names,
CLI commands, code examples, status enums and version identifiers are legitimate
reader-facing content when needed to use or inspect the system. Explain them
locally and check them against source. The manuscript artifact-leakage rule still
excludes private workstation paths, secrets, chat transcripts, irrelevant internal
history and unexplained identifiers. Do not remove a necessary command merely
to satisfy a manuscript-only heuristic. Scientific narrative still uses scientific
objects rather than unnecessary implementation trivia.

The zero-context reader test is profile-specific: a technical reader may be
required to install documented dependencies, but must not need the author's chat,
private files or undocumented environment. Record prerequisites explicitly.

## Coordinate updates and review

Parallel findings enter the existing change/review queue with stable claim or
section IDs, source/evidence revisions, affected dependencies and proposed edits.
An appointed editor reconciles overlapping terminology, assumptions and outcomes
on a named candidate. A session may propose freely; submitting an idea does not
grant authority to overwrite accepted text or another session's current edit.

Use dependency-aware delta review. Recheck every changed claim and its affected
definitions, proofs, figures, examples, summaries and cross-volume consumers.
Reuse a prior proof/review only when its exact claim, assumptions, evidence,
dependency fingerprints and applicable review policy remain valid; record the
reuse decision. An unchanged paragraph can still be invalidated by an upstream
change. Do not restart a full review merely because a new event arrived, and do
not infer unaffectedness from a clean textual diff. Independent final-artifact
coverage and release binding still apply to the rebuilt PDF.

The reviewer harness prepares the frozen packet, enforces access/identity and
conflict boundaries, records concerns and checks closure evidence. It does not
replace domain judgment or certify its own quality. Initial reviewers work from
the current candidate and necessary evidence without prior verdicts or author
reassurance; freeze their concerns before synthesis. Subsequent targeted review
receives the relevant delta and earlier concern IDs. Keep contributor lineage
across model switches, children and handoffs; neither role switching nor another
model name grants independent status. Authors cannot approve their own work.

Publish a compatible cross-volume release cut: an immutable manifest naming the
operations, theory and technical editions and their dependency hashes. Only the
affected volumes need new editions, but verify that every retained edition is
compatible with the cut. Update the current index after that cut passes; an
interrupted update must expose the old complete cut or an explicit incomplete
draft, never a mixture advertised as current. Preserve prior cuts and errata.

Measure substantive defect detection, false approvals, false blocks, valid novel
contributions, rework, review latency and total cost on held-out task families.
Compare the reviewer harness with a declared simpler review baseline under
matched information and budgets. Proposed rival frameworks and unconventional
methods remain admissible to investigation; stronger review applies to claimed
results and release. An always-refuse reviewer fails usefulness even if it never
approves a bad claim. Passing workflow checks alone cannot establish better review.

## Version and release binding

Maintain one canonical source authority per volume. TeX and PDF are a coupled
release: PDF bytes must derive from the named source and build environment,
and reviewer evidence must bind the final reader artifact. Markdown/README
summaries are projections with links and version labels, not competing authorities.

Record document ID/version, profile version, source commit and source-tree digest,
dependency pins, writing-pipeline repository/commit, build toolchain/command,
claim and concern ledgers, figure/data provenance, final PDF hash, reviewers,
visual QA and exact release artifacts. Do not place a self-hash inside its own
manifest. Record the manifest digest in the governing release record.

Reuse the host repository's immutable version/history/dependency policy.
A changed formal meaning, assumption, contract or conclusion requires the
corresponding substantive version bump and consumer invalidation. A typographic
patch still rebuilds/reviews affected surfaces and binds new bytes. Never replace
an accepted PDF silently, reuse an old review fingerprint for a rebuild, or name
an unreviewed branch `latest` as if it were a released edition.

Before a release claim, load `publication-release-integrity.md` and run the
existing `verify_publication_release.py` against the actual final package,
using its supported release state appropriate to the delivery route. Do not add
a fabricated `documentation_pass` status or substitute a custom schema checker.
A required current research-integrity ledger, independent final-PDF coverage and
every-page rendered QA must exist. Preserve the existing final human
visual/accessibility review obligation. An internal manual does not thereby
become an externally accepted paper.

A verifier PASS proves its bounded identity/ledger checks only. It does not
authenticate reviewer independence, prove scientific truth, establish a reproducible
build, run the documented software or demonstrate unattended operation. Retain
separate evidence for those properties and for the substantive writing loop.

## Figures, mathematics and homepage projections

Plan diagrams by reader question: lifecycle, ownership, dependency, data flow,
failure/recovery sequence and model assumptions. Use a consistent visual vocabulary,
legible final-size labels, restrained colour and accessible alternatives. Retain
editable diagram source and build/export configuration. Distinguish proposed and
observed paths in captions; never draw an unimplemented edge as a verified service.

Use plots only for a real measurement or explicitly labelled analytic/synthetic
illustration. Bind data, units, denominators, uncertainty, transforms and render
code. Do not invent performance curves or add a plot quota. Reuse the ordinary
scientific-display contracts for evidence-bearing figures.

Use LaTeX equations with defined symbols. For GitHub README projections, use
supported inline/block math and Mermaid fences; render-check the actual supported
syntax. For PDF, export diagrams to suitable vector artifacts or use a maintained
TeX backend. A browser-looking diagram is not proof the PDF export is legible.
Check every page, cross-reference, caption, clipping, font and accessibility issue.

Each homepage states repository purpose, boundaries, current entry point,
dependencies and links to the three canonical volumes with release status.
Keep generated indexes generated. Do not publish private repository details in
a public organization profile without an explicit visibility decision.
Avoid copying entire manuals into READMEs or creating a new folder for each session.

## Sources and transfer limits

- [Diataxis](https://diataxis.fr/) separates tutorial, how-to, reference and
  explanation by user need. Use this as a content-design aid, not a proof that
  four folders or four books are required.
- [Google developer documentation style](https://developers.google.com/style/)
  prioritizes project context and reader clarity; its editorial guidance is not
  a scientific-validation standard.
- [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
  and [diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
  document supported Markdown rendering, not PDF rendering or semantic validity.

These primary documentation sources were inspected on 2026-11-13. The profile
is an engineering adaptation of the existing pipeline; no measured improvement
in research quality, speed or publication acceptance is claimed.

