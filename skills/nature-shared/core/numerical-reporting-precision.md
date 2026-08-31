# Numerical reporting and precision contract

> Shared contract for reporting scientific numbers with enough precision to be accurate and reproducible without implying information the study does not contain.
>
> Preserve full computational precision internally. **Display precision is a scientific communication decision.**

## Core principle

More digits are not more rigorous.

A manuscript number should reflect:

```text
quantity type
× measurement / sampling resolution
× inferential uncertainty
× exactness status
× reader task
× target-venue convention
```

Do not print raw floating-point output merely because it exists.

## 1. Separate stored precision from displayed precision

Keep full machine precision in:

- analysis artifacts;
- source data;
- exact result files;
- reproducibility records;
- calculations used for thresholds or equality checks.

Render a scientifically justified rounded representation in:

- abstract;
- prose;
- tables;
- figures;
- legends.

The manuscript may include a more precise value when the extra digits affect a threshold, reproduce an exact test, distinguish near-equal methods, or are otherwise scientifically consequential.

## 2. Identify the numerical object first

Classify each reported number:

- exact count;
- exact fraction/rational quantity;
- deterministic benchmark score over a finite enumerated set;
- empirical proportion/rate;
- measured physical/biological quantity;
- model parameter/estimate;
- effect size;
- confidence/credible/prediction interval;
- P value;
- loss/error/metric;
- computational time/resource quantity;
- exact mathematical constant/bound;
- identifier/hash/version number.

Different classes need different precision logic.

## 3. Counts are exact; derived percentages are not infinitely precise

When `n/N` is informative, prefer reporting it.

Example:

```text
49/96 (51.0%)
```

is usually more informative than

```text
0.510417
```

for a finite empirical proportion.

For small/moderate denominators, six decimal places often imply a resolution the sample cannot support.

Use enough decimal places to communicate the comparison without disguising the discrete support.

## 4. Bounded metrics such as accuracy, F1, recall, error rate

For ordinary manuscript reporting, default to a compact precision such as:

- proportion scale: usually 2–3 decimal places;
- percentage scale: often 1 decimal place;

subject to field and venue norms.

These are **defaults, not universal rules**.

Use more digits when:

- very small differences are scientifically meaningful and uncertainty supports them;
- exact benchmark ranking depends on those digits;
- the target venue or benchmark convention requires them;
- a threshold comparison would change after coarser rounding.

Use fewer when:

- denominator is small;
- values are clearly separated;
- the extra digits do not change interpretation.

### Perfect scores

Do not routinely render a perfect finite-sample score as `1.000000`.

Prefer `1.00`, `1.0`, or `100%` according to local convention, and report the numerator/denominator when useful.

Reserve many trailing zeros for exact-computation contexts where fixed-width precision is itself meaningful.

## 5. Significant figures should reflect uncertainty and resolution

For measured or estimated quantities:

- avoid reporting more significant figures than measurement resolution or statistical uncertainty can justify;
- round estimate and uncertainty coherently;
- keep units and scale visible;
- do not preserve detector/software precision that exceeds scientific precision.

A useful default for many estimates is 2–3 meaningful significant figures, but exact field rules override this.

Do not apply a universal `three significant figures everywhere` rule.

## 6. Confidence and credible intervals

The point estimate and interval should use compatible precision.

Avoid patterns such as:

```text
estimate = 0.500000
95% CI = [0.414062, 0.585938]
```

unless those exact rational endpoints are scientifically necessary.

For ordinary interpretation, something like

```text
0.50 (95% CI 0.41–0.59)
```

may be more appropriate.

If exact bootstrap grid values or finite-enumeration endpoints are important for reproducibility, keep the exact values in supporting artifacts and render the reader-facing interval at justified precision.

## 7. P values

Follow the target venue/field when specified.

General principles:

- do not report `P = 0`;
- avoid meaningless long decimal strings;
- preserve enough precision to distinguish the inferential statement;
- very small values can be reported using scientific notation or a threshold such as `P < 0.001` when consistent with venue policy;
- do not let P-value precision imply effect-size precision.

Exact tests may legitimately yield exact rational/computational values; the manuscript can still round unless the exact number matters.

## 8. Exact mathematics and finite combinatorics are exceptions

An exact theorem, algebraic identity, rational bound, or finite enumeration may warrant exact representation.

Examples:

```text
25/41
27/36
1 - 1/4 = 3/4
```

