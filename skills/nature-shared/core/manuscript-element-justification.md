# Manuscript element justification

> Shared contract for deciding whether every element of a scholarly manuscript earns its place. This generalizes content selection, paragraph necessity, sentence logic, figure-purpose reasoning, and venue-space allocation into one hierarchical rule.

## Governing invariant

Nothing belongs in a manuscript merely because it is true, available, conventional, already written, requested during revision, or produced by the analysis.

Every retained element must perform a justified reader-facing, scientific, reproducibility, compliance, or structural function **in this paper, at this location, in this form**.

The governing question is:

> Why is this element here, why here rather than elsewhere, and what useful reader/scientific capability would be lost if it disappeared or were represented differently?

This applies recursively to:

```text
paper
-> section
-> subsection
-> paragraph
-> sentence
-> clause when consequential
-> equation / definition / theorem / proof step
-> citation
-> example / case / caveat
-> table / figure / panel / caption
-> heading / transition
-> Methods detail
-> supplementary item
-> availability / compliance statement
```

The justification is an **authoring and review discipline**. Do not expose internal justification labels in manuscript prose.

## 1. Hierarchical justification tree

Treat the manuscript as a dependency tree rather than a flat collection of content.

Each child element must serve a function required by its parent.

Example:

```text
paper question
└─ Results section: establish bounded answer
   ├─ paragraph 1: establish primary phenomenon
   │  ├─ sentence 1: state local question
   │  ├─ sentence 2: report decisive comparison
   │  └─ sentence 3: bound local inference
   └─ paragraph 2: test strongest alternative
      ├─ sentence 1: motivate discriminator
      ├─ sentence 2: report test
      └─ sentence 3: update interpretation
```

A locally polished sentence does not earn its place if its paragraph is unnecessary. A useful paragraph does not earn its place in a section whose function is already complete. A technically correct section does not earn its place if the paper's argument does not require it.

Audit from the top down before polishing bottom-up.

## 2. Element justification record

For any element under active review, record enough of the following to make the decision explicit:

```text
element_id
element_type
parent_id
location
reader_question
function
incoming_dependency
new_contribution
outgoing_dependency
claim_ids / evidence_ids when applicable
deletion_consequence
placement_reason
representation_reason
redundancy_check
status: keep / compress / merge / move / replace / delete / unresolved
```

The record may be concise. Do not create paperwork that costs more reasoning than the content warrants.

## 3. Allowed functions

A retained element should perform at least one real function. Common functions include:

- **orient** — establish context, scope, system, population, or local question;
- **define** — give a reader-usable identity to a term, symbol, object, variable, condition, or distinction;
- **motivate** — explain why the next scientific operation is needed;
- **connect** — expose a real dependency between adjacent ideas, paragraphs, analyses, or sections;
- **evidence** — provide observation, comparison, proof, estimate, control, counterexample, or source support;
- **quantify** — make magnitude, uncertainty, denominator, scale, or operating regime recoverable;
- **interpret** — explain what evidence changes scientifically;
- **compare** — distinguish alternatives, methods, regimes, prior work, or hypotheses;
- **bound** — state assumption, limitation, failure regime, non-implication, or generalization boundary;
- **exemplify** — make an abstract object concrete when the example materially improves comprehension;
- **reproduce** — provide method detail necessary for interpretation or replication;
- **comply** — satisfy ethics, reporting, provenance, disclosure, attribution, or target requirements;
- **synthesize** — close several established points into a higher-level conclusion;
- **navigate** — help readers locate or decode material when navigation itself reduces cognitive cost.

An element may serve more than one function, but do not invent labels to protect weak material.

## 4. Reader-state test

For an important element, describe:

```text
before: what the intended reader can currently know / infer / locate
after: what becomes possible after this element
remaining uncertainty: what still does not follow
```

A retained element need not always add a new factual claim. A definition, transition, signpost, caption, or orientation sentence can be justified because it reduces ambiguity or processing cost.

But if `before` and `after` are materially identical and the element is not required for reproducibility/compliance, it is a strong deletion/compression candidate.

## 5. Deletion test

For every paragraph and for suspicious lower-level elements, ask:

> If this element disappears, what exactly breaks?

Valid answers include:

