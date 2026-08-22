# Explanatory Sufficiency: Is the Paper Explained Enough?

[中文](explanatory-sufficiency.md)

A paper can be concise, grammatically clean, and still be hard to understand because it has compressed away the reasoning the reader needs. This guide explains how to detect and repair **explanatory underspecification** without making the manuscript verbose.

## The central problem

Machine-assisted writing often jumps from a label to a conclusion:

```text
We introduce X, which improves Y.
```

The sentence may be correct, but the reader may still not know:

- what X changes;
- why that change should affect Y;
- how Y is measured;
- what comparison makes the improvement meaningful;
- when the claim stops holding.

The right question is not `Can this be shorter?` It is:

> Can the intended reader reconstruct the scientific idea without supplying missing premises themselves?

## Minimum sufficient explanation

For each important new idea, use only the explanation elements the reader needs:

1. **Identity** — what is it?
2. **Purpose** — why is it needed here?
3. **Mechanism / logic** — how does it work or how does the inference follow?
4. **Evidence / observable consequence** — how do we know?
5. **Boundary / assumption** — when does it hold?
6. **Connection** — what does it enable next?

Not every idea needs all six. A familiar field term may need none; a paper-defining mechanism may need nearly all of them.

## Adaptive elaboration

Spend explanation where three factors are high:

`centrality × unfamiliarity × inferential dependence`

Elaborate more for:

- the central new concept;
- a mechanism required for the headline claim;
- a cross-disciplinary method unfamiliar to the target readership;
- a consequential analytical choice;
- a new metric whose scale is not intuitive;
- a surprising result;
- a failure boundary that changes the interpretation;
- an assumption on which the main conclusion depends.

Compress:

- routine specialist knowledge;
- already explained definitions;
- implementation details with no scientific consequence;
- secondary robustness checks that do not change the interpretation.

## Hidden-premise test

For every important inference A → B, ask:

> What must the reader know or believe for B to follow from A?

A missing premise can be:

- safe shared knowledge;
- already established in the manuscript;
- specialist but essential and worth one sentence;
- a paper-specific assumption that must be stated;
- a disputed inference that needs evidence or qualification;
- an unsupported leap that should be removed.

Words such as `therefore`, `thus`, and `suggesting that` do not create the missing logic.

## Section-by-section expectations

### Introduction

Explain enough for the reader to understand the problem, why existing knowledge does not settle it, what question is being asked, and why the proposed contribution could answer it. Do not turn the Introduction into a textbook history.

### Methods

For consequential choices, explain:

`what was done → how → why this choice → assumptions/parameters that affect interpretation`

A list of software packages or method names is not a scientific explanation.

### Results

A major Results block should normally make recoverable:

`local question → essential setup/comparison → observation/estimate → evidence/uncertainty → bounded inference → why the next analysis follows`

Do not repeat detailed Methods unless the reader needs a brief reminder to interpret the result.

### Discussion

Do not jump directly from a finding to broad significance. Make the intermediate scientific meaning visible:

`finding → interpretation → relation to alternatives/prior evidence → boundary → implication`

### Figures

The main text should tell readers **what to notice and why it matters**. The legend should tell them **what is shown and how to read it**. Neither should duplicate the other.

### Equations

When an equation is central, define the variables and explain the scientific role of the expression. Formal specialists do not need tutorials on standard notation; cross-disciplinary readers may need a short intuitive explanation.

## Common under-explanation patterns

- a new method is named but no scientific rationale is given;
- a metric value is reported without baseline, scale, or uncertainty;
- a mechanism is claimed without discriminating evidence;
- a figure is cited without explaining the pattern;
- an equation is presented without explaining what its terms mean conceptually;
- a citation is used instead of explaining a concept needed locally;
- several reasoning steps are packed into one novelty sentence;
- dense noun phrases hide the relationships among concepts.

## Do not over-correct

Explanation can also become excessive. Cut or relocate material when:

- a definition is repeated without a new purpose;
- specialist readers receive textbook-level explanation of routine knowledge;
- Results repeatedly restate background before each analysis;
- Methods become a tutorial rather than a reproducibility account;
- code/repository operations are explained instead of the scientific method;
- figures are described panel-by-panel when the visual pattern is obvious.

The target is the **first sufficient explanation**, then brief reminders only when the reader needs them.

## Reader reconstruction checklist

For every central idea, result, mechanism, or method choice, ask whether the intended reader can explain back:

- What is it?
- Why is it here?
- How does it work or how does the inference follow?
- What evidence or comparison supports it?
- What important assumption or boundary applies?
- What does it change or enable next?

If several answers require guessing, the manuscript needs more explanation even if the prose already sounds polished.

## Research basis

Current Nature Portfolio guidance explicitly warns authors not to assume that every reader has the specialist background needed for a study. Flagship Nature requires clear, simple writing accessible across disciplines and notes that highly technical papers may need a slightly longer summary so non-specialists can understand the background and how the result changes the field. Nature Climate Change describes Methods as explaining **what was done, how it was done, and why**, while still using brief method descriptions in the main text when they help readers interpret results.

Reader-comprehension research points in the same direction. Gopen and Swan's reader-expectation framework emphasizes context, sentence linkage, visible actions, and new-information placement. Experimental work on scientific prose found that improving both relationships among text ideas and links to reader knowledge supported deeper comprehension. Jargon studies show that specialist terminology can reduce processing fluency even when definitions are present, reinforcing the need to manage the reader's knowledge state rather than merely define terms once.

The practical rule is:

> Be concise about what the reader already knows; be explicit about the reasoning the reader cannot safely infer.
