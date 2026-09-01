# Paper existence and scientific mass gate

> Fail-closed contract for deciding whether a scientifically bounded result should become a full paper at all, whether it needs more evidence, whether it should merge with a sibling contribution, or whether it belongs as a note/resource/internal record. This gate sits above claim correctness and below manuscript polish. Last reviewed: 2026-09-01.

## Why this gate exists

A manuscript can be internally correct, reproducible, carefully qualified, and still be too weak, too derivative, too fragmented, or too under-observed to justify a standalone paper.

The ordinary paper pipeline is good at repairing overclaiming by narrowing claims. That creates a second-order failure mode:

```text
ambitious claim
-> hostile review
-> claim narrowed until technically defensible
-> manuscript polished
```

The missing question is:

> **After the claim has been narrowed to what the evidence really supports, is the surviving scientific object still large enough and independent enough to justify this publication form?**

Claim support and paper existence are different states. A green build, complete claim ledger, exact reproducibility record, or submission package does not answer the paper-existence question.

## Mandatory trigger

Run this gate for any substantial publication-oriented project:

- before committing to a full-paper manuscript;
- after a headline claim is materially narrowed or a central result is withdrawn;
- after hostile review reveals that the main evidence is a protocol demonstration, synthetic conformance test, tiny independent sample, interface mismatch, or same-programme gold;
- when several sibling papers share adjacent theory, data, benchmark families, terminology, or implementation machinery;
- before declaring a paper `simulated_publication_ready_for_target`, `submission_ready`, or an equivalent terminal;
- whenever a user asks which projects should be published, merged, deferred, downgraded to a note, or stopped.

A project that already has a complete manuscript is **not exempt**. If the surviving scientific object fails this gate, stop polishing and return the appropriate non-writing terminal.

## Independent hostile panel

Use at least five logically independent lenses. They may be executed by separate agents/contexts or by one system under frozen independent passes, but each pass must be completed before synthesis.

1. **Field/action editor** — asks whether an informed reader learns a sufficiently important new fact and whether the contribution deserves standalone attention.
2. **Methods/benchmark/statistics reviewer** — attacks independent units, controls, baselines, nuisance shortcuts, scorer latitude, effective sample size, uncertainty, and external validity.
3. **Theory reviewer** — strips project vocabulary, maps results to standard mathematical/statistical/computer-science lineages, and distinguishes new theorem content from renamed known facts or direct corollaries.
4. **Systems/reproducibility reviewer** — separates evidence that a computation happened correctly from evidence that the scientific interpretation is valid; attacks simplest implementations and unnecessary machinery.
5. **Literature/portfolio reviewer** — names the nearest current papers and sibling manuscripts, tests feature-union/combinatorial novelty, and asks whether merging would produce one stronger contribution.

Do not count votes. Synthesis is argument-weighted. A single valid fatal objection can block a full paper.

## Required decision object

Materialize a paper-existence ledger conforming to:

`../analysis-contracts/paper-existence-scientific-mass.schema.json`

Validate it with:

`../scripts/verify_paper_existence_scientific_mass.py`.

The decision object must identify the current surviving claim, actual independent scientific units, nearest external neighbours, sibling overlap, simplest mechanism, serious baselines, theory lineage, external-validity level, integrity-vs-validity distinction, and the cheapest next evidence that would materially change the decision.

## The hostile gates

### G1 — Paper existence / posterior-change gate

State the strongest surviving result in ordinary field language with project branding removed.

Then answer:

```text
What new fact would an informed reader believe differently after seeing this result?
What observation, theorem, mechanism, or negative result causes that belief change?
Would the paper still exist if all workflow, receipt, audit, packaging and project-governance machinery were moved to an appendix/repository?
```

Fail the full-paper route when the surviving result is only one or more of:

- “we implemented the protocol once”;
- “the system obeyed the rules we encoded”;
- “the repository can replay the computation”;
- “two internally related components agreed once”;
- “we created a schema/ontology/ledger” without evidence that it resolves a field-level problem;
- “no prior paper has exactly this combination of named components” without an emergent result caused by the combination.

These objects may still justify a protocol, benchmark/resource, software, methods note, technical report, or internal record.

### G2 — Scientific payload / mass gate

Count **independent scientific observations**, not files, test cases, receipts, generated rows, seeds, commits, proof scripts, or manuscript artifacts.

Record:

