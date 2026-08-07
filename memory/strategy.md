# Bull Trading Strategy

_Last updated: 2026-08-07 (W13 close — first update since 2026-05-01 inception; four rule additions following F-grade week and recalibration criterion (b) trigger)_

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

## Lessons Learned
- [2026-05-01] Initial setup. No trades placed yet. Starting fresh.
- [2026-08-07] W13 closes as first F-grade week in Bull history (-3.53% SPY-benchmark alpha; +3.53% SPY vs 0.00% cash-sleeve). Cumulative-from-inception drops to ~-4.49% midpoint = 4.5x deeper than any prior sub-band excursion. Recalibration criterion (b) triggers. Four rule additions above operationalize the remediation. BRANCH-a re-consideration mandatory at W14 close.
