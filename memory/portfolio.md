# Portfolio Status

**Bot:** Bull | **Modus:** Paper Trading | **Zuletzt aktualisiert:** 2026-06-17 16:00 ET

---

## Aktueller Stand (Marktschluss)

```
Gesamtwert:       100.002,43 $
Investiert:           1.000,77 $  (1,0%)
Cash:                99.001,66 $  (99,0%)
Unrealisiert P/L:        2,43 $
Realisiert P/L:          0,00 $
Offene Positionen:       1 / 8
```

> Hinweis: Alpaca Paper-Account zeigt $100k. Memory verwendet ab heute USD direkt
> (vorheriger 10k€-Wert war Memory-Initial, nicht Alpaca-Realität).

---

## Performance-Tracking

```
Startkapital:     100.000,00 $  (2026-05-29 Alpaca / 2026-05-31 Bull Init)
All-Time-High:    100.002,43 $
Aktueller DD:          0,00%  (vom ATH)
DD-Alarm bei:        -15,00%  → 85.000 $
DD-Stopp bei:        -20,00%  → 80.000 $

Performance heute:    +0,0024%
SPY heute:            -1,27%
Alpha heute:          +1,27%
```

---

## Offene Positionen (Detail)

| Symbol | Qty | Entry | Close | Unreal. P/L | % | Stop-Loss V1 | TP1/V3 | TP2/V4 |
|--------|-----|-------|-------|-------------|---|--------------|--------|--------|
| JPM    | 3   | 332,78 $ | 333,56 $ | +2,43 $ | +0,24% | 306,16 $ | 399,34 $ | 449,25 $ |

---

## Risiko-Status (Marktschluss 16:00 ET)

```
Daily P/L:            +0,0024%  [GRÜN — Limit: -3%]
Weekly P/L:           +0,0024%  [GRÜN — Limit: -5%]   (Montag-Basis 100.000 $)
Käufe diese Woche:    1 / 2      (JPM gefüllt)
VIX (letzter Stand):  16,41     [GRÜN]
Crash-Filter aktiv:   NEIN      (SPY -1,27%, Schwelle -5%)
VIX-Filter aktiv:     NEIN
Drawdown vom ATH:     0,00%     [GRÜN]
```

---

## Pending Orders

*Keine pending Orders (JPM gefüllt um 15:20 ET @ 332,78 $).*

---

## Signal-Check JPM (V1–V6) am Marktschluss

```
V1 Stop-Loss   -8%:   Trigger 306,16 $ — Kurs 333,59 $ → SICHER
V2 Trailing  -12%:    nicht relevant (Position <1 Tag, kein 52w-Hoch-Tracking)
V3 TP1      +20%:    Trigger 399,34 $ — nicht erreicht
V4 TP2      +35%:    Trigger 449,25 $ — nicht erreicht
V5 Death Cross:       EMA50 306,94 > EMA200 305,80 → KEIN Cross
V6 RSI>80 & RS<0:    RSI 68,5 < 80 → NICHT ausgelöst
```

→ Keine Verkaufsorder nötig.

---

## Tagesbilanz-Log

**Close 2026-06-17 16:00 ET:**
Gesamtwert: 100.002,43 $ | Cash: 99.001,66 $ (99,0%) | Investiert: 1.000,77 $ (1,0%)
P/L heute: +2,43 $ (+0,0024%) | Alpha vs. SPY: +1,27%
ATH: 100.002,43 $ | DD: 0,00% [GRÜN]
Guardrails: Daily +0,0024% | Weekly +0,0024% | Käufe 1/2 | VIX 16,41 | Crash-Filter: NEIN

**Midday 13:04 ET 2026-06-17:** (vorherig)
Positionen: 0/8 | Pending JPM Limit $332.80 (Kurs $336.82)

---

## Update-Template (täglich eintragen)

```markdown
**[DATUM] [UHRZEIT]**
Gesamtwert: X.XXX,XX $ | Cash: X.XXX $ | Investiert: X.XXX $ (X%)
P/L heute: +/-X $ (+/-X%) | vs. SPY: +/-X%
ATH: X.XXX $ | Aktueller DD: X%
Guardrails: Daily X% | Weekly X% | Käufe X/2 | VIX X | Crash-Filter: JA/NEIN
```
