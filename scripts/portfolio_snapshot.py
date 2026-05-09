#!/usr/bin/env python3
"""
Generate a full portfolio snapshot and update memory/portfolio.md.
Reads from Alpaca API and writes formatted state to memory/portfolio.md.

Usage:
    python scripts/portfolio_snapshot.py
    python scripts/portfolio_snapshot.py --print-only
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime


def get_headers():
    key = os.environ.get("ALPACA_API_KEY")
    secret = os.environ.get("ALPACA_SECRET_KEY")
    if not key or not secret:
        print("ERROR: ALPACA_API_KEY and ALPACA_SECRET_KEY must be set as environment variables.")
        sys.exit(1)
    return {
        "APCA-API-KEY-ID": key,
        "APCA-API-SECRET-KEY": secret,
        "Content-Type": "application/json",
    }


def get_base_url():
    url = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
    return url.rstrip("/").removesuffix("/v2")


def api_get(path):
    url = f"{get_base_url()}{path}"
    req = urllib.request.Request(url, headers=get_headers(), method="GET")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()}")
        sys.exit(1)


def generate_snapshot():
    account = api_get("/v2/account")
    positions = api_get("/v2/positions")
    orders = api_get("/v2/orders?status=open")

    equity = float(account.get("equity", 0))
    cash = float(account.get("cash", 0))
    buying_power = float(account.get("buying_power", 0))

    now = datetime.now().strftime("%Y-%m-%d %H:%M ET")

    lines = [
        "# Portfolio State",
        "",
        f"_Last updated: {now}_",
        "",
        "## Account Summary",
        f"- **Mode**: {'Paper Trading' if 'paper' in get_base_url() else 'Live Trading'}",
        f"- **Current Equity**: ${equity:,.2f}",
        f"- **Cash**: ${cash:,.2f}",
        f"- **Buying Power**: ${buying_power:,.2f}",
        "",
        "## Open Positions",
        "",
        "| Symbol | Shares | Avg Cost | Current Price | Market Value | P&L | P&L % | Notes |",
        "|--------|--------|----------|---------------|--------------|-----|--------|-------|",
    ]

    if positions:
        for p in positions:
            symbol = p.get("symbol", "")
            qty = p.get("qty", "0")
            avg = float(p.get("avg_entry_price", 0))
            cur = float(p.get("current_price", 0))
            mv = float(p.get("market_value", 0))
            upl = float(p.get("unrealized_pl", 0))
            uplpc = float(p.get("unrealized_plpc", 0)) * 100
            lines.append(
                f"| {symbol} | {qty} | ${avg:.2f} | ${cur:.2f} | ${mv:,.2f} | "
                f"${upl:+.2f} | {uplpc:+.1f}% | |"
            )
    else:
        lines.append("| — | — | — | — | — | — | — | No positions |")

    lines += ["", "## Pending Orders"]
    if orders:
        for o in orders:
            lines.append(
                f"- {o.get('side', '').upper()} {o.get('qty')} {o.get('symbol')} "
                f"| Type: {o.get('type')} | Status: {o.get('status')}"
            )
    else:
        lines.append("_None_")

    equity_pct = (equity / 10000.0 - 1) * 100
    cash_pct = (cash / equity * 100) if equity > 0 else 100
    equity_alloc_pct = 100 - cash_pct

    lines += [
        "",
        "## Allocation Summary",
        f"- Cash: {cash_pct:.1f}%",
        f"- Equities: {equity_alloc_pct:.1f}%",
        f"- Total Return vs Start ($10,000): {equity_pct:+.2f}%",
        f"- Open positions: {len(positions)} / 5 max",
    ]

    return "\n".join(lines)


def main():
    snapshot = generate_snapshot()
    print_only = "--print-only" in sys.argv

    if print_only:
        print(snapshot)
    else:
        output_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "memory",
            "portfolio.md",
        )
        with open(output_path, "w") as f:
            f.write(snapshot)
        print(f"Portfolio snapshot written to {output_path}")
        print(snapshot)


if __name__ == "__main__":
    main()
