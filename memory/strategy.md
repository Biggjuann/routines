# Bull Trading Strategy

_Last updated: 2026-09-11 (W18 close — Rule A regime-status marker + Rule E formalization following W15 6-week-evaluation-window close and W18 AMZN §8.4 first empirical trigger test)_

## Core Philosophy

Fundamentals-driven swing trading. We are NOT day traders. We are long-term thinkers making medium-term bets (hold period: 2–8 weeks per position). The edge is doing better research than the average retail investor and maintaining iron discipline on risk management.

## Primary Strategy: Earnings Momentum + Sector Rotation

### Step 1 — Macro Context (Pre-market, weekly)
- What is the Fed doing? (rate environment)
- Which sectors are showing institutional inflows? (check XLK, XLF, XLE, XLV, XLY ETF flows)
- What is the VIX saying? (>25 = reduce risk, <15 = can be more aggressive)
- S&P 500 trend: above or below 50-day and 200-day SMA?

### Step 2 — Stock Screening Criteria
Must meet at least 4 of 5:
1. Revenue growth YoY > 10%
2. EPS growth YoY > 15% OR positive earnings surprise last quarter
3. Analyst consensus: Buy or Strong Buy (majority)
4. Institutional ownership increasing (13F signals)
5. Sector ETF is in uptrend (above 50-day SMA)

### Step 3 — Entry Timing
- Enter in the first 30 minutes of market open or after 11 AM (avoid open volatility)
- Prefer limit orders, not market orders
- Never chase a stock that has already moved >3% on the day before entry

### Step 4 — Position Management
- Immediately after entry: set 10% trailing stop
- At +15% gain: sell half the position, move stop to break-even on remainder
- At +25% gain: full exit or hold with tight 5% trailing stop
- Cut losers at -7% without emotion

## Sector Watchlist (as of 2026)
- **Technology**: AI infrastructure, semiconductors, cloud
- **Healthcare**: biotech with near-term catalysts, medical devices
- **Energy**: traditional + clean energy depending on macro
- **Financials**: regional banks if rates are favorable
- **Consumer Discretionary**: discretionary spending signals

## Signals That Trigger a BUY Review
1. Earnings beat + raised guidance
2. Analyst upgrade from major firm
3. Sector ETF breaking out to new 52-week high
4. Insider buying cluster (3+ insiders buying in 30-day window)
5. Product launch or FDA approval catalyst

## Signals That Trigger a SELL Review
1. Earnings miss
2. Guidance cut
3. Sector ETF breaks below 50-day SMA
4. CEO or CFO departure
5. Multiple analyst downgrades in same week

## Risk Budget
- Max portfolio drawdown tolerance: -15% from peak
- Max single-position loss: -10% (hard stop)
- Target annual return: S&P + 5–10%
- Current mode: **PAPER TRADING** (switch to LIVE when comfortable)

## Rule Additions (W13 Close — 2026-08-07)

### Rule A — Mega-Cap-Ex-Semi 3-of-5 Hard-Mandatory Monday Pre-Market Screen
For any non-semiconductor mega-cap name with $500B+ market cap, execute a 3-of-5 light screen every Monday pre-market in parallel with (not replacing) the standard 4-of-5 formal screen:
1. Market cap ≥ $500B ✓
2. 50-day SMA above (name in confirmed uptrend) ✓
3. Last-earnings not-a-miss (Q print delivered above expectations on ≥ 2 metrics) ✓
If 3-of-5 PASSES, name is elevated to formal BUY-consideration at limit orders — subject to all other trading rules (5% position cap, 2-signal minimum for entry, 10% trailing stop set immediately post-fill, 20% sector cap, 10% cash reserve). Multi-overlay DEFER from other layers does NOT auto-lock the name at PASS if the 3-of-5 PASSES.
Rationale: W12 + W13 delivered +10.44% combined counterfactual miss on MSFT/AMZN/GOOGL/META/AAPL when the pre-existing default multi-overlay DEFER architecture kept all 5 names locked at PASS. Empirical evidence definitive for rule addition.

### Rule B — Insider-Veto Carry Expiry Protocol
Insider-sell carry-veto EXPIRES when BOTH:
(a) T-N-days since sell > 120 AND
(b) Stock has rallied ≥ 20% from the sell price.
On expiry, veto is reduced from "structural DEFER" to "monitoring watchlist" — the name becomes eligible for the 3-of-5 or 4-of-5 formal screen. New insider sells reset T-N clock.
Rationale: NVDA Stevens-885k T-120+ with NVDA up ~40%+ since sell; the market has fully priced-in the insider signal. Insider-veto retention on already-rallied names is a structural miss-driver.

### Rule C — Earnings-Blackout Tier T+3+ Expiration
Post-print earnings-blackout DEFER formally EXPIRES at T+3 sessions after print (T+0 = print day). On expiry, execute the appropriate formal screen (3-of-5 for mega-cap-ex-semi, 4-of-5 for other DEFER-list): if PASS, elevate to BUY-consideration; if FAIL, categorize as OBSERVATION-only. Blackout applies pre-print through T+2 inclusive.
Rationale: META/AAPL/LRCX all had T+3+ recovery bounces not captured in W13. The earnings-blackout tier previously lacked a formal expiration mechanism.

