# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

#### 2026-05-08 — Market Close Session
- **Action**: None. Reviewed only — no fills today, no entries triggered.
- **Account**: equity $100,000.00, cash $100,000.00, daytrade_count 0, status ACTIVE.
- **History**: `alpaca_client.py history 1` → "No filled orders in this period."
- **Anomaly**: `GET /v2/orders?status=open` returned HTTP 404 from this paper environment, breaking `portfolio_snapshot.py`. Other endpoints (`/v2/account`, `/v2/positions`, `/v2/account/portfolio/history`) responded normally. Wrote `portfolio.md` manually for this session. Investigate before re-running `portfolio_snapshot.py` — likely a paper-API path or auth scope issue, not a script bug, but confirm. Do not retry blindly per CLAUDE.md guardrails.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
