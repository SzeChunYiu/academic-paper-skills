# Acceptance optimization evidence ledger — 2026-08-29

**Purpose:** record what current official policy and empirical meta-research actually support about improving publication opportunity, and separate that from folklore, survivorship bias, and individual-editor/reviewer targeting.

This ledger supports `../core/acceptance-optimization-protocol.md`.

It is not a causal acceptance model and does not justify numeric acceptance probabilities.

## Evidence classes

- **A — direct experimental / quasi-experimental evidence**
- **B — multi-journal / large-scale observational meta-research**
- **C — single-journal / narrow-domain observational evidence**
- **D — official current venue policy / reviewer criteria**
- **E — expert editorial guidance / practice commentary**
- **H — public review-history heuristic / selected case evidence**
- **X — prohibited or invalid optimization**

## Stable conclusions

### 1. There is no universal acceptance function

Different venues explicitly optimize different scientific/publication objectives.

Nature requires technically sound data, strong evidence, novelty, importance to the specific field and interest to a general scientific audience.

Nature Communications initial editorial triage evaluates novelty/potential impact, editorial scope, conceptual or methodological advance and likely readership interest before external review.

PLOS ONE explicitly evaluates original research, technical standard, support for conclusions, intelligibility, ethics, reporting and data standards rather than perceived significance as a universal gate.

TMLR explicitly centers whether claims are supported by accurate/convincing/clear evidence and whether at least some of its audience would be interested, while warning against rejecting technically sound work merely for modest significance.

**Engineering consequence:** exact venue/article-type resolution is a hard prerequisite. Do not create one prestige-weighted score.

Evidence: D.

Sources:

- Nature criteria: <https://www.nature.com/nature/for-referees/policies-and-processes>
- Nature Communications editorial process: <https://www.nature.com/ncomms/submit/editorial-process>
- PLOS ONE criteria: <https://journals.plos.org/plosone/s/criteria-for-publication>
- TMLR acceptance criteria: <https://jmlr.org/tmlr/acceptance-criteria.html>

### 2. Editorial triage is a major, partially subjective bottleneck

A 2026 study of three co-editors-in-chief at the International Journal of Public Health found full independent agreement on desk-screen decisions for only 43% of 30 manuscripts; disagreement was particularly associated with soft criteria such as novelty/originality. Agreement increased after second opinions.

**Engineering consequence:** use independent multi-editor desk lenses and synthesize the strongest valid blocker rather than relying on one simulated editor.

Do not infer that a second opinion universally increases acceptance; in the study it increased agreement and changed screening decisions.

Evidence: C.

Source:

- Künzli et al. 2026: <https://pmc.ncbi.nlm.nih.gov/articles/PMC12979234/>

### 3. Novelty can help, but novelty that is scientifically ungrounded is not the target

A multi-journal study of more than 27,000 manuscripts across Cell, Cell Reports and 47 Institute of Physics journals found higher measured novelty associated with higher acceptance. Higher conventionality was also positively associated with acceptance. Editors selected for novelty even conditional on reviewer recommendations.

This is observational, and the novelty/conventionality measures are bibliometric constructions, not direct judgments of scientific quality.

**Engineering consequence:** aim for a contribution that is genuinely new while strongly situated in established knowledge. Do not maximize novelty by severing the argument from conventional scientific anchors.

Evidence: B.

Source:

- Wang et al., PNAS 2022: <https://doi.org/10.1073/pnas.2118046119>

### 4. Rejection reports repeatedly identify preventable failure classes

A content analysis of 898 rejection reports from the Indian Journal of Psychological Medicine found desk rejection commonly associated with lack of novelty and being out of scope. Post-review/editorial re-review reasons commonly included insufficient methods elaboration, poor/unscientific writing, weak rationale, discussion problems and design flaws.

A content analysis of 369 desk-rejected manuscripts at Academic Medicine found frequent editor comments about ineffective study questions/designs, data collection problems, weak discussion/conclusions, topic relevance, data analysis/results presentation and difficult-to-follow text.

These are single-journal/domain studies and cannot supply universal frequencies.

