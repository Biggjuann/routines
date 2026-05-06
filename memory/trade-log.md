# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

- [2026-05-06 12:00 ET] Midday check — No open positions, no open orders. No exit rules to apply. No action taken.
  - Account equity: $100,000 (paper trading default — note: portfolio.md previously stated $10,000 starting value; reconciled to actual $100K in latest snapshot).
  - Operational note: `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` also appends `/v2/...` to every path, producing a doubled `/v2/v2/` and HTTP 404. Worked around this session by overriding `ALPACA_BASE_URL=https://paper-api.alpaca.markets` inline. Either the env var should drop the trailing `/v2`, or the script should detect/strip it. Flagging for follow-up — do NOT silently retry on 404 per guardrails.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
