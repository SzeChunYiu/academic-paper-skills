# Scholarly surface semantics failure ledger — 2026-08-30

## Triggering observation

A rendered JMLR-style manuscript exposed a cluster of failures that were individually small but collectively showed a missing boundary in the academic-writing pipeline: authoring, code, audit and build semantics were surviving into publication-facing surfaces.

Observed classes included:

- rhetorical inline bold inherited from authoring/chat markup;
- typewriter/monospace treatment of scientific semantic labels;
- enum-like all-caps/snake-case tokens used as prose concepts;
- raw source-style mathematical tokens outside proper math typography;
- CI/test vocabulary used as scientific result language;
- dashboard/state-machine visual language in a scientific workflow figure;
- missing/ambiguous table caption/numbering structure;
- rendered line overflow/clipping;
- a title-level named construct without a maximally explicit compact definition;
- a derived state-cost difference whose operands required a type/class compatibility audit;
- title modifiers whose formal necessity needed checking;
- novelty phrased correctly as a bounded search-frontier claim but requiring freshness at submission.

## Generalization

These are not one typography defect. They span three independent layers.

### A. Authoring-to-publication semantic boundary

Internal markup and machine-readable tokens must be translated into scholarly prose, mathematical notation, or target-supported labels. Literal code typography is retained only when literal syntax is itself scientifically necessary.

### B. Scientific/formal semantic integrity

A named construct must be explicitly defined. Derived quantities must compare compatible mathematical types/classes/units or supply a proven bridge. Title claims must correspond to the actual formal or empirical machinery. Correctness and contribution mass are separate questions.

### C. Rendered publication integrity

A source file that compiles can still fail as a paper. Every-page rendering review must catch clipping, overflow, missing captions, table numbering drift, accidental font-family changes and diagram typography that obscures scientific hierarchy.

## Transfer limits

- Bold, monospace and all-caps text are not universally wrong; exact target/genre conventions and the scientific role control disposition.
- Software/interface papers may legitimately expose literal tokens when exact syntax is the evaluated object.
- Internal PASS/BLOCKED/CANNOT_CHECK vocabularies remain useful in audit ledgers; the issue is leakage into manuscript result language without explicit scientific definition.
- A simple theorem can support a strong paper when the novel assessment object, empirical evidence, synthesis or certification boundary supplies sufficient contribution mass. The gate must not manufacture theory or experiments merely to increase apparent sophistication.
- Table numbering/caption requirements are target-dependent in exact form, but unexplained numbering gaps and unlabeled manuscript tables remain universal review signals.

## Pipeline response

The repository now adds `scholarly-surface-semantics.md` plus `audit_scholarly_surface_semantics.py`, always loaded by `academic-writing` and `academic-paper-pipeline`. The contract requires a three-layer release audit: source/markup semantics, scientific/formal semantics, and rendered-artifact integrity.
