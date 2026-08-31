# Manuscript budget utilization and marginal-value contract

> Companion contract to `venue-constrained-manuscript-budget.md` for deciding how much of an available word/page/display budget should actually be used. It prevents two opposite errors: padding a manuscript simply to approach a venue ceiling, and leaving important scientific functions underdeveloped merely because the manuscript is technically under the limit.

## Governing principle

Do **not** maximize words used. Maximize scientifically useful content under the target's publication constraints.

A useful planning heuristic for a mature full paper with a hard main-text word limit is that roughly **85–95% utilization often deserves no special concern**, but this is a diagnostic band, not a quota, norm, or quality score.

Never infer:

```text
90–95% used -> good paper
<85% used -> bad paper
unused words -> add more material
```

Instead use:

```text
scientific sufficiency first
+ target compliance
+ explicit revision reserve
+ marginal value of additional content
```

A 3,300-word paper under a 4,000-word ceiling can be complete. A 3,800-word paper can still be padded, repetitive, or badly allocated.

## 1. Under-utilization is a diagnostic question, not a padding trigger

When a mature manuscript uses substantially less than the available hard main-text budget, ask:

> Is the paper short because it is unusually efficient, or because an important scientific function is missing or compressed?

Audit, in order:

1. Is the central problem/question fully established for a zero-context qualified reader?
2. Are contribution-defining objects, assumptions, terminology and formal relations activated before use?
3. Is the decisive evidence chain complete rather than merely summarized?
4. Does each headline result receive enough interpretation to explain what changed scientifically?
5. Is the strongest plausible alternative addressed when it matters?
6. Are claim-changing limitations and generalization boundaries explicit?
7. Are Methods sufficiently reproducible for the paper type without turning into implementation documentation?
8. Are important negative/adverse results represented rather than silently compressed away?
9. Does the Discussion deepen the result rather than merely restate it?
10. Are displays/captions doing work that makes a shorter main text genuinely efficient?

If these functions are complete, unused words remain unused.

Never repair low utilization by adding generic background, more related work, extra caveats, redundant examples, literature catalogues, development chronology, or repeated summaries.

## 2. The 85–95% band is a heuristic only

For a mature article with a hard word ceiling:

- **below ~80–85%**: trigger a functional-sufficiency review, not an error;
- **~85–95%**: ordinarily no utilization-specific action is needed if section functions pass;
- **above ~95%**: inspect revision headroom and low-value material, especially while substantive revision is expected;
- **100%**: not automatically wrong, but scientifically fragile if clarification or review is still likely.

These bands do not apply mechanically to:

- page-limited venues where rendered area is the binding currency;
- short communications/letters where compactness is intentional;
- structured abstracts or reporting-mandated surfaces;
- article types with advisory rather than hard length guidance;
- disciplines where a complete contribution is naturally much shorter than the allowed maximum.

Exact target rules always override this diagnostic heuristic.

## 3. Reserve is headroom for science, not empty-space theatre

When substantive revision is expected, keep deliberate headroom for genuinely useful additions such as:

- clarification exposed by clean-reader review;
- interpretation of a result whose meaning was underdeveloped;
- one essential comparator or boundary;
- figure/table/legend changes;
- production/template changes.

A useful reserve may correspond to roughly 5–10% of a hard word budget in some mature manuscripts, but there is **no universal reserve percentage**. Derive it from target rigidity, manuscript maturity, expected review burden, figure volatility and article type.

Do not deliberately withhold scientifically necessary content simply to preserve a numerical reserve.

## 4. Allocate from the contribution outward

Do not begin with conventional section percentages and fill them.

Allocate scarce surface in this order:

```text
central scientific question / object
-> reader prerequisites
-> decisive evidence or formal result
-> interpretation / mechanism / strongest alternative
-> claim-changing boundary
-> only then positioning, reproducibility detail and optional enrichment
```

Then map these functions onto the target's section structure.

This prevents a paper from spending hundreds of words on nearest-work positioning while giving the actual formulation, decisive experiment or Discussion only a few sentences.

## 5. Marginal scientific value per unit of space

For every optional addition, compression, display or paragraph, ask:

```text
What scientifically decision-relevant understanding does this add?
What scarce publication surface does it consume?
What higher-value content could that space otherwise support?
```

A conceptual decision aid is:

```text
marginal value
≈ gain in reader understanding
 + gain in evidential strength
 + gain in interpretability
 + gain in reproducibility when claim-relevant
 - duplication
 - cognitive burden
 - displaced higher-priority science
```

Do not turn this into a fake numerical score.

