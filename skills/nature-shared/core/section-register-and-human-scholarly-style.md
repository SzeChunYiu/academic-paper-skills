# Section register and human scholarly style

> Shared contract for realizing a scientifically correct manuscript in the **section-appropriate scholarly register** used by expert human authors. This is not an AI-detector evasion guide and not a template for imitating any journal or paper.

Last reviewed: 2026-09-02.

## Core invariant

A strong paper should sound like **one author thinking differently for different intellectual jobs**.

```text
same scientific voice
+ different section function
-> different legitimate local register
```

Do not flatten Abstract, Introduction, theory/formulation, Methods, Results, Discussion, captions, tables, and supplementary material into one uniformly polished cadence.

The governing rule is:

> **Choose the rhetorical function first; let sentence form, agency, stance, density, citations, numbers, equations, lists, and display references follow that function.**

Natural scholarly style is not random sentence-length variation, slang, deliberate roughness, prestige vocabulary, or copying phrases from top journals.

## 1. Evidence model: learn conditionally, not by imitation

Calibrate style from three evidence layers that answer different questions.

### A. Large genre/corpus evidence

Use move-analysis, phraseology, stance, syntax, citation, and cross-disciplinary corpora to learn which patterns are stable and which vary by field/section.

This layer can establish, for example, that:

- abstract move priorities differ among disciplines;
- Introduction move sequences and phraseology vary substantially across disciplines;
- Methods sections perform credibility/rigour functions, not only procedural description;
- Discussion writing is rhetorically denser and more recursive than simple result reporting;
- first-person use varies by discipline **and by section**;
- LLM academic prose may use narrower/repetitive stance, formulaic syntax, ornamental lexis, and synonym substitution without genuine rhetorical variation.

### B. Current editorial / venue evidence

Use official author instructions and editorials to resolve what the target actually expects: structured versus unstructured abstracts, named versus unnamed headings, main-text/display limits, Key Points/Highlights, tense/voice recommendations, caption conventions, or article-type structure.

Venue mechanics are not universal prose laws.

### C. Deep real-paper reading

Read a small stratified set of genuinely close, strong papers to see how expert authors *realize* the relevant function:

```text
reader state before
-> paragraph/section move
-> language choices
-> evidence/display interaction
-> reader state after
```

Record abstractions, never reusable sentences.

A frequent pattern in published papers is descriptive evidence about practice, not proof that the pattern caused publication or is optimal.

## 2. Storytelling means dependency, not drama

Scientific storytelling is:

```text
question/tension
-> reason for next intellectual operation
-> evidence/formal step
-> changed understanding
-> remaining uncertainty
-> next necessary operation
```

It is **not**:

- hiding the answer for suspense;
- exaggerated adjectives;
- promotional claims;
- a chronological lab diary;
- manufactured conflict;
- forcing every paragraph into a cinematic arc.

A paper can be restrained, formal, and highly technical while still having a strong story if its dependencies are clear.

Use `manuscript-narrative-architecture.md` for global argument order and `manuscript-element-justification.md` for why each retained element exists.

## 3. One voice, multiple registers

The manuscript should preserve stable author-level traits such as terminology, degree of directness, and characteristic agency, while section-level language changes because the reader task changes.

### Abstract register — compressed scientific case

Dominant mode:

```text
problem / context
-> exact question or intervention
-> approach/design at sufficient resolution
-> minimum decisive result
-> bounded meaning
```

Typical language properties:

- high information density but low digression;
- very little metadiscourse;
- few or no citations unless target permits/requires them;
- only numbers that identify design scale or materially anchor the headline result;
- strong noun/verb precision, minimal internal terminology;
- no table-of-contents roadmap;
- no secondary result battery merely because space remains.

Do not force one abstract form across genres. A JAMA-style trial may require labeled structured moves and many reporting-mandated numbers; a Nature-style Article usually uses one compact unstructured paragraph; a theory abstract may foreground theorem class, assumptions, and practical consequence.

Load `abstract-information-budget.md` and exact target rules.

### Introduction register — motivated argument

Dominant mode:

```text
relevant field state
-> unresolved tension / limitation / question
-> why that gap matters
-> present scientific response
```

Human-like realization usually comes from **selective argument**, not catalogue prose.

Useful tendencies:

