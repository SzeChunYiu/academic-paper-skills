# Academic paper iteration pipeline

> Shared orchestration contract for taking an academic manuscript through repeated research, writing, figure/statistics work, independent review, editor synthesis, revision, and re-review until it reaches a defensible simulated publication-ready state or a real-world blocker. Last reviewed: 2026-08-25.

## Purpose

The repository contains specialized capabilities for literature research, citation verification, statistics, writing, polishing, figures, reviewer simulation, and response/revision. This contract turns them into a **closed-loop manuscript development process**.

The pipeline is designed to be realistic rather than flattering.

It must not stop because:

- one reviewer says `accept`;
- most reviewers are positive;
- the manuscript sounds polished;
- the user has made many revisions;
- all reviewer requests were answered in prose.

It stops successfully only when the **simulated editor** determines that the current manuscript satisfies the resolved target's publication criteria and the central scientific claims are adequately established, explained, displayed, reported, and technically clean.

This remains a simulation. It cannot guarantee acceptance by a real journal.

## Core lifecycle

```text
0 target + archetype resolution
1 source / evidence / manuscript intake
2 research calibration
3 argument + claim/evidence architecture
4 content + figure/statistics planning
5 writing / rewriting
6 technical + reporting + surface QA
7 editorial triage simulation
8 independent reviewer round
9 editor synthesis + decision letter
10 minimum-sufficient revision plan
11 execute research / analysis / figures / writing repairs
12 revision delta + response map
13 targeted re-review
14 editor closure check
   ↳ repeat 10–14 while a repairable blocker remains
15 simulated publication-ready OR explicit blocked/retarget state
```

The loop is **editor-controlled, concern-led, and stateful**.

## State model

Maintain these ledgers across the whole session.

### Manuscript state

- `manuscript_version` — monotonically increasing round/version ID;
- `target_journal_or_venue`;
- `article_type`;
- `submission_stage`;
- `dominant_archetype`;
- `secondary_archetypes`;
- `intended_reader`;
- `current_editor_posture`.

### Claim ledger

For each headline/decision-relevant claim:

```text
claim_id
claim_text
claim_type
importance: headline / major / supporting
scientific_unit_or_object
evidence_pointer
uncertainty_or_boundary
strongest_alternative
status: established / partially_established / unsupported / removed
```

### Evidence ledger

```text
evidence_id
evidence_type
source: manuscript / user_data / analysis / literature / proof / qualitative_source
supports_claim_ids
limitations
main_or_support_location
verification_status
```

### Figure ledger

```text
figure_id
reader_question
claim_ids
scientific/statistical_unit
estimand_or_visual_object
uncertainty_or_alternative_to_expose
role
main_or_support
status: planned / built / verified / remove
```

### Research/source ledger

```text
source_id
type: official_rule / reporting_guideline / close_analogue / broad_corpus / evidence_source
citation_or_url
date_checked
supports_which_rule_or_claim
confidence
```

### Concern ledger

Concern IDs are stable across rounds.

```text
concern_id
origin: editor / reviewer_1 / reviewer_2 / reviewer_3 / QA
round_opened
class
severity
blocking
claim_pointer
evidence_pointer
target_criterion
concern
resolution_test
owner_for_recheck
status
closure_route
closure_evidence
round_closed
```

Allowed status:

- `open`;
- `repair_in_progress`;
- `resolved`;
- `resolved_by_claim_removal`;
- `resolved_by_target_change`;
- `blocked_on_author_evidence`;
- `optional_not_pursued`.

### Revision delta

Every round records:

- claims added/removed/narrowed;
- evidence added/reanalysed;
- figures added/rebuilt/moved/removed;
- methods/reporting changes;
- explanation/logic changes;
- citations/research added;
- surface/format changes;
- unresolved issues.

Reviewers must receive the **current manuscript**, not an imagined cumulative draft.

## Stage 0 — resolve the real publication objective

Before writing or review:

1. identify target journal/venue if known;
2. identify article/content type;
3. identify stage;
4. resolve publication model using current official sources when it matters;
5. classify dominant paper archetype using `paper-archetype-atlas.md`;
6. identify applicable reporting guideline/checklist when relevant;
7. define the reader baseline.

Do not infer the target from a legacy `nature-*` skill name.

If no target is known, use a scientifically rigorous generic publication model and avoid invented house rules.

