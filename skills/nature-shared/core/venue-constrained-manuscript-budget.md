# Venue-constrained manuscript budget and allocation contract

> Shared contract for treating manuscript space as a finite scientific resource when a target venue, article type, or page/word constraint is known. The purpose is not to force universal section percentages. It is to allocate limited publication surface to the scientific functions that most strongly determine reader understanding and evaluation.

## Core principle

A manuscript budget is not a late copy-editing problem.

When the target imposes a finite word, page, character, display-item, reference, legend, or other publication limit, budget the paper **before prose expansion**.

The governing optimization is:

```text
finite publication surface
-> required venue/compliance surfaces
-> reader prerequisites
-> decisive evidence/formal spine
-> interpretation and claim-changing boundaries
-> only then secondary positioning, robustness detail, provenance, and enrichment
```

A technically correct paper can still be badly allocated if it spends too much space on secondary prior-work accounting, defensive caveats, development chronology, or implementation detail while leaving the problem, method, decisive result, or scientific meaning underdeveloped.

## 1. Resolve the exact budget tuple

When a target is specified, resolve from current official sources:

```text
exact venue
× exact article/content type
× submission stage
× as-of date
```

Then record every applicable limit separately.

Possible limit classes include:

- title words/characters/printed lines;
- abstract/summary words;
- main-text words;
- total content pages;
- display items;
- figure/table area or page consumption;
- figure-legend words;
- Methods words/pages;
- reference count;
- appendix/supplement eligibility;
- checklist, impact, ethics, availability, or other mandatory surfaces;
- file/template/layout constraints that change usable space.

Do not infer a budget from the journal name alone. Article types within the same venue can have very different limits.

### Count-basis table

For each surface, record:

```text
surface
limit unit
hard / guideline / none stated
included in main limit? yes/no/conditional
official source
observed/effective date
current actual
remaining budget
```

If the venue does not state a limit, record `none_stated`; do not invent one.

## 2. Budget units are venue-specific

### Word-constrained venues

Track counted words according to the exact official exclusion rules.

Do not assume abstract, Methods, references, captions, acknowledgements, or supplementary material are included or excluded; resolve each one.

### Page-constrained venues

The binding resource is the **rendered page**, not source word count.

Figures, tables, equations, whitespace, headings, captions, algorithms, footnotes, and column breaks all consume page area. A source-level word count is only a planning proxy.

For page-limited targets:

1. budget approximate text/figure area early;
2. compile in the official template;
3. measure actual page use repeatedly;
4. reallocate after every major figure/table/equation change;
5. never shrink fonts/margins or otherwise violate template rules to manufacture space.

### Mixed budgets

Some targets constrain words **and** display items/references/legends. Track them as separate currencies; one cannot always compensate for another.

A spare reference slot does not buy 100 words. A spare word does not buy a seventh figure when the display limit is six.

## 3. Build a publication-surface inventory

Before detailed drafting, inventory every potential manuscript surface. Mark each as `required`, `scientifically_needed`, `optional`, `support_only`, or `not_applicable` for the current paper and target.

Potential surfaces include:

### Front matter

- title;
- subtitle if permitted;
- abstract/summary;
- keywords;
- highlights/significance statement;
- graphical abstract/TOC item if required;
- author/affiliation metadata.

### Main scientific narrative

- opening context/problem;
- knowledge/decision gap;
- contribution statement;
- closest-prior-work positioning;
- problem formulation/theory/framework;
- study/task/data/system setup;
- Methods content that must remain in main text;
- decisive Results blocks;
- robustness/generalization/ablation blocks when claim-changing;
- Discussion/interpretation;
- limitations/boundaries;
- conclusion/closing synthesis when useful or required.

### Displays

- figures;
- tables;
- equations/display mathematics;
- algorithms/pseudocode;
- boxes/sidebars where allowed;
- figure/table legends/captions.

### Back matter/compliance

- references;
- Methods if separated;
- Data Availability;
- Code Availability;
- ethics/IRB/consent statements;
- broader impact/societal impact when required;
- acknowledgements;
- funding;
- author contributions;
- competing interests;
- reporting checklist;
- appendices;
- Supplementary/Extended Data.