- independent experimental/observational units;
- independent domains/programmes/sites/providers/operators where relevant;
- theorem/proof objects that are genuinely logically independent;
- negative/null/adverse observations retained;
- number of materially distinct failure opportunities;
- amount of implementation/governance/audit material required only to establish provenance or reproducibility.

Do not create a universal numeric threshold. Instead ask whether the current evidence mass can support the exact population/domain/importance claim being made.

A large generated benchmark with 10,000 rows may still have an effective scientific `N` of 5 attack families. A prospective benchmark executed on one frontier remains one prospective unit even if it has many typed records.

### G3 — Effective-N and dependence gate

Identify the unit at which outcomes could genuinely have varied independently.

Explicitly test for:

- repeated cases generated from one template/family;
- attack-family or subject clustering;
- multiple seeds over one underlying dataset;
- repeated measurements from one model/programme/operator;
- pseudo-replication from decomposing one scientific event into many rows;
- case-level uncertainty intervals whose scientific inference unit is a higher-level cluster.

Report both the raw row count and the scientifically defensible independent-unit count when they differ materially.

### G4 — Minimum-mechanism / trivial-baseline attack

Construct or specify the simplest credible mechanism that could reproduce the headline result.

Examples include:

- timestamped JSON + evidence hash + preregistered scorer instead of a large temporal benchmark framework;
- a few explicit if/then gates instead of a complex authority architecture;
- majority/default policy;
- cheapest-intervention-first;
- simple logistic/tree/meta-classifier;
- a direct mathematical computation instead of a learned architecture;
- a standard data structure instead of a new named ontology.

If the simple mechanism matches the scientific benefit, the paper must explain and demonstrate what additional capability the proposed machinery buys. Complexity, typing, auditability, extensibility, or architectural elegance are not scientific benefit by themselves unless the paper measures the resulting property.

### G5 — Strong-baseline diversity gate

A serious empirical paper should not win only against a deliberately weak foil.

Where scientifically applicable, cover multiple baseline roles:

- trivial/default/majority/random;
- cheapest or most common operational heuristic;
- strong conventional method;
- nearest published method/benchmark;
- learned/meta baseline;
- human/expert baseline;
- oracle/upper-bound or information-matched control;
- ablation of the exact proposed mechanism.

Not every paper needs every role. Missing roles require a reason tied to the estimand, not convenience.

### G6 — Named nearest-neighbour gate

Do not position only against categories such as “static benchmarks”, “multi-agent debate”, “provenance systems”, or “graph methods”.

Name the 3–6 closest current primary works and compare them head-to-head on:

```text
scientific question
independent unit / data regime
information available
intervention or comparison
outcome / score
prospective vs retrospective timing
baseline strength
external validity
what the new paper measures that the neighbour cannot
```

Search changed vocabulary and adjacent fields. If a close 2025–2026 work materially changes the novelty boundary, rewrite the contribution around the residual or stop the standalone route.

### G7 — Feature-union / combinatorial-novelty attack

When every component already exists in prior work, ask:

> If the contribution is “A + B + C + D”, what phenomenon becomes measurable or possible only because they are coupled?

A checklist of individually known features is weak novelty unless the coupling yields a new theorem, identification result, empirical effect, failure mode, benchmark capability, or useful decision consequence.

The ledger must distinguish:

- component novelty;
- composition novelty;
- emergent scientific result;
- engineering integration value.

Do not convert “no paper has exactly this feature vector” into a strong novelty claim.

### G8 — Portfolio anti-fragmentation / merge attack

For each sibling paper or manuscript sharing substantial machinery, ask:

```text
What exact scientific question is uniquely owned by each paper?
What unique evidence object or theorem would disappear if the papers were merged?
Would one combined paper be clearer, stronger, and less repetitive?
Does the separation exist for readers, or only in an internal ownership ledger?
```

Return `MERGE_WITH_SIBLING` when the standalone scientific separation is not reader-visible or when splitting mostly distributes one framework across adjacent terminology.

Internal claim-ownership maps are useful provenance but do not by themselves justify multiple archival papers.

### G9 — Designer's-advantage / same-programme-gold gate

When the same programme authors the ontology, benchmark construction, gold labels, candidate rule, scoring relation, and evaluation code, distinguish:

- semantic/specification conformance;
- benchmark performance;
- external scientific validity.

Attack whether the result could be true merely because the system and benchmark encode the same designer assumptions.

Repairs can include:

