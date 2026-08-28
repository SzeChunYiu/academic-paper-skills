# `nature-figure` Skill

[中文说明](README.md)

`nature-figure` plans, designs, generates, and audits journal-aware scientific figures. It can work **before plotting** to decide which figures a paper actually needs, calibrate those roles to the paper's scientific archetype, determine what each panel must let the reader inspect, and choose plot families from the estimand/data/uncertainty rather than a prestige-journal template. Rendering then follows in Python or R, and manuscript-facing legends/captions receive a final artifact-leakage and punctuation QA pass.

## What To Use It For

- Decide whether a claim needs a figure at all, or whether prose/table is clearer.
- Resolve whether the paper is primarily mechanism/discovery, randomized intervention, observational, computational/ML, method/tool/software, resource/dataset, theory/proof, qualitative, review/synthesis, or hybrid before proposing a full figure sequence.
- Build a claim-driven figure plan: `claim -> reader question -> statistical unit -> estimand -> data structure -> uncertainty/alternative explanation -> plot -> main/support placement`.
- Materialize a scientific display decision contract linking each display to its reader task, estimand, statistical unit, allowed/prohibited inference, immutable data/analysis/render/source-data chain, caption, and accessibility state.
- Suggest plot families for distributions, paired effects, trajectories, associations, agreement, calibration, classification, survival, heterogeneity, sensitivity, benchmarks, ablations, imaging, high-dimensional data, null results, and more.
- Study a broad corpus for conditional visual tendencies and a few close analogue papers for **figure roles and evidence expectations** without copying layout, palette, normalization, or visual identity.
- Decide which evidence belongs in main figures versus Extended Data/SI using the shared manuscript-content-selection logic.
- Recognize legitimate archetype-specific variants: a trial may start with participant flow, a resource paper with coverage/workflow, a mechanism paper with the phenomenon, and a qualitative/theory paper may need few or no quantitative plots.
- Generate Python / R plotting scripts and editable publication figures from data, legends, or manuscript claims.
- Redraw existing figures into clearer multi-panel evidence chains.
- Plan Figure 1, mechanism diagrams, workflows, graphical abstracts, or supplementary figures.
- Audit panel labels, uncertainty, statistical units, accessibility, actual PDF glyph sizes, source data, image integrity, and export formats.
- Scrub final figure titles/legends/table notes/alt text for plot-script names, source/output filenames, paths, helper identifiers, CLI/developer residue, raw project links, punctuation/spacing/bracket errors, and target-specific typography issues.
- Adapt final packaging to exact target-journal/article-type/stage rules without changing the underlying evidence.
- When explicitly requested, use the separate OpenRouter GPT Image 2 route for draft concept schematics/graphical abstracts, subject to target-policy and human scientific review.

## Workflow

Planning comes before rendering:

```text
paper archetype
-> claim
-> reader question
-> figure necessity
-> scientific/statistical unit
-> estimand
-> data structure
-> alternative explanation / uncertainty
-> representation
-> scientific display decision contract
-> panel/evidence sequence
-> main vs support
-> broad-corpus / close-analogue calibration when useful
-> Python/R rendering
-> exact journal adaptation
-> visual + source-data QA
-> legend/caption manuscript-surface leakage + punctuation QA
```

Important rules:

- **Planning-only tasks do not require choosing Python or R.** Backend selection begins when plotting/rendering starts.
- There is no universal ideal number of figures or universal `Fig. 1 -> Fig. N` sequence.
- There is no universal best chart: maintained adapters return candidate families and obligations, and unmatched tasks require domain research.
- Adapter rules are linked to a 39-source evidence registry with read depth, supported decisions, contradictions, and transfer limits rather than an unattributed bibliography.
- Denominator, group, transformation, data snapshot, analysis receipt, render receipt, source data, and caption must not drift independently.
- A chart's popularity in a top journal or analogue set is never sufficient justification.
- Small-sample continuous data often need visible individual observations/distributions rather than mean bars alone.
- Paired data should expose pairing when pairing is the estimand.
- AUC does not replace calibration/threshold behavior when those are the scientific/clinical questions.
- A UMAP/t-SNE image alone should not carry a quantitative separation or mechanistic claim.
- A null result should be shown with an effect estimate and relevant uncertainty/equivalence logic, not inferred from `P > 0.05` alone.
- A failure/limitation can deserve a **main figure** when it changes the headline interpretation.
- A qualitative paper may legitimately need no main figure.
- A panel exists only when it closes a real evidentiary or orientation question.
- A legend describes the scientific display, **not the plotting pipeline or repository tree**.

## Typical Requests

- "Given these Results, first classify the paper type, then tell me what Figures 1–4 should be and what each panel should prove before you plot anything."
- "This is paired data. Recommend the plot that best shows the actual treatment effect and uncertainty."
- "Read 4 similar Nature Methods papers and tell me which validation/benchmark/generalization figures our method paper is missing."
- "Study a broader corpus first: what figure roles are typical for this paper archetype, and which of those actually fit our claims?"
- "Our model claims external generalization. Suggest the right site-level, calibration, and failure-boundary plots rather than one pooled metric."
- "Audit this figure legend and remove `plot_auc.py`, `results/site_metrics.csv`, helper names and broken punctuation; keep only the scientific description."
- "Make the planned figure set in Python and export editable SVG/PDF plus source-data mapping."
- "Draft a graphical abstract, but keep generated imagery separate from quantitative evidence."

## Example Preview

