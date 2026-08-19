# Editor/reviewer source basis

> Public-source research basis for the journal-aware reviewer simulation. Last reviewed: 2026-08-19.

## Contents

- [Source hierarchy](#source-hierarchy)
- [Cross-journal findings](#cross-journal-findings)
- [Nature exact findings](#nature-exact-findings)
- [IEEE findings](#ieee-findings)
- [PLOS findings](#plos-findings)
- [JAMA Network findings](#jama-network-findings)
- [eLife findings](#elife-findings)
- [Empirical anti-gaming findings](#empirical-anti-gaming-findings)
- [Implementation implications](#implementation-implications)

## Source hierarchy

For an actual target journal:

1. exact current official journal editor/reviewer/publication criteria;
2. exact article-type/stage guidance;
3. shared `../nature-shared/core/editor-reviewer-decision-engine.md`;
4. shared `../nature-shared/journal-formats/editorial-decision-profiles.md`;
5. this cross-journal research summary;
6. manuscript facts supplied by the user.

The local Nature source file `editorial criteria and processes.md` remains authoritative **only for flagship Nature Articles within its documented scope**.

## Cross-journal findings

### 1. The editor and reviewer solve different problems

Across conventional peer-review systems, reviewers provide expert assessment while editors make the publication decision. Reviewer recommendations are therefore advisory evidence rather than votes that mechanically determine acceptance.

Operational consequence:

- simulate an **editorial triage/decision layer** separately from independent reviewer reports;
- do not average reviewer recommendations into an acceptance score;
- preserve a technically decisive single-reviewer objection even without majority support.

### 2. Publication criteria vary materially

Current public guidance shows incompatible objective functions:

- selective broad-interest journals can require technical validity **plus** priority/significance/readership;
- PLOS ONE explicitly centers technical rigor and scientific/ethical eligibility rather than perceived importance;
- IEEE exposes scope, novelty, validity, data, clarity, compliance and advancement as separate checks;
- clinical journals can add priority and implications for patient care/policy/research agendas;
- eLife's current model separates significance of findings from strength of evidence and does not use conventional post-review accept/reject gatekeeping.

Operational consequence:

Never use one universal `novelty + rigor + impact` formula.

### 3. Decision-relevant reviewer comments need reasons and resolution tests

Nature and PLOS editor guidance both emphasize reviewer information that allows editors to determine whether publication criteria are met. PLOS specifically tells editors to distinguish comments that **must** be addressed from non-essential feedback and to weight comments according to expertise.

Operational consequence:

Every Major Concern should state:

`challenged claim -> visible evidence -> why insufficient -> decision consequence -> resolution test`.

### 4. Revisions are evaluated on closure, not response length

Official reviewer/editor guidance for Nature, IEEE and PLOS expects authors to address prior concerns in revised manuscripts and responses. A response that says `addressed` without a changed evidentiary state is not closure.

Operational consequence:

Use explicit states such as `resolved_by_evidence`, `resolved_by_analysis`, `resolved_by_correction`, `resolved_by_clarification`, `resolved_by_claim_narrowing`, or `resolved_by_claim_removal`.

## Nature exact findings

Current official Nature guidance says Articles should report original research, be of outstanding scientific importance, and reach conclusions interesting to an interdisciplinary readership.

Nature's initial editor screening can decline manuscripts without peer review even when the technical work may be valid. For external review, Nature asks reviewers to consider strong evidence, novelty, importance, general audience interest, data/methodology and technical failings.

Nature explicitly states that editorial decisions are not vote counting. Editors weigh the arguments and relevant expertise of reviewers and remain reluctant to disregard technical criticisms.

Working exact axes:

- originality;
- scientific importance/significance;
- interdisciplinary readership;
- technical soundness/strong evidence;
- readability for nonspecialists.

Sources:

- https://www.nature.com/nature/for-authors/editorial-criteria-and-processes
- https://www.nature.com/nature/editorial-policies/peer-review

## IEEE findings

IEEE Author Center currently tells reviewers/editors to assess:

- scope;
- novelty;
- validity;
- data analysis/interpretation;
- clarity;
- compliance;
- advancement/contribution.

Reviewer guidance additionally emphasizes literature completeness, method/design soundness, reproducibility, logical flow and supported conclusions.

Sources:

- https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/about-the-peer-review-process/
- https://journals.ieeeauthorcenter.ieee.org/submit-your-article-for-peer-review/become-an-ieee-reviewer/

## PLOS findings

### PLOS ONE

PLOS ONE explicitly contrasts its criteria with importance-gated journals. Peer review asks whether work is technically rigorous and meets scientific and ethical standards for the scholarly record.

Therefore a mock PLOS ONE reviewer must not reject a technically sound manuscript merely because it seems insufficiently high-impact.

Source:

- https://journals.plos.org/plosone/s/reviewer-guidelines

### PLOS selective titles

PLOS Biology and PLOS Medicine demonstrate that PLOS titles do not share one editorial objective. PLOS Biology includes originality, field importance, outside-field interest, rigorous methodology and substantial evidence. PLOS Medicine adds importance of the question, substantial advance and implications for patient care, policy or clinical research agendas.

Sources:

- https://journals.plos.org/plosbiology/s/reviewer-guidelines
- https://journals.plos.org/plosmedicine/s/reviewer-guidelines

### Editor synthesis

PLOS editor resources instruct editors to determine which reviewer comments must be addressed to meet publication criteria and which are non-essential, and to weight comments by expertise rather than treating them uniformly.

Source:

- https://explore.plos.org/editor-resources/editorial-decisions

## JAMA Network findings

JAMA Network reviewer guidance asks peer reviewers to assess manuscript characteristics including:

- quality;
- priority;
- originality;
- data validity;
- reasonableness of conclusions.

The guidance emphasizes that reviewers recommend suitability but editors make final decisions.

Source:

- https://jamanetwork.com/pages/guidance-and-benefits-for-peer-reviewers

## eLife findings

eLife's current Reviewed Preprint model uses an assessment that keeps two dimensions separate:

- **significance of findings** from `useful` through `landmark`;
- **strength of evidence** from `inadequate` through `exceptional`.

This is a valuable cross-journal lesson even when reviewing conventional journals: importance and evidence quality are different variables and should not be collapsed.

Sources:

- https://elifesciences.org/about/elife-assessments
- https://elifesciences.org/articles/83889

## Empirical anti-gaming findings

Peer-review research provides reasons to avoid manipulative `acceptance engineering`.

- A JAMA study found author-suggested reviewers tended to make more favorable publication recommendations than editor-suggested reviewers even when review quality did not differ.
- Recent eLife research on open peer review reports an association between requested/added reviewer citations and reviewer recommendations.

Operational consequence:

Do not use reviewer suggestion strategy, reviewer-targeted citation, or citation concessions as techniques for acceptance. Build the scientific case so it survives independent reviewer selection.

Sources:

- https://jamanetwork.com/journals/jama/fullarticle/202193
- https://elifesciences.org/articles/108748

## Implementation implications

The journal-aware reviewer should:

1. resolve the exact target and publication model;
2. run a bounded **editorial triage simulation** before external-review simulation;
3. create independent reviewer reports against universal scientific axes plus target-conditional axes;
4. freeze reports before synthesis;
5. synthesize reviewer arguments as an editor would, separating blockers, repairable majors, claim recalibration and optional requests;
6. produce an author-facing **decision engineering map** after the simulated decision analysis;
7. never claim certainty about acceptance or invent numeric acceptance probability;
8. recommend transfer/repositioning when target fit is the real problem instead of manufacturing importance language;
9. use `add evidence / reanalyse / correct / clarify / narrow claim / remove claim` as legitimate resolution routes.
