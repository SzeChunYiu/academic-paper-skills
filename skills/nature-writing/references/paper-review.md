# Manuscript argument and writing audit

Use this reference for a full-paper self-review before submission or after a major rewrite. This is not a generic `make it more impressive` checklist. Audit whether the manuscript lets a skeptical domain reader reconstruct and trust the argument.

## Contents

- [Audit hierarchy](#audit-hierarchy)
- [1. Contribution validity](#1-contribution-validity)
- [2. Claim–warrant alignment](#2-claimwarrant-alignment)
- [3. Whole-paper argument continuity](#3-whole-paper-argument-continuity)
- [4. Introduction and positioning](#4-introduction-and-positioning)
- [5. Methods / evidentiary credibility](#5-methods--evidentiary-credibility)
- [6. Results / analysis logic](#6-results--analysis-logic)
- [7. Discussion and interpretation](#7-discussion-and-interpretation)
- [8. Paragraph and sentence logic](#8-paragraph-and-sentence-logic)
- [9. Literature and citation integrity](#9-literature-and-citation-integrity)
- [10. Reproducibility and reporting](#10-reproducibility-and-reporting)
- [11. Journal/article-type fit](#11-journalarticle-type-fit)
- [Discipline-specific evidence questions](#discipline-specific-evidence-questions)
- [Severity and repair decisions](#severity-and-repair-decisions)
- [Adversarial audit workflow](#adversarial-audit-workflow)

## Audit hierarchy

Review in this order:

`scientific/intellectual validity -> evidence/inference -> whole-paper logic -> section logic -> paragraph logic -> sentence style -> journal mechanics`

Do not spend time polishing sentence rhythm while the paper's answer, evidence, or inferential boundary is unclear.

A manuscript can be beautifully written and still be logically weak. Conversely, a technically sound paper can fail because readers cannot recover why the evidence answers the stated question.

## 1. Contribution validity

Write the central contribution in one bounded sentence, then classify it:

- empirical finding/discovery;
- mechanism/explanation;
- method/algorithm/instrument;
- dataset/resource/benchmark;
- theory/proof/model;
- replication/validation/robustness;
- negative/null result;
- synthesis/review/framework;
- practical/clinical/policy implication;
- interpretive/historical argument.

Ask:

1. Is the contribution actually demonstrated in this manuscript?
2. Is its relationship to prior work explicit and accurate?
3. Is an incremental contribution represented as an auditable increment rather than disguised as discontinuous novelty?
4. Is a replication, null result, resource, or synthesis being undervalued because the manuscript is forcing a `novel method` story?
5. Are secondary contributions clearly subordinate to or connected with the main spine?
6. Does the contribution matter for a defensible reason: new knowledge, stronger evidence, broader/narrower boundary, improved capability, better measurement, removed assumption, synthesis, validation, or practical consequence?

Do not use `surprising`, `non-obvious`, or prestige expectations as universal acceptance tests. Many important papers validate, delimit, reproduce, synthesize, or falsify rather than introduce a new module.

## 2. Claim–warrant alignment

Create a claim ledger for every headline claim in title, abstract, Introduction ending, Results/analysis, Discussion and Conclusion.

For each record:

`claim -> evidence/reasoning -> evidence type -> uncertainty -> boundary -> alternative interpretation -> section(s)`

Audit for:

- claims with no visible warrant;
- statistical association rewritten as causation;
- simulation rewritten as real-world demonstration;
- one population/dataset rewritten as universal capability;
- proof under assumptions rewritten without those assumptions;
- local qualitative interpretation rewritten as prevalence/generalization;
- absence of evidence rewritten as evidence of absence without adequate sensitivity;
- method intention rewritten as proven advantage before evaluation;
- claim strength increasing as the manuscript becomes shorter (especially title/abstract).

If the claim is too strong, weaken it or add the evidence needed. Do not repair an evidentiary problem with rhetorical confidence.

## 3. Whole-paper argument continuity

Use `article-architecture.md` and the rhetorical engine.

Can the paper be reconstructed as:

`question/tension -> response -> evidence chain -> interpretation -> boundary -> meaning`?

Check:

1. Is the question posed in the Introduction the one the Results/analysis actually answer?
2. Does the method/design generate evidence capable of answering that question?
3. Does every major evidence block have a reason to appear at that point?
4. Does analysis B follow because analysis A changed what is uncertain?
5. Are key qualifications introduced before the paper generalizes beyond them?
6. Does the Discussion interpret the evidence that was actually generated rather than a stronger imagined study?
7. Is the Conclusion the post-qualification durable answer?

### Section-handoff test

At each boundary write the reader's next question:

- after Introduction: what evidence/design would answer this?
- after Methods: what did that design show?
- after each major Result: what question does this create next?
- after Results: what does this mean relative to alternatives/prior knowledge?
- after Discussion: what remains defensible?

If the next section does not answer the expected question, the handoff may be broken.

## 4. Introduction and positioning

Audit whether the Introduction creates a **real research need**, not merely a generic gap sentence.

Ask:

1. Is enough context provided for the intended reader, but no more than needed to understand the question?
2. Is the research need correctly typed: unanswered question, contradiction, missing mechanism, weak evidence, measurement problem, trade-off, missing regime/population, replication, benchmark/resource need, theory-data mismatch, or new opportunity?
3. Is prior work synthesized fairly, including what it succeeds at?
4. Are `not studied`, `not demonstrated`, `not generalizable`, `not measured`, and `does not work` kept distinct?
5. Does the final study response genuinely address the need the Introduction created?
6. Are the contribution and evidence classes previewed at an appropriate level for the field/article type?

Reject-risk warning: a dramatic gap that the study does not actually close is worse than a modest, precise research need.

## 5. Methods / evidentiary credibility

Methods must establish why the evidence is trustworthy enough for the intended inference.

Ask:

- Are data/material/population/source provenance clear?
- Are sampling/selection/inclusion/exclusion choices visible?
- Are measurement/construct/label definitions recoverable?
- Are consequential design choices justified?
- Are controls, comparators or baselines appropriate?
- Are leakage, confounding, bias, missingness or alternative explanations handled where relevant?
- Are analysis/statistical/model assumptions visible?
- Is uncertainty/sensitivity/robustness treated appropriately?
- Can readers reproduce or independently evaluate the work at the field-appropriate level?
- Are ethics, registration, consent, code/data/material availability and reporting standards addressed when applicable?

Do not require ablations, randomization, blinding, preregistration or inter-rater agreement universally. Require the credibility checks appropriate to the study design and claim.

## 6. Results / analysis logic

Review evidence sequence rather than simply asking whether there are `enough experiments`.

For each block:

1. What local question is being answered?
2. What observation/estimate/proof/source evidence answers it?
3. Is the comparator/reference condition clear?
4. Is magnitude/uncertainty/sample meaning reported when needed?
5. What narrow inference follows?
6. What new uncertainty motivates the next block?

### Evidence completeness

Look for missing tests that would materially distinguish interpretations, not ritual extras.

Examples:

- ablation if a component-level causal contribution is claimed;
- external validation if generalization is claimed;
- sensitivity analysis if an inference depends on a modeling/selection choice;
- negative cases if a qualitative/theme claim would otherwise look one-sided;
- counterexample if a theorem/claim has an assumed boundary;
- adverse outcomes if clinical benefit is discussed;
- robustness/repeated runs when stochasticity matters;
- primary-source counterevidence in historical/interpretive work.

A large experiment count does not compensate for the one missing discriminating test.

## 7. Discussion and interpretation

For each major finding check the cycle:

`finding -> interpretation -> relation to prior knowledge/alternatives -> qualification -> implication`

Not every finding needs every move.

Ask:

- Are alternative explanations considered before mechanism/generalization claims?
- Does comparison with prior work explain *why* results agree/disagree rather than merely saying they do?
- Are important limitations attached near the claims they constrain?
- Does each limitation state its consequence for interpretation?
- Are practical/policy/clinical recommendations proportional to design strength?
- Does future work follow from a real unresolved dependency?
- Does the Discussion add understanding instead of replaying figures?

## 8. Paragraph and sentence logic

For every paragraph write its **nucleus** in one line and list satellites (evidence, explanation, comparison, qualification, implication, bridge).

Check:

- Does every satellite serve the nucleus?
- Are two independent nuclei competing?
- Does the paragraph ending create or complete a useful handoff?
- Can paragraph nuclei reconstruct the section argument?

At sentence level:

- Is given/new information progression recoverable?
- Are central entities named consistently?
- Are pronoun/demonstrative references unambiguous?
- Is the main claim buried inside a subordinate clause or noun stack?
- Does sentence complexity match the rhetorical function?
- Are connectives encoding real relations rather than decorating jumps?

Do not audit clarity by sentence length alone.

## 9. Literature and citation integrity

Use `related-work.md`.

Ask:

- Does each citation have a clear role?
- Are primary sources used for specific primary claims when appropriate?
- Are strongest relevant alternatives represented?
- Are contradictory/limiting sources included where they affect interpretation?
- Are reviews used as synthesis/background rather than misrepresented as primary evidence?
- Are citation clusters supporting the same proposition, or several propositions accidentally bundled together?
- Is the present contribution's relationship to predecessors easy to verify?

## 10. Reproducibility and reporting

Check the field-appropriate reporting contract.

Examples include:

- statistical/effect-size/uncertainty reporting;
- participant/sample definitions;
- biological vs technical replicates;
- image/source-data integrity;
- code/software versions and parameters;
- benchmark splits/leakage controls;
- trial registration/protocol deviations;
- qualitative analytic procedure/reflexivity;
- source/corpus provenance;
- theorem assumptions/notation;
- data/code/material accessibility.

Use recognized reporting guidelines where the study design requires them. Do not replace reporting obligations with house style.

## 11. Journal/article-type fit

Only after the scientific/rhetorical audit passes, resolve:

`exact journal -> article/content type -> stage -> component`

Check current instructions for:

- section/abstract structure;
- length/display/reference constraints;
- anonymity/review format;
- required declarations;
- supplementary/data/code expectations;
- citation rendering;
- figure/table mechanics.

For stylistic calibration, compare recent **matching article types**, not a random famous paper from the same publisher.

## Discipline-specific evidence questions

### Experimental natural science

- controls/replicates/uncertainty adequate?
- conditions/materials/instrumentation interpretable?
- mechanism separated from correlation?

### Engineering / computer science

- baselines fair and current?
- evaluation protocol reproducible?
- ablations only where component claims require them?
- runtime/complexity/data/compute trade-offs visible?
- failure/generalization conditions tested when claimed?

### Clinical / epidemiological

- design supports causal vs associational language?
- population/eligibility/outcomes/confounding/missing data visible?
- effect sizes and confidence/uncertainty reported?
- generalizability/adverse consequences bounded?

### Social science / psychology

- constructs and measures valid for claimed inference?
- theory alternatives represented?
- sampling/power/preregistration status addressed where relevant?

### Qualitative research

- sampling/context/analytic approach transparent?
- evidence supports themes/interpretations?
- negative cases/reflexivity/credibility criteria appropriate to method?
- transferability not rewritten as statistical generalization?

### Theory / mathematics

- assumptions explicit and used consistently?
- theorem/result actually follows?
- counterexamples/boundaries identified?
- informal interpretation does not outrun the formal result?

### Humanities / historical work

- source base/provenance adequate?
- counterevidence/alternative readings engaged?
- historiographic relationship accurate?
- inference from source to argument explicit?

### Review / synthesis

- evidence selection transparent enough for the review type?
- synthesis distinguishes consensus, heterogeneity and uncertainty?
- agenda claims arise from evidence rather than selective examples?

## Severity and repair decisions

Classify findings:

- **critical** — central claim unsupported, study design cannot warrant inference, missing/counterevidence overturns headline, major integrity/reporting issue;
- **major** — argument discontinuity, consequential method detail missing, important comparator/alternative omitted, contribution mispositioned, limitation changes interpretation;
- **moderate** — paragraph architecture, local evidence placement, unclear citation role, terminology or section handoff problem;
- **minor** — sentence economy, transition, wording, mechanics.

Repair critical/major issues before stylistic rewriting.

A `needs new evidence` finding is different from `needs clearer writing`. Do not blur them.

## Adversarial audit workflow

1. Write the argument spine and contribution type.
2. Build the headline claim ledger.
3. Reverse-outline sections using paragraph nuclei.
4. Trace each headline claim to evidence/method/reasoning.
5. Search for counterevidence, alternative explanations and hidden boundaries.
6. Audit study-design-specific credibility/reporting.
7. Repair whole-paper and section logic.
8. Repair paragraph/sentence flow.
9. Apply target-journal formatting/style last.
10. Re-run the audit only on changed dependencies plus a final claim-drift sweep.

The goal is not reviewer-proof marketing. It is a manuscript whose scientific argument remains coherent under skeptical reading.