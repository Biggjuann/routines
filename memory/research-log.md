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

## 2026-05-06 — Market Open

**Session**: Market Open (08:30 ET)
**Perplexity Queries**: None — pre-trade checklist failed before research stage.
**Macro**: Not assessed this session (no research conducted, see Decision).
**Watchlist Candidates**: None — no pre-market session ran today, so no thesis exists for any candidate.
**Decision**: PASS — no trades placed.
**Reason**: The market-open routine requires a written thesis in `memory/research-log.md` for every trade (per `strategy.md` and the pre-trade checklist). The most recent research-log entry before today was the 2026-05-01 initialization; no pre-market session populated a trade plan. Per the strategy ("If you are uncertain, do nothing and document why") I did not enter any positions.
**Confidence Level**: High in the decision to pass.
**Operational Notes**:
  - Discovered `ALPACA_BASE_URL` env var is set to `https://paper-api.alpaca.markets/v2`, but `scripts/alpaca_client.py` and `scripts/portfolio_snapshot.py` append `/v2/...` paths, producing `/v2/v2/...` and HTTP 404. Fixed both scripts to strip a trailing `/v2` and `/` from the base URL so they tolerate either env-var form.
  - Reconciled `memory/portfolio.md` — Alpaca paper account starting equity is $100,000, not the $10,000 documented during init. Updated `portfolio_snapshot.py` baseline to $100,000 so the "Total Return vs Start" figure is correct.
**Lesson for next session**: A market-open session is downstream of the pre-market session. If `research-log.md` has no fresh trade plan for today, the right action is always to pass — never improvise entries on the open.

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
