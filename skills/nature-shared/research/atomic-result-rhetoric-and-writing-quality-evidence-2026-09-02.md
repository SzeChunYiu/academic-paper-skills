# Atomic result rhetoric and scientific-writing quality evidence — 2026-09-02

**Purpose:** evidence ledger for the fine-grained `scientific-rhetorical-act-and-result-state.md` contract.

This note asks two related questions:

1. How should distinct scientific evidence states—directional findings, ordinary non-significance, evidence of absence, equivalence, non-inferiority, harm, heterogeneity, failed hypotheses, controls, robustness, exploratory results and contradictions—be written differently?
2. What recurring properties distinguish a well-written scientific article from a grammatically polished but scientifically poor one?

The evidence is deliberately separated into:

- methodological/reporting standards;
- meta-research on spin and selective reporting;
- editorial/scientific-writing guidance;
- deep reading of real research papers that contain mixed positive, null, adverse or boundary findings.

Published-paper frequency is descriptive evidence, not proof that a writing choice is optimal or causal for publication.

---

## 1. Methodological and reporting evidence

### 1.1 CONSORT 2025 — effect estimate and uncertainty, not P-value-only reporting

**Source**

Hopewell S, Chan A, Collins GS, et al. `CONSORT 2025 explanation and elaboration: updated guideline for reporting randomised trials.` BMJ 2025;389:e081124.

https://www.bmj.com/content/389/bmj-2024-081124

**Support**

- Trial reports should identify the treatment-effect measure and accompany the estimate with a confidence interval.
- Results should not be reported solely as P values.
- Confidence intervals are especially informative for non-significant findings because they show whether clinically important effects remain compatible with the data.
- Authors should avoid interpreting a non-significant superiority result as equivalence.
- Prespecified and post hoc analyses should be distinguished.
- Multiplicity makes chance significant findings more likely and therefore changes the interpretation of secondary/subgroup findings.

**Engineering consequence**

Result rhetoric must be driven by effect/uncertainty/decision class and study role, not threshold crossing alone.

**Transfer limit**

CONSORT is a randomized-trial reporting standard. The statistical principles about effect estimates, uncertainty and the non-equivalence of `P > alpha` and absence transfer broadly; exact reporting items do not.

### 1.2 Nature Human Behaviour — ordinary null versus evidence of absence

**Sources**

`Points of significance.` Nature Human Behaviour (2023).
https://www.nature.com/articles/s41562-023-01586-w

`Up close and personal.` Nature Human Behaviour (2023).
https://www.nature.com/articles/s41562-023-01753-z

**Support**

- Statements such as `there is no association` or `X has no effect on Y` are not warranted merely by failure to reject a null hypothesis.
- Main null results should use methods capable of interpreting absence when an absence claim is made, for example equivalence tests or Bayes factors.
- Power/sensitivity to theoretically or practically meaningful effect sizes matters to null interpretation.

**Engineering consequence**

The writing system must distinguish:

```text
ordinary non-significance
from
inconclusive imprecision
from
evidence of absence
from
equivalence.
```

### 1.3 Communications Psychology 2025 — reporting null and equivalence findings

**Source**

`Improving statistical reporting in psychology.` Communications Psychology (2025).
https://www.nature.com/articles/s44271-025-00356-w

**Support**

- Descriptive statistics, effect sizes and analytical decisions should be reported transparently even for exploratory analyses.
- Exploratory/non-confirmatory status should be visible.
- Equivalence margins should be justified and the interval/test interpreted relative to those margins.
- Post hoc equivalence tests require explicit disclosure and caution because margin selection after seeing results weakens inference.

**Engineering consequence**

The rhetorical state record needs prespecification/analysis-role fields and a distinct equivalence state.

### 1.4 CONSORT Harms 2022 — harms and zero events are first-class results

**Source**

Junqueira DR, Zorzela L, Golder S, et al. `CONSORT Harms 2022 statement, explanation, and elaboration.` BMJ 2023;381:e073725.
https://www.bmj.com/content/381/bmj-2022-073725

