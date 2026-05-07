#!/usr/bin/env python3
"""
Perplexity API client for Bull trading agent research.
Reads PERPLEXITY_API_KEY from environment variables.

Usage:
    python scripts/perplexity_research.py "What is the current market outlook for NVDA?"
    python scripts/perplexity_research.py --topic premarket
    python scripts/perplexity_research.py --topic sector --sector technology
    python scripts/perplexity_research.py --topic stock --symbol AAPL
    python scripts/perplexity_research.py --topic macro
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import date


PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"


def get_api_key():
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key:
        print("ERROR: PERPLEXITY_API_KEY must be set as an environment variable.")
        sys.exit(1)
    return key


def query(prompt, model="sonar"):
    """Send a research query to Perplexity and return the response."""
    headers = {
        "Authorization": f"Bearer {get_api_key()}",
        "Content-Type": "application/json",
    }
    body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a financial research assistant helping a quantitative trading agent. "
                    "Provide concise, factual, data-driven answers. Focus on: recent earnings, "
                    "analyst ratings, price catalysts, sector trends, and macro signals. "
                    "Always cite sources when possible. Be brief and structured."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "return_citations": True,
        "search_recency_filter": "day",
    }

    data = json.dumps(body).encode()
    req = urllib.request.Request(PERPLEXITY_API_URL, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode())
            content = result["choices"][0]["message"]["content"]
            citations = result.get("citations", [])
            print(content)
            if citations:
                print("\n--- Sources ---")
                for i, c in enumerate(citations[:5], 1):
                    print(f"{i}. {c}")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()}")
        sys.exit(1)


def _today():
    return date.today().strftime("%B %d, %Y")

TOPIC_PROMPTS = {
    "premarket": (
        f"Today is {_today()}. Give me a concise pre-market briefing for TODAY's US stock market. "
        "All data must be from today — do not use data from prior days. Include: "
        "1) S&P 500 and Nasdaq futures direction right now, "
        "2) Top 3 pre-market movers (up and down) as of this morning, "
        "3) Key economic data releases scheduled for today, "
        "4) Overnight news that could move markets today, "
        "5) VIX level as of this morning and what it signals. "
        "If you are uncertain about any live figure, say so explicitly rather than guessing. "
        "Format as bullet points."
    ),
    "macro": (
        f"Today is {_today()}. What is the current US macroeconomic environment as of today? Cover: "
        "Fed rate stance and next meeting outlook, "
        "inflation trend (CPI/PCE latest), "
        "10-year treasury yield trend, "
        "USD strength, "
        "recession risk signals. "
        "Keep it brief and actionable for a swing trader."
    ),
}

SECTOR_PROMPT = (
    "Analyze the current state of the {sector} sector. Include: "
    "1) Is the sector ETF above or below its 50-day SMA? "
    "2) Top performing stocks in the sector this week, "
    "3) Any major news (earnings, regulation, macro tailwinds/headwinds), "
    "4) Institutional flow signals, "
    "5) One actionable insight for a swing trader. "
    "Be concise."
)

STOCK_PROMPT = (
    "Give me a comprehensive but brief research summary on {symbol} stock. Include: "
    "1) Most recent earnings result (beat/miss/in-line), "
    "2) Revenue and EPS growth YoY, "
    "3) Current analyst consensus and price target, "
    "4) Any recent news (past 7 days) that could move the stock, "
    "5) Technical summary: above/below 50-day and 200-day SMA? "
    "6) Any insider buying/selling in past 30 days? "
    "Rate the setup as: Strong Buy / Buy / Neutral / Avoid."
)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    if args[0] == "--topic":
        topic = args[1] if len(args) > 1 else ""
        if topic == "premarket":
            query(TOPIC_PROMPTS["premarket"])
        elif topic == "macro":
            query(TOPIC_PROMPTS["macro"])
        elif topic == "sector":
            sector = args[3] if len(args) > 3 and args[2] == "--sector" else "technology"
            query(SECTOR_PROMPT.format(sector=sector))
        elif topic == "stock":
            symbol = args[3] if len(args) > 3 and args[2] == "--symbol" else "SPY"
            query(STOCK_PROMPT.format(symbol=symbol))
        else:
            print(f"Unknown topic: {topic}")
            print(__doc__)
    else:
        # Free-form query
        query(" ".join(args))


if __name__ == "__main__":
    main()