## Stage 0b — self-research fallback for an uncovered paper type

If the paper does not fit the existing archetype atlas, or the session is materially uncertain about how this class of paper should be written/evaluated, **research before imposing a template**.

Trigger self-research when any of these is true:

- no archetype fits without distortion;
- unfamiliar study design or evidence modality;
- unusual article type;
- target journal criteria are uncertain or changed;
- local static guidance conflicts with recent papers;
- reviewer expectation would otherwise be guessed;
- figure/plot convention is uncertain and consequential;
- reporting standard is unknown;
- a strong writing rule cannot be justified from current references.

Use `unknown-paper-research-protocol.md`.

The result is a **temporary manuscript-specific archetype profile**, not a permanent universal rule.

## Stage 1 — intake and evidence boundary

Freeze what is actually known.

Separate:

- author-provided scientific facts/results;
- available raw/processed data;
- manuscript claims;
- external literature evidence;
- implementation/project artifacts;
- missing evidence;
- user constraints on experiments/analysis.

Never convert a literature fact into a new experimental result of the manuscript.

Never fabricate an experiment because a reviewer requests one.

## Stage 2 — research calibration

Research has several legitimate jobs.

### Literature evidence

Use current high-quality sources to:

- frame prior work;
- verify novelty boundaries;
- resolve disputed interpretation;
- identify reporting/analysis standards;
- support Discussion/context claims.

### Writing/genre research

Use:

- broad stratified corpus for tendencies;
- 3–6 close analogues for deep local reasoning;
- exact journal/venue instructions for compliance.

Learn functions and dependencies, not sentences or visual identity.

### Reviewer-triggered research

When a reviewer raises an unfamiliar issue, research whether it reflects:

- a real scientific/reporting norm;
- a target-journal criterion;
- a field convention;
- a reviewer preference;
- a mistaken premise.

Do not automatically obey a reviewer request merely because it sounds authoritative.

## Stage 3 — manuscript architecture

Build:

`question/tension -> bounded answer -> evidence progression -> alternative/boundary -> meaning`

Then build decision proofs for headline claims.

Use `manuscript-content-selection.md` and `explanatory-sufficiency.md` so the paper is both selective and rich enough to understand.

## Content richness gate

`Rich` does not mean long.

For each central idea/result, ask whether the paper contains the necessary subset of:

- conceptual identity;
- motivation/research need;
- mechanism or inferential logic;
- decisive evidence;
- meaningful comparator/baseline;
- uncertainty;
- strongest alternative explanation;
- assumption/boundary;
- relation to prior work;
- scientific consequence;
- visual evidence when prose is inefficient.

A manuscript is **content-thin** when it repeatedly names ideas/results without developing the reasoning/evidence needed for the intended reader.

A manuscript is **bloated** when it repeats already-established ideas, includes artifact documentation, or adds background/analyses that do not change understanding or evaluation.

Repair thinness with specific missing scientific content; do not add generic filler.

## Stage 4 — figures, plots, diagrams and statistics

Use paper archetype + claim/evidence ledgers.

For each major claim:

```text
reader question
-> scientific/statistical unit
-> estimand / visual object
-> data structure
-> uncertainty / competing explanation
-> best representation
-> main/support/omit
```

Use `figure-evidence-planning.md` and `paper-archetype-atlas.md`.

For conceptual diagrams, workflows, mechanism schematics, state diagrams or flowcharts, route through the scientific diagram workflow rather than forcing a data-plot backend.

No plot or diagram exists merely because a peer paper used it.

## Stage 5 — academic writing

Writing order is:

1. scientific relation;
2. paragraph dependency;
3. sentence dependency;
4. explanation sufficiency;
5. information flow and identity chains;
6. stance/evidence calibration;
7. syntax/connectives;
8. author voice/natural scholarly tone;
9. target adaptation;
10. surface QA.

Use `sentence-logic-and-cohesion.md` for difficult sentence-to-sentence flow.

Do not optimize for AI detection.

## Stage 6 — pre-review QA

Before each review round, run:

- claim/evidence consistency;
- statistics/reporting checks;
- figure adequacy and legends;
- explanatory sufficiency;
- sentence/paragraph logic;
- main-versus-support allocation;
- citations/source verification as needed;
- artifact leakage scrub;
- punctuation/typography QA;
- exact target compliance when known.