| Direction | Preview | Reusable Pattern |
|-----------|---------|------------------|
| Multi-panel manuscript figure | <a href="assets/gallery/fig1-material-mechanism-rich.png"><img src="assets/gallery/fig1-material-mechanism-rich.png" width="220" alt="Material design and physical validation"></a> | Study how heterogeneous evidence can be organized into one visual argument; do not treat the exact composition as a template. |
| Chart-type atlas | <a href="assets/chart-atlas/atlas-03-heatmaps.png"><img src="assets/chart-atlas/atlas-03-heatmaps.png" width="220" alt="Heatmap atlas"></a> | Candidate visual grammars; final choice must follow data structure and reader task. |
| Third-party figures4papers reference | <a href="assets/figures4papers/figure_VIGIL/figures/comparison_radar.png"><img src="assets/figures4papers/figure_VIGIL/figures/comparison_radar.png" width="220" alt="VIGIL comparison radar"></a> | Inspiration/reference only; read copyright notices and never inherit a chart merely because it appears publication-like. |

## What You Need To Provide

For planning:

- headline claims/questions;
- what data exist for each claim;
- statistical/experimental unit, pairing/repeated structure, groups/conditions, time/order, and important uncertainty when known;
- target field, study design, contribution archetype and journal/venue when known.

For rendering:

- raw data or analysis-ready table;
- selected plot/figure plan or permission to propose one;
- output format and target dimensions/stage;
- Python/R preference; if absent, the skill asks or reuses the saved local preference.

## Outputs

Depending on the task:

- paper-archetype-specific main/support figure-role plan;
- figure/plot suggestion ledger: `claim/question -> unit -> estimand -> plot -> uncertainty/comparator -> main/support`;
- Figure 1–N evidence-role plan and panel map;
- main-versus-Extended-Data/SI visual allocation;
- broad-corpus descriptive tendencies plus close-analogue `adopt / adapt / reject` notes;
- runnable Python or R plotting script;
- SVG/PDF/TIFF/PNG figure files, with editable vector output preferred;
- panel notes, source-data mapping, exclusion counts, and panel-by-panel QA;
- artifact-clean, punctuation-checked manuscript-facing legends/captions;
- for AI-schematic tasks, a concept draft plus elements requiring human scientific verification/redrawing.

## Built-In References

- `../nature-shared/core/paper-archetype-atlas.md`: archetype-specific evidence and figure-role priors.
- `../nature-shared/research/stratified-paper-reading-2025-2026.md`: recent cross-archetype direct-reading calibration.
- `../nature-shared/core/figure-evidence-planning.md`: claim-driven figure necessity and question-to-plot atlas.
- `../nature-shared/core/manuscript-content-selection.md`: main/support/Methods/availability/repository allocation.
- `../nature-shared/core/manuscript-surface-qa.md`: final legend/caption artifact-leakage and punctuation/typography gate.
- `references/analogue-figure-calibration.md`: learn visual evidence roles from similar papers without copying identity.
- `references/figure-legend-conventions.md`: target-aware title/panel/statistics/attribution rules; the Nat Commun CS/AI corpus is a local profile, not a fixed skeleton.
- [`docs/deep-paper-calibration_EN.md`](../../docs/deep-paper-calibration_EN.md): public guide to archetypes, broad corpora, close analogues and surface QA.
- [`docs/manuscript-content-and-figures_EN.md`](../../docs/manuscript-content-and-figures_EN.md): public guide to manuscript content and figure planning.
- `references/figure-contract.md`: core conclusion, evidence hierarchy, panel map, and review-risk checks.
- `references/qa-contract.md`: export QA, source-data constraints, and visual inspection.
- `references/journal-adaptation.md`: exact-target/stage packaging.
- `references/ai-graphical-abstract-workflow.md`: evidence/policy/provenance boundary for AI-assisted graphical abstracts.
- `references/template-catalog.md`, `references/chart-types.md`, and `references/demos.md`: candidate implementations/patterns, never automatic scientific choices.

## Boundaries

- The skill does not invent data, statistical tests, sample sizes, uncertainty, mechanisms, or experimental conditions.
- It does not choose plots merely because top papers use them or because a broad corpus reports them frequently.
- It does not silently drop observations/variables, hide adverse variation, or change axes/crops/normalization deceptively.
- It does not treat embeddings, bars, radar plots, or other visually familiar forms as evidence unless they answer the actual reader question.
- It does not force a figure into qualitative/theory work when prose/table/proof is clearer.
- It does not expose plot scripts, paths, filenames, helper identifiers or developer workflow in paper-facing legends merely because the rendering pipeline knows them.
- AI-generated images are never treated as quantitative data or experimental evidence.
- Automated validators do not replace final physical-size visual inspection or contextual copy-editing.
- Published figures are not submission contracts; exact current target rules are resolved separately.
- Third-party assets remain subject to their original terms and notices.

## Related Skills

- `nature-writing`: builds the paper archetype, claim/evidence/content plan and can request figure suggestions before prose is fixed.
- `nature-statistics`: audits estimands, uncertainty, statistical units, multiplicity, and inferential display choices.
- `nature-reviewer`: stress-tests whether figures close decision-relevant reviewer questions.
- `nature-paper2ppt`: reuses validated manuscript figures in presentations.

## Relationship With Other Skills

- If the user asks **what to plot**, `nature-figure` can answer at the planning layer without a backend choice.
- If the user asks **what belongs in the paper at all**, combine with `nature-writing` / shared manuscript-content selection.
- If the main uncertainty is statistical, let `nature-statistics` determine the correct estimand/inference first.
- If the final figure needs prose integration, `nature-writing` owns the Results/Discussion narration.
- `nature-figure` owns visual evidence planning/rendering/QA and paper-facing legend/caption hygiene; it does not replace manuscript argument design or statistical review.
