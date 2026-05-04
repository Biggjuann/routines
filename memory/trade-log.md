# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

---

## Session Log

### 2026-05-04 — Midday Check
- **Action**: No action. Zero open positions, zero open orders.
- **Account state**: Paper account, equity $100,000, cash $100,000, buying power $200,000, status ACTIVE.
- **Exit rules applied**: N/A (no positions to evaluate against -7% / +15% / +25% rules).
- **API issue encountered**: First calls to `alpaca_client.py` returned `HTTP 404 Not Found`. Investigated per guardrails before retrying. Root cause: the `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `alpaca_client.py` and `portfolio_snapshot.py` already append `/v2/...` to the base, producing `/v2/v2/account`. Worked around for this session by overriding `ALPACA_BASE_URL=https://paper-api.alpaca.markets` inline. **Follow-up needed**: either strip the trailing `/v2` from the env var in the deployment config, or change the scripts to tolerate a `/v2`-suffixed base URL.
- **Other observation**: `portfolio_snapshot.py` hardcodes `$10,000` as the starting value when computing "Total Return vs Start", but the live paper account is $100k, so the snapshot reports `+900%`. Cosmetic; flagged for a future fix.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