- a claim loses decisive support;
- a term becomes undefined before use;
- an inference becomes a jump;
- a comparison loses its baseline;
- uncertainty or denominator disappears;
- the strongest alternative is no longer tested;
- a conclusion becomes overgeneralized;
- a method can no longer be interpreted/reproduced;
- a reporting/ethics obligation is violated;
- the reader can no longer understand why the next paragraph/analysis exists.

Weak answers include:

- `it is interesting`;
- `we already wrote it`;
- `reviewers might like more detail`;
- `other papers usually have this`;
- `the analysis produced it`;
- `the section would look short without it`;
- `we have room under the word limit`.

If nothing breaks, delete, merge, compress, or move it.

## 6. Placement test

An element can be justified but misplaced.

Ask:

> Why must the reader encounter this **here**?

Main-text placement is justified when delaying the element would cause misunderstanding, mis-evaluation, or overgeneralization of the current argument.

Otherwise consider:

- Methods;
- figure/table/caption;
- Extended Data/SI;
- appendix;
- availability statement;
- repository/artifact documentation;
- response letter;
- omission.

Do not use smooth prose to hide a placement error.

## 7. Representation test

Even when the information is necessary, its current representation may not be.

Ask:

> Is this the lowest-friction, highest-information representation for the reader's task?

Examples:

- two exact values may belong in one sentence rather than a bar chart;
- a repeated list may belong in a compact table;
- a difficult relation may need an equation rather than three vague paragraphs;
- an equation may need one semantic sentence rather than a longer derivation in main text;
- a paragraph of benchmark values may belong in a plot/table plus interpretation;
- a definition may need to precede a table that uses its terms;
- a caveat may be merged into the claim sentence instead of repeated later.

For scientific displays use `figure-purpose-representation-optimization.md` and `scientific-display-decision-contract.md`.

## 8. Redundancy and unique-contribution test

A major claim may legitimately recur across abstract, Results, Discussion, and conclusion, but each occurrence must have a different job.

For each repeated element ask:

```text
What does this occurrence contribute that the others do not?
```

Legitimate differences include:

- introduce;
- demonstrate;
- decode;
- interpret;
- qualify;
- synthesize;
- operationalize;
- provide exact detail.

If two occurrences perform the same job for the same reader at the same level of detail, merge/delete one.

## 9. Paragraph contract

A paragraph is not a bag of sentences. It should normally have one dominant reader/scientific job.

For each paragraph identify:

```text
local question / nucleus
incoming dependency
required propositions
local conclusion or handoff
```

Then audit every sentence:

- Does it serve the paragraph nucleus?
- Does it inherit something identifiable?
- What relation does it have to the previous sentence?
- What new information or processing benefit does it add?
- Does it enable the next sentence or close the paragraph?
- Could it move almost anywhere without changing logic? If so, it may be orphaned.

A paragraph that needs only one sentence should become one sentence. A sentence that contains two independent jobs may need splitting. Do not enforce paragraph size mechanically.

## 10. Sentence and clause discipline

For claim-bearing or difficult sentences, use:

```text
inherits X
-> relation R
-> adds Y
-> enables Z
```

A sentence can be retained for cohesion/orientation even when `adds Y` is small, but the processing benefit must be real.

Audit clauses when they materially change meaning, scope, evidence, or readability. Do not create clause-level bureaucracy for ordinary fluent prose.

Remove or rewrite:

- generic prestige filler;
- meta-writing (`This section discusses...`) when direct scientific prose is clearer;
- connective stuffing without a real relation;
- repeated qualifications;
- throat-clearing before the actual result;
- sentences whose only function is to announce that an analysis was performed;
- sentences that restate a figure instead of interpreting it.

## 11. Citation justification

A citation must have a local scholarly function, not merely decorate a sentence.

For each citation cluster ask:

- Which proposition does this source support?
- Is the source needed for attribution, evidence, prior-art positioning, method provenance, or context?
- Is this the strongest/canonical/version-of-record source for that job?
- Are several citations doing the same job without added value?
- Does the manuscript accidentally cite a source merely because it appeared in the search ledger?

Do not turn exhaustive internal literature search into exhaustive manuscript citation.

## 12. Equation, definition, theorem and formal-element justification

A formal element earns main-text space when it defines the scientific object, exposes a relation readers must reason about, states a claim precisely, or enables later inference more efficiently than prose.

Ask:

- What later reasoning depends on this formal element?
- Is every symbol needed and defined before/at use?
- Could the same job be done more clearly with a simpler equivalent form?
- Is a displayed equation justified, or would inline notation suffice?
- Is the derivation central, or should routine detail move to appendix/SI?
- Does compression preserve the contribution-defining formal spine?

Do not add equations to make a paper look rigorous.

## 13. Example and caveat justification

Examples are useful when they disambiguate a definition, expose a boundary, demonstrate a failure mode, or materially reduce abstraction cost.

Delete examples that merely repeat the same intuition.

Caveats are necessary when they prevent a materially wrong inference. They are not a requirement to enumerate every imaginable limitation after every claim.

Prefer one precise boundary at the point where it matters over repeated defensive prose.

## 14. Headings and transitions

A heading earns its place when it helps the reader predict or locate a meaningful scientific unit.

Avoid headings that expose internal workflow (`Claim subtraction`, `V3 audit`, `Post-saturation successor`) rather than reader-facing science.

A transition earns its place when it exposes a real dependency that is not otherwise recoverable. `Moreover` or `Next` does not justify an unrelated paragraph.

## 15. Element-value and opportunity-cost test

Publication space and reader attention are scarce.

For optional elements ask conceptually:

```text
value
≈ reader understanding gained
 + evidential strength gained
 + interpretability gained
 + reproducibility/compliance gained when needed
 - duplication
 - cognitive burden
 - displaced higher-value science
```

Do not turn this into a fake numerical score.

When a new element is proposed under a fixed venue budget, identify what it displaces or which reserve funds it.

## 16. Revision-accretion rule

A reviewer request, author thought, or new analysis does not automatically append prose.

For each proposed addition:

1. state the new function;
2. identify whether an existing element already performs it;
3. prefer replacement, merge, compression, or relocation before append;
4. re-run deletion and redundancy tests on the affected parent paragraph/section;
5. preserve decision-changing evidence and mandatory reporting.

## 17. Adaptive audit granularity

The invariant applies to every element, but the **audit depth is proportional to risk**.

Default:

- paper/section architecture — always justify;
- every paragraph — justify during substantial drafting/revision/review;
- every sentence — audit in central, dense, confusing, high-stakes, or suspicious paragraphs;
- clauses — audit only when they change logic, scope, qualification, or readability;
- citations/formal objects/displays — justify whenever claim-bearing or space-expensive.

Escalate granularity when there is:

- unexplained terminology;
- weak logical connection;
- defensive/repetitive prose;
- very tight word limits;
- reviewer-request accretion;
- central formal/statistical claims;
- a surprising table/figure/model/dataset appearing without setup;
- clean-reader failure.

This preserves AI-session efficiency while keeping the invariant universal.

## 18. Clean-reader deletion challenge

For a mature manuscript, a clean reviewer should sample central and randomly chosen elements and ask:

1. What job does this element perform?
2. What does it depend on?
3. What later reasoning depends on it?
4. What breaks if it is removed?
5. Why is it here rather than elsewhere?
6. Why is it represented this way?
7. Is there a shorter/clearer equivalent that preserves the same scientific function?

If the reviewer cannot answer, the element is unresolved rather than automatically retained.

## 19. Blocking failures

Block or require revision when:

- a central paragraph has no identifiable scientific/reader job;
- a claim-bearing sentence has no recoverable relation to its context;
- an element is necessary but appears only after the first place that depends on it;
- a repeated element has no unique function;
- a main-text element is clearly better placed in Methods/SI/artifact documentation and disrupts the argument;
- a space-expensive element displaces contribution-defining explanation/evidence without comparable value;
- a citation/formal/display element is included by habit rather than a local scholarly job;
- removing an element changes nothing and no reproducibility/compliance requirement protects it;
- revision accretion creates multiple elements serving the same function.

## 20. Boundary

This contract does not mean every sentence must be maximally dense or every paragraph must advance a new claim. Scientific writing needs orientation, definitions, transitions, examples, and breathing room.

The criterion is not `new fact per sentence`.

It is:

> **Every retained element must make a defensible contribution to understanding, evaluation, inference, reproduction, compliance, or navigation that is worth its local cost.**

Final rule:

> **If an element cannot explain why it exists, why it is here, and what the manuscript loses without it, it has not yet earned its place.**
