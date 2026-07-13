#!/usr/bin/env python3
"""
Alpaca API client for Bull trading agent.
All credentials are read from environment variables — never hardcoded.

Usage examples:
    python scripts/alpaca_client.py account
    python scripts/alpaca_client.py positions
    python scripts/alpaca_client.py orders
    python scripts/alpaca_client.py buy AAPL 5 limit 180.00
    python scripts/alpaca_client.py sell AAPL 5 market
    python scripts/alpaca_client.py trailing-stop AAPL 10
    python scripts/alpaca_client.py cancel <order_id>
    python scripts/alpaca_client.py history 30
    python scripts/alpaca_client.py bars NVDA 60
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta


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


def api_request(method, path, body=None):
    url = f"{get_base_url()}{path}"
    headers = get_headers()
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"HTTP {e.code} error: {error_body}")
        sys.exit(1)


def get_account():
    account = api_request("GET", "/v2/account")
    print(json.dumps({
        "equity": account.get("equity"),
        "cash": account.get("cash"),
        "buying_power": account.get("buying_power"),
        "portfolio_value": account.get("portfolio_value"),
        "daytrade_count": account.get("daytrade_count"),
        "status": account.get("status"),
        "trading_blocked": account.get("trading_blocked"),
    }, indent=2))


def get_positions():
    positions = api_request("GET", "/v2/positions")
    if not positions:
        print("No open positions.")
        return
    for p in positions:
        print(json.dumps({
            "symbol": p.get("symbol"),
            "qty": p.get("qty"),
            "avg_entry_price": p.get("avg_entry_price"),
            "current_price": p.get("current_price"),
            "market_value": p.get("market_value"),
            "unrealized_pl": p.get("unrealized_pl"),
            "unrealized_plpc": float(p.get("unrealized_plpc", 0)) * 100,
            "side": p.get("side"),
        }, indent=2))


def get_orders():
    orders = api_request("GET", "/v2/orders?status=open")
    if not orders:
        print("No open orders.")
        return
    for o in orders:
        print(json.dumps({
            "id": o.get("id"),
            "symbol": o.get("symbol"),
            "qty": o.get("qty"),
            "side": o.get("side"),
            "type": o.get("type"),
            "limit_price": o.get("limit_price"),
            "trail_percent": o.get("trail_percent"),
            "status": o.get("status"),
            "created_at": o.get("created_at"),
        }, indent=2))


def place_order(symbol, qty, side, order_type, limit_price=None):
    body = {
        "symbol": symbol.upper(),
        "qty": str(qty),
        "side": side,
        "type": order_type,
        "time_in_force": "day",
    }
    if order_type == "limit" and limit_price:
        body["limit_price"] = str(limit_price)

    order = api_request("POST", "/v2/orders", body)
    print(json.dumps({
        "id": order.get("id"),
        "symbol": order.get("symbol"),
        "qty": order.get("qty"),
        "side": order.get("side"),
        "type": order.get("type"),
        "status": order.get("status"),
        "filled_avg_price": order.get("filled_avg_price"),
    }, indent=2))


def set_trailing_stop(symbol, trail_percent):
    """Set a trailing stop order for an existing position."""
    positions = api_request("GET", "/v2/positions")
    pos = next((p for p in positions if p["symbol"] == symbol.upper()), None)
    if not pos:
        print(f"No open position found for {symbol}")
        sys.exit(1)

    qty = pos["qty"]
    body = {
        "symbol": symbol.upper(),
        "qty": qty,
        "side": "sell",
        "type": "trailing_stop",
        "time_in_force": "gtc",
        "trail_percent": str(trail_percent),
    }
    order = api_request("POST", "/v2/orders", body)
    print(json.dumps({
        "id": order.get("id"),
        "symbol": order.get("symbol"),
        "qty": order.get("qty"),
        "trail_percent": order.get("trail_percent"),
        "status": order.get("status"),
    }, indent=2))


def cancel_order(order_id):
    api_request("DELETE", f"/v2/orders/{order_id}")
    print(f"Order {order_id} cancelled.")


def get_bars(symbol, window=60):
    """Fetch daily bars for a symbol and print latest close + 50DSMA + gap.

    Uses Alpaca market data API (data.alpaca.markets). Returns the last `window`
    trading days; computes 50-day simple moving average when >=50 bars available.
    """
    window = int(window)
    # Alpaca's IEX feed requires explicit start/end; `limit` alone returns empty.
    # Pad calendar days to cover weekends/holidays: ~1.5x trading days + buffer.
    calendar_days = int(window * 1.7) + 10
    start = (datetime.utcnow() - timedelta(days=calendar_days)).strftime("%Y-%m-%d")
    end = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
    data_url = (
        f"https://data.alpaca.markets/v2/stocks/{symbol.upper()}/bars"
        f"?timeframe=1Day&start={start}&end={end}&feed=iex&limit=1000&adjustment=raw"
    )
    req = urllib.request.Request(data_url, headers=get_headers(), method="GET")
    try:
        with urllib.request.urlopen(req) as resp:
            payload = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} error: {e.read().decode()}")
        sys.exit(1)

    bars = payload.get("bars") or []
    if not bars:
        print(json.dumps({"symbol": symbol.upper(), "error": "no bars returned"}, indent=2))
        return

    closes = [float(b["c"]) for b in bars]
    latest = bars[-1]
    latest_close = float(latest["c"])
    sma50 = sum(closes[-50:]) / 50 if len(closes) >= 50 else None
    gap_pct = ((latest_close / sma50) - 1) * 100 if sma50 else None

    print(json.dumps({
        "symbol": symbol.upper(),
        "bars_returned": len(bars),
        "latest_date": latest.get("t", "")[:10],
        "latest_close": round(latest_close, 4),
        "sma50": round(sma50, 4) if sma50 else None,
        "gap_pct_vs_sma50": round(gap_pct, 2) if gap_pct is not None else None,
        "reconnect_status": ("ABOVE" if sma50 and latest_close >= sma50 else ("BELOW" if sma50 else "insufficient_bars")),
    }, indent=2))


def get_history(days=30):
    end = datetime.utcnow().strftime("%Y-%m-%d")
    start = (datetime.utcnow() - timedelta(days=int(days))).strftime("%Y-%m-%d")
    activities = api_request("GET", f"/v2/account/activities/FILL?after={start}T00:00:00Z&until={end}T23:59:59Z")
    if not activities:
        print("No filled orders in this period.")
        return
    for a in activities:
        print(json.dumps({
            "date": a.get("transaction_time", "")[:10],
            "symbol": a.get("symbol"),
            "side": a.get("side"),
            "qty": a.get("qty"),
            "price": a.get("price"),
            "type": a.get("type"),
        }, indent=2))


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    cmd = args[0].lower()

    if cmd == "account":
        get_account()
    elif cmd == "positions":
        get_positions()
    elif cmd == "orders":
        get_orders()
    elif cmd == "buy":
        # buy SYMBOL QTY [market|limit] [PRICE]
        symbol, qty = args[1], args[2]
        order_type = args[3] if len(args) > 3 else "market"
        price = args[4] if len(args) > 4 else None
        place_order(symbol, qty, "buy", order_type, price)
    elif cmd == "sell":
        symbol, qty = args[1], args[2]
        order_type = args[3] if len(args) > 3 else "market"
        price = args[4] if len(args) > 4 else None
        place_order(symbol, qty, "sell", order_type, price)
    elif cmd == "trailing-stop":
        symbol, trail_pct = args[1], args[2]
        set_trailing_stop(symbol, trail_pct)
    elif cmd == "cancel":
        cancel_order(args[1])
    elif cmd == "history":
        days = args[1] if len(args) > 1 else 30
        get_history(days)
    elif cmd == "bars":
        symbol = args[1]
        window = args[2] if len(args) > 2 else 60
        get_bars(symbol, window)
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
