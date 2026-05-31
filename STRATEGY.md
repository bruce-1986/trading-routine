# Trading-Strategie: Momentum-Quality Bot

**Version:** 1.0 | **Datum:** 2026-05-31  
**Strategie-Typ:** Momentum + Quality Factor  
**Benchmark:** S&P 500 (SPY)  
**Startkapital:** 10.000 € (Paper Money)  
**Zeithorizont:** 6–12 Monate Long-Term

---

## ASSET-UNIVERSE

```
ERLAUBT:
- US-Aktien aus S&P 500 oder S&P MidCap 400
- Marktkapitalisierung: >= 5 Mrd. €
- Tagesvolumen: >= 5 Mio. Shares/Tag (30-Tage-Schnitt)
- Mindest-Kurs: >= 10 $
- ETFs: SPY, QQQ, XLK, XLF, XLV, XLE, XLI

TABU:
- Optionen, Futures, Leveraged ETFs, Krypto, REITs
- Penny Stocks (< 10 $)
- SPACs, Biotech Phase 1/2
- Mehr als 3 Positionen im selben Sektor (max. 30% Sektorgewicht)
```

---

## KAUFSIGNALE — alle 5 müssen erfüllt sein

| # | Signal | Bedingung |
|---|---|---|
| K1 | Trend | EMA50 > EMA200 (Golden Cross aktiv) |
| K2 | Momentum | RSI(14) zwischen 50 und 70 |
| K3 | Relative Stärke | Aktie outperformt SPY über letzte 63 Handelstage |
| K4 | Volumen | Kaufvolumen >= 120% des 20-Tage-Durchschnitts |
| K5 | Fundamentals | Forward P/E <= 35 UND Umsatzwachstum YoY >= 10% |

**Kaufausführung:** Nächster Handelstag, Limit-Order max. +0,5% über Vortagesschluss.

---

## VERKAUFSSIGNALE — eines reicht

| # | Signal | Auslöser | Ausführung |
|---|---|---|---|
| V1 | Hard Stop-Loss | -8% vom Kaufkurs | Sofort, Market Order |
| V2 | Trailing Stop | -12% vom rollierenden 52-Wochen-Hoch | Sofort, Market Order |
| V3 | Take-Profit 1 | +20% Gewinn → 50% der Position verkaufen | Limit-Order |
| V4 | Take-Profit 2 | +35% Gewinn → restliche 50% verkaufen | Limit-Order |
| V5 | Momentum-Bruch | EMA50 < EMA200 (Death Cross) | Nächster Tag, Limit |
| V6 | Überkauft+schwach | RSI > 80 UND RS vs. SPY negativ (4 Wochen) | Nächster Tag, Limit |

---

## POSITION-SIZING

```
Max. pro Position:         10% des Portfolios (= 1.000 € bei Start)
Max. Positionen gesamt:    8
Min. Cash-Reserve:         20% (immer gehalten)
Max. investiert:           80%
VIX > 25:                  Max. 7% pro Position
Einstieg:                  Einmalig (kein Averaging-in)
Basis:                     Tagesaktueller Portfoliowert
```

---

## RISIKO-GUARDRAILS

| Trigger | Schwelle | Aktion |
|---|---|---|
| Daily Loss Cap | -3% Portfolio/Tag | Keine neuen Orders für 24h |
| Weekly Loss Cap | -5% Portfolio/Woche | Pause bis Montag |
| Max. neue Positionen | 2 Käufe/Woche | Rest in Warteschlange |
| Drawdown-Alarm | -15% unter All-Time-High | Max. 5% pro Position, Cash auf 50% |
| Drawdown-Stopp | -20% unter All-Time-High | Alle Positionen schließen, 100% Cash, manueller Reset |
| Marktcrash-Filter | SPY fällt > 5% an einem Tag | Keine neuen Käufe für 5 Handelstage |
| VIX-Filter | VIX > 30 | Keine neuen Käufe bis VIX < 25 (3-Tage-Schnitt) |
| Earnings-Blackout | 3 Tage vor Earnings | Keine neuen Käufe; Stop auf -5% eng |

---

## RESEARCH-FREQUENZ

| Zeit | Aufgabe |
|---|---|
| 08:30 Uhr (vor Markt) | VIX, SPY Premarket, Makro-News, Earnings-Kalender |
| 09:30 Uhr (Marktöffnung) | Kaufsignal-Scan, offene Orders prüfen |
| 13:00 Uhr (Midday) | Trailing Stops aktualisieren, RSI offener Positionen |
| 16:00 Uhr (Marktschluss) | Performance vs. SPY, Verkaufssignale, Watchlist |
| Freitag 17:00 Uhr | RS-Ranking, Fundamentals-Screen, Sektorgewichtung |
| Monatlich | Strategie-Review, Benchmark-Vergleich, Parameter-Check |

---

## SCHNELL-REFERENZ FÜR DEN BOT

```python
# Kaufbedingung (Pseudocode)
def should_buy(stock):
    return (
        ema50 > ema200 and                          # K1: Trend
        50 <= rsi_14 <= 70 and                      # K2: Momentum
        rs_vs_spy_63d > 0 and                       # K3: Relative Stärke
        volume_today >= 1.2 * avg_volume_20d and    # K4: Volumen
        forward_pe <= 35 and revenue_growth >= 0.10 # K5: Fundamentals
    )

# Verkaufsbedingung (Pseudocode)
def should_sell(position):
    return (
        price <= entry_price * 0.92 or              # V1: Stop-Loss -8%
        price <= high_52w * 0.88 or                 # V2: Trailing Stop -12%
        gain >= 0.20 or                             # V3: Take-Profit 1
        gain >= 0.35 or                             # V4: Take-Profit 2
        ema50 < ema200 or                           # V5: Death Cross
        (rsi_14 > 80 and rs_4w < 0)                # V6: Überkauft
    )

# Position-Sizing
MAX_POSITION_PCT = 0.10      # 10% pro Aktie
MAX_POSITIONS    = 8
MIN_CASH_PCT     = 0.20      # 20% immer bar
VIX_HIGH_THRESH  = 25        # bei VIX > 25: max 7%

# Risiko-Guardrails
DAILY_LOSS_CAP   = -0.03     # -3% -> Pause 24h
WEEKLY_LOSS_CAP  = -0.05     # -5% -> Pause bis Montag
DRAWDOWN_ALARM   = -0.15     # -15% -> Cash auf 50%
DRAWDOWN_STOP    = -0.20     # -20% -> alles schließen
CRASH_FILTER_SPY = -0.05     # SPY -5% -> 5 Tage keine Käufe
VIX_STOP         = 30        # VIX > 30 -> keine Käufe
MAX_BUYS_PER_WEEK = 2
```

---

## ERWARTETE PERFORMANCE

| Szenario | Jahresrendite | Max. Drawdown |
|---|---|---|
| Bärenmarkt | -5% bis -10% | ca. -20% (Stopp greift) |
| Seitwärtsmarkt | +5% bis +15% | ca. -10% |
| Bullenmarkt | +20% bis +40% | ca. -12% |
| S&P 500 historisch | ~10% p.a. | variabel |

**Ziel:** Bullenmarkt outperformen, Bärenmarkt begrenzen durch harte Stops.

---

*Strategie erstellt: 2026-05-31 | Nächster Review: 2026-06-30*
