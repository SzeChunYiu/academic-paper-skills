# Formal-spine preservation for academic writing

> Shared contract for preserving the irreducible formal scientific object of a manuscript through drafting, restructuring, compression, target adaptation, and revision. This contract prevents a common AI-writing failure: retaining the prose-level ideas while deleting the equations, definitions, operators, invariants, or non-implications that make the contribution scientifically identifiable.

Last reviewed: 2026-08-30.

## Purpose

A manuscript can become shorter, smoother, and apparently clearer while becoming scientifically less specific.

This happens when a rewrite preserves statements such as “we introduce a state-based framework” or “we distinguish execution from scientific warrant” but removes the formal object that tells the reader exactly what the state is, what transition is studied, and what relation does or does not follow.

For papers whose contribution is partly formal, the main-text formalism is not decorative notation. It can be **orientation-critical, interpretation-critical, and contribution-defining content**.

The core rule is:

> **Compression may shorten the explanation of a formal contribution; it must not silently erase the minimum formal object required to identify that contribution.**

This contract complements `atomic-claim-verification.md`. Atomic verification asks whether formal statements are correct and warranted. Formal-spine preservation asks whether the defining formal statements remain visible, connected, and interpretable after rewriting.

## When this contract is active

Activate the formal-spine gate when one or more of the following is true:

- the manuscript proposes a new formal object, state representation, operator, transition system, metric, criterion, law, axiom candidate, theorem, bound, decision rule, or typed relation;
- an equation or definition is necessary to distinguish the proposed framework from a verbal taxonomy;
- a central claim depends on a formal non-implication, incompatibility, conservation rule, admissibility condition, or authority/validity ceiling;
- the paper is a theory/proof paper or a theory-heavy hybrid;
- a method/framework/perspective paper makes a scientific contribution through an explicit formalization even if it is not a theorem paper;
- the source material contains a compact formal core that is repeatedly referenced by later concepts, diagrams, laws, or empirical tests;
- removing the formal notation would make a competent reader ask, “What exactly is the scientific object being proposed?”

Do **not** activate the gate merely because equations could make prose look more technical. Never invent formalism that is absent from, unsupported by, or stronger than the author’s scientific framework.

## The formal spine

Before substantial rewriting or compression, freeze a **formal-spine inventory**.

For each candidate item record:

```text
formal_id
kind: primitive / definition / state / operator / transition / relation /
      criterion / invariant / non_implication / theorem / bound /
      candidate_law / composition / hierarchy / other
canonical_source
canonical_expression_or_definition
scientific_role
claim_ids_or_sections_that_depend_on_it
main_text_requirement: required / preferred / support_ok
minimum_explanation
assumptions_or_scope
status: established / proposed / candidate / conjectured / illustrative
relocation_allowed: yes / no / conditional
```

The inventory is manuscript-specific. It is not a demand for a fixed number of equations.

### Irreducible formal set

Mark an item `main_text_requirement: required` when deleting it would remove one of these reader capabilities:

1. identify the central scientific object;
2. identify the transformation, mapping, mechanism, or operation being studied;
3. distinguish admissible from inadmissible transitions or claims;
4. recover a central assumption, boundary, or non-implication;
5. understand how named subcomponents relate hierarchically;
6. distinguish proposed/candidate laws from already established laws;
7. understand what later figures, examples, falsifiers, experiments, or evaluation criteria are testing.

A main-text-required formal item may be rewritten or notationally simplified, but it cannot be silently removed or moved to support material during compression.

## Minimum formal core for framework papers

When a framework, perspective, synthesis, or methods paper makes a genuinely formal contribution, the minimum main-text core commonly contains some subset of four roles.

### 1. The scientific object

State the object being studied in an explicit form appropriate to the field, for example a tuple, graph, distribution, dynamical state, optimization problem, logical structure, or typed record.

Generic illustration only:

\[
Z_t=(z_1,z_2,\ldots,z_k).
\]

Do not replace the actual author-defined object with this generic form.

### 2. The scientific transition or operator

