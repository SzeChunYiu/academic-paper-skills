# Abstract information budget and entry-point contract

> Shared contract for writing, revising, and reviewing research-paper abstracts as standalone scholarly entry points rather than compressed Results tables or project summaries.
>
> Resolve the exact target venue, article type, abstract structure, word/character limit, citation policy, reporting guideline, and audience before applying this contract.

## Core principle

An abstract is not a miniature copy of every manuscript section.

It is the smallest self-contained representation of the paper that lets the intended reader recover:

```text
why this question matters
-> what exact problem/objective is addressed
-> what the paper did or established
-> what the decisive result is
-> what that result means
-> where the claim stops, when a boundary is decision-relevant
```

The abstract has a **scarce information budget**. Every sentence, technical term, and number must earn its place by changing the reader's understanding of the paper's central scientific case.

## 1. Resolve the abstract regime before writing

Record:

```text
venue
article type
abstract limit: words / characters / structured fields / none stated
structured or unstructured
references allowed? yes/no
required headings, if any
reporting guideline or checklist, if applicable
dominant paper archetype
intended reader breadth
headline claim IDs
headline evidence IDs
```

Do not infer a universal abstract format from another journal.

A 70-word Brief Communication, 150-word multidisciplinary Article, 250-word structured clinical abstract, and unrestricted field-journal abstract are different optimization problems.

## 2. Draft a rhetorical spine, not a section sampler

A useful default spine for many research papers is:

```text
context / scientific need
-> specific gap or question
-> approach or formal object only to the depth needed
-> headline finding or theorem
-> one decisive quantitative/formal anchor when useful
-> interpretation / immediate implication
-> claim-changing boundary when necessary
```

Not every move is mandatory. Remove any move that does not help this paper and target.

### Do not force a mini-IMRaD sequence

An abstract should not allocate one sentence to every manuscript section merely because those sections exist.

Examples:

- a theory paper may need almost no methods language;
- a new method paper may need more method identity and validation;
- a resource paper may need scale/coverage and access/utility;
- a qualitative paper may need context, data/source identity, analytic approach, central interpretation, and boundary rather than benchmark metrics;
- a trial may be obligated by a reporting guideline to include design, participant counts, group outcomes, effect estimates, uncertainty, harms, registration, and funding.

## 3. Archetype-specific abstract roles

### Empirical discovery / mechanism

Prefer:

```text
problem -> approach/design -> decisive observation -> discriminator or uncertainty -> bounded interpretation
```

Do not enumerate every experiment, ablation, cohort, or robustness check.

### Computational / ML benchmark or diagnostic paper

Prefer:

```text
failure/question -> controlled evaluation design -> one or two headline comparisons -> what the comparison diagnoses -> scope boundary
```

Do not reproduce the leaderboard.

A battery count, every comparator score, every confidence interval, every secondary test, and every implementation-control result rarely belong together in the abstract.

### Method / tool / software

Prefer:

```text
unmet need -> method identity -> validation against the most decision-relevant comparator(s) -> utility / generalization boundary
```

If the method itself is the contribution, the abstract may spend more space on what it does and how it differs from existing approaches.

### Theory / proof / formal framework

Prefer:

```text
formal problem -> central object/condition/theorem -> decisive implication/counterexample/bound -> scientific meaning
```

Exact quantities may be central. Do not add empirical-looking numbers merely to make the abstract feel concrete.

### Dataset / resource

Prefer:

```text
need -> what resource exists -> scientifically meaningful scale/coverage -> validation/quality -> intended use and boundary
```

Report scale only when it helps a reader judge what the resource actually enables.

### Review / Perspective / synthesis

Prefer:

```text
field-level problem -> synthesis lens or thesis -> major organizing insight -> consequences / research agenda
```

Do not fabricate a Results-style finding or imply primary empirical evidence.

### Clinical / regulated / reporting-mandated studies

Follow the applicable current reporting standard and exact journal structure.

For example, a structured randomized-trial abstract may legitimately require several numerical objects: numbers randomized/analyzed, group outcomes, effect size and precision, harms, and registration information. Do not apply a generic low-number heuristic that would make the abstract non-compliant or clinically uninterpretable.

## 4. The numerical-salience gate

The rule is **not** `maximum N numbers per abstract`.

Instead classify each candidate quantitative object:

