"""
Bull-Bot Watchlist-Backtest
Testet alle Watchlist-Symbole mit der Bull-Momentum-Strategie (2022-2024)
und gibt eine Vergleichstabelle aus.

Watchlist anpassen: WATCHLIST-Liste unten bearbeiten
"""

import os, json, math, sys, time
from datetime import date
from pathlib import Path

try:
    import requests
    import pandas as pd
    import numpy as np
except ImportError:
    sys.exit("Fehlende Pakete. Bitte ausführen: pip install requests pandas numpy")

# ── Konfiguration ─────────────────────────────────────────────────────────────
WATCHLIST = ["AAPL", "MSFT", "NVDA", "JPM", "LLY", "V", "AVGO", "BAC", "XOM"]
BENCHMARK    = "SPY"
DATA_START   = "2021-06-01"   # Warmup für EMA200
BACKTEST_START = date(2022, 1, 1)
DATA_END     = "2024-12-31"
INITIAL_CASH = 100_000.0
POSITION_PCT = 0.10
SLIPPAGE_PCT = 0.005
RUN_DIR      = Path(__file__).parent

# ── API-Setup ─────────────────────────────────────────────────────────────────
API_KEY    = os.environ.get("ALPACA_API_KEY")
SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY")

if not API_KEY or not SECRET_KEY:
    sys.exit("FEHLER: ALPACA_API_KEY und ALPACA_SECRET_KEY müssen als Env-Vars gesetzt sein.")

HEADERS  = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}
DATA_URL = "https://data.alpaca.markets"


def fetch_bars(symbol: str) -> pd.DataFrame:
    bars, token = [], None
    while True:
        params = {
            "timeframe": "1Day",
            "start": DATA_START,
            "end": DATA_END,
            "feed": "sip",
            "adjustment": "split",
            "limit": 1000,
        }
        if token:
            params["page_token"] = token
        r = requests.get(
            f"{DATA_URL}/v2/stocks/{symbol}/bars",
            headers=HEADERS, params=params
        )
        r.raise_for_status()
        data = r.json()
        bars.extend(data.get("bars", []))
        token = data.get("next_page_token")
        if not token:
            break
    df = pd.DataFrame(bars)
    df["t"] = pd.to_datetime(df["t"]).dt.tz_convert("US/Eastern").dt.date
    df = df.rename(columns={"t": "date", "o": "open", "h": "high",
                             "l": "low", "c": "close", "v": "volume"})
    return df.set_index("date").sort_index()[["open", "high", "low", "close", "volume"]]


def calc_ema(s, span):
    return s.ewm(span=span, adjust=False).mean()


def calc_rsi(s, period=14):
    delta = s.diff()
    gain  = delta.clip(lower=0)
    loss  = -delta.clip(upper=0)
    ag = gain.ewm(alpha=1/period, adjust=False).mean()
    al = loss.ewm(alpha=1/period, adjust=False).mean()
    return 100 - (100 / (1 + ag / al.replace(0, np.nan)))


