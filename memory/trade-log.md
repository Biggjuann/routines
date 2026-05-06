# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026

- **2026-05-06 (Market Open)** — NO TRADE. No pre-market trade plan in `research-log.md`; pre-trade checklist failed the "written thesis" requirement. Passed per strategy.
- **2026-05-06 (Ops)** — Logged Alpaca API issue: `ALPACA_BASE_URL` env var includes `/v2` suffix, causing `/v2/v2/...` URL → HTTP 404 in `alpaca_client.py` and `portfolio_snapshot.py`. Fixed both scripts to normalize the base URL (strip trailing `/` and `/v2`). Verified `account` and `positions` calls succeed afterward.
- **2026-05-06 (Ops)** — Reconciled portfolio baseline. Alpaca paper account reports $100,000 starting equity; `portfolio.md` previously documented $10,000. Updated `portfolio_snapshot.py` STARTING_EQUITY constant and regenerated `portfolio.md`.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
