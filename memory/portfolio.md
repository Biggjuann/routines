# Portfolio State

_Last updated: 2026-09-23 08:30 ET (Wed W20 D3 market-open cron; Alpaca account/positions/orders re-verified; MSFT $502.30 pre-market → $501.99 at 08:30 on essentially-flat overnight drift after +$3.86 gap-up vs Tue close; equity -$3.10 / -0.003% vs 06:15 pre-market; day P&L +$36.75 / +0.037% vs Tue 15:05 close $99,788.72; 44-session mechanical HOLD carry continues)_

## Account Summary
- **Mode**: Paper Trading
- **Current Equity**: $99,825.47
- **Cash**: $94,805.57
- **Buying Power**: $393,278.00

## Open Positions

| Symbol | Shares | Avg Cost | Current Price | Market Value | P&L | P&L % | Notes |
|--------|--------|----------|---------------|--------------|-----|--------|-------|
| MSFT | 10 | $500.00 | $501.99 | $5,019.90 | $+19.90 | +0.398% | Second consecutive session with MSFT above cost after Wed pre-market $502.30 read (essentially flat -$0.31/sh drift vs pre-market; +$3.55/sh vs Tue 15:05 close $498.44); 10% trailing stop armed since 8/11 (order `6f280579…`; day 43 incl. weekend); **$13.99/sh above $488 Q-trigger**; 7.398pp above -7% forced-sell floor ($465); 10.398pp above -10% Rule E hard-cut ($450) — well outside middle-band (≤1.5pp AND >0.5pp) and deep-band (≤0.5pp); thesis intact (no earnings event, no downgrade; overnight tech firmness reinforces); 14.6pp away from +15% partial-profit gate ($575) — no action needed |

## Pending Orders
- SELL 10 MSFT | Type: trailing_stop | 10% trail | Status: new (order `6f280579-a397-4141-b1eb-cff350e456a4`)

## Allocation Summary
- Cash: 94.97%
- Equities: 5.03% (MSFT only; nudging just above 5% cap on gain-drift only — NOT a rule violation because the cap applies to new-entry sizing, not gain-driven drift)
- Total Return vs Start ($100,000): **-0.175%**
- Open positions: 1 / 5 max
- W20 fills: 0 (D3 08:30)
- W20 new positions: 0 / 3
- W20 Perplexity Q ledger: 8 / 8 (Mon 3 + Tue 4 + Wed pre-market 2 + Wed market-open 0; **at cap**; 0 Qs remaining for Wed midday/EOD + Thu 3 sessions + Fri 3 sessions unless §9 contingency fires per Wed pre-market pre-commit)
- Today (Wed 9/23 W20 D3 08:30 ET market-open): **Sixth real W20 session** (after Mon full-day chain + Tue full-day chain + Wed 06:15 pre-market). Executed full market-open routine per `routines/market-open.md`: memory load (4 files) → 3 Alpaca reads → 6-item pre-trade checklist (all clear) → §4 Rule E check (well outside; DOES NOT arm) → NO orders placed → memory update → ClickUp SUPPRESSED → commit + push. **Key state deltas vs Wed 06:15 pre-market**: MSFT $502.30 → $501.99 (essentially flat -$0.31/sh drift); equity $99,828.57 → $99,825.47 (-$3.10 / -0.003%); cash unchanged (74th zero-drift session). **Day P&L vs Tue 15:05 close $99,788.72**: +$36.75 / +0.037% (modest overnight lift held into open cron). **Pre-trade checklist (routine §3 mandate)**: all 6 guardrails clear (positions 1/5, weekly new 0/3, portfolio -0.175% (>-10% floor with 9.825pp cushion), MSFT 5.03% (gain-drift, not new-entry), thesis intact, time 08:30 not in 15:45–16:00 window). **§4 Rule E middle-band check**: MSFT cushion 10.398pp above -10% hard-cut — **well outside** middle-band (≤1.5pp AND >0.5pp) and deep-band (≤0.5pp). **DOES NOT arm.** **§5 Rule A REGIME-STATUS**: SUSPENDED continues (19th consecutive session incl. weekend; 10Y ~4.95–5.00% per Wed pre-market pull; auto-resume gate 25–30bp away). **§6 ClickUp**: SUPPRESSED per routine §6 explicit ("If NO trades were placed, do NOT send"). **§7 Perplexity**: 0 Qs (W20 running total: 8/8; at cap; 06:15 pre-market pulls cover session's material research needs). Pre-committed ladder held for **44th consecutive session** without discretionary override. Next scheduled session: Wed 9/23 W20 D3 midday 12:04 ET.