def run_backtest(symbol: str, bars: pd.DataFrame, spy_bars: pd.DataFrame) -> dict:
    df = bars.copy()
    df["ema50"]    = calc_ema(df["close"], 50)
    df["ema200"]   = calc_ema(df["close"], 200)
    df["rsi14"]    = calc_rsi(df["close"])
    df["vol_ratio"] = df["volume"] / df["volume"].rolling(20).mean()
    df["ret63"]    = df["close"].pct_change(63)
    spy_r          = spy_bars["close"].pct_change(63).reindex(df.index)
    df["rs_vs_spy"] = df["ret63"] - spy_r
    df["high_52w"]  = df["close"].rolling(252).max()

    sim    = df[df.index >= BACKTEST_START].copy()
    dates  = sim.index.tolist()

    cash, shares, entry, sold_half = INITIAL_CASH, 0, 0.0, False
    trades, equity_list = [], []

    for i, d in enumerate(dates):
        row = sim.loc[d]
        equity_list.append(cash + shares * row["close"])

        if i + 1 >= len(dates):
            continue
        next_d   = dates[i + 1]
        next_row = sim.loc[next_d]
        nf_buy   = round(next_row["open"] * (1 + SLIPPAGE_PCT), 4)
        nf_sell  = round(next_row["open"] * (1 - SLIPPAGE_PCT), 4)

        in_pos = shares > 0

        if in_pos:
            reason, qty_sell, market = None, shares, False

            if row["close"] <= entry * 0.92:
                reason, market = "V1", True
            elif not pd.isna(row["high_52w"]) and row["close"] <= row["high_52w"] * 0.88:
                reason, market = "V2", True
            elif not sold_half and row["close"] >= entry * 1.20:
                reason, qty_sell = "V3", shares // 2
            elif sold_half and row["close"] >= entry * 1.35:
                reason = "V4"
            elif row["ema50"] < row["ema200"]:
                reason = "V5"
            elif row["rsi14"] > 80 and row["rs_vs_spy"] < 0:
                reason = "V6"

            if reason:
                fp = row["close"] if market else nf_sell
                pnl = (fp - entry) * qty_sell
                cash += qty_sell * fp
                shares -= qty_sell
                trades.append({"side": "sell", "pnl": pnl, "reason": reason,
                                "date": str(d if market else next_d)})
                if reason == "V3":
                    sold_half = True
                else:
                    sold_half, entry = False, 0.0

        if not in_pos:
            k1 = row["ema50"] > row["ema200"]
            k2 = 50 <= row["rsi14"] <= 70
            k3 = row["rs_vs_spy"] > 0
            k4 = row["vol_ratio"] >= 1.20
            if k1 and k2 and k3 and k4:
                if cash - INITIAL_CASH * POSITION_PCT >= INITIAL_CASH * 0.20:
                    qty = int(INITIAL_CASH * POSITION_PCT / nf_buy)
                    if qty > 0:
                        cash -= qty * nf_buy
                        shares, entry, sold_half = qty, nf_buy, False
                        trades.append({"side": "buy", "pnl": 0, "reason": "K1-K4",
                                       "date": str(next_d)})

    final_equity = cash + shares * sim.iloc[-1]["close"]
    total_ret    = (final_equity - INITIAL_CASH) / INITIAL_CASH * 100
    n_years      = (sim.index[-1] - sim.index[0]).days / 365.25
    ann_ret      = ((final_equity / INITIAL_CASH) ** (1 / n_years) - 1) * 100

    eq = pd.Series(equity_list, dtype=float)
    dd = ((eq - eq.cummax()) / eq.cummax() * 100).min()
    dr = eq.pct_change().dropna()
    sharpe = (dr.mean() / dr.std() * math.sqrt(252)) if dr.std() > 0 else 0.0

    sells    = [t for t in trades if t["side"] == "sell"]
    buys     = [t for t in trades if t["side"] == "buy"]
    wins     = [t for t in sells if t["pnl"] > 0]
    losses   = [t for t in sells if t["pnl"] <= 0]
    win_rate = len(wins) / len(sells) * 100 if sells else 0.0
    gp       = sum(t["pnl"] for t in wins)
    gl       = abs(sum(t["pnl"] for t in losses))
    pf       = gp / gl if gl > 0 else float("inf")

    return {
        "symbol":       symbol,
        "total_ret":    round(total_ret, 2),
        "ann_ret":      round(ann_ret, 2),
        "max_dd":       round(dd, 2),
        "sharpe":       round(sharpe, 3),
        "final_equity": round(final_equity, 2),
        "n_buys":       len(buys),
        "n_sells":      len(sells),
        "win_rate":     round(win_rate, 1),
        "profit_factor": round(pf, 2),
        "trades":       trades,
    }


# ── Haupt-Run ─────────────────────────────────────────────────────────────────
print("\n" + "="*70)
print("  BULL-BOT WATCHLIST-BACKTEST — 2022-01-01 bis 2024-12-31")
print("="*70)

