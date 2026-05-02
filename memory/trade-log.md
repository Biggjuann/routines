# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

- **[2026-05-02 08:30 ET] Market Open Session — NO TRADES.** Three blockers:
  1. Today is Saturday — US equities markets closed. Routine fired on schedule but no trading possible.
  2. No pre-market plan exists in `research-log.md` (pre-market session never produced trade candidates).
  3. **Alpaca API misconfiguration discovered**: `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` also prepends `/v2` to every path → all requests hit `…/v2/v2/...` and return HTTP 404. Per strategy ("do NOT retry blindly — investigate first"), no further API calls attempted. **Action required from operator**: set `ALPACA_BASE_URL=https://paper-api.alpaca.markets` (no `/v2` suffix), or update the script to strip a trailing `/v2`.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
