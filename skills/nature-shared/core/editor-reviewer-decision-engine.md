# Editor–reviewer decision engine

> Shared pre-submission decision model for writing, mock review, and revision workflows. Last reviewed: 2026-08-29.
>
> This file operationalizes public editorial/reviewer guidance. It does **not** claim that acceptance is predictable or controllable.

## Contents

- [Purpose](#purpose)
- [Ethical definition of acceptance engineering](#ethical-definition-of-acceptance-engineering)
- [Decision stages](#decision-stages)
- [Decision proof for each headline claim](#decision-proof-for-each-headline-claim)
- [Editorial triage gate](#editorial-triage-gate)
- [Multi-editor desk preflight](#multi-editor-desk-preflight)
- [Editor expertise and routing boundary](#editor-expertise-and-routing-boundary)
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

`integrity/compliance -> editorial triage -> editor/expertise routing -> external review -> editorial synthesis -> revision closure`

Different journals weight these stages differently. Selective broad-interest journals may screen for priority and breadth before review. Rigor-first journals may explicitly avoid perceived importance as a publication threshold. Other models separate significance from strength of evidence. Resolve the exact journal and article type before assigning target-specific weights.

For full target-specific submission optimization, load `journal-acceptance-readiness.md`. For public editor/team/section information, load `editor-expertise-routing.md` and treat identity as routing metadata rather than a persuasion target.

## Ethical definition of acceptance engineering

**Acceptance engineering** means making a valid contribution easier to evaluate and harder to misunderstand by:

- matching the actual journal/article-type criteria;
- making the central question, answer, evidence and boundary explicit;
- supplying discriminating evidence for the claims actually made;
- surfacing limitations before they become reviewer discoveries;
- making methods, analyses and provenance auditable;
- resolving contradictions and internal inconsistencies;
- narrowing or removing claims the design cannot establish;
- clarifying editor/reviewer expertise needed for fair routing;
- closing decision-relevant concerns during revision.

It does **not** mean gaming reviewers, exaggerating novelty, hiding limitations, strategically omitting competitors, flattering likely editors/reviewers with citations, suggesting reviewers because they are expected to be favorable, suggesting editors because they are expected to be favorable, profiling editor personality/leniency, or adding cosmetic experiments that do not discriminate between interpretations.

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
7. Can the editorial office identify the scientific domain, methods and expertise needed to route the paper without reconstructing the project?

Keep editorial priority/readership separate from technical validity when the target does so.

### Stage 1b — editor/expertise routing

If public editor/team information is relevant, use it only to assess professional expertise coverage, subject-section fit, permitted editor suggestions and conflicts. Do not infer a specific editor's likely decision.

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

Triage failure classes include `scope_mismatch`, `article_type_mismatch`, `contribution_unclear`, target-specific priority/breadth or field-advance failures, `technical_case_obviously_incomplete`, `readability_blocks_evaluation`, `routing_ambiguity`, `integrity_or_compliance_blocker`, and `mature_but_better_target_elsewhere`.

Do not repair a true target mismatch with stronger adjectives.

## Multi-editor desk preflight

Desk-triage judgments can differ, especially on soft criteria such as novelty/originality. Do not rely on one simulated editor voice.

Run independent non-biographical lenses:

1. `scope_article_type` — does the paper belong in this journal/content type?
2. `contribution_positioning` — is the advance real, recoverable, and fairly situated against close prior work?
3. `evidence_maturity` — is the scientific case mature enough to justify external review?
4. `readership_objective` — does it meet the target's explicit interest/importance/utility standard?
5. `routing_clarity` — are field, methods, evidence class, and reviewer expertise easy to identify?

Freeze each assessment before synthesis.

A plausible desk-rejection argument becomes an editorial-risk item even when another lens would send the paper to review. Do not count lens votes; resolve the strongest valid blocker or mark the judgment genuinely uncertain.

## Editor expertise and routing boundary

Public editor identities may be used for professional routing only.

Allowed:

- official role/team/section;
- publicly stated subject coverage;
- public professional research expertise;
- conflict checks;
- a target-permitted editor suggestion;
- testing whether the journal appears to have suitable expertise coverage.

Not allowed:

- personality or ideology profiling;
- inferred leniency/harshness;
- acceptance-rate ranking by editor;
- strategic citation of a potential editor;
- flattery or name-dropping;
- presumed reviewer friendships;
- targeting based on personal demographic characteristics.

If the exact current journal permits authors to suggest/request editors, choose qualified independent candidates by expertise and conflict status. Otherwise do not manufacture an editor-selection channel.

A routing mismatch is best repaired through clearer title/abstract/keywords/section selection or a better target, not manuscript references to editor identities.

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

### Reviewer expertise coverage

Before suggesting or simulating reviewers, decompose the manuscript into expertise required to evaluate its central claims: domain science, design/identification, statistics, computation, measurement/instrumentation, clinical/translation context, resource/data stewardship, and specialized techniques.

If the journal permits author reviewer suggestions, choose independent experts for coverage rather than expected favorability.

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

Do not derive simulated reviewer/editor personalities from real named people.

## Anti-gaming rules

Never optimize acceptance by:

- omitting adverse or contradictory evidence;
- hiding a close competitor or misdescribing prior work;
- citing a potential editor/reviewer merely to influence them;
- suggesting reviewers because they are expected to be favorable;
- suggesting editors because they are expected to be favorable;
- exploiting author-suggested-reviewer effects;
- profiling editor personality, ideology, leniency, or presumed decision tendency;
- adding irrelevant citations requested for reviewer self-interest;
- disguising an incremental result as a discontinuous breakthrough;
- using a cover letter to claim significance the manuscript cannot support;
- hiding limitations in Supplementary Information when they change the headline interpretation;
- constructing fake consensus among simulated reviewers.

Empirical peer-review findings about reviewer suggestions, editor disagreement, or citation requests are reasons for stronger anti-gaming safeguards, not tactics to exploit.

## Source basis

Current public guidance and meta-research reviewed 2026-08-29 includes Nature/Nature Communications editorial criteria and peer review, Nature Communications editor-team pages, Nature Geoscience cover-letter guidance, PLOS editor assignment and PLOS ONE editor-request workflow, 2026 meta-research on reviewer disagreement/editorial outcomes, 2026 desk-rejection disagreement across co-editors, multi-journal novelty/acceptance research, IEEE Author Center reviewer guidance, JAMA Network reviewer guidance, eLife Assessments, and venue-specific ACM criteria. Exact live target guidance always overrides this shared fallback model.
