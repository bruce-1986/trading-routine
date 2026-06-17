"""
Bull-Bot Backtest: MSFT, Bull-Momentum-Strategie, 2022-01-01 bis 2024-12-31
Fetch: Alpaca REST API (ALPACA_API_KEY, ALPACA_SECRET_KEY aus Env-Vars)
Fill:  next_open + 0.5% Slippage
K5:    Annahme TRUE (MSFT Fundamentals erfüllen Kriterien im Backtest-Zeitraum)
"""

import os, json, math, sys
from datetime import date, timedelta
from pathlib import Path

try:
    import requests
    import pandas as pd
    import numpy as np
except ImportError:
    sys.exit("Fehlende Pakete. Bitte ausführen: pip install requests pandas numpy")

# ── Konfiguration ────────────────────────────────────────────────────────────
SYMBOL       = "MSFT"
BENCHMARK    = "SPY"
START        = "2021-06-01"   # früher start für EMA200-Warmup (~200 Handelstage)
BACKTEST_START = date(2022, 1, 1)
END          = "2024-12-31"
INITIAL_CASH = 100_000.0
POSITION_PCT = 0.10           # 10% pro Position
SLIPPAGE_PCT = 0.005          # 0.5%
RUN_DIR      = Path(__file__).parent

# ── API-Setup ────────────────────────────────────────────────────────────────
API_KEY    = os.environ.get("ALPACA_API_KEY")
SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY")

if not API_KEY or not SECRET_KEY:
    sys.exit("FEHLER: ALPACA_API_KEY und ALPACA_SECRET_KEY müssen als Env-Vars gesetzt sein.")

HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}
DATA_URL = "https://data.alpaca.markets"


def fetch_bars(symbol: str, start: str, end: str) -> pd.DataFrame:
    """Alle Tages-Bars für ein Symbol von Alpaca holen (paginiert)."""
    bars, token = [], None
    print(f"  Fetche {symbol} Bars {start} → {end} ...")
    while True:
        params = {
            "timeframe": "1Day", "start": start, "end": end,
            "feed": "sip", "adjustment": "split", "limit": 1000,
        }
        if token:
            params["page_token"] = token
        r = requests.get(f"{DATA_URL}/v2/stocks/{symbol}/bars", headers=HEADERS, params=params)
        r.raise_for_status()
        data = r.json()
        bars.extend(data.get("bars", []))
        token = data.get("next_page_token")
        if not token:
            break
    df = pd.DataFrame(bars)
    df["t"] = pd.to_datetime(df["t"]).dt.tz_convert("US/Eastern").dt.date
    df = df.rename(columns={"t": "date", "o": "open", "h": "high", "l": "low",
                             "c": "close", "v": "volume"})
    return df.set_index("date").sort_index()[["open", "high", "low", "close", "volume"]]


def calc_ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()


def calc_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain  = delta.clip(lower=0)
    loss  = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1/period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def calc_return_n(series: pd.Series, n: int) -> pd.Series:
    return series.pct_change(n)


# ── Daten holen ──────────────────────────────────────────────────────────────
print("\n[1/4] Marktdaten laden ...")
msft = fetch_bars(SYMBOL, START, END)
spy  = fetch_bars(BENCHMARK, START, END)
print(f"  MSFT: {len(msft)} Bars | SPY: {len(spy)} Bars")

# ── Indikatoren berechnen ────────────────────────────────────────────────────
print("[2/4] Indikatoren berechnen ...")
msft["ema50"]   = calc_ema(msft["close"], 50)
msft["ema200"]  = calc_ema(msft["close"], 200)
msft["rsi14"]   = calc_rsi(msft["close"], 14)
msft["vol_ratio"] = msft["volume"] / msft["volume"].rolling(20).mean()
msft["ret63"]   = calc_return_n(msft["close"], 63)
spy["ret63"]    = calc_return_n(spy["close"], 63)
msft["rs_vs_spy"] = msft["ret63"] - spy["ret63"].reindex(msft.index)
msft["52w_high"] = msft["close"].rolling(252).max()

# Nur Backtest-Zeitraum simulieren (Warmup-Daten verworfen)
sim = msft[msft.index >= BACKTEST_START].copy()

# ── Simulation ───────────────────────────────────────────────────────────────
print("[3/4] Simulation läuft ...")

cash      = INITIAL_CASH
shares    = 0
entry     = 0.0
sold_half = False      # V3 bereits ausgelöst
trades    = []
equity_curve = []

dates = sim.index.tolist()

