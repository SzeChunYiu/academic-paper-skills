# Evidence ledger: excellent academic writing, AI-writing failure modes, and numerical precision

Date: 2026-08-31

## Research question

Which recurrent weaknesses in AI-assisted academic manuscripts are not solved by citation integrity, sentence-level cohesion, or surface cleanup alone, and what writing/review controls should the pipeline add?

## Expert lenses used

1. **Scientific editor / genre architect** — asks whether section order, evidence progression, discussion, comparison rationale, and contribution framing match how strong research papers communicate a scientific case.
2. **Academic-discourse / rhetoric researcher** — asks how reader expectations, stance, information flow, formulaicity, hedging, authorial presence, and paragraph choreography differ between strong human academic writing and common LLM output.
3. **Statistical reporting editor** — asks whether numerical precision, uncertainty, denominators, effect reporting, and cross-surface consistency are scientifically interpretable rather than formatter-driven.
4. **Zero-context technical reader** — asks whether a qualified reader who has never seen the repository/programme can reconstruct definitions, experiment roles, tables, and the evidence-to-conclusion chain in reading order.

These lenses are deliberately different: a manuscript can be accurate yet rhetorically weak; clear locally yet incoherent globally; transparent yet self-defeating; reproducible yet numerically overprecise.

## Triggering manuscript evidence

The recent skill-produced papers showed recurring failures:

- raw fixed-width numeric output such as `1.000000`, `0.510417`, `0.906250` and six-decimal confidence limits despite small finite samples;
- central project IDs and experimental families becoming active after first use;
- `Qwen` and other result-bearing entities appearing without an earlier narrative role;
- short setup/problem-formulation sections that technically introduce some symbols but do not discharge all prerequisites later Results depend on;
- Results organized around frozen campaign/version history rather than reader questions;
- Discussion/limitations sections dominated by lists of non-claims, audit status, and future gates rather than interpretation of the headline findings;
- repeated `does not establish`, `not evidence of`, `CannotCheck`, `retained terminal`, `donor`, `parent`, and related governance language;
- development chronology and verification virtue competing with the scientific story.

These failures motivated the distinction:

```text
verification quality != narrative quality != rhetorical quality
```

## Editorial and scientific-writing evidence

### Nature Computational Science (2025), “On writing accessible computational science papers”

DOI: 10.1038/s43588-025-00847-0

Key transferable points:

- Introduction should give relevant context, clear motivation, and a concise preview of approach, findings, and implications.
- Results should be organized in a **logical order supporting the research narrative**, not experiment chronology like a lab report.
- Only methodological detail needed to understand Results belongs there; deeper derivations/training/architecture detail belongs in Methods when it distracts.
- Benchmark comparisons should be justified, and practical meaning of performance should be explained.
- Discussion should address broader implications, limitations, remaining challenges, and future opportunities rather than merely summarize.

Transfer limit: editorial guidance for computational science is highly relevant to the triggering papers but is not a universal section template for every discipline.

### Nature Computational Science (2026), “What reviewers request the most”

DOI: 10.1038/s43588-026-00989-9

Editors group common reviewer requests into:

- comparisons and validation;
- context of the work;
- practical usefulness;
- overall clarity.

They specifically note missing/weak comparison rationale, incomplete context, insufficient discussion of limitations/usefulness, missing methodological details, unclear figures, organization/flow problems, and unclear or overstated claims.

This supports a macro-level reviewer gate rather than relying on sentence polishing.

### Nature Cancer (2023), “The craft (and art) of scientific writing”

DOI: 10.1038/s43018-023-00579-y

The Discussion should put findings in perspective, connect them to existing knowledge, highlight implications, outstanding questions, and future study, while remaining concise and avoiding hype.

### Nature Structural & Molecular Biology (2010), “Scientific writing 101”

DOI: 10.1038/nsmb0210-139

Useful transferable distinction:

- Introduction supplies only the background needed to understand how the question fills a gap.
- Results describe findings.
- Discussion interprets findings in broader context and explains conceptual advance rather than repeating Results.