**Engineering consequence:** create explicit desk-rejection stress tests for target fit, rationale, design, methods/analysis, evidence presentation and readability.

Evidence: C.

Sources:

- Menon et al. 2022: <https://pmc.ncbi.nlm.nih.gov/articles/PMC9022928/>
- Meyer et al. 2018 / Academic Medicine: <https://pubmed.ncbi.nlm.nih.gov/28767495/>

### 5. Better statistical review can measurably improve manuscript quality

A randomized trial in biomedical publishing found that adding a statistical reviewer improved overall manuscript quality and specific items including quantitative methods, clear reporting, design, figures/tables and organization.

The trial measured manuscript quality, not a clean causal increase in acceptance probability.

**Engineering consequence:** for quantitatively central papers, a pre-submission statistical red team is a high-value quality intervention. Label its benefit as quality/error reduction unless acceptance is directly studied.

Evidence: A.

Sources:

- Cobo et al. 2007: <https://pmc.ncbi.nlm.nih.gov/articles/PMC1824709/>
- DOI: <https://doi.org/10.1371/journal.pone.0000332>

### 6. Reporting-guideline review may improve manuscript quality, but checklist completion is not a substitute for science

A masked randomized trial of additional guideline-based review found modest improvement in final manuscript quality, with more papers showing improvement from baseline in the intervention group; the effect was smaller than hypothesized and adherence to guideline-based suggestions was difficult.

**Engineering consequence:** resolve reporting standards early and use them as completeness/transparency controls, while keeping study validity and reporting compliance separate.

Evidence: A.

Source:

- Cobo et al., BMJ 2011: <https://www.bmj.com/content/343/bmj.d6783>

### 7. Reviewer disagreement is common; editors adjudicate rather than simply count votes

A 2026 manuscript-level study of 12,187 published and 3,819 rejected manuscripts at one journal found first-round reviewer discordance common in both groups. Discordance decreased substantially among ultimately published manuscripts but often persisted among rejected manuscripts. Majority reviewer recommendation aligned strongly, but not perfectly, with final editorial outcome.

**Engineering consequence:** do not optimize for unanimous reviewer enthusiasm. Track the strongest valid concern, the quality of the reasoning and whether the revision actually closes it.

Evidence: C (large one-journal longitudinal dataset).

Source:

- De las Cuevas 2026: <https://pmc.ncbi.nlm.nih.gov/articles/PMC13248283/>

### 8. Revision can substantially strengthen evidence; significance is harder to retrofit

An eLife analysis of 2,051 articles comparing first Reviewed Preprint and final Version of Record found strength-of-evidence terms improved in 43.8% of articles, remained the same in 53.7%, and decreased in 2.4%. Significance terms improved in 20.3% and remained unchanged in 76.1%. Most final versions followed one revision round, with fewer requiring two.

Because eLife's model is not a conventional post-review accept/reject model, this should not be interpreted as an acceptance-rate study.

**Engineering consequence:** revision is a strong opportunity to improve evidence and claims, but a low-fit/low-importance research question may not be repairable by endless post hoc experimentation.

Evidence: C / E (publisher analysis of a large internal cohort).

Source:

- eLife 2026 revision analysis: <https://elifesciences.org/inside-elife/e9d530fc/the-elife-model-comparing-elife-assessments-across-revisions>

### 9. Registered Reports can shift review to the design stage and decouple publication from result direction

Current Nature Human Behaviour, Nature Ecology & Evolution, Nature Methods, Scientific Reports, Communications Medicine and many other venues offer Registered Reports in which Stage 1 methods/analyses are peer reviewed before results are known and high-quality protocols may receive in-principle acceptance.

Scientific Reports explicitly states that final acceptance does not depend on the direction/significance of the results, provided the approved protocol is followed and the interpretation is defensible.

A matched evaluation of 29 Registered Reports and 57 comparison papers found Registered Reports numerically higher on all 19 quality criteria, with sizeable differences in methodological and analytical rigor and overall paper quality; novelty/creativity were not detectably reduced in that sample.

**Engineering consequence:** for eligible prospective work, the pipeline should check the Registered Report route before data collection rather than waiting until the final manuscript.

