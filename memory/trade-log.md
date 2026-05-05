# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

#### 2026-05-05 — EOD Market Close Session
- No trades filled. No new orders placed.
- Account: $100,000 cash, 0 positions.
- Infra issues encountered (logged for follow-up, not blind retry per strategy):
  - `ALPACA_BASE_URL` env var includes trailing `/v2` which double-appends and 404s. Worked around for this session by overriding inline.
  - `perplexity_research.py` references deprecated model `llama-3.1-sonar-large-128k-online`. Worked around by calling Perplexity API directly with `sonar` model.
  - `portfolio_snapshot.py` hardcodes $10K as baseline; actual paper account is $100K.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
