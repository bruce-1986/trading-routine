# Strategy Quick-Reference (Bull Bot)

**Letzte Änderung:** 2026-05-31 | **Vollständige Strategie:** `../STRATEGY.md`

---

## KAUFEN — alle 5 müssen true sein

```
K1: EMA50 > EMA200 (Golden Cross aktiv)
K2: 50 <= RSI(14) <= 70
K3: Aktie > SPY-Performance der letzten 63 Handelstage (Relative Stärke > 0)
K4: Tagesvolumen >= 120% des 20-Tage-Durchschnitts
K5: Forward P/E <= 35 UND Umsatzwachstum YoY >= 10%
```

**Ausführung:** Limit-Order nächster Handelstag, max. +0,5% über Vortagesschluss.

---

## VERKAUFEN — eines reicht

```
V1: Kurs <= Kaufkurs * 0.92          → -8% Stop-Loss       → Market Order SOFORT
V2: Kurs <= 52w-Hoch * 0.88          → -12% Trailing Stop  → Market Order SOFORT
V3: Gewinn >= 20%                     → 50% verkaufen       → Limit-Order
V4: Gewinn >= 35%                     → Rest verkaufen      → Limit-Order
V5: EMA50 < EMA200 (Death Cross)      → alles raus          → Limit-Order nächster Tag
V6: RSI > 80 UND RS vs. SPY < 0      → alles raus          → Limit-Order nächster Tag
```

---

## POSITION-SIZING

```
Max. pro Position:    10% Portfolio (VIX > 25: max. 7%)
Max. Positionen:      8
Min. Cash-Reserve:    20%
Max. Investiert:      80%
Einstieg:             Einmalig (kein Averaging-in)
```

---

## RISIKO-GUARDRAILS (Prioritätsreihenfolge)

```
1. Daily Loss Cap:    -3%/Tag    → Pause 24h, kein Kaufen
2. Weekly Loss Cap:   -5%/Woche  → Pause bis Montag
3. Drawdown-Alarm:    -15% ATH   → Cash auf 50%, Max-Pos auf 5%
4. Drawdown-Stopp:    -20% ATH   → ALLE Positionen schließen, 100% Cash, STOPP
5. Crash-Filter:      SPY -5%/Tag → Keine Käufe für 5 Handelstage
6. VIX-Filter:        VIX > 30   → Keine Käufe bis VIX < 25 (3-Tage-Schnitt)
7. Earnings-Blackout: 3 Tage vor Earnings → Stop auf -5% eng
8. Max. neue Käufe:   2 pro Woche
```

---

## ASSET-UNIVERSE

```
ERLAUBT: S&P 500 + S&P MidCap 400 Komponenten
         Marktkapitalisierung >= 5 Mrd. €
         Tagesvolumen >= 5 Mio. Shares (30-Tage-Schnitt)
         Kurs >= 10 $
         ETFs: SPY, QQQ, XLK, XLF, XLV, XLE, XLI

TABU:    Optionen, Futures, Leveraged ETFs, Krypto, REITs
         Penny Stocks < 10 $, SPACs, Biotech Phase 1/2
         > 3 Positionen gleicher Sektor (max. 30% Sektorgewicht)
```
