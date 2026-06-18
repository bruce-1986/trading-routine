# Portfolio Status

**Bot:** Bull | **Modus:** Paper Trading | **Zuletzt aktualisiert:** 2026-06-18 13:02 ET (Midday Stop-Check)

---

## Aktueller Stand (Midday 13:02 ET)

```
Gesamtwert:       100.001,63 $   (Alpaca equity)
Investiert:        10.637,66 $   (10,6%, JPM + UNH Marktwert)
Cash:              89.363,97 $   (89,4%)
Unrealisiert P/L:       +1,63 $  (JPM -10,37 $ / UNH +12,00 $)
Realisiert P/L:          0,00 $
Offene Positionen:       2 / 8
Pending Orders:          0        (UNH Limit gefüllt zwischen Open & Midday)
```

> Hinweis: Alpaca Paper-Account zeigt $100k. Memory verwendet ab heute USD direkt
> (vorheriger 10k€-Wert war Memory-Initial, nicht Alpaca-Realität).

---

## Performance-Tracking

```
Startkapital:     100.000,00 $  (2026-05-29 Alpaca / 2026-05-31 Bull Init)
All-Time-High:    100.012,97 $
Aktueller DD:         -0,011%  (vom ATH 100.012,97 $)
DD-Alarm bei:        -15,00%  → 85.011 $
DD-Stopp bei:        -20,00%  → 80.010 $

Performance heute:    -0,0004%   (equity 100.001,63 / last_equity 100.002,03)
SPY heute:            n/a
Alpha heute:          n/a
```

---

## Offene Positionen (Detail)

| Symbol | Qty | Entry | Aktuell | Unreal. P/L | % | Stop-Loss V1 | TP1/V3 | TP2/V4 |
|--------|-----|-------|---------|-------------|---|--------------|--------|--------|
| JPM    | 3   | 332,78 $ | 329,33 $ | -10,37 $ | -1,04% | 306,16 $ | 399,34 $ | 449,25 $ |
| UNH    | 24  | 401,57 $ | 402,07 $ | +12,00 $ | +0,12% | 369,44 $ | 481,88 $ | 542,12 $ |

---

## Risiko-Status (Midday 13:02 ET)

```
Daily P/L:            -0,0004%  [GRÜN — Limit: -3%]   (equity 100.001,63 / last 100.002,03)
Weekly P/L:           +0,0016%  [GRÜN — Limit: -5%]   (Montag-Basis 100.000 $)
Käufe diese Woche:    2 / 2      (JPM gefüllt 17.06., UNH gefüllt 18.06.)
VIX (letzter Stand):  17,10     [GRÜN — Open-Wert, intraday nicht neu erhoben]
Crash-Filter aktiv:   NEIN
VIX-Filter aktiv:     NEIN
Drawdown vom ATH:     -0,011%   [GRÜN]
```

---

## Pending Orders

_Keine — UNH-Limit zwischen Open und Midday gefüllt._

---

## Signal-Check Midday 13:02 ET (V1–V4)

```
JPM @ 329,42 $  (Entry 332,78 $, P/L -1,01%)
V1 Stop-Loss   -8%:   Trigger 306,16 $ — Kurs 329,42 → SICHER
V2 Trailing  -12%:    max bisher ~333,59 → Stop ~293,56 → SICHER
V3 TP1      +20%:    Trigger 399,34 $ — nicht erreicht
V4 TP2      +35%:    Trigger 449,25 $ — nicht erreicht

UNH @ 402,07 $  (Entry 401,57 $, P/L +0,12%)
V1 Stop-Loss   -8%:   Trigger 369,44 $ — Kurs 402,07 → SICHER
V2 Trailing  -12%:    max bisher 402,07 → Stop 353,82 → SICHER
V3 TP1      +20%:    Trigger 481,88 $ — nicht erreicht
V4 TP2      +35%:    Trigger 542,12 $ — nicht erreicht
```

RSI/EMA werden bei Midday nicht geprüft (nur Open & Close).
→ Keine Verkaufsorder nötig. Keine Stops ausgelöst.

---

## Tagesbilanz-Log

**Midday 13:02 ET 2026-06-18:**
Positionen: 2/8 | Ø P/L: -0,46% | UNH-Limit gefüllt seit Open
Schlechteste Position: JPM -1,01% | Beste Position: UNH +0,12%
Stops: alle regulär (V1/V2/V3/V4 für JPM und UNH nicht ausgelöst)
Daily P/L: -0,0004% [GRÜN] | Cash: 89.363,97 $ (89,4%) | Pending: 0

**Market Open 2026-06-18 09:34 ET:**
Gesamtwert: 100.012,97 $ | Cash: 99.001,65 $ (99,0%) | Investiert: 1.011,69 $ (1,0%)
P/L heute: +10,94 $ (+0,011%) | JPM +1,34% intraday
Pending: UNH Buy 24 @ $401,57 Limit Day | Käufe 2/2 (UNH pending zählt mit)
ATH: 100.012,97 $ | DD: 0,00% [GRÜN]
Guardrails: Daily +0,01% | Weekly +0,01% | VIX 17,10 | Crash-Filter: NEIN

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
