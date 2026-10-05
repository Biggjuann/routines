# Portfolio State

_Last updated: 2026-10-05 06:12 ET (Mon W22 D1 PRE-MARKET on-cron fire; routine `routines/pre-market.md` cron `0 6 * * 1-5`; **4 Perplexity Q spent** premarket + macro + AX + ONB per W21 weekly-review authorization; **zero orders / zero stop changes / zero fills / 0 ClickUp sends**; equity **$99,982.87** (+$2.00 vs Sun 10/4 weekend quote on MSFT drift only); cash **$94,805.57** unchanged (**98th consecutive weekday-session zero-drift streak** — weekend fires did not break; Mon pre-market quote-only session also preserves streak); MSFT **10 @ $500 → $517.73 / +$177.30 / +3.546%** (+$0.20/+0.039% vs Sun quote $517.53; essentially flat weekend-to-Mon-open); Rule A REGIME-STATUS **SUSPENDED-BY-MACRO-GATE-1** (44th consecutive session incl. weekends; 10Y 5.2-5.3% ~50-60bp above 4.70% auto-resume gate; Mon = screen day but screen formally suspended); trailing 10% stop **day 60 armed** (order `6f280579…`; 8/11 origination; server-side auto-ratchet high-water held at $519.50 from Thu 10/1 open-session advance); cumulative-from-inception absolute return **-0.017%** (-$17.13 vs $100k start; essentially flat vs Sun -0.019%); MSFT exit-rule scan **9/9 FAIL** → HOLD; VIX **16.4** carried from Fri 10/2 close (pre-market Q did not surface a fresh VIX read; sub-caution regime); W22 Perplexity Q ledger **4/15-18 new baseline** (pre 2 + AX 1 + ONB 1; 11-14 Q remaining); AX/ONB per-name 4-of-5 deep-dive **FAILED on Perplexity ticker-mis-resolve** (AX→AXP American Express; ONB→ONBPO crypto) — DEFER retained on macro overlay regardless; **cumulative-from-inception alpha ~-4.34% midpoint** (unchanged from W21 close); **trailing-5-week alpha -0.274pp** (W17-W21 window; unchanged); **W-counter formally reset to W22 D1 Mon-anchor per W21 lessons**; branch `claude/epic-shannon-o26elj`)_

## Account Summary
- **Mode**: Paper Trading
- **Current Equity**: $99,982.87
- **Cash**: $94,805.57
- **Buying Power**: $393,718.72

## Open Positions

| Symbol | Shares | Avg Cost | Current Price | Market Value | P&L | P&L % | Notes |
|--------|--------|----------|---------------|--------------|-----|--------|-------|
| MSFT | 10 | $500.00 | $517.73 | $5,177.30 | $+177.30 | +3.5% | Mon 06:12 ET pre-market quote (+$0.20/+0.039% vs Sun 10/4 quote $517.53); all 9 exit-rule conditions FAIL vs pre-market quote → **HOLD**; not down >7% (up +3.546%; 10.546pp cushion above -7% floor at $465); thesis intact (next earnings Nov 2026 outside blackout); VIX 16.4 carried from Fri close (sub-caution regime; pre-market Q did not surface fresh print); NOT up +15% (need $575; $57.27/sh away = +11.46pp headroom); trailing 10% stop **day 60 armed** since 8/11 (order `6f280579…`; auto-ratchet high-water held at $519.50 from Thu 10/1 open-session advance); Rule E DOES-NOT-ARM (cushion $67.73/sh = 13.546pp above -10% hard-cut at $450 — well outside middle-band ≤1.5pp AND >0.5pp and deep-band ≤0.5pp); passive-drift weight 5.18% is 0.18pp over 5% entry cap on price appreciation only (entry-sizing rule not violated — resolves at +15% partial-profit trim if hit); $488 Q-trigger cushion $29.73/sh; $485 tighten pre-commit cushion $32.73/sh; $482.50 SELL contingency cushion $35.23/sh |

## Pending Orders
- SELL 10 MSFT | Type: trailing_stop | 10% trail | Status: new (order `6f280579-a397-4141-b1eb-cff350e456a4`; day 60 armed; server-side auto-ratchet high-water held at $519.50 from Thu 10/1 open-session advance)

## Allocation Summary
- Cash: 94.8%
- Equities: 5.2% (MSFT only; passive-drift over 5% entry cap by 0.18pp on price appreciation, NOT a fresh buy)
- Total Return vs Start ($100,000): **-0.017%** (Mon 06:12 ET pre-market quote; essentially flat vs Sun 10/4 weekend quote)
- Open positions: 1 / 5 max
- W22 fills: 0
- W22 new positions: 0 / 3
- Day P&L (Mon 10/5 pre-market vs Sun 10/4 weekend quote): **+$2.00 / +0.002%** (MSFT quote +$0.20/sh drift only)
- Watchlist carry: **AX** (Axos Financial) and **ONB** (Old National Bancorp), both financials with 2-of-5 verified criteria. **W22 Mon pre-market per-name Qs FAILED** on Perplexity ticker-mis-resolution (AX→AXP American Express; ONB→ONBPO crypto); macro overlay still negative for regional banks (10Y 5.2-5.3%, ~50-60bp above Rule A gate), so DEFER retained regardless. Next attempt should use explicit full-company-name disambiguation in a single Q, OR await 10Y compression toward gate.
- Today (Mon 10/5 W22 D1 pre-market on-cron fire): 4 memory reads → 4 Perplexity Qs (premarket + macro + AX + ONB) → §3 Rule A SUSPENDED screen suspended → §4 candidate screen zero new → §5 MSFT exit-rule 9/9 FAIL → §6 trade plan HOLD-only → write research-log → commit + push on designated branch → §7 ClickUp SUPPRESSED. **Zero orders, zero stop changes, zero fills, ClickUp SUPPRESSED**. **W-counter formally reset to W22 D1 per W21 lesson** — all narrative references now anchored to W22 Mon-start. Next scheduled session: **Mon 10/5 W22 D1 market-open 08:30 ET** (ISM Services PMI 10:00 AM ET primary catalyst; MSFT exit-rule re-scan; trailing-stop auto-ratchet watch at $519.50 server-side).
