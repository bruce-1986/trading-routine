# Trade Log

**Bot:** Bull | **Startkapital:** 10.000 € | **Modus:** Paper Trading (Alpaca)

---

## Offene Positionen

| Symbol | Kaufdatum | Kaufkurs | Aktuell | Gewinn/Verlust | Stop-Loss | TP1 | TP2 | Signale |
|--------|-----------|----------|---------|----------------|-----------|-----|-----|---------|
| — | — | — | — | — | — | — | — | — |

**Gesamt investiert:** 0 € | **Cash:** 10.000 € | **Positionen:** 0/8

---

## Offene Orders (pending)

| Symbol | Datum | Typ | Qty | Limit | Status | Order-ID |
|--------|-------|-----|-----|-------|--------|----------|
| JPM | 2026-06-17 09:35 ET | Buy Limit Day | 3 | $332.80 | new | d90de96d-9084-4a6a-b5a1-de48899e75f4 |

---

## Geschlossene Trades

| Symbol | Kauf | Verkauf | Einstieg | Ausstieg | Ergebnis € | Ergebnis % | Grund |
|--------|------|---------|----------|----------|-----------|-----------|-------|
| — | — | — | — | — | — | — | — |

**Realisierter Gewinn/Verlust:** 0 € | **Win-Rate:** — | **Avg. Gewinn:** — | **Avg. Verlust:** —

---

## Trades

### KAUF (pending): JPM am 2026-06-17
- Limit-Order:    $332.80 (Day, +0,5% über Vortagesschluss $331.14)
- Menge:          3 Shares
- Investiert:     ~998 $ (~10% Portfolio)
- Stop-Loss:      $306.18 (-8% vom Fill ~ Annahme)
- Trailing Stop:  -12% vom 52w-Hoch
- TP1:            $399.36 (+20% → 50% verkaufen)
- TP2:            $449.28 (+35% → Rest verkaufen)
- Kaufsignale:    K1✓ EMA50 $306.94>EMA200 $305.80 | K2✓ RSI 68.5 | K3✓ RS+3.57% | K4✓ Vol 127% | K5✓ FwdP/E 14.58 + Rev+10%YoY
- Sektor:         Financials (XLF Top-3)
- Earnings:       2026-07-15 (kein Blackout, >3 Tage)
- Alpaca Order-ID: d90de96d-9084-4a6a-b5a1-de48899e75f4

---

## Trade-Template

```markdown
### KAUF: [SYMBOL] am [DATUM]
- Kaufkurs:       $X.XX (Limit-Order)
- Menge:          X Shares
- Investiert:     X €  (X% des Portfolios)
- Stop-Loss:      $X.XX (-8%)
- Trailing Stop:  -12% vom Hoch
- TP1:            $X.XX (+20% → 50% verkaufen)
- TP2:            $X.XX (+35% → Rest verkaufen)
- Kaufsignale:    K1✓ K2✓ K3✓ K4✓ K5✓
- Alpaca Order-ID: [ID]

### VERKAUF: [SYMBOL] am [DATUM]
- Verkaufskurs:   $X.XX
- Menge:          X Shares
- Erlös:          X €
- Ergebnis:       +/-X € (+/-X%)
- Grund:          [V1 Stop-Loss / V2 Trailing / V3 TP1 / V4 TP2 / V5 Death Cross / V6 Überkauft]
- Alpaca Order-ID: [ID]
```

---

## Wöchentliche Performance

| Woche | Depot-Start | Depot-Ende | Wochenergebnis | vs. SPY |
|-------|-------------|------------|----------------|---------|
| 2026-W22 | 10.000 € | — | — | — |
