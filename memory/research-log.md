# Research Log

_Running log of market research, news, and analysis from each session._

## Format
Each entry: `[DATE TIME] [SESSION] — Summary of findings`

---

## 2026-05-01 — Initialization

**Session**: Setup  
**Perplexity Queries**: None yet  
**Market Context**: Agent initialized. No research conducted yet.  
**Watchlist Candidates**: None identified yet.  
**Action Taken**: None. Awaiting first pre-market session.

---

## 2026-05-03 — Pre-Market (for Mon 2026-05-04 open)

**Macro**: Fed held 3.5–3.75% in divisive 8-4 vote (most fractured since 1992); Goolsbee called recent inflation "bad news," urging caution on cuts. PCE at 3.5% YoY (March), sticky. LEI down 0.6%, Sahm Rule nearing trigger, U-Mich Consumer Expectations at historical low. S&P 500 closed record 7,230.12 on May 1; futures +0.06%, Nasdaq futures +0.68%. VIX low (favorable for risk per strategy). Tilt: defensives over cyclicals, fade rate-cut hopes.

**Sector Posture**:
- Healthcare (XLV): defensive bias — favored
- Energy (XLE): oil escalation tailwind — favored
- Tech/Semis: pullback on OpenAI growth miss, NVDA -8% from ATH — caution into NVDA earnings May 20

**Earnings Just Reported (Apr 30 – May 1)**: LLY, XOM, GOOGL all beat. NVDA reports May 20.

**Watchlist Review (screened against 5-criteria; need 4/5)**:

- **LLY (Eli Lilly)** — Healthcare. Q1: rev $19.8B (+55.5% YoY), EPS $8.55 (+156% YoY), beat both lines, raised FY guidance to $82–85B rev. Above 50/200-day SMA. BofA PT raised to $1,133 May 2 (Buy). Down 11% YTD creates value setup. **Score 4/5** ✅. Signal: **STRONG**.

- **XOM (ExxonMobil)** — Energy. Q1 EPS $1.16 vs $0.98 est (beat ~18%). Energy Products segment +$2B YoY. Permian 1.8M boe/d target, Golden Pass LNG Train 1 online. Qatar damage 3-yr repair = bullish supply-tightening side effect. TIKR PT $181 (~18% upside from $153). **Score 3/5** (missing rev growth + ETF confirm). Signal: **MEDIUM**.

- **NVDA (NVIDIA)** — Tech/AI. Last quarter rev +75% YoY data center, Q1 FY27 guide $78B. Stock $198.45 (-8% from ATH) on OpenAI growth-miss WSJ story. Reports May 20. **Score 3/5** — earnings risk too close. Signal: **WEAK / WAIT**.

**Trade Plan for Monday 2026-05-04 Open**:

| Action | Symbol | Thesis | Confidence | Entry | Target | Stop |
|--------|--------|--------|------------|-------|--------|------|
| BUY | LLY | Earnings beat + raised guidance + above 50/200 SMA + defensive sector. Best risk/reward in book. | HIGH | Limit ~$1,058 (no chase >3% above) | $1,133 (+7%) initial; $1,212 stretch | 10% trailing, hard at -7% |
| BUY | XOM | Earnings beat + LNG/Permian growth + supply tailwind (Qatar repair) + defensive energy. | MEDIUM | Limit ~$153 | $181 (+18%) | 10% trailing, hard at -7% |
| PASS | NVDA | Setup good but May 20 earnings risk + semi pullback on OpenAI news. Wait for post-earnings. | — | — | — | — |

**Sell Candidates**: None (no open positions).
**Hold**: N/A.

**Position Sizing**: Per 5% max rule on $10K portfolio = $500/position. LLY ~0.47 shares (fractional via Alpaca), XOM ~3.27 shares. Total deployment ~$1,000 = 10% of portfolio. Maintains 90% cash, well above 10% minimum.

**Notes / Risks**:
- Today is Sunday — orders queued for Monday 2026-05-04 open routine.
- Avoid first 30 min volatility per strategy (enter after 9:30 ET window settles).
- If LLY or XOM gaps up >3% pre-open, skip entry (no chase rule).
- Monitor Fed speak this week — any dovish surprise accelerates risk-on (bullish all); any hawkish surprise hurts long duration (bearish LLY, neutral XOM).

**Continuous Improvement**: First real research session. Lesson: Perplexity script `model` field needed update from deprecated llama model to `sonar`. Fixed in scripts/perplexity_research.py.

**Action Taken**: Watchlist drafted. No trades placed (market closed Sunday). Hand off to market-open routine Monday.

---

## Research Template (copy for each session)

```
## [DATE] — [SESSION TYPE]

**Macro**: [Fed stance, VIX level, S&P trend]
**Sector Leaders Today**: [Top performing sectors]
**Sector Laggards Today**: [Underperforming sectors]
**Key News**: [Top 3 market-moving stories]
**Earnings This Week**: [Companies reporting]
**Watchlist Review**:
  - [SYMBOL]: [Thesis] [Signal strength: Strong/Medium/Weak]
**Decision**: [Buy / Hold / Sell / Pass — with reason]
**Confidence Level**: [High / Medium / Low]
```
