# Bull — 24/7 AI Trading Agent

A Claude Code Routines-based trading agent that runs on a schedule, researches markets, places trades via Alpaca, and sends daily summaries to ClickUp.

## Architecture

```
routines/
├── CLAUDE.md                    # Bull's identity, strategy, and hard rules
├── memory/
│   ├── strategy.md              # Trading strategy and signal criteria
│   ├── portfolio.md             # Current positions and account state (auto-updated)
│   ├── trade-log.md             # All trades with rationale (auto-updated)
│   ├── research-log.md          # Daily research findings (auto-updated)
│   └── weekly-review.md         # Weekly performance reviews (auto-updated)
├── scripts/
│   ├── alpaca_client.py         # Alpaca API wrapper (account, orders, positions)
│   ├── perplexity_research.py   # Perplexity API wrapper (market research)
│   ├── clickup_notify.py        # ClickUp task creation for notifications
│   └── portfolio_snapshot.py    # Generates portfolio.md from live Alpaca data
├── .claude/
│   ├── settings.json            # Routines schedule + permissions config
│   └── commands/
│       ├── research.md          # /research slash command
│       ├── trade.md             # /trade slash command
│       ├── analyze.md           # /analyze slash command
│       └── review.md            # /review slash command
└── routines/
    ├── pre-market.md            # 6:00 AM ET Mon–Fri prompt
    ├── market-open.md           # 8:30 AM ET Mon–Fri prompt
    ├── midday.md                # 12:00 PM ET Mon–Fri prompt
    ├── market-close.md          # 3:00 PM ET Mon–Fri prompt
    └── weekly-review.md         # 4:00 PM ET Fridays prompt
```

## Schedule

| Routine | Time (ET) | Days | Purpose |
|---------|-----------|------|---------|
| Pre-Market | 6:00 AM | Mon–Fri | Research catalysts, draft trade plan |
| Market Open | 8:30 AM | Mon–Fri | Execute trades, set 10% trailing stops |
| Midday | 12:00 PM | Mon–Fri | Cut -7% losers, tighten stops on winners |
| Market Close | 3:00 PM | Mon–Fri | EOD review + ClickUp summary |
| Weekly Review | 4:00 PM | Fridays | Performance grade + strategy refinement |

## Setup

### 1. Required API Keys
Set these as environment variables in your Claude Code cloud environment (named `trading`):

```
ALPACA_API_KEY=<your alpaca key id>
ALPACA_SECRET_KEY=<your alpaca secret key>
ALPACA_BASE_URL=https://paper-api.alpaca.markets  # or live URL
PERPLEXITY_API_KEY=<your perplexity key>
CLICKUP_API_TOKEN=<your clickup token>
CLICKUP_LIST_ID=<your clickup list id>
```

**Never put these in files or commit them to git.**

### 2. Claude Code Desktop App
- Open this project in Claude Code Desktop
- Go to Routines → New Routine → Remote
- Set environment to `trading`
- Enable "Allow unrestricted branch pushes" for all 5 routines
- Model: `claude-opus-4-7`

### 3. GitHub Repo
This project must be in a GitHub repo for remote routines to persist memory. The agent commits and pushes memory file updates after every session so the next routine picks up where the last left off.

### 4. Paper Trading First
The default `ALPACA_BASE_URL` points to the paper trading API. Test for at least 2 weeks before switching to live money.

## Memory Architecture

Every routine wakes up stateless. Files are how Bull "remembers":

1. **Reads** all memory files at session start
2. **Does** the work (research, trade, analyze)
3. **Writes** updated memory files
4. **Pushes** to GitHub so the next session sees the updates

## Guardrails

- Max 5% per position
- Max 5 open positions
- Max 3 new positions per week
- 10% trailing stop on every position
- Cut positions at -7% midday
- Pause new buys if portfolio down >10% from start
- Never trade in last 15 minutes before close

## Objective

Beat the S&P 500 (SPY) on a rolling 90-day basis using fundamentals-driven swing trading.
