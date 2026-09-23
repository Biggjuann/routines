# Portfolio State

_Last updated: 2026-09-23 12:04 ET (Wed W20 D3 midday cron; Alpaca account/positions/orders re-verified; MSFT $498.64 midday print vs $501.99 at 08:30 open cron = -$3.35/sh intraday fade back to essentially-flat vs Tue 15:05 close $498.44; equity -$33.50 / -0.034% vs 08:30 open; day P&L +$3.25 / +0.003% vs Tue 15:05 close; 45-session mechanical HOLD carry continues)_

## Account Summary
- **Mode**: Paper Trading
- **Current Equity**: $99,791.97
- **Cash**: $94,805.57
- **Buying Power**: $393,184.20

## Open Positions

| Symbol | Shares | Avg Cost | Current Price | Market Value | P&L | P&L % | Notes |
|--------|--------|----------|---------------|--------------|-----|--------|-------|
| MSFT | 10 | $500.00 | $498.64 | $4,986.40 | $-13.60 | -0.272% | Intraday drift back below cost after Wed pre-market $502.30 / 08:30 open $501.99 pair of above-cost prints; 10% trailing stop armed since 8/11 (order `6f280579…`; day 44 incl. weekend); **$10.64/sh above $488 Q-trigger** (narrowed from $13.99 at 08:30); 6.728pp above -7% forced-sell floor ($465); 9.728pp above -10% Rule E hard-cut ($450) — well outside middle-band (≤1.5pp AND >0.5pp) and deep-band (≤0.5pp); thesis intact (no earnings event, no downgrade; normal chip/AI-megacap intraday reversion off pre-market strength); 15.272pp away from +15% partial-profit gate ($575) — no action needed |

## Pending Orders
- SELL 10 MSFT | Type: trailing_stop | 10% trail | Status: new (order `6f280579-a397-4141-b1eb-cff350e456a4`)

## Allocation Summary
- Cash: 95.0%
- Equities: 5.0% (MSFT only; back below the 5% cap after intraday fade)
- Total Return vs Start ($100,000): **-0.208%**
- Open positions: 1 / 5 max
- W20 fills: 0 (D3 12:04)
- W20 new positions: 0 / 3
- W20 Perplexity Q ledger: 8 / 8 (Mon 3 + Tue 4 + Wed pre-market 2 + Wed market-open 0 + Wed midday 0; **at cap**; 0 Qs remaining for Wed EOD + Thu 3 sessions + Fri 3 sessions unless §9 contingency fires per Wed pre-market pre-commit)
- Today (Wed 9/23 W20 D3 12:04 ET midday): **Seventh real W20 session** (after Mon full-day chain + Tue full-day chain + Wed 06:15 pre-market + Wed 08:30 market-open). Executed full midday routine per `routines/midday.md`: memory load (5 files) → 3 Alpaca reads → 5-condition exit-rule scan on MSFT (all HOLD) → §4 quick-research gate (not triggered; MSFT at -0.27% is 4.73pp above the -5% borderline entry) → NO orders placed → `portfolio_snapshot.py` run → memory update → ClickUp SUPPRESSED → commit + push. **Key state deltas vs Wed 08:30 open**: MSFT $501.99 → $498.64 (-$3.35/sh intraday fade back below cost; normal chip/AI-megacap reversion off pre-market highs); equity $99,825.47 → $99,791.97 (-$33.50 / -0.034%); cash unchanged (74th zero-drift session). **Day P&L vs Tue 15:05 close $99,788.72**: +$3.25 / +0.003% (essentially flat on the day; the +$36.75 open-cron gain evaporated into a small +$3.25 midday gain). **Exit-rule scan (routine §3 mandate)**: all 5 conditions HOLD — (a) MSFT at -0.272% not > 7% down (6.728pp cushion to -7% floor); (b) thesis intact (no earnings event, no downgrade); (c) VIX ~14.6-14.9 sub-20 low-vol; (d) not up +15%; (e) trailing stop armed unchanged (day 44). **§4 quick-research gate**: NOT triggered (routine §4 targets -5% to -6% borderline; MSFT at -0.272% is 4.728pp above that zone; 0 Perplexity Q spent). **§5 Rule A REGIME-STATUS**: SUSPENDED continues (20th consecutive session incl. weekend; 10Y ~4.95-5.00% per Wed pre-market pull; auto-resume gate 25-30bp away; no re-pull warranted midday — structural read). **§6 ClickUp**: SUPPRESSED per routine §7 explicit ("Only send if: position was cut, major loss realized, or portfolio moved significantly"; -0.034% intraday drift well below >3% CLAUDE.md threshold). **§7 Perplexity**: 0 Qs (W20 running total: 8/8; at cap; no borderline position and no thesis-break signal warrant a spend). Pre-committed 10% trailing-stop ladder held for **45th consecutive session** without discretionary override. Next scheduled session: Wed 9/23 W20 D3 market-close 15:05 ET.
