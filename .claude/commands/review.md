Conduct a comprehensive weekly review and send summary to ClickUp.

## Steps

1. Pull full account history for the week:
   ```
   python scripts/alpaca_client.py history 7
   python scripts/alpaca_client.py positions
   python scripts/alpaca_client.py account
   ```

2. Research S&P 500 performance this week:
   ```
   python scripts/perplexity_research.py "What was the S&P 500 (SPY) return percentage this week? What were the main market drivers?"
   ```

3. Calculate performance metrics:
   - Portfolio weekly return %
   - S&P 500 weekly return %
   - Alpha = Portfolio return - S&P return
   - Win rate on closed positions this week
   - Average gain on winners, average loss on losers

4. Review each trade made this week in `memory/trade-log.md`:
   - Was the thesis correct?
   - Was entry/exit timing good?
   - What would you do differently?

5. Review the strategy in `memory/strategy.md`:
   - Any rules that need updating?
   - Any new signals observed?

6. Write the weekly review using the template in `memory/weekly-review.md` and append it.

7. Update `memory/portfolio.md`:
   ```
   python scripts/portfolio_snapshot.py
   ```

8. Send the full weekly review to ClickUp:
   ```
   python scripts/clickup_notify.py --eod
   ```
   (pipe the review content to stdin)

9. Push all changes to GitHub:
   ```
   git add -A
   git commit -m "Weekly review $(date +%Y-%m-%d)"
   git push origin main
   ```

## Self-Grading Rubric

| Grade | Criteria |
|-------|----------|
| A | Beat S&P by >2%, all rules followed, clear lessons documented |
| B | Beat S&P by 0–2%, minor rule deviation, lessons documented |
| C | Matched S&P ±1%, some rules broken or lessons unclear |
| D | Underperformed S&P by 1–3%, significant rule violations |
| F | Underperformed by >3% or major risk management failure |
