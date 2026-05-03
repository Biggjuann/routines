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

## 2026-05-03 — Market Close Routine (Sunday, market closed)

**Session**: EOD / Market Close  
**Perplexity Queries**: 1 — recap of Friday 2026-05-01 S&P 500 action.  
**Market Context (Friday close, most recent session)**:
- S&P 500 closed at a record 7,230.12 on Fri 2026-05-01, +0.14% on the day.
- Five straight weekly gains. Q1 earnings beats running 11.5% above estimates (long-term avg 4.4%); consensus 27.8% YoY EPS growth, highest since Q4 2021.
- Big Tech leadership: Amazon +77%, Alphabet +81%, Meta +61% earnings YoY.
- Sector rotation broadening: financials (rates) and energy (commodity stability) participating.
- Apple announced $100B share buyback — supportive for tape.

**Portfolio State**: $100,000 cash, 0 positions. No alpha measurement yet (no exposure).  
**Watch For Monday 2026-05-04**:
- Megacap tech follow-through after AAPL buyback news.
- Earnings cadence continues — track names with raised guidance.
- VIX level and 10Y yield direction at the open.

**Lessons / What to do differently**:
1. The local `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` already prepends `/v2/...` — caused 404s. Worked around for this session by overriding `ALPACA_BASE_URL` inline. **Action**: harden client to strip a trailing `/v2` from the env var, or document the canonical base URL.
2. `scripts/perplexity_research.py` defaulted to deprecated model `llama-3.1-sonar-large-128k-online` (HTTP 400). Updated default to `sonar`.
3. `scripts/portfolio_snapshot.py` hardcodes a $10,000 starting baseline; actual paper equity is $100,000. Reported "+900% return", which is misleading. **Action**: parametrize starting value (env var or memory file) before the first real trade so alpha vs SPY is measured correctly.
4. No new positions opened — Sunday, markets closed. Correct behavior.

**Action Taken**: None on positions. Memory + scripts updated for next session.

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
