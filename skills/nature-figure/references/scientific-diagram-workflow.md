# Scientific diagram and illustration workflow

Use this reference for manuscript-facing **flowcharts, mechanism diagrams, conceptual schematics, state diagrams, study workflows, algorithm diagrams, experimental timelines, system diagrams, graphical models, and mixed diagram+data figures**.

The goal is not `make boxes and arrows prettier`. The goal is to encode the scientific relationship with the right topology, layout engine, visual hierarchy, and publication-quality vector output.

## Core principle

Start from the relationship graph:

```text
entities/states/processes
+ edge meanings
+ grouping/levels
+ reading direction
+ evidence status
-> diagram topology
-> layout backend
-> visual hierarchy
-> manuscript integration
```

Do not start from a decorative template.

## Diagram necessity test

Use a diagram when prose alone imposes unnecessary working-memory load because the reader must reconstruct:

- a multi-step process;
- branching decision logic;
- causal/mechanistic relationships;
- hierarchy/containment;
- state transitions;
- data flow;
- experimental timeline;
- interacting components;
- spatial arrangement;
- study population flow;
- conceptual taxonomy.

Do not add a workflow diagram merely because top papers often have a Figure 1 schematic.

## Topology first

Classify the scientific relation.

### Directed acyclic flow / pipeline

Examples:

- cohort selection;
- preprocessing/analysis stages;
- experimental workflow;
- evidence/decision pipeline.

Prefer layered left-to-right or top-to-bottom layout.

### Branching decision tree

Use explicit decision nodes and label branches with the criterion/outcome.

### State machine / cycle

Use when entities transition among repeatable states. Curved/recurrent arrows should encode real transitions, not decoration.

### Hierarchy / taxonomy

Use tree/cluster structure. Avoid arbitrary arrows between sibling categories.

### Network / interaction graph

Use force-directed/network layout only when pairwise relationships/network topology are the object of interest. Do not turn a causal pathway into a hairball.

### Mechanism/process schematic

Often needs custom spatial placement rather than automatic graph layout because physical/biological location matters.

### Timeline

Use a common time axis and aligned events. Do not use a generic flowchart if duration/order is the key variable.

### Mathematical/conceptual diagram

Use geometry, axes, regions, manifolds, sets, transformations, or commutative relationships as required by the concept.

## Backend toolkit inspired by mature open-source peers

These are optional implementation routes, not mandatory dependencies and not sources of scientific content.

### Graphviz

Best for:

- directed flows/DAGs;
- hierarchical diagrams;
- clustered pipelines;
- dependency graphs;
- medium-size networks.

Useful engines:

- `dot` — layered directed graphs; aims edges in one direction and reduces crossings/edge length;
- `neato` / `fdp` / `sfdp` — force-directed network relations;
- `circo` — circular topology;
- `twopi` — radial layout.

Graphviz produces SVG/PDF and supports clusters, node/edge attributes, shapes and typography.

**Publication rule:** use automatic layout to solve geometry, then inspect the output at final size. Automatic graph drawing does not know the scientific emphasis hierarchy.

### Schemdraw

Best for:

- electrical/electronic circuits;
- signal-processing diagrams;
- state machines;
- compact flowcharts;
- precise arrows/connectors;
- SVG-first schematics.

Its flow module provides process/decision/state blocks, anchors, arrows, arcs and containers.

**Publication rule:** use its primitives when they match the scientific object; do not make a biology paper look like an electrical diagram merely because the library is available.

### Mermaid

Best for:

- fast logic drafts;
- flowcharts;
- state diagrams;
- sequence diagrams;
- manuscript planning/collaboration where text-defined diagrams are useful.

Use Mermaid as a **logic/prototyping layer** when convenient. For final high-density scientific figures, inspect whether its layout/typography gives enough control; redraw or post-process to vector when needed.

### Python `diagrams` / Graphviz wrappers

Projects such as `mingrammer/diagrams` demonstrate useful diagram-as-code ideas:

- nested clusters;
- reusable node/edge abstractions;
- consistent themes;
- explicit flow direction;
- Graphviz-backed automatic placement.

That project is specialized for software/cloud architecture. Borrow the **design-as-code patterns**, not its iconography or infrastructure aesthetic for unrelated scientific mechanisms.

### Matplotlib / SVG custom drawing

Best for:

- mechanism schematics with scientific geometry;
- hybrid data + diagram panels;
- annotated spatial processes;
- bespoke icons/shapes;
- exact journal-size typography;
- tightly integrated plot/schematic visual language.

Use `matplotlib.patches`, paths, annotations and transforms or an SVG-native route. Keep all text editable/vector where possible.

### TikZ / vector-authoring route

Useful for:

- mathematical diagrams;
- precise publication geometry;
- LaTeX-native typography;
- commutative/graphical structures.

Use only when the user's workflow supports it; do not force LaTeX drawing for a Python/R manuscript pipeline.

## Icon/illustration assets

External icon libraries can reduce redraw effort, but every asset needs:

- compatible license;
- attribution if required;
- scientific accuracy;
- coherent visual treatment;
- no trademark/brand misuse;
- provenance record.