**Support**

- Benefits and harms should both receive effect estimates and uncertainty when appropriate.
- Zero-event harms should still be reported when prespecified/systematically assessed.
- `No events observed` must be distinguished from outcomes that were not investigated or not reported.
- Absolute and relative effect information can both matter.

**Engineering consequence**

Adverse/harm states cannot be optional or rhetorically minimized because they are inconvenient to the main positive story.

### 1.5 Subgroup and heterogeneity interpretation

**Source**

SPIRIT 2025 explanation and elaboration, BMJ 2025.
https://www.bmj.com/content/389/bmj-2024-081660

**Support**

- Differences between subgroups should be assessed through interactions or another appropriate heterogeneity comparison.
- `significant in subgroup A` and `not significant in subgroup B` does not establish that the subgroups differ.
- Post hoc subgroup analyses have high risk of spurious findings and should be identified as such.

**Engineering consequence**

The writing taxonomy needs a heterogeneity/interaction state distinct from two independent subgroup result sentences.

### 1.6 Non-inferiority/equivalence reporting

**Source**

EQUATOR Network, `Reporting of noninferiority and equivalence randomized trials: extension of the CONSORT statement.`
https://www.equator-network.org/reporting-guidelines/consort-non-inferiority/

**Support**

Non-inferiority/equivalence claims require explicit margins, effect scales, compatible confidence bounds and a design/analysis aligned to that objective.

**Engineering consequence**

Do not collapse non-inferiority, equivalence and ordinary non-significance into one `no difference` wording rule.

---

## 2. Meta-research on spin and selective rhetoric

### 2.1 Systematic review of spin

**Source**

Chiu K, Grundy Q, Bero L. `Spin in published biomedical literature: a methodological systematic review.` PLOS Biology 2017;15:e2002173.
https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2002173

**Support**

Spin frequently appears in conclusions of studies with non-significant/inconclusive results. High-level spin includes failure to acknowledge the non-significant primary outcome, unwarranted certainty, and practice recommendations unsupported by the primary evidence.

**Engineering consequence**

The system should audit abstract/conclusion rhetoric against primary-result state, not only Results wording.

### 2.2 Spin strategies in trials

**Sources**

`The SSSPIN study—spin in studies of spin.` BMJ 2019;367:l6202.
https://www.bmj.com/content/367/bmj.l6202

`Spin in the neurosurgical trauma literature: prevalence and associated factors – protocol.` BMJ Open 2022.
https://bmjopen.bmj.com/content/12/1/e046602

**Support**

Recurring spin strategies include:

- reporting non-significant results as a `trend`;
- emphasizing significant secondary/subgroup/within-group findings when the primary outcome is non-significant;
- interpreting non-significant superiority findings as comparable effectiveness/equivalence;
- making favorable recommendations despite unsupported primary evidence;
- causal wording unsupported by study design;
- over-extrapolating beyond the observed population/design.

**Engineering consequence**

These patterns become explicit anti-spin checks in the atomic result contract.

### 2.3 Spin can propagate from abstracts and visual summaries

**Sources**

`Spin in media coverage of research can be traced to abstracts.` BMJ 2012;345:e6106.

Zadro JR et al. `Do infographics ‘spin’ the findings of health and medical research?` BMJ Evidence-Based Medicine 2025;30:84.
https://ebm.bmj.com/content/30/2/84

**Support**

- Favorable emphasis in abstracts can influence downstream communication.
- Spin also occurs in visual summaries/infographics, including focusing on positive secondary outcomes or favorable interpretations despite non-significant primary outcomes.

**Engineering consequence**

Result-state consistency must be checked across abstract, prose, tables, figures/infographics and conclusions.

---

## 3. Editorial evidence on well-written versus poorly written papers

### 3.1 Nature Computational Science — logical research narrative

**Source**

`On writing accessible computational science papers.` Nature Computational Science 2025;5:515.
https://www.nature.com/articles/s43588-025-00847-0

**Support**

