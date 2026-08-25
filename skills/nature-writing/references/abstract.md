# Abstract Writing Guide

## Contents

- [Goal](#goal)
- [Pre-Writing Questions (Important)](#pre-writing-questions-important)
- [Version 1: Challenge -> Contribution](#version-1-challenge-contribution)
- [Version 2: Challenge -> Insight -> Contribution](#version-2-challenge-insight-contribution)
- [Version 3: Multiple Contributions](#version-3-multiple-contributions)
- [Example Bank](#example-bank)
- [Abstract Quality Checklist](#abstract-quality-checklist)


## Goal

Write a strong abstract by doing three things repeatedly:

1. Think through the abstract logic first.
2. Follow one template (Version 1/2/3 below).
3. Revise the abstract many times.

## Pre-Writing Questions (Important)

Answer these before writing:

1. What technical problem do we solve, and why is there no well-established solution? (important)
2. What is our technical contribution?
3. Why can our method work in essence?
4. What technical advantage and new insight do we provide? (important)

## Version 1: Challenge -> Contribution

Introduce the technical challenge, then use one to two sentences to present the technical contribution that solves the challenge.

### Structure

1. Task.
2. Technical challenge for previous methods.
3. One to two sentences introducing the technical contribution for solving the challenge.
4. Benefits of the technical contribution.
5. Experiment summary.

### Expert Notes

1. Discuss previous work around the technical challenge that we actually solve.
2. Use a technical name alone only when it is conventional and immediately
   interpretable for the intended reader. Otherwise describe the scientific
   object/role first and defer or omit the label. Do not explain implementation
   detail, but do supply the identity needed to prevent a reading jump.
3. Expand or define every retained non-universal abbreviation, coined term,
   internal label, and formal symbol locally in the standalone abstract.
4. This ability is very important for writing a good abstract.

Version 1 local cite:

1. `references/examples/abstract/template-a.md`

## Version 2: Challenge -> Insight -> Contribution

Introduce the technical challenge, then use one to two sentences to present the insight for solving the challenge, and then one sentence to present the technical contribution that implements this insight.

### Structure

1. Task.
2. Technical challenge for previous methods.
3. One sentence introducing the insight for solving the challenge.
4. One to two sentences introducing the technical contribution that implements the insight.
5. Benefits of technical novelty.
6. Experiment summary.

### Expert Notes

1. Discuss previous work around the technical challenge that we actually solve.
2. Introduce the insight in one clear sentence.
3. Use a technical name alone only when it is conventional and immediately
   interpretable. Otherwise describe the scientific object/role first and defer
   or omit the label. Omit implementation detail, not reader-facing identity.
4. Define retained abbreviations, paper-specific labels, and symbols locally;
   never guess an unknown expansion.
5. This ability is very important for writing a good abstract.

Version 2 local cite:

1. `references/examples/abstract/template-b.md`

## Version 3: Multiple Contributions

Version 3: When there are multiple technical contributions, describe each contribution together with its technical advantage.

### Structure

1. Task.
2. If needed, one contrast sentence about prior methods.
3. Contribution sentence 1 + technical advantage.
4. Contribution sentence 2 + technical advantage.
5. Contribution sentence 3 + technical advantage.
6. Experiment summary.

### Expert Notes

1. When there are multiple technical contributions, describe each contribution together with its technical advantage.
2. The ability to express "contribution + advantage" in one sentence is very important for writing a good abstract.

Version 3 local cite:

1. `references/examples/abstract/template-c.md`

## Example Bank

1. `references/examples/abstract-examples.md`
2. `references/examples/abstract/template-a.md`
3. `references/examples/abstract/template-b.md`
4. `references/examples/abstract/template-c.md`

## Abstract Quality Checklist

1. Can a reader identify task, challenge, insight/contribution, and results in one pass?
2. Are all major claims supported by experiments?
3. Are technical names self-contained and readable?
4. Is there any sentence that mixes too many messages?
5. Is the abstract self-contained even when read without the body?
6. Does every internal/coined label have a necessary reader-facing identity, or
   should it be replaced/removed?
7. Are displayed equations permitted by the exact target and necessary for
   comprehension? For an unknown target, prefer verbal or inline mathematics.
8. Is the notation load proportional to the central result?
