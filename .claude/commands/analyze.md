Analyze current portfolio performance and positions.

## Steps

1. Get current account status:
   ```
   python scripts/alpaca_client.py account
   ```

2. Get all open positions with P&L:
   ```
   python scripts/alpaca_client.py positions
   ```

3. Get open orders:
   ```
   python scripts/alpaca_client.py orders
   ```

4. For each open position, assess:
   - Is it up or down? By how much?
   - Is the original thesis still intact? (check with Perplexity if needed)
   - Should the trailing stop be tightened?
   - Are we at a +15% target (partial profit taking) or -7% cut level?

5. Midday specific actions:
   - **Cut** any position down > -7% immediately (market sell)
   - **Tighten** trailing stop on winners (reduce from 10% to 5% if up > 15%)
   - **Take partial profits** on positions up > 15% (sell half)

6. Update `memory/portfolio.md`:
   ```
   python scripts/portfolio_snapshot.py
   ```

7. Log analysis findings to `memory/research-log.md`.

## Decision Framework

| Condition | Action |
|-----------|--------|
| Position down > 7% | Sell immediately — no exceptions |
| Position up > 15% | Sell half, tighten stop to 5% |
| Position up > 25% | Exit fully or hold with 5% trailing stop |
| Original thesis broken | Sell regardless of P&L |
| VIX spikes > 30 | Reduce all positions by 25% |