A surface being required by the publication package does not mean it belongs in the counted main narrative.

## 4. Allocate by scientific function, not conventional section name

Build a **section/function budget ledger** before prose expansion.

For each planned section/subsection/result block, record:

```text
section_id
reader question
scientific function
claims enabled/supported
prerequisites introduced
priority class
counted surface? yes/no
budget unit
soft target/range
hard ceiling if target-specific
current actual
variance
scientific reason for variance
overflow/compression route
```

### Priority classes

Use these as functional priorities, not rigid section order:

- `P0 mandatory_target_or_integrity` — content required by venue, ethics, reporting, or scientific integrity;
- `P1 reader_prerequisite` — definitions/setup/context without which later claims cannot be understood;
- `P2 decisive_claim_evidence` — results/proofs/comparisons that establish headline claims;
- `P3 interpretation_boundary` — meaning, strongest alternative, uncertainty, claim-changing limitation, generalization boundary;
- `P4 positioning_context` — enough prior-work/context to orient and distinguish the contribution;
- `P5 reproducibility_support` — implementation/procedural depth needed for replication but not first-pass narrative;
- `P6 optional_enrichment` — secondary examples, extra historical context, extended robustness, exhaustive literature accounting.

P4–P6 should not crowd out an underdeveloped P1–P3 function.

## 5. No universal section percentages

Do **not** encode rules such as:

- Introduction must be 15%;
- Related Work must be 20%;
- Discussion must be 10%;
- Methods must be 25%.

Those ratios vary by venue, article type, archetype, field, figure density, and scientific story.

Instead derive soft ranges from three inputs:

1. official target constraints;
2. the current paper's argument/claim dependency graph;
3. a small set of strong close analogues in the same venue/article type when available.

Analogue proportions are descriptive priors, not quotas.

## 6. Functional minimum before stylistic compression

For every section, define the **minimum scientific payload** before setting a word/page target.

Examples:

### Opening / Introduction

Needs enough space to establish only what the reader must know to understand:

- the problem;
- why it matters for this paper;
- what is unresolved;
- what this paper asks/does;
- the bounded contribution.

It does not need a field history unless that history is necessary to the gap.

### Problem formulation / theory opening

Must activate every central object, assumption, target, comparator role, and formal relation later used.

If that cannot fit within the current budget, simplify notation, merge redundant objects, move derivations to support, or reconsider the paper's scope. Do not solve the problem by leaving objects undefined.

### Results

Protect the shortest evidence chain that establishes the headline case.

A result block earns space by answering a decision-relevant question, discriminating an alternative, establishing generalization/boundary, or providing required uncertainty.

### Discussion

Allocate enough space to interpret the headline findings, compare the strongest relevant alternative/prior work, state the claim-changing boundary, and explain the scientific consequence.

Do not turn Discussion into a second literature review or an integrity ledger.

## 7. Closest / nearest work receives a function-limited budget

Nearest-work analysis is essential **internally** for novelty and fair attribution, but its manuscript footprint should be the minimum needed to perform reader-facing functions.

The manuscript normally needs to do only the relevant subset of:

1. identify the intellectual origin/established baseline;
2. name the closest relevant comparator or conceptual predecessor;
3. state the exact unresolved difference/gap;
4. explain how the present paper differs;
5. revisit the closest work in Discussion if the new result changes interpretation.

Do not publish the entire internal nearest-work matrix, donor map, ownership analysis, claim-subtraction ledger, or exhaustive search inventory.

A dedicated Related Work section is optional unless the venue/genre or argument benefits from it.

### Positioning-overweight review trigger

Review the allocation when:

- prior-work positioning consumes enough space that the central problem/setup is compressed;
- several paragraphs repeat essentially the same novelty distinction;
- each nearby paper receives a mini-summary although only one distinction matters;
- a long Related Work section is followed by a one-paragraph formulation of the paper's own scientific object;
- Discussion spends more effort restating nearest work than interpreting the paper's findings.

No numeric ratio is universal; compare against the paper's unresolved reader needs and the target/analogue budget.

