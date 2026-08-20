# Writing workflow

Run this workflow for drafting or restructuring. The order is `argument -> analogue/voice calibration when useful -> rhetorical moves -> paragraph nuclei -> sentences -> journal adaptation`, not `template -> prose`.

## 1. Build the argument spine

Before drafting, identify:

- **question / tension** — what is not yet settled, explained, measured, compared, validated, synthesized, or enabled?
- **answer / contribution** — what does this paper actually establish or provide?
- **evidence chain** — which results, analyses, proofs, cases, comparisons, or sources make that answer credible?
- **boundary** — where does the answer stop holding?
- **meaning** — why does the bounded answer matter to the intended research community?

If there are multiple contributions, identify one dominant spine and attach secondary branches. Do not compress unrelated contributions into a misleading single novelty claim.

If an essential link is absent, expose the missing link rather than inventing it.

## 1b. Build the Terminology Ledger

On first contact with the material, extract recurring terms, abbreviations, notation, variables, datasets, models, populations, conditions, and proper names. Lock canonical forms and reuse them across every section. See `../../../nature-shared/core/terminology-ledger.md`.

## 2. Classify contribution and evidence type

Use `static/core/rhetorical-engine.md` to classify the dominant contribution: empirical finding, mechanism, method, resource/benchmark, theory/proof, validation/replication, negative/null result, synthesis/review, or practical/clinical/policy implication.

Also identify the evidence type and research paradigm. A randomized trial, qualitative interview study, theorem paper, materials experiment, benchmark paper, and historical argument require different rhetorical structures even when they target similarly selective journals.

## 2b. Run focused analogue-paper study for substantial rewrites

When the task is a substantial rewrite/restructure and the field, study design, contribution class, or target is known, load `../../../nature-shared/core/analogue-paper-calibration.md`.

Use a few close papers as **structural/evidence priors**. Prefer comparability over prestige. Study:

- how the research need is created;
- how the contribution is positioned;
- how evidence blocks are sequenced and why;
- what main-text evidence is visible for comparable claims;
- what the main figures are meant to establish;
- what data/uncertainty/controls/validation/generalization/failure boundaries are shown;
- what is moved to Methods/SI/Extended Data;
- how much background, signposting, citation synthesis, and local interpretation the audience receives.

Do not copy phrases, distinctive paragraph structures, figure compositions, palettes, normalization/statistical choices, or journal mechanics inferred from published PDFs.

If detailed figure/plot planning is required, route to `nature-figure` and its analogue-figure workflow; keep writing focused on **figure role and evidence dependency**.

Skip or bound this step for tiny edits or when no trustworthy comparator set exists.

## 2c. Build an author-voice profile when the rewrite should remain recognizably theirs

When representative author prose is available or the user asks to preserve style, load `../../../nature-shared/core/author-voice-profile.md`.

Record a compact profile:

- voice invariants: cadence, agency, technical directness, signposting level, stable terminology, epistemic rhythm;
- flexible traits: paragraph/sentence length, transitions, headings, context amount, local compression.

Do not preserve errors or ambiguity as `voice`.

Use the separation:

`author evidence = truth constraint`

`journal rules = compliance constraint`

`analogue papers = structural/evidence priors`

`author voice = expression prior`

After any large structural rewrite, run a re-voice pass so the improved section does not sound like generic academic English or a clone of the analogue set.

## 3. Select section moves, not a universal skeleton

Load the requested section fragment. When the material does not fit its default pattern, or cross-disciplinary calibration matters, load `references/section-move-atlas.md`.

For each section:

1. Write the reader question the section must answer.
2. Select the minimum rhetorical moves needed to answer it.
3. Order the moves so each creates a reason for the next.
4. Mark optional/recurrent moves instead of forcing every move once.
5. Check the final move hands the reader a useful question for the next section.

Use `references/cross-disciplinary-writing-evidence.md` when deciding whether a proposed rule is robust or merely local to one discipline or corpus.

## 3a. Map paragraphs as nucleus + satellites

Each paragraph needs one **nucleus**: the proposition or reader task that makes the paragraph necessary.

Supporting **satellites** may include evidence, explanation, comparison, example, qualification, counterargument, implication, methodological reminder, or a bridge.

Do **not** require one rhetorical function per paragraph. Split only when two independent nuclei compete for control or when the paragraph becomes difficult to parse.

For each planned paragraph record:

`nucleus -> supporting evidence/reasoning -> qualification if needed -> next-reader question`

This map is more informative than a label such as `context` or `result` alone.

## 3b. Allocate Results evidence before drafting

When the task includes Results, full-manuscript compression, or main-versus-SI placement, load `../../../nature-shared/core/main-text-discipline.md`.

Classify each result as core discovery, necessary support, qualification, robustness, heterogeneity, provenance detail, alternative inference, or edge case. Build the shortest sufficient main-text evidence chain, but do not hide conclusion-changing qualifications in Supplementary Information.

Use the analogue set only as a prior about local expectations. Final placement follows the function of the evidence in this paper plus exact journal requirements.

