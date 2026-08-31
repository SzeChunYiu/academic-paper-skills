# Atomic claim verification

> Fail-closed scientific-content contract for full manuscripts, submission-ready
> sections, and decision-relevant revisions. Use after the evidence boundary is
> frozen and before publication-readiness or scientific-closure language.

## Purpose

A headline-claim checklist is not coverage-complete. A manuscript can state a
correct central theorem while an undefined symbol, hidden quantifier, unsupported
specialization, stale citation, numerical mismatch, or unverified availability
statement remains elsewhere.

This contract inventories every atomic scientific assertion and gives it an
explicit disposition. It does not promise infallibility. It prevents unchecked,
unresolved, or contradicted content from being silently released as verified.

Use it for:

- full-paper drafting, rewriting, review, or finalization;
- theory/proof papers and any section containing formal claims;
- public-posting, preprint, archival, or submission-readiness decisions;
- revisions that add, remove, narrow, or relocate scientific claims;
- a local section when its claims can change the paper's central conclusion.

For partial inputs, audit the supplied scope and label the rest `NOT_ASSESSABLE`.
Do not turn missing material into a fabricated blocker or a clean bill of health.

## Atomic inventory

Read the manuscript from title through references and split coordinated sentences
when they contain independently falsifiable propositions. Keep negation,
comparators, quantifiers, conditions, uncertainty, population/domain, and
exceptions attached to the proposition they constrain.

Inventory at least:

1. definitions, coined terms, abbreviations, symbols, notation, and domains;
2. empirical or numerical results, including values repeated in prose/displays;
3. formal assumptions, lemmas, theorems, corollaries, proof steps, and claimed
   consequences;
4. method/procedure statements and reproducibility-critical parameters;
5. interpretations, mechanisms, causal statements, hypotheses, and limitations;
6. literature, novelty, priority, and field-state claims;
7. figure/table/caption assertions and every body-text interpretation of them;
8. statistics, units, sample definitions, estimands, uncertainty, and comparisons;
9. every in-text citation and bibliography entry, including identity, metadata,
   relevance, and the proposition for which it is used;
10. availability, provenance, ethics, compliance, metadata, and submission claims;
11. cross-section restatements in title, abstract, Introduction, Discussion, and
    Conclusion.

Stylistic preferences do not need scientific evidence, but a style edit that
changes scope, certainty, causality, or identity creates a new atomic claim.

## Ledger schema

Maintain one row per atomic content item. Express claim-bearing items as the
smallest proposition that can be checked independently:

```text
atomic_id
location
exact_atomic_proposition
claim_class: definition / empirical_result / formal_claim / method / interpretation /
             literature_fact / figure_or_table / statistics / availability_or_compliance
importance: headline / major / supporting / local
qualifiers_and_scope
dependencies_and_hidden_premises
warrant_pointer
warrant_class: author_data / displayed_result / proof / source / method_record /
               definition / not_applicable
evidence_resolution_status
support_or_entailment_status
strongest_alternative_or_counterexample
boundary_or_uncertainty
cross_section_locations
independent_check
status
release_action
```

A pointer is not verification. Check whether the cited proof, data, display, or
source actually entails the proposition at its stated strength and scope.
`Author supplied` records provenance, not truth.

## Status vocabulary

Verification-complete release statuses:

- `VERIFIED` - independently checked against the relevant data, proof, source, or
  deterministic derivation;
- `BOUNDED_INFERENCE` - explicitly presented as an interpretation and no stronger
  than its evidence;
- `COHERENT_DEFINITION` - well-defined, consistently used, and not contradicted;
- `NOT_APPLICABLE` - no warrant is required for this item class, with the reason
  recorded and independently checked.

Non-closing and fail-closed statuses:

- `SUPPORTED_INTERNAL` - traceable to a clearly located manuscript result, but
  the underlying data, derivation, or record needed for independent verification
  is outside the supplied scope. It may describe a conventional review-level
  limitation, but it is not atomic verification and cannot support a claim that
  every item was verified;

- `UNRESOLVED` - a required definition, premise, warrant, or source check is
  missing;
- `CONTRADICTED` - the manuscript, supplied evidence, derivation, or verified
  source conflicts with the proposition;
- `BLOCKED` - verification requires unavailable author evidence, data, proof, or
  compliance information;
- `NOT_ASSESSABLE` - outside the supplied scope.

No `looks fine`, unchecked blank, or silent omission is allowed. An item in a
non-closing or fail-closed state prevents a verification-complete publication-
ready terminal state for the audited scope. A contradicted or unresolved item
cannot remain as an unqualified manuscript assertion. Preserve it
only as an explicitly marked draft question/placeholder outside final prose, or
revise, qualify, remove, or obtain the missing warrant. Never invent a bridge.

## Verification by claim class

### Definitions and terminology

- State the denotation, domain, and scientific role before claim-bearing use.
- For a proof-bearing rule, operator, grammar, feasible family, objective, or
  derivation system, define its admissible inputs, output or conclusion
  semantics, side conditions, composition/transition rule, and any support,
  feasibility, cost, or length measure used later. A name, symbol, terminal
  state, or type signature alone is not a semantic definition.
- Check that later specializations satisfy the original definition.
- Treat the abstract, highlights, legends, and table notes as standalone surfaces;
  a body definition does not satisfy their first-use requirement.
- Do not guess expansions for private labels. Replace them with reader-facing
  descriptions unless the label is scientifically necessary, stable, and locally
  defined.

### Formal and theory claims

For every formal statement:

1. normalize objects, domains, assumptions, quantifiers, and conclusion;
2. list every definition and earlier result it depends on;
3. check each proof step rather than accepting `it follows`;
4. derive immediate consequences of the definitions and compare them with every
   later claim;