# SPY einmal fetchen (Benchmark + RS-Berechnung)
print(f"\n  Lade SPY (Benchmark + RS-Basis) ...")
spy_bars = fetch_bars("SPY")
spy_sim  = spy_bars[spy_bars.index >= BACKTEST_START]
spy_start_price = spy_sim.iloc[0]["open"] * (1 + SLIPPAGE_PCT)
spy_shares_bh   = int(INITIAL_CASH / spy_start_price)
spy_final       = float(spy_shares_bh * spy_sim.iloc[-1]["close"]
                        + (INITIAL_CASH - spy_shares_bh * spy_start_price))
spy_ret         = (spy_final - INITIAL_CASH) / INITIAL_CASH * 100
spy_eq          = spy_shares_bh * spy_sim["close"] + (INITIAL_CASH - spy_shares_bh * spy_start_price)
spy_dr          = spy_eq.pct_change().dropna()
spy_sharpe      = (spy_dr.mean() / spy_dr.std() * math.sqrt(252)) if spy_dr.std() > 0 else 0.0

results = []
for symbol in WATCHLIST:
    print(f"  [{WATCHLIST.index(symbol)+1}/{len(WATCHLIST)}] {symbol} ...", end=" ", flush=True)
    try:
        bars = fetch_bars(symbol)
        res  = run_backtest(symbol, bars, spy_bars)
        results.append(res)
        print(f"Return {res['total_ret']:+.1f}% | Sharpe {res['sharpe']:.2f} | "
              f"Trades {res['n_buys']} | WinRate {res['win_rate']:.0f}%")
    except Exception as e:
        print(f"FEHLER: {e}")
    time.sleep(0.3)  # Rate-Limit schonen

# ── Ergebnisse sortieren und ausgeben ─────────────────────────────────────────
results.sort(key=lambda x: x["sharpe"], reverse=True)

print("\n" + "="*70)
print("  ERGEBNIS-VERGLEICH (sortiert nach Sharpe)")
print("="*70)
print(f"\n  {'Symbol':7s} {'Return':>8s} {'Ann.Ret':>8s} {'MaxDD':>8s} "
      f"{'Sharpe':>7s} {'Trades':>7s} {'WinRate':>8s} {'ProfFact':>9s}")
print("  " + "-"*68)

for r in results:
    vs_spy = r["total_ret"] - spy_ret
    flag   = " ✓" if r["sharpe"] > spy_sharpe else ""
    print(f"  {r['symbol']:7s} {r['total_ret']:>+7.1f}%  {r['ann_ret']:>+6.1f}%  "
          f"{r['max_dd']:>7.1f}%  {r['sharpe']:>6.3f}  {r['n_buys']:>6d}  "
          f"{r['win_rate']:>7.1f}%  {r['profit_factor']:>8.2f}{flag}")

print("  " + "-"*68)
print(f"  {'SPY B&H':7s} {spy_ret:>+7.1f}%  {'—':>7s}  {'—':>8s}  "
      f"{spy_sharpe:>6.3f}  {'—':>6s}  {'—':>7s}  {'—':>8s}  ← Benchmark")
print(f"\n  ✓ = Sharpe besser als SPY Buy-and-Hold ({spy_sharpe:.3f})")

# ── CSV speichern ──────────────────────────────────────────────────────────────
summary_df = pd.DataFrame([{
    "symbol":        r["symbol"],
    "total_ret_pct": r["total_ret"],
    "ann_ret_pct":   r["ann_ret"],
    "max_dd_pct":    r["max_dd"],
    "sharpe":        r["sharpe"],
    "n_trades":      r["n_buys"],
    "win_rate_pct":  r["win_rate"],
    "profit_factor": r["profit_factor"],
    "final_equity":  r["final_equity"],
    "vs_spy_pct":    round(r["total_ret"] - spy_ret, 2),
} for r in results])

csv_path = RUN_DIR / "watchlist_summary.csv"
summary_df.to_csv(csv_path, index=False)

print(f"\n  Ergebnisse gespeichert: {csv_path}")
print("\n  WICHTIG: Hypothetische Simulation — keine echte Trading-Performance.")
print("  Details: https://alpaca.markets/disclosures")
print("="*70 + "\n")
