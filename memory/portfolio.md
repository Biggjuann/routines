# Portfolio State

_Last updated: 2026-09-25 08:37 ET (Fri W20 D5 MARKET-OPEN cron per `routines/market-open.md`; Alpaca account/positions/orders re-verified; MSFT $498.066 vs Fri 06:15 pre-market $496.95 = +$1.116/sh modest overnight-into-open recovery; equity $99,786.37 vs Fri 06:15 pre-market $99,775.07 = +$11.30 / +0.011% since pre-market; 10Y still ~5.1-5.2% carry (Rule A REGIME-STATUS SUSPENDED 25th consecutive session incl. weekend); VIX 14.6-15.7 sub-caution; 48-session mechanical HOLD carry continues; W20 Perplexity Q ledger: **13/8** unchanged from pre-market — 5 over informal cap on routine-mandated pulls only; **0 Q spent this session** per routine §4 clause "get current price before ordering" — not triggered since no order placed)_

## Account Summary
- **Mode**: Paper Trading
- **Current Equity**: $99,786.37
- **Cash**: $94,805.57
- **Buying Power**: $393,168.52

## Open Positions

| Symbol | Shares | Avg Cost | Current Price | Market Value | P&L | P&L % | Notes |
|--------|--------|----------|---------------|--------------|-----|--------|-------|
| MSFT | 10 | $500.00 | $498.066 | $4,980.66 | $-19.34 | -0.387% | Modest overnight-into-open recovery from Fri 06:15 pre-market $496.95 → 08:37 market-open $498.066 (+$1.116/sh); still below cost on 10Y ~5.1-5.2% 2007-high-neighbor carry; **Rule E DOES NOT arm** (cushion 9.613pp above -10% hard-cut — well outside middle-band ≤1.5pp AND >0.5pp and deep-band ≤0.5pp); market-open §3 pre-trade checklist: 6/6 items ✓ (open positions 1/5 max; W20 fills 0/3 max; portfolio -0.214% not >10% down; MSFT weight 4.99% ≤ 5% cap; MSFT HOLD thesis intact — no new position candidate today; time 08:37 ET not in 15:45-16:00 no-trade window); §3 exit-rule scan on MSFT: NOT down >7% from cost (only -0.387%; 6.613pp cushion to forced-sell); thesis NOT broken (no earnings event; next print Nov 2026; macro yield-headwind reaction only); VIX 14.6-15.7 (well below 30 spike-gate); **all §3 sell-immediately conditions FAIL → HOLD**; 10% trailing stop armed since 8/11 (order `6f280579…`; **day 48** incl. weekend); **$10.066/sh above $488 Q-trigger** (widened from $8.95 at pre-market on overnight-into-open recovery); 6.613pp above -7% forced-sell floor ($465); 9.613pp above -10% Rule E hard-cut ($450); $76.934/sh away from +15% partial-profit gate ($575) — no action needed |

## Pending Orders
- SELL 10 MSFT | Type: trailing_stop | 10% trail | Status: new (order `6f280579-a397-4141-b1eb-cff350e456a4`)

## Allocation Summary
- Cash: 95.01%
- Equities: 4.99% (MSFT only; fade below cost persists on 10Y ~5.1-5.2% carry)
- Total Return vs Start ($100,000): **-0.214%** (recovered from Fri 06:15 pre-market -0.225% on +$11.30 overnight-into-open lift; still within W15-close recovery band)
- Open positions: 1 / 5 max
- W20 fills: 0 (D5 08:37 market-open)
- W20 new positions: 0 / 3
- W20 Perplexity Q ledger: **13 / 8** (Mon 3 + Tue 4 + Wed 3 + Thu pre-market 1 + Thu EOD 1 + Fri pre-market 2 = **5 over informal 8-Q cap**; all over-cap spends are routine-mandated; **0 Q spent this session** — routine §4 pre-price Q not triggered since no order placed)
- Today (Fri 9/25 W20 D5 08:37 ET market-open): **Fourteenth real W20 session** (after Mon full-day chain + Tue full-day chain + Wed full-day chain of 4 + Thu 06:15 pre-market + Thu 08:37 market-open + Thu 12:04 midday + Thu 15:02 market-close + Fri 06:15 pre-market). Executed full market-open routine per `routines/market-open.md`: memory load (4 files: strategy + portfolio + research-log + trade-log tail) → 3 Alpaca reads (account + positions + orders) → §3 pre-trade checklist (6 items ✓) → §3 exit-rule scan on MSFT (5 conditions × 1 position) → §4 planned-trade execution SKIPPED (no planned trades per pre-market carry-in) → §5 memory writes → §6 ClickUp SUPPRESSED (no trade placed per routine §6 explicit criteria) → §7 commit + push. **Zero orders, zero stop changes, zero fills, 0 Perplexity Q**. Pre-committed 10% trailing-stop ladder held for **48th consecutive session** without discretionary override. **Key state deltas vs Fri 06:15 pre-market $99,775.07**: MSFT $496.95 → $498.066 (+$1.116/sh modest overnight-into-open recovery); equity $99,775.07 → $99,786.37 (+$11.30 / +0.011%); cash unchanged (**79th consecutive zero-drift session**). **Key state deltas vs Thu 15:02 close $99,774.66**: +$11.71 / +0.012% overnight (essentially flat). **§5 Rule A REGIME-STATUS**: SUSPENDED continues (25th consecutive session incl. weekend; 10Y ~5.1-5.2% per Fri pre-market Perplexity pull = **~40-50bp above 4.70% auto-resume gate**; auto-resume probability unchanged and very low). **§6 ClickUp**: SUPPRESSED (routine §6 explicit — only send if trade placed). Next scheduled session: Fri 9/25 W20 D5 midday 12:04 ET.