Do not send an obviously mechanically broken draft to simulated reviewers unless the user specifically wants diagnosis of that draft.

## Stage 7 — editorial triage simulation

The editor first evaluates whether the manuscript is ready for external review under the resolved publication model.

Possible triage states:

- `send_to_review`;
- `repair_before_review`;
- `scientifically_sound_but_target_mismatch`;
- `central_case_not_established`;
- `blocked_by_integrity_or_compliance`.

Do not let reviewers repair a fatal target mismatch that should have been caught editorially.

## Stage 8 — initial independent review

Default reviewer lenses:

- **Reviewer 1 — validity/methods/data/inference**;
- **Reviewer 2 — contribution/prior work/target-specific significance or utility**;
- **Reviewer 3 — reproducibility/reporting/clarity/boundaries/readership**.

Add domain-specific expertise only when the paper requires it.

Initial reviewer packets are mutually blind and frozen before synthesis.

Each Major Concern needs:

- stable ID;
- blocking status;
- claim/evidence pointer;
- why it matters;
- plausible alternative interpretation;
- resolution test.

Do not impose a concern quota.

## Stage 9 — editor synthesis

The editor does **not** count votes.

Synthesize reviewer arguments against:

- publication criteria;
- claim/evidence state;
- reviewer expertise;
- whether concerns overlap or conflict;
- whether a request is necessary to establish the manuscript's case.

Classify each request:

- `publication_criteria_blocker`;
- `technical_blocker`;
- `major_repairable`;
- `claim_recalibration`;
- `clarity_explanation_reporting`;
- `surface_copyedit`;
- `optional_enrichment`.

The editor explicitly marks which items are **must address** and which are **non-essential**.

## Stage 10 — choose minimum-sufficient repair

For every must-address issue, choose the cheapest scientifically valid route that passes the resolution test.

Allowed routes:

- `research_literature`;
- `reanalyze_existing_data`;
- `add_existing_unreported_evidence`;
- `new_plot_or_figure`;
- `figure_redesign`;
- `statistics_or_reporting_correction`;
- `clarify_or_restructure`;
- `expand_explanation`;
- `correct_error`;
- `narrow_claim`;
- `remove_claim`;
- `change_target_or_article_type`;
- `request_real_new_experiment_or_data_from_author`.

Never fabricate the last route.

Do not perform an unnecessary experiment just to signal effort.

## Stage 11 — execute revision

The session should actively perform every repair that is possible from available evidence/tools:

- research and add/replace citations;
- inspect close analogues;
- reanalyse supplied data when permitted;
- calculate/check statistics;
- design/rebuild plots;
- draft/restructure text;
- improve explanation depth;
- fix sentence flow;
- move content between main/SI/Methods/availability;
- scrub artifact leakage/punctuation;
- narrow/remove unsupported claims.

When a repair needs real new wet-lab/clinical/field data or an unavailable dataset, mark it `blocked_on_author_evidence` and specify the resolution test.

## Stage 12 — freeze revision delta

Before re-review:

- update manuscript version;
- update claim/evidence/figure ledgers;
- record exact concern closures;
- verify the response accurately describes what changed;
- run consistency and surface QA again.

Do not claim a concern is resolved solely because the response letter says it is.

## Stage 13 — targeted re-review

Use **reviewer continuity** by default.

### Major revision

Re-invite the original reviewer responsible for a technical blocker unless:

- the reviewer lacks the needed expertise;
- the target's process strongly suggests editor-only closure;
- the concern was withdrawn/overruled by the editor;
- the manuscript changed into a materially different paper.

The re-review packet contains:

- current manuscript/version;
- editor decision conditions;
- the reviewer's prior concern IDs;
- author revision/response for those concerns;
- relevant revision delta;
- new/changed evidence.

Do not ask the reviewer to re-review unchanged unrelated material from scratch.

### Minor revision

The editor may close minor clarity/reporting/surface issues without re-inviting reviewers when the target process permits and no specialist technical judgment is needed.

## Moving-goalpost protection

Reviewers cannot create endless revision churn.

A **new blocking concern after round 1** must be labeled with one of these justifications:

- `new_evidence_created_new_issue`;
- `revision_introduced_regression`;
- `previously_unassessable_now_visible`;
- `expertise_gap_discovered`;
- `original_major_issue_was_incompletely_scoped`.

