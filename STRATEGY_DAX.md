# Trading-Strategie: Momentum-Quality Bot — DAX-Variante

**Version:** 1.0 | **Datum:** 2026-06-18  
**Strategie-Typ:** Momentum + Quality Factor  
**Benchmark:** DAX (EXS1 / iShares Core DAX UCITS ETF)  
**Startkapital:** 10.000 € (Paper Money)  
**Zeithorizont:** 6–12 Monate Long-Term  
**Basis:** Adaptiert von [STRATEGY.md](STRATEGY.md) für den deutschen Markt

---

## ASSET-UNIVERSE

```
ERLAUBT:
- Deutsche Aktien aus DAX, MDAX oder SDAX
- Marktkapitalisierung: >= 1 Mrd. €
- Tagesvolumen (Xetra): >= 20 Mio. €/Tag (30-Tage-Schnitt)
- Mindest-Kurs: >= 5 €
- ETFs: EXS1 (DAX), EXXT (TecDAX), EXH1 (MDAX), EXSA (STOXX Europe 600)

TABU:
- Optionen, Futures, Leveraged ETFs, Krypto, REITs
- Penny Stocks (< 5 €)
- SPACs, Biotech Phase 1/2
- Mehr als 3 Positionen im selben Sektor (max. 30% Sektorgewicht)
- Nebenwerteindizes mit Tagesvolumen < 5 Mio. €
```

---

## KAUFSIGNALE — alle 5 müssen erfüllt sein

| # | Signal | Bedingung |
|---|---|---|
| K1 | Trend | EMA50 > EMA200 (Golden Cross aktiv) |
| K2 | Momentum | RSI(14) zwischen 50 und 70 |
| K3 | Relative Stärke | Aktie outperformt EXS1 (DAX-ETF) über letzte 63 Handelstage |
| K4 | Volumen | Kaufvolumen >= 120% des 20-Tage-Durchschnitts (in €) |
| K5 | Fundamentals | Forward P/E <= 25 UND Umsatzwachstum YoY >= 7% |

> **Hinweis:** Forward P/E und Wachstumsschwelle wurden gegenüber der US-Variante gesenkt,
> da DAX-Werte historisch niedriger bewertet sind und geringere Wachstumsraten aufweisen.

**Kaufausführung:** Nächster Xetra-Handelstag (09:00–17:30 Uhr), Limit-Order max. +0,5% über Vortagesschluss.

---

## VERKAUFSSIGNALE — eines reicht

| # | Signal | Auslöser | Ausführung |
|---|---|---|---|
| V1 | Hard Stop-Loss | -8% vom Kaufkurs | Sofort, Market Order |
| V2 | Trailing Stop | -12% vom rollierenden 52-Wochen-Hoch | Sofort, Market Order |
| V3 | Take-Profit 1 | +20% Gewinn → 50% der Position verkaufen | Limit-Order |
| V4 | Take-Profit 2 | +35% Gewinn → restliche 50% verkaufen | Limit-Order |
| V5 | Momentum-Bruch | EMA50 < EMA200 (Death Cross) | Nächster Tag, Limit |
| V6 | Überkauft+schwach | RSI > 80 UND RS vs. EXS1 negativ (4 Wochen) | Nächster Tag, Limit |

---

## POSITION-SIZING

```
Max. pro Position:         10% des Portfolios (= 1.000 € bei Start)
Max. Positionen gesamt:    8
Min. Cash-Reserve:         20% (immer gehalten)
Max. investiert:           80%
VDAX > 25:                 Max. 7% pro Position  (VDAX statt VIX)
Einstieg:                  Einmalig (kein Averaging-in)
Basis:                     Tagesaktueller Portfoliowert
```

> **Hinweis:** Als Volatilitätsindikator wird der **VDAX-NEW** (Deutsche Börse) statt des VIX verwendet.

---

## RISIKO-GUARDRAILS

| Trigger | Schwelle | Aktion |
|---|---|---|
| Daily Loss Cap | -3% Portfolio/Tag | Keine neuen Orders für 24h |
| Weekly Loss Cap | -5% Portfolio/Woche | Pause bis Montag |
| Max. neue Positionen | 2 Käufe/Woche | Rest in Warteschlange |
| Drawdown-Alarm | -15% unter All-Time-High | Max. 5% pro Position, Cash auf 50% |
| Drawdown-Stopp | -20% unter All-Time-High | Alle Positionen schließen, 100% Cash, manueller Reset |
| Marktcrash-Filter | EXS1 fällt > 5% an einem Tag | Keine neuen Käufe für 5 Handelstage |
| VDAX-Filter | VDAX > 30 | Keine neuen Käufe bis VDAX < 25 (3-Tage-Schnitt) |
| Earnings-Blackout | 3 Tage vor Earnings | Keine neuen Käufe; Stop auf -5% eng |
| Makro-Event | EZB-Zinsentscheid, DAX-Rebalancing | Keine neuen Käufe am Ereignistag |

---

## RESEARCH-FREQUENZ

