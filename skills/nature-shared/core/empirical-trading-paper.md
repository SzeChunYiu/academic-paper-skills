# Empirical trading papers: findings, worked episodes and economic displays

Use for empirical strategy/backtest papers, retrospective trading-research syntheses, and manuscript work that explains positive results through example trades. This is a domain reporting adapter, not investment advice, an execution engine, or a rule that other scientific papers must follow. Load alongside the existing standalone-reader, statistical-inference and display contracts.

## Lead with what the reader can learn

Define the instrument, long/short payoff, account equity, notional, funding, leverage, fills and drawdown before they carry an inference. Introduce a strategy by its observable decision rule, then its name. Organize Results by scientific question rather than development chronology.

For each positive finding connect: timely observation → proposed mechanism → action → observed outcome → matched comparator → uncertainty → failure boundary. A positive finding may concern prediction, accounting, execution, software correctness or learning; do not silently promote one into another. Keep payer hypotheses distinct from identified causal mechanisms. Keep engineered machinery distinct from learned behavior and matched-parent novelty.

Use a coverage projection over existing study identities and corrections. Account for positive, null, negative, superseded and unresolved variants. A positive historical cell is a candidate for explanation, not an independent validated finding. Keep the main narrative selective while making coverage and exclusions inspectable in supporting material. An incomplete inventory must not be called exhaustive.

## Preserve economic meaning

Report units, capital denominator, calendar convention, universe, dates, information timing, exposure, execution and funding completeness. Separate arithmetic simple returns, mean log returns and geometric growth; never rename their units for convenience. Separate per-notional, per-trade and full-account returns. Idle days belong in calendar-day rates. Bankruptcy is not a missing value to clip before taking logarithms.

Panel means are summaries of panels, not combined accounts. Show individual panels and their dependence/overlap; a duplicated gated panel is not independent replication. Combine strategies only through an identified shared-capital account treatment. Matched comparisons hold information, capital, risk and execution fixed for the axis being tested.

Place growth beside drawdown, tail losses, capacity and execution sensitivity. A positive average with negative component panels is heterogeneous evidence. Zero modeled breaches does not establish safety outside the model; finite stress tests are not universal mathematical guarantees. A reported confidence interval must target the same estimand as its headline and account for the actual dependence/selection structure. If unavailable, say so rather than inventing precision.

When arithmetic cash components fail to reconcile, preserve the original values and expose the residual. Determine whether it reflects aggregation, units, missing events or an error before claiming exact conservation. A self-consistent equation alone cannot prove event completeness.

## Worked trade contract

State the eligible set and an explicit selection rule before presenting examples. If selected after results, call the rule retrospective. A teaching set can use first chronological winner and loser plus a rejected/unfilled decision when logged. Show all outcomes or their distribution alongside the examples; do not let a winner represent expected performance.

Bind each episode to its contract, evidence tier (illustrative, modeled, prospective paper, authenticated execution, or external source report), decision-time information, timestamps, side, quantity, adds/partials, prices, exit reason, price P&L, both-leg fees, signed funding and net cash. Specify episode/order/fill denominators separately. Unknown fields stay unknown; do not infer a rejected order from absence of a fill or reconstruct intratrade prices from endpoints.

Give a readable cash walkthrough and interpret the result relative to account capital and the full outcome set. A source author's reported return is not the project's return. A modeled target touch is not a verified fill. Include a no-trade or failure case when it changes the mechanism or execution claim.

## Display selection

- Use signed contribution plots to distinguish funding, price, fees and net results with a common denominator.
- Use episode bars/tables when only episode records exist; use price/position/cash timelines only with adequate event records.
- Pair chronological equity with drawdown when a valid complete account series exists; retain idle days, split boundaries and losses.
- Show per-panel growth and risk, and execution/cost/capital stress outcomes, before a grand average. Do not fabricate confidence intervals from a handful of dependent panels.
- Keep inferential details in captions and artifact pins in the source map; use descriptive strategy names in manuscript surfaces.