Show what can change and what a transition returns, for example:

\[
F_t:(Z_t,u_t,w_t)\mapsto(Z_{t+1},r_t).
\]

The scientific prose must say what makes the transition valid, interesting, testable, or bounded. The presence of an arrow alone is not an explanation.

### 3. The context or competence boundary

If the framework is explicitly context-relative, define the contextual tuple, domain, regime, criterion, or boundary that prevents universalizing a local result.

### 4. The decisive implication or non-implication

Preserve compact relations that state what the framework rejects or limits, for example:

\[
\text{successful execution}\not\Rightarrow\text{warranted scientific transition}.
\]

A central non-implication is often more informative than several paragraphs of rhetorical qualification. If the manuscript’s scientific identity depends on it, it is not expendable decoration.

These are **roles**, not mandatory syntax. A paper may need one equation, four equations, a formal definition without an equation, or a theorem/proof block instead.

## Hierarchy and composition must remain visible

When later formal objects extend an earlier state, do not present them as disconnected metaphors.

If, for example, a base state has optional or decision-relevant coordinates, the manuscript should make the composition explicit:

```text
base scientific state
+ generative/representational regime when relevant
+ locality/perspective frame when relevant
+ map/atlas/horizon object when relevant
-> complete decision-relevant state
```

A compression pass fails if it preserves the names of these concepts but removes their formal containment or dependency relation.

## Candidate laws are not established axioms

Framework papers often propose conservation rules, transport constraints, closure conditions, admissibility criteria, or other law-like statements.

Keep three layers distinct:

- **definition/primitive** — introduced by stipulation;
- **derived or proved statement** — established under stated assumptions;
- **candidate law/hypothesis** — proposed for empirical, theoretical, or cross-domain testing.

Do not upgrade a candidate law into a universal axiom merely because an axiomatic presentation is concise.

When many candidate laws exist, the main text need not display every one as a separate equation. Preserve the minimum formal core and summarize the larger set as explicitly testable candidate constraints, with full formalization in the appropriate framework/theory/supplementary record.

## Compression order

When a manuscript must lose words, compress in this order unless the target or science requires otherwise:

1. repeated prose that restates the same formal relation;
2. generic motivation or background the target reader already knows;
3. duplicated definitions after the canonical definition is fixed;
4. secondary examples that do not establish scope or a falsifier;
5. long derivations whose result can remain in main text and whose derivation can move to Methods/SI/appendix;
6. exhaustive candidate-law lists when a representative typed summary preserves the contribution;
7. implementation or repository detail that is not scientifically constitutive.

Only after these should the writer consider reducing formal content, and then only by **equivalence-preserving simplification**, not deletion of the irreducible formal set.

If a target word limit conflicts with the formal spine, first trim or relocate an equivalent amount of prose/derivation. Do not solve the word limit by converting the scientific object into vague prose.

## Equivalence-preserving simplification

A formal item may be shortened when all of these remain recoverable:

- object identity;
- type/domain/codomain where scientifically important;
- essential coordinates/variables;
- quantifier/condition/assumption scope;
- directionality of the relation;
- negation/non-implication;
- candidate-versus-established status;
- dependency on context or perspective where relevant.

Permissible examples include:

- introducing a compact tuple and defining several coordinates in one sentence;
- moving a long derivation to support material while retaining the theorem/result and assumptions;
- grouping candidate constraints in prose after the formal state/transition has been defined;
- replacing repeated expanded notation with a canonical symbol after the symbol is unambiguously defined.

Not permissible:

- deleting the state tuple but keeping only its nickname;
- deleting the transition operator while retaining prose about “transitions”;
- changing `not imply` into a softer stylistic contrast;
- omitting the context tuple and then writing as if competence or validity were universal;
- presenting a proposed law without its candidate/hypothesis status;
- moving every defining equation to SI in a paper whose novelty is the formal framework itself.

## Formal-spine delta audit

After any substantial rewrite, compression, journal transfer, abstracting pass, or reviewer-driven restructure, compare the new manuscript against the frozen formal-spine inventory.

