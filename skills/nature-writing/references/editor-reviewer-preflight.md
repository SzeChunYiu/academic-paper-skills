# Editor/reviewer preflight for manuscript writing

> Use before submission, after a major rewrite, or when the user explicitly asks how to make a paper more likely to survive editorial and peer-review decisions.

## Contents

- [Principle](#principle)
- [Step 1 — resolve the decision objective](#step-1--resolve-the-decision-objective)
- [Step 2 — build the editor brief](#step-2--build-the-editor-brief)
- [Step 3 — build claim decision proofs](#step-3--build-claim-decision-proofs)
- [Step 4 — engineer the evidence sequence](#step-4--engineer-the-evidence-sequence)
- [Step 5 — simulate reviewer attacks](#step-5--simulate-reviewer-attacks)
- [Step 6 — repair by decision consequence](#step-6--repair-by-decision-consequence)
- [Step 7 — re-run from the top](#step-7--re-run-from-the-top)
- [Decision-critical manuscript locations](#decision-critical-manuscript-locations)
- [Acceptance-readiness output](#acceptance-readiness-output)
- [Anti-gaming rules](#anti-gaming-rules)

## Principle

Do not ask `How do I make this sound acceptable?`

Ask:

> `What would an editor/reviewer need to conclude from the evidence to move this manuscript forward, and is that conclusion currently easy to recover and scientifically warranted?`

Acceptance-readiness is a property of **fit + evidence + argument + reporting + clarity**, not rhetorical confidence alone.

Load:

- `../../nature-shared/core/editor-reviewer-decision-engine.md`;
- `../../nature-shared/journal-formats/journal-resolution.md`;
- `../../nature-shared/journal-formats/editorial-decision-profiles.md` when the exact target decision model needs fallback calibration;
- `paper-review.md` for the full manuscript audit.

## Step 1 — resolve the decision objective

Before changing prose, write:

```text
Exact journal/venue
Article type
Publication model
Hard scientific gates
Target-specific editorial priorities
Reviewer axes
Criteria not used by this target
```

Examples of incompatible models:

- broad-interest selective journal;
- field-advancement engineering journal;
- rigor-first record journal;
- clinical/policy-priority journal;
- evidence-assessment model;
- conference selection.

Do not optimize a paper for all of them simultaneously.

## Step 2 — build the editor brief

Create a compact **editor decision brief**:

### Question

What unresolved scientific/intellectual problem is this paper actually addressing?

### Answer

What does the paper establish/provide that was not established/provided before?

### Decisive evidence

What one or two evidence classes make that answer credible?

### Target-specific value

Which verified publication criterion does the contribution satisfy?

### Boundary

What does the paper explicitly not establish?

### Reader/community

Who needs this result/resource and what changes for them?

If the brief is vague, do not compensate with adjectives. Fix the manuscript argument or target choice.

## Step 3 — build claim decision proofs

For every claim that could determine the decision, build:

| Claim | Decision axis | Decisive evidence | Strongest alternative | Discriminating evidence | Boundary | Current status |
|---|---|---|---|---|---|---|

Headline claims include:

- title claim;
- abstract result/implication;
- final Introduction contribution claim;
- each major Results subsection claim;
- central Discussion interpretation;
- Conclusion claim.

### Decision-proof test

A claim is `closed` only if a skeptical qualified reader can trace it to enough evidence **without importing an unstated assumption**.

## Step 4 — engineer the evidence sequence

Do not order analyses by chronology or by how expensive they were.

Order them by **reviewer uncertainty reduction**:

`claim -> most important uncertainty -> evidence that resolves it -> next uncertainty -> next discriminating evidence`

For each transition ask:

- What doubt remains after the previous result?
- Why is the next analysis the cheapest convincing way to reduce that doubt?
- Does the manuscript state that reason?

### Strong evidence sequence patterns

Examples only:

- establish phenomenon -> discriminate mechanism -> external validation -> boundary/failure mode;
- benchmark main effect -> test fairness of comparison -> ablate claimed source -> stress/generalize;
- association -> sensitivity/confounding analysis -> negative control -> bounded interpretation;
- qualitative theme -> triangulating evidence -> negative/deviant case -> transferability boundary;
- theorem -> assumptions -> proof -> counterexample/boundary -> implication.

## Step 5 — simulate reviewer attacks

Before polishing, generate independent questions from at least three lenses:

### Lens A — validity

`What central claim can I falsify or weaken by pointing to design, data or analysis?`

### Lens B — positioning/decision value

`What is actually new/useful/important under this target's criteria, and is the distinction from prior work fair?`

### Lens C — reproducibility/boundary/readability

`What would stop me from trusting, reproducing, interpreting or correctly delimiting the result?`

For each likely concern write the **resolution test before writing the rebuttal**.

The purpose is not to predict a specific reviewer's personality. It is to expose decision-relevant scientific uncertainty.

## Step 6 — repair by decision consequence

Use this order:

### 1. Fatal target mismatch

If the work is scientifically sound but cannot satisfy a target-specific editorial criterion without exaggeration, change the target/article type.

### 2. Blocking central-evidence problem

Add/reanalyse decisive evidence or narrow the central claim.

### 3. Major repairable inference problem

Add a discriminating analysis/control/validation only if it resolves a real alternative interpretation.

### 4. Claim recalibration

Narrow or remove a claim whose evidence is good but scope is overstated.

### 5. Clarity/reporting problem

Move the existing evidence into a form reviewers can evaluate. If a reviewer would miss an existing control because it is buried, that is a manuscript problem.

### 6. Optional enrichment

Do not bloat the paper with experiments or discussion that do not affect publication criteria or central inference.

## Step 7 — re-run from the top

Every substantive repair can change:

- contribution scope;
- title/abstract claim;
- target fit;
- evidence sequence;
- Discussion implication;
- limitations;
- cover-letter positioning.

After critical/major edits, rebuild the editor brief and headline claim proofs rather than only patching local prose.

## Decision-critical manuscript locations

These locations deserve special alignment because they create the manuscript's evaluative contract.

### Title

Must not claim more than the strongest closed evidence supports.

### Abstract

Must make question/contribution/evidence/boundary recoverable under the target's genre rules. Do not let compressed wording increase causal/generalization strength.

### End of Introduction

Should state the actual response/contribution and evidence class, not a promise the Results cannot close.

### Figure 1 / first major Results block

Should orient the reader to the evidence architecture or establish the first decisive claim, depending on field/article type.

### Results subsection openings/closings

Make clear what uncertainty is being tested and what narrow conclusion is licensed.

### Discussion

Attach major limitations/alternatives to the claims they constrain. Do not postpone every caveat to a generic final paragraph.

### Conclusion

State the durable post-qualification answer.

### Cover letter

Use only target-specific value already supported by the manuscript. Do not create a second, more inflated scientific story for the editor.

## Acceptance-readiness output

Return:

### Editorial triage risks

- fit/scope;
- contribution clarity;
- target-specific priority/breadth/advancement;
- review readiness.

### Reviewer blockers

Rank by scientific decision consequence.

### Claim recalibration

Claims best solved by narrowing/removal rather than more work.

### Minimum decisive evidence

Only experiments/analyses that discriminate important alternatives.

### Manuscript engineering changes

Structural/clarity/reporting changes that expose existing evidence better.

### Optional / do not overbuild

Requests that would add cost/bloat without improving the decision-critical case.

### Transfer trigger

When another journal/article type is a better match for the scientifically honest contribution.

## Anti-gaming rules

Never use this preflight to:

- hide adverse evidence;
- omit competing papers;
- inflate novelty/significance;
- select friendly reviewers;
- cite likely reviewers strategically;
- add irrelevant reviewer citations for favor;
- bury decision-changing limitations;
- manufacture a broad-interest story unsupported by evidence;
- turn reviewer simulation into fake consensus.

The engineering target is a paper that remains convincing when evaluated by independent experts, not a paper that exploits the review system.
