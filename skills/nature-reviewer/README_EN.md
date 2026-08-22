# `nature-reviewer` Skill

[中文说明](README.md)

`nature-reviewer` simulates a **journal-aware editor + reviewer decision process** before submission. It does not assume flagship Nature from the legacy skill name and does not count reviewer votes. It resolves the target publication model, separates editorial triage from independent technical review, then produces an editor synthesis and an author-facing repair map.

## What To Use It For

- Stress-test a manuscript, abstract, figure set, or Results storyline before submission.
- Resolve the exact target's decision model rather than applying one universal novelty/impact score.
- Simulate editorial triage: scope, article type, target-specific priority, recoverability of contribution/evidence, and maturity for external review.
- Generate mutually blind reviewer reports with validity/methods, contribution/positioning, and reproducibility/clarity/boundary lenses.
- Require a **resolution test** for every Major Concern.
- Classify issues as publication-criteria blockers, technical blockers, major repairable, claim recalibration, clarity/reporting, or optional enrichment.
- Distinguish `needs more evidence` from `needs reanalysis`, `needs clearer structure`, `narrow/remove claim`, or `change target/article type`.
- Use close analogue papers as **context for field-specific evidence expectations**, never as invented publication policy.
- Check whether main-text content and figures expose the decisive evidence or are cluttered by non-scientific implementation/repository detail.
- Flag missing validation/generalization/failure-boundary plots when the manuscript's headline claims require them.
- Cross-check manuscript-internal terminology, units, counts, numeric precision, Methods facts, tables, and claims.

## Typical Requests

- "Review this for Nature Methods: first simulate editor triage, then three independent reviewers, then synthesize."
- "For this PLOS ONE paper, don't penalize it for not being broad-interest; focus on validity and reporting."
- "Tell me which reviewer concerns really require experiments and which can be closed by narrowing the claim."
- "Are our figures sufficient to support external generalization, or are we hiding site heterogeneity behind pooled metrics?"
- "Which implementation/code details should be removed from the manuscript and left in Methods/availability/repository docs?"

## What You Need To Provide

- Manuscript, key sections, figures/legends, Methods, or author notes.
- Exact target journal/venue and article type when known.
- Known study design, central claims, and any constraints on new experiments/analyses.
- Supplementary evidence when you want the reviewer simulation to consider it.

## Outputs

- Editorial triage simulation.
- Independent reviewer reports.
- Editor synthesis that weighs concern reasoning rather than votes.
- Decision-engineering map with concern class, blocking status, resolution test, and minimum valid repair route.
- Claim/evidence/boundary weaknesses and missing alternative-explanation tests.
- Figure/evidence gaps, including when a new plot or reallocation to main text would improve decisionability.
- Optional target-fit recommendation when the science is sound but the publication objective is mismatched.

## Boundaries

- The skill does not invent reviewer identities, hidden editorial information, or the real journal's final decision/probability.
- Reviewers remain mutually blind; the simulated triage conclusion is not fed into reviewer packets.
- Analogue-paper patterns are contextual evidence expectations, not policy.
- It does not recommend friendly-reviewer selection, strategic reviewer citation, concealment of competitors/adverse evidence, or cosmetic experiments.
- More experiments are not automatically better; evidence, reanalysis, clarification, claim narrowing/removal, or target change can be the right repair.
- For actual post-decision rebuttals/revision packages, use `nature-response`.

## Related Skills

- `nature-writing`: repair argument/content/figures before submission.
- `nature-figure`: design or rebuild missing decision-relevant visual evidence.
- `nature-statistics`: deep statistical validity and reporting audit.
- `nature-response`: close real editor/reviewer concerns after a decision.