Evidence: D + B.

Sources:

- Nature Human Behaviour RR policy: <https://www.nature.com/nathumbehav/submission-guidelines/registeredreports>
- Scientific Reports RR policy: <https://www.nature.com/srep/journal-policies/registered-reports>
- Nature Ecology & Evolution RR policy: <https://www.nature.com/natecolevol/submission-guidelines/registeredreports>
- Nature Methods RR policy: <https://www.nature.com/nmeth/submission-guidelines/registered-reports>
- Chambers et al. quality comparison: <https://www.nature.com/articles/s41562-021-01142-4>

Transfer limit: Registered Reports are not offered equally across fields and are unsuitable for studies where relevant data/results have already been accessed beyond the target's Stage 1 rules.

### 10. Cover letters should support fit/routing, not rescue the manuscript

Current Elsevier guidance recommends a short cover letter that states the study aim/main findings, fit with the journal's scope, novelty and broader implications, while deferring to exact journal-specific requirements.

Nature-family editorial guidance similarly treats the cover letter as contextual support; the manuscript still carries the scientific case.

There is weak evidence that a particular cover-letter style causally increases journal acceptance.

**Engineering consequence:** use cover letters as concise evidence-bound routing briefs. Grade as D/E, not A/B acceptance evidence.

Evidence: D/E.

Sources:

- Elsevier Support Center, updated 2026: <https://www.elsevier.support/publishing/answer/what-should-be-included-in-a-cover-letter>
- Nature Geoscience editor guidance: <https://www.nature.com/articles/s41561-021-00824-y>

### 11. Author-suggested reviewers can be more favorable, which is a reason for anti-gaming safeguards

A multi-journal JAMA study found author-suggested reviewers were more favorable than editor-suggested reviewers when recommendations disagreed, but final editorial decisions were evenly aligned between the more favorable author-suggested and less favorable editor-suggested reviewer preferences in the discordant cases.

**Engineering consequence:** if a journal permits reviewer suggestions, use independent expertise coverage and conflicts only. Do not exploit expected favorability.

Evidence: B/C historical multi-journal study; anti-gaming only.

Source:

- Schroter et al. / JAMA: <https://jamanetwork.com/journals/jama/fullarticle/202193>

### 12. Public review histories are valuable but selected

Nature Communications states that original research papers submitted from 1 November 2022 and accepted for publication have public peer-review files with reviewer comments to authors and author rebuttal letters. It also explicitly warns that internal editorial discussions, decision letters and confidential comments are not fully represented.

PLOS can publish decision letters, reviewer reports, author responses and attachments for opted-in accepted manuscripts.

eLife exposes public reviews, assessments, responses and version histories.

TMLR uses an open-review discussion process; non-desk-rejected submissions are public, but desk-rejected submissions are not.

**Engineering consequence:** build a concern-to-repair corpus from these sources, but mark it Grade H and pair accepted cases with rejection-report evidence.

Evidence: D/H.

Sources:

- Nature Communications transparent peer review: <https://www.nature.com/ncomms/submit/tpr-faq>
- Nature Communications editorial process: <https://www.nature.com/ncomms/submit/editorial-process>
- PLOS ONE editorial/peer-review process: <https://journals.plos.org/plosone/s/editorial-and-peer-review-process>
- TMLR editorial policies: <https://www.jmlr.org/tmlr/editorial-policies.html>
- TMLR reviewer guide: <https://www.jmlr.org/tmlr/reviewer-guide.html>

### 13. Claim narrowing is a legitimate publication repair

TMLR's current acceptance criteria explicitly state that gaps between claims and evidence can be repaired either by providing more evidence or by reducing claims.

Nature Communications reviewer guidance similarly asks reviewers to assess whether data support the main conclusions rather than merely listing experiments that expand scope.

**Engineering consequence:** the package must compare `new evidence` versus `claim narrowing/removal` rather than reflexively recommending more experiments.

Evidence: D.

Sources:

- TMLR acceptance criteria: <https://jmlr.org/tmlr/acceptance-criteria.html>
- Nature Communications reviewer guidance: <https://www.nature.com/articles/ncomms13625>

