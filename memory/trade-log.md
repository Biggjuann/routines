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
- **[2026-05-09 ~19:05 ET] Market-Close Session — NO TRADES.** Saturday; US equity markets closed (no Friday-of-this-session activity exists — last trading day was Fri 2026-05-08). Verified live Alpaca state: paper, equity $100,000, cash $100,000, buying_power $200,000, 0 positions, 0 filled orders past 1d, trading not blocked. Refreshed `portfolio.md` via `portfolio_snapshot.py` (clean run, no 503s this time); the misleading "+900% vs $10k baseline" line persists — still awaiting operator decision on baseline (see 2026-05-09 discrepancy entry above). Researched Fri 2026-05-08 SPY action via Perplexity for context (S&P +0.84% to 7,398 record close; semis/AI led, SOX +5% Fri). No fills today, so no day P&L to compute; portfolio flat at $100,000 (0.00%) vs SPY +0.84% Fri = -0.84% alpha for last trading day (cash drag). EOD ClickUp summary sent. Branch: committing to `claude/epic-davinci-RyCG1` per session instruction (overrides routine's `git checkout main`).

---

## Running P&L Summary

| Month | Trades | Winners | Losers | Net P&L | Win Rate |
|-------|--------|---------|--------|---------|----------|
| May 2026 | 0 | 0 | 0 | $0.00 | — |

## Key Trade Lessons
_Populated as trades are made and reviewed._
