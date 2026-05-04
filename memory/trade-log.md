# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026

- **2026-05-04 (Mon, Market Open)** — NO TRADE. No pre-market trade plan existed in research-log.md, so there was nothing to execute. Account verified ACTIVE on Alpaca paper ($100k equity, 0 positions, 0 open orders).

#### Operational notes
- **2026-05-04** — `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` and `scripts/portfolio_snapshot.py` append `/v2/...` paths themselves, producing requests to `/v2/v2/account` (HTTP 404). Worked around for this session by overriding `ALPACA_BASE_URL=https://paper-api.alpaca.markets` inline. Permanent fix required: either strip the `/v2` from the env var, or update the scripts to handle a base URL that already includes it. Did NOT retry blindly per the guardrail.
- **2026-05-04** — `scripts/portfolio_snapshot.py` hard-codes a $10,000 starting value in its "Total Return vs Start" calculation, but the actual Alpaca paper account starts at $100,000. Snapshot currently reports +900% return spuriously. Track this for cleanup; does not affect trading decisions.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