### Rule D — SMCI-Specific Momentum-Continuation Override
The chase-guard hard-DEFER on SMCI (triggered by any single-week +10%+ move) converts to a 48h observation window instead of permanent DEFER. If SMCI continues +5%+ on n=2 sessions during the 48h post-guard window, re-classify as MOMENTUM-VALIDATED and elevate to 3-of-5 light criteria. If no continuation, chase-guard converts to standard DEFER-list eligibility after 48h.
Rationale: n=4 SMCI observation dataset (W9 +8%, W11 +24%, W12 -5.68%, W13 +9.53%) = 3 momentum-continuation + 1 mean-reversion = base rate is momentum-continuation-dominant.

## Rule Additions (W18 Close — 2026-09-11)

### Rule E — §8.4 Middle-Band Review-Zone Conditional Q-Trigger (per-position, all open positions)
On any close, if a position's cushion above hard-cut (-10% stop) is **≤1.5pp AND >0.5pp** (middle band):
- ARM a conditional Perplexity Q for next session pre-market
- Q content: name-specific thesis-break check + macro-overlay read
- If next pre-market cushion re-expands ≥2.0pp: DE-ARM without Q spend
- If next pre-market cushion remains ≤1.5pp OR breaches ≤1.0pp: SPEND the Q and execute review at 09:30 ET open

On any close, if a position's cushion **≤0.5pp** (deep band):
- HARD-ARM stop-tighten to 5% trailing (from 8% or 10%); no Q required
- Escalate to defensive-trim conversation at midday if cushion does not re-expand ≥1.5pp intraday

Rationale: AMZN Thu 9/10 close cushion 1.30pp = first §8.4 trigger since the concept was instantiated in trade-log ad-hoc form; Fri 9/11 pre-market cushion recovery to 2.09pp cleared the re-arm zone and DE-ARMED cleanly without Q spend. The mechanism worked exactly as designed; formalization to strategy.md prevents ad-hoc drift and generalizes to future positions. This is a codification of proven empirical behavior, not a new discretionary rule.

## Regime-Contingent Rule Status Markers

### Rule A REGIME-STATUS (as of 2026-09-11, W18 close)
**SUSPENDED-BY-MACRO-GATE-1** since 2026-08-24 (W16 D1).
- **Cause**: 10Y > 4.70% every session W14-W18 (5 consecutive weeks). Rolling 0-of-15 formal PASS rate is the correct mechanical outcome under a rate-hostile regime, not a discipline failure.
- **Empirical validation basis**: W15 (+1.17pp positive alpha) and W18 (+0.705pp positive alpha) both delivered on down-tape weeks where Rule A held cash correctly; W16 (-0.27pp) and W17 (-0.39pp) up-tape drags were structural cash-drag math, not a Rule A miss on strong mega-cap-ex-semi rallies (neither week had one).
- **Auto-resume trigger**: Rule A automatically resumes weekly-Mon-pre-market screening on any single session's 10Y close ≤4.70%.
- **Next evaluation trigger**: no further 6-week-window formal evaluations while suspension persists; the next evaluation cycle begins on the first session of Rule A resumption + 6 weeks thereafter.
- **W15 pre-commit HONORED**: this suspension marker is formal execution of branch (b) — "accept the rule as designed and formally record that the mega-cap-ex-semi cohort is out of BUY-consideration during the current macro regime" — from the W15 close 6-week-evaluation-window pre-commit.

## Lessons Learned
- [2026-05-01] Initial setup. No trades placed yet. Starting fresh.
- [2026-08-07] W13 closes as first F-grade week in Bull history (-3.53% SPY-benchmark alpha; +3.53% SPY vs 0.00% cash-sleeve). Cumulative-from-inception drops to ~-4.49% midpoint = 4.5x deeper than any prior sub-band excursion. Recalibration criterion (b) triggers. Four rule additions above operationalize the remediation. BRANCH-a re-consideration mandatory at W14 close.
- [2026-09-11] W18 closes B-grade (+0.705pp positive alpha; first positive-alpha week since W15). Two formalizations: (a) Rule E — §8.4 middle-band review-zone conditional Q-trigger promoted from trade-log ad-hoc carry to strategy.md rule following AMZN Thu 9/10 → Fri 9/11 first empirical test cycle executed correctly (arm on trigger → observe cushion recovery → de-arm without Q spend or forced action); (b) Rule A REGIME-STATUS marker added following W15 6-week-evaluation-window close per pre-commit branch (b) — Rule A is regime-suspended under 10Y >4.70% conditions and auto-resumes on 10Y ≤4.70% close. Cumulative-from-inception alpha midpoint recovers to ~-3.75% (best since W15 close). Trailing-5-week cumulative alpha rebuilds to +0.75pp (from -0.15pp at W17 close). No BRANCH-a activation.
