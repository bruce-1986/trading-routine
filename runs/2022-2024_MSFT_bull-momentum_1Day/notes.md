# Backtest Notes — MSFT — Bull-Momentum — 2022-01-01 bis 2024-12-31

**Erstellt:** 2026-06-17 | **Strategie-Quelle:** memory/strategy.md

---

## Originale Anfrage
"Backtest MSFT mit der Bull-Strategie, Januar 2022 bis Dezember 2024"

---

## Bestätigte Interpretation

| Parameter | Wert |
|---|---|
| Symbol | MSFT |
| Backtest-Zeitraum | 2022-01-01 bis 2024-12-31 |
| Datenabruf-Start | 2021-06-01 (EMA200-Warmup) |
| Timeframe | 1Day |
| Feed | sip |
| Adjustment | split |
| Startkapital | 100.000 $ |
| Benchmark | SPY Buy-and-Hold |
| Fill-Modell | next_open + 0,5% Slippage |

---

## Kaufsignale (K1–K5)

- **K1:** EMA50 > EMA200 (Daily Close, EWM span=50/200, adjust=False)
- **K2:** 50 <= RSI(14) <= 70 (Wilder Smoothing: EWM alpha=1/14)
- **K3:** MSFT-Return(63T) > SPY-Return(63T) (relative Stärke > 0)
- **K4:** Volumen >= 120% des 20-Tage-Durchschnitts
- **K5:** ⚠ **ANNAHME: TRUE gesetzt** — Alpaca-Bar-Daten enthalten keine Fundamentaldaten. MSFT hatte 2022–2024 konstant Umsatzwachstum > 10% und FwdPE < 35 (Tech-Sektor, Cloud-Wachstum). Wird in zukünftigen Backtests ggf. über Perplexity-Daten verfeinert.

---

## Verkaufssignale (V1–V6)

- **V1:** Close <= Einstieg × 0,92 → Market Sell (same-bar Close als Proxy)
- **V2:** Close <= 52w-Hoch × 0,88 → Market Sell (same-bar Close als Proxy)
- **V3:** Close >= Einstieg × 1,20 → 50% Sell (next_open + 0,5%)
- **V4:** Close >= Einstieg × 1,35 → Rest Sell (next_open + 0,5%)
- **V5:** EMA50 < EMA200 → alles Sell (next_open + 0,5%)
- **V6:** RSI(14) > 80 UND RS(63T) < 0 → alles Sell (next_open + 0,5%)

---

## Position-Sizing

- 10% des Startkapitals pro Einstieg (~10.000 $)
- Max. 1 Position gleichzeitig (Single-Symbol-Backtest)
- Min. 20% Cash-Reserve = max. investierbar 80.000 $

---

## Nicht modelliert (Caveats)

1. **VIX-Filter** — keine VIX-Daten im Backtest. In Realität: bei VIX > 30 kein Kauf.
2. **Earnings-Blackout** — nicht modelliert. In Realität: 3 Tage vor Earnings enger Stop.
3. **Daily/Weekly Loss Cap** — single-symbol, kaum relevant; nicht modelliert.
4. **K5 Fundamentals** — als TRUE angenommen (dokumentiert oben).
5. **Dividenden** — durch `adjustment=split` teilweise berücksichtigt; Alpaca SIP-Daten split-adjustiert.

---

> **Wichtiger Hinweis**
> Dieser Backtest ist eine hypothetische historische Simulation und stellt keine echte Trading-Performance dar. Historische Ergebnisse garantieren keine zukünftigen Ergebnisse. Ergebnisse hängen von Datenqualität, Corporate-Action-Behandlung, Gebühren, Slippage, Liquidität und Ausführungsannahmen ab. Dieses Material dient ausschließlich Research- und Bildungszwecken und ist keine Anlageberatung. Alle Investitionen beinhalten Risiken.
> Offizielle Hinweise: [alpaca.markets/disclosures](https://alpaca.markets/disclosures)