If a decimal is added for reader convenience, label the exact object clearly and round the decimal sensibly.

Do not confuse exact computational output with exact scientific truth.

## 9. Threshold and decision-bound quantities

When a decision depends on a threshold, preserve enough digits to show the decision accurately.

Example:

If the prespecified margin is `0.05`, reporting an estimate as `0.05` when the unrounded value is `0.0496` may obscure which side of the threshold it lies on.

Use one of:

- additional justified digits;
- explicit unrounded decision statement;
- exact fraction/value in a note;
- confidence interval relative to the threshold.

Never let cosmetic rounding reverse or obscure a registered decision.

## 10. Cross-surface consistency

For the same result identity, use a declared rounding policy across:

- abstract;
- Results;
- table;
- figure labels;
- caption;
- Discussion;
- supplement.

Small differences caused only by independently rounding the same stored value are avoidable manuscript defects.

Record:

```text
stored value
render scale
rounding rule
rendered value
allowed tolerance
```

for headline results when useful.

## 11. Table precision

A table may use slightly more precision than prose when readers need exact comparison.

But each column should have a coherent precision rule.

Avoid tables where every metric is printed to six decimals by default because the software formatter used `%.6f`.

Ask:

- What difference could the reader meaningfully interpret?
- Is the denominator/sample size compatible with this resolution?
- Does uncertainty swamp the last displayed digits?
- Does fixed width improve comparison or merely expose machine formatting?

## 12. Figure precision

Axis ticks, data labels, annotations, and legends should not carry more digits than the visual can resolve.

A plotted point whose uncertainty bar spans 0.1 units rarely needs a label with six decimal places.

For logarithmic or very small quantities, scientific notation may be clearer than decimal padding.

## 13. Runtime and resource measurements

Do not report execution time such as `231.909885 seconds` in scientific prose unless sub-millisecond distinctions matter to the claim and measurement conditions justify them.

For ordinary runtime comparisons, round to a scale appropriate to variability and reader purpose.

Detailed exact logs stay in the artifact record.

## 14. Precision consistency with sample size

For a finite proportion with denominator `N`, the empirical grid spacing is `1/N`.

Use this as a diagnostic signal:

- if displayed decimal resolution is far finer than `1/N`, inspect whether the extra digits serve any scientific function;
- this is not a mandatory rounding formula because transformed metrics, averages across folds, weighting, and uncertainty can alter the relevant resolution.

## 15. Precision and uncertainty are different

Rounding does not replace uncertainty reporting.

`0.84` is not more honest than `0.836806` if the paper omits the sampling unit, interval, or replicate structure.

The correct sequence is:

```text
valid estimand / unit
-> valid uncertainty
-> scientifically justified display precision
```

## 16. Numeric readability audit

Flag passages where:

- many long decimals dominate the sentence;
- prose duplicates exact table values unnecessarily;
- exact values obscure the scientific comparison;
- readers must mentally subtract six-decimal numbers to discover the effect;
- ratios, counts, or percentages would communicate the result more directly.

Use tables for exact comparison and prose for the scientific pattern.

## 17. Automated review signals

Treat these as review triggers, not universal errors:

- ordinary bounded metrics with 5+ decimal places;
- repeated `1.000000`, `0.000000`, or other fixed six-decimal formatting;
- P values with excessive digits;
- runtime/resource numbers with implausible precision;
- inconsistent rounding of the same result across surfaces.

The contextual audit decides whether extra precision is scientifically necessary.

## 18. Release checklist

Before full-manuscript readiness:

- every headline numeric result has a clear quantity/scale/unit;
- counts/denominators are visible when needed;
- display precision is justified by resolution/uncertainty/decision use;
- exact mathematical quantities remain exact where appropriate;
- P values follow target/field conventions;
- tables and figures do not expose raw formatter precision by default;
- the same result is rounded consistently across surfaces;
- rounding does not alter a threshold-based conclusion;
- machine precision remains available in reproducibility artifacts when needed.

## Evidence basis and transfer limit

Statistical-reporting guidance such as SAMPL explicitly recommends reporting numbers with an appropriate degree of precision and rounding to a reasonable extent for comprehension. This principle transfers widely, but exact decimal/significant-figure conventions remain field- and venue-dependent.

Do not treat biomedical formatting examples as universal requirements for physics, mathematics, engineering, economics, or computer science.