Otherwise the concern is normally treated as late optional enrichment unless the editor independently finds it essential to publication criteria or scientific validity.

This protects realism without suppressing genuine newly visible problems.

## Reviewer disagreement

When reviewers disagree:

1. identify the exact proposition/criterion in dispute;
2. weight arguments by evidence and relevant expertise;
3. research the disputed norm/fact if needed;
4. request a focused additional expert only when the disagreement cannot be resolved from existing evidence;
5. let the editor decide.

Do not average scores.

## Stage 14 — editor closure check

For each must-address concern, the editor asks:

- did the resolution test pass?
- did revision create a new claim/evidence inconsistency?
- is the central scientific case now established?
- are target criteria now satisfied?
- is remaining work only non-essential enrichment or ordinary production copy-editing?

## Successful terminal state

Use the label:

`simulated_publication_ready_for_target`

only when all are true:

- no integrity/compliance blocker;
- no unresolved publication-criteria blocker;
- no unresolved technical blocker for a headline claim;
- every headline claim is established or appropriately narrowed/removed;
- key uncertainty/boundaries are visible;
- figure/evidence architecture is sufficient;
- methods/reporting/statistics are adequate for the claim;
- central ideas are sufficiently explained for the intended reader;
- manuscript sentence/paragraph logic is coherent;
- citations/prior work are materially fair/verified where needed;
- main/support allocation is not hiding decision-changing evidence;
- final manuscript surfaces pass artifact-leakage and punctuation QA;
- remaining reviewer requests are editor-classified optional enrichment or production-level copyedit.

This state means **ready to submit/finalize under the simulation**, not guaranteed real-world acceptance.

## Other terminal states

### `blocked_on_author_evidence`

A must-address concern requires real new data/experiment/material unavailable to the session.

Return:

- exact experiment/data/decision needed;
- why it is blocking;
- minimum resolution test;
- whether claim narrowing/removal could avoid it.

### `scientifically_sound_but_target_mismatch`

The work may be valid but does not meet the target publication objective.

Prefer transfer/repositioning over cosmetic significance language.

### `current_claims_not_established`

Central claims remain unsupported after all available valid repairs.

Narrow/remove claims or return to research/data collection.

### `blocked_by_integrity_or_compliance`

Do not continue acceptance engineering around an integrity/ethical/reporting blocker.

## Revision-round expectations

Do not hard-code a required number of rounds.

Empirical open-review evidence shows many papers improve materially after revision and most eLife VORs in a 2,051-article analysis were finalized after one revision round, with a smaller group after two. This supports **focused convergence**, not arbitrary endless cycling.

Continue only while:

- a real must-address concern remains;
- a valid repair is available or author evidence is pending;
- the next round has a concrete resolution test.

Stop adding rounds when only optional enrichment remains.

## Research-grounded realism notes

Current public editorial guidance supports several pipeline choices:

- Nature/Nature Communications: editorial decisions are based on strength of reviewer/author arguments, not vote counting; revisions are normally re-refereed.
- PLOS editor guidance: distinguish comments that must be addressed to meet publication criteria from non-essential comments; major revisions can be re-reviewed while minor revisions may often be editor-closed.
- eLife: revised Reviewed Preprints can be reassessed by editors/reviewers, and 2026 analysis of 2,051 articles showed strength-of-evidence ratings often improved after revision.

Use the exact target's current process when available rather than forcing one journal's re-review practice everywhere.

## Anti-gaming rules

Never:

- strategically cite likely reviewers;
- choose friendly reviewers to manufacture agreement;
- hide contradictory/adverse evidence;
- inflate novelty/significance in prose;
- add cosmetic experiments;
- suppress a technical concern because two other reviewers are positive;
- treat reviewer satisfaction as more important than scientific validity;
- invent results, experiments, citations or editorial policy;
- optimize a numeric `acceptance probability` score.

## Minimal loop output

At the end of each round, return or maintain compactly:

```text
Round/version
Editor posture
Must-address concerns still open
Concerns closed this round
Claims changed
Evidence/analysis added
Figures changed
Research added
Writing/explanation changes
Surface QA state
Next action
Terminal state if reached
```

The process should feel like a rigorous editorial office plus author team, not a collection of disconnected prompts.