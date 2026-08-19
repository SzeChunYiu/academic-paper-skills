# Editor–reviewer decision engine

> Shared pre-submission decision model for writing, mock review, and revision workflows. Last reviewed: 2026-08-19.
>
> This file operationalizes public editorial/reviewer guidance. It does **not** claim that acceptance is predictable or controllable.

## Contents

- [Purpose](#purpose)
- [Ethical definition of acceptance engineering](#ethical-definition-of-acceptance-engineering)
- [Decision stages](#decision-stages)
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

Do not collapse manuscript evaluation into one score such as `quality`, `novelty`, or `acceptance probability`.

Use this stack:

`integrity/compliance -> editorial triage -> external review -> editorial synthesis -> revision closure`

Different journals weight these stages differently. Selective broad-interest journals may screen for priority and breadth before review. Rigor-first journals may explicitly avoid perceived importance as a publication threshold. Other models separate significance from strength of evidence. Resolve the exact journal and article type before assigning target-specific weights.

## Ethical definition of acceptance engineering

**Acceptance engineering** means making a valid contribution easier to evaluate and harder to misunderstand by:

- matching the actual journal/article-type criteria;
- making the central question, answer, evidence and boundary explicit;
- supplying discriminating evidence for the claims actually made;
- surfacing limitations before they become reviewer discoveries;
- making methods, analyses and provenance auditable;
- resolving contradictions and internal inconsistencies;
- narrowing or removing claims the design cannot establish;
- closing decision-relevant concerns during revision.

It does **not** mean gaming reviewers, exaggerating novelty, hiding limitations, strategically omitting competitors, flattering likely reviewers with citations, suggesting friendly reviewers to obtain favorable recommendations, or adding cosmetic experiments that do not discriminate between interpretations.

Optimize decisionability and scientific credibility, not persuasion independent of evidence.

## Decision stages

### Stage 0 — integrity and compliance

Check authorship/conflicts, ethics/consent/registration, duplicate publication, image/data integrity, required availability statements, reporting standards, and submission completeness. These are not rhetorical problems.

### Stage 1 — editorial triage

Ask:

1. Is the manuscript in scope and the article type appropriate?
2. What is the actual contribution?
3. Why does it matter under this target's publication model?
4. Is the case mature enough for external review?
5. Can the editor recover the question, evidence class, implication and boundary quickly?
6. Are there obvious integrity, fit or central-evidence blockers?

Keep editorial priority/readership separate from technical validity when the target does so.

### Stage 2 — external review

Reviewers test whether the case is established. Depending on venue/article type, assess validity, claim–evidence alignment, design/method/analysis, prior-work positioning, target-specific significance or advancement, data interpretation, reproducibility, ethics, clarity, limitations and alternative explanations.

A reviewer recommendation is evidence for the editor, not the decision itself.

### Stage 3 — editorial synthesis

Weigh arguments and relevant expertise rather than counting reviewer votes. Ask which concerns map to publication criteria, which are technically blocking, which are repairable, which are useful but non-essential, and whether claim narrowing changes target fit.

### Stage 4 — revision closure

A decision-relevant concern needs a real closure state:

- `resolved_by_evidence`;
- `resolved_by_analysis`;
- `resolved_by_correction`;
- `resolved_by_clarification`;
- `resolved_by_claim_narrowing`;
- `resolved_by_claim_removal`;
- `resolved_by_target_change`;
- `not_resolved_with_reason` and explicitly escalated.

Do not call an issue resolved because the response is polite or longer.

## Decision proof for each headline claim

For every headline claim record:

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

Ask what a skeptical expert needs to believe the exact claim, whether that evidence exists, whether the claim can be narrowed, and whether the narrowed paper still fits the target. If not, genuinely new evidence or a different target may be required.

## Editorial triage gate

Build an editor-facing preflight with exact journal/venue, article type, scope, readership, and verified/unresolved criteria.

Create a compact decision brief:

- `Question` — what is unresolved?
- `Answer` — what does the manuscript establish/provide?
- `Evidence` — what is decisive?
- `Why this target` — which verified criterion is met?
- `Boundary` — what is not established?

Triage failure classes include `scope_mismatch`, `article_type_mismatch`, `contribution_unclear`, target-specific priority/breadth or field-advance failures, `technical_case_obviously_incomplete`, `readability_blocks_evaluation`, `integrity_or_compliance_blocker`, and `mature_but_better_target_elsewhere`.

Do not repair a true target mismatch with stronger adjectives.

## External reviewer gate

For each substantive concern record:

```text
Concern
Challenged claim
Visible evidence
Why insufficient or ambiguous
Alternative interpretation
Severity
Blocking status
Resolution test
Target-journal criterion affected
```

For each central claim ask whether the claim is accurate, prior-work positioning is fair, the design permits the inference, controls/comparators are appropriate, uncertainty and failure boundaries are visible, important alternatives are discriminated, analyses answer the stated question, and methods/data are sufficiently auditable.

A concern without a resolution test is incomplete.

## Editor synthesis gate

After independent reviews are frozen, classify concerns into:

1. `publication_criteria_blockers`;
2. `technical_blockers`;
3. `major_repairable`;
4. `claim_recalibration`;
5. `clarity_or_reporting`;
6. `optional_enrichment`.

### No vote counting

Consensus can increase confidence, but a single technically decisive objection can remain blocking. Several negative recommendations do not automatically establish a valid technical objection. Weight reasoning and the assigned review lens without inventing hidden expertise.

## Revision-to-acceptance gate

Choose the cheapest scientifically valid closure route.

### Route 1 — add decisive evidence

Use when preserving the central claim matters and the missing evidence genuinely discriminates among important interpretations.

### Route 2 — reanalyse existing evidence

Use when current data can answer the concern with a better analysis.

### Route 3 — correct an error

Use for factual, statistical, computational, citation, figure or reporting errors.

### Route 4 — clarify the existing evidence chain

Use when the evidence exists but is hard to find or connect. Revise the manuscript, not only the response letter.

### Route 5 — narrow the claim

Use when the evidence supports a more limited inference than originally claimed.

### Route 6 — remove the claim

Use when a secondary claim is unnecessary and cannot be responsibly supported.

### Route 7 — change target/article type

Use when the science is sound but the verified journal objective, scope, readership or article-type contract is mismatched. Transfer/repositioning is preferable to manufacturing broader significance or adding irrelevant experiments.

Do not add experiments solely to appease a reviewer if claim narrowing/removal or a better target resolves the publication criterion more cleanly.

## Concern severity and repair

Classify by decision consequence:

- `fatal_current_target` — current study/target mismatch cannot be repaired without fundamentally changing the study or target;
- `blocking_repairable` — central case is not established but a defined revision could establish it;
- `major_nonblocking` — materially affects confidence, significance, reproducibility or interpretation;
- `minor` — localized correction that does not change central inference;
- `optional` — improvement not required by the publication criteria.

Difficulty and cost do not determine severity.

## Decision-risk map

For high-risk issues record risk, stage, criterion, claim affected, qualitative noticeability, consequence if valid, existing defense, best repair and residual risk. Never invent numeric acceptance probabilities.

Prioritize scientific consequence, not merely reviewer visibility.

## Reviewer-panel simulation

Use independent lenses without inventing biographies:

- validity/evidence;
- field-positioning/significance under the target's actual criteria;
- reader/translation/reproducibility and boundaries.

Adapt lenses to the study design and keep reviewers independent until reports are frozen.

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
- hiding limitations in Supplementary Information when they change the headline interpretation;
- constructing fake consensus among simulated reviewers.

Empirical peer-review findings about reviewer suggestions or citation requests are reasons for stronger anti-gaming safeguards, not tactics to exploit.

## Source basis

Current public guidance reviewed 2026-08-19 includes Nature editorial criteria/peer review, IEEE Author Center reviewer guidance, PLOS reviewer/editor resources, JAMA Network reviewer guidance, eLife Assessments, and venue-specific ACM criteria. Exact live target guidance always overrides this shared fallback model.