For every required item answer:

```text
present in current manuscript? yes/no
scientific role still explicit? yes/no
scope/assumptions preserved? yes/no
status preserved (defined/proved/candidate/etc.)? yes/no
dependencies/hierarchy preserved? yes/no
main-text placement still adequate? yes/no
```

If any answer is `no`, the rewrite is not complete. Restore the item, repair the relation, or make an explicit scientifically justified decision to change the contribution itself.

A stylistic preference, target-word pressure, or a desire to “make the paper more accessible” is not by itself sufficient justification to remove a main-text-required formal item.

## Reader recovery test

For a paper with a formal contribution, a competent target reader should be able to answer from the main manuscript:

1. **What is the formal scientific object?**
2. **What operation/transition/relation is the paper about?**
3. **Under what context, assumptions, or criterion does it apply?**
4. **What does the formalism license, forbid, or explicitly fail to imply?**
5. **Which constraints are definitions, which are established results, and which are candidate hypotheses/laws?**
6. **How do later conceptual components attach to the base object?**

If the manuscript discusses these ideas but the reader cannot reconstruct the answers, the formal spine has been over-compressed.

## Perspective and review articles

A Perspective or synthesis is not exempt merely because it is not a primary theorem paper.

If the article proposes a possible discipline, framework, taxonomy with formal semantics, or testable theoretical programme, include enough formal content to show that the proposal has a scientific object and not only terminology.

At the same time, do not turn a Perspective into an unvalidated axiomatic system. A useful pattern is:

```text
compact formal object
-> compact transition/relation
-> one or two decisive boundary statements
-> candidate constraints/laws described as hypotheses to test
-> empirical/theoretical falsifiers and research programme
```

This preserves the mathematical spine without making unsupported universality claims.

## Interaction with article type and target journal

Exact target rules can affect equation count, section placement, display style, and word budget. They do not automatically determine whether a defining formal object is scientifically dispensable.

When target adaptation suggests removing formal content:

1. verify the exact article-type rule rather than inferring it from comparable prose style;
2. distinguish a house-style preference from a hard constraint;
3. test whether the formal item is contribution-defining;
4. try notational compression, prose trimming, or derivation relocation first;
5. if the target truly cannot accommodate the irreducible formal set, consider a different article type, supplementary architecture, or target rather than silently changing the scientific identity of the paper.

## Interaction with atomic verification

Every formal-spine item that makes a scientific assertion must still satisfy atomic verification.

Preservation does not mean automatic truth.

A central equation that is unsupported, internally inconsistent, contradicted, or stronger than its assumptions must be corrected, narrowed, marked as candidate/conjectural, or removed. The formal-spine gate protects **scientific identity and visibility**, not bad mathematics.

Conversely, a fully verified equation can still be mishandled by writing if it is hidden so deeply that the reader cannot recover the contribution. Correctness and salience are separate requirements.

## Anti-overformalization safeguards

Do not:

- manufacture equations to make a conceptual paper look rigorous;
- translate ordinary prose into symbols when the symbols add no precision;
- preserve every equation merely because it existed in an early draft;
- confuse notation density with scientific depth;
- retain a full derivation in main text when only the result/assumptions are contribution-defining;
- use formalism to conceal uncertainty or empirical underdetermination.

The goal is the **minimum sufficient formal core**, not maximum mathematics.

## Release gate

For any manuscript with an active formal spine, do not describe the rewrite as complete, final, or submission/publication ready until:

- the formal-spine inventory exists;
- every `main_text_requirement: required` item is present or explicitly retired because the scientific contribution changed;
- object/operator/context/boundary relations are interpretable by the target reader;
- notation and definitions are consistent across text, equations, figures, tables, and supplementary material;
- candidate/conjectural/established statuses are preserved;
- compression did not erase a central non-implication, assumption, qualifier, or hierarchy;
- the current formal items pass the relevant atomic definition/proof/claim checks.

The key failure to prevent is:

> **ideas retained; formal scientific object deleted.**

That is a scientific-content regression even when the prose reads well.
