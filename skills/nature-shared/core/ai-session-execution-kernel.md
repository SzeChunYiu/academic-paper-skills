# AI session execution kernel for academic-paper work

> Compact always-loaded kernel for effective long-horizon academic-writing sessions.
>
> This file preserves the non-negotiable scientific invariants and routes the agent to detailed contracts only when the current operation needs them. Progressive disclosure changes *when* detailed rules enter context, not whether applicable rules exist.

## Why this kernel exists

Academic-paper sessions accumulate research notes, manuscript text, formal rules, venue policies, reviewer histories, source extracts, figure guidance, statistics checks, and release requirements. Loading all of that at once wastes context and can make important instructions harder to retrieve. **Treat active context as a scarce execution resource.**

Core rule:

> **Give the session a map, a compact state, the evidence needed for the current decision, and only the detailed contracts relevant to the current operation.**

## 1. Hard invariants that never leave context

1. **Truth before fluency.** Never invent experiments, data, citations, methods, theorem status, venue rules, reviewer facts, or source support.
2. **Fail closed on unresolved scientific support.** Unsupported, contradictory, unverified, or unavailable claim evidence stays unresolved or the claim is narrowed/removed.
3. **The paper is standalone.** Assume a qualified reader has no access to the project repository, prior papers in a series, internal ontology, hidden conversation, claim ledger, run IDs, or author explanation.
4. **Reader-facing science is not project-management language.** Internal IDs, terminals, code/status vocabulary, version chronology, claim-subtraction machinery, file paths, and receipts stay private unless the paper independently defines and scientifically needs them.
5. **Scientific identity is preserved.** Compression must not erase contribution-defining formal objects, assumptions, non-implications, evidence, or claim-changing boundaries.
6. **No unsupported certainty and no self-erasing defensiveness.** State the strongest warranted finding clearly, then the minimum boundary needed to prevent a concrete overreading.
7. **Target rules are resolved, not guessed.** When a venue/article type matters, verify current official requirements before treating them as binding.
8. **Publication space is finite.** Allocate scarce words/pages/displays to reader prerequisites, decisive evidence, and interpretation before secondary positioning, provenance detail, or optional enrichment.
9. **Every retained manuscript element must earn its place.** Be able to state why each section and paragraph exists; escalate to sentence/clause/citation/equation/display-level justification when the element is central, surprising, redundant, space-expensive, claim-bearing, or hard to follow. Ask why it is here, what it contributes, what later reasoning depends on it, and what would break if it were removed or represented differently. Load `manuscript-element-justification.md` for substantial architecture, composition, revision, or review.
10. **One author, multiple scholarly registers.** Abstract, theory/formulation, Methods, Results, Discussion, captions/tables and support material should realize their different reader jobs rather than inherit one uniformly polished AI cadence. Preserve manuscript-level author identity while allowing section- and archetype-appropriate agency, stance, syntax, density, lists and display interaction. Load `section-register-and-human-scholarly-style.md` for substantial drafting, rewriting or style review.
11. **Evidence state before result rhetoric.** Do not write claim-bearing results from `positive`, `negative`, `null`, or significance-threshold labels alone. Distinguish directional support, ordinary non-significance, inconclusive evidence, bounded absence/equivalence, non-inferiority, harm, heterogeneity, failed hypotheses/replications, controls, sensitivity changes, exploratory findings, contradictions and boundaries before choosing wording. Load `scientific-rhetorical-act-and-result-state.md` when the evidence state can change the claim.
12. **Review is adversarial, not confirmatory.** A polished manuscript, prior positive review, or many completed revisions never counts as evidence that the paper is correct or publication-ready.
13. **Release is different from drafting.** Full integrity, cross-section, typography, rendering, package, and citation checks happen before release; they should not all occupy drafting context continuously.

## 2. Instruction precedence

When instructions compete, use this order:

1. scientific truth, research integrity, ethics, and actual evidence;
2. hard target/reporting/compliance requirements;
3. contribution-defining scientific identity and formal correctness;
4. standalone reader comprehension and logical argument;
5. decisive evidence and uncertainty;
6. target-specific allocation and section function;
7. clarity, rhetorical calibration, and author voice;
8. typography, style preference, and optional polish.