Do not scrape attractive scientific icons or figures from papers and reuse them.

When a licensed icon set is used, normalize visual weight/line style so the figure does not become an `icon soup` collage.

## Diagram grammar

### Nodes

Each node should represent one coherent thing:

- entity;
- state;
- process;
- decision;
- compartment;
- evidence/result;
- population/stage.

Use concise labels. Put explanations in legend/body rather than shrinking long paragraphs into boxes.

### Edges

Every arrow must have a defined semantic meaning.

Examples:

- causes/activates/inhibits;
- transforms;
- flows to;
- precedes;
- selects/excludes;
- measures;
- trains on;
- predicts;
- depends on;
- corresponds to.

If different edge semantics exist, distinguish them by line style/arrowhead/labels and explain the encoding.

Do not use arrows merely to guide the eye when they imply causality.

### Grouping

Use whitespace/enclosure to show:

- experimental stages;
- cellular compartments;
- populations;
- computational modules;
- evidence classes;
- conceptual levels.

Do not box everything.

### Reading direction

Choose one dominant reading flow. Avoid unnecessary zig-zag/serpentine paths.

Use left-to-right for process/causal narratives when compatible with the target layout; top-to-bottom can work for hierarchical/study flow. Physical mechanism diagrams may follow spatial reality instead.

## Visual hierarchy

Prioritize:

1. scientific path/relationship;
2. primary entities/stages;
3. decision-changing branch or mechanism;
4. secondary annotations;
5. decorative detail.

The reader should be able to identify the diagram's message at manuscript viewing size before reading every label.

## Beauty through constraint

A professional diagram usually benefits from:

- consistent line weights;
- consistent corner radii/shape grammar;
- restrained semantic color system;
- aligned baselines/centers;
- controlled whitespace;
- repeated spacing increments;
- readable labels;
- no gratuitous gradients/3D shadows;
- limited icon styles;
- visually balanced clusters;
- short, meaningful arrows.

Do not equate `beautiful` with `decorative`.

## Scientific color semantics

Assign colors by meaning, not by box index.

Examples:

- treatment/control;
- observed/inferred;
- input/process/output;
- activation/inhibition;
- train/validation/test;
- healthy/disease when ethically/semantically appropriate.

Use non-color cues when important. Check grayscale/color-vision accessibility.

## Mechanism diagrams

For a claimed mechanism, separate:

- directly observed elements;
- inferred/putative elements;
- established prior-knowledge elements;
- experimentally manipulated steps.

Use visual encoding or legend wording so inference does not look like direct observation.

Do not draw an arrow as established causality if the manuscript only shows association.

## Study/clinical flow diagrams

Show:

- source population;
- eligibility/exclusion;
- allocation/groups;
- follow-up/analysis population;
- losses/exclusions with counts when required;
- relevant timing.

Use the applicable reporting guideline rather than inventing a flowchart grammar.

## Computational/ML diagrams

Keep architecture figures at the scientific abstraction level.

Show only modules/data transformations needed to understand or evaluate the contribution.

Do not expose:

- source-code filenames;
- class/function names;
- repository modules;
- config keys;
- internal checkpoint names;
- file paths.

The figure should describe the **method**, not the codebase.

## Hybrid diagram + quantitative evidence

A strong main figure can combine:

- orientation schematic;
- decisive quantitative result;
- validation/failure panel.

But every panel must share one evidence story. Do not attach an unrelated diagram to make the figure look sophisticated.

## Label and caption rules

All diagram text is manuscript-facing.

Before delivery, run:

- terminology ledger;
- manuscript surface QA;
- target-aware legend/caption rules.

Never leave Graphviz node IDs, Mermaid syntax, Python variable names, filenames or internal module labels in the final figure unless they are scientifically meaningful identifiers.

## Layout QA

Inspect:

- edge crossings;
- ambiguous arrow endpoints;
- labels colliding with edges;
- uneven node spacing;
- excessively long edge routes;
- cluster nesting depth;
- visual center of mass;
- panel balance;
- reading path;
- final physical-size text;
- accessibility.

Automatic layout is a starting solution, not a publication verdict.

## Source inspiration and boundary

Useful peer projects/frameworks include:

- Graphviz — graph layout and vector export;
- Schemdraw — schematic/flow/state primitives;
- Mermaid — text-defined flow/state/sequence diagrams;
- `mingrammer/diagrams` — Graphviz-backed diagram-as-code architecture patterns.

Use their documented APIs/libraries according to their licenses when appropriate. Do not copy project source code or visual assets into this repository merely to imitate them.

We absorb **capabilities and design lessons**, then build original scientific diagrams for the current manuscript.

## Output contract

For a diagram task, maintain:

```text
Scientific purpose
Diagram topology
Entities/nodes
Edge semantics
Groups/compartments
Evidence status encoding
Reading direction
Chosen backend + reason
Main/support placement
Caption/body explanation split
Accessibility checks
Surface-leakage checks
```

The final criterion is not `looks professional` alone. The diagram must make a scientifically valid relationship easier to understand.