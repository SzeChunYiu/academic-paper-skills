# Manuscript excellence release gate

> Mandatory orchestration layer for substantial manuscript drafting, revision, review, and publication-readiness decisions.
>
> This gate complements integrity, correctness, reporting, target-budget compliance, and surface QA. A paper can be true and reproducible yet still fail as scholarly communication.

## Release principle

Do not call a manuscript publication-ready merely because:

- its claims are verified;
- citations are correct;
- formatting is clean;
- reviewers find no technical blocker;
- every section exists;
- every limitation is disclosed;
- it fits the venue limit after emergency trimming;
- the abstract is under its word limit.

A release-ready paper must also form a **coherent, sufficiently developed, reader-activated scientific argument with a high-information abstract, section-specific craftsmanship, calibrated numerical/rhetorical presentation, and scientifically efficient use of the target's finite publication surface**.

## Mandatory contract loading

For every substantial research manuscript, this gate requires active use of:

- `manuscript-section-craftsmanship.md` for the reader-facing job of each applicable manuscript surface;
- `abstract-information-budget.md` for the title/abstract entry point and numerical-salience decisions;
- `manuscript-narrative-architecture.md` for whole-paper and cross-section dependency;
- `venue-constrained-manuscript-budget.md` when a target/length constraint is known.

The section-craftsmanship and abstract contracts are not optional style references. They are release dependencies whenever those surfaces exist.

When a section convention is unfamiliar, discipline-sensitive, target-sensitive, or disputed, inspect `section-specific-academic-writing-evidence-2026-08-31.md`, current official venue guidance, current reporting standards, and close peer-reviewed analogue papers before imposing a template.

## Mandatory stage integration

### Before drafting / major restructuring

Create or refresh:

1. **whole-paper argument graph** using `manuscript-narrative-architecture.md`;
2. **section-function and craftsmanship map** using `manuscript-section-craftsmanship.md`;
3. **reader-state activation map** for central terms/entities/experiments;
4. **headline result -> interpretation matrix** for eventual Discussion;
5. **abstract regime and information budget** using `abstract-information-budget.md` — exact target limit/structure, headline claims, candidate quantitative anchors, required reporting items, and claim-changing boundary;
6. **numeric presentation policy** for headline quantities using `numerical-reporting-precision.md`;
7. **epistemic-stance plan** for headline claims using `epistemic-rhetoric-and-qualification.md`;
8. **target manuscript budget ledger** using `venue-constrained-manuscript-budget.md` whenever a venue/article type or explicit word/page limit is known.

The budget ledger resolves title/abstract/main-text/page/display/reference/legend/Methods/support constraints as separate currencies when the target does so. It also records section/function soft allocations, actual use, and remaining revision reserve.

For a substantial manuscript, inspect several close peer-reviewed analogue papers when available. Extract function and proportion, not wording:

- how titles identify the scientific object without unsupported modifiers;
- how abstracts allocate context, method/formal identity, headline evidence, quantitative anchors, implications, and boundaries;
- how Introductions move from field state to exact question;
- when central terminology becomes active;
- how setup/theory sections discharge downstream definitions and assumptions;
- how Methods organize scientific procedure and credibility rather than code layout;
- how Results blocks depend on one another;
- what belongs in setup/Methods versus Results;
- how much scarce main-text/page area is spent on setup, decisive evidence, interpretation, and positioning;
- how numerical precision is rendered;
- how Discussion relates findings to alternatives and prior work;
- how limitations are tied to inferential consequence;
- how figures, tables, captions, equations, references, support and availability divide reader tasks;
- how many caveats are local versus consolidated.

Do not copy section names, word counts, move counts, numerical counts, or percentage allocations mechanically.

### Before writing each major section

Write a one-line section contract:

```text
reader enters knowing X
-> asks Q
-> section supplies Y
-> reader leaves able to infer/test Z
```

Then use the applicable section entry in `manuscript-section-craftsmanship.md`.

If `X` is not active yet, repair earlier exposition.

If `Y` contains a central model/dataset/hypothesis/comparator never introduced before, activate it before result-bearing use.

If a target budget is active, state the section's provisional allocation and overflow route before expansion. A section may exceed its soft range only for a scientific reason that justifies the opportunity cost.

A section heading does not count as performing the section's function.

