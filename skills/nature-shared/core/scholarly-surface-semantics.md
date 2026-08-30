# Scholarly surface semantics and publication-form integrity

> Shared contract for preventing authoring-, chat-, code-, audit-, and build-layer semantics from leaking into manuscript-facing prose, notation, tables, figures, and final rendered artifacts. It also protects the type consistency and explicit definition of named formal objects. Last reviewed: 2026-08-30.

## Purpose

A manuscript can be scientifically interesting and still look or behave like an internal AI/editor/developer artifact. Typical symptoms include chat-style bold emphasis, code-font semantic labels, raw `snake_case` or `_`/`^` notation in prose, CI-like `PASS`/`FAIL` states, dashboard-like all-caps diagrams, missing table captions, and rendered overflow.

A separate but related failure occurs when polished notation hides a formal type mismatch: a derived difference, ratio, premium, or comparison is built from quantities defined over different mathematical objects without an explicit bridge.

The invariant is:

> **Manuscript semantics are not authoring, Markdown, code, CI, or build semantics.**

A final paper should expose scientific objects, operations, evidence states, and uncertainty in reader-facing scholarly form. Internal implementation and audit vocabulary may exist in provenance records, but it must not leak into the publication merely because the drafting system used it.

This contract complements:

- `manuscript-surface-qa.md` for mechanical last-mile checks;
- `formal-spine-preservation.md` for keeping contribution-defining formal objects visible;
- `atomic-claim-verification.md` for correctness and warrant;
- `natural-scholarly-prose.md` for sentence-level scholarly realization.

## 1. Emphasis is a rhetorical decision, not a markup reflex

### Default rule

Do not use inline boldface merely to make an argument feel clearer or more important.

In ordinary manuscript prose, prefer emphasis through:

- sentence position and information structure;
- explicit contrast;
- paragraph architecture;
- a displayed equation when genuinely needed;
- theorem/definition structure;
- a properly designed table or figure;
- precise wording.

Inline bold is normally appropriate only when the target or genre convention supports it, for example:

- section/subsection headings;
- table headers;
- explicitly formatted definition/theorem labels;
- a target-mandated structured abstract label;
- a small number of reader-facing labels in a diagram when the visual grammar requires them.

### Review signals

Flag for contextual review:

- isolated bold words such as **not**, **now**, **only**, **must**, or **exact** inside ordinary prose;
- whole research questions or conclusion sentences bolded for rhetorical force;
- repeated inline bold in an abstract or Introduction;
- bold used to compensate for weak paragraph hierarchy;
- bold that was inherited from chat/Markdown authoring rather than chosen for the target.

Do not mechanically remove all bold. Determine whether it performs a legitimate publication function.

## 2. Code and monospace typography must preserve semantic type

Backticks, `\texttt{...}`, `\verb`, code fences, and monospace fonts signal **literal code or machine-readable tokens**. They must not become the default typography for scientific concepts.

### Usually translate

Authoring/internal tokens such as:

- `ANY_OPTIMAL_ACTION`;
- `CANNOT_CHECK`;
- `CURRENT_STATE_OK`;
- `PRESENT_EQUIVALENCE_GATE`;
- `C_dyn^*` written literally in prose;
- enum, config, class, function, field, or status names;

should be translated into one of:

- ordinary roman scientific prose (`any-optimal-action semantics`);
- a formally defined mathematical symbol (`\sigma=\mathrm{any}`);
- a conventional operator/label in math mode (`\mathrm{RETAIN}`, `\mathrm{REOPEN}`);
- small caps or another target-supported typographic convention when the label itself is scientifically meaningful.

### Legitimate exceptions

Retain monospace only when literal syntax is itself the object, for example:

- a programming-language token under study;
- an API/CLI interface in a software/interface paper when exact syntax matters;
- a file-format field or command in a designated artifact/reproducibility appendix;
- target-required code snippets.

A label is not literal code merely because the drafting system represented it as an enum.

## 3. Mathematical material belongs in mathematical typography

A symbol is not publication-ready merely because a reader can infer what the source token means.

### Source-to-manuscript boundary

Flag raw source-like mathematical tokens in prose, such as:

- `C_dyn^*`;
- `A_x^*(h)`;
- `Omega_dyn`;
- `delta(h,x)` when intended as mathematical notation;
- bare LaTeX control sequences rendered as text;
- underscore/caret expressions that escaped math mode.

