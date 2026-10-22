# Review cases: mathematical exposition in empirical trading research

Use alongside the empirical trading paper adapter and formal-spine contract. These synthetic cases check writing behavior, not investment validity.

| Input situation | Required behavior | Failure to reject |
|---|---|---|
| Reader has a mathematics PhD but no trading background | Explain instruments, timing, notional and funding; retain equations and derivations | Equating lack of domain knowledge with lack of mathematical skill |
| Source says a 72-bar hold retains targets at panel rows divisible by 72 | Define scheduled phase and distinguish weights from quantities | Describing a new 72-bar cohort opened at every bar |
| Two rank operations use different masks | State each ranking universe and operation order | Applying the final mask retroactively to both ranks |
| 240 catalogue entries but only 12 family templates inspected | Report both counts and preserve exact-formula gaps | Claiming all 240 strategies are mathematically reproduced |
| Three cash contributions sum to 4.1, reported net is 4.0 | Show a −0.1 reconciliation residual as unresolved | Inventing an unrecorded fee to force agreement |
| Code uses sqrt(sum((weight × sigma)^2)) | Call it a diagonal volatility proxy and identify omitted covariance | Calling it exact portfolio volatility without an assumption |
| Claimed safe leverage is (1−m)/a; model loss is La and maintenance Lm | Derive conditional requirement L < 1/(a+m), identify difference | Repeating a universal safety guarantee from a docstring |
| A confidence routine clips losses and caps its radius | State the changed estimand and missing coverage assumptions | Calling its output a valid time-uniform confidence bound solely from its name |
| Only closed-episode cash records are available | Show complete outcome distribution plus cash components | Fabricating an intratrade price or equity trajectory |
| Mathematical HTML intended for offline reading | Render equations and bundle required fonts; inspect layout | Replacing equations with bold text or relying on missing network fonts |

A successful revision should show its formal-source map and reader-facing output, identify unresolved warrants, and avoid importing private study values into a public reusable skill package.
