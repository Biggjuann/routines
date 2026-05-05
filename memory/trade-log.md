# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

#### 2026-05-05 — Market open session (no trades)
- **Action**: None. No pre-market trade plan in `memory/research-log.md` to execute.
- **Account check**: Alpaca paper account ACTIVE. Equity $100,000.00, cash $100,000.00, 0 positions, 0 open orders.
- **Bug found and fixed**: `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` and `scripts/portfolio_snapshot.py` also prepend `/v2/...` to every path → produced `/v2/v2/account` → HTTP 404. Added defensive normalization in `get_base_url()` to strip a trailing `/v2` from the env var so both forms work.
- **Data discrepancy noted**: `portfolio_snapshot.py` hardcodes the starting value as $10,000 (matching `memory/strategy.md`), but the live paper account starts at $100,000. The "Total Return vs Start" line currently reads +900% — misleading. Not fixing today (out of scope for market-open); flagged for the next pre-market or weekly-review session to reconcile.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
