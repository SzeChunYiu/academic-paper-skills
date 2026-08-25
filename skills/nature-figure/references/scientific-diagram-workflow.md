# Scientific diagram and illustration workflow

Use this reference for manuscript-facing **flowcharts, mechanism diagrams, conceptual schematics, state diagrams, study workflows, algorithm diagrams, experimental timelines, system diagrams, graphical models, and mixed diagram+data figures**.

The goal is not `make boxes and arrows prettier`. The goal is to encode the scientific relationship with the right topology, layout engine, visual hierarchy, and publication-quality vector output.

## Contents

- [Core principle](#core-principle)
- [Diagram necessity test](#diagram-necessity-test)
- [Topology first](#topology-first)
- [Backend toolkit inspired by mature open-source peers](#backend-toolkit-inspired-by-mature-open-source-peers)
- [Icon/illustration assets](#iconillustration-assets)
- [Diagram grammar](#diagram-grammar)
- [Visual hierarchy](#visual-hierarchy)
- [Beauty through constraint](#beauty-through-constraint)
- [Scientific color semantics](#scientific-color-semantics)
- [Mechanism diagrams](#mechanism-diagrams)
- [Study/clinical flow diagrams](#studyclinical-flow-diagrams)
- [Computational/ML diagrams](#computationalml-diagrams)
- [Hybrid diagram + quantitative evidence](#hybrid-diagram--quantitative-evidence)
- [Label and caption rules](#label-and-caption-rules)
- [Layout QA](#layout-qa)
- [Source inspiration and boundary](#source-inspiration-and-boundary)
- [Output contract](#output-contract)

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

Best for directed flows/DAGs, hierarchies, clustered pipelines, dependency graphs, and medium-size networks.

Useful engines include `dot` for layered directed graphs, `neato`/`fdp`/`sfdp` for force-directed networks, `circo` for circular topology, and `twopi` for radial layouts. Graphviz produces SVG/PDF and supports clusters, node/edge attributes, shapes, and typography.

**Publication rule:** use automatic layout to solve geometry, then inspect at final size. Automatic graph drawing does not know the scientific emphasis hierarchy.

### Schemdraw

Best for electrical/electronic circuits, signal-processing diagrams, state machines, compact flowcharts, precise connectors, and SVG-first schematics. Its flow module provides process/decision/state blocks, anchors, arrows, arcs, and containers.

Use these primitives only when they match the scientific object; do not make an unrelated biology mechanism look like an electrical schematic merely because the library is available.

### Mermaid

Best for fast logic drafts, flowcharts, state diagrams, sequence diagrams, and collaborative text-defined planning. Use it as a **logic/prototyping layer** when convenient. For final high-density scientific figures, inspect whether layout/typography control is sufficient; redraw or post-process to vector when necessary.

### Python `diagrams` / Graphviz wrappers

Projects such as `mingrammer/diagrams` demonstrate useful diagram-as-code ideas: nested clusters, reusable node/edge abstractions, consistent themes, explicit flow direction, and Graphviz-backed placement.

That project is specialized for software/cloud architecture. Borrow the **design-as-code patterns**, not its iconography or infrastructure aesthetic for unrelated scientific mechanisms.

### Matplotlib / SVG custom drawing

Best for mechanism schematics with scientific geometry, hybrid data+diagram panels, annotated spatial processes, bespoke shapes, exact journal-size typography, and tightly integrated plot/schematic visual language. Keep text editable/vector where possible.

### TikZ / vector-authoring route

Useful for mathematical diagrams, precise publication geometry, LaTeX-native typography, and commutative/graphical structures. Use only when the user's workflow supports it; do not force LaTeX drawing onto a Python/R workflow.

## Icon/illustration assets

External icon libraries can reduce redraw effort, but every asset needs compatible licensing, attribution when required, scientific accuracy, coherent visual treatment, no trademark misuse, and a provenance record.

Do not scrape attractive scientific icons or figures from papers and reuse them. Normalize licensed asset line weight/style so the figure does not become an `icon soup` collage.

## Diagram grammar

### Nodes

Each node should represent one coherent entity, state, process, decision, compartment, evidence/result, or population/stage. Use concise labels. Put explanation in body/legend rather than shrinking paragraphs into boxes.

### Edges

Every arrow must have a defined semantic meaning, such as causes/activates/inhibits, transforms, flows to, precedes, selects/excludes, measures, trains on, predicts, depends on, or corresponds to.

If multiple edge semantics exist, distinguish them by line style/arrowhead/labels and explain the encoding. Do not use arrows merely to guide the eye when they imply causality.

### Grouping

Use whitespace/enclosure for experimental stages, cellular compartments, populations, computational modules, evidence classes, or conceptual levels. Do not box everything.

### Reading direction

Choose one dominant reading flow and avoid unnecessary zig-zag paths. Left-to-right often suits process/causal narratives; top-to-bottom can suit hierarchy/study flow. Physical mechanism diagrams may follow spatial reality instead.

## Visual hierarchy

Prioritize:

1. scientific path/relationship;
2. primary entities/stages;
3. decision-changing branch or mechanism;
4. secondary annotations;
5. decorative detail.

The diagram's message should be visible at manuscript viewing size before every label is read.

## Beauty through constraint

Professional diagrams usually benefit from consistent line weights and shape grammar, restrained semantic color, aligned baselines/centers, controlled whitespace, repeated spacing increments, readable labels, limited icon styles, balanced clusters, and short meaningful arrows.

Avoid gratuitous gradients/3D shadows. Do not equate `beautiful` with `decorative`.

## Scientific color semantics

Assign colors by meaning, not box index: treatment/control, observed/inferred, input/process/output, activation/inhibition, train/validation/test, or health/disease when appropriate. Use non-color cues for important distinctions and check grayscale/color-vision accessibility.

## Mechanism diagrams

Separate directly observed, inferred/putative, established-prior-knowledge, and experimentally manipulated elements. Use visual encoding or legend wording so inference does not look like direct observation.

Do not draw an arrow as established causality if the manuscript only shows association.

## Study/clinical flow diagrams

Show source population, eligibility/exclusion, allocation/groups, follow-up/analysis population, losses/exclusions with counts when required, and relevant timing. Use the applicable reporting guideline rather than inventing a flowchart grammar.

## Computational/ML diagrams

Keep architecture figures at the scientific abstraction level. Show only modules/data transformations needed to understand/evaluate the contribution.

Do not expose source-code filenames, class/function names, repository modules, config keys, checkpoint names, or file paths. The figure should describe the **method**, not the codebase.

## Hybrid diagram + quantitative evidence

A main figure can combine an orientation schematic, decisive quantitative result, and validation/failure panel when they share one evidence story. Do not attach an unrelated diagram merely to make the figure look sophisticated.

## Label and caption rules

All diagram text is manuscript-facing. Before delivery, run the terminology ledger, manuscript-surface QA, and target-aware legend/caption rules.

Never leave Graphviz node IDs, Mermaid syntax, Python variable names, filenames, or internal module labels in the final figure unless they are scientifically meaningful identifiers.

## Layout QA

Inspect edge crossings, ambiguous endpoints, label/edge collisions, uneven spacing, long edge routes, cluster nesting, visual balance, reading path, final physical-size text, and accessibility.

Automatic layout is a starting solution, not a publication verdict.

## Source inspiration and boundary

Useful peer projects/frameworks include Graphviz for graph layout/vector export, Schemdraw for schematic/flow/state primitives, Mermaid for text-defined diagrams, and `mingrammer/diagrams` for Graphviz-backed diagram-as-code architecture patterns.

Use their documented APIs/libraries according to their licenses when appropriate. Do not copy project source code or visual assets merely to imitate them.

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