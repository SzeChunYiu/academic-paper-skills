# Figure purpose and representation optimization

> Shared contract for deciding why a scientific figure exists, what reader task it must support, why one representation is preferable to plausible alternatives, what information it preserves or hides, and whether it earns scarce manuscript space. Use after identifying a candidate evidence role and before rendering a claim-bearing figure or table.

## Core principle

A scientific display is not a decorative container for results and not the automatic output of an analysis package.

The design problem is:

```text
scientific claim / question
-> reader decision task
-> scientific object / estimand
-> statistical unit and dependence
-> evidence and uncertainty
-> plausible alternative explanation
-> candidate representations
-> information-loss and perceptual audit
-> counterfactual comparison
-> chosen representation
-> figure sequence / placement
-> final-size reader test
```

There is no universal best plot.

The best representation is conditional on the exact reader task, scientific object, evidence structure, uncertainty, audience, publication medium, and claim boundary.

For a candidate representation `R`, think conceptually about:

```text
L(R)
= scientific information loss
+ perceptual decoding burden
+ inferential distortion risk
+ hidden dependence / uncertainty
+ manuscript-space cost
+ accessibility cost
```

Choose a representation that minimizes relevant loss while preserving the scientific object. **Do not turn this conceptual expression into a fake numerical score.**

## 1. Every main figure needs a scientific purpose

Before choosing a chart family, state one primary reader question in ordinary language.

Examples:

- Does the effect exist and how large is it?
- Does the result persist across sites or tasks?
- Where does the method fail?
- Is the predicted probability calibrated?
- Does an intervention change the same unit over time?
- What mechanism best distinguishes the competing explanations?
- What does this resource cover and where are its gaps?
- What is the temporal or spatial structure?
- What formal regime or phase boundary does the theory predict?
- What conceptual relationships organize this synthesis?

A figure that cannot state a reader question is not ready for rendering.

### Reader-state transition test

For every main figure, complete:

```text
reader enters believing/knowing X
-> figure allows inspection of Y
-> reader can now conclude/test Z
-> remaining uncertainty is W
```

If removing the figure would not change any scientifically important reader state, move it to support or omit it.

## 2. Representation tournament is mandatory for claim-bearing displays

Unless the representation is genuinely mandated by the scientific object, reporting standard, or target venue, compare at least two plausible representations before final selection.

For each candidate record:

```text
candidate family
reader task supported
information preserved
information hidden or aggregated
perceptual decoding task
statistical/dependence structure visible?
uncertainty visible?
heterogeneity/failure visible?
exact-value recovery
transformations / tuning choices
known inference risks
space / attention cost
accessibility risks
reason to prefer or reject
```

Examples of meaningful tournaments:

- mean bar + error vs raw points + interval vs estimation plot;
- pooled benchmark bar vs paired task-level differences vs exact-value table;
- ROC vs precision-recall vs calibration vs threshold operating-point plot;
- spaghetti trajectories vs small multiples vs summary curve + raw data vs heatmap/lasagna representation;
- heatmap vs dot matrix vs clustered table;
- stacked composition vs dot/interval comparison vs compositional log-ratio display;
- image plate alone vs image + population-level quantification;
- UMAP/t-SNE orientation vs quantitative distance/classification evidence;
- workflow diagram vs causal DAG vs mechanism model.

Do not create alternatives merely to satisfy a quota. Alternatives must be plausible for the declared reader task.

## 3. Representation dominance

For the current task, representation `A` may dominate `B` when:

1. `A` preserves every claim-relevant quantity that `B` preserves;
2. `A` exposes additional information needed for the reader's decision;
3. `A` does not introduce materially worse perceptual or inferential distortion;
4. `A` does not create disproportionate space/accessibility cost.

When one candidate clearly dominates, prefer it.

When candidates trade exactness against pattern visibility, use a mixed display or split responsibilities:

```text
figure = pattern / relationship / uncertainty / heterogeneity
 table = exact values / denominators / multi-metric lookup
  text = interpretation + decisive observations
```

Do not duplicate the same evidence across all three surfaces without distinct reader functions.

## 4. Information-loss audit

Every visual transformation hides something. For each claim-bearing display, explicitly audit relevant losses introduced by:

- aggregation to a mean/median/rate;
- binning;
- smoothing or fitted curves;
- normalization/standardization;
- log or other axis transformation;
- clipping/truncation;
- dimension reduction/projection;
- clustering and row/column ordering;
- ranking;
- rescaling to percentages;
- stacking;
- faceting/small multiples;
- color quantization;
- sampling/downsampling;
- omission of groups/outcomes/timepoints;
- representative-image selection;
- pooling across sites/tasks/seeds/replicates.

For each loss ask:

> Could the hidden information change the claim, reveal an alternative explanation, expose a failure regime, or alter the reader's uncertainty?

If yes, the representation is insufficient unless a companion display or explicit support surface restores that information.

## 5. Scientific stress tests for a candidate plot

### Same-summary-different-data test

Could materially different underlying datasets produce essentially the same displayed summary?

If yes, and those differences matter to the claim, expose the underlying distribution/units or narrow the claim.

### Alternative-explanation visibility test

What pattern would the strongest plausible alternative explanation produce?

The preferred display should make that pattern inspectable when feasible.

A figure that shows only the author's favored summary while hiding the discriminator is weak evidence.

### Dependence visibility test

Does the display reveal or at least correctly encode pairing, repeated measures, nesting, clustering, technical versus independent replicates, censoring, site/task/seed structure, or other dependence that changes interpretation?

Displaying every raw point does not repair pseudoreplication.

### Uncertainty visibility test

Does the representation expose the uncertainty quantity that the claim actually uses?

Do not use undefined error bars or substitute variability across technical observations for uncertainty in the scientific unit.

### Transformation sensitivity test

Would a reasonable change in:

- bin width;
- smoothing bandwidth;
- axis range;
- row/column order;
- normalization;
- distance/linkage;
- threshold;
- color scale;
- projection seed/parameters

materially change the apparent conclusion?

If yes, either show sensitivity, justify the choice, or avoid making the visual appearance carry the claim.

### Denominator and unit test

Can the reader recover the scientific/statistical unit, denominator, units, missingness/exclusions, and meaning of every displayed quantity?

### Occlusion and density test

Does overplotting hide multiplicity, density, outliers, or subgroup structure?

If yes, use transparency, jitter, binning, density, hexbin, small multiples, summaries with raw companions, or another representation appropriate to the task.

### Exact-value recovery test

If the scientific/reporting task requires exact estimates, denominators, or confidence intervals, can the reader recover them from text/table/source data even when the figure prioritizes pattern perception?

## 6. Perceptual task matters

A plot is decoded through visual operations, not merely seen.

Before selecting visual channels, identify whether the reader primarily needs to judge:

- position on a common scale;
- length;
- direction/slope;
- angle;
- area;
- color/lightness;
- shape;
- adjacency/topology;
- temporal order;
- spatial location;
- relative frequency/density;
- distribution/quantiles;
- exact value.

Controlled graphical-perception research supports treating these decoding tasks differently. Do not universalize a single hierarchy beyond the task and evidence studied, but prefer encodings that make the required comparison direct rather than requiring mental arithmetic, legend hopping, or working-memory retention.

### Direct-comparison rule

When the scientific question is a difference, ratio, paired change, or effect, consider plotting the contrast directly rather than forcing readers to subtract separated summaries mentally.

### Global-pattern versus exact-comparison rule

Human vision can extract some broad/global patterns rapidly, while repeated exact subset comparisons are cognitively expensive. If the task is exact lookup across many values, a table may dominate a visually elaborate plot.

## 7. Plot family follows the scientific task

Plot names are not epistemic roles. A scatter plot, heatmap, line plot, or bar chart can serve many different scientific jobs.

Route by question first.

### Distribution / heterogeneity

Prefer representations that expose observations or distributional shape when that shape can change interpretation. A mean bar with error is rarely sufficient for small continuous datasets.

### Paired / repeated observations

Prefer connected points, paired-difference distributions, within-unit trajectories, or models/intervals that preserve the pairing.

### Longitudinal / ordered processes

Use line/trajectory representations only where order/continuity is scientifically meaningful. For dense trajectories, consider small multiples, model curves plus raw observations, or heatmap/lasagna-style views rather than unreadable spaghetti.

### Effect / comparison

Prefer direct effect estimates and uncertainty when the inferential question is the magnitude/precision of a difference. Use raw observations when distributional structure matters.

### Prediction / classification

Choose according to the claim:

- ROC: sensitivity/specificity trade-off across thresholds;
- precision-recall: positive retrieval under imbalance;
- calibration: probability accuracy;
- operating-point plot/table: deployment threshold behavior;
- decision curve/net benefit: utility when clinically appropriate;
- confusion matrix: error composition at a defined operating point.

One metric or curve cannot silently answer all of these questions.

### Survival / event time

Use censoring-aware survival/cumulative-incidence representations and numbers at risk when required. A generic line chart is not a substitute.

### Spatial

Use maps when spatial pattern is the object, but preserve denominators/rates and uncertainty. Raw-count choropleths do not establish risk when populations differ.

### Composition

Stacked relative displays are orientation views when part-to-whole structure matters. They do not by themselves establish absolute abundance changes, and internal segments are difficult to compare precisely.

### Heatmaps / clustering

Heatmaps are appropriate when matrix structure is itself the object. Declare transformations, scaling, color center, distance/linkage/order, and do not treat visual cluster adjacency as independent proof of natural clusters.

### Embeddings

UMAP/t-SNE and related projections are usually orientation/exploration views. They do not alone establish quantitative separation, natural clusters, mechanism, or generalization.

### Images / microscopy

Representative images should be paired with quantitative evidence when the claim is population-level. Show scale, selection/cropping, processing and annotations honestly; preserve source-image integrity.

### Diagrams

Declare semantic type before drawing:

- workflow = operations/sequence;
- architecture = components/interfaces;
- causal DAG = causal assumptions;
- mechanism model = bounded observed/inferred relations;
- state diagram = states/transitions;
- conceptual synthesis = relationships/taxonomy.

A workflow must not visually masquerade as causal evidence.

## 8. Multi-panel figures need one scientific thesis

A figure may contain different plot families when the panels answer linked subquestions of one larger scientific question.

Require:

```text
figure-level question
panel A subquestion
panel B subquestion
...
why these panels belong together
what conclusion requires their conjunction
```

Avoid **Frankenfigures** assembled because panels were available.

A strong multi-panel sequence often performs a logical progression such as:

```text
orientation -> phenomenon -> discriminator -> validation -> boundary
```

or

```text
population/design -> primary effect -> uncertainty -> clinically relevant consequence
```

but these are role patterns, not templates.

## 9. Figure sequence is part of the paper's argument

Plan main figures as a sequence of scientific decisions rather than an inventory of analyses.

For each main figure record:

```text
figure_id
question answered
claim(s) enabled
why it follows the previous figure
what uncertainty it closes
what uncertainty remains
why main text rather than support
```

A figure should not appear simply because the experiment was run next in chronological order.

### Main-text priority rises when

- the figure is necessary to judge a headline claim;
- it exposes a decisive alternative or control;
- it reveals a claim-changing failure boundary;
- it establishes generalization claimed in title/abstract;
- it provides orientation without which later evidence is difficult to interpret.

### Support priority rises when

- it repeats the same conclusion under additional seeds/specifications;
- it is a non-central diagnostic;
- it is an exhaustive parameter sweep;
- it provides exact detail already summarized in a main display;
- it documents provenance rather than changing the scientific interpretation.

## 10. Scientific information value per unit of space

A figure consumes page area and reader attention.

Ask:

> What scientifically decision-relevant information does this figure provide per unit of scarce manuscript space and attention?

High-value figures often expose several linked aspects of one central question—effect, heterogeneity, uncertainty, failure boundary—without obscuring the primary pattern.

Low-value figures often:

- visualize one or two values better stated in text;
- duplicate an exact-value table without exposing a pattern;
- show a decorative architecture/workflow already obvious from prose;
- present a complex embedding with no claim it can validly support;
- repeat a conclusion already established more directly;
- use visually impressive but inferentially weak dimensionality reduction or 3D effects.

Do not maximize panel count or visual density.

## 11. Real-paper evidence is calibration, not imitation

Use real published papers in three distinct research layers:

### Broad corpus layer

Use large figure corpora to learn conditional prevalence by field, article type, year, and topic.

This answers:

> What do scientists commonly publish here?

It does **not** answer:

> What representation is best?

### Controlled evidence layer

Use graphical-perception, statistical-cognition, uncertainty-communication and human-computer-interaction experiments to learn when representations improve or impair specific reader judgments.