## 8. Displays have an opportunity cost

Every figure, table, equation block, algorithm, and large caption consumes scarce publication surface even when the venue counts only pages.

For every display, record:

```text
display_id
reader question
claim/evidence role
space cost
text displaced
can multiple panels be logically combined?
can exact values move to a table/support artifact?
main/support/omit
```

Protect displays that allow the reader to evaluate distributions, relationships, uncertainty, mechanism, heterogeneity, or complex formal structure more efficiently than prose.

Remove decorative or redundant displays.

### Formal papers

Preserve the contribution-defining formal spine in main text.

Move long derivations, routine lemmas, exhaustive cases, and proof details to appendix/support when the target permits, but do not delete the formal object/operator/decisive implication merely because equations consume vertical space.

## 9. Abstract and title are separate micro-budgets

Do not write the abstract by shrinking the Introduction after the fact.

Resolve the target's abstract/title limits first and budget their functions explicitly.

An abstract normally needs the minimum target-appropriate subset of:

```text
problem/context
-> gap/question
-> approach/design
-> decisive result
-> bounded meaning
```

The exact number of sentences depends on the target.

Do not spend abstract space on project labels, exhaustive caveats, secondary baselines, or reference accounting unless essential.

The title budget should be spent on the scientific object/question/result, not internal project identity.

## 10. Captions and legends are not free storage

Resolve whether captions/legends count toward the target limit.

Even when excluded, keep them functionally disciplined:

- identify what is shown;
- decode groups/panels/symbols/units/statistics;
- state sample/statistical units and uncertainty where needed;
- avoid duplicating Results prose;
- avoid turning legends into hidden Methods/Discussion unless the target requires it.

A 300-word legend can still impose reader cost even if it is not counted against main text.

## 11. References are selected under a relevance budget

Reference count is not a literature-search target.

The internal search may be broad; the manuscript bibliography should be selective and fair.

Prioritize references that:

- establish essential background;
- identify intellectual origin;
- define the closest comparison;
- support claim-bearing context;
- provide methods/data provenance;
- represent material contradictory/limiting evidence.

Do not consume reference slots to document every paper inspected during novelty search.

When the venue recommends/limits references, track the count early rather than deleting citations indiscriminately at submission time.

## 12. Methods, appendices, and supplement are allocation valves, not hiding places

Use non-main surfaces for detail that is scientifically necessary but not needed in the first-pass argument.

Good candidates often include:

- long derivations/proofs;
- full hyperparameter/configuration tables;
- secondary robustness analyses;
- extended ablations;
- exhaustive benchmark tables;
- implementation details;
- machine-readable provenance;
- full literature-search inventory.

Do **not** move to support:

- evidence that changes the headline claim;
- a limitation that materially narrows the claim;
- a comparator necessary to judge the central result;
- a definition required to understand the main result;
- adverse evidence that reverses the interpretation.

## 13. Every addition must be funded

Once a target budget is active, new manuscript content has an opportunity cost.

For every substantive addition during revision, record one of:

- funded from remaining reserve;
- replaces existing text;
- compresses another section;
- moves lower-priority detail to Methods/appendix/SI/artifact;
- increases total length because the venue permits it and the scientific gain justifies it;
- creates a target mismatch requiring article-type/venue reconsideration.

Do not let reviewer revisions accumulate indefinitely as append-only prose.

A response letter can explain the full repair history; the manuscript should contain only the resulting science.

## 14. Maintain a deliberate reserve

For hard word/page targets, avoid drafting the first complete version exactly to the ceiling when revision is still expected.

Maintain an explicit **reserve** for:

- reviewer-required clarification;
- a missing result interpretation;
- an additional essential comparator;
- figure/legend expansion;
- production/template changes.

There is no universal reserve percentage. Choose it from target rigidity, manuscript maturity, figure volatility, and expected revision stage.

If reserve falls to zero, every new addition requires explicit reallocation.

## 15. Budget by information gain, not paragraph count

For each candidate paragraph/display, ask:

> What decision-relevant understanding does the reader gain per unit of scarce publication surface?

High-value units often:

- define a central object used throughout the paper;
- distinguish the strongest alternative;
- show the decisive result;
- expose uncertainty/heterogeneity;
- explain why a result changes understanding;
- prevent a material misinterpretation.

Low-value units often:

- repeat a conclusion already visible;
- narrate development chronology;
- list inspected prior work without a distinction;
- restate caveats;
- reproduce artifact metadata;
- explain code structure rather than science.

Do not reduce this to a numeric score. The question is a decision aid.

## 16. Reallocate after figures and layout stabilize

A budget plan is provisional until rendered.

Re-run allocation when:

- a figure grows/shrinks;
- a table is added;
- a theorem/equation block changes substantially;
- the target template changes column/page usage;
- a reviewer adds a new decision-relevant requirement;
- an abstract/title change alters duplication;
- a result is removed/narrowed;
- a section moves to/from appendix or Methods.

For page-limited targets, final compliance is determined from the rendered official template, not estimated words.

## 17. Manuscript budget ledger

Maintain a compact ledger during substantial writing/revision:

```text
target tuple:
budget basis:
hard limits:
guideline limits:
count exclusions:
reserve:

surface | function | priority | target | actual | delta | action
```

Then a section-level ledger:

```text
section | reader question | claims | soft range | actual | status | repair
```

Possible statuses:

- `within_budget`;
- `underdeveloped`;
- `overweight`;
- `over_limit`;
- `needs_render_measurement`;
- `unresolved_target_rule`;
- `reallocate`.

## 18. Pre-review budget audit

Before simulated review/submission, verify:

1. exact target/article-type limits were resolved from current official sources when available;
2. every counted/excluded surface is known;
3. main text/display/reference limits are currently satisfied or explicitly unresolved;
4. P1–P3 functions are not underdeveloped because P4–P6 content consumed the budget;
5. nearest-work/Related Work is selective rather than exhaustive;
6. every main display earns its space;
7. abstract/title use their micro-budget on the scientific message;
8. legends/captions do not duplicate prose excessively;
9. important definitions/evidence/boundaries were not exiled to support to solve length pressure;
10. revision additions were funded rather than merely appended;
11. a remaining reserve exists when further substantive revision is expected, or zero-reserve status is explicit;
12. page-limited manuscripts were measured in the official rendered template.

## 19. Reviewer/editor budget questions

At least one reader/editor pass should ask:

- What section is consuming the most scarce main-text/page budget, and does its scientific function justify that?
- Which central reader question is most underfunded?
- Is prior-work positioning longer than needed to establish the actual novelty boundary?
- Could a table/figure replace lower-yield prose, or is a display itself wasting space?
- Did reproducibility/audit detail crowd out interpretation?
- Are caveats repeated because the manuscript lacks one well-placed boundary statement?
- Is the Discussion spending space on literature inventory instead of meaning/alternatives/implications?
- Would removing 10% of the manuscript damage the central evidence chain? If not, where is the low-yield material?

The last question is diagnostic, not a requirement to shorten by 10%.

## 20. Target examples and transfer limits

Different current targets illustrate why this contract must remain target-specific:

- a Nature Computational Science Article currently specifies a main-text word limit, abstract limit, display-item limit, and reference guideline;
- flagship Nature uses page/word/display trade-offs and explicitly notes that larger composite figures require text reduction;
- NeurIPS uses a content-page limit in which figures and tables consume the same page budget as prose;
- TMLR permits any length but states that unusually long papers and main bodies over 12 pages can incur longer review timelines.

These examples justify budget resolution, not universal section ratios.

## Non-negotiable boundaries

Never use space pressure to:

- hide contradictory/adverse evidence;
- remove a claim-changing limitation;
- delete a definition needed for comprehension;
- remove required statistics/uncertainty;
- delete the contribution-defining formal spine;
- violate a venue template;
- shrink typography/margins illegitimately;
- cite fewer sources by dropping fair attribution or material contrary evidence;
- replace scientific explanation with dense undefined notation;
- turn supplementary material into a hidden dependency for understanding the main claim.

The objective is **maximum scientific and reader value under the actual publication constraint**, not maximum compression.