### Gopen & Swan (1990), “The Science of Scientific Writing”, American Scientist 78, 550–558

Reader-expectation principles relevant to the pipeline:

- context should generally precede new information;
- topic positions help readers establish perspective and backward linkage;
- sentence stress should align with intended emphasis;
- complexity of thought does not require impenetrable expression.

This supports reader-state activation and dependency ordering. It is writing guidance, not a controlled universal law.

## Numerical reporting evidence

### Lang & Altman, SAMPL Guidelines, International Journal of Nursing Studies 52, 5–9 (2015)

DOI: 10.1016/j.ijnurstu.2014.09.006

The guidelines explicitly advise reporting numbers, especially measurements, with an **appropriate degree of precision** and rounding to a reasonable extent for comprehension.

They also emphasize sufficient detail for a knowledgeable reader to verify reported results.

Transfer limit: SAMPL is biomedical statistical-reporting guidance. The principle of appropriate precision transfers widely; specific decimal conventions do not.

## Research on AI-generated academic prose

### Lingua (2024), corpus-driven comparison of ChatGPT and human academic writing

DOI: 10.1016/j.lingua.2024.103838

Reported tendencies include:

- overuse of infrequent academic vocabulary and flowery language;
- only partial matching of human formulaic sequences;
- synonym substitution within recurring syntactic structures;
- differences in syntactic complexity.

This supports anti-formulaic and precision-over-ornament controls.

### Journal of English for Academic Purposes (2025), Mo & Crosthwaite

DOI: 10.1016/j.jeap.2025.101499

Comparative corpus work on stance/engagement found systematic differences between LLM and human academic writing and supports treating stance as a rhetorical resource that must be calibrated by function rather than generated uniformly.

Related research on GenAI revision of research writing reports a risk-averse tendency toward over-hedging and mechanically inserted stance markers.

### Ampersand (2025), engagement strategies in human vs AI academic essays

DOI: 10.1016/j.amper.2025.100237

The study reports weaker rhetorical complexity and different hedge/assertion/engagement behavior in AI-generated academic texts compared with human writing.

Transfer limit: essay corpora are not research articles. They provide plausible language/rhetoric failure hypotheses, not direct manuscript-quality laws.

### System (2025), human-written vs ChatGPT-generated research article abstracts

DOI: 10.1016/j.system.2025.103842

Large abstract corpora show measurable differences in stance use, reinforcing that apparently fluent academic text can still differ from human scholarly rhetorical practice.

## Current AI-publishing policy evidence

### Nature Computational Science (2026), “Responsible and transparent use of AI in scientific publishing”

DOI: 10.1038/s43588-026-01043-4

AI may support language, structure, formatting and translation, but scholarly judgment, responsibility and accountability remain human. The editorial explicitly warns that AI can generate inaccurate, misleading, or fabricated content.

### Nature Methods (2026), “Using AI responsibly in scientific publishing”

DOI: 10.1038/s41592-026-03020-1

Authors are advised not to take AI-generated text at face value and to carefully check and edit it for accuracy.

## Synthesis

The evidence supports five independent controls:

1. **macro argument architecture** — a paper must be one dependency graph, not a collection of polished modules;
2. **reader-state activation** — central terms/entities/experiments must be active before use, including tables and figures;
3. **section functional sufficiency** — short is acceptable only when all downstream prerequisites are discharged;
4. **discussion and epistemic rhetoric** — interpret findings and state bounded positive conclusions directly; do not substitute audit disclaimers for scholarship;
5. **numerical precision** — retain machine precision in artifacts but render only scientifically meaningful digits.

## What this research does not justify

It does **not** justify:

- one universal section structure;
- minimum word counts for Introduction/Problem formulation/Discussion;
- a fixed number of significant figures across disciplines;
- banning hedges, caveats, or negative results;
- hiding preregistered failures;
- copying Nature style into TMLR/ACL/physics/biomedicine;
- treating every linguistic difference between AI and humans as an error;
- optimizing to evade AI detectors.

The pipeline should learn function, dependency, precision and rhetorical calibration, then resolve exact local conventions from the target venue and close analogue papers.
