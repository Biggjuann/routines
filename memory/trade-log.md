# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

#### 2026-05-04 — Market Close session
- No fills today. No open positions. Cash 100%.
- Reconciled memory with live Alpaca paper account: actual equity is $100,000.00 (memory had stated $10,000.00 — corrected).
- Tooling fixes during this session:
  - `scripts/alpaca_client.py` and `scripts/portfolio_snapshot.py`: normalized `ALPACA_BASE_URL` to strip trailing `/v2` so the live env value `https://paper-api.alpaca.markets/v2` no longer produces a `/v2/v2/...` 404.
  - `scripts/perplexity_research.py`: switched default model from retired `llama-3.1-sonar-large-128k-online` to `sonar`.
  - `scripts/portfolio_snapshot.py`: starting-value reference now driven by `BULL_STARTING_VALUE` env var (default $100,000) instead of hardcoded $10,000.
  - `scripts/clickup_notify.py`: strip stray query string / path from `CLICKUP_LIST_ID` (env var contained `901416050491?pr=...` which mangled the task POST path).
- ClickUp EOD posted: https://app.clickup.com/t/86b9rd70e

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