This answers:

> What do people decode accurately for this task under studied conditions?

### Deep-paper layer

Read complete strong papers and figure captions in context to reconstruct:

- why each main figure was needed;
- why its panels were grouped;
- what alternative representations were possible;
- what information was placed in main text versus supplement;
- how the figure changed the argument;
- what the Discussion inferred from it.

This answers:

> Why did this representation serve this scientific story?

Do not copy visual identity, color palette, layout or panel structure mechanically.

## 12. Analogue-paper figure calibration

For substantial manuscripts, study a small stratified set of close papers when available. Prefer direct inspection of the full figure sequence and captions, not only thumbnails.

Record:

```text
paper / DOI
paper archetype
figure count and role sequence
for each main figure: reader question / evidence role / representation family
main vs Extended Data/SI allocation
what exact values remain outside the figure
what adverse/failure evidence is visible
what appears conventional vs scientifically necessary
counterexample to current assumptions
```

At least one analogue should be selected because it challenges a proposed figure rule when such a counterexample exists.

## 13. Clean-reader figure test

Give the final figure and caption to a field-competent reader with no project context.

They should be able to state:

1. the scientific question;
2. what is being compared or related;
3. the scientific/statistical unit;
4. the meaning of axes, groups, symbols and transformations;
5. the uncertainty shown;
6. the headline pattern;
7. the major boundary or caveat visible in the display;
8. what conclusion the figure supports and what it does not establish.

If the figure only becomes understandable after reading several paragraphs of Results, repair the figure/caption or reconsider whether it is the right representation.

## 14. Final-size and accessibility test

Inspect the assembled manuscript at actual publication size.

Check:

- text/marker/line legibility;
- panel ordering and scanning path;
- colorblind/grayscale accessibility where relevant;
- redundant non-color encoding for critical distinctions;
- scale bars and image annotations;
- axis labels/units;
- legend lookup burden;
- overplotting/occlusion;
- whether uncertainty remains visible at final size;
- whether multi-panel density is still cognitively tractable.

A scientifically valid plot that cannot be read at final size is not a successful manuscript figure.

## 15. Required decision record

For every main or claim-bearing figure/table/mixed display, retain a compact internal record:

```text
figure_id
reader_question
reader_state_before
reader_state_after
claim_ids
scientific_object_or_estimand
statistical_unit
dependence_structure
alternative_explanation
candidate_representations[]
chosen_representation
why_chosen
information_lost
uncertainty_encoding
exact_value_companion
main_or_support
space_rationale
inference_boundary
clean_reader_status
final_size_status
```

This record is internal authoring/audit infrastructure. Do not dump it into the manuscript.

## 16. Blocking failures

Block a claim-bearing display when any applies:

- no reader question or scientific role exists;
- representation chosen only because software/default/template/analogue used it;
- a plausible alternative would preserve materially more claim-relevant information with no worse important cost and was not considered;
- aggregation/projection hides claim-changing structure;
- pairing/dependence is visually misrepresented;
- uncertainty needed for interpretation is absent or mislabeled;
- a transformation materially controls the visual conclusion and is unjustified/unreported;
- figure implies causal/mechanistic/cluster/equivalence conclusions beyond its evidence;
- representative image is used as population-level evidence without appropriate quantification;
- exact primary values required by reporting/science are unrecoverable;
- main figure is a redundant/decorative panel package that does not change reader state;
- critical information is inaccessible at final size or relies on color alone;
- adverse/failure evidence necessary to interpret the headline claim has been visually suppressed.

## 17. Non-blocking review signals

Review, but do not automatically reject, when:

- published analogues commonly use another representation;
- a less familiar plot may reduce audience comprehension despite scientific advantages;
- visual density is high but all panels are scientifically linked;
- exact values could move to a companion table;
- a figure might be replaced by concise prose;
- a support figure may deserve promotion because it changes the claim boundary;
- multiple reasonable representations remain with different trade-offs.

## 18. Guarantee boundary

This contract cannot prove that a chosen figure is globally optimal. Visualization quality depends on human perception, scientific domain, audience expertise, medium, and the actual data. The purpose is to replace habitual/default plotting with explicit, evidence-informed, counterfactual representation reasoning.

Final invariant:

> **A scientific figure must justify both why it exists and why this representation is better for its reader task than the plausible alternatives.**
