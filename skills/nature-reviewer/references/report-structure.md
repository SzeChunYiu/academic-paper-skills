# Journal-aware editor/reviewer report structure

## Contents

- [Default output contract](#default-output-contract)
- [Review setup](#review-setup)
- [Editorial triage simulation](#editorial-triage-simulation)
- [Per-reviewer structure](#per-reviewer-structure)
- [Concern traceability](#concern-traceability)
- [Editor synthesis](#editor-synthesis)
- [Decision-engineering map](#decision-engineering-map)
- [Risk / unsupported claims](#risk--unsupported-claims)
- [Style rules](#style-rules)

## Default output contract

Return in this order unless the user asks otherwise:

1. `Review setup`
2. `Editorial triage simulation`
3. `Reviewer 1`
4. `Reviewer 2`
5. `Reviewer 3`
6. `Editor synthesis (post-review; simulated)`
7. `Decision engineering map (author-facing)`
8. `Risk / unsupported claims`

The editor and reviewers are separate simulation layers. The author-facing repair map is generated only after reports are frozen.

## Review setup

Include:

- `Input scope`;
- `Assessment boundary`;
- `Exact target journal / venue`;
- `Article/content type`;
- `Publication model`;
- `Verified decision criteria`;
- `Unresolved target criteria`;
- `Shared manuscript claim summary`;
- `Visible evidence base`;
- `Missing materials affecting confidence`.

## Editorial triage simulation

Include:

- `Triage posture`;
- `Scope/article-type fit`;
- `Question and contribution clarity`;
- `Decisive evidence class`;
- `Target-specific priority / breadth / advancement readout` only when applicable;
- `Review-readiness blockers`;
- `Readability / evaluability risk`;
- `Likely best next action before external review`.

Use bounded language. Never state that the real editor will send/reject the manuscript or assign a numeric probability.

## Per-reviewer structure

Each isolated report uses the same skeleton:

- `Overall assessment`;
- `Central claim and evidence readout`;
- `Major strengths`;
- `Major Concerns`;
- `Minor Comments`;
- `Blocking technical failings`;
- `Assessment against target criteria`;
- `Recommendation posture`.

For a target that values readership/significance, include who would care and why. For a rigor-first journal, do not force broad-interest criticism.

### Assessment against target criteria

Explicitly distinguish:

- universal scientific axes;
- target-conditional axes;
- criteria not used by this publication model;
- items not assessable from supplied material.

## Concern traceability

Give every substantive concern a stable reviewer-local ID.

### Major Concern

```text
R1-M1 [claim_evidence_validity]
**Severity** Major
**Blocking** Yes / No
**Target criterion** [criterion or not applicable]
**Claim pointer** [faithful paraphrase]
**Evidence pointer** [verified location or location not provided]
**Concern** [grounded critique]
**Alternative interpretation** [when relevant]
**Why it matters** [decision/scientific consequence]
**Resolution test** [what would close the issue]
```

### Minor Comment

```text
R1-m1 [clarity_and_argument_logic]
**Severity** Minor
**Target criterion** [criterion or not applicable]
**Affected element** [claim/reporting element]
**Evidence pointer** [verified location or location not provided]
**Issue** [localized problem]
**Required correction** [specific closure]
```

Rules:

- a resolution test may be new evidence, reanalysis, correction, clarification, claim narrowing or claim removal;
- Minor Comments are never blocking;
- do not force a minimum issue count;
- use `None identified from the supplied material` when appropriate;
- do not expose the full private coverage matrix.

## Editor synthesis

Generate only after all reviewer reports are frozen.

Include:

- `What external review changed relative to triage`;
- `Consensus strengths`;
- `Publication-criteria blockers`;
- `Technical blockers`;
- `Major repairable concerns`;
- `Claim-recalibration opportunities`;
- `Clarity/reporting issues`;
- `Optional enrichment requests`;
- `Where reviewer emphasis genuinely differs`;
- `Simulated decision posture`;
- `Why this posture follows from criteria and evidence`.

### No vote counting

A concern enters a consensus bucket only when at least two reviewers independently raised the same underlying issue, but lack of consensus does not erase a technically decisive single-reviewer concern.

Do not average reviewer recommendations or numerical scores into an acceptance probability.

## Decision-engineering map

This section is author-facing, not part of the simulated reviewer reports.

Prioritize the smallest scientifically sufficient repairs.

| Priority | Risk | Stage | Criterion | Claim affected | Best closure route | Minimum sufficient change | Residual risk |
|---|---|---|---|---|---|---|---|

Closure routes:

- `add_decisive_evidence`;
- `reanalyse_existing_evidence`;
- `correct_error`;
- `clarify_or_restructure`;
- `narrow_claim`;
- `remove_claim`;
- `change_target_or_article_type`.

Also include:

### Do before submission/revision

Only decision-relevant actions.

### Do not waste effort on

Reviewer-like requests or extra experiments classified as optional/non-essential.

### Stop / transfer conditions

State when the current target is mismatched or the study cannot establish the desired claim without fundamentally different work.

## Risk / unsupported claims

Flag:

- unsupported novelty/significance/priority claims;
- central claims without decisive evidence;
- untested alternatives that materially change interpretation;
- target-specific criteria not verified;
- missing controls/validations/comparators when claim-dependent;
- internal contradictions;
- partial-input limitations;
- any judgement that would require hidden editorial knowledge.

## Style rules

- Keep tone formal, direct and evidence-based.
- Preserve legacy punctuation guardrails in reviewer prose where this skill requires them: avoid em dashes, en dashes, and colons as habitual sentence connectors when clearer sentence boundaries work.
- Do not invent reviewer identities, line numbers, figure panels, datasets, prior studies, experiments or hidden editor knowledge.
- Do not write a real editorial decision letter unless the user provided one for analysis.
- Do not present the simulation posture as an actual journal outcome.
- Do not turn `acceptance engineering` into manipulation of reviewer selection, citations, or disclosure.