### During abstract drafting and finalization

Treat the abstract as a **standalone entry point**, not a miniature Results table or concatenation of section summaries.

Resolve the exact target abstract regime first: word/character limit, structured versus unstructured form, reference policy, reporting standard, and intended readership.

Build the smallest manuscript-specific rhetorical spine needed to recover:

```text
problem / gap
-> what was done or established
-> headline result / theorem
-> minimum decisive quantitative or formal anchor(s), when useful
-> scientific meaning
-> claim-changing boundary, when necessary
```

Apply the numerical-salience classes from `abstract-information-budget.md`:

- **Q0** — target/reporting-required design or result information;
- **Q1** — headline scientific anchor;
- **Q2** — secondary support;
- **Q3** — audit/provenance/process diagnostic;
- **Q4** — formatter residue.

The default is to preserve required Q0, use the minimum sufficient Q1 set, include Q2 only for a genuinely independent headline claim, relocate Q3 unless it is itself the scientific result, and remove/round Q4.

There is **no universal maximum number of numbers** in an abstract. A randomized-trial abstract may legitimately require multiple group results, effect sizes, uncertainty and harms; a theory abstract may need no empirical number at all. Judge quantitative objects by scientific function and exact reporting obligations.

Treat an estimate plus comparator plus uncertainty as a semantic inferential bundle rather than mechanically counting digits. At the same time, do not reproduce several batteries, secondary diagnostics, provenance counts and formatter-level decimals merely because they are available.

Draft an early abstract skeleton if useful for testing whether the paper has a coherent claim, but finalize the abstract only after headline claims, evidence, terminology, numerical policy and target budget are stable. Recheck the title after the final abstract.

### During Results drafting

Every major result block must pass:

- **necessity** — why this analysis now?
- **setup** — what comparison is being made?
- **evidence** — what was observed/estimated?
- **uncertainty/discriminator** — how should the pattern be judged?
- **local answer** — what question is now answered?
- **handoff** — what remains that motivates the next block?
- **space efficiency** — does this block earn its counted words/page area, or can secondary detail move to support without hiding claim-changing evidence?

Do not narrate version chronology when scientific dependency is the real order.

Do not make prose a duplicate of a dense results table. State the scientific pattern in prose and let the display carry exact multi-value lookup when appropriate.

### During Discussion drafting

For every headline result, select the minimum necessary subset of:

```text
meaning
mechanism/explanation
strongest alternative
relation to closest prior work
boundary/generalizability
methodological/practical implication
next discriminator
```

A list of limitations does not satisfy the Discussion requirement.

A list of prior papers does not satisfy the relation-to-prior-work requirement.

Closest/nearest-work discussion is function-limited: enough to credit origins, identify the strongest relevant comparator, state the unresolved difference, and interpret the present result. Internal claim-subtraction or nearest-work inventories do not automatically deserve manuscript space.

### During numerical rendering

Keep full precision in artifacts but explicitly resolve manuscript precision for:

- primary estimates;
- proportions/accuracies/F1/recall/etc.;
- intervals;
- P values;
- exact finite counts/fractions;
- runtimes/resources when claim-bearing.

Reject fixed `%.6f`-style output as the default manuscript policy.

Apply the same rule to abstracts: a six-decimal value must be justified by scientific resolution, inferential/decision need, or target convention—not by the formatter that produced it.

### During epistemic-language revision

For each headline claim:

1. state the strongest positive bounded result directly;
2. attach only the qualification needed to prevent a concrete overreading;
3. consolidate repeated global limitations in Discussion;
4. move audit chronology/status language out of the scientific narrative unless it changes interpretation.

Disclosure and transparency remain mandatory; repetitive defensive narration does not.

### During revision under a target limit

Every substantive manuscript addition must be funded from one of:

- remaining reserve;
- replacement/compression of existing text;
- relocation of lower-priority detail to Methods/appendix/SI/artifact;
- scientifically justified expansion when the target permits it;
- explicit retarget/article-type reconsideration.

Do not let reviewer responses become append-only manuscript growth.

When a result changes, update every dependent surface including abstract, title if necessary, Results, displays, Discussion, conclusion and response letter. The abstract is not exempt from result-lineage consistency.

## Pre-review excellence QA

Before simulated peer review, require all of the following:

### E1 — macro logic

- whole-paper argument graph has no unexplained central jumps;
- every major section has a reader question and a handoff;
- Results are ordered by scientific dependency rather than repository/run chronology.

### E2 — functional section sufficiency

- every applicable manuscript surface performs its reader-facing function under `manuscript-section-craftsmanship.md`;
- setup/formulation sections discharge every prerequisite used later;
- Methods expose the design choices needed to understand/evaluate the evidence rather than merely implementation detail;
- no section is accepted merely because its heading exists;
- no short section is expanded by arbitrary quota; missing dependencies, not length, drive repair;
- no conventional section is included merely because a generic template has it.

### E3 — reader-state activation

- central terminology is defined/characterized before first claim-bearing use;
- no surprise model/dataset/hypothesis/comparator appears only in Results or a table;
- tables/figures are locally understandable and do not introduce central paper objects silently.

### E4 — discussion depth

- headline findings are interpreted;
- strongest relevant alternatives are addressed when material;
- relation to closest prior work is explained rather than merely cited;
- limitations are linked to what inference they change;
- implications are specific enough to follow from the evidence.

### E5 — rhetorical calibration

- positive bounded findings remain visible;
- caveats are not repeated without a distinct function;
- adverse/null results are interpreted scientifically;
- project-governance language does not dominate reader-facing prose.

### E6 — numerical precision

- manuscript digits reflect scientific resolution/uncertainty/decision use;
- exact counts/fractions are preserved where useful;
- thresholds are not obscured by rounding;
- same results use consistent rounding across surfaces.

### E7 — close-analogue plausibility

When comparable high-quality papers exist, verify that the manuscript's explanation depth, result sequencing, section functions, discussion depth, abstract information density, numerical presentation, and section/display proportions are not obviously anomalous without a scientific reason.

Analogue conformity is not itself a goal. Unexplained genre deviation is a review trigger.

### E8 — venue-constrained allocation

When a target/explicit limit is known:

- exact count basis and exclusions are resolved from current official sources;
- hard word/page/display/reference/legend limits are satisfied or explicitly unresolved;
- page-limited targets have been measured in the official rendered template rather than inferred from words;
- P1–P3 reader/evidence functions are not underdeveloped because positioning, robustness, provenance, or audit material consumed the budget;
- nearest-work/Related Work is selective rather than exhaustive;
- figures/tables/equations earn their space;
- title and abstract use their micro-budgets on the scientific message;
- important definitions, evidence, and claim-changing boundaries were not moved out of main text merely to fit;
- revision reserve is explicit while substantive revision remains expected.

No universal section percentage is required.

### E9 — abstract information and cross-section craftsmanship

When the article type has an abstract:

- exact abstract regime is resolved;
- a clean reader can recover the problem, what was done/established, central result, meaning and necessary boundary;
- the headline result is not buried under secondary batteries, audit/provenance counts, or implementation diagnostics;
- quantitative content is dominated by required Q0 and headline Q1 objects rather than Q2–Q4 material;
- no universal number quota was applied where reporting standards legitimately require dense quantitative reporting;
- raw formatter precision and unexplained private experiment/version IDs are absent;
- each retained number/quantitative bundle passes the number-to-meaning test;
- abstract propositions and numbers are bound to current body claims/evidence and do not exceed body scope;
- abstract and title remain accurate after revision.

Across the full manuscript:

- Introduction, setup, Methods, Results, Discussion, limitations/conclusion when present, displays, captions, formal surfaces, references, support and availability each perform the appropriate reader-facing function;
- cross-section repetition has distinct functions rather than being copy-pasted summary;
- no section transition depends on project chronology instead of scientific logic.

## Reviewer requirements

At least one reviewer/editor pass must assess the paper as a **reader, argument, finite publication object, and set of section-specific interfaces**, not merely as a verifier.

The pass must answer:

1. From the title and abstract alone, can I recover the scientific object/problem, what was done or established, the central result, its meaning and its main boundary?
2. Does the abstract contain only quantitative objects that earn their entry-point space, or is it reproducing multiple Results substories?
3. Can I state the paper's research question after the Introduction without repository knowledge?
4. Can I define every central paper-specific object before Results use it?
5. Can I explain why each major Results block follows the previous one?
6. Can I distinguish the strongest result from the audit/provenance history?
7. Does the Discussion tell me what the findings mean, how they relate to alternatives/prior work, and where they stop?
8. Are displayed numbers as precise as the science warrants, rather than as precise as the software produced?
9. Is the paper appropriately confident rather than defensive or promotional?
10. If the target is constrained, which section/display consumes the most scarce space, and does its scientific function justify that opportunity cost?
11. Does every applicable section perform a necessary scholarly function rather than merely conform to a template?

A technically capable reviewer being able to reconstruct missing logic by effort does **not** count as a pass.

## Clean-reader closure

The final clean-room reviewer should receive only:

- current manuscript;
- normal supplementary/publication material;
- ordinary public scholarly sources needed for verification.

They should not receive:

- internal project ontology;
- claim-subtraction ledger;
- version genealogy;
- author explanation of what a missing term was intended to mean;
- prior review discussions.

If the reviewer needs those to reconstruct the paper, readiness is blocked.

For a target-constrained paper, the clean reader/editor should also be able to identify the main scientific message without seeing that scarce space has been dominated by secondary positioning, provenance, or repeated qualifications.

### Clean-reader abstract check

Give the final abstract alone to a reviewer with no project context. They should be able to state:

```text
problem
what the paper did or established
headline result
the evidence/formal anchor that makes it credible
meaning
important boundary
```

They should not need to decode D0/D1/M1/P4-X-style identifiers, benchmark genealogy, internal terminals, or a dense numerical result ledger.

## Automated support

Use `audit_narrative_precision.py` as a conservative pre-review signal for:

- excessive decimal precision;
- fixed-width perfect/zero metrics;
- defensive qualification density;
- experiment/version-ID narrative density;
- suspiciously short setup/formulation sections.

Use `audit_abstract_information.py` for a conservative abstract-specific signal on:

- hard abstract word limits supplied from the exact target;
- high numerical density and multiple quantitative substories;
- raw long-decimal/formatter precision;
- private experiment/version identifiers;
- excessive inferential-detail stacks;
- defensive-boundary density;
- disallowed abstract citations when the target rule is supplied.

The abstract scanner has an explicit reporting-mandated mode because structured trial/regulatory abstracts can legitimately require multiple quantitative objects. It must never be interpreted as a universal number-count rule.

Use `verify_manuscript_budget.py` when a target-specific manuscript budget ledger exists. It can block hard-limit overflow or explicitly underdeveloped central sections and returns unresolved rather than guessing page compliance when rendered measurement is missing.

Scanner/verifier findings require contextual review. Soft budget ranges and numerical-density signals are manuscript-specific planning/review constraints, not universal section or number quotas.

## Publication-ready terminal extension

A manuscript cannot enter a publication-ready terminal unless:

- all E1–E9 applicable gates pass;
- every applicable section/surface passes its reader-facing function under `manuscript-section-craftsmanship.md`;
- the abstract passes its information-budget, clean-reader and abstract-to-paper consistency checks when present;
- no central object appears before its meaning is active;
- no headline evidence block lacks a recoverable dependency on the paper's question;
- Discussion is interpretively sufficient for the article type;
- numerical precision is scientifically justified;
- direct positive bounded findings remain identifiable;
- exact target word/page/display/reference/abstract constraints are satisfied when applicable;
- scarce publication surface is not materially misallocated away from reader prerequisites, decisive evidence, or interpretation;
- no unresolved narrative/reader-state/abstract/section-craft/budget review item could cause a qualified new reader to misread the scientific case.

## Boundaries

This gate must not:

- reward longer manuscripts by default;
- force IMRaD where inappropriate;
- force a dedicated Related Work, Discussion, Problem Formulation, Limitations, or Conclusion heading;
- impose universal section percentages or reserve percentages;
- impose a universal abstract sentence count, rhetorical-move count, or number count;
- remove quantitative detail required by a reporting guideline merely to make the abstract look cleaner;
- remove inconvenient evidence;
- weaken necessary methodological transparency;
- invent mechanisms or implications;
- force human-like stylistic noise;
- optimize for AI-detector scores;
- treat fitting under a hard limit as more important than scientific comprehensibility.

The objective is an **excellent scientific argument for a real reader under the actual target constraints**, not a performance of human authorship or maximal compression.