## 3c. Alignment gate when framing is genuinely ambiguous

Do not stop routine drafting merely because several stylistic choices are possible. Use an alignment gate only when a wrong assumption would materially change the scientific argument.

Surface, compactly:

- the proposed argument spine;
- dominant contribution/evidence type;
- section move map;
- primary reader/audience;
- high-leverage assumptions that are not author-provided.

If the user is available, ask only the few questions that materially change the claim or structure. If immediate drafting is preferred, proceed with explicit placeholders/assumptions rather than inventing evidence.

## 4. Draft from evidence and reasoning outward

Keep claims near the evidence or reasoning that warrants them. Avoid large claim stacks followed much later by support.

For Results, make the local question and evidentiary answer recoverable. A useful block is often:

`question -> setup if needed -> observation/estimate -> evidence -> bounded local inference -> bridge`

Not every paragraph needs every element, and some disciplines defer most interpretation to Discussion.

For theory/humanities/qualitative work, replace quantitative evidence logic with the corresponding proof, source, case, theme, interpretation, or analytic warrant.

## 5. Engineer sentence-to-sentence flow

For each sentence, identify:

- what information is already **given** to the reader;
- what **new** information is added;
- the relation to surrounding sentences: evidence, cause, consequence, contrast, concession, specification, example, sequence, or inference.

Keep central entities lexically stable enough to be tracked. Use pronouns only when reference is unambiguous.

Do not add transition words as decoration. If the logical relation is already obvious through information structure and lexical continuity, an explicit connective may be unnecessary.

For deeper repair, load `references/paragraph-flow.md`.

## 6. Match syntax to rhetorical function

Do not optimize for uniformly short sentences or uniformly dense academic syntax.

- use chronological syntax for procedures when sequence matters;
- use explicit clauses for new causal or conceptual relations;
- use compact noun phrases for established technical concepts when readers can unpack them;
- separate observation from interpretation when combining them would blur evidentiary strength;
- place the sentence's main new claim where readers can find the emphasis easily.

If a sentence is difficult, first diagnose the hidden relation; shortening alone may not fix it.

## 7. Calibrate epistemic stance to evidence

Distinguish observed, estimated, inferred, simulated, proved, hypothesized, associated, and causally identified claims.

`show` / `demonstrate` require strong direct warrant. `suggest` / `indicate` fit indirect or bounded evidence. `may` / `could` fit plausible but unverified interpretations.

Sweep for unsupported `first`, `unique`, `unprecedented`, `comprehensive`, `complete`, `always`, and `never`. Replace them with bounded, testable statements.

Do not hide an incremental relationship to prior work merely to make the contribution sound larger. Explain precisely what changes and why that change matters.

## 8. Run the reader-prediction, voice, and coherence audit

After each paragraph ask:

1. What should a competent skeptical reader now believe?
2. What question will that reader probably ask next?
3. Does the next paragraph answer or intentionally redirect that question?
4. Is any needed evidence, definition, comparison, or qualification missing?

Then reverse-outline the section using paragraph nuclei. If the nucleus sequence does not reconstruct the section argument, fix the structure before polishing sentences.

For a full manuscript, also check section handoffs: Introduction -> Methods/evidence plan -> Results -> Discussion -> bounded conclusion.

If an author-voice profile is active, also ask whether the revised text still sounds like the same author after structural repair: stable terminology, recognizable agency, directness, cadence, and signposting without preserving defects.

## 9. Apply journal and article-type adaptation last

Only after the scientific argument works, resolve the exact journal/content type/stage using the journal axis and shared journal resolver.

Journal adaptation may change audience assumptions, section labels, compression, title/abstract conventions, reference rendering, and submission mechanics. It must not change evidence, causal strength, uncertainty, novelty boundary, limitations, or the manuscript's coherent author identity beyond what the target actually requires.

When the user asks for a broader characterization of target-venue writing practice beyond a few close analogue papers, load `references/target-corpus-calibration.md` and build a temporary profile from a stratified corpus.

## 10. Return prose plus reasoning-facing notes

Return the requested draft together with only the notes that help the author revise it: important assumptions, missing evidence, unresolved boundaries, risky claims, and structural choices that materially affect interpretation. Do not bury the prose under generic writing advice.

When an analogue pass materially changed the draft, it can be useful to summarize only the decision-relevant transfer as `adopt / adapt / reject / unresolved` rather than listing every observed pattern.

## 11. Revise locally before rewriting globally

When the author redirects a draft:

- change only the affected claims/paragraphs unless the new information breaks the argument spine;
- preserve the Terminology Ledger and author-voice invariants;
- if a new sentence duplicates an existing function, prefer replacement/compression to accumulation;
- re-run stance and coherence checks on changed text;
- if the premise itself changes, rebuild the argument/move map before re-drafting;
- if the change invalidates a prior analogue-derived assumption, drop that assumption rather than forcing conformity.

Revision should strengthen the argument without introducing reviewer-driven prose accretion or target-corpus style cloning.
