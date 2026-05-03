# Research Log

_Running log of market research, news, and analysis from each session._

## Format
Each entry: `[DATE TIME] [SESSION] — Summary of findings`

---

## 2026-05-01 — Initialization

**Session**: Setup  
**Perplexity Queries**: None yet  
**Market Context**: Agent initialized. No research conducted yet.  
**Watchlist Candidates**: None identified yet.  
**Action Taken**: None. Awaiting first pre-market session.

---

## 2026-05-03 — Market Open Session (off-schedule)

**Session**: Market Open
**Perplexity Queries**: None — no trade plan in research log to validate against.
**Market Context**: 2026-05-03 is a Sunday; US equity markets are closed. Market-open routine cron is Mon–Fri, so this run is off-schedule.
**Account Status**: Paper trading account is ACTIVE with $100,000 equity, $100,000 cash, $200,000 buying power, 0 open positions, 0 open orders. Reconciled `memory/portfolio.md` to actual broker state (it had stale $10,000 placeholder from initialization).
**Pre-Trade Checklist**:
  - Open positions < 5: PASS (0)
  - New positions this week < 3: PASS (0)
  - Portfolio not down >10%: PASS (flat)
  - Position size ≤ 5%: N/A (no orders)
  - Written thesis in research-log.md for each trade: FAIL — no pre-market plan exists
  - Time not 3:45–4:00 PM ET: PASS (market closed)
**Decision**: PASS / no trades. Per CLAUDE.md ("If you are uncertain, do nothing and document why"), I do not invent trades without an upstream pre-market thesis, and trades cannot fill on a Sunday anyway.
**Confidence Level**: High (in the decision to abstain).
**Operational Notes**:
  - `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` and `scripts/portfolio_snapshot.py` already append `/v2/...` to the base. That doubled path causes HTTP 404. Worked around it for this session by overriding `ALPACA_BASE_URL=https://paper-api.alpaca.markets` per-command. The env var (or the scripts) should be reconciled in a follow-up.
  - `scripts/portfolio_snapshot.py` hardcodes `$10,000` as the starting value when computing "Total Return vs Start" — the snapshot now reports +900% because the actual paper account is $100k. Cosmetic, but worth fixing.
**Lesson / Try Next Time**: Run a pre-market session (or backfill a watchlist + thesis) before the market-open routine fires; otherwise market-open has nothing to execute. Add a guard to `market-open.md` that skips Step 4 if no plan is present and skips entirely on weekends/holidays.

---

## Research Template (copy for each session)

```
## [DATE] — [SESSION TYPE]

**Macro**: [Fed stance, VIX level, S&P trend]
**Sector Leaders Today**: [Top performing sectors]
**Sector Laggards Today**: [Underperforming sectors]
**Key News**: [Top 3 market-moving stories]
**Earnings This Week**: [Companies reporting]
**Watchlist Review**:
  - [SYMBOL]: [Thesis] [Signal strength: Strong/Medium/Weak]
**Decision**: [Buy / Hold / Sell / Pass — with reason]
**Confidence Level**: [High / Medium / Low]
```