- paragraphs often have different jobs rather than identical `background -> however -> we` templates;
- citations cluster around intellectual claims/origins and are synthesized rather than listed one paper per sentence;
- the present-paper statement is often more direct than earlier background prose;
- first person can legitimately mark the authors' objective, choice, or contribution when field/target permits it;
- a broad first sentence is justified only when it materially establishes the problem.

Avoid prestige filler, universal history lessons, repeated `however`, and a mechanical mini-review.

### Theory / problem formulation register — explicit conceptual exposition

Dominant mode:

```text
object/problem
-> notation/definitions
-> assumptions
-> relation/operator/criterion
-> proposition/theorem/algorithm
-> interpretation or consequence
```

Theory writing can legitimately be more explicit and signposted than a short empirical paper.

Useful tendencies:

- stable technical terms are repeated rather than replaced with synonyms;
- definitions keep term and defining property close;
- theorem statements and proof transitions are compact, but motivation/interpretation surrounds contribution-defining formal objects;
- section cross-references and roadmaps can be useful in long formal papers because reader navigation is a real problem;
- phrases such as `we first define`, `we now show`, or `the following theorem` are not automatically mechanical when they perform navigation or proof-state work;
- examples/counterexamples are used when they reduce abstraction cost or expose a boundary.

Avoid decorative equations, excessive `it is easy to see`, undefined symbols, and long notation inventories before the reader knows why the objects matter.

### Methods register — procedural credibility

Dominant mode:

```text
design / material / data
-> consequential procedure
-> controls / selection / measurements
-> analysis / uncertainty
-> reproducibility and deviations
```

Methods do not need to sound like Results.

Useful tendencies:

- procedure/object can be foregrounded, so passive voice is sometimes efficient;
- author agency is useful for deliberate design choices (`we prespecified`, `we selected`, `we excluded`) when responsibility matters;
- chronology is legitimate when order affects replication;
- justification appears next to choices that affect inference;
- exact values, versions, thresholds, and parameter definitions can be dense because recoverability matters;
- headings/lists/tables may be appropriate when they improve procedural lookup or are required by reporting standards.

Avoid repository narration, source-tree prose, celebratory interpretation, and arbitrary variation inserted merely to sound less procedural.

### Results register — evidence-led progression

Dominant mode:

```text
local question/rationale
-> setup/comparison
-> observation/estimate
-> uncertainty/discriminator
-> bounded local inference
-> next scientific need
```

Useful tendencies seen in strong empirical papers:

- concrete scientific subjects and finite verbs;
- active first-person narration is common in many fields when authors are describing analytical/experimental choices (`we tested`, `we observed`, `we next asked`), but is not compulsory;
- past tense often carries completed observations; present tense may state figure content or durable interpretation depending on field;
- figure/table calls attach to the observation they support, not to generic `results are shown` sentences;
- dense numbers are delegated to tables/figures when the prose-level pattern is more important;
- short local interpretation is allowed when it directly follows from the evidence, while broader implications wait for Discussion;
- negative/failure evidence is written as science, not `PASS/FAIL` status language.

Avoid the monotone sequence `We did X. We found Y. We then did Z.` when the reason for Z is missing. The repair is the scientific dependency, not a prettier connective.

### Discussion register — interpretive synthesis

Dominant mode is more recursive than Results:

```text
surviving finding
-> interpretation
-> relation to prior evidence/theory
-> alternative explanation
-> boundary/generalizability
-> implication
```

Not every paragraph needs every move.

Useful tendencies:

- present tense often increases because the section discusses what findings mean, what evidence suggests, and what remains true;
- prior work is integrated at the point where the current result makes comparison meaningful;
- stance varies locally: direct for established findings, conditional for mechanisms/implications, explicit for speculation;
- authorial evaluation and synthesis are more visible than in Methods;
- paragraph structures can recurse between result, comparison, explanation, and qualification rather than follow one fixed template;
- limitations are connected to the inference they alter.

Avoid a Results recap, a ceremonial limitations list, repetitive `this suggests`, or generic future-work endings.

### Conclusion register — closure, if needed

The Conclusion should normally be the most compressed interpretive surface after the abstract.

Use it only when it adds a useful closure function that Discussion has not already discharged.