For deterministic screening of normalized reported panel summaries, use
`../scripts/verify_trading_summary.py`. Its input is a JSON object with
`metric` (`simple_bp_day`, `log_bp_day`, or `geometric_bp_day`),
`aggregation` (`equal_panel_mean`), nonempty `panels` containing unique `id`,
`return`, and `max_drawdown_pct` in [0,100], `reported_mean`, and optional
boolean `claims_all_positive`. It checks this narrow arithmetic/reporting
contract only. It does not validate a backtest, uncertainty, causal claims,
trade selection, source authenticity, or native settlement. Do not coerce other
aggregation schemes to this format; use the appropriate existing statistical
contract and identify the actual account calculation.

## Completion and transfer

A useful draft can expose unresolved evidence while improving explanation. Publication readiness additionally needs full claim coverage, verified literature, source reconciliation, defensible uncertainty, visual review and the existing release gate. Do not require fresh market experiments merely to improve a draft; do not call a draft economically certified because its reporting checks pass.

This adapter generalizes reporting failures that can occur in archived strategy research. Its example checks are synthetic and contain no private project results. Methodological background: Bailey et al., The Probability of Backtest Overfitting, revised February 2015, https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf (selection-risk rationale; not a universal choice of correction or proof that any particular study is overfit).

## Mathematical audience and recursive explanation

Determine domain familiarity separately from mathematical proficiency. A reader can know calculus, probability and optimization while knowing nothing about perpetuals, funding or execution. Preserve the formal spine for that reader; do not replace defining equations with elementary prose because the reader was called a layperson. Load `formal-spine-preservation.md` when expanding formal depth.

Use the dependency order observations → operators → scores → targets → fills → cash → inference. For each defining equation explain the economic question, symbols and units, timing and index sets, assumptions and edge cases, then the observable implication. Expand unfamiliar operators until they reach the reader's stated prerequisites. Reuse linked definitions instead of recursively repeating elementary mathematics. Include an explicitly illustrative numerical calculation where it clarifies signs, units or capital denominators; never pass synthetic values off as an observed trade.

Distinguish (a) an identity or definition, (b) a conditional derivation, (c) an exact code transcription, (d) a descriptive-source rule, and (e) a family template or hypothesis. Record source pin, dependencies and unresolved details. Transcribing code does not prove that it generated an archived result. Generic family equations do not supply missing variant-specific rules. Preserve tie handling, missingness, warm-up, ranking universe, rebalance phase, lag, state-update chronology, clipping and fallback branches when they affect meaning.

For large strategy inventories separate family exposition, per-variant catalogue coverage and exact mathematical reproduction. Count each explicitly; do not call all variants reproduced when only family templates exist. Inherited verdicts remain attributed historical text, especially when they conflict or refer to an old live status. Keep family taxonomies distinct unless an explicit mapping exists.

A claimed theorem needs assumptions and a proof, not a suggestive class name or code comment. Check dimensional consistency and derive simple limiting cases. In particular, compare a risk cap with its stated maintenance and loss inequalities; test whether covariance terms are omitted; inspect clipped log returns, claimed increment bounds and capped confidence radii before accepting statistical guarantees. Preserve any contradiction as an open proof obligation rather than cosmetically rewriting it away.

## Mathematical and visual delivery

Render equations with a real math engine, with stable numbering, readable symbols and offline fonts where an offline artifact is promised. Keep source equations editable. Verify the rendered output, long-equation overflow, navigation, figure labels and any catalogue search/filter controls. Do not flatten formulas to bold plain text or substitute screenshots for accessible mathematical text.

Choose geometry by inferential task: waterfalls for cash reconciliation (unexplained residual separately labeled), paired points for matched stress changes, growth-versus-drawdown plots for joint risk interpretation, and full episode distributions beside a teaching pair's cash components. Inventory counts show reporting coverage, not independent trials or economic superiority. Do not connect incompatible windows as an account path, fabricate event trajectories, or use a decorative equity curve unsupported by records.

Review prompts for this adapter are in `empirical-trading-math-review.md`; they are behavioral checks, not certification of source truth.
