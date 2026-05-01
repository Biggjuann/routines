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

## 2026-05-01 — Pre-Market (Friday)

**Macro**: Unable to fetch — see infra note below.
**Sector Leaders Today**: Unknown — research APIs blocked.
**Sector Laggards Today**: Unknown — research APIs blocked.
**Key News**: Unknown — Perplexity API call returned `HTTP 403: Host not in allowlist`.
**Earnings This Week**: Unknown.
**Watchlist Review**: None — no data to screen against.
**Decision**: **Pass / No action.** Per CLAUDE.md guardrail: "If you are uncertain, do nothing and document why in memory/research-log.md."
**Confidence Level**: N/A.

**Infra note**: Sandbox network allowlist is blocking both `api.perplexity.ai` and Alpaca (`paper-api.alpaca.markets` / `api.alpaca.markets`). `scripts/perplexity_research.py --topic premarket` and `scripts/portfolio_snapshot.py` both failed with `HTTP 403: Host not in allowlist`. Until those hosts are allowlisted in the routine's sandbox config, pre-market research cannot run end-to-end from this environment. No ClickUp alert sent — this is an environment/config issue, not an urgent market event. Portfolio is 100% cash with zero open positions, so there is no risk exposure to manage in the meantime.

**One thing to try differently next session**: Before attempting research, verify network reachability to `api.perplexity.ai` and the Alpaca host implied by `ALPACA_BASE_URL`. If blocked, surface it as the first action item rather than running the full routine and discovering it mid-flow.

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