Do not mechanically restate the abstract or enumerate every contribution.

### Caption / legend register — local decoding

Dominant mode is descriptive and referential, not argumentative.

Use compact noun phrases and finite clauses to identify panels, groups, units, uncertainty, sample/statistical units, tests, scales, transformations, and essential conditions.

A legend can be information-dense without sounding like narrative prose. Do not `humanize` it by adding interpretation or storytelling that belongs in Results/Discussion.

### Table register — exact lookup

Tables use terse labels, controlled parallelism, canonical terminology, units, denominators, and notes. Point-like fragments are often correct here.

Do not turn a table into prose, and do not turn prose into a giant table merely because the information can be tabulated.

### Supplementary / Extended Data register — scrutiny and recoverability

Support material can be denser, more enumerative, and more procedural than the first-pass narrative when its job is exhaustive robustness, derivation, parameter detail, diagnostics, or specialist replication.

Do not use the main-text language target to erase useful support detail.

## 4. Archetype overlays

Section function is necessary but not sufficient. Apply the paper archetype.

### Mechanism / experimental discovery

Common language trajectory:

```text
phenomenon
-> perturbation/dependency
-> competing explanation
-> orthogonal/rescue evidence
-> mechanism/boundary
```

Results can read like a sequence of increasingly discriminating questions. Discussion usually synthesizes mechanism and competing interpretations.

### Randomized / clinical intervention

The register is constrained by reporting standards.

Expect:

- structured abstract/Key Points where required;
- exact denominators, effect estimates, intervals and harms;
- concise Introduction focused on clinical uncertainty;
- Results organized around participant flow, primary outcome, key secondary/safety outcomes;
- Discussion opening with the primary finding rather than rhetorical buildup;
- cautious subgroup/mechanism language.

Do not `de-mechanize` mandated reporting structure for stylistic variety.

### Computational / ML empirical

Avoid the common AI-paper monotone:

```text
architecture -> benchmark table -> ablation -> more benchmarks
```

Language should expose the scientific/evaluation questions: generalization, calibration, mechanism/explanation, efficiency, data bias, failure regime, or robustness.

Model/dataset names should enter only when their role is active for the reader.

### Theory / proof / theory+numerics

Long papers can legitimately use explicit roadmaps, definitions, numbered propositions, proof-state transitions, and cross-references. This is not `AI-like` merely because it is systematic.

Narrative quality comes from motivation and dependency between formal objects, not from removing technical signposts.

### Resource / dataset / software-method paper

The prose answers trust/reuse questions: what the resource contains, how it was constructed, how quality was assessed, what is missing, and how it can be used.

File names, schemas, fields, or access details may legitimately appear when the resource itself is the contribution—an important exception to generic repository-leakage heuristics.

### Observational / population / policy analysis

Results often alternate operational definition, estimate/pattern, heterogeneity, and robustness. Discussion can carry more explicit societal/policy interpretation, but normative statements must remain distinguishable from empirical findings.

### Review / Perspective / conceptual synthesis

The argument can be more essay-like and conceptual. Headings, taxonomies, boxes, and schematic figures may carry synthesis rather than original empirical evidence.

`Story` here can mean progression through conceptual tensions or competing frameworks rather than experiments.

### Qualitative / interpretive

Do not force quantitative Results cadence. Theme development, cases, quotations, contrasts, reflexive interpretation, and methodological positioning may require longer interpretive paragraphs. Frequency language must not imply quantitative prevalence unless that is the analytic design.

## 5. Point form, lists, boxes and structured elements

Main narrative prose in original research is **usually paragraph-led**, but point form is not intrinsically unacademic.

Use point form when the *genre or reader task* benefits:

- structured abstracts or Key Points required by the target;
- Cell-style Highlights;
- formal assumptions, definitions, criteria, hypotheses, algorithm steps, or contributions when discrete parallel items are genuinely the object;
- Methods checklists/procedural steps;
- resource field definitions;
- review/Perspective boxes or taxonomies;
- tables and supplementary checklists.

Avoid point form when it merely replaces connected reasoning in Introduction, Results, or Discussion.

A useful test:

> If order, causality, contrast, or inference among the items matters, prose or a diagram may be superior to bullets.

Do not infer `human` from paragraph form or `AI` from bullets. JAMA Key Points and Cell Highlights are venue-defined scholarly genres.

