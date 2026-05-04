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

## 2026-05-04 — Pre-Market

**Macro**: Fed funds 3.50–3.75% (held last week, divided 8-4 vote, hawkish tilt). Inflation pressures rising w/ oil; 10Y yield ~4.37%. 94.8% odds Fed holds in June. Cautious tape — fade rallies risk.
**Sector Leaders**: AI/cloud infra, semis (ON Semi pre-mkt +1.15%), energy infra (WMB).
**Sector Laggards**: Rate-sensitive; mixed signals (Dow futures -0.22% vs S&P/Nasdaq +0.10%/0.07%).
**Key News**: OPEC+ raised output 188k bpd (post-UAE exit); oil +1.15–1.49%; Trump 'Project Freedom' Hormuz vessels; Yardeni bullish on earnings.
**Earnings This Week**: NBIS 5/13, ON Holding (ONON) 5/12 — Bull universe relevant: NBIS.

**Watchlist Review**:
  - **NBIS (Nebius Group)**: AI cloud infra. Q4 2025 revenue +547% YoY but missed estimates by -8%. $7B Microsoft upfront payment Friday (+12%); Eigen AI acquisition $643M; analyst avg PT $165.30 (Buy). Already +85% YTD, +3.53% pre-mkt nearing 52-wk high $168.71. **Signal: Strong fundamentals BUT extended.** Strategy violates: "never chase >3% move before entry"; earnings 5/13 = binary risk pre-entry. **Pass — monitor for pullback to 50d SMA.**
  - **ON Semiconductor (ON)**: Pre-mkt +1.15% ahead of earnings. Insufficient research data via Perplexity (results conflated w/ ONON). Defer until clean data; not actionable today.
  - **WMB (Williams Cos)**: Energy infra, strong trend. Not researched in depth this session — flagged for later.

**Decision**: **PASS — no buys at open today.** Cash 100%; no positions to manage.
**Reasoning**:
  1. Hawkish Fed + rising inflation = elevated tail risk; prefer high-quality clean setups.
  2. Best momentum name (NBIS) violates entry rule (>3% prior move) and faces binary earnings 5/13.
  3. ON data insufficient; will not enter blind.
  4. Strategy: "If uncertain, do nothing." First real trading session — discipline > FOMO.

**Confidence Level**: High (in the pass decision).

**Next Session Focus**:
  - Re-research ON Semi w/ explicit "ON Semiconductor NASDAQ" framing.
  - Watch NBIS for pullback entry; do NOT enter pre-earnings (5/13).
  - Add WMB and one healthcare name (biotech catalyst) to deeper screen.
  - Watch VIX level (not surfaced today — get explicit reading).

**Lesson**: Perplexity ticker disambiguation matters — "ON" returns ONON. Always use full company name + exchange for unambiguous tickers.

**Tooling Note**: Updated `scripts/perplexity_research.py` model from deprecated `llama-3.1-sonar-large-128k-online` to `sonar-pro`. Was blocking all research calls.

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
