# Adversarial review and confirmation-bias control

> Shared contract for making simulated manuscript review actively falsification-seeking rather than merely independent, polite, or comprehensive. Use with the editor/reviewer decision engine and atomic-claim verification. The goal is not hostile tone. The goal is to prevent the manuscript's own framing, earlier reviewer commitments, or editorial momentum from becoming evidence that the paper is good.

Last reviewed: 2026-08-31.

## Core invariant

Reviewer independence is necessary but not sufficient.

Three mutually blind reviewers can still reproduce the same confirmation bias if all three inherit the same author framing and ask only whether the presented case seems convincing.

The review system must therefore distinguish:

```text
independence of reviewers
!=
independence from the manuscript's framing
!=
active falsification pressure
```

The release objective is:

> A central claim survives only after independent reviewers have tried to make it fail using applicable counterexamples, alternative explanations, prior-art challenges, boundary cases, incompatible interpretations, and evidence-quality attacks.

Criticism is measured by the quality of attempted disconfirmation, not by the number or harshness of comments.

## 1. Start central claims in a non-established state

For review purposes, every headline or decision-relevant claim starts as:

`NOT_YET_ESTABLISHED`

The reviewer must independently locate sufficient warrant before upgrading it.

Do not begin from:

- the abstract's conclusion;
- the author's contribution list;
- a prior editor's positive posture;
- another reviewer's acceptance recommendation;
- a response letter claiming closure;
- the fact that the manuscript has survived many revision rounds;
- polished prose, professional typesetting, or a strong narrative.

The question is not `why is this probably right?`

The question is:

`what exact evidence would make this claim fail, and has that failure route been excluded or correctly bounded?`

## 2. Reconstruct the case independently before using author framing

Each blind reviewer must reconstruct, from the immutable manuscript and allowed source packet:

```text
central question
central claims
definitions / estimands / scientific objects
assumptions
primary evidence or proof
strongest boundary
closest prior-work comparator
what would falsify or materially weaken the claim
```

Author claim/evidence notes may be supplied as provenance or navigation aids only after, or separately from, this reconstruction. They must not provide pre-adjudicated statuses, concern closures, desired recommendation, or a canonical claim decomposition that the reviewer is required to accept.

If the review environment cannot prevent framing inheritance, record that limitation explicitly.

## 3. Mandatory adversarial attack log

For every headline claim, each reviewer performs the applicable attacks and records the result even when no concern is found.

Use this schema:

```text
claim_id
attack_family
attack_attempted
evidence_or_case_examined
outcome: survived / failed / narrowed / not_assessable
reason
new_concern_id_if_any
```

There is no concern quota. A claim may survive every applicable attack. The required output is the attempted falsification record, not manufactured criticism.

### Attack families

Select only those scientifically applicable.

#### A. Counterexample / boundary attack

- degenerate case;
- smallest nontrivial case;
- extreme parameter regime;
- scope boundary;
- counterexample search;
- theorem assumption removal;
- incompatible specialization.

For formal work, derive immediate consequences independently and test small constructions when useful. Executable search is a counterexample aid, not a substitute for proof.

#### B. Alternative-explanation attack

Ask for the strongest plausible interpretation under which the visible observations occur but the headline interpretation is false or too strong.

Examples include confounding, selection, leakage, reverse causality, proxy effects, measurement artifact, alternative mechanism, reconstruction through another channel, or a weaker decision-theoretic interpretation.

#### C. Design / identification attack

Ask whether the comparison, randomization, sampling, intervention, control, unit of analysis, dependence structure, missingness, censoring, or stopping rule permits the stated inference.

#### D. Statistical / quantitative attack

Challenge estimand choice, uncertainty, multiplicity, calibration, denominator, sensitivity, effect scale, equivalence/noninferiority logic, model fit, convergence, robustness, and repeated-measures dependence as applicable.

#### E. Prior-art / novelty attack

Search or inspect the closest plausible parent and competitor rather than only the manuscript's cited comparison set. Ask whether the contribution survives the strongest fair reformulation of prior work.

A novelty claim survives only within a dated search boundary. `We found no prior work` is not timeless evidence.

#### F. Negative-evidence attack

Search for adverse, null, contradictory, failed, boundary, or exception evidence that would change the headline interpretation. Do not treat absence from the author's narrative as evidence of absence.

#### G. Definition / type attack

Check whether named objects are explicitly defined and whether derived quantities combine compatible mathematical types, domains, units, probability spaces, representation classes, estimands, or optimization sets.

A numerically meaningful toy example does not prove a generally well-typed definition.

#### H. Cross-surface contradiction attack

Compare title, abstract, main text, equations, figures, tables, Methods, Discussion, limitations, supplement and availability statements for scope or certainty inflation.

#### I. Reproducibility / provenance attack

Ask whether the central evidence could be independently reconstructed or audited, and whether data, code, proof, source, protocol, status and version claims are bound to the current artifact.

## 4. Interpretation-blind evidence pass when feasible

For empirical, computational and some formal manuscripts, use a first-pass review that temporarily masks high-level author interpretation when technically feasible.

Possible packet:

```text
Methods / design
Results / primary displays
formal definitions + proof body where needed
registered analysis or protocol information
```

Temporarily withhold or defer:

```text
title framing
abstract conclusion
Discussion interpretation
contribution adjectives
cover letter
response letter
prior simulated decision posture
```

The reviewer first records what the visible evidence independently supports, then reads the author framing and compares the two.