## 6. Sentence rhythm: functional variation, not burstiness engineering

Do not optimize a numeric variance in sentence length.

Vary sentence architecture because rhetorical work varies:

- direct result -> shorter finite clause may be effective;
- condition/boundary -> subordinate clause may be necessary;
- comparison -> parallel structures help visual comparison;
- formal definition -> compact declarative form;
- synthesis -> longer sentence can integrate evidence and qualification;
- transition -> often one concise dependency sentence is enough.

Flag a monotone only when repeated form no longer corresponds to repeated function.

A run of parallel sentences can be excellent when the underlying evidence is genuinely parallel.

## 7. Agency: use `we`, passive, and impersonal subjects deliberately

There is no universal `avoid first person` rule.

Use `we` when authorial agency clarifies:

- objective/contribution;
- experimental/analytical choice;
- interpretive responsibility;
- proof or derivation navigation;
- deliberate inclusion/exclusion or prespecification.

Use process/object-centered syntax when:

- the procedure/result should be the topic;
- authorship is irrelevant;
- reporting convention favors it;
- repeated `we` would displace the scientific entity.

Avoid fake objectivity such as agentless `it was decided` when the authors made a consequential decision.

Use close-paper/discipline evidence to calibrate frequency; first-person use differs strongly across disciplines and sections.

## 8. Stance should move with epistemic status

Human academic prose does not hedge every sentence equally.

For each proposition classify the status:

```text
observed / estimated / associated / experimentally manipulated / causally identified /
proved under assumptions / simulated / interpreted / hypothesized / speculative
```

Then select stance.

Avoid:

- one repeated hedge (`may`, `might`, `could`) across all uncertainty;
- uniform booster language;
- defensive disclaimer chains;
- treating interpretation and observation with the same grammatical certainty.

Discussion usually carries a wider stance range than Methods or Results.

## 9. Citation integration is part of style

Citation density and position are section- and discipline-dependent.

Distinguish:

- **attribution** — who established an idea/method;
- **evidence synthesis** — what a literature body supports;
- **contrast** — where current results agree/disagree;
- **method provenance** — source of a procedure/resource;
- **priority/lineage** — intellectual origin.

Avoid `citation wallpaper`: several references appended to generic sentences whose relation to the claim is unclear.

Avoid one-paper-per-sentence catalogues when the rhetorical job is synthesis.

Discussion can legitimately use more narrative comparison with named studies than Results.

## 10. Numerical and formal density follow section purpose

Do not equalize number density across the paper.

- Abstract: minimum decisive quantitative anchors unless reporting standard requires more.
- Methods: high parameter/threshold/detail density may be necessary.
- Results: prose states pattern/estimate; figures/tables carry dense arrays.
- Discussion: usually fewer raw values; use numbers when magnitude is central to interpretation/comparison.
- Theory: equation density can be high when formal objects are the argument; prose must still state role and implication.
- Captions/tables: exact decoding/recovery can justify dense numeric content.

Use `numerical-reporting-precision.md` and `abstract-information-budget.md`.

## 11. Figures and tables change the prose register

A manuscript with strong displays should not duplicate them in prose.

Use:

```text
figure = inspect pattern / relationship / uncertainty / heterogeneity
 table = exact lookup / multi-dimensional values
 prose = question + interpretation + decisive observations
```

Figure-rich experimental papers often use shorter Results prose around each display because the visual carries evidence. Theory papers may allocate more space to formal exposition and fewer displays. Resource papers may rely more on tables/workflows. Qualitative papers may legitimately have no figures.

Do not set a global `figures per 1,000 words` or `tables per paper` target.

Use `figure-purpose-representation-optimization.md` and target constraints.

## 12. Paragraph register and choreography

Every paragraph should have a nucleus, but nuclei differ by section.

### Introduction paragraph

Common nuclei: field state, problem, unresolved contradiction, closest limitation, present response.

### Theory paragraph

Common nuclei: definition, motivation, lemma/theorem role, assumption, derivation step, interpretation.

### Methods paragraph

Common nuclei: design choice, procedure, measurement, control, analysis rule.

### Results paragraph

Common nuclei: local question, observation, effect/comparison, discriminator, boundary.

