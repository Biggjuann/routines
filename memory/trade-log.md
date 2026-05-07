# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

- **2026-05-07 market-open**: No trades placed. Reasons: (1) research-log has no pre-market plan for this date, so there is nothing to execute; (2) Alpaca API calls (`account`, `positions`) returned HTTP 404. Investigation: `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` appends `/v2/account`, producing a doubled `/v2/v2/...` path. Config issue, not an API outage. Recommended fix: drop the trailing `/v2` from `ALPACA_BASE_URL` (script default already includes `/v2`). Did NOT retry blindly per guardrails. Did NOT modify the script — env config is the source of truth.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
