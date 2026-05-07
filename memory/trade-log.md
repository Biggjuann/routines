# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

#### 2026-05-07 — Market Close Session
- **Trades filled today**: None.
- **Positions**: 0 open. Cash $100,000 / Equity $100,000 / Buying Power $200,000.
- **API note**: `/v2/orders` returned HTTP 404 from `paper-api.alpaca.markets` during EOD pull. Account and positions endpoints worked fine. Not retrying blindly per guardrails — verified zero activity through `history 1` (no filled orders) and positions endpoint (none open). Will recheck during tomorrow's pre-market; if persistent, investigate Alpaca API status / endpoint path before any new orders.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