for i, d in enumerate(dates):
    row = sim.loc[d]
    portfolio_value = cash + shares * row["close"]
    equity_curve.append({"date": str(d), "equity": round(portfolio_value, 2),
                          "cash": round(cash, 2), "shares": shares,
                          "close": row["close"]})

    # Nächste Bar für Fill (next_open)
    if i + 1 >= len(dates):
        continue
    next_d   = dates[i + 1]
    next_row = sim.loc[next_d]
    next_fill_buy  = round(next_row["open"] * (1 + SLIPPAGE_PCT), 2)
    next_fill_sell = round(next_row["open"] * (1 - SLIPPAGE_PCT), 2)  # sell ohne Aufschlag

    in_position = shares > 0

    # ── SELL-Prüfung (tagesend, same-bar für Stop-Loss V1/V2) ────────────────
    if in_position:
        sell_reason = None
        sell_qty    = shares
        use_market  = False  # Market = sofortig (same-bar Close), Limit = next_open

        # V1: -8% Stop (Close unterschreitet Schwelle → next_open sell)
        if row["close"] <= entry * 0.92:
            sell_reason, use_market = "V1 Stop-Loss -8%", True

        # V2: -12% Trailing Stop
        elif not pd.isna(row["52w_high"]) and row["close"] <= row["52w_high"] * 0.88:
            sell_reason, use_market = "V2 Trailing Stop -12%", True

        # V3: +20% → 50% verkaufen (nur wenn noch nicht verkauft)
        elif not sold_half and row["close"] >= entry * 1.20:
            sell_reason = "V3 TP1 +20%"
            sell_qty = shares // 2

        # V4: +35% → Rest verkaufen
        elif sold_half and row["close"] >= entry * 1.35:
            sell_reason = "V4 TP2 +35%"

        # V5: Death Cross
        elif row["ema50"] < row["ema200"]:
            sell_reason = "V5 Death Cross"

        # V6: RSI > 80 UND RS < 0
        elif row["rsi14"] > 80 and row["rs_vs_spy"] < 0:
            sell_reason = "V6 RSI>80 & RS<0"

        if sell_reason:
            fill_price = row["close"] if use_market else next_fill_sell
            proceeds   = sell_qty * fill_price
            cash      += proceeds
            shares    -= sell_qty
            pnl        = (fill_price - entry) * sell_qty

            trades.append({
                "date": str(next_d if not use_market else d),
                "side": "sell",
                "symbol": SYMBOL,
                "qty": sell_qty,
                "price": fill_price,
                "pnl": round(pnl, 2),
                "reason": sell_reason,
            })

            if sell_reason in ("V3 TP1 +20%",):
                sold_half = True
            elif sell_reason not in ("V3 TP1 +20%",):
                sold_half = False
                entry = 0.0

    # ── KAUF-Prüfung (kein Kauf wenn bereits in Position) ────────────────────
    if not in_position:
        # Kauffilter
        k1 = row["ema50"] > row["ema200"]
        k2 = 50 <= row["rsi14"] <= 70
        k3 = row["rs_vs_spy"] > 0
        k4 = row["vol_ratio"] >= 1.20
        k5 = True  # Annahme: MSFT erfüllt Fundamentalkriteria

        if k1 and k2 and k3 and k4 and k5:
            budget  = INITIAL_CASH * POSITION_PCT
            # Cash-Check: min. 20% Reserve
            if cash - budget >= INITIAL_CASH * 0.20:
                qty = int(budget / next_fill_buy)
                if qty > 0:
                    cost   = qty * next_fill_buy
                    cash  -= cost
                    shares = qty
                    entry  = next_fill_buy
                    sold_half = False
                    trades.append({
                        "date": str(next_d),
                        "side": "buy",
                        "symbol": SYMBOL,
                        "qty": qty,
                        "price": next_fill_buy,
                        "pnl": 0.0,
                        "reason": f"K1={k1} K2={k2} K3={k3} K4={k4} K5={k5}",
                    })

# ── Ergebnisse berechnen ─────────────────────────────────────────────────────
print("[4/4] Report erstellen ...")

equity_df = pd.DataFrame(equity_curve).set_index("date")
final_equity = cash + shares * sim.iloc[-1]["close"]

# Benchmark: SPY Buy-and-Hold mit gleichem Startkapital
spy_sim = spy[spy.index >= BACKTEST_START]
spy_start_price = spy_sim.iloc[0]["open"] * (1 + SLIPPAGE_PCT)
spy_shares      = int(INITIAL_CASH / spy_start_price)
spy_equity_curve = spy_shares * spy_sim["close"] + (INITIAL_CASH - spy_shares * spy_start_price)
spy_final        = float(spy_equity_curve.iloc[-1])

# Performance-Metriken
total_return   = (final_equity - INITIAL_CASH) / INITIAL_CASH * 100
spy_return     = (spy_final - INITIAL_CASH) / INITIAL_CASH * 100
n_years        = (sim.index[-1] - sim.index[0]).days / 365.25
ann_return     = ((final_equity / INITIAL_CASH) ** (1 / n_years) - 1) * 100

# Drawdown
eq_series   = pd.Series([e["equity"] for e in equity_curve])
rolling_max = eq_series.cummax()
drawdowns   = (eq_series - rolling_max) / rolling_max * 100
max_dd      = float(drawdowns.min())