5. test degenerate cases, boundary cases, small instances, and plausible
   counterexamples;
6. distinguish a theorem proved in the manuscript from an externally cited fact;
7. require both upper- and lower-bound locators for `sharp`, `exact`, `optimal`,
   `necessary`, or `intrinsic` claims;
8. require an explicit attainment/existence premise before starting a proof from
   an optimum;
9. check that a local one-step bound is valid for the claimed multi-step edit,
   including telescoping and feasibility assumptions.
10. define sequence operators such as `subword`, `subsequence`, `factor`, and
    `deletion` precisely. Never let a proof silently switch between contiguous
    factors and arbitrary not-necessarily-contiguous subsequences.
11. for a least/shortest derivable, provable, representable, or computable
    quantity, separate the construction from the non-derivability obligation. A
    terminal normal form is by itself only an existence or upper witness in a
    minimization claim. The lower bound must exclude all shorter derivations by
    an invariant, adversary/model argument, or exhaustive proof over the stated
    derivation system. Terminality supplies that lower bound only after soundness
    and completeness, the conclusion semantics, and the relevant measure's
    preservation have been established.

If a bounded executable oracle is useful, treat it as a counterexample/sanity
check, not as a replacement for an all-size proof.

## Epistemic-status transitions and historical negatives

An unresolved, indeterminate, `CANNOT_CHECK`, or equivalent record is a dated
finding about a stated evidence boundary. It is not an immutable scientific
outcome. Re-audit it when evidence availability, parsing, or derivability changes.

If already-frozen evidence now permits the stated check, perform the smallest
deterministic reconstruction needed to resolve it. This is defect correction,
not optional new science, and it does not authorize a broader experiment,
retuning, or claim expansion.

Do not silently erase the old status or leave it active. Create an explicit
correction or supersession record that names the old finding, its evidence
boundary, the newly usable evidence and method, the corrected result, and the
result's scope. Preserve the original finding and raw evidence as provenance,
then update every current-authority surface that still describes the check as
unavailable. Retain any adverse or null corrected result; resolution of
checkability is not conversion into a positive result.

### Empirical, numerical, and statistical claims

- Trace each value to a table, figure, analysis output, or supplied data.
- Verify the scientific/statistical unit, comparator, uncertainty, exclusions,
  and multiplicity policy.
- Reconcile every repeated number and every prose interpretation of a display.
- Do not convert association to causation, simulation to real-world validation,
  or non-significance to equivalence.

### Literature and reference claims

- Verify metadata and source identity.
- Check that the source supports the exact proposition, not merely the topic.
- Check priority/novelty against the search boundary and state that boundary.
- Represent contrary or limiting literature when it changes interpretation.

### Availability, metadata, and compliance claims

- Confirm that named data/code/materials and persistent identifiers exist and are
  accessible as stated.
- Treat `to be supplied`, `must be inserted`, `TBD`, or equivalent markers as
  release blockers, not completed availability.
- For rendered artifacts, inspect metadata, every page, and final-page spill or
  accessibility defects separately from source-text linting.

## Cross-claim reconciliation

After row-level checks, run these graph checks:

- definition -> theorem -> corollary -> specialization;
- method/design -> evidence -> inference;
- figure/table -> Results sentence -> abstract/title/Conclusion;
- citation -> literature proposition -> novelty boundary;
- limitation/assumption -> every downstream generalization;
- revision delta -> all dependent claims and response-letter statements.

Search explicitly for mutually incompatible rows and for claims that become
stronger when compressed into the title or abstract.

## Worked proof-obligation pattern

Suppose a manuscript defines `H = span(A) <= F_2^n` and uses a zero-sum-free
word over the unrestricted alphabet `A`, where a forbidden zero-sum `subword`
means a nonempty subsequence of selected positions, not necessarily a contiguous
factor. The manuscript must state this convention; the identity below is not a
claim about the different contiguous-factor invariant.

```text
H = span(A)
-> extract a basis B subset A
-> the word listing each element of B once is zero-sum-free
-> zsf(H; A) >= rank(H)
-> linear dependence gives zsf(H; A) <= rank(H)
-> zsf(H; A) = rank(H)
```

Therefore a later claim that this invariant can be strictly smaller than
`rank(H)` is `CONTRADICTED` under those definitions. A wording change cannot
close it. The claim must be removed/corrected, or the invariant must be changed
to a genuinely restricted admissible-word/language object and re-proved.

## Independent coverage pass

For full manuscripts and readiness decisions, use a second context or reviewer
to audit the immutable manuscript without receiving a pre-adjudicated concern
list. The independent pass must:

1. recreate the atomic inventory or check every row against the source;
2. identify missed propositions, split claims, definitions, and dependencies;
3. challenge every headline/formal claim and every fail-closed disposition;
4. report coverage gaps before seeing the synthesis.

Reviewer blindness still applies. Reconcile ledgers only during editor synthesis.

## Release rule

Do not use `simulated_publication_ready_for_target`, `submission ready`, or an
equivalent public-release label unless:

- every in-scope atomic item has an allowed release status;
- `SUPPORTED_INTERNAL + UNRESOLVED + CONTRADICTED + BLOCKED = 0` for in-scope
  manuscript assertions under a verification-complete readiness claim;
- `NOT_ASSESSABLE` items are outside the claimed readiness scope and disclosed;
- every headline/formal claim passed an independent check;
- every placeholder, undefined reader-facing term, and contradictory restatement
  is resolved;
- the final revision delta has been re-audited.

When the count is nonzero, return the appropriate blocked state and the cheapest
valid resolution test. Continue drafting work where useful, but do not confuse a
workable draft with verified scientific closure.
