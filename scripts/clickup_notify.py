#!/usr/bin/env python3
"""
ClickUp notification sender for Bull trading agent.
Reads CLICKUP_API_TOKEN and CLICKUP_LIST_ID from environment variables.

Usage:
    python scripts/clickup_notify.py --title "Title" --body "Message body"
    python scripts/clickup_notify.py --eod  # end of day summary (reads from stdin)
    python scripts/clickup_notify.py --alert "STOP HIT: AAPL -7.2%"
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime


CLICKUP_API_URL = "https://api.clickup.com/api/v2"


def get_credentials():
    token = os.environ.get("CLICKUP_API_TOKEN")
    list_id = os.environ.get("CLICKUP_LIST_ID")
    if not token or not list_id:
        print("ERROR: CLICKUP_API_TOKEN and CLICKUP_LIST_ID must be set as environment variables.")
        sys.exit(1)
    list_id = list_id.split("?", 1)[0].split("/", 1)[0].strip()
    return token, list_id


def create_task(title, body, priority=3):
    """
    Create a ClickUp task as a notification.
    priority: 1=urgent, 2=high, 3=normal, 4=low
    """
    token, list_id = get_credentials()
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    payload = {
        "name": title,
        "description": body,
        "priority": priority,
        "status": "to do",
        "tags": ["bull-trading-agent"],
    }
    data = json.dumps(payload).encode()
    url = f"{CLICKUP_API_URL}/list/{list_id}/task"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode())
            task_url = result.get("url", "")
            print(f"ClickUp task created: {result.get('name')} — {task_url}")
    except urllib.error.HTTPError as e:
        print(f"ClickUp HTTP {e.code}: {e.read().decode()}")
        sys.exit(1)


def format_eod_summary(portfolio_value, cash, positions, spy_return, day_pnl, day_pnl_pct, notes=""):
    date_str = datetime.now().strftime("%Y-%m-%d %A")
    lines = [
        f"# Bull Trading Agent — EOD Summary {date_str}",
        "",
        f"## Portfolio",
        f"- **Total Value**: ${portfolio_value:,.2f}",
        f"- **Cash**: ${cash:,.2f}",
        f"- **Day P&L**: ${day_pnl:+,.2f} ({day_pnl_pct:+.2f}%)",
        f"- **SPY Today**: {spy_return:+.2f}%",
        f"- **Alpha Today**: {day_pnl_pct - spy_return:+.2f}%",
        "",
        "## Open Positions",
    ]
    if positions:
        for p in positions:
            lines.append(
                f"- {p['symbol']}: {p['qty']} shares @ {p['avg_cost']} | "
                f"Current: {p['current']} | P&L: {p['pnl_pct']:+.1f}%"
            )
    else:
        lines.append("- No open positions")

    if notes:
        lines += ["", "## Notes", notes]

    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    if "--alert" in args:
        idx = args.index("--alert")
        message = args[idx + 1] if idx + 1 < len(args) else "Alert from Bull"
        create_task(
            title=f"🚨 Bull Alert: {message}",
            body=message,
            priority=1,
        )
    elif "--eod" in args:
        # Read body from stdin or remaining args
        body = sys.stdin.read() if not sys.stdin.isatty() else " ".join(args[args.index("--eod") + 1:])
        date_str = datetime.now().strftime("%Y-%m-%d")
        create_task(
            title=f"Bull EOD Summary — {date_str}",
            body=body,
            priority=3,
        )
    elif "--title" in args and "--body" in args:
        title_idx = args.index("--title")
        body_idx = args.index("--body")
        title = args[title_idx + 1]
        body = args[body_idx + 1]
        create_task(title=title, body=body)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
