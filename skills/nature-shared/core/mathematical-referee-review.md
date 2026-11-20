# Mathematical referee review

> Shared contract for reviewing a **theory/proof (mathematics) manuscript** the way a careful
> mathematics referee does. It is used by blind reviewers inside the editor/reviewer simulation
> and by the pipeline's revision loop. It extends `atomic-claim-verification.md` (statement- and
> step-level verification) and `formal-spine-preservation.md` (keeping the formal object visible).
> It does not replace either.

Last reviewed: 2026-11-16.

## Contents

- [Purpose and scope](#purpose-and-scope)
- [Source basis and evidence grades](#source-basis-and-evidence-grades)
- [The four separated axes](#the-four-separated-axes)
- [Referee packet](#referee-packet)
- [Statement audit](#statement-audit)
- [Proof audit](#proof-audit)
- [Dependency and condition propagation](#dependency-and-condition-propagation)
- [Computer-assisted and computational inputs](#computer-assisted-and-computational-inputs)
- [Small-case falsification](#small-case-falsification)
- [Novelty and priority](#novelty-and-priority)
- [Severity calibration for mathematics](#severity-calibration-for-mathematics)
- [Mathematics referee report skeleton](#mathematics-referee-report-skeleton)
- [Recommendation vocabulary](#recommendation-vocabulary)
- [Convergence of the revision loop](#convergence-of-the-revision-loop)
- [Anti-gaming and honesty rules](#anti-gaming-and-honesty-rules)

## Purpose and scope

Activate when the dominant archetype is *G. Theory / proof / mathematical paper*
(`paper-archetype-atlas.md`), or when a theory-heavy hybrid makes a theorem a headline claim.

A mathematics paper is accepted mainly because its **main theorems are correct, new, and worth
stating**, and because a competent reader can **check** them in reasonable time. The review
therefore inverts the usual empirical order. Correctness of the stated results is the first gate.
Exposition is judged by whether it lets a reader verify. Significance is judged against the
literature, not against rhetoric.

## Source basis and evidence grades

Grades as in `acceptance-optimization-protocol.md`. Nothing here is a numeric acceptance
predictor.

- **D (official policy).** The American Mathematical Society *Guidelines for the Submission,
  Refereeing and Publication of Computer-Assisted Proofs* (approved 2017; ams.org). Experts must
  get enough detail to validate the proof, and independent researchers must be able to examine all
  relevant calculations. Code may be attached to the arXiv submission or to the online version.
  The full text was not re-read on 2026-11-16 (the page refused automated fetch); the summary
  comes from the search abstract and must be re-checked before it is quoted.
- **D (official policy).** The London Mathematical Society publications policy on computer-aided
  proofs. The body of the article states where and how the computation is used. Articles are
  reviewed to the usual standard. Code may not be verified line by line, but compliance with the
  policy is checked. The same caveat applies.
- **E (practice).** Refereeing large computer-assisted proofs (the Kepler/Flyspeck history) shows
  that human refereeing can stop at a confidence statement rather than certification. A
  confidence statement is not a certificate.
- **C (case study).** arXiv:2608.13067, *Computer-assisted proof under audit: typos, certificate
  errors and reproducible exact checks*. Published certificates can contain errors that only an
  independent exact re-check finds.
- **MANUSCRIPT_INTERNAL.** The manuscript, its cited sources, and its computational receipts are
  the only evidence about its own correctness.

Transfer limit: these sources set norms for disclosure and checkability. They do not tell a
referee that a particular proof is right.

## The four separated axes

Keep these as separate verdicts. Never let one stand in for another.

1. **Correctness.** Is every main statement proved, under exactly its stated hypotheses?
2. **Checkability / exposition.** Can a competent specialist verify the proofs from the text,
   cited results and supplied material in reasonable time?
3. **Novelty / priority.** Is each main result new? If it is not, is the new proof or the new
   range explicitly credited against the prior result?
4. **Significance / fit.** Is the result worth publishing in this venue? This axis is
   venue-relative (`venue-decision-contract.md`).

A beautiful exposition of a false lemma fails axis 1. A correct, new but unreadable proof fails
axis 2 and is repairable. A correct, readable, known result fails axis 3 unless it is presented
as a new proof.

## Referee packet

Each blind reviewer receives the same immutable packet:

- the full manuscript source (LaTeX preferred) and the compiled PDF if available;
- every cited unpublished input the paper depends on (preprints, theses, technical reports);
- for computer-assisted steps: the code, inputs, outputs, receipts or certificates, and the
  stated reproduction procedure;
- the deterministic audit output of `../scripts/audit_math_manuscript.py`. It is a locator, not a
  verdict. Reviewers must still read the proofs.

Reviewers do not receive the authors' internal audit history, earlier simulated reports or the
editor's synthesis (`adversarial-review-bias-control.md`).

## Statement audit

For every theorem-like statement (theorem, proposition, lemma, corollary, claim), record:

```text
statement_id            label or number in the manuscript
kind                    theorem / proposition / lemma / corollary / claim / conjecture / hypothesis
quantifiers             every variable with its range: "for all primes p >= 5", "for every K"
hypotheses              explicit; including standing assumptions inherited from a section
conclusion              the exact assertion, including equality vs inequality
conditional_on          named unproved hypotheses, conjectures, or computations it rests on
where_proved            section/lemma, external citation, or "not proved here"
restatements            every other place it is stated (abstract, intro, body, conclusion)
```

Checks:

1. **Restatement identity.** Abstract, introduction and body versions of a headline theorem
   assert the same quantifiers, hypotheses and conclusion. A condition present in the body but
   missing from the abstract is a **Major** concern, even if it is "obvious from context".
2. **Standing assumptions.** Every "throughout this section" assumption is recoverable at each
   statement that uses it.
3. **Edge cases of the quantifier range.** Check the smallest admissible parameters, degenerate
   cases (trivial group, rank 1, p = 2 or 3) and parity splits explicitly.
4. **Equality claims need both bounds.** For an exact value, locate the lower-bound construction
   and the upper-bound proof separately.
5. **Status words.** "We prove", "we show", "it follows", "conjecturally", "computationally"
   match what is actually established.

## Proof audit

Read every proof that supports a headline statement line by line. For supporting lemmas, read
them line by line unless the reviewer's preassigned emphasis says otherwise, and say which ones
were not read.

For each proof step check:

- **Cited results:** the hypotheses of the cited lemma are met *exactly*. This includes version,
  numbering, field characteristic, finiteness, rank and indexing conventions. A citation to a
  preprint states which version.
- **Quantifier order and selection:** "there exists a factorization" is not "for every
  factorization". Selected objects are not silently universalized.
- **Case splits:** cases are exhaustive and the reason they are exhaustive is written down.
- **Induction:** the base case, the measure that decreases, and that the induction hypothesis is
  applied only to smaller instances.
- **Hand-waving markers:** "clearly", "obviously", "it is easy to see", "similarly", "the same
  argument shows", "routine" are points to verify, not to accept. Where verification takes more
  than a few lines, ask for the lines.
- **Notation drift:** the same symbol keeps the same meaning; overloaded symbols are flagged.
- **Arithmetic and constants:** recompute every displayed numerical identity, bound and count.

Record each proof as `VERIFIED`, `VERIFIED_WITH_FIX` (gap closable from the text, with the fix
written out), `GAP` (a step that does not follow and whose closure is not evident), or
`NOT_READ` (with reason). A `GAP` in a headline proof is a Blocking Major concern.

## Dependency and condition propagation

Build the result dependency graph: an edge from A to B when the proof of A uses B.

- **Cycles** are Blocking unless the paper proves a joint statement by simultaneous induction
  and says so.
- **Forward references in proofs** (a proof citing a result stated later) must not create a
  cycle; flag them for explicit check.
- **Condition propagation:** if any ancestor of a headline theorem is a conjecture, hypothesis,
  unreceipted computation or unpublished external claim, the headline statement must name that
  condition (in body *and* abstract), or the paper must give an unconditional proof. A silent
  condition is Blocking.
- **External unpublished inputs** (preprints, theses, unpublished computations) are listed with
  their status. A conclusion that rests on them inherits their status.

`audit_math_manuscript.py` extracts a conservative version of this graph from `\ref`/`\cref`
usage inside proof environments. The reviewer confirms or corrects it.

## Computer-assisted and computational inputs

A computation used in a proof needs all five of the following; if one is missing, that is a
Major concern:

1. **The exact finite statement** that is checked, stated in the paper itself (not only in the
   code).
2. **Why the finite check implies the mathematical step**: the reduction and its completeness.
3. **Availability:** code, inputs and outputs are archived (arXiv ancillary files or a permanent
   repository), with versions and checksums.
4. **Independent confirmation** where feasible: a second, separately written program, an exact
   certificate checkable by a simple verifier, or a formal proof. Agreement of two programs
   is evidence, not proof. The paper says which it is.
5. **Known-answer controls:** smaller cases with known answers, run by the same code.

A computational step without (1)–(3) makes the theorem conditional on that computation. The
statement must then say so (see condition propagation).

## Small-case falsification

Before accepting an inequality or an exact value, test it on the smallest cases the reviewer can
compute by hand or from published tables. Write down the instances tried. A single verified
counterexample decides axis 1 against the statement, whatever its exposition. Do not run
unreviewed code in place of reading the proof. Hand checks and published tables are the default.
Any machine check the reviewer relies on is itself disclosed as such.

## Novelty and priority

- Search arXiv, zbMATH Open and MathSciNet (when accessible) and the standard monographs of the
  area. Record the search strings, dates and what could not be accessed.
- For each headline result classify it as: `new`, `new range of a known result`, `new proof of a
  known result`, `known` (cite), or `unresolved` (search incomplete).
- Classify recent preprints as unrefereed, and record their versions.
- An unsupported literature claim, in either direction ("open in print", "first", or "follows
  from [X]"), is a Major concern until a source is given.
- Priority statements in the paper itself are checked like theorems.

## Severity calibration for mathematics

| Finding | Severity |
|---|---|
| False headline statement, or a headline proof with a `GAP` | Major, Blocking |
| Silent condition (a headline depends on an unproved input not named in its statement) | Major, Blocking |
| Cited lemma used outside its hypotheses, fix not evident | Major, Blocking |
| Cited lemma used outside its hypotheses, fix written out by the reviewer | Major, not blocking |
| Computational step missing statement, reduction or availability | Major |
| Abstract/intro statement differs from the body statement | Major |
| Novelty claim unsupported, or prior result not credited | Major |
| "Clearly"-type step needing more than a few lines | Minor (Major if it hides a headline step) |
| Notation drift, undefined symbol, typo in a formula that a reader can repair | Minor |
| Exposition order, missing roadmap, overlong routine verifications | Minor |

Minor comments are never blocking (`editor-reviewer-decision-engine.md`).

## Mathematics referee report skeleton

```text
1. Summary of the claimed results (the referee's own words, with exact statements).
2. Correctness
   2.1 Proofs read and verdicts (VERIFIED / VERIFIED_WITH_FIX / GAP / NOT_READ with reasons)
   2.2 Small cases checked
   2.3 Dependency/conditions: what each headline result rests on
   2.4 Computational inputs: compliance with the five requirements
3. Novelty and priority (searches done, classification per headline result)
4. Significance and fit for the target venue
5. Major concerns  (ID, location, why it matters, minimal repair, resolution test)
6. Minor comments  (location, fix)
7. Recommendation (vocabulary below) and what would change it
```

## Recommendation vocabulary

`accept`, `minor revision`, `major revision`, `reject (incorrect)`,
`reject (not new / out of scope)`, `cannot assess` (state what is missing). In this simulation a
reviewer's recommendation is advice to the simulated editor. It is never the editor's decision
and never a probability.

## Convergence of the revision loop

The pipeline's simulated editor (`academic-paper-iteration-pipeline.md`) declares a mathematics
manuscript `simulated_publication_ready_for_target` only when all of the following hold:

- every headline proof is `VERIFIED` or `VERIFIED_WITH_FIX`, with the fix applied, by **at least
  two** blind reviewers who read it, and no reviewer reports an open `GAP`;
- every condition of every headline statement is named in that statement, in the body and in
  the abstract;
- every computational input meets requirements 1–3, and the paper states its status under 4–5;
- novelty classification is complete for each headline result, or the unresolved searches are
  disclosed in the paper;
- the deterministic audit reports no errors (warnings may remain with a recorded reason).

Re-review after revision goes to the reviewer who raised each Major concern, with the concern ID
and its resolution test. A fixed `GAP` is re-read in full; a diff alone is not enough.

## Anti-gaming and honesty rules

- Do not soften a statement's conditions to make it look unconditional, or move a condition into
  a footnote.
- Do not delete a proof step a reviewer flagged in order to hide it. Close it or narrow the
  claim.
- Do not claim "new" without the search record. Do not drop a credit to a prior result because
  it weakens novelty.
- Simulated acceptance is not real acceptance. A paper ready under this contract still needs real
  referees.
