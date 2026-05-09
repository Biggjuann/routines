# Trade Log

_All trades Bull has executed. Updated after every session._

## Format
Each entry: `[DATE] [ACTION] [SYMBOL] [SHARES] @ [PRICE] | Reason | Outcome`

---

## 2026 — Trade History

### May 2026
_No trades yet. Agent initialized 2026-05-01._

#### Session Log

- **[2026-05-09 12:38 ET] Market-Open Session — NO TRADES.** Today is Saturday; US equity markets closed. Pre-market plan (see research-log) targeted Mon 2026-05-11 with conditional AVGO entry only on a non-chase pullback. Account checked: paper, equity $100,000, cash $100,000, 0 positions, 0 open orders, trading not blocked.
- **[2026-05-09] Infra fix:** `scripts/portfolio_snapshot.py` was 404-ing because it appended `/v2` to `ALPACA_BASE_URL` which already includes `/v2`. Patched `get_base_url()` to strip the suffix (matches `alpaca_client.py`). Snapshot now writes correctly.
- **[2026-05-09] Discrepancy flagged for human review:** `memory/strategy.md` and prior `portfolio.md` reference a $10,000 starting value, but the live paper account reports $100,000 equity. `portfolio_snapshot.py` still hardcodes a $10k baseline → reports a misleading "+900% return". Not auto-corrected — needs operator decision on whether to (a) reset Alpaca paper account to $10k, or (b) update the documented starting value to $100k and rescale all 5%/$ position sizing rules accordingly.
- **[2026-05-09 ~12:00 ET] Midday Session — NO ACTION.** Saturday; US equity markets closed. Live Alpaca state verified: 0 positions, 0 open orders, equity $100,000, cash $100,000, buying_power $200,000, trading not blocked. No exit rules apply (nothing to manage). `portfolio_snapshot.py` hit intermittent HTTP 503 DNS failures; skipped the rewrite since live state matches `portfolio.md` (last updated 12:38 ET today). No ClickUp alert — no significant action. Branch note: routine prompts `git checkout main`, but session instructions require committing to `claude/sleepy-ptolemy-sn99A`; following the branch instruction.

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