### 14. Clear writing can be a publication criterion, but "humanization" is not acceptance evidence

PLOS ONE explicitly requires intelligible presentation and standard English and states that manuscripts may be rejected if language is difficult to understand or contains many errors.

Rejection content analyses also repeatedly identify difficult/poor writing as a failure class.

This supports clarity, logical flow, explanation depth and copy-editing. It does not support AI-detector evasion, random stylistic variation, or cosmetic "humanization" tricks.

**Engineering consequence:** natural scholarly prose remains a reader-facing quality layer; acceptance optimization must not become detector optimization.

Evidence: D + C.

Sources:

- PLOS ONE criteria: <https://journals.plos.org/plosone/s/criteria-for-publication>
- Menon et al. 2022: <https://pmc.ncbi.nlm.nih.gov/articles/PMC9022928/>

## Public review-history seed cases for future corpus work

These are examples of available public histories, not acceptance exemplars or universal templates.

### eLife 2026

- Tool/method: *A tool to pulse-label yeast nuclear pore complexes in imaging and biochemical experiments* — public reviews + response + versions: <https://elifesciences.org/articles/108399/peer-reviews>
- Quantitative imaging method: *A quantitative pipeline for whole-mount deep imaging and analysis of multi-layered organoids across scales*: <https://elifesciences.org/articles/107154/peer-reviews>
- Cognitive/behavioral: *Effort produces after-effects costly for others but valued for self*: <https://elifesciences.org/articles/103566/peer-reviews>
- Theory/learning: *Information, certainty, and learning*: <https://elifesciences.org/articles/102155/peer-reviews>
- Computational biology/ML: *Separating selection from mutation in antibody language models*: <https://elifesciences.org/articles/109644/peer-reviews>
- Mechanistic biology: *A conserved mycobacterial nucleomodulin hijacks the host COMPASS complex...*: <https://elifesciences.org/articles/107677/peer-reviews>

### PLOS ONE 2026

- Systematic review/meta-analysis: <https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0354619>
- Cross-sectional epidemiology: <https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0355164>
- Visualization/meta-research: <https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0336917>

### Nature Communications 2026

Accepted primary-research pages expose downloadable transparent peer-review files, for example:

- *Cryoelastic and cryochromic organic crystals*: <https://www.nature.com/articles/s41467-026-73539-6>
- *scE2TM improves single-cell embedding interpretability and reveals cellular perturbation signatures*: <https://www.nature.com/articles/s41467-026-76825-5>

For systematic corpus extraction, use the peer-review files as accepted-case evidence and explicitly record that Nature Communications does not publish all internal decision information.

## What this evidence does **not** justify

Do not infer:

- a universal acceptance percentage for a manuscript;
- that one stylistic change causes acceptance;
- that more experiments always improve acceptance;
- that public editors can be ranked by leniency;
- that likely reviewers should be strategically cited;
- that a prestigious-journal convention is scientifically optimal;
- that accepted public review histories reveal why rejected manuscripts failed;
- that a checklist score is a causal acceptance score;
- that post hoc significance can rescue weak design.

## Current implementation priorities derived from the evidence

1. Add evidence grades to acceptance advice.
2. Start optimization before the study when possible.
3. Check Registered Report eligibility for prospective hypothesis-driven work.
4. Require claim-backward design and outcome-neutral quality controls.
5. Add pre-submission domain/method/statistical red teams.
6. Maintain a fit-first target ladder rather than prestige-only ordering.
7. Run independent multi-editor desk simulations.
8. Pair accepted public review histories with rejection-report evidence.
9. Track concern-to-repair closure across revision rounds.
10. Keep uncontrollable editorial context separate from repairable manuscript state.
11. Never output acceptance probabilities or editor/reviewer favorability scores.

## Update triggers

Re-review this ledger when:

- major venue decision criteria change;
- a journal changes Registered Report availability or Stage 1/Stage 2 rules;
- new large-scale manuscript-level acceptance/rejection datasets appear;
- new randomized trials of editorial/peer-review interventions appear;
- transparent peer-review availability materially expands;
- the package promotes a Grade H heuristic into a hard reusable rule.
