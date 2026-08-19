# Section: Results / Experiments (writing)

## Reader job

Results should let the reader recover:

`what question was examined -> what evidence was obtained -> what narrow conclusion that evidence warrants -> why the next analysis follows`

Do not impose one fixed ladder or require every paragraph to be conclusion-first.

## Build an evidence dependency graph

Before prose, map major evidence blocks and the reason each follows the previous one. Common patterns include:

- measurement/assay validation -> main finding -> mechanism
- baseline -> primary comparison -> ablation/diagnosis -> robustness/generalization
- discovery -> independent validation -> external validation
- descriptive pattern -> inferential test -> explanatory analysis
- contradiction -> discriminating analysis -> revised interpretation
- capability -> benchmark -> stress test -> failure analysis
- theme -> contrast/negative case -> integrated finding
- theorem/lemma -> main result -> implication

Use the order that makes the paper's inference easiest to follow, not necessarily the chronological experiment order.

## Local result block

A robust block often selects from:

1. **question / local purpose** — what is being tested or established?
2. **setup reminder** — only what readers need to interpret this result
3. **observation / estimate** — what happened?
4. **evidence** — numbers, uncertainty, comparison, qualitative material, proof, figure/table
5. **bounded local inference** — what does this result establish?
6. **bridge** — what new question does it create?

Not every paragraph needs all six. A paragraph may combine evidence and a narrow interpretation when the field/journal permits it.

## Main-text evidence discipline

Load `../../../../nature-shared/core/main-text-discipline.md` before allocating analyses.

- keep decisive discovery and necessary support in the main text;
- keep conclusion-changing robustness, heterogeneity, alternative inference and negative evidence visible enough to constrain the claim;
- move routine diagnostics/provenance/secondary checks to captions, Methods, source data or SI where appropriate;
- do not repeat all display values in prose.

## Reporting rules

- Report direction, magnitude and uncertainty at the level needed to support the claim.
- Define sample size/replicate meaning where ambiguity would affect inference.
- Name comparator/baseline explicitly.
- Match statistical language to the actual analysis; do not use `significant` as a synonym for important.
- Keep observation, model-based estimate and interpretation distinguishable.
- Use figure/table calls as evidence pointers, not as the grammatical subject of every paragraph.

## Commentary boundary varies

Some journals/fields integrate interpretation into Results; others reserve most interpretation for Discussion or use a combined Results and Discussion section.

Therefore:

- do not ban all interpretive sentences from Results;
- do not turn Results into a Discussion by speculating beyond local evidence;
- follow exact journal/article-type convention after the scientific evidence map works.

## Computational/benchmark subtype

For ML/engineering experiments, common evidence questions include:

- Are baselines fair and competitive?
- Does the main result hold across datasets/tasks?
- Which components matter (ablation)?
- What mechanism/behavior explains performance?
- What are runtime/compute/data trade-offs?
- Does it generalize or fail under shift/stress?
- Are uncertainty and repeated-run variation reported where relevant?

Load `references/experiments.md` for deeper benchmark-specific planning.

## Anti-patterns

- `Experiment 1 / Experiment 2` with no argument linking them
- a strong claim followed by only a figure pointer
- paragraph-by-paragraph conclusion statements with no visible uncertainty
- exhaustive reviewer-defense analyses crowding out the decisive evidence chain
- interpreting every small difference as mechanism
- hiding a failed/limiting test that changes the headline conclusion
- repeating the same result in prose, caption and Discussion

## Handoff test

After each major block ask: **What did we learn, and what question becomes worth asking next because of it?**

If the next subsection cannot answer that question or clearly open a new evidence branch, reconsider the sequence.