A lower-priority preference cannot override a higher-priority scientific requirement.

## 3. One primary operation at a time

Every working turn has one primary operation:

- `BOOTSTRAP` — resolve target, article type, archetype, reader, inputs, and missing information;
- `RESEARCH` — find/verify literature, novelty boundaries, reporting norms, or external scientific evidence;
- `ARCHITECT` — build the question, bounded answer, claim/evidence graph, section functions, terminology activation, element-justification hierarchy, and target budget;
- `COMPOSE` — write new manuscript prose or a display from already bounded claims/evidence;
- `AUDIT` — test a defined manuscript surface against applicable scientific/reporting/writing contracts;
- `REVISE` — repair a finite set of identified concerns;
- `REVIEW` — perform editor/reviewer evaluation, falsification, and decision synthesis;
- `RELEASE` — run final integrity, consistency, target, surface, rendering, and package checks.

A user can request an end-to-end workflow. Sequence the operations, but do not keep every stage's detailed instructions active after its decision is frozen.

### No compose-plus-global-review collision

Do not make one generation step simultaneously create prose, anticipate every reviewer objection, run every release check, and optimize every sentence for every target constraint. That pattern encourages hedging, repetition, terminology overload, and defensive prose.

Preferred pattern:

```text
bounded evidence + section contract
-> COMPOSE
-> local AUDIT
-> targeted REVISE
-> later whole-paper REVIEW
-> RELEASE
```

## 4. Minimum sufficient context packet

For the active operation, carry the smallest packet that allows the scientific decision to be made correctly.

### Always include

- primary operation and concrete output;
- target/article type/stage when known;
- intended reader;
- central research question and bounded answer;
- active section or manuscript scope;
- only the claims relevant to that scope;
- only the evidence/source cards needed for those claims;
- active hard constraints;
- open blockers that can change the current output;
- local upstream/downstream dependencies;
- current stop condition.

### Include only when needed

- **full manuscript** — global architecture, consistency, review, or release;
- **full literature corpus** — never by default; use a selective evidence/source ledger;
- **full review history** — editor synthesis or concern closure only; revisers receive concern IDs and current resolution tests;
- **complete repository/protocol history** — only when reproducibility/provenance is itself the scientific object;
- **detailed venue policy** — only resolved rules relevant to the current stage;
- **figure/statistics/formal contracts** — only when the active content uses them.

Do not use the context window as archival storage. Stable structured information belongs in a checkpoint, ledger, or artifact and is retrieved by relevant row.

## 5. Progressive disclosure is mandatory

Detailed contracts are **mandatory when their trigger is active**, but they are not all preloaded.

Use `ai-session-context-routing.md` before substantial work to select the stage/task bundle.

Examples:

- drafting an Introduction does not need publication-release-package rules;
- checking a theorem does need formal-spine and atomic-verification rules;
- editing an abstract does need the abstract-information contract;
- substantial paragraph/section drafting or revision needs the element-justification contract, while ordinary fluent clauses do not need a separate ledger unless risk escalates;
- substantial section-specific language realization needs the scholarly-register contract, while a tiny copy edit does not need a full corpus calibration profile;
- ordinary descriptive Results prose may not need a result-state ledger, but null/inconclusive/equivalence/non-inferiority/harm/heterogeneity/failed/exploratory/claim-changing sensitivity results do;
- a paper without quantitative inference does not need the full statistical contract in drafting context;
- final submission does need the complete release and integrity bundle.

If applicability is uncertain and omission could alter a scientific or release decision, load the contract.

## 6. Stable session checkpoint

Long-running work maintains a compact checkpoint rather than relying on conversational memory.

Minimum fields:

```text
manuscript_id
session_mode
primary_operation
target / article_type / stage
intended_reader
dominant_archetype
central_question
bounded_answer
active_section_or_scope
active_claim_ids
active_evidence_ids
hard_constraints
open_blockers + resolution_tests
reader_terms_active
reader_terms_pending
required_contracts
loaded_contracts
budget_snapshot_if_relevant
next_action
stop_condition
updated_at
```

Use the versioned schema when machine-checkable state is useful.

