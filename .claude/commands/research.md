Research the market using Perplexity API and update the research log.

## Steps

1. Run pre-market briefing:
   ```
   python scripts/perplexity_research.py --topic premarket
   ```

2. Run macro context check:
   ```
   python scripts/perplexity_research.py --topic macro
   ```

3. For each symbol on the watchlist in `memory/strategy.md`, run:
   ```
   python scripts/perplexity_research.py --topic stock --symbol <SYMBOL>
   ```

4. Research any sectors showing signals:
   ```
   python scripts/perplexity_research.py --topic sector --sector <SECTOR>
   ```

5. Synthesize all findings into a structured research entry and append to `memory/research-log.md` using the template in that file.

6. Identify 1–3 actionable trade candidates with your confidence level (High / Medium / Low).

## Output
- Updated `memory/research-log.md` with today's findings
- A short summary of top trade candidates for the session