| Zeit | Aufgabe |
|---|---|
| 08:45 Uhr (vor Xetra) | VDAX, EXS1 Premarket, Makro-News (EZB, ifo, ZEW), Earnings-Kalender |
| 09:00 Uhr (Xetra-Öffnung) | Kaufsignal-Scan, offene Orders prüfen |
| 12:30 Uhr (Midday) | Trailing Stops aktualisieren, RSI offener Positionen |
| 17:30 Uhr (Xetra-Schluss) | Performance vs. EXS1, Verkaufssignale, Watchlist |
| Freitag 18:00 Uhr | RS-Ranking, Fundamentals-Screen, Sektorgewichtung |
| Monatlich | Strategie-Review, Benchmark-Vergleich, Parameter-Check |

---

## SEKTORBESONDERHEITEN DAX

```
Automobilindustrie (BMW, Mercedes, Volkswagen, Porsche):
  - Stark exportabhängig → USD/EUR-Wechselkurs beobachten
  - Max. 2 Positionen gleichzeitig (Klumpenrisiko)

Chemie/Industrie (BASF, Bayer, Siemens, Infineon):
  - Energiepreissensitiv → Erdgaspreis als Zusatzfilter sinnvoll
  - Bayer: laufende Rechtsrisiken → Earnings-Blackout auf 5 Tage verlängern

Finanzwerte (Deutsche Bank, Allianz, Münchener Rück):
  - EZB-Zinsentscheid als Makro-Event-Filter einhalten
```

---

## SCHNELL-REFERENZ FÜR DEN BOT

```python
# Kaufbedingung (Pseudocode) — DAX-Variante
def should_buy(stock):
    return (
        ema50 > ema200 and                           # K1: Trend
        50 <= rsi_14 <= 70 and                       # K2: Momentum
        rs_vs_exs1_63d > 0 and                       # K3: Relative Stärke vs. DAX-ETF
        volume_eur_today >= 1.2 * avg_volume_eur_20d and  # K4: Volumen in €
        forward_pe <= 25 and revenue_growth >= 0.07  # K5: Fundamentals (DAX-adjustiert)
    )

# Verkaufsbedingung (Pseudocode)
def should_sell(position):
    return (
        price <= entry_price * 0.92 or               # V1: Stop-Loss -8%
        price <= high_52w * 0.88 or                  # V2: Trailing Stop -12%
        gain >= 0.20 or                              # V3: Take-Profit 1
        gain >= 0.35 or                              # V4: Take-Profit 2
        ema50 < ema200 or                            # V5: Death Cross
        (rsi_14 > 80 and rs_4w < 0)                 # V6: Überkauft
    )

# Position-Sizing
MAX_POSITION_PCT  = 0.10      # 10% pro Aktie
MAX_POSITIONS     = 8
MIN_CASH_PCT      = 0.20      # 20% immer bar
VDAX_HIGH_THRESH  = 25        # bei VDAX > 25: max 7%

# Risiko-Guardrails
DAILY_LOSS_CAP    = -0.03     # -3% -> Pause 24h
WEEKLY_LOSS_CAP   = -0.05     # -5% -> Pause bis Montag
DRAWDOWN_ALARM    = -0.15     # -15% -> Cash auf 50%
DRAWDOWN_STOP     = -0.20     # -20% -> alles schließen
CRASH_FILTER_DAX  = -0.05     # EXS1 -5% -> 5 Tage keine Käufe
VDAX_STOP         = 30        # VDAX > 30 -> keine Käufe
MAX_BUYS_PER_WEEK = 2
```

---

## UNTERSCHIEDE ZUR US-VARIANTE (STRATEGY.md)

| Parameter | US-Variante | DAX-Variante |
|---|---|---|
| Benchmark | SPY (S&P 500) | EXS1 (DAX-ETF) |
| Marktkapitalisierung | ≥ 5 Mrd. € | ≥ 1 Mrd. € |
| Volumenschwelle | ≥ 5 Mio. Shares/Tag | ≥ 20 Mio. €/Tag |
| Mindest-Kurs | ≥ 10 $ | ≥ 5 € |
| Forward P/E | ≤ 35 | ≤ 25 |
| Umsatzwachstum | ≥ 10 % | ≥ 7 % |
| Volatilitätsindex | VIX | VDAX-NEW |
| Handelszeiten | NYSE (15:30–22:00 Uhr MEZ) | Xetra (09:00–17:30 Uhr) |
| Zusatz-Filter | — | EZB-Ereignisse, DAX-Rebalancing |

---

## ERWARTETE PERFORMANCE

| Szenario | Jahresrendite | Max. Drawdown |
|---|---|---|
| Bärenmarkt | -5% bis -12% | ca. -20% (Stopp greift) |
| Seitwärtsmarkt | +3% bis +12% | ca. -10% |
| Bullenmarkt | +15% bis +35% | ca. -12% |
| DAX historisch | ~8% p.a. | variabel |

**Ziel:** DAX im Bullenmarkt outperformen, Bärenmarkt durch harte Stops begrenzen.

---

*Strategie erstellt: 2026-06-18 | Nächster Review: 2026-07-31*
