# Trade Log

**Bot:** Bull | **Startkapital:** 100.000 $ | **Modus:** Paper Trading (Alpaca)

---

## Offene Positionen

| Symbol | Kaufdatum  | Kaufkurs   | Aktuell   | Gewinn/Verlust | Stop-Loss | TP1     | TP2     | Signale         |
|--------|------------|------------|-----------|----------------|-----------|---------|---------|-----------------|
| JPM    | 2026-06-17 | 332,78 $   | 333,56 $  | +2,43 $ (+0,24%) | 306,16 $  | 399,34 $ | 449,25 $ | K1✓K2✓K3✓K4✓K5✓ |

**Gesamt investiert:** 1.000,77 $ | **Cash:** 99.001,66 $ | **Positionen:** 1/8

---

## Offene Orders (pending)

| Symbol | Datum | Typ | Qty | Limit | Status | Order-ID |
|--------|-------|-----|-----|-------|--------|----------|
| UNH | 2026-06-18 | Buy Limit (Day) | 24 | 401,57 $ | new | b9674f87-9cad-4ac0-a39f-756157f8b5ed |

---

## Geschlossene Trades

| Symbol | Kauf | Verkauf | Einstieg | Ausstieg | Ergebnis $ | Ergebnis % | Grund |
|--------|------|---------|----------|----------|-----------|-----------|-------|
| — | — | — | — | — | — | — | — |

**Realisierter Gewinn/Verlust:** 0 $ | **Win-Rate:** — | **Avg. Gewinn:** — | **Avg. Verlust:** —

---

## Trades

### KAUF (pending): UNH am 2026-06-18
- Limit-Order:    $401.57 (Day, +0,5% über Vortagesschluss $399.57)
- Menge:          24 Shares
- Budget:         $10.001,30 (10% von $100.012,97; VIX 17,10 < 25 → 10%)
- Erwartete Kosten: ~$9.637,68 (bei Fill am Limit)
- Stop-Loss V1:   wird auf Fill * 0.92 gesetzt (ca. $369.44 bei Limit-Fill)
- TP1 / V3:       Fill * 1.20 (ca. $481.88 bei Limit-Fill)
- TP2 / V4:       Fill * 1.35 (ca. $542.12 bei Limit-Fill)
- Kaufsignale:    K1✓ EMA50 370,76>EMA200 333,10 | K2✓ RSI 57,7 | K3✓ RS +28,57% vs SPY 63d | K4✓ Vol 135% Avg20 | K5✓ FwdP/E 30,63 + Rev+18,63% YoY
- Sektor:         Health Care (XLV) — kein Konflikt mit JPM (Financials/XLF)
- Earnings:       2026-07-16 (28 Tage entfernt, kein Blackout)
- Pre-Market-Quote: ~$403,56 → Limit $401,57 erfordert Retracement zum Fill
- Alpaca Order-ID: b9674f87-9cad-4ac0-a39f-756157f8b5ed
- Status:         NEW / Day Order — bei Tagesende ggf. expired

### KAUF (filled): JPM am 2026-06-17
- Limit-Order:    $332.80 (Day, +0,5% über Vortagesschluss $331.14)
- Fill:           $332.78 um 15:20 ET (knapp unter Limit)
- Menge:          3 Shares
- Investiert:     998,34 $ (~1,0% Portfolio — kleines Pilotrun, Sizing wegen $100k Account-Größe untergewichtet)
- Stop-Loss V1:   $306.16 (-8% vom Fill)
- Trailing V2:    -12% vom 52w-Hoch (tracking ab morgen)
- TP1 / V3:       $399.34 (+20% → 50% verkaufen)
- TP2 / V4:       $449.25 (+35% → Rest verkaufen)
- Kaufsignale:    K1✓ EMA50 $306.94>EMA200 $305.80 | K2✓ RSI 68.5 | K3✓ RS+3.57% | K4✓ Vol 127% | K5✓ FwdP/E 14.58 + Rev+10%YoY
- Sektor:         Financials (XLF Top-3)
- Earnings:       2026-07-15 (kein Blackout, 28 Tage entfernt)
- Status Close 17.06.: $333.56 Tagesschluss, +0,24% Position-PnL, V5/V6 nicht ausgelöst
- Alpaca Order-ID: d90de96d-9084-4a6a-b5a1-de48899e75f4

---

## Trade-Template

```markdown
### KAUF: [SYMBOL] am [DATUM]
- Kaufkurs:       $X.XX (Limit-Order)
- Menge:          X Shares
- Investiert:     X $  (X% des Portfolios)
- Stop-Loss:      $X.XX (-8%)
- Trailing Stop:  -12% vom Hoch
- TP1:            $X.XX (+20% → 50% verkaufen)
- TP2:            $X.XX (+35% → Rest verkaufen)
- Kaufsignale:    K1✓ K2✓ K3✓ K4✓ K5✓
- Alpaca Order-ID: [ID]

### VERKAUF: [SYMBOL] am [DATUM]
- Verkaufskurs:   $X.XX
- Menge:          X Shares
- Erlös:          X $
- Ergebnis:       +/-X $ (+/-X%)
- Grund:          [V1 Stop-Loss / V2 Trailing / V3 TP1 / V4 TP2 / V5 Death Cross / V6 Überkauft]
- Alpaca Order-ID: [ID]
```

---

## Wöchentliche Performance

| Woche | Depot-Start | Depot-Ende | Wochenergebnis | vs. SPY |
|-------|-------------|------------|----------------|---------|
| 2026-W25 | 100.000,00 $ (Mo 15.06.) | 100.002,43 $ (lfd. Mi) | +0,0024% | TBD |
