# Epistemic rhetoric and qualification contract

> Shared contract for writing scientific claims that are honest without becoming timid, defensive, repetitive, or dominated by audit language.
>
> Scientific caution is required. **Self-erasing rhetoric is not.**

## Core principle

The manuscript should say the strongest statement the evidence warrants, no stronger and no weaker.

That means avoiding both:

- **overclaiming** — carrying evidence beyond its design, population, assumptions, or uncertainty;
- **underclaiming / defensive narration** — repeatedly weakening an established bounded result until the reader can no longer tell what the paper actually found.

Use proposition-level calibration:

```text
evidence state
-> scientific claim strength
-> necessary qualification
-> reader-facing wording
```

Do not translate the entire integrity/audit ledger into manuscript prose.

## 1. Separate scientific qualification from audit narration

Scientific qualification tells the reader something necessary about the claim.

Examples:

- the result is limited to one held-out domain;
- the comparison is descriptive rather than population-level;
- a causal interpretation is not identified;
- an interval is wide;
- one comparator is interface-limited;
- an important alternative explanation remains.

Audit narration documents how the research programme managed itself.

Examples:

- exact terminal names;
- pass/fail gate vocabulary;
- repeated statements that a result was `retained`;
- every historical failed protocol;
- every pre-outcome freeze event;
- every review correction;
- every reason an internal branch was not promoted.

Audit narration belongs in the manuscript only when it changes scientific interpretation, bias risk, or credibility.

Otherwise keep it in Methods, provenance records, preregistration, supplementary material, or the repository.

## 2. Truthful does not mean maximally cautious

If the study directly establishes a bounded result, state it directly.

Weak/self-defeating:

`We do not claim a general advantage, and this does not establish broad superiority, but the result is retained as a bounded positive.`

Better when supported:

`On the frozen held-out domain, the typed relational representation outperformed the untyped comparator. Whether this advantage generalizes beyond the tested domain remains open.`

The second version preserves the same boundary while making the scientific result legible.

## 3. One qualification should do one job

For each claim, identify the exact reason for qualification:

- sampling / population;
- design / causal identification;
- measurement;
- model/interface;
- statistical uncertainty;
- external validity;
- source/evidence authority;
- novelty priority;
- temporal/version dependence;
- unresolved alternative explanation.

Use the smallest wording that communicates that reason.

Do not stack multiple generic caution phrases when one precise boundary is enough.

## 4. Caveat placement hierarchy

Place qualifications where they have the highest scientific value with the least repetition.

### Local qualification

Keep a caveat next to a claim when omitting it would immediately mislead the reader.

Example:

`The effect was positive on the single historical case; it is not a population estimate.`

### Result-block qualification

Use one sentence at the end of a result block when several sentences share the same boundary.

### Discussion limitation

Use the Discussion for broader limitations, generalizability, alternative explanations, and consequences.

### Methods/provenance

Use Methods or artifact records for chronology, custody, version, freeze, and implementation details that do not alter the local interpretation.

Avoid repeating the same limitation in Abstract + Introduction + every Results subsection + Discussion unless each occurrence serves a distinct rhetorical function.

## 5. Defensive-phrase audit

Review repeated patterns such as:

- `we do not claim`;
- `does not establish`;
- `should not be read as`;
- `nothing here claims`;
- `not evidence of`;
- `remains undetermined`;
- `cannot check`;
- `not a result`;
- `does not authorize`;
- `not superiority`;
- `not population evidence`;
- `retained terminal`;
- `withdrawn rather than...`.

These phrases are sometimes exactly right.

They become a writing problem when they:

- outnumber direct positive scientific statements;
- repeat an already active boundary;
- narrate project governance instead of science;
- interrupt every result before the reader can integrate it;
- turn the Discussion into a disclaimer ledger;
- obscure the strongest surviving claim.

Repair by consolidating boundaries and stating the positive bounded result first when scientifically appropriate.

## 6. Positive-claim visibility gate

For each headline finding, the reader should be able to underline one sentence that says what the study found.

That sentence should contain:

- the object/comparison;
- the direction or relation;
- the relevant regime/population;
- essential uncertainty/boundary when needed.

If the only way to discover the result is to subtract several disclaimers from a paragraph, the rhetoric has failed.

## 7. Adverse and null results should be scientific, not ceremonial

Do not hide failed hypotheses, null results, adverse controls, or contradictory evidence.

But do not present them as virtue-signalling audit events either.

Instead ask:

> What does this adverse result change in the scientific interpretation?

Then write that consequence.

Example:

Instead of:

`The registered monotone-scaling hypothesis is an authoritative negative and is retained exactly as written.`

prefer, when accurate:

`The preregistered monotone-scaling hypothesis failed: larger models did not improve the targeted diagnostic under this protocol. This rules out model scale as the explanation for the observed separation in this experiment.`

If the failure has no bearing on the paper's central argument, move it to supporting material rather than elevating it merely because it was preregistered.

## 8. Integrity language is not automatically manuscript language

Machine-epistemic terms such as:

- authority;
- promotion;
- terminal;
- gate;
- receipt;
- freeze;
- ledger;
- fail-closed;
- cannot-check;

may be legitimate scientific terms in a paper that formally studies those objects.

Otherwise translate them to ordinary scholarly language.

Examples:

- `gate failed` -> `the prespecified criterion was not met`;
- `terminal is CANNOT_CHECK` -> `the available evidence was insufficient to determine the outcome`;
- `promotion not authorized` -> `the evidence does not support the stronger claim`;
- `receipt confirms` -> `an independent replay reproduced the result`.

## 9. Calibrate novelty language

Do not write novelty as ownership accounting.

Avoid reader-facing formulations such as:

- `X owns this idea`;
- `donor family`;
- `parent work`;
- `claim subtraction`;
- `we do not own...`.

Use ordinary scholarly relations:

- introduced;
- established;
- extended;
- adapted;
- applied;
- generalized;
- contrasted;
- combined;
- independently developed;
- closely related.

State the surviving contribution positively after crediting prior work.

## 10. AI-writing stance risks

Comparative corpus research on LLM-generated academic prose reports several relevant tendencies across genres and prompts:

- narrower or less nuanced stance repertoires;
- formulaic academic sequences;
- unusual or ornamental academic vocabulary;
- risk-averse over-hedging in some research-writing revision tasks;
- weaker rhetorical engagement or authorial presence in some corpora;
- combinations of hedging and boosting that produce internally awkward stance.

Treat these as diagnostic risks, not universal fingerprints.

### Stance contradiction audit

Flag constructions such as:

- `it seems clear`;
- `may definitively`;
- `strongly suggests with certainty`;
- repeated hedge + booster combinations whose epistemic force is unclear.

Choose one evidence-calibrated stance instead.

## 11. Authorial judgment should remain visible

A strong paper distinguishes:

- what the data show;
- what the authors infer;
- what the literature suggests;
- what remains speculative.

Use authorial presence where it clarifies responsibility:

- `we interpret...`;
- `we chose... because...`;
- `we regard this as...`;

when the target field permits it.

Do not hide every interpretation behind agentless phrases such as `it is suggested that`.

## 12. Discussion rhetoric

A Discussion should be willing to make an argument.

For each major finding:

```text
finding
-> interpretation
-> strongest alternative
-> relation to prior work
-> boundary
-> implication
```

Do not replace this chain with:

```text
finding
-> list of things not claimed
-> future work
```

A limitations paragraph is part of a Discussion, not a substitute for one.

## 13. Abstract rhetoric

The abstract must expose the positive scientific object and result early enough to be understood.

Avoid spending disproportionate abstract space on:

- novelty disclaimers;
- audit chronology;
- internal labels;
- version history;
- multiple layers of caveat.

A useful abstract sequence is:

```text
problem
-> approach/object
-> principal result(s)
-> bounded implication
```

One precise limitation is often stronger than several generic cautions.

## 14. Rhetorical-economy test

For every defensive sentence ask:

1. Which specific overinterpretation would occur if this sentence were removed?
2. Has that boundary already been established nearby?
3. Could the same scientific boundary be expressed in fewer, more concrete words?
4. Does the sentence advance interpretation, or merely document author caution?

If no concrete reader error is prevented, compress or remove it.

## 15. Release checks

Before publication-ready status:

- every headline result has a direct positive bounded statement;
- necessary limitations remain visible;
- repeated caveats have been consolidated;
- adverse/null results are interpreted rather than ceremonially retained;
- project-governance vocabulary is absent unless scientifically necessary;
- novelty is expressed as scholarly relation, not ownership bookkeeping;
- stance is proposition-specific and internally coherent;
- Discussion contains interpretation, not only qualification.

## Boundaries

Never use this contract to:

- remove a limitation that changes the claim;
- hide a failed preregistered primary outcome;
- convert uncertainty into certainty;
- suppress adverse evidence;
- oversell novelty or importance;
- replace transparent deviations with polished ambiguity.

The goal is **calibrated scientific confidence**.