- Introduction should balance relevant context and technical detail and end with a concise preview of approach/findings/implications.
- Results should follow a logical research narrative rather than experiment chronology.
- Benchmark comparator choices should be justified.
- Main text should prioritize important evidence; exhaustive technical detail belongs in Methods/support when appropriate.
- Discussion should address implications, limitations and remaining challenges rather than merely summarize.

**Engineering consequence**

Writing quality is partly dependency architecture and allocation, not sentence fluency.

### 3.2 Nature Computational Science 2026 — common reviewer complaints

**Source**

`What reviewers request the most.` Nature Computational Science 2026;6:317.
https://www.nature.com/articles/s43588-026-00989-9

**Support**

Common reviewer concerns include:

- missing/inadequate comparisons and validation;
- weak context;
- unclear practical usefulness;
- missing methodological details;
- selective reporting;
- missing statistical tests;
- insufficient limitations;
- unclear figures;
- poor manuscript organization/discussion flow;
- unclear or overstated claims.

**Engineering consequence**

`Well-written` should be audited across evidence completeness, interpretation and organization—not judged as prose aesthetics alone.

### 3.3 Nature Cancer — data-led narrative rather than chronology or preferred story

**Source**

`The craft (and art) of scientific writing.` Nature Cancer 2023;4:583–584.
https://www.nature.com/articles/s43018-023-00579-y

**Support**

- Identify key scientific messages by considering the data in toto.
- Guard against building a story around preferred but unvalidated hypotheses.
- A paper need not be dry or chronological; identify the narrative thread connecting decisive data.
- Results should complement figures rather than become a laundry list.
- Introduction should selectively synthesize relevant literature, including conflicts/controversies.
- Discussion should put findings in perspective and avoid hype.

**Engineering consequence**

The result-act layer must support both narrative coherence and hostile evidence fidelity.

### 3.4 Reader expectation approach

**Source**

Gopen GD, Swan JA. `The Science of Scientific Writing.` American Scientist 78 (1990), 550–558. Reprint:
https://www.cs.tufts.edu/comp/105-2015s/readings/sci.html

**Support**

The purpose of scientific discourse is communication to readers, not merely encoding correct information in sentences. Reader expectations for structure/emphasis affect comprehension.

**Engineering consequence**

A scientifically valid sentence can still be poor writing if its message, relation or emphasis forces unnecessary reconstruction by the reader.

---

## 4. Deep reading: mixed positive, null and boundary results in real papers

These examples are used for rhetorical-function analysis, not phrase copying.

### 4.1 Positive local effect plus evidence of absent far transfer

**Paper**

`Cognitive control training with domain-general response inhibition does not change children’s brains or behavior.` Nature Neuroscience (2024).
https://www.nature.com/articles/s41593-024-01672-w

**Observed writing behavior**

- The paper reports a genuine positive result: targeted/near training measures improved and persisted.
- It separately reports broad failure of far-transfer behavioral/neural effects.
- The authors use Bayesian analyses to justify stronger evidence-of-absence statements for those far-transfer outcomes rather than inferring absence from non-significance alone.
- The Discussion uses successful near transfer/positive-control-like evidence to strengthen interpretation of absent far transfer.

**Generalizable lesson**

A paper can contain a positive mechanism-local result and a negative broader result without treating one as an embarrassment. Different evidence states receive different inferential language.

### 4.2 Apparent positive performance that collapses under confounding control

**Paper**

`Audio-based AI classifiers show no evidence of improved COVID-19 screening over simple symptoms checkers.` Nature Machine Intelligence (2024).
https://www.nature.com/articles/s42256-023-00773-8

**Observed writing behavior**

- Unadjusted AI performance is reported as strong rather than hidden.
- Matching on measured confounders sharply lowers the performance estimate.
- The paper uses this contrast as the scientific story: the `positive` benchmark result is reinterpreted as partly confounded rather than simply celebrated.
- Additional analyses inspect residual predictive variation and external replication.

**Generalizable lesson**