Use math mode for variables and operators. Use `\mathrm{...}`/`\text{...}` or target-equivalent notation for semantic action labels where appropriate.

### Do not confuse code style with mathematical semantics

`ANY_OPTIMAL_ACTION` and `A^*(h)` are different kinds of objects. The former is a semantic policy label; the latter is mathematical notation. Typography should make that distinction visible.

## 4. Named scientific objects require explicit definitions

If the title, abstract, or contribution statement names a new scientific object, criterion, adequacy notion, metric, audit, state, or principle, the manuscript must provide a recoverable definition at the appropriate level.

Examples of named-object obligations:

```text
name in title/abstract
-> explicit definition or operational criterion
-> domain/scope
-> success/failure condition
-> relation to theorems/measurements/audit procedure
```

A paper titled around `X adequacy`, `Y consistency`, `Z robustness`, or a named audit should not force the reader to reconstruct the definition from several later statements.

For formal objects, prefer a compact Definition/criterion when possible. For empirical constructs, give an operational definition tied to observables and decision rules.

A theorem that characterizes a property does not automatically substitute for defining the named property unless the equivalence is explicitly stated.

## 5. Derived quantities need type-compatible operands

Before defining a difference, ratio, premium, gap, distance, or normalized score, audit the mathematical type of every operand.

For a derived quantity

\[
D = U - V,
\]

record:

```text
U: mathematical object optimized/measured over, codomain, unit/scale, conditioning
V: mathematical object optimized/measured over, codomain, unit/scale, conditioning
bridge or nesting relation between admissible classes
reason subtraction/comparison is meaningful
```

### Fail-closed rule

Do not treat `D` as a scientifically interpretable premium/gap if `U` and `V` are minima over different object classes, different units, different conditionings, or different loss semantics unless an explicit theorem/definition maps them onto a common scale.

Typical repairs:

- redefine both minima over nested representation classes;
- introduce a proven equivalence between selector cost and representation cost;
- rename the quantity so it does not imply a difference of like objects;
- report the two quantities separately;
- narrow the claim to the specific witness where comparability has been proved.

The same rule applies to normalized metrics, cross-model scores, information quantities, utilities, risks, and state-size measures.

## 6. Internal audit states must be translated for publication

Internal workflows often use states such as:

`PASS / FAIL / BLOCKED / CANNOT_CHECK / REGISTER / GATE / SCORE`

These can be excellent audit vocabulary and poor manuscript vocabulary.

### Manuscript translation

Prefer reader-facing scientific states such as:

- `verified on the stated finite fixtures`;
- `not verified`;
- `inconclusive under the bounded search`;
- `could not be assessed with the available observation channel`;
- `pre-specified criterion`;
- `exclusion/reconstruction control`;
- `evaluation step`.

Retain an uppercase/internal state label only when it is an explicitly defined scientific category that the paper itself studies. If retained, define it once, explain its semantics, and use typography consistent with the target rather than inheriting CI/dashboard styling.

### Registration language

Do not use `registered` as a generic synonym for `chosen`, `fixed`, or `declared` if readers could reasonably infer public preregistration or an external registry.

Distinguish:

- `preregistered/registered` — actually registered with an identifiable protocol/record when that meaning is intended;
- `pre-specified` — fixed before the relevant outcome/evidence was examined;
- `declared` — defined as part of the formal setup;
- `held fixed` — controlled within the analysis.

## 7. Diagram and table language must be reader-facing

A scientific diagram is not an internal state-machine dashboard.

Review conceptual figures containing:

- many all-caps command labels;
- implementation-like gate names;
- long underscore-separated tokens;
- test-harness states;
- arrows that encode workflow order but not scientific dependency;
- excessive bold that makes every box equally salient.

Translate each node into the scientific question/action it represents. Preserve formal labels only when they are actual scientific states or operators.

### Tables

Every manuscript table must have the target-required equivalent of:

- an identifier/number when the target numbers tables;
- a title/caption;
- column headers with interpretable units/semantics;
- notes for non-obvious abbreviations or statistical conventions;
- an explicit continuation mechanism when a table spans pages and the target requires it.

Before release, reconcile:

`table environment/count -> caption count -> numbering sequence -> body callouts`.

A manuscript with an uncaptioned table followed by `Table 2` is a release defect, even if the data themselves are correct.

## 8. Rendered-artifact correctness is part of manuscript correctness