# Daily Returns & Sharpe
eq_series_f = pd.Series([e["equity"] for e in equity_curve], dtype=float)
daily_ret   = eq_series_f.pct_change().dropna()
sharpe      = (daily_ret.mean() / daily_ret.std()) * math.sqrt(252) if daily_ret.std() > 0 else 0

# SPY Sharpe
spy_eq_daily = spy_equity_curve.pct_change().dropna()
spy_sharpe   = (spy_eq_daily.mean() / spy_eq_daily.std()) * math.sqrt(252) if spy_eq_daily.std() > 0 else 0

# Trade-Statistik
sell_trades  = [t for t in trades if t["side"] == "sell"]
buy_trades   = [t for t in trades if t["side"] == "buy"]
win_trades   = [t for t in sell_trades if t["pnl"] > 0]
lose_trades  = [t for t in sell_trades if t["pnl"] <= 0]
win_rate     = len(win_trades) / len(sell_trades) * 100 if sell_trades else 0
gross_profit = sum(t["pnl"] for t in win_trades)
gross_loss   = abs(sum(t["pnl"] for t in lose_trades))
profit_factor = gross_profit / gross_loss if gross_loss > 0 else float("inf")

first_trade  = trades[0] if trades else None
last_trade   = trades[-1] if trades else None

# ── Artifacts speichern ──────────────────────────────────────────────────────
trades_path = RUN_DIR / "trades.csv"
equity_path = RUN_DIR / "equity.csv"
summary_path = RUN_DIR / "summary.json"
bench_path  = RUN_DIR / "benchmark_equity.csv"

pd.DataFrame(trades).to_csv(trades_path, index=False)
equity_df.to_csv(equity_path)
spy_equity_curve.reset_index().rename(columns={0: "equity", "date": "date"}).to_csv(bench_path, index=False)

summary = {
    "symbol": SYMBOL, "start": str(BACKTEST_START), "end": END,
    "initial_cash": INITIAL_CASH, "final_equity": round(final_equity, 2),
    "total_return_pct": round(total_return, 2),
    "ann_return_pct": round(ann_return, 2),
    "max_drawdown_pct": round(max_dd, 2),
    "sharpe": round(sharpe, 3),
    "n_trades": len(buy_trades),
    "n_sell_trades": len(sell_trades),
    "win_rate_pct": round(win_rate, 1),
    "profit_factor": round(profit_factor, 2),
    "benchmark_return_pct": round(spy_return, 2),
    "benchmark_sharpe": round(spy_sharpe, 3),
    "k5_assumption": "TRUE (MSFT Fundamentals angenommen als erfuellt)",
    "fill_model": "next_open + 0.5% slippage",
    "feed": "sip, adjustment=split",
}
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2)

# ── Report ausgeben ──────────────────────────────────────────────────────────
print("\n" + "="*65)
print("  BULL-BOT BACKTEST REPORT — MSFT — 2022-01-01 bis 2024-12-31")
print("="*65)
print(f"\n{'':30s} {'Strategie':>12s}  {'SPY B&H':>10s}")
print(f"  {'Gesamt-Return':30s} {total_return:>11.2f}%  {spy_return:>9.2f}%")
print(f"  {'Ann. Return':30s} {ann_return:>11.2f}%  {(((spy_final/INITIAL_CASH)**(1/n_years)-1)*100):>9.2f}%")
print(f"  {'Max. Drawdown':30s} {max_dd:>11.2f}%")
print(f"  {'Sharpe Ratio':30s} {sharpe:>12.3f}  {spy_sharpe:>10.3f}")
print(f"  {'End-Kapital':30s} ${final_equity:>11,.2f}  ${spy_final:>9,.2f}")
print()
print(f"  Anzahl Käufe:         {len(buy_trades)}")
print(f"  Anzahl Verkäufe:      {len(sell_trades)}")
print(f"  Win Rate:             {win_rate:.1f}%")
print(f"  Profit Factor:        {profit_factor:.2f}")
if first_trade:
    print(f"  Erster Trade:         {first_trade['side'].upper()} {first_trade['qty']} @ ${first_trade['price']:.2f} ({first_trade['date']})")
if last_trade:
    print(f"  Letzter Trade:        {last_trade['side'].upper()} {last_trade['qty']} @ ${last_trade['price']:.2f} ({last_trade['date']})")
print()
print("  ANNAHMEN:")
print("  - K5 = TRUE (MSFT Fundamentals, keine API-Daten)")
print("  - Fill: next_open + 0.5% Slippage")
print("  - Max. 1 Position gleichzeitig (Single-Symbol-Backtest)")
print("  - VIX-Filter NICHT modelliert (keine VIX-Daten im Backtest)")
print()
print("  WICHTIG: Hypothetische Simulation. Keine echte Trading-Performance.")
print("  Vergangene Ergebnisse garantieren keine zukünftigen Resultate.")
print("  Details: https://alpaca.markets/disclosures")
print("="*65)
print(f"\n  Artefakte gespeichert in: {RUN_DIR}")
print(f"  trades.csv | equity.csv | benchmark_equity.csv | summary.json\n")