A well-written paper can present a positive numerical result and then explain why it is not the result the headline claim requires. Rhetorical salience follows scientific meaning, not metric magnitude.

### 4.3 Positive primary outcome plus null secondary outcomes

**Paper**

`Oral Semaglutide and Cardiovascular Outcomes in High-Risk Type 2 Diabetes.` New England Journal of Medicine (2025).
https://www.nejm.org/doi/10.1056/NEJMoa2501006

**Observed writing behavior**

- Primary outcome is given with event counts, hazard ratio, confidence interval and P value.
- Confirmatory secondary outcomes are explicitly stated as not significantly different rather than omitted.
- Serious adverse-event incidence is reported alongside benefit.

**Generalizable lesson**

A favorable primary result does not justify deleting null secondary results or harms. Role hierarchy and evidence symmetry remain visible.

### 4.4 Null primary outcome and hierarchy-aware secondary reporting

**Paper**

`Tenecteplase for Stroke at 4.5 to 24 Hours with Perfusion-Imaging Selection.` New England Journal of Medicine (2024).
https://www.nejm.org/doi/full/10.1056/NEJMoa2310392

**Observed writing behavior**

- The primary estimate and confidence interval are reported directly.
- Because the primary efficacy comparison was not significant, formal hypothesis testing of secondary outcomes was not performed under the planned hierarchy.
- Secondary estimates are still reported descriptively rather than used to rescue the primary claim.

**Generalizable lesson**

A well-written article preserves inferential hierarchy even when secondary values look favorable.

### 4.5 Mixed positive and null effects across repeated studies

**Paper**

`Online searches to evaluate misinformation can increase its perceived veracity.` Nature (2023/2024 publication context).
https://www.nature.com/articles/s41586-023-06883-y

**Observed writing behavior**

- The paper reports significant positive effects in some studies and a non-significant effect in another.
- The null case is not silently dropped; the authors report the estimate and test, and use a Bayesian analysis in that study to characterize support for the null.
- The narrative is organized around what the series of studies establishes and where results differ.

**Generalizable lesson**

Multi-study papers should expose study-to-study differences rather than smooth them into a single monotone story.

### 4.6 Negative regulator / control-rich mechanistic Results

**Paper**

`Paraspeckle condensation is controlled via TDP-43 polymerization and linked to neuroprotection.` Nature Cell Biology (2026).
https://www.nature.com/articles/s41556-026-01895-y

**Observed writing behavior**

- Results open with a direct mechanistic claim (`negative regulator`) and immediately provide the observation that motivated it.
- Multiple comparator proteins and tag/construct controls are reported to narrow alternative explanations.
- Quantitative effect size/context is included where it matters.
- Controls are not merely listed; each supports a specific inference about specificity/artifact.

**Generalizable lesson**

Good mechanistic writing gives controls rhetorical jobs. A long control list without a stated alternative being addressed is weaker.

### 4.7 Global experiment with both polarization effects and no evidence of behavioral difference

**Paper**

`The differential impact of climate interventions along the political divide in 60 countries.` Nature Communications (2024).
https://www.nature.com/articles/s41467-024-48112-8

**Observed writing behavior**

- Abstract juxtaposes positive ideological differences in beliefs/policy support with no statistically significant difference in a behavioral tree-planting task.
- The authors then make the mismatch itself the scientific object (`conceptual-behavioral` incongruence) rather than treating the null behavior result as failed filler.

**Generalizable lesson**

A null result can be central when it creates a scientifically meaningful contrast with positive results on related outcomes.

---

## 5. Result-state distinctions supported by this tranche

### 5.1 Non-significant is not absence

Supported by CONSORT, Nature Human Behaviour and Communications Psychology.

### 5.2 Absence claims require a meaningful effect region or absence-capable method

Supported by Nature Human Behaviour and equivalence/Bayesian guidance.

### 5.3 Equivalence and non-inferiority are positive inferential decisions, not failed superiority tests

Supported by CONSORT/EQUATOR.

### 5.4 Failed prespecified hypothesis does not prove its strongest alternative

