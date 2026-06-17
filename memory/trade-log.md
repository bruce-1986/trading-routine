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
| — | — | — | — | — | — | — |

---

## Geschlossene Trades

| Symbol | Kauf | Verkauf | Einstieg | Ausstieg | Ergebnis $ | Ergebnis % | Grund |
|--------|------|---------|----------|----------|-----------|-----------|-------|
| — | — | — | — | — | — | — | — |

**Realisierter Gewinn/Verlust:** 0 $ | **Win-Rate:** — | **Avg. Gewinn:** — | **Avg. Verlust:** —

---

## Trades

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