Source text can pass while the PDF fails.

For every final rendered page inspect:

- clipping beyond margins;
- overfull lines/boxes;
- overlapping text/equations;
- orphaned/stranded headings;
- broken table continuation;
- figure/caption separation;
- unreadably small text;
- accidental font-family changes;
- monospace/typewriter fonts applied to scientific prose or math labels;
- missing glyphs and substitution boxes;
- page-number/reference spill defects.

For LaTeX, any `Overfull \hbox`/`\vbox` in manuscript-facing material is a release review item; visually clipped content is a release error.

Do not infer that a PDF is clean because compilation succeeded.

## 9. Title, scope, and mathematical machinery must agree

Every scientifically loaded title modifier must earn its place.

Audit words such as:

- autoregressive;
- causal;
- optimal;
- universal;
- exact;
- robust;
- safe;
- general;
- prospective;
- online;
- long-horizon.

For each modifier ask:

1. Where does it enter the formal object, assumptions, method, data, or evaluation?
2. Would the main theorem/result remain unchanged if the modifier were removed?
3. Does the manuscript establish the modifier, merely motivate it, or only give an example in that setting?

If the modifier is only application framing, phrase the title accordingly rather than making it appear theorem-essential.

## 10. Contribution mass and article-type fit are separate from correctness

A manuscript can be correct and still underpowered for its intended article type or venue.

For theory/framework papers, distinguish:

- mathematical novelty of the formal result;
- novelty of the assessment object/criterion;
- operational usefulness of the audit/procedure;
- empirical evidence that the failure occurs in real systems;
- generality beyond a finite witness;
- relation to mature parent theory.

If the main theorem is deliberately elementary and no empirical study is provided, the paper must make clear what other contribution carries the article: a new assessment problem, synthesis, benchmark protocol, impossibility/certification boundary, or other substantial object. Otherwise consider deepening the theory, adding an empirical demonstration, changing article type, or retargeting.

This is an editor/readiness question, not permission to manufacture extra mathematics or experiments.

## 11. Novelty and search-frontier statements are time-bounded

Statements such as `we found no prior work using this complete sequence` are high-risk literature claims.

Require:

- the search boundary and date;
- query/source-family coverage sufficient for the claim;
- explicit wording that absence in the search is not proof of universal priority;
- refresh close to submission/public posting when the field is fast-moving;
- narrowing/removal if a close prior work is found.

Prefer `through our search ending <date>, we found no direct prior work...` to unbounded `this is the first...` unless priority has been independently established at the required scope.

## 12. Three-layer release audit

For any full manuscript or submission/public-posting candidate, run three distinct passes.

### Layer A — semantic/source scan

Use conservative text scanning for:

- chat/Markdown emphasis residue;
- inline code/monospace leakage;
- uppercase snake-case/internal state tokens;
- raw source-like math tokens outside math mode;
- repository/developer residue;
- unresolved placeholders.

### Layer B — scientific/formal audit

Independently check:

- named-object definition completeness;
- type/unit/domain compatibility of derived quantities;
- title-to-formal-object alignment;
- candidate/established status;
- claim/source verification and novelty boundary;
- contribution/article-type fit.

A linter cannot close this layer.

### Layer C — rendered-artifact audit

Inspect every final page and relevant compiler/render log for:

- overflow/clipping;
- font leakage;
- missing captions/numbers;
- layout failure;
- mismatched figure/table callouts;
- final-page/reference defects.

Release requires all three layers to be reconciled.

## Release gate

Do not describe a manuscript as final, submission-ready, publication-ready, or public-posting-ready while any of the following remains unresolved in the audited scope:

- unjustified chat-style emphasis or code-font scientific prose;
- raw authoring/code/math tokens on manuscript surfaces;
- an undefined title-level or contribution-defining named object;
- a derived quantity whose operands are not type-compatible or explicitly bridged;
- internal CI/audit vocabulary masquerading as scientific result language;
- ambiguous `registered` language that overstates procedural status;
- missing/broken table or figure caption/number/callout structure;
- visually clipped/overflowing rendered content;
- a loaded title modifier unsupported by the actual formal/empirical object;
- a stale/unbounded high-risk novelty statement;
- a known article-type/contribution-mass mismatch not acknowledged in readiness review.

The target is not typographic uniformity. The target is a manuscript whose typography, notation, vocabulary, formal definitions, and rendered structure all communicate the same scientific object.