# Portfolio State

_Last updated: 2026-09-22 12:04 ET (Tue W20 D2 midday cron; Alpaca account/positions/orders re-verified; MSFT $507.40 pre-open → $494.65 midday on intraday chip/AI-megacap fade; equity -$127.49 / -0.13% vs 08:37 market-open; 42-session mechanical HOLD carry continues)_

## Account Summary
- **Mode**: Paper Trading
- **Current Equity**: $99,752.08
- **Cash**: $94,805.57
- **Buying Power**: $393,072.49

## Open Positions

| Symbol | Shares | Avg Cost | Current Price | Market Value | P&L | P&L % | Notes |
|--------|--------|----------|---------------|--------------|-----|--------|-------|
| MSFT | 10 | $500.00 | $494.65 | $4,946.51 | $-53.49 | -1.07% | Midday fade from $507.40 pre-open → $494.65 (-$12.75/sh / -2.51% intraday); 10% trailing stop armed since 8/11 (order `6f280579…`; day 42 incl. weekend); **$6.65/sh above $488 Q-trigger** (narrowed from $19.40 at 08:37 pre-open); 5.93pp above -7% forced-sell floor ($465); 8.93pp above -10% Rule E hard-cut ($450) — well outside middle-band (≤1.5pp AND >0.5pp) and deep-band (≤0.5pp); thesis intact (no earnings event, no downgrade; chip/AI-megacap intraday reversion off strong pre-open, not thesis-break); 16.07pp away from +15% partial-profit gate — no action needed |

## Pending Orders
- SELL 10 MSFT | Type: trailing_stop | 10% trail | Status: new (order `6f280579-a397-4141-b1eb-cff350e456a4`)

## Allocation Summary
- Cash: 95.04%
- Equities: 4.96% (MSFT only)
- Total Return vs Start ($100,000): **-0.248%**
- Open positions: 1 / 5 max
- W20 fills: 0 (D2 midday)
- W20 new positions: 0 / 3
- W20 Perplexity Q ledger: 5 / 8 (Mon 2 pre-market + Mon 1 EOD SPY + Tue 2 pre-market; 0 this midday)
- Today (Tue 9/22 W20 D2 12:04 ET midday): **Fourth real W20 session** (after Mon full-day chain + Tue 06:15 pre-market + Tue 08:37 market-open). Executed full midday routine per `routines/midday.md`: memory load (5 files) → 3 Alpaca reads → §3 exit-rule scan (all 5 conditions HOLD) → NO orders placed → memory update → commit + push. **Key state deltas vs Tue 08:37 market-open**: MSFT $507.40 → $494.65 (-$12.75/sh / -2.51% intraday fade); equity $99,879.57 → $99,752.08 (-$127.49 / -0.13%); cash unchanged (73rd zero-drift session). Midday fade wiped the pre-open above-cost print — position back underwater but still deep-cushioned. **§3 Exit-rule scan (routine §3 mandate)**: (a) down > 7% forced-sell — NOT triggered (-1.07% < 7%; 5.93pp cushion); (b) thesis broken — NOT triggered (no earnings, no downgrade; intraday reversion is not thesis-break); (c) VIX > 30 — NOT triggered (~14.6-14.9 low regime per 06:15 pre-market read; no midday re-pull warranted for structural read); (d) up > 15% partial-profit — NOT applicable (underwater); (e) trailing stop change — NOT applicable (no +15% gain; no thesis-break). All 5 conditions HOLD. **§4 Quick research (routine §4)**: NOT triggered — position at -1.07% is not in the -5% to -6% borderline range routine names; no news signal from carry that breaks thesis; Q spend would burn 12.5% of W20 budget for zero decision quality. **§3 Rule E status**: cushion 5.93pp above -7%, 8.93pp above -10% hard-cut — well outside both middle-band and deep-band; Rule E DOES NOT arm. Ladder cushion at $488 Q-trigger narrowed to $6.65/sh (from $19.40 pre-open) — watching but still positive. **§4 Rule A REGIME-STATUS**: SUSPENDED continues (14th consecutive session); 10Y ~5.00% unchanged; auto-resume gate ~30bp away. **§6 ClickUp**: SUPPRESSED per routine §7 ("Only send if: position was cut, major loss realized, or portfolio moved significantly"). Zero cuts + zero major loss + intraday -0.13% (immaterial move) = zero notification-triggering event. Next scheduled ClickUp: today's market-close 15:05 ET (Tue W20 D2 EOD summary). Pre-committed ladder held for **43rd consecutive session** without discretionary override. Session P&L vs 08:37 market-open: **-$127.49 / -0.13%**. Next scheduled session: today's market-close 15:05 ET.
