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

## 2026-05-08 — Market Open

**Session**: Market Open (8:30 AM ET routine)
**Perplexity Queries**: None — see below
**Account Status**: Paper account, $100,000 equity, $100,000 cash, 0 open positions, 0 pending orders.
**Pre-Market Plan**: NONE. No pre-market session ran ahead of today's open; research-log.md held no trade thesis for any symbol.
**Pre-Trade Checklist**:
  - Open positions: 0/5 ✓
  - New positions this week: 0/3 ✓
  - Portfolio drawdown: 0% ✓
  - Position size: N/A (no planned trades)
  - Written thesis in research-log.md: ✗ (no theses present)
  - Time window OK: ✓
**Decision**: PASS — do not execute any trades. Per strategy guardrail "If you are uncertain, do nothing and document why," entering positions without a researched thesis violates entry rules (need ≥2 independent signals + written thesis).
**Confidence Level**: High (in the decision to pass)
**Issue Discovered**: `scripts/portfolio_snapshot.py` was hitting HTTP 404 because it was not stripping `/v2` from `ALPACA_BASE_URL` the way `scripts/alpaca_client.py` does. Patched `get_base_url()` to match. Snapshot now writes successfully.
**Note**: `portfolio.md` previously listed starting value of $10,000 but the live paper account is $100,000. The snapshot script's "Total Return vs Start ($10,000)" line is therefore misleading. Flagging for a future session — do not treat the +900% number as real performance.
**Continuous Improvement**: Pre-market session must run before market open to produce a trade plan. If no plan exists at open, the correct action is exactly what was done here: pass and log.

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