- external adjudication;
- separately governed gold;
- independent task generation;
- hidden adversarial cases by a team that did not see the rule;
- naturally occurring cases;
- source-disjoint replication;
- strong deployed-style donor/baseline at matched information.

Do not label same-programme agreement as independent scientific corroboration.

### G10 — Benchmark discrimination and failure-opportunity gate

For each claimed axis, verify that the benchmark could have produced a scientifically meaningful failure.

Ask:

- does the metric vary across plausible systems?
- are positive/benign cases difficult enough to expose unnecessary refusal or false negatives?
- are negative/hostile cases difficult enough to expose unsafe promotion?
- does the benchmark contain disagreement, partial resolution, invalidation, and cannot-check cases when those semantics are central?
- is the outcome recoverable from nuisance cues such as length, missing fields, naming, ordering, or templates?

A saturated axis is a design limit, not a positive comparative result.

### G11 — Comparator interface-parity gate

Before interpreting a score difference as capability, verify that compared systems can express the target terminal/action.

If one comparator cannot emit `CANNOT_CHECK`, abstain, escalate, or another required state, the measured gap may be interface attainability rather than epistemic or decision quality.

Use a predeclared semantics-preserving adapter when valid. Otherwise narrow the claim to interface expressiveness.

### G12 — Scorer-latitude and post-outcome flexibility gate

For deferred scoring, qualitative alignment, expert adjudication, or broad success criteria:

- define what future evidence would make the original decision clearly wrong;
- enumerate plausible alternative decisions at freeze time;
- bind scorer rules before outcome access where possible;
- measure scorer agreement or adjudication stability when interpretation is nontrivial;
- preserve `UNRESOLVED` and `INVALIDATED` instead of forcing success/failure;
- test whether many future outcomes would have been called “aligned”.

A scorer that can reinterpret a broad decision after the fact does not supply a strong prospective result.

### G13 — External-validity ladder

Classify the strongest evidence actually executed:

```text
L0 specification / unit tests / proof-of-concept
L1 synthetic authored cases
L2 protected synthetic or procedural holdout
L3 historical real data or retrospective natural cases
L4 live prospective same-programme cases
L5 multi-programme / multi-domain prospective or naturalistic cases
L6 externally governed/adjudicated or source-disjoint replication
L7 deployed independent use / replication where the target claim requires it
```

The level is descriptive, not a score. Claim scope must not outrun the level actually reached.

A paper may be excellent at L1–L2 if its contribution is formal or benchmark-measurement theory. It may be inadequate there if it claims scientific judgement, general prediction, calibration, deployment reliability, or broad domain utility.

### G14 — Theory lineage / vocabulary stripping gate

For every central theorem, proposition, bound, or formal characterization:

1. remove project-specific names and symbols;
2. restate it in standard field language;
3. map it to the nearest established theorem families;
4. identify which part is known, a direct corollary, a new specialization, or genuinely new;
5. verify that the proof contributes more than terminology substitution.

Explicitly search classical lineages when relevant: Bayes risk/sufficiency, Blackwell comparison of experiments, data processing, hypothesis testing/total variation, lattice/order theory, type systems, program logics, provenance, authorization logics, information theory, category/sheaf/graph formulations, and field-specific predecessors.

Known mathematics may still be valuable as an explanatory tool. Label it as such instead of manufacturing theorem novelty.

### G15 — Integrity versus scientific-validity gate

Maintain two separate ledgers:

**Integrity / execution evidence** answers:

- were these exact bytes/data/code used?
- can the computation be reproduced?
- were receipts, splits, epochs, and provenance preserved?
- did the implementation satisfy the declared contract?

**Scientific-validity evidence** answers:

- does the benchmark measure the intended construct?
- are the gold labels/assumptions defensible?
- are alternatives ruled out?
- are baselines fair?
- does the result generalize to the claimed scope?
- has an independent scientific party corroborated the conclusion where required?

Never let more integrity artifacts substitute for missing scientific observations.

### G16 — Authority synchronization gate

One authoritative scientific state must generate or constrain:

- title;
- abstract;
- introduction/contribution bullets;
- results;
- figures/tables;
- claim ledger;
- README/readiness summary;
- submission package.

If the current README says the paper's scientific identity changed but the canonical manuscript still foregrounds the retired result, the paper is not ready regardless of build status.

### G17 — Evidence-acquisition stop rule

For every open scientific blocker, ask:

> What next observation, computation, proof, external adjudication, baseline, or experiment would most reduce uncertainty about whether this paper should exist in its current form?

If a real evidence acquisition dominates further prose work, return `WAIT_FOR_EVIDENCE` and **block additional manuscript polishing** except protocol preparation, analysis code, preregistration, or text needed to execute that evidence.

Do not keep generating readiness ledgers, prose revisions, figures, or reviewer simulations when none can change the scientific terminal.

## Re-run after claim narrowing

This is mandatory.

If a headline claim changes from, for example:

```text
system predicts useful scientific decisions
```

to:

```text
we executed the decision-recording lifecycle once and later evidence was compatible with the recorded move
```

then the pipeline must not celebrate merely because the second claim is supportable. Re-run this gate against the surviving result.

A claim can become valid while the paper becomes too small.

## Publication-form decisions

The gate must return exactly one primary disposition:

### `WRITE_FULL_PAPER`

Use only when the surviving contribution has sufficient scientific mass, a defensible novelty residual, fair comparisons/lineage, and evidence maturity for the intended full-paper claim.

This does not mean a top-tier venue is earned. Targeting is resolved separately.

### `WAIT_FOR_EVIDENCE`

Use when the question is promising but the decisive experiment, computation, independent unit series, baseline, external adjudication, proof, or replication has not yet been executed.

Output the minimum evidence-acquisition checklist and stop prose optimization that cannot alter the decision.

### `MERGE_WITH_SIBLING`

Use when a sibling contribution supplies the same scientific spine or when combining the results would produce one substantially stronger and clearer paper without losing a genuinely independent question.

Name the merge candidates and the surviving combined contribution.

### `RECLASSIFY_AS_NOTE`

Use for useful but sub-paper scientific objects such as:

- protocol/specification with no mature empirical series;
- reproducibility or implementation note;
- benchmark/resource release whose scientific claim is intentionally narrow;
- negative technical finding;
- internal research record;
- appendix/supplement/successor protocol.

Specify the appropriate note/resource/internal form rather than treating this as failure.

### `KILL_CLAIM`

Use when the contribution is subsumed, defeated by a valid hostile control, depends on an invalid comparison, cannot be repaired without changing the scientific question, or no longer offers a meaningful residual.

Preserve adverse evidence and provenance. Killing a claim must not delete the research history.

## Top-tier and second-tier readiness

Do not create universal prestige rules or acceptance probabilities.

For portfolio triage, use these descriptive tiers only after the paper-existence disposition is `WRITE_FULL_PAPER`:

- **top-tier candidate** — central result is difficult to explain away, nearest work is directly beaten or sharply differentiated, effective independent evidence is strong for the claim, external-validity level matches the breadth asserted, serious baselines/alternatives are covered, and the result changes field-level understanding rather than only project-level implementation;
- **second-tier / strong specialist candidate** — scientifically sound and independently useful, but narrower in scope, evidence breadth, external validity, impact, or theoretical reach;
- **not yet venue-ready** — the full paper may exist conceptually, but a real evidence/analysis/lineage/synchronization blocker remains.

Exact journal fit and current policy remain governed by the venue-decision and acceptance-readiness contracts.

## Portfolio review output

When reviewing multiple papers, emit a table with at least:

```text
paper_id
dominant contribution type
strongest surviving claim
scientific independent N / unit
external-validity level
fatal/major hostile concern
paper-existence disposition
top-tier route status
second-tier route status
minimum next evidence/computation/theory task
merge/internal-note candidate
```

Then produce a **checkable execution plan**. Every task must say what observation or closure test changes the disposition. Avoid vague items such as “improve experiments” or “strengthen related work”.

## Release invariant

A paper cannot receive a full-paper simulated readiness terminal while this gate is in any of:

```text
WAIT_FOR_EVIDENCE
MERGE_WITH_SIBLING
RECLASSIFY_AS_NOTE
KILL_CLAIM
UNRESOLVED
```

Packaging readiness and paper-existence readiness are orthogonal. A perfect submission ZIP can package a scientifically immature paper.

## Minimal user-facing synthesis

For each paper, state plainly:

1. **what is genuinely new**;
2. **what the evidence actually proves**;
3. **the strongest hostile reason not to publish it as a standalone full paper**;
4. **the disposition**;
5. **the cheapest valid path to a stronger disposition**.

Do not soften `WAIT`, `MERGE`, `NOTE`, or `KILL` into generic “minor revisions”.