High-value additions often clarify a central object, expose the decisive comparison, distinguish the strongest alternative, explain why a finding matters, or prevent a material misinterpretation.

Low-value additions often repeat background, enumerate neighboring papers, restate caveats, narrate experiment/version chronology, dump provenance, or reproduce values already legible in a table.

## 6. Final available space should deepen before it broadens

When a mature manuscript has remaining space, default to strengthening the weakest central scientific function rather than adding a new substory.

Ask:

> Which existing headline claim is currently least well explained, least well interpreted, least convincingly bounded, or hardest for a zero-context reader to reconstruct?

Prefer deepening that function over:

- another baseline that does not change the claim;
- another Related Work paragraph;
- another robustness analysis with no inferential consequence;
- another caveat already stated elsewhere;
- another implementation detail.

## 7. Compression is asymmetric

When over budget, do not cut every section proportionally.

Default compression order, subject to the current paper's science:

1. exact duplication and generic transition prose;
2. repeated motivation/background;
3. secondary prior-work summaries and exhaustive positioning;
4. repeated qualifications/caveats;
5. implementation/development/provenance detail that belongs in support;
6. redundant examples and non-claim-changing robustness detail;
7. long derivations/routine proof detail that can move to appendix when allowed;
8. only then reconsider core-science scope.

Protect longest:

- the central scientific object/question;
- definitions and assumptions needed for comprehension;
- contribution-defining formal spine;
- decisive evidence;
- uncertainty required to interpret the claim;
- strongest material alternative;
- claim-changing limitation/boundary;
- Discussion needed to explain scientific meaning.

Compression must not produce a technically compliant but intellectually hollow paper.

## 8. Information density is not sentence stuffing

High information density means removing material that does little scientific work while giving difficult, central ideas enough explanation.

Do not optimize density by:

- packing multiple independent claims into one sentence;
- deleting semantic interpretation of equations/results;
- replacing explanation with jargon;
- moving central definitions out of the reader's path;
- converting prose into unexplained tables of identifiers/numbers.

A slightly longer explanation can have higher scientific value per word if it removes ambiguity that otherwise infects the rest of the paper.

## 9. Figures, tables and equations share the attention budget

Word utilization alone is not the manuscript objective.

A useful figure may replace several paragraphs while improving evidence visibility. Conversely, a decorative workflow figure can consume scarce page area and reader attention while adding little.

For each display ask:

- what reader question it answers;
- whether it carries evidence that prose cannot communicate as efficiently;
- what prose/display it displaces;
- whether exact lookup belongs in a table while interpretation stays in prose;
- whether the display preserves the contribution-defining formal object.

For page-limited venues, use rendered page area rather than word-utilization heuristics.

## 10. Under-utilization release test

For a mature manuscript under a hard main-text word limit, a clean reviewer should answer:

1. Is the manuscript materially below the available budget?
2. If yes, which central scientific function, if any, is still underdeveloped?
3. Would adding content strengthen that function, or merely increase length?
4. Is the Discussion deep enough relative to the importance of the results?
5. Is the problem/formulation/setup deep enough to support later terminology, tables and experiments?
6. Are missing explanations being hidden behind citations, labels or presumed project knowledge?
7. If no central function is missing, can the manuscript remain shorter without loss? If yes, pass without padding.

## 11. High-utilization release test

When a mature hard-limited manuscript is above roughly 95% utilization, ask:

1. Is substantive revision still expected?
2. Is there enough reserve for likely clarification?
3. Which paragraph/display currently has the lowest marginal scientific value?
4. Is any nearest-work, caveat, provenance, robustness or implementation material displacing P1–P3 content?
5. Could support material absorb lower-priority detail without hiding claim-changing evidence?

Do not compress merely to hit 90–95%; compress only when the released space can improve resilience, clarity or scientific allocation.

## 12. Pipeline integration

Use this contract whenever:

- the target has a hard main-text word limit;
- a manuscript is materially shorter than its available budget and appears underdeveloped;
- a manuscript is close to its ceiling while further revision is expected;
- section allocation is being decided;
- a reviewer asks for new content under a fixed limit;
- compression threatens the problem formulation, formal spine, decisive Results or Discussion.

It complements rather than replaces:

- `venue-constrained-manuscript-budget.md`;
- `manuscript-section-craftsmanship.md`;
- `manuscript-narrative-architecture.md`;
- `explanatory-sufficiency.md`;
- `formal-spine-preservation.md`;
- `main-text-discipline.md`.

Final rule:

> **Use as much space as the science needs, not as much space as the venue allows. Investigate conspicuous unused space for missing science; never fill it for its own sake.**
