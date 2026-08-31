# Standalone manuscript and zero-context reader contract

> Shared release contract for treating every paper as an independent scholarly object rather than a projection of a repository, research programme, paper series, audit ledger, or prior conversation. Last reviewed: 2026-08-31.

## Purpose

A manuscript can be scientifically correct and still fail as a paper when it assumes that the reader already knows the project's private vocabulary, experiment genealogy, artifact structure, companion papers, internal statuses, or development history.

The governing invariant is:

> **Every paper must first stand on its own for a qualified reader who has never seen the project, repository, internal notes, earlier papers, review history, or authoring pipeline.**

Self-contained does not mean textbook-complete. It means the paper supplies every paper-specific identity, definition, dependency, comparison, and boundary required to understand and evaluate its own contribution.

This contract is complementary to `explanatory-sufficiency.md`, `terminology-ledger.md`, `manuscript-content-selection.md`, `scholarly-surface-semantics.md`, and `formal-spine-preservation.md`. Those contracts remain necessary. This one adds a stronger independence requirement and a reading-order test.

## 1. The paper is the primary public object

Treat these as different layers:

```text
private project / repository state
-> authoring and verification state
-> manuscript-facing scientific state
-> external scholarly reader
```

The manuscript is not a serialized copy of the first two layers.

Internal objects may be essential for provenance or reproducibility without being good reader-facing vocabulary. Translate them into scientific meaning before they reach the paper.

A fact earns manuscript space because it helps the reader understand, evaluate, reproduce, or correctly bound the science, not because the repository records it.

## 2. Zero-context reader baseline

Before drafting, freeze a reader baseline that assumes no knowledge of:

- the repository or directory structure;
- internal project codenames;
- paper numbers in a series;
- prior chat or author notes;
- development-stage identifiers;
- protocol IDs;
- machine terminal names;
- previous simulated reviews;
- unpublished companion-paper definitions;
- internal claim ledgers, donor maps, ownership maps, or novelty audits.

The intended reader may still be a field specialist. Standard field knowledge may be assumed when appropriate. **Project-private knowledge may not.**

### Zero-context reconstruction question

At each major checkpoint ask:

> Could a qualified reader encountering only this manuscript explain what the paper studies, what its central objects mean, what was compared, why the comparison matters, what the main result is, and where the claim stops?

If not, the manuscript is not standalone even if the missing information exists somewhere in the project.

## 3. Reading-order definition law

A definition that appears later in the manuscript does not repair an opaque earlier use.

For every paper-private term, label, symbol, experiment name, metric, state, or abbreviation, record:

```text
first occurrence
reader-facing identity
meaning / denotation
scientific role
whether a short identifier is needed afterward
```

At its first claim-bearing use, the reader must already be able to recover the identity and role.

This is stronger than global terminology consistency. It is a **temporal dependency constraint**:

```text
meaning available before use
```

not merely

```text
meaning exists somewhere in the paper.
```

### Examples

Bad:

`D1 improves transfer relative to the baseline.`

when `D1` is defined several pages later.

Better:

`We next test whole-domain procedural transfer (experiment D1), training on two procedural domains and holding out a third in its entirety.`

After that local definition, `D1` may be used sparingly if it saves space.

Bad:

`M1 reaches its ceiling.`

Better:

`The simple-model stage (M1) first asks whether generic classical learners can exploit the information already present in each view.`

## 4. Reader-facing name first; internal identifier second

For experiment/study/module identifiers such as `D0`, `D1`, `M1`, `A5`, `V3`, `P4-X`, `H2`, or similar project-local shorthand, use this order:

```text
reader-facing scientific name first
(optional internal identifier second)
```

Do not make internal IDs the primary nouns of the paper.

Use an ID only when at least one of these is true:

- the paper repeatedly compares several experiments and the ID reduces genuine ambiguity;
- the ID is needed to link a preregistration or public artifact;
- the venue convention strongly favors numbered studies/hypotheses;
- the identifier itself is a public standardized term.

Otherwise omit it.

### Hypotheses

`H1`, `H2`, and similar labels may be useful, but the plain-language hypothesis must be stated first or simultaneously. The reader should never need to remember a code to know what was tested.

## 5. Paper-series independence

A manuscript in a larger programme must not require another paper in the series to be intelligible.

Avoid reader-facing constructions such as:

- `Paper III owns...`;
- `as established in P4...`;
- `the later programme...`;
- `our previous internal paper defines...`;
- `the predecessor/successor terminal...`.

When prior work from the same programme is genuinely necessary:

1. cite it as ordinary scholarly prior work if it is public/accepted and citable;
2. restate the minimum definition or result required for the current paper;
3. explain what the current paper adds without requiring the reader to reconstruct the programme chronology;
4. do not use an unpublished/internal companion document as the sole support for an externally facing scientific claim.

A series label may appear as navigation metadata, not as a substitute for scientific explanation.

## 6. Private research-management vocabulary stays private by default

The following kinds of language are usually authoring or programme-management objects rather than manuscript concepts:

- `claim subtraction`;
- `donor family`, `donor-owned`, `donor-complete` unless explicitly formalized as a scientific object;
- `parent`, `strongest parent`, `nearest-work disposition`;
- `post-saturation successor`;
- `claim owner`;
- `promotion terminal` when ordinary outcome/state language is sufficient;
- `gate`, `microgate`, `freeze`, `receipt`, `ledger`, `binding`, `custody`, `pass` when the specific governance mechanism is not itself the study object;
- machine state strings such as long upper-snake identifiers;
- internal version histories such as `V2 -> V3 -> V4 -> ...` when the reader only needs the final scientifically distinct studies.

These concepts can still be useful internally for rigor. Their output should be the **scientific conclusion they support**, not the bookkeeping vocabulary itself.

### Translation examples

Internal:

`P9_NEURAL_ESCALATION_NOT_JUSTIFIED`

Reader-facing:

`The current evidence does not justify escalation to a more complex learned model.`

Internal:

`PUBLIC_V3_NO_HARM_SUPERIORITY`

Reader-facing:

`The revised evaluation achieved complete envelope coverage but did not improve the declared downstream harm relative to the comparator.`

Internal:

`donor-complete product`

Reader-facing, when this is what is meant:

`a comparator supplied with provenance, verification, version, and custody information but not the target-specific decision relation`.

If the compact term is genuinely useful after this definition, it may be introduced secondarily.

## 7. Claim subtraction is an authoring operation, not a manuscript section

The pipeline should privately perform:

```text
candidate contribution
- what the closest prior work already establishes
= surviving contribution
```

Do **not** normally expose this operation as a section called `claim subtraction`, `ownership`, `donor engulfment`, or similar.

The manuscript should show the result through ordinary scholarly positioning:

- what the closest work already does;
- what remains unresolved or untested;
- what this paper specifically changes or tests;
- what the paper does not claim.

A defensive inventory of who `owns` each ingredient is not a substitute for synthesis.

## 8. Related work is a function, not a mandatory section

A separate `Related Work` section is optional unless the target/article type requires or strongly expects it.

Prior work can instead be integrated into:

- the Introduction, where it establishes the research need;
- Methods, where it motivates a consequential method choice;
- Results, where a comparator or prior finding is directly interpreted;
- Discussion, where the result is placed into the field;
- a concise dedicated section when the field/venue benefits from one.

### Proportionality rule

The reader needs **enough prior work to understand and evaluate the contribution**, not an exhaustive catalogue of everything found during search.

Prefer synthesis around scientific questions or contrasts over one paragraph per paper/family.

Bad pattern:

```text
Work A does X.
Work B does Y.
Work C does Z.
None owns our residual.
```

Better pattern:

```text
Existing approaches solve extraction and schema alignment, while provenance-aware methods preserve source context. The unresolved question for this study is narrower: when two structured claims are locally compatible, what conditions justify treating them as scientifically identical?
```

Citations then support the synthesized clauses.

### Dedicated-section trigger

Create a dedicated related-work section only when it performs a real reader function, for example:

- the venue convention expects it;
- several distinct literatures must be reconciled before the contribution is understandable;
- the closest comparator needs more technical contrast than the Introduction can carry;
- novelty would otherwise be difficult to assess.

Do not create it merely because a generic paper template contains one.

## 9. Development chronology is not the default Results structure

The repository may contain many scientifically responsible iterations. The paper should not automatically narrate all of them.

Use the **scientifically smallest set of distinct studies/results** needed to support and bound the claim.

Collapse implementation/development history when later stages differ only by:

- runtime repair;
- parser/adapter repair;
- path or schema correction;
- dependency compatibility;
- artifact-shape validation;
- repeated identity preflight;
- a failed attempt whose only consequence is engineering provenance.

Retain a failure in main text when it changes scientific interpretation, estimand validity, comparator identity, generality, or the design of a decisive subsequent test.

Otherwise move it to:

- Methods;
- Supplementary Information;
- artifact documentation;
- a machine-readable provenance timeline.

A reader should see the **scientific dependency graph**, not necessarily the Git/history graph.

## 10. Audit-log prose must be projected into scientific prose

Replace event-log narration such as:

`V17 failed, V18 repaired the surface, V19 changed the universe, V20 passed, V21 rescored...`

with the scientific relation, for example:

`After correcting an interface mismatch without changing the ontology or reference data, both systems could be scored on the same frozen case. The resulting comparison is therefore valid for that case only.`

The detailed stage identifiers remain in the artifact map.

## 11. Reproducibility does not require repository dumping

A manuscript should provide one clear access path to the reproducibility package, then report the scientifically consequential identities.

Prefer:

```text
Data, code, protocols, and frozen evaluation artifacts are available in the archived repository [persistent identifier]. A machine-readable manifest maps each reported result to the corresponding immutable artifact.
```

over pages of:

- source paths;
- JSON filenames;
- script paths;
- hashes for every intermediate object;
- CLI commands;
- `make` targets;
- branch/PR identifiers;
- internal development directories.

