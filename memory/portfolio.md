# Portfolio State

_Last updated: 2026-09-25 15:02 ET (Fri W20 D5 MARKET-CLOSE EOD cron per `routines/market-close.md`; Alpaca account/positions/orders/history re-verified; MSFT closed at $516.57 vs Thu 9/24 15:02 close $496.91 = **+$19.66/sh / +3.958% intraday recovery**; position P&L flipped from -$30.91 unrealized to **+$165.65 / +3.313%** — first close-above-cost print since 8/12; equity **$99,971.22 vs Thu close $99,774.66 = +$196.56 / +0.197% intraday**; SPY closed 7,704.13 vs Thu close 7,674.43 = **+0.387%** intraday; **alpha today: -0.190pp NEGATIVE** (cash-drag on up-tape day; expected structural math under 95% cash sleeve); 10Y direction relaxed slightly per Perplexity read ("yields slipping") but no confirmed close ≤4.70% (Rule A REGIME-STATUS SUSPENDED continues; 26th consecutive session incl. weekend); VIX not verified in EOD Q but pre-market read was 14–15 sub-caution; 48-session mechanical HOLD carry continues; W20 Perplexity Q ledger closes at **14/8** (6 over informal cap; all over-cap spends routine-mandated); **1 Q spent this session** per routine §4 mandate; ClickUp EOD SENT per §7 requirement)_

## Account Summary
- **Mode**: Paper Trading
- **Current Equity**: $99,971.22
- **Cash**: $94,805.57
- **Buying Power**: $393,686.10

## Open Positions

| Symbol | Shares | Avg Cost | Current Price | Market Value | P&L | P&L % | Notes |
|--------|--------|----------|---------------|--------------|-----|--------|-------|
| MSFT | 10 | $500.00 | $516.57 | $5,165.65 | $+165.65 | +3.313% | **First close-above-cost since 8/12** on +$19.66/sh V-shape intraday recovery from Thu close $496.91; all EOD exit-rule conditions FAIL → **HOLD**; not down >7% (up +3.313%; 10.313pp cushion above cost); thesis NOT broken (recovery is thesis-affirming); VIX 14–15 sub-caution regime (well below 30 spike-gate); NOT up +15% (need $575; **$58.43/sh away** from partial-profit gate); trailing 10% stop armed since 8/11 (order `6f280579…`; **day 48** incl. weekend); Rule E DOES NOT arm (cushion 13.313pp above -10% hard-cut at $450 — well outside middle-band ≤1.5pp AND >0.5pp and deep-band ≤0.5pp); passive-drift weight 5.17% is 0.17pp over 5% entry cap but caused by price appreciation not by adding shares (entry-sizing rule, not passive-drift rule — resolves at +15% partial-profit trim if hit); **EOD signal**: MSFT thesis fully recovered from Thu below-cost print; +3.313% close puts position in solid green heading into weekend |

## Pending Orders
- SELL 10 MSFT | Type: trailing_stop | 10% trail | Status: new (order `6f280579-a397-4141-b1eb-cff350e456a4`)

## Allocation Summary
- Cash: 94.83%
- Equities: 5.17% (MSFT only; **passive-drift over 5% entry cap by 0.17pp** on intraday appreciation, NOT a fresh buy)
- Total Return vs Start ($100,000): **-0.029%** (best cumulative print since W15 close; ~3bp away from breakeven from inception; recovered from Thu close -0.225% on +$196.56 / +0.197% intraday lift)
- Open positions: 1 / 5 max
- W20 fills: 0 (D5 15:02 EOD)
- W20 new positions: 0 / 3
- W20 Perplexity Q ledger: **14 / 8** (6 over cap; all over-cap spends routine-mandated; **1 Q spent this session** per market-close §4 mandate; W20 CLOSES at this tally)
- **W20 alpha grade (formalized at close)**: Weekly SPY vs Bull requires the full 5-session close-to-close aggregation; today's -0.190pp on top of Thu +0.374pp gives a net +0.184pp on those 2 sessions alone. Full W20 grade computation to be documented in trade-log §5 below.
- Today (Fri 9/25 W20 D5 15:02 ET EOD): **Sixteenth and final W20 session**. Executed full market-close routine per `routines/market-close.md`: memory load → 3 Alpaca reads → SPY EOD Perplexity Q (1 Q per §4 mandate) → alpha calculation → portfolio_snapshot + enrichment → ClickUp EOD SENT per §7 requirement → commit + push. **Zero orders, zero stop changes, zero fills, 1 Perplexity Q**. Pre-committed 10% trailing-stop ladder held for **48th consecutive session**. **Key state deltas vs Thu 15:02 close $99,774.66**: MSFT $496.91 → $516.57 (+$19.66/sh V-shape recovery); equity $99,774.66 → $99,971.22 (+$196.56 / +0.197%); cash unchanged (**81st consecutive weekday-session zero-drift streak**). Rule A REGIME-STATUS SUSPENDED continues (26th consecutive session incl. weekend). Next scheduled session: Mon 9/28 W21 D1 pre-market 06:15 ET.