Use this only when section masking does not destroy the scientific object or make the task artificial. For qualitative, conceptual, perspective or tightly integrated theory papers, mark it `not_applicable` rather than forcing a misleading blind pass.

## 5. Steelman the strongest rejection case before editor synthesis

After blind reports are frozen, the editor must construct two separate cases before choosing a posture.

### Best rejection / non-closure case

State the strongest evidence-grounded argument that the current manuscript should not yet receive the target terminal state.

It may be based on:

- one decisive technical objection;
- contribution not surviving closest prior work;
- central inference not identified;
- proof/type inconsistency;
- missing decisive evidence;
- target/article-type mismatch;
- unresolved integrity or provenance;
- contribution mass insufficient for the claimed article type;
- a limitation that collapses the headline claim.

### Best survival / acceptance-readiness case

State the strongest evidence-grounded argument that the paper survives the attacks and meets the verified target criteria.

The editor then resolves the conflict proposition by proposition.

Do not write the positive case first and treat objections as exceptions. Do not write the negative case as rhetorical hostility. Both are steelman exercises.

## 6. A single decisive objection can dominate consensus

Vote counting remains prohibited.

Three positive reviews do not close a technically decisive counterexample, invalid estimand, fatal prior-art overlap, missing proof premise, impossible causal inference, or integrity blocker.

Likewise, several negative preferences do not create a scientific defect.

The editor must record why each blocking objection is valid, invalid, resolved, narrowed, or not assessable.

## 7. Reviewer continuity does not substitute for a cold review

Reviewer continuity is useful for checking whether a specific concern was actually repaired, but it creates anchoring, consistency and sunk-cost risks.

After a major revision that changes any headline claim, central proof, primary analysis, central evidence set, contribution framing, or article type, use both:

1. **continuity review** — the original responsible reviewer checks the prior resolution test;
2. **cold review** — a fresh isolated reviewer receives only the current manuscript/source packet and verified target criteria, with no prior reviews, author responses, concern ledger, editor synthesis, revision narrative or previous recommendation.

The cold reviewer asks whether the current paper stands on its own and whether new central problems are visible without historical anchoring.

For minor copy-editing or localized reporting corrections, a cold review is not required.

## 8. Final clean-room closure review

Before `simulated_publication_ready_for_target` for a full manuscript, require at least one clean-room closure pass that has not participated in drafting, revision planning, earlier review synthesis, or author-response construction.

The clean-room reviewer must receive:

- the current immutable manuscript;
- current verified target criteria;
- necessary source/evidence material;
- no desired decision;
- no prior concern list;
- no author response letter;
- no statement that earlier reviewers were positive.

It must independently reconstruct the headline claim inventory and perform applicable adversarial attacks.

If true context isolation is unavailable, state that confirmation-bias protection is incomplete and do not claim clean-room independence.

## 9. Counterevidence search is asymmetric by design

A manuscript naturally presents supporting evidence. Review therefore must spend explicit effort seeking information the manuscript is less likely to foreground.

For high-risk or headline claims, actively inspect:

- closest contradictory literature;
- null/negative results when available;
- failure cases;
- limitations that change generality;
- alternative analyses/specifications where available;
- counterexamples and degenerate cases;
- known retractions/corrections/version changes relevant to cited support.

This is not a requirement to find contradictory evidence. It is a requirement to search for it proportionately to claim risk.

## 10. No positivity momentum

Do not let these become evidence for readiness:

- many completed revision rounds;
- a long response letter;
- previous simulated `accept` or `minor revision` labels;
- reviewer fatigue;
- stylistic polish;
- successful CI/tests unrelated to the scientific claim;
- the fact that the reviewer helped design the repair;
- the user's preference that the paper be good;
- earlier assistant statements praising the manuscript.

Each terminal decision is made on the current artifact.

## 11. Failure-seeking is not performative harshness

Do not manufacture flaws, demand impossible experiments, reject incremental but valid work because it feels insufficiently exciting for the wrong target, or convert taste into a Major Concern.

A strong adversarial review can conclude:

`No blocking concern survived the attempted falsification passes.`

That conclusion is stronger than generic praise because it records what was actually challenged.

## 12. Required reviewer output extension

For full-manuscript or decision-readiness review, add an internal or user-visible section as appropriate:

```text
Adversarial attack summary
- headline claim
- strongest attempted falsifier
- result
- residual uncertainty
```

Also record:

```text
framing_independence: pass / limited
interpretation_blind_pass: pass / not_applicable / limited
counterevidence_search: pass / incomplete / not_applicable
cold_review_required: yes / no
cold_review_status: pass / pending / limited
```

## 13. Editor closure rule

Do not issue the target terminal state unless all are true:

- blind initial reviewer reports were frozen before synthesis;
- headline claims have adversarial attack logs;
- the strongest rejection/non-closure case has been explicitly constructed and answered or accepted;
- decisive single-reviewer objections are resolved rather than outvoted;
- high-risk counterevidence searches are complete enough for the claimed scope;
- major central revisions received a cold review;
- a final clean-room closure review passed for full-manuscript readiness;
- no reviewer or editor treats revision history, polish, or prior positive posture as evidence;
- unresolved isolation limits are disclosed.

## Guarantee boundary

This contract reduces confirmation bias; it cannot eliminate it.

Simulated reviewers can share model priors, training data, blind spots and reasoning errors even when contexts are isolated. A clean review simulation is therefore evidence of systematic challenge, not proof that real experts will agree or that the paper is correct.