Exact file-level detail belongs in the repository manifest or a venue-required artifact appendix unless a particular identity is itself necessary to understand or reproduce a central result.

Do not confuse **auditability of the package** with **readability of the manuscript**.

## 12. Definition completeness for scientific objects

Every central paper-specific construct must receive, before use as an inference-bearing object:

1. identity — what it is;
2. distinction — how it differs from nearby concepts;
3. role — why the paper needs it;
4. operational/formal definition where consequential;
5. boundary — what it does not mean when ambiguity is likely.

An equation alone does not necessarily satisfy this requirement. A name alone does not either.

For mathematical papers, symbols additionally require their domain/codomain or quantification when nonstandard and necessary for interpretation.

For empirical papers, experiment codes do not count as definitions of the experimental intervention or comparison.

## 13. Borrowed terminology from neighbouring work

Do not silently inherit project-private terminology from a neighbouring/companion paper merely because the authoring context contains it.

Classify every recurring term as:

- established field term;
- public coined term from a citable source;
- paper-defined term;
- private/project-local term.

For a public coined term, cite and explain it at the depth needed locally.

For a private term, either:

- replace it with field-standard language;
- define it as a new term only if the current paper genuinely needs it;
- omit it.

Do not create a chain in which Paper B is only intelligible after reading Paper A's private vocabulary.

## 14. Introduction independence test

By the end of the Introduction, a qualified target reader should be able to answer:

- What scientific problem is being addressed?
- What has relevant prior work already established?
- What remains unresolved for this paper?
- What is the paper's bounded contribution or question?
- What kind of evidence/theory will answer it?
- Which central coined terms, if any, must be remembered?

The Introduction should not require knowledge of internal experiment numbers or programme chronology to answer these.

## 15. Methods first-use test

At the start of each Methods/Problem-formulation object, ask:

- Is the scientific object named descriptively before any code?
- Are its inputs, outputs, conditions, and role recoverable?
- Is an internal identifier truly necessary?
- Has a reader seen every symbol/term needed to understand the next equation or experiment?

If not, rewrite before continuing.

## 16. Results local-orientation test

Every major Results block should begin from the local scientific question, not from an internal stage ID.

Prefer:

`We next asked whether the remaining error reflected missing information or a computation that the learner did not execute.`

not:

`M1 then motivated A5.`

The reader should be able to enter a Results subsection from its heading and opening paragraph without consulting the repository genealogy.

## 17. Conclusion independence test

The Conclusion should synthesize the scientific findings, not replay the full version history.

Do not require the reader to remember a chain of `V2`, `V3`, `V4`, `V5`, `V6`, etc. to understand the take-home message.

Name distinct scientific evidence layers descriptively, for example:

- controlled synthetic study;
- protected replication;
- exact-contract boundary test;
- one-case external comparison;
- prospective naturalistic study not yet executed.

## 18. Clean-room reader review

For full-manuscript readiness, perform a clean reader pass with no project context.

The reviewer receives only:

- the current manuscript;
- the target journal/article type if relevant;
- public/citable sources needed for fact checking.

The reviewer must not receive:

- repository terminology ledger;
- prior papers unless encountered through ordinary citations;
- author claim-subtraction notes;
- internal experiment genealogy;
- artifact paths;
- previous review/revision rationale.

Ask the reviewer to reconstruct:

```text
paper question
central contribution
central definitions
study/experiment identities
main comparisons
main result
strongest limitation
relation to closest prior work
```

Then record every term or transition that required guessing.

A paper fails this gate when the reviewer can only reconstruct the argument by importing unstated project context.

## 19. Release blockers

Do not call a manuscript submission/publication ready while any of the following remains true:

- a paper-private term is used before its reader-facing definition;
- an opaque experiment ID is the primary identity of a central study without local explanation;
- title/abstract depend on internal programme labels;
- the paper requires an unpublished companion paper to understand a central construct;
- `claim subtraction`, donor/parent/ownership bookkeeping, or novelty-audit language is exposed as manuscript rhetoric without scientific necessity;
- machine terminal strings or repository paths replace reader-facing outcomes;
- development chronology dominates the Results despite not changing scientific interpretation;
- the availability section functions as a file manifest rather than an access statement;
- a clean zero-context reader cannot reconstruct the paper's central argument from the manuscript alone.

## 20. Legitimate exceptions

This contract does not ban:

- numbered experiments/studies/hypotheses when they are clearly defined and useful;
- public standardized labels such as `D1` when they are genuinely standard in the field;
- a dedicated Related Work section when the venue or scientific structure benefits from it;
- detailed artifact paths in a formal artifact-evaluation appendix;
- protocol identifiers needed to establish preregistration;
- machine-state vocabulary when the machine state itself is the scientific object under study;
- companion-paper citations.

The exception must serve the reader or scientific claim, not merely mirror the repository.

## Final invariant

Before release ask:

> If the repository disappeared and the reader had never heard of the programme, would this manuscript still communicate a complete, correctly bounded scientific argument?

If the answer is no, the manuscript is not yet a standalone paper.
