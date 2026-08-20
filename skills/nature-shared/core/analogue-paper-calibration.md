# Analogue-paper calibration

> Shared contract for learning from a small set of genuinely comparable papers before rewriting a manuscript, restructuring evidence, or redesigning figures. Last reviewed: 2026-08-20.
>
> Analogue papers are **comparators and design evidence**, not prose or figure templates to copy.

## Contents

- [Purpose](#purpose)
- [When to run the analogue pass](#when-to-run-the-analogue-pass)
- [How to select useful analogues](#how-to-select-useful-analogues)
- [What to extract from each paper](#what-to-extract-from-each-paper)
- [Cross-paper synthesis](#cross-paper-synthesis)
- [Writing transfer](#writing-transfer)
- [Evidence and figure transfer](#evidence-and-figure-transfer)
- [Main-text versus supplementary transfer](#main-text-versus-supplementary-transfer)
- [Author-voice boundary](#author-voice-boundary)
- [What must not be copied](#what-must-not-be-copied)
- [Failure modes](#failure-modes)
- [Output contract](#output-contract)
- [Evidence basis](#evidence-basis)

## Purpose

When rewriting or planning a serious paper, do not rely only on generic academic-writing rules. Study a few **near-neighbor papers** to understand how this research community makes comparable claims reviewable.

The analogue pass asks:

- How do comparable papers frame the same class of scientific problem?
- Which evidence appears in the main paper, and in what order?
- Which figures carry the main decision-relevant claims?
- What data are shown directly versus summarized?
- Which plot forms make the important comparisons visible?
- Where do authors place robustness, mechanism, external validation, negative results, limitations, and supplementary detail?
- How much technical background does this audience appear to need?
- Which rhetorical/visual patterns recur, and which are author-specific?

The objective is **structural and evidentiary calibration**, not imitation.

## When to run the analogue pass

Run it when any of the following applies:

- rewriting an abstract, Introduction, Results, Discussion, or full manuscript for a known field/target;
- deciding which experiments/analyses deserve main-text space;
- deciding what Figure 1 should do;
- redesigning a figure set or choosing plot types;
- transferring a paper to a materially different venue;
- diagnosing why a manuscript is scientifically sound but feels unlike papers in its intended community;
- preparing an editor/reviewer preflight where comparable evidence architectures are informative.

For a normal rewrite, a **small close-reading set** is usually more useful than a large unstratified corpus. Start with roughly 3–6 very close analogues when available. Use the larger `target-corpus-calibration.md` workflow when the goal is to infer stable field/journal distributions across many papers.

The number is a working heuristic, not a publication rule. Comparability matters more than count.

## How to select useful analogues

Rank candidates by **research comparability**, not prestige or citation count.

Prefer, in order:

1. same research question or contribution class;
2. same study design / evidence type;
3. same article type;
4. same target journal/venue when possible;
5. same subfield and intended audience;
6. recent enough to reflect current practice;
7. comparable data scale / modality / evaluation setting.

Examples:

- a cohort study is a better analogue for another cohort study than a methods paper in the same medical journal;
- a benchmark/resource paper may be a better comparator for another benchmark than a highly cited algorithm paper;
- a mechanistic materials paper with synthesis + characterization + theory is more useful than an unrelated materials paper that merely shares the journal.

Include at least one legitimate counterexample when possible. If every sampled paper looks identical, check whether selection bias created the pattern.

## What to extract from each paper

Build one structured record per analogue.

### Paper-level argument

- research question / tension;
- contribution type;
- headline claim;
- evidence classes;
- evidence order;
- stated boundaries / limitations;
- intended audience/community;
- article structure.

### Writing architecture

For the sections relevant to the user's rewrite, record:

- opening move;
- research-need construction;
- prior-work synthesis strategy;
- contribution statement location;
- paragraph nuclei and common satellites;
- how one analysis/argument motivates the next;
- where interpretation occurs;
- where limitations/alternatives appear;
- citation integration style;
- degree of first-person agency;
- sentence density / technical compression;
- how much explicit signposting is used.

Do not save reusable sentences from the analogue papers.

### Evidence architecture

For every main claim, record:

`claim -> evidence shown -> comparator/control -> uncertainty -> alternative addressed -> boundary`

Then note which evidence is:

- decisive main evidence;
- mechanism/explanation;
- validation/generalization;
- robustness/sensitivity;
- qualification/failure mode;
- provenance/reproducibility;
- supplementary enrichment.

### Figure architecture

For every main figure, record:

- scientific question answered;
- role in the paper (`orientation`, `main effect`, `mechanism`, `validation`, `generalization`, `boundary`, `resource`, etc.);
- data type and sample unit;
- plot/image/table/schematic modality;
- panel order;
- comparator/reference condition;
- uncertainty/raw-data visibility;
- figure-to-text handoff;
- what detail was moved to Extended Data/SI.

The purpose is to learn **what the figure proves**, not its colors, dimensions, or decorative style.

## Cross-paper synthesis

After reading the analogue set, classify every observed pattern as one of:

- `scientific necessity` — required by the claim/design regardless of fashion;
- `field convention` — helps the intended community read the work;
- `target/article-type tendency` — useful local default;
- `author choice` — do not generalize;
- `possibly weak convention` — common but potentially misleading or inferior for the user's data.

Then produce three layers.

### A. Recurrent useful patterns

Patterns that solve the same communication/evidence problem across several analogues.

### B. Legitimate alternatives

Different successful ways comparable papers solve the same problem.

### C. Our design decision

Choose what best serves the user's actual evidence and author voice. Do **not** mechanically choose the modal pattern.

## Writing transfer

Use analogue papers to calibrate:

- section/move order;
- amount of context assumed;
- contribution placement;
- evidence-to-interpretation rhythm;
- level of methodological detail in prose;
- citation density and synthesis behavior;
- where limitations are introduced;
- how aggressively results are previewed;
- how much explicit signposting readers in the field receive.

Then rewrite using the user's **author-voice profile**. Analogue papers influence architecture and local expectations, not the user's sentence identity.

## Evidence and figure transfer

Use analogues to answer two different questions.

### What evidence should be visible?

Ask:

- Which evidence types repeatedly carry claims like ours?
- What would a skeptical reader expect to see before accepting this claim?
- What validation/generalization appears necessary for this contribution class?
- Which negative controls, failure cases, sensitivity analyses, or uncertainty displays are decision-relevant?

Do not add an experiment merely because a neighboring paper has one. Add it only if it closes a real claim dependency or target criterion.

### How should that evidence be shown?

Choose the representation from the user's data properties and comparison task.

Examples:

- small-sample continuous distributions -> show individual observations/distributions when scientifically appropriate rather than hiding them behind means alone;
- paired/repeated measurements -> show pairing/change when the paired effect is the estimand;
- time/ordered progression -> line/trajectory representation when order matters;
- relationship between two continuous variables -> scatter with appropriate uncertainty/model display;
- composition -> part-to-whole only when components form a meaningful total;
- many categories -> ranked/structured alternatives rather than unreadable legends;
- images -> representative examples plus quantitative support when the claim requires both;
- model comparison -> fair common axes/scales and uncertainty across relevant runs/tasks;
- calibration/diagnostic claims -> diagnostic plot rather than only aggregate accuracy.

Published frequency is never a reason to use a misleading encoding.

## Main-text versus supplementary transfer

Compare what analogue papers reserve for the main narrative versus SI/Extended Data, but decide placement by **function in this paper**.

Keep in the main text evidence that:

- establishes the central discovery/answer;
- is necessary to trust the central claim;
- materially changes interpretation or scope;
- demonstrates a mechanism/generalization explicitly claimed in the headline.

Route supporting robustness/provenance/detail to Methods/SI when it does not change the central interpretation, subject to target requirements.

Use `main-text-discipline.md` for the final placement decision.

## Author-voice boundary

Load `author-voice-profile.md` when the user supplies existing prose or wants the rewrite to remain recognizably theirs.

Priority:

1. scientific truth and evidence boundary;
2. clarity and reproducibility;
3. exact target requirements;
4. author voice;
5. analogue-paper tendencies.

Analogue papers must never erase a coherent author voice merely because another style is common.

## What must not be copied

Never copy from analogue papers:

- distinctive sentences or paragraph wording;
- figure artwork or visual identity;
- panel layouts whose originality is part of the presentation;
- color palettes or graphical motifs merely to resemble a specific paper;
- unverified processing/normalization choices;
- axis truncation, aggregation, exclusion, or statistical annotations without scientific justification;
- journal production dimensions inferred from a PDF.

Learn **functions, relations, evidence architecture, and visual grammar**, not expressive surface.

## Failure modes

### Cargo-cult writing

Symptom: the manuscript contains `However... Here we...` because nearby papers do.

Repair: identify the real rhetorical move and express it in the author's voice.

### Cargo-cult figures

Symptom: a volcano plot/heatmap/bar chart appears because analogues use one, despite not answering the user's main comparison.

Repair: state the claim/question first, then choose the representation.

### Survivorship bias

Symptom: every published pattern is treated as causally responsible for acceptance.

Repair: treat published papers as successful examples under many hidden factors, not controlled experiments on manuscript design.

### Prestige contamination

Symptom: famous papers receive more weight than closer methodological analogues.

Repair: rank by comparability.

### Style cloning

Symptom: rewritten prose loses the author's cadence and sounds like a synthetic average of target papers.

Repair: restore author-voice invariants and keep only structurally useful analogue patterns.

## Output contract

A completed analogue pass should produce a compact working brief:

```text
Analogue set
- selection rationale
- important coverage gaps

Writing observations
- recurrent moves
- legitimate alternatives
- target-local tendencies

Evidence observations
- decisive evidence patterns
- common validation/boundary patterns
- likely reviewer expectations

Figure observations
- figure roles and sequence
- common data/plot mappings
- what belongs in main vs SI

Author voice to preserve
- invariants
- flexible elements

Our manuscript plan
- adopt
- adapt
- reject
- unresolved
```

The final manuscript/figure should be independently defensible even if the analogue papers are removed from the working context.

## Evidence basis

Useful public guidance and research reviewed for this contract:

- IEEE Author Center, `Create Graphics for Your Article`, emphasizes accurate/clear graphics and redundant visual encodings so figures remain interpretable without color alone: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/
- PLOS Biology submission guidance recommends showing distributions/individual observations for continuous data, particularly small samples, instead of relying on bar/line summaries: https://journals.plos.org/plosbiology/s/submission-guidelines
- Weissgerber et al. (2015), *Beyond Bar and Line Graphs*, showed that many different distributions can produce the same summary bar/line display and argued for more complete visualization of continuous data: https://doi.org/10.1371/journal.pbio.1002128
- Rougier, Droettboom & Bourne (2014), *Ten Simple Rules for Better Figures*, emphasizes audience, message, appropriate visual encoding, and avoiding misleading graphics: https://doi.org/10.1371/journal.pcbi.1003833

These sources support a central rule: **study comparable papers for communicative and evidentiary solutions, but choose the final representation from the user's scientific question and data.**