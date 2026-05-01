Execute trades via the Alpaca API based on researched signals.

## Pre-Trade Checklist (run through every item before placing ANY order)

1. Read `memory/portfolio.md` — confirm current cash, open positions count, and weekly trade count
2. Confirm: open positions < 5 (max 5 at a time)
3. Confirm: new positions this week < 3 (max 3/week)
4. Confirm: VIX < 25 (if VIX > 25, only close positions, do not open new ones)
5. Confirm: position size ≤ 5% of total portfolio value
6. Confirm: you have a written thesis in `memory/research-log.md` for this trade

## Placing a Buy Order

```bash
# Check account balance first
python scripts/alpaca_client.py account

# Place a limit buy (preferred over market orders)
python scripts/alpaca_client.py buy <SYMBOL> <SHARES> limit <PRICE>

# Immediately set 10% trailing stop after fill
python scripts/alpaca_client.py trailing-stop <SYMBOL> 10
```

## Placing a Sell Order

```bash
# Sell all shares of a position
python scripts/alpaca_client.py sell <SYMBOL> <SHARES> market

# Or use a limit sell
python scripts/alpaca_client.py sell <SYMBOL> <SHARES> limit <PRICE>
```

## After Every Trade

1. Log the trade to `memory/trade-log.md`:
   - Date, symbol, action, shares, price, reason, confidence level
2. Update `memory/portfolio.md` by running:
   ```
   python scripts/portfolio_snapshot.py
   ```
3. Send ClickUp notification if a trade was placed:
   ```
   python scripts/clickup_notify.py --title "Bull Trade: BUY <SYMBOL>" --body "<details>"
   ```

## Risk Rules (Hard Stops — Never Skip)
- Never open a position >5% of portfolio value
- Never trade in the last 15 minutes before market close (3:45 PM ET)
- If portfolio is down >10% from starting value, pause all new buys immediately
- Always set trailing stop within the same session as the buy
