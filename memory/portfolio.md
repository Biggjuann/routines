# Portfolio State

_Last updated: 2026-05-08 19:09 UTC (3:09 PM ET)_

## Account Summary
- **Mode**: Paper Trading
- **Starting Value**: $10,000.00 (strategy reference); Alpaca paper account funded at $100,000
- **Current Equity**: $100,000.00
- **Current Cash**: $100,000.00
- **Buying Power**: $200,000.00
- **Total P&L (today)**: $0.00 (0.00%)
- **S&P 500 Benchmark Today**: ~ -0.59% (proxy via S&P 3% Capped Index TR; real-time confirm via Bloomberg/Yahoo)

## Open Positions

| Symbol | Shares | Avg Cost | Current Price | Market Value | P&L | P&L % | Stop Price | Notes |
|--------|--------|----------|---------------|--------------|-----|--------|------------|-------|
| — | — | — | — | — | — | — | — | No positions |

## Pending Orders
_None_

## Closed This Week
_None_

## Allocation Summary
- Cash: 100.0%
- Equities: 0.0%
- Open positions: 0 / 5 max
- Max new positions remaining this week: 3 (limit: 3/week)

## Notes
- Account `status: ACTIVE`, `trading_blocked: false`, `daytrade_count: 0`.
- Equity is reported as $100,000 in Alpaca paper — strategy doc tracks performance against a $10,000 reference; will continue using Alpaca equity for real performance attribution.
- No fills today — agent has not yet placed a real entry. Awaiting first signal from pre-market screener.
- `/v2/orders` endpoint returned HTTP 404 from this environment when called via `portfolio_snapshot.py`; logged in trade-log for follow-up. Other Alpaca endpoints (account, positions, history) responded normally.