```text
Q0 required reporting / design identity
   e.g. trial sample size when required by reporting standard

Q1 headline scientific anchor
   e.g. main effect/comparison, exact theorem quantity, decisive benchmark difference

Q2 secondary support
   e.g. robustness, secondary cohort, second battery, secondary metric

Q3 audit/provenance/process diagnostic
   e.g. number of search records, fixture counts, internal validation batteries,
        exact terminal counts, implementation-control totals

Q4 formatter residue
   e.g. 1.000000, 0.510417 when those digits do not change interpretation
```

Default manuscript-facing policy:

- include Q0 when the exact target/reporting standard requires it;
- include the minimum Q1 set needed to make the headline result concrete;
- include Q2 only when it supports a genuinely independent headline claim that cannot be communicated efficiently otherwise;
- move Q3 to the body, Methods, supplement, or artifact record unless it is itself the scientific result;
- remove or round Q4 using `numerical-reporting-precision.md`.

## 5. Treat an inferential result as one semantic bundle

Do not count digits mechanically.

A scientifically meaningful bundle can be:

```text
estimate + comparator + uncertainty
```

For example, an effect estimate and its confidence interval may be one necessary inferential object, not three unrelated numbers.

But an abstract that contains:

```text
battery A: n, score, comparator score, difference, CI, p
battery B: n, score, comparator score, difference, CI
battery C: n, score, comparator score
source audit: numerator/denominator
```

is probably reproducing the Results ledger rather than communicating the central claim.

## 6. Number-to-meaning test

For every number or quantitative bundle ask:

1. What headline proposition does this number support?
2. Would the reader understand the paper materially worse without it?
3. Is this the best number to carry that information?
4. Does it need its uncertainty, denominator, comparator, or unit to be interpretable?
5. Is it already better communicated in a table/figure/body section?
6. Does it create a new sub-story that the abstract cannot explain?

If the number does not survive these questions, remove it from the abstract.

### Prefer scientific resolution to software resolution

Use `numerical-reporting-precision.md`.

A finite benchmark result such as `49/96 (51.0%)` can be more informative than `0.510417` because it exposes the denominator and does not imply artificial precision.

Do not routinely expose six-decimal formatter output in the abstract.

## 7. Numeric-density warning patterns

These are review signals, not universal failures:

- several consecutive abstract sentences each containing multiple numerical bundles;
- more than one full benchmark/battery result described quantitatively;
- a secondary diagnostic receiving more numerical detail than the headline finding;
- exact `p` plus confidence interval plus multiple raw group values when one inferential object would suffice and no guideline requires all of them;
- multiple counts describing provenance/search/audit process rather than the scientific outcome;
- long decimal strings or repeated trailing zeros;
- model/dataset/test identifiers attached to many numbers before the reader knows why those objects matter.

For reporting-intensive clinical or regulatory abstracts, evaluate density against the applicable guideline rather than this generic pattern.

## 8. No abstract result catalogue

A research abstract should normally not read like:

```text
Experiment 1 did X.
Experiment 2 did Y.
Experiment 3 did Z.
Ablation A did ...
Audit B found ...
Search C found ...
```

Compress across experiments at the **claim level**.

Example transformation:

```text
Detailed:
Across three exact batteries, comparator A scores ..., comparator B scores ...,
control C scores ..., and audit D verifies ... .

Reader-facing:
Across controlled benchmarks, the representation-aware procedure eliminated the
failure mode that persisted under the strongest information-matched comparator;
an explicit computation control showed that the remaining residual was procedural
rather than informational.
```

Then retain one decisive number if it materially strengthens the statement.

## 9. Technical-term budget

Because the abstract is read before the paper's terminology has been activated:

- prefer scientific names over project IDs;
- avoid internal experiment labels such as `D1`, `M1`, `P4-X`, `V7` unless the label itself is a public field-standard object;
- avoid code/config/terminal vocabulary;
- avoid defining a dense private ontology inside the abstract;
- expand uncommon abbreviations unless the target/field clearly treats them as standard;
- do not make a table-like list of coined terms.

A term that requires two sentences of explanation probably should not be introduced in a short abstract unless it names the central contribution.

## 10. Prior-work budget inside the abstract

The abstract is usually not the place to perform detailed nearest-work accounting.

Default:

- no literature catalogue;
- no claim-subtraction narrative;
- no author-by-author comparison;
- no priority defense;
- no citations when the venue disallows them.