Inference from the distinction between hypothesis testing and alternative explanation; reinforced by null-result guidance and real-paper examples.

### 5.5 Heterogeneity is an interaction question

Supported by SPIRIT 2025.

### 5.6 Harms and zero events are scientific results

Supported by CONSORT Harms 2022.

### 5.7 Exploratory status is part of the result's meaning

Supported by CONSORT 2025 and Communications Psychology 2025.

### 5.8 Positive and negative evidence must remain symmetric in reporting role

Supported by spin literature, CONSORT and deep-paper examples.

### 5.9 Sensitivity analyses are meaningful only relative to a stable scientific target

Supported by the repository's statistical-inference contract and by the broader reporting principle that analytical decisions and deviations must be transparent.

### 5.10 A null/negative result can be the narrative hinge

Supported by the climate-intervention paper, cognitive-control paper and audio-AI paper.

---

## 6. Operational model of well-written versus poorly written science

The evidence supports treating quality as a multidimensional property rather than a style score.

A strong paper aligns:

```text
truth / evidence state
x argument architecture
x reader-state activation
x uncertainty
x reporting completeness
x section/rhetorical register
x element economy
x displays
x literature relation
x authorial judgment
```

### High-value characteristics

- central question and scientific target are recoverable;
- every decisive result states magnitude/uncertainty appropriate to the design;
- inferential states remain distinct;
- positive, null, adverse and contradictory evidence is not selectively weighted by desirability;
- experiment order follows scientific dependency rather than lab chronology;
- reader prerequisites precede use;
- figures/tables and prose divide labor intelligently;
- Discussion interprets rather than repeats;
- limitations are connected to the claims they weaken;
- prior work is synthesized, including conflicts;
- abstract/title/conclusion do not become more favorable than the body;
- detail is allocated by scientific value under venue constraints.

### Recurrent poor-writing signatures

- P-value threshold becomes the message;
- `no effect` from ordinary non-significance;
- `trend toward significance`;
- secondary-outcome rescue;
- post hoc result written as predicted;
- subgroup difference inferred from separate significance tests;
- harms/negative controls/failures omitted or buried;
- data dump with no message hierarchy;
- Results chronology without scientific dependency;
- Discussion as Results recap or caveat list;
- undefined terminology appearing in tables/results;
- decorative equations or figures;
- citation wallpaper;
- abstract optimism drift;
- generic AI cadence where evidence states with different epistemic status receive the same sentence template.

---

## 7. Transfer limits

1. Clinical reporting standards are not universal manuscript templates.
2. Bayesian/equivalence methods are examples of absence-capable inference, not mandatory methods for every field.
3. `No evidence` language can itself be too weak if the study genuinely supports equivalence/absence at a meaningful scale.
4. `Evidence of absence` should remain bounded to the effect region, population, design and assumptions actually tested.
5. Real papers are calibration examples, not phrase banks.
6. Publication in a top journal does not make every sentence/style choice optimal.
7. Statistical correctness does not by itself make prose readable; reader architecture still matters.
8. Reader-friendly writing must not erase study-design/reporting detail required for transparency.
9. Negative findings should not be fetishized as virtuous; their manuscript prominence depends on scientific consequence.
10. No writing-quality score can certify a paper as scientifically excellent.

---

## 8. Engineering consequences

This tranche supports:

- `scientific-rhetorical-act-and-result-state.md`;
- a machine-readable result-rhetorical-act record for claim-bearing evidence states;
- explicit anti-spin semantic checks;
- correction of existing examples that over-infer from failed hypotheses/non-significance;
- a reviewer gate for abstract/title/conclusion optimism drift;
- result-state routing layered beneath section register;
- paragraph-level writing audits that ask both `what is this paragraph doing?` and `what evidence state is being communicated?`;
- no universal `positive/negative/null` sentence templates.

Operating synthesis:

> **Good scientific writing preserves the structure of the evidence while reducing the reader's reconstruction burden. Poor scientific writing either distorts that structure or makes the reader reconstruct it unaided.**
