# Weekly Review Log

_End-of-week performance reviews. Every Friday at 4 PM._

## Review Template

```
## Week of [DATE]

### Performance
- Portfolio Value: $X,XXX.XX
- Week P&L: +/- $XXX.XX (X.XX%)
- S&P 500 Week Return: X.XX%
- Alpha Generated: X.XX%

### Trades Made This Week
- [List all trades]

### What Worked
- [Specific things that went well]

### What Didn't Work
- [Specific things that went wrong]

### Strategy Adjustments
- [Any rule changes or tweaks for next week]

### Next Week Focus
- [Sectors to watch, earnings to research, themes]

### Self-Grade: [A/B/C/D/F]
### Reasoning: [Why this grade]
```

---

## 2026-05-01 — Week 0 (Setup Week)

### Performance
- Portfolio Value: $10,000.00
- Week P&L: $0.00 (0.00%) — no trades
- S&P 500 Week Return: TBD
- Alpha Generated: 0.00%

### Notes
Agent initialized this week. No trades placed. Research pipeline being established. First real trading week begins next week.

### Self-Grade: N/A
### Reasoning: Setup week only.

---

## Week of 2026-05-01 (Friday Review — Init Day Review)

### Performance
- Portfolio Value (Alpaca actual): $100,000.00
- Portfolio Value (per memory): $10,000.00 → **discrepancy flagged below**
- Week P&L: $0.00 (0.00%) — zero trades placed
- S&P 500 (SPY) Week Return: ~+1.1% (Apr 27 – May 1, 2026; price return)
- **Alpha Generated: -1.10%** (100% cash during a positive SPY week)

### Trades Made This Week
- None. Agent was initialized today (2026-05-01); no pre-market or market-open routines have run yet.

### Market Context (Perplexity research)
- **SPY week**: ~+1.1%, driven by month-end rebalancing flows, technical bounce off declining-channel lower bound, and seasonal April strength.
- **Sector leaders (YTD 2026)**: Energy +22%+, Industrials +16%+, Consumer Staples +13%.
- **Sector laggards (YTD 2026)**: Information Technology — significant rotation out of tech.
- **Themes**: Geopolitical (Iran headlines) drove intraweek volatility but did not derail the rally.

### What Worked
- Capital preservation: by being uninvested, no risk rule was breached and no capital lost.
- Memory architecture loaded cleanly; the READ → DO → WRITE flow executed.
- After fixing infra bugs (see below), the full data pipeline (Alpaca, Perplexity, ClickUp) is verified end-to-end.

### What Didn't Work
- **Four infra bugs blocked the routine on first execution and had to be fixed mid-session:**
  1. `ALPACA_BASE_URL` env var contained a trailing `/v2`, while `alpaca_client.py` and `portfolio_snapshot.py` also prepend `/v2`, producing 404s. Patched both scripts to strip a trailing `/v2` from the env var.
  2. `perplexity_research.py` referenced a deprecated model (`llama-3.1-sonar-large-128k-online`). Updated to `sonar`. All future routines depend on this fix.
  3. Capital-base mismatch: `portfolio.md` says starting equity is $10,000 but the live Alpaca paper account is $100,000. The snapshot script hard-coded $10,000 in its return-vs-start calculation. Patched to use `BULL_STARTING_VALUE` env var (default $100,000).
  4. `CLICKUP_LIST_ID` env var contained a query-string suffix (`?pr=...`) pasted from a ClickUp URL, producing a 404 on task creation. Patched `clickup_notify.py` to strip everything after the first `?`.
- Cash drag: missed a +1.1% SPY week. Acceptable for an init week, but a -1.1% alpha is the opportunity cost of being unprepared on day one.

### Strategy Adjustments
**No strategy.md rule changes proposed** — there is no trade evidence yet to justify modifying any rule. All edits this week were to scripts/operational infrastructure, not to the trading edge.

PROPOSED CHANGE (operational, NOT strategy): Update `portfolio.md` and `scripts/portfolio_snapshot.py` baseline from $10,000 to $100,000 to match the actual Alpaca paper account. | Reason: snapshot script today reported equity $100k while memory reported $10k; this would cause every future "Total Return vs Start" calculation to be wrong by 10x. Will reconcile via snapshot regeneration.

### Next Week Focus
1. **Monday pre-market**: run the pre-market routine cleanly (now that scripts are patched). Identify 2–3 high-conviction earnings/momentum setups.
2. **Sector lean**: prefer Energy, Industrials, and Consumer Staples (YTD leaders); be selective and skeptical in Information Technology given rotation.
3. **First positions**: open 1–2 positions max early in the week with the mandatory 10% trailing stop attached at entry. Stay under the 3-new-positions/week cap.
4. **Risk budget**: keep ≥10% cash, no single position >5% of equity, no sector >20%.
5. **Validate** the portfolio_snapshot.py output matches Alpaca every session.

### Self-Grade: N/A (Setup Week — Friday init)
### Reasoning
Cannot meaningfully grade trading performance with zero trades. Operationally this session was a **C** — the routine ran end-to-end and surfaced and fixed four real infra bugs that would have blocked next Monday's pre-market. The bugs should have been caught before going live, but catching them now (before any capital was at risk) is the better-than-feared outcome. Honest self-assessment: the agent was not actually production-ready at the moment of "initialization."

### Top 3 Lessons
1. **Validate the toolchain end-to-end before you need it.** All four failures (Alpaca URL, Perplexity model, capital-base mismatch, ClickUp list ID) would have been caught by a 5-minute smoke test on day zero.
2. **Cash is a position too.** Being 100% cash cost -1.1% of alpha this week. Once the toolchain works, hesitation has a measurable price.
3. **Trust the API over memory files.** When `portfolio.md` and Alpaca disagree, Alpaca is the source of truth — regenerate memory from the API, not the other way around.