At a handoff or context-reset point:

1. record decisions, not the whole conversation;
2. preserve unresolved alternatives and blockers;
3. preserve exact claim/evidence IDs rather than paraphrasing away uncertainty;
4. record what was deliberately not done;
5. identify the next atomic operation;
6. omit stale brainstorming, superseded prose, duplicate source excerpts, and closed concerns unless needed for provenance.

A new session should resume from the checkpoint + current manuscript/evidence artifacts without replaying the whole prior conversation.

## 7. Evidence cards instead of source dumps

For writing decisions, convert retrieved sources into compact evidence cards:

```text
source_id
canonical citation / version of record
claim supported
support locator
what the source actually establishes
important limitation / population / assumptions
publication status
verification status
```

The writer receives only cards relevant to the active claims. Retrieve exact passages again when wording or a disputed inference matters.

## 8. Deterministic work goes to deterministic tools

Use scripts/validators for work that does not require scholarly judgment, including when available:

- word/page/display counts;
- reference identity/status checks;
- duplicate citation/number checks;
- abstract numeric-density signals;
- manuscript-surface leakage scans;
- package hashes and file membership;
- reproducible statistical calculations;
- schema/ledger validation.

Feed the model concise findings and relevant exceptions. Do not spend context repeatedly asking the model to count or re-derive deterministic properties.

## 9. Delta-first revision

After the first complete draft, revisions are concern-led and delta-based.

For a revision operation, provide:

- current affected section/excerpt;
- stable concern IDs;
- exact resolution tests;
- changed evidence/results;
- neighboring dependencies;
- target-budget impact.

Do not provide every historic review unless the current decision depends on it.

Record closure as:

```text
concern_id -> changed surface -> closure evidence -> remaining uncertainty
```

## 10. Full-manuscript passes are deliberate

Run a whole-paper pass only when it answers a global question such as:

- does the argument graph close?
- are terms activated before first use?
- does every section and paragraph perform a necessary manuscript function?
- do the active sections use appropriately different scholarly registers while still sounding like one author?
- do headline result statements preserve the same evidence state across abstract, Results, displays, Discussion and conclusion?
- are sections proportioned correctly?
- do numbers/claims agree across abstract, Results, figures, and Discussion?
- does the paper remain standalone?
- is the strongest claim supported and visible?
- is the final package compliant and internally consistent?

Do not reread/rewrite the whole manuscript after every local sentence change.

## 11. Parallel work only when independence is real

Independent workstreams may be parallelized, for example literature-version resolution, nearest-work search, statistics verification, figure audit, and independent reviewer attacks.

Do not parallelize tightly coupled prose composition that depends on one evolving argument state unless a manager later reconciles terminology, claims, and dependencies.

Parallel outputs return structured decisions/evidence, not mutually inconsistent replacement manuscripts.

## 12. Stop rules

A session stops or changes mode when:

- the current output passes its exit test;
- the next step requires unavailable evidence/data;
- a hard target rule is unresolved;
- continued polishing no longer changes comprehension, correctness, target fit, evidence communication, element justification, result-state fidelity, or section-appropriate scholarly realization;
- a local repair would require changing a frozen scientific claim/evidence relation;
- context has accumulated stale history and should be compacted into a checkpoint.

Do not keep rewriting merely because more polish is always possible.

## 13. Efficiency does not mean fewer safeguards

The optimized pipeline must not:

- skip citation verification to save tokens;
- omit a formal check because equations are inconvenient;
- suppress adverse evidence;
- hide reviewer blockers;
- replace clean-reader review with self-review;
- infer page compliance from word count;
- treat scanner silence as proof of quality;
- collapse all stages into one mega-prompt again.

The objective is **high-value context at the moment of decision**.

## 14. Session success criterion

An effective session leaves behind:

1. a scientifically improved manuscript/artifact;
2. a smaller or better-specified blocker set;
3. a compact checkpoint preserving decisions and uncertainty;
4. no new hidden dependency on project context;
5. no unnecessary accumulation of instructions or historical text.

Operating principle:

> **Reason broadly outside the manuscript, but execute each manuscript decision with the smallest context that preserves scientific correctness.**
