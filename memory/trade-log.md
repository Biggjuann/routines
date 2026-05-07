# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

#### 2026-05-07 — Midday Check
- **Action**: None (no open positions to manage)
- **Account**: Equity $100,000.00, Cash $100,000.00, 0/5 positions, 0 open orders
- **Note**: Fixed bug in `scripts/portfolio_snapshot.py` — `get_base_url()` did not strip trailing `/v2` from `ALPACA_BASE_URL`, causing all API requests to 404. Now matches `alpaca_client.py` behavior.
- **Lesson**: Cross-check helper scripts share the same base-URL handling so a single env var change doesn't silently break one path.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