A compact contrast with prior capability may be useful when it is essential to identify the contribution, but it should normally be expressed by scientific function rather than a list of papers.

## 11. Method detail budget

Include only enough method information to identify what was done and why the result is credible.

Method detail earns space when:

- the method itself is the contribution;
- design is necessary to interpret the result;
- a comparator/control is central to the causal/diagnostic inference;
- a reporting guideline requires the detail.

Do not include implementation settings, paths, seeds, model checkpoints, every baseline, or full protocol chronology merely for reproducibility. Those belong elsewhere.

## 12. Boundary and limitation budget

The abstract should not become a compressed limitations section.

Include a boundary when omitting it would cause a reasonable reader to overgeneralize the headline claim.

Good boundary functions:

- finite/synthetic rather than naturalistic evidence;
- association rather than causal identification;
- formal result under explicit assumptions;
- method validated in one domain rather than universal deployment;
- non-certification result rather than evidence that all deployed systems exhibit the failure.

Do not stack multiple defensive sentences that merely repeat narrower versions of the same boundary.

## 13. Positive-claim visibility

After reading the abstract, a qualified reader should be able to underline one or two sentences that state what the paper actually establishes.

If every finding is immediately buried under `does not establish`, `should not be read as`, `cannot show`, and similar disclaimers, use `epistemic-rhetoric-and-qualification.md`.

Truthfulness and directness are compatible.

## 14. Abstract-to-paper consistency

Bind every abstract proposition to the current claim/evidence ledger.

For each abstract sentence record when useful:

```text
abstract_sentence_id
claim_ids
evidence_ids
number/result IDs
status/boundary
body locator
```

Block release if the abstract:

- contains a result absent from the paper;
- uses a stronger quantifier/generalization than the body;
- reports a stale number after reanalysis;
- changes the comparator, denominator, uncertainty semantics, or population;
- foregrounds a secondary result as if it were primary;
- omits a boundary required to make the headline claim accurate.

## 15. Write-order rule

A useful workflow is:

1. draft an abstract skeleton early to test whether the paper has a coherent claim;
2. do **not** polish it while the evidence architecture is still moving;
3. finalize the abstract after headline claims, evidence, terminology, numerical policy, and target budget are stable;
4. revise the title after the final abstract;
5. rerun abstract/body consistency after every conclusion-changing revision.

Do not generate the final abstract by mechanically truncating the Introduction or concatenating Results sentences.

## 16. Abstract reader-recovery test

Give only the abstract to a clean reader.

They should be able to answer:

1. What problem or gap motivates the work?
2. What did the paper actually do or establish?
3. What is the central result?
4. What evidence or formal result makes that answer credible?
5. What does the result mean?
6. What important boundary prevents overreading?

They should **not** need to decode project IDs, a benchmark genealogy, or a dense sequence of unexplained numbers.

## 17. Abstract economy audit

For every sentence ask:

```text
Does this sentence perform a unique entry-point function?
```

Typical deletion/merger candidates:

- second background sentence after the gap is already clear;
- detailed method phrase not needed to interpret the result;
- second or third numerical battery supporting the same claim;
- audit/provenance detail;
- repeated limitation;
- generic significance language;
- nearest-work accounting;
- exact number already made redundant by a clearer headline comparison.

The space recovered should strengthen the problem, central result, or meaning—not simply make the abstract shorter.

## 18. Release gate

Do not call an abstract ready when any applicable item fails:

- exact target abstract rule unresolved;
- word/character limit violated;
- central problem/question absent;
- central paper contribution not recoverable;
- headline result absent or buried under secondary details;
- numerical content is dominated by Q2–Q4 material;
- raw formatter precision remains;
- abstract contains unexplained private terms/project IDs;
- main implication is hype or unsupported;
- claim-changing boundary is absent;
- abstract and body disagree;
- a clean reader cannot recover the paper's scientific identity.

## 19. Non-negotiable transfer limits

Do not universalize:

- a fixed number of sentences;
- a fixed number of numbers;
- one IMRaD move sequence;
- one ratio of background/method/results/conclusion;
- one decimal-place rule;
- one stance profile.

Abstract conventions vary by discipline, paper archetype, journal, article type, and reporting standard.

The invariant is **minimum sufficient information for the central scientific case under the exact abstract regime**.
