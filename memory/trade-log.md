# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

- **2026-05-05 12:00 ET — Midday check**: No open positions, no open orders. No exit rules triggered. Account active, equity $100,000 (paper), 100% cash. No action taken.
- **2026-05-05 12:00 ET — ENV BUG (investigate before retrying per guardrail)**: `ALPACA_BASE_URL` is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` already appends `/v2/...` to every path, producing `/v2/v2/positions` → HTTP 404. Worked around for this session by overriding `ALPACA_BASE_URL=https://paper-api.alpaca.markets` inline. Fix permanently: either (a) remove the trailing `/v2` from the env var (matches CLAUDE.md spec), or (b) strip a trailing `/v2` in `get_base_url()`. Future routines will fail until this is fixed.
- **2026-05-05 12:00 ET — Note**: Live paper account equity is $100,000, but `memory/strategy.md` and prior `memory/portfolio.md` recorded a $10,000 starting value. Snapshot now shows +900% vs that baseline, which is meaningless. Reconcile starting baseline at next pre-market session.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
