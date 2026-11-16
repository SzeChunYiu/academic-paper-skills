# Mathematical exposition contract

> Shared writing/revision contract for **theory/proof (mathematics) manuscripts**. Its target is
> *checkability*: a specialist referee should be able to state the main results after reading
> the introduction, and verify each proof without reconstructing missing steps. It is the
> author-side counterpart of `mathematical-referee-review.md`.

Last reviewed: 2026-11-16.

## Contents

- [Scope](#scope)
- [Front matter](#front-matter)
- [Introduction architecture](#introduction-architecture)
- [Statements](#statements)
- [Proof architecture](#proof-architecture)
- [Conditional and computer-assisted results](#conditional-and-computer-assisted-results)
- [Literature and credit](#literature-and-credit)
- [Revision rules for a frozen-scope paper](#revision-rules-for-a-frozen-scope-paper)
- [Pre-submission checklist](#pre-submission-checklist)

## Scope

Activate with archetype G (`paper-archetype-atlas.md`). Field conventions differ: analysis, algebra,
combinatorics and logic differ in proof density and preferred layout. Research the target venue
and 3–6 recent close analogues (`unknown-paper-research-protocol.md`) before imposing any
convention below. These are defaults, not universal rules.

## Front matter

- **Title** names the object and the result type: "The Davenport constant of …", not a slogan.
- **Abstract** states the main results with their quantifiers and *all* conditions, in words a
  specialist can match against the theorem. It contains no citations unless the venue allows
  them. It contains no internal identifiers.
- **MSC 2020 classification** codes and keywords, when the venue asks for them.
- **Disclosure** of computer assistance and of AI assistance as the venue's policy requires.

## Introduction architecture

Default order; deviate only for a reason:

1. The problem and its history in a few paragraphs, with exact prior results.
2. **Main results stated precisely** as numbered theorems in the introduction. Restatements in
   the body must be verbatim, or cross-referenced as "Theorem 1.2 restated".
3. What is new, against the strongest prior results: new values, a new range, or a new method.
4. The idea of the proof in one or two paragraphs: the mechanism, not a table of contents.
5. The conditions, if any, and why they are there.
6. Organization of the paper.

## Statements

- One theorem-like environment per assertion. Every hypothesis is in the statement or in a
  clearly marked standing assumption.
- Exact values are stated as equalities, with the lower-bound construction and the upper-bound
  argument each identifiable.
- Conjectures, hypotheses and computational statements get their own environments and labels,
  so that every dependency on them is visible (`\begin{hypothesis}` or similar).
- Notation is introduced once, near first use, or in a notation section; it is never redefined
  silently.

## Proof architecture

- Long proofs get a roadmap: the steps, and which lemma does what.
- A lemma used once and short may be inlined; a lemma used several times is stated separately.
- Replace "clearly / obviously / it is easy to see" with the reason, or with a reference. Keep the
  word only when the step really is one line.
- Case analyses say why the cases are exhaustive.
- Each proof cites the exact earlier statement it uses (`\ref`), so that the dependency graph can
  be extracted (`audit_math_manuscript.py`).
- Forward references inside proofs are avoided. If unavoidable, they are marked and acyclic.

## Conditional and computer-assisted results

- A theorem that depends on an unproved input says so **in its statement**, by naming that input
  and labelling it. The abstract repeats the condition.
- Every computation used in a proof: the finite statement in the text; the reduction showing why
  it suffices; archived code, inputs and outputs with versions (arXiv ancillary files or a
  permanent repository); controls with known answers; and the independence status (one program,
  two programs, exact certificate, formal proof). Follow the target's policy (AMS 2017
  computer-assisted proof guidelines; LMS policy) where it applies.
- Agreement of programs is described as computational evidence, never as a proof, unless an exact
  certificate or formal verification is supplied.

## Literature and credit

- Cite the version of record. For preprints, cite the version read.
- Every "open", "new", "first" or "not in print" sentence has a search basis that the authors can
  produce. When it is uncertain, write "as far as we know", with what was searched.
- Credit special cases already in print explicitly, even when they weaken the novelty claim.
- Erroneous published claims are corrected with exact pointers (paper, statement number, page),
  in a neutral tone, and the authors of the original are informed when possible.

## Revision rules for a frozen-scope paper

When the project has frozen the paper's scope (no new results enter), a referee-driven revision
may:

- close gaps (the proof of an existing statement may grow);
- correct or narrow statements;
- add missing conditions to statements and abstract;
- improve exposition, notation and roadmap;
- update literature and credit;
- add one-paragraph remarks that follow from in-scope results without a new lemma.

It may not add new theorems that need new proofs. Those belong to the next paper. If a referee
asks for a new result, answer that it is outside this paper's scope, rather than letting the
scope creep.

## Pre-submission checklist

- [ ] `audit_math_manuscript.py` reports no errors; each remaining warning has a recorded reason.
- [ ] Every headline statement is identical in abstract, introduction and body (quantifiers,
      conditions).
- [ ] The dependency graph is acyclic; every unproved ancestor of a headline is named in its
      statement.
- [ ] Every computational input meets the five requirements of `mathematical-referee-review.md`.
- [ ] Novelty classification and search record exist for each headline result.
- [ ] At least two blind simulated referees report every headline proof `VERIFIED` or
      `VERIFIED_WITH_FIX` (fix applied).
- [ ] Compiles cleanly: no undefined references or citations, no overfull boxes in displayed
      mathematics that hide content.
- [ ] MSC codes, keywords, computer- and AI-assistance disclosure as the venue requires.
