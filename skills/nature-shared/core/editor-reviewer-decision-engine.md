# Editor–reviewer decision engine

> Shared pre-submission decision model for writing, mock review, and revision workflows. Last reviewed: 2026-08-19.
>
> This file operationalizes public editorial/reviewer guidance. It does **not** claim that acceptance is predictable or controllable.

## Contents

- [Purpose](#purpose)
- [Ethical definition of acceptance engineering](#ethical-definition-of-acceptance-engineering)
- [The four decision stages](#the-four-decision-stages)
- [Decision proof for each headline claim](#decision-proof-for-each-headline-claim)
- [Editorial triage gate](#editorial-triage-gate)
- [External reviewer gate](#external-reviewer-gate)
- [Editor synthesis gate](#editor-synthesis-gate)
- [Revision-to-acceptance gate](#revision-to-acceptance-gate)
- [Concern severity and repair](#concern-severity-and-repair)
- [Decision-risk map](#decision-risk-map)
- [Reviewer-panel simulation](#reviewer-panel-simulation)
- [Anti-gaming rules](#anti-gaming-rules)
- [Source basis](#source-basis)

## Purpose

A manuscript is evaluated through several different questions. Do not collapse them into one score such as `quality`, `novelty`, or `acceptance probability`.

The reusable decision stack is:

`integrity/compliance -> editorial triage -> external review -> editorial synthesis -> revision closure`

Different journals weight these stages differently. Some selective journals screen heavily for priority, breadth, or field-changing significance before review. Some journals deliberately judge technical rigor without using perceived importance as a publication threshold. Some publication models separate significance from strength of evidence instead of reducing them to accept/reject.

Resolve the exact journal and article type before assigning weights.

## Ethical definition of acceptance engineering

**Acceptance engineering** means making a valid contribution easier to evaluate and harder to misunderstand by:

- matching the actual journal/article-type criteria;
- making the central question, answer, evidence and boundary explicit;
- supplying the discriminating evidence needed for the claims actually made;
- surfacing limitations before they become reviewer discoveries;
- making methods, analyses and provenance auditable;
- resolving contradictions and internal inconsistencies;
- removing claims that the design cannot establish;
- answering decision-relevant concerns completely during revision.

It does **not** mean gaming reviewers, exaggerating novelty, hiding limitations, strategically omitting competitors, flattering likely reviewers with citations, suggesting friendly reviewers to obtain favorable recommendations, or adding cosmetic experiments that do not discriminate between interpretations.

Optimize **decisionability and scientific credibility**, not persuasion independent of evidence.

## The four decision stages

### Stage 0 — integrity and compliance

Before editorial positioning, check for issues that can independently stop consideration:

- authorship/conflict disclosures;
- ethics/consent/registration where applicable;
- plagiarism/duplicate publication;
- image/data integrity;
- required data/code/material availability;
- required reporting standards;
- basic submission completeness.

These are not rhetorical problems. Fix or disclose them directly.

### Stage 1 — editorial triage

The handling editor asks a target-specific version of:

1. Is this in scope?
2. What is the paper's actual contribution?
3. Why does that contribution matter under this journal's publication model?
4. Is the manuscript mature enough to justify external-review cost?
5. Can the editor understand the question, evidence class, and claimed implication without reconstructing them from scattered details?
6. Are there obvious fatal fit, integrity, or evidentiary problems?

For selective broad-interest journals, priority/readership/significance can be independent gates from technical validity. For rigor-first journals, perceived importance may not be a publication gate at all.

### Stage 2 — external review

Reviewers primarily test whether the manuscript's **case is established**. Depending on venue and article type, they assess combinations of:

- validity and technical soundness;
- claim–evidence alignment;
- appropriateness of design/method/analysis;
- originality and relationship to prior work;
- significance or advancement when the journal asks them to assess it;
- data quality and interpretation;
- reproducibility/reporting completeness;
- ethical validity;
- clarity and logical presentation;
- limitations and alternative explanations.

A reviewer recommendation is evidence for the editor, not the decision itself.

### Stage 3 — editorial synthesis

The editor should be simulated as weighing **arguments and expertise**, not counting reviewer votes.

The synthesis asks:

- Which concerns map directly to publication criteria?
- Which concerns are technically blocking?
- Which are repairable without changing the central study?
- Which requests are useful but non-essential?
- Does one reviewer have special expertise relevant to a disputed technical point?
- Does the revised claim still meet the journal's target-specific significance/fit bar after necessary narrowing?
- Is the requested revision proportionate to the manuscript's remaining potential?

### Stage 4 — revision closure

A revision is not strong because the response letter is long. It is strong when every decision-relevant concern has a closure state:

- `resolved_by_evidence`;
- `resolved_by_analysis`;
- `resolved_by_correction`;
- `resolved_by_clarification`;
- `resolved_by_claim_narrowing`;
- `resolved_by_claim_removal`;
- `not_resolved_with_reason` and explicitly escalated to the editor.

Never claim an issue is resolved because the response is polite or because text was added.

## Decision proof for each headline claim

For every headline claim in the title, abstract, contribution statement, main Results and Conclusion, build this internal object:

```text
Claim
Why it matters
Evidence type
Decisive evidence
Strongest plausible alternative explanation
Discriminating test or analysis
Uncertainty / boundary
Relevant figure/table/source
Target-journal decision axis
Current status
```

The strongest manuscript is not the one with the most evidence. It is the one where the **decisive evidence is visibly matched to the decisive claim**.

### Claim closure test

Ask:

1. What would a skeptical expert need to believe this exact claim?
2. Is that evidence already present?
3. If not, can the claim be narrowed to what the existing evidence establishes?
4. Would the narrowed claim still constitute a worthwhile paper for the target?

If the answer to 3 and 4 is no, new evidence may be genuinely required.

## Editorial triage gate

Produce an editor-facing preflight before simulated peer review.

### A. Scope and article-type fit

- exact journal/venue;
- article/content type;
- scope match;
- target readership/community;
- current official criteria verified or unresolved.

### B. One-minute decision brief

This is a **design artifact**, not a claim about literal editor reading time.

State in compact form:

- `Question` — what is unresolved?
- `Answer` — what does this manuscript establish/provide?
- `Evidence` — what is the decisive evidence class?
- `Why this target` — which verified publication criterion does it satisfy?
- `Boundary` — what does it explicitly not establish?

If this brief cannot be written faithfully, the manuscript's editorial positioning is not ready.

### C. Triage failure classes

- `scope_mismatch`;
- `article_type_mismatch`;
- `contribution_unclear`;
- `priority_or_breadth_not_established` when the target requires it;
- `insufficient_field_advance` when the target requires it;
- `technical_case_obviously_incomplete`;
- `readability_blocks_evaluation`;
- `integrity_or_compliance_blocker`;
- `mature_but_better_target_elsewhere`.

Do not try to repair a true scope mismatch with more assertive writing.

## External reviewer gate

Each independent reviewer should create a private concern ledger. For each issue record:

```text
Concern
Challenged claim
Visible evidence
Why the evidence is insufficient or ambiguous
Alternative interpretation
Severity
Blocking status
Resolution test
Target-journal criterion affected
```

The **resolution test** is critical. A concern without a closure test tends to become vague reviewer preference.

### Reviewer question set

For each central claim:

- Is the claim accurately stated?
- Is the prior-work distinction fair and verifiable?
- Does the design permit this inference?
- Are controls/comparators/baselines/source evidence appropriate?
- Are uncertainty and failure boundaries visible?
- Is there a plausible alternative explanation the manuscript has not discriminated from?
- Does the analysis answer the research question actually stated?
- Are data/methods detailed enough for scrutiny and field-appropriate reproduction?
- Are limitations proportional to their consequences for interpretation?

Use discipline-specific gates only when activated by the claims and design.

## Editor synthesis gate

After independent reviews are frozen, convert reviewer concerns into a **decision map**.

### Required buckets

1. `publication_criteria_blockers` — failure to meet an explicit journal criterion;
2. `technical_blockers` — central case cannot currently be established;
3. `major_repairable` — substantive but closable without replacing the study;
4. `claim_recalibration` — evidence is usable if wording/scope is narrowed;
5. `clarity_or_reporting` — the underlying science may be adequate but evaluation is obstructed;
6. `optional_enrichment` — potentially useful, not necessary for publication criteria.

The editor simulation must explicitly separate **must address** from **nice to have**.

### No vote counting

Consensus increases confidence, but a single technically decisive concern can remain blocking. Conversely, several negative recommendations do not automatically establish a valid technical objection.

Weight the reasoning and the reviewer's relevant expertise as far as it can be inferred from the assigned review lens. Do not invent identities or hidden expertise.

## Revision-to-acceptance gate

For each editor/reviewer item, choose the cheapest scientifically valid closure route:

### Route 1 — add decisive evidence

Use when the current central claim is worth preserving and the missing test genuinely discriminates between important interpretations.

### Route 2 — reanalyse existing evidence

Use when the data can answer the concern but the current analysis does not.

### Route 3 — correct an error

Use when the problem is factual, statistical, computational, citation, figure, or reporting error.

### Route 4 — clarify the existing evidence chain

Use when reviewers missed something because the manuscript made it hard to find or connect. Revise the manuscript, not merely the response letter.

### Route 5 — narrow the claim

Use when the evidence is sound but supports a more limited inference than originally claimed.

### Route 6 — remove the claim

Use when a secondary claim is not needed for the central contribution and cannot be responsibly supported.

Do not add experiments solely to appease a reviewer if claim narrowing/removal resolves the publication criterion more cleanly.

## Concern severity and repair

Classify by **decision consequence**:

- `fatal_current_target` — cannot be repaired without a fundamentally different study, or the manuscript does not fit the target;
- `blocking_repairable` — central case is not established but a defined revision could establish it;
- `major_nonblocking` — materially affects confidence, significance, reproducibility, or interpretation;
- `minor` — localized correction that does not change central inference;
- `optional` — improvement not required to meet the publication criteria.

A difficult experiment is not automatically blocking. A one-line correction is not automatically minor.

## Decision-risk map

Before submission, produce a table with one row per high-risk issue:

| Risk | Stage | Criterion | Claim affected | Probability of being noticed | Consequence if valid | Existing defense | Best repair | Residual risk |
|---|---|---|---|---|---|---|---|---|

`Probability of being noticed` is a qualitative planning label (`low/medium/high`), not a statistical acceptance prediction. Never invent numeric acceptance probabilities.

Prioritize issues with high scientific consequence, not merely high reviewer visibility.

## Reviewer-panel simulation

Use independent lenses that correspond to real decision needs without inventing biographies:

- **validity/evidence lens** — can the methods/data/analysis support the central claims?
- **field-positioning/significance lens** — what exactly advances relative to prior knowledge, and does that matter under this journal's model?
- **reader/translation/reproducibility lens** — can the intended community understand, evaluate, reuse or act on the work?

Change the lenses when the article type requires it. A clinical paper may need stronger design/statistical/clinical-interpretation coverage; a theorem paper may need proof/boundary/interpretation coverage; a qualitative paper may need sampling/analytic-credibility/transferability coverage.

Keep reviewers independent until reports are frozen.

## Anti-gaming rules

Never optimize acceptance by:

- omitting adverse or contradictory evidence;
- hiding a close competitor or misdescribing prior work;
- citing a potential reviewer merely to influence them;
- suggesting reviewers because they are expected to be favorable;
- exploiting author-suggested-reviewer effects;
- adding irrelevant citations requested for reviewer self-interest;
- disguising an incremental result as a discontinuous breakthrough;
- using a cover letter to claim significance the manuscript cannot support;
- burying limitations in Supplementary Information when they change the headline interpretation;
- constructing fake consensus among simulated reviewers.

Recent open-peer-review research has reported reviewer recommendation changes associated with citation requests, and older studies have found author-suggested reviewers can make more favorable recommendations. Treat these as reasons for **stronger anti-gaming safeguards**, not strategies to exploit.

## Source basis

Current public guidance reviewed 2026-08-19:

- Nature, `Editorial criteria and processes`: https://www.nature.com/nature/for-authors/editorial-criteria-and-processes
- Nature, `Peer Review`: https://www.nature.com/nature/editorial-policies/peer-review
- IEEE Author Center, `About the Peer Review Process`: https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/about-the-peer-review-process/
- IEEE Author Center, `Become an IEEE Reviewer`: https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/become-an-ieee-reviewer/
- PLOS ONE, `Reviewer Guidelines`: https://journals.plos.org/plosone/s/reviewer-guidelines
- PLOS editor resources, `Assessing reviews and making decisions`: https://explore.plos.org/editor-resources/editorial-decisions
- PLOS Biology and PLOS Medicine reviewer/editorial criteria for selective-journal contrasts.
- JAMA Network, `Guidance and Benefits for Peer Reviewers`: https://jamanetwork.com/pages/guidance-and-benefits-for-peer-reviewers
- eLife Assessments: https://elifesciences.org/about/elife-assessments
- ACM venue review criteria are venue-specific; current examples expose relevance, novelty/significance, reproducibility, validity, prior work and presentation as separate dimensions.

These sources demonstrate that publication objectives vary. Always verify the exact target journal's current criteria before converting this shared engine into a target-specific decision model.