### Discussion paragraph

Common nuclei: interpretation, prior-work relationship, alternative, limitation, implication.

A manuscript sounds mechanical when every paragraph has the *same* nucleus type and satellite order despite changing intellectual work.

## 13. Section handoffs should change register naturally

A section transition is not just a heading change.

Examples:

- Introduction -> formulation: motivation gives way to explicit object definition.
- formulation -> Results: definitions stop expanding; evidence questions begin.
- Results -> Discussion: reporting gives way to interpretation and synthesis.
- main text -> Methods: argumentative pressure drops; recoverability/procedure rises.

The same author should remain recognizable while the rhetorical temperature changes.

## 14. Anti-monotone audit

After scientific logic is correct, review representative paragraphs across the manuscript.

Ask:

1. Do Abstract, Introduction, Methods, Results, and Discussion sound as if they were generated from one prose template?
2. Do paragraphs repeatedly open with the same grammatical subject (`We`, `This study`, `These results`) without functional reason?
3. Do all paragraphs close with generic significance or future-work sentences?
4. Are additive transitions (`Moreover`, `Furthermore`, `Additionally`, `In addition`) substituting for real dependencies?
5. Is stance uniform despite different epistemic statuses?
6. Is every sentence approximately the same syntactic size/shape without functional cause?
7. Are stable technical terms being replaced by synonyms for variation?
8. Are lists being used where reasoning relations matter?
9. Are formal/procedural sections being artificially conversationalized?
10. Are Discussion paragraphs merely Results sentences with more hedges?

Repair the *function-form mismatch*, not the superficial symptom.

## 15. Deep analogue style observation

For substantial rewriting at a known target, study roughly 3–6 close papers plus at least one counterexample when available.

For each relevant section record:

```text
reader job
opening move
paragraph nucleus patterns
argument tempo
agency / first-person behavior
stance range
sentence/clause tendencies
citation integration
number/formal density
list/box use
figure/table interaction
transition behavior
closing/handoff behavior
what is deliberately absent
```

Then classify observations:

- `scientific necessity`;
- `reporting/venue requirement`;
- `field/archetype tendency`;
- `legitimate alternative`;
- `author-specific choice`;
- `weak convention / do not transfer`.

Never store or reuse characteristic sentences.

Use the machine-readable scholarly-register observation schema when a long multi-session project benefits from a persistent calibration record.

## 16. Copyright and originality boundary

Do not copy, patchwrite, or imitate distinctive wording from analogue papers.

The transferable unit is:

```text
rhetorical function
+ information order
+ degree of explicitness
+ evidence/prose interaction
+ section-appropriate register
```

not phraseology.

A good final manuscript should remain independently writable if all analogue prose is removed from context.

## 17. Interaction with author voice

Use `author-voice-profile.md` above this section-register layer.

Conceptual stack:

```text
truth/evidence
-> section/archetype register
-> reader clarity
-> author voice
-> target mechanics
-> local polish
```

The goal is not to make the author sound like an average Nature/JAMA/Cell author. It is to make the author's reasoning sound **native to the intellectual job being performed**.

## 18. Clean-reader register test

For final review, give representative sections to a reader without internal project context and ask:

- Can they identify what kind of intellectual work this section is doing?
- Does the language help them perform the section's reader task?
- Does the section feel authored rather than assembled from generic academic sentences?
- Does the register change appropriately between reporting, formal exposition, procedure, and interpretation?
- Are any local conventions copied from another genre where they do not belong?

A section can be grammatically flawless and still fail this test.

## 19. Exit condition

Section-specific scholarly style is ready when:

1. every active section has a clear reader job and dominant rhetorical mode;
2. language form follows that job rather than one global prose template;
3. agency, stance, tense, citations, numbers, equations, lists, and display calls are locally justified;
4. paragraph structures vary because intellectual functions vary, not because random `humanization` was applied;
5. the author voice remains stable across legitimate register changes;
6. target-mandated structures such as structured abstracts/Key Points are preserved;
7. close-paper calibration has been abstracted into functions rather than copied wording;
8. no detector-oriented edits, artificial errors, or prestige-language inflation have been introduced.

Final principle:

> **Human scholarly writing is not one style. It is disciplined control over multiple rhetorical registers in service of one scientific argument.**
