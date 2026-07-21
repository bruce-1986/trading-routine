# Portfolio Status

**Bot:** Bull | **Modus:** Paper Trading | **Zuletzt aktualisiert:** 2026-07-21 16:03 ET (Market Close Di KW30 Tag 2, alle 7 V1-V6 SICHER, GS Rebound-Tag +2,89 % chg, KEINE Limit-Order für Mi 22.07., Daily +0,64 %, Alpha -0,16 pp, Weekly KW30 +0,18 %)

---

## Market Close 2026-07-21 16:03 ET (Di, KW30 Tag 2) — Alle 7 V1-V6 SICHER, GS ERHOLT-TAG +2,89 % chg, KEINE Limit-Order Mi, GOOGL Blackout-Aktivierungssensitiv NEGATIV (Owner-Freigabe letzte Chance Mi Vormittag)

```
Alpaca clock:      is_open=false | next_open Mi 22.07. 09:30 ET | next_close Mi 22.07. 16:00 ET
Equity:            98.417,11 $   (Alpaca /v2/account, portfolio_value)
Cash:              40.026,27 $   (40,67 %)
Portfolio MV:      58.390,84 $   (59,33 %, 7 Positionen)
Buying_power:     323.599,42 $
Daily P/L:          +630,17 $     (+0,6444 % vs last_equity 97.786,94)          [GRÜN, Cap -3 %]
                    +639,89 $     (+0,6544 % vs Memory 20.07. Close 97.777,22)
ATH:              100.066,47 $   DD -1,648 % [GRÜN — Alarm bei -15 %]
Weekly KW30:        +0,184 %     (Tag 2, vs Fr-Close 98.236,14)                 [GRÜN, Cap -5 %]
SPY Close IEX:    748,155        (vs Mo-Close 742,15 = +0,8091 %)
Alpha vs SPY:      -0,165 pp     (Portfolio +0,644 % vs SPY +0,809 %)           [LEICHT NEGATIV]
Käufe KW30:            1/2       (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0         (keine V5/V6-Trigger → keine Limit-Order Mi)
Guardrails: alle 8 GRÜN (GOOGL Blackout Tag 0 vor Mi AMC Earnings, Aktivierungssensitiv negativ Owner-Freigabe HEUTE letzte Chance)
```

**Positionen Close 16:03 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Close      | Entry      | Chg    | P/L %    | V1-Stop     | V1-Puffer      | V5 EMA-Spread | RSI    | Status |
|--------|------------|------------|--------|----------|-------------|----------------|---------------|--------|--------|
| **GOOGL**|  347,36  | 368,10     | -1,32% | -5,63 %  | 338,65      | **+2,57 % 🔴** | +41,40 ✓      | 44,90  | SICHER (verschlechtert vs Mo-Close +3,97 %; Blackout-Aktivierungssensitivität JETZT **-0,67 % negativ** V1_neu 349,70 > Kurs → Aktivierung würde Sofort-Stop auslösen; Option A Strategie-Lock **weiter aktiv**, Owner-Freigabe **letzte Chance Mi Vormittag** vor AMC Earnings) |
| **GS** | 1.085,56   | 1.141,74   | +2,89% | -4,92 %  | 1.050,40    | **+3,35 %**    | +116,60 ✓     | ~52    | SICHER (**REBOUND-TAG**, deutlich verbessert vs Mo-Close +0,50 % um +2,85 pp; Fill-Day+4-Muster AVGO/MU-Präzedenz überwunden, aber V1-Puffer bleibt eng-mittel) |
| LLY    | 1.174,80   | 1.193,89   | +2,43% | -1,60 %  | 1.098,38    | +6,96 %        | +127,48 ✓     | ~49    | SICHER (**REBOUND** +2,43 % chg vs Mo -2,78 %, RSI unter 50 XLV-Watch bleibt aber Momentum stabilisiert) |
| V (NEU)|   355,82   |   357,18   | -1,32% | -0,38 %  |   328,60    | +8,28 %        | **+4,17 ✓**   | ~63    | SICHER (Fill-Day+1 -1,32 % — Konsolidierung, V5 EMA-Spread marginal aber Golden Cross intakt, kein Fill-Day-Drop-Muster wie AVGO/MU/GS) |
| AAPL   |   327,305  | 316,86     | +0,22% | +3,30 %  |   291,51    | +12,28 %       | +27,67 ✓      | ~64    | SICHER (verbessert vs Mo-Close +12,05 %) |
| JPM    |   345,00   |   332,78   | +1,81% | +3,67 %  |   306,16    | +12,69 %       | +13,50 ✓      | ~59    | SICHER (verbessert vs Mo-Close +10,69 %) |
| UNH    |   437,00   |   401,57   | +3,67% | +8,82 %  |   369,44    | **+18,29 %**   | +47,67 ✓      | ~57    | SICHER (**BESTE Chg heute** +3,67 %, beste P/L +8,82 %, komfortabel) |

**V5/V6-Check alle 7 SICHER (EMA/RSI Wilder-Fortschreibung vs Mo-Close-Basis):**
- V5 (Death Cross EMA50 < EMA200) alle 7 negativ: **V +4,17 (engste, marginal aber Golden Cross intakt)**, JPM +13,50, AAPL +27,67, GOOGL +41,40, UNH +47,67, GS +116,60, LLY +127,48 — kein V5-Trigger
- V6 (RSI > 80 UND RS_4w < 0) alle 7 negativ: max RSI ~64 (AAPL/V) weit unter 80-Threshold; RS_4w negativ nur GOOGL (-3,68 %) + GS (-3,15 %), aber RSI dort ~45/~52 — V6 verlangt BEIDES → nicht ausgelöst
- **→ KEINE Limit-Order für Mi 22.07. platziert**

**Sektor-Gewichte Close:**
| Sektor | Positionen | MV       | % investiert | % Portfolio | Status |
|--------|------------|----------|--------------|-------------|--------|
| XLF    | GS+JPM+V   | 19.327   | 33,10 %      | 19,64 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLV    | UNH + LLY  | 19.886   | 34,06 %      | 20,21 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLK    | AAPL       | 10.146   | 17,38 %      | 10,31 %     | GRÜN |
| XLC    | GOOGL      |  9.031   | 15,47 %      |  9,18 %     | GRÜN |

**Close-Fazit:**
- **Positionen geprüft:** 7/8 (Slot 2/2 KW30 offen bis Fr 24.07.)
- **Ø P/L (weighted):** **+0,06 %** (Unrealized PL +32,84 $ / Cost-Basis 58.357,99)
- **Beste Position (P/L):** UNH +8,82 % | **Beste Chg heute:** UNH +3,67 %
- **Schlechteste Position (P/L):** GOOGL -5,63 % | **Schlechteste Chg heute:** GOOGL -1,32 %
- **Stops/Limits ausgelöst:** NEIN (alle 7 V1-V6 SICHER; GOOGL +2,57 % engste V1-Puffer, GS +3,35 %, LLY +6,96 %)
- **V3/V4 TP-Signale:** keine (max P/L +8,82 % UNH — weit von +20 %-Schwelle)
- **Daily P/L:** +0,644 % [GRÜN, Cap -3 % weit entfernt]
- **Weekly KW30 Tag 2:** +0,184 % [GRÜN, Cap -5 %]

**GS Rebound-Tag — Fill-Day+4-Muster ÜBERWUNDEN:**
- Verlauf: Entry 15.07. 1.141,74 → Do-Close +1,42 % Puffer → Fr-Close +1,46 % → Mo-Open +2,80 % → Mo-Midday **+0,41 %** → Mo-Close **+0,50 % ENGSTE** → Di-Open +2,17 % → Di-Close **+3,35 % (+30,53 $ chg)**
- Präzedenz AVGO Fill-Day+3 V1 / MU Fill-Day+4 V1 → **GS Fill-Day+4-Fenster HEUTE ohne V1-Auslösung überstanden, Muster als überwunden zu werten** (aber V1-Puffer bleibt eng-mittel bis endgültige Erholung)
- Δ zum V1: 1.085,56 - 1.050,40 = **35,16 $** = 3,35 % — komfortabler als Vortag, aber weiter Watchlist

**GOOGL Blackout-Aktivierung Mi 22.07. AMC Earnings — LETZTE CHANCE für Owner-Freigabe:**
- V1_neu Blackout = 368,10 × 0,95 = **349,70** vs Standard V1 338,65 (Strategie-Lock)
- Kurs Close 347,36 < V1_neu 349,70 = **-0,67 % negativ** → Blackout-Tightening würde JETZT Sofort-Stop auslösen
- Verlauf Blackout-Sensitivität: Mo-Close +0,69 % positiv → Di-Pre +0,41 % → Di-Open -0,05 % → Di-Close **-0,67 % negativ**
- **Option A Strategie-Lock beibehalten** (V1 = Standard 338,65) — Owner-Freigabe pending
- **Mi 22.07. Vormittag ist die letzte Gelegenheit** für Blackout-Entscheidung vor AMC-Earnings
- **PushNotification Prio 3 an Owner** (Zeitkritisch: Entscheidung morgen Vormittag zwingend)

**Watchlist Mi 22.07. + KW30 Slot 2/2 (LOCK-Ende Fr 24.07.):**
- Alpaca-Screener über 20 Non-XLK/XLV/XLF/XLC-Symbole (heutiger Close als Basis) → **NEUER LEAD 3/3 K1-K3:**
  - **MMM 170,72** (XLI Industrials, K1 EMA50 157,27 > EMA200 155,14 Spread +2,12 ✓ marginal, RSI 68,72 ✓ **knapp am K2-Cap 70**, RS_63d **+7,18 %** ✓, Ret63 +12,73 %) — **K5-Recheck + Earnings-Blackout Mi Pre-Market zwingend** (Q2 typisch Ende Juli)
- **UPS 116,33** 3/3 K1-K3 (Rebound heute +2,80 % vs Mo-Close 113,16, K3 verbessert von +1,78 % → +3,02 %) — **K5 dauerhaft FAIL** (Rev-Growth TTM -2,65 % Multi-Source) → REJECT stabil
- **ABBV 256,14 / MRK 126,26 / JNJ 250,66** alle 3/3 K1-K3 (XLV) — **XLV-Sektor-Cap-Frage weiter Owner-Pending** (aktuell 20,21 % Portfolio + jeweils ~9 % Neu-Position → wäre 29 % knapp am 30 %-Cap)
- **KO** fällt aus 3/3 (RSI 49,55 K2-Fail durch heutigen -0,18 % Kurs 81,96)
- **Rejects:** HON (K3 -55,55 %), RTX (K3 -6,62 %), CVX (K3 -1,29 %), XOM (K3 -2,80 %), COP (K3 -4,63 %), CAT (K2 43,00 <50), DE (K3 -6,84 %), LMT (K3 -18,33 %), NOC (K3 -27,76 %), WMT (K3 -19,31 %), PG (K1-Fail), PEP (K1-Fail), COST (K1-Fail), GE (K2 42,71 <50)
- **Prio Mi 22.07.:** MMM (neu, K5-Recheck) + ABBV/MRK/JNJ (falls Owner Sektor-Cap freigibt); UPS bleibt K5-blocked; KO 2/3 unter Beobachtung

**Guardrails alle 8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     +0,644 %                                          [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 2 +0,184 %                               [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,648 %                                          [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,648 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,809 %                                      [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (Perplexity Pre-Market carry-over)         [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi 22.07. AMC Tag 0 (Option A Owner-Pending, aktivierungssensitiv negativ -0,67 %) | [WARN — GOOGL zeitkritisch] |
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                [FREI 1]
```

**Nächste Routine:** Mi 22.07. 08:30 ET Pre-Market Check — GOOGL Blackout-Entscheidung LETZTE CHANCE, MMM K5-Multi-Source-Recheck + Earnings-Datum, GS/LLY Rebound-Fortsetzung Watch.

---

## Market Open 2026-07-21 09:40 ET (Di, KW30 Tag 2) — Alle 7 V1-V6 SICHER, GS Puffer +2,17 % ERHOLT, KO+UPS K5-FAIL → KEIN Kauf

```
Alpaca clock:      is_open=true | next_close Di 21.07. 16:00 ET
Equity:            97.780,68 $   (Live-Kalk aus Cash + Positions-MV)
Cash:              40.026,27 $   (40,93 %)
Portfolio MV:      57.754,41 $   (59,07 %, 7 Positionen)
Buying_power:     321.784,23 $
Daily P/L:          -0,006 %      (vs Alpaca last_equity 97.786,94, Reset bei Open)  [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -2,284 % [GRÜN — Alarm bei -15 %]
Weekly KW30:        -0,464 %      (Tag 2, vs Fr-Close 98.236,14)                     [GRÜN, Cap -5 %]
SPY Live 09:40:    745,67         (vs Mo-Close 742,15 = +0,474 %)                    [POSITIV]
VIX carry-over:    17,6-18,0      (Perplexity Pre-Market)                             [GRÜN]
Käufe KW30:            1/2        (V gefüllt, Slot 2/2 offen bis Fr 24.07.)          [FREI 1]
Open Orders:           0
Guardrails: alle 8 GRÜN (GOOGL Blackout Tag -1 vor Mi 22.07. AMC weiter Owner-Pending Option A)
```

**Positionen Live 09:40 ET (Alpaca /v2/positions + latest trades) — sortiert Puffer ENG→WEIT:**

| Sym    | Live       | Entry      | Chg vs Open | P/L %    | V1-Stop     | V1-Puffer      | Signal Δ |
|--------|------------|------------|-------------|----------|-------------|----------------|----------|
| **GS** | 1.073,235  | 1.141,74   | +1,67 %     | -6,00 %  | 1.050,40    | **+2,17 %**    | SICHER, ERHOLT vs Mo-Close +0,50 % um +1,67 pp, Fill-Day+4-Fenster (AVGO/MU Präzedenz Fill-Day+3/+4 V1) |
| **GOOGL**|  349,515 | 368,10     | -0,74 %     | -5,05 %  | 338,65      | **+3,21 %**    | SICHER, leicht verschlechtert vs Mo-Close +3,97 %, Blackout Tag -1 vor Mi AMC (V1_neu 349,70 > Kurs = -0,05 % neg → aktivierungssensibel, Owner-Freigabe zwingend heute) |
| LLY    | 1.145,55   | 1.193,89   | -0,07 %     | -4,05 %  | 1.098,38    | +4,29 %        | SICHER, marginal verschlechtert vs Mo-Close +4,37 %, RSI unter 50 XLV-Watch |
| V (NEU)|   357,190  |   357,18   | -0,00 %     | +0,00 %  |   328,60    | +8,70 %        | SICHER, Fill-Day+1 flat (kein Fill-Day+3-Muster-Trigger heute) |
| JPM    |   338,870  |   332,78   | -0,01 %     | +1,83 %  |   306,16    | +10,68 %       | SICHER |
| AAPL   |   324,720  |   316,86   | -0,59 %     | +2,48 %  |   291,51    | +11,39 %       | SICHER, verbessert vs Mo-Close +12,05 % durch weiteren Chg -0,59 % (XLK-Divergenz-Watch bleibt) |
| UNH    |   424,570  |   401,57   | +0,64 %     | +5,73 %  |   369,44    | +14,92 %       | SICHER, verbessert vs Mo-Close +14,19 % um +0,73 pp |

**V1-V6-Check alle 7 SICHER:** kein V1 gebrochen (engste GS +2,17 %), kein V2-Trail (52w-Hoch weit von Kurs), kein V3/V4 (max UNH +5,73 % << 20 % TP-Schwelle), V5/V6 stabil aus Mo-Close-Analyse (alle 7 EMA50>EMA200, RSI max 64 << 80). **→ Keine Sell-Order Di 09:40 ET.**

**Market-Open-Scan Slot 2/2 KW30 — Entscheidung KEIN Kauf:**

| Kandidat | K1 EMA-Spread | K2 RSI | K3 RS_63d vs SPY | K4 Vol | K5 FwdPE | K5 RevGrowth | Entscheidung |
|----------|---------------|--------|------------------|--------|----------|--------------|--------------|
| **KO**   | +5,59 ✓ (81,12/75,53) | 50,36 ✓ | +4,33 pp ✓ (+9,12 % vs +4,79 %) | offen (10 min in Session) | 23-26 ✓ | **KONFLIKT** TTM +5,1 % ✗ vs Q1 FY26 +12,1 % ✓ | **REJECT** (K5-Multi-Source-Konflikt + pre-Q2-Earnings 28.07. BMO 5 HT weg + Fr 17.07. -4,58 % Drop unerklärt → Level-0-Regel "No-Action bei Unsicherheit") |
| **UPS**  | +7,42 ✓ (107,59/100,17) | 56,16 ✓ | +3,30 pp ✓ (+8,09 % vs +4,79 %) | offen (10 min in Session) | 14-15 ✓ | **FAIL** TTM -2,65 % ✗ und MRQ -0,3 % ✗ | **REJECT** (K5 klar negativ + Mo 20.07. -3,88 % Drop unerklärt + pre-Q2-Earnings 28.07.) |

**Zusätzliche Warnsignale:**
- **KO -4,58 % Fr 17.07.** (85,48 Open → 81,565 Close, intraday-High 85,52 → -Low 80,84 = -5,47 % Range) — Perplexity ohne News-Bestätigung, pre-Earnings-Weakness möglich
- **UPS -3,88 % Mo 20.07.** (117,73 Fr-Close → 113,16 Mo-Close, intraday-Low 112,68) — Perplexity ohne News-Bestätigung, pre-Earnings-Weakness möglich
- **Beide Q2-Earnings am 28.07. BMO** = 5 HT weg, Standard-Blackout aktivierbar ab Do 23.07. Close → sehr enges Kauf-Fenster (nur Di+Mi verbleibend), dann Blackout-Sperre

**Guardrails alle 8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     -0,006 % (frisch nach Open, Reset)                [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 2 -0,464 %                               [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,284 %                                          [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,284 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Live +0,474 %                                 [INAKTIV]
6. VIX-Filter (>30):          17,6-18,0 (Perplexity carry-over Pre)             [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi 22.07. AMC Tag -1 (Option A Owner-Pending; V1_neu 349,70 > Kurs 349,515 = -0,05 % negativ → **aktivierungssensibel heute**) | [WARN] |
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                [FREI 1]
```

**GOOGL-Blackout-Entscheidung SENSIBEL:**
- V1_neu Blackout (368,10 × 0,95 = 349,70) vs Live 349,515 = **-0,05 % negativ** → Blackout-Aktivierung würde JETZT einen Sofort-Stop auslösen
- Option A Strategie-Lock (Standard V1 338,65) weiter aktiv, aber der Puffer schmilzt (Mo-Close +0,69 % positiv → jetzt -0,05 % negativ)
- **Letzte Chance heute Di + Mi Vormittag** für Owner-Blackout-Entscheidung vor Mi-Close-Earnings
- PushNotification an Owner erneut zwingend (Blackout-Aktivierungssensitivität erreicht)

**Entscheidung Market Open 09:40 Di 21.07.:** **Keine Aktion Buy-seitig** (regelkonform: KO K5-Konflikt + UPS K5-FAIL → REJECT beide). **Keine Aktion Sell-seitig** (alle 7 V1-V6 SICHER, GS erholt auf +2,17 %). **PushNotification Prio 3** an Owner (GOOGL Blackout aktivierungssensibel + KO/UPS REJECT-Begründung). ClickUp-Fallback wegen bekanntem "Team not authorized"-Fehler → nur PushNotification.

**Nächste Routine:** Di 21.07. 13:00 ET Midday Stop-Check — GS V1 1.050,40 weiter Watch (Puffer +2,17 %), GOOGL V1 338,65 + Blackout-Entscheidung, LLY RSI-Watch, KO/UPS-Watchlist bleibt für Mi Slot 2/2 (aber K5 weiter Blockade → wahrscheinlich Slot 2/2 KW30 unbelegt bleibt).

---

## Pre-Market 2026-07-21 08:36 ET (Di, KW30 Tag 2) — Alle 8 Guardrails GRÜN, GS pre-Puffer ~+1,38 % entspannt, Market-Open-Scan JA

```
Alpaca clock:      is_open=false | next_open Di 21.07. 09:30 ET (in ~55 min)
Equity:            97.656,39 $   (Alpaca /v2/account)
Cash:              40.026,27 $   (40,99 %)
Portfolio MV:      57.630,12 $   (59,01 %, 7 Positionen)
Buying_power:     321.469,41 $
Daily P/L (overnight): -0,133 %  (vs last_equity 97.786,94, Reset bei Open)   [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -2,409 % [GRÜN — Alarm bei -15 %]
Weekly KW30:        -0,590 %     (Tag 2, vs Fr-Close 98.236,14)               [GRÜN, Cap -5 %]
SPY Pre-Market:    744,91         (vs Mo-Close 742,15 = +0,37 %)               [Crash-Filter INAKTIV]
VIX (Perplexity):  17,6-18,0     (vs Vortag 18,65 = -5-6 %)                   [GRÜN, < 30]
10Y Treasury:      4,25-4,35 %   (leicht höher vs Vortag)
Käufe KW30:            1/2       (Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0
Guardrails: alle 8 GRÜN (GOOGL Blackout Owner-Pending Option A Strategie-Lock)
```

**Positionen Pre-Market 08:36 ET (Alpaca /v2/positions, current_price = stale/pre-market letzter Trade):**

| Sym    | Cur.Price  | Entry      | P/L %    | V1-Stop     | V1-Puffer     | Status |
|--------|------------|------------|----------|-------------|---------------|--------|
| **GS** | 1.064,88   | 1.141,74   | -6,73 %  | 1.050,40    | **~+1,38 %**  | entspannt vs Mo-Close +0,50 %, aber Quote-Spread breit → Open-Bestätigung zwingend |
| **GOOGL**|  351,14  | 368,10     | -4,61 %  | **338,65** (Option A) | ~+3,69 % | Q2 Mi 22.07. AMC bestätigt → Blackout Tag -1, Owner-Pending V1_neu 349,70 (Kurs +0,41 % darüber) |
| LLY    | 1.140,13   | 1.193,89   | -4,50 %  | 1.098,38    | ~+3,80 %      | (leicht verschlechtert vs Mo-Close +4,37 %) |
| V (NEU)|   358,07   |   357,18   | +0,25 %  |   328,60    | ~+8,97 %      | Fill-Day+1 (kein Sofort-Drop-Muster wie AVGO/MU/GS) |
| JPM    |   339,00   |   332,78   | +1,87 %  |   306,16    | ~+10,73 %     | |
| AAPL   |   325,00   |   316,86   | +2,57 %  |   291,51    | ~+11,49 %     | (leicht verschlechtert vs Mo-Close +12,05 %) |
| UNH    |   421,06   |   401,57   | +4,85 %  |   369,44    | ~+13,97 %     | (leicht verschlechtert vs Mo-Close +14,19 %) |

**Guardrails alle 8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     -0,133 % overnight, Reset bei Open              [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 2 -0,590 %                             [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,409 %                                        [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,409 %                                        [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Mo -0,152 %, Pre +0,37 %                    [INAKTIV]
6. VIX-Filter (>30):          17,6-18,0                                       [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi 22.07. AMC (Owner-Pending Option A)   [WARN] |
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)              [FREI 1]
```

**Pre-Market-Entscheidung:**
- Guardrail-Status: **GRÜN**
- VIX: **17,6-18,0** | SPY Pre-Market: **+0,37 %**
- Earnings-Blackouts: **NUR GOOGL** (Mi 22.07. AMC — Option A Strategie-Lock)
- Market-Open-Scan: **JA** (Slot 2/2 KW30 offen, Prio KO + UPS K4/K5-Bestätigung)
- **Kritisch:** GS V1 1.050,40 Sofort-Sell bei Break (Bestätigung Open 09:30 zwingend, Alpaca Pre-Quote-Spread unzuverlässig)
- **Blackout-Owner-Erinnerung:** letzte Chance heute Di + Mi Vormittag für GOOGL-Blackout-Entscheidung vor Mi-Close-Earnings

**Nächste Routine:** Di 21.07. 09:30 ET Market Open + Kaufsignal-Scan (KO + UPS K4/K5, GS V1-Bestätigung).

---

## Market Close 2026-07-20 16:02 ET (Mo, KW30 Tag 1) — Alle 7 V1-V6 SICHER, GS Puffer +0,50 % RAZOR-THIN, KEINE Limit-Order Di

```
Alpaca clock:      is_open=false | next_open Di 21.07. 09:30 ET
Equity:            97.777,22 $   (Alpaca /v2/account)
Cash:              40.026,28 $   (40,94 %)
Portfolio MV:      57.750,94 $   (59,06 %, 7 Positionen)
Buying_power:     321.807,75 $
Daily P/L:          -458,92 $     (-0,467 % vs last_equity 98.236,14)         [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -2,288 % [GRÜN — Alarm bei -15 %]
Weekly KW30:        -0,467 %     (Tag 1)                                       [GRÜN, Cap -5 %]
SPY Close IEX:    742,15         (vs Fr-Close 743,28 = -0,152 %)
Alpha vs SPY:      -0,315 pp     (GS -0,957 % Drag + LLY -2,777 % + UNH -1,312 %) [NEGATIV]
Käufe KW30:            1/2       (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0         (keine V5/V6-Trigger → keine Limit-Order Di)
Guardrails: alle 8 GRÜN
```

**Positionen Close 16:02 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Close      | Entry      | Chg    | P/L %    | V1-Stop     | V1-Puffer      | V5 EMA-Spread | RSI    | Status |
|--------|------------|------------|--------|----------|-------------|----------------|---------------|--------|--------|
| **GS** | 1.055,66   | 1.141,74   | -0,96% | **-7,60 %** | 1.050,40   | **+0,50 % 🔴** | +116,11 ✓     | 49,77  | SICHER (Fill-Day+3 Drop-Muster VOLLBILD, 5,26 $ vom V1, minimal verbessert vs Midday +0,41%, aber weiter ENGSTE ALLER ZEITEN) |
| **GOOGL**|  352,11  | 368,10     | +1,55% | -4,28 %  | 338,65      | **+3,97 %**    | +42,14 ✓      | 45,82  | SICHER (leichter Rebound vs Midday +4,36% → +3,97% durch Close-Bar, Blackout Owner-Pending, V1_neu Blackout 349,70 < Kurs = +0,69% positiv, kein Sofort-Stop-Risiko) |
| LLY    | 1.146,38   | 1.193,89   | -2,78% | -3,98 %  | 1.098,38    | +4,37 %        | +127,10 ✓     | 47,72  | SICHER (schlechteste Chg heute, verschlechtert vs Midday +6,15%, RSI unter 50 gekippt = Momentum-Neutralisierung — Watch Di) |
| V (NEU)|   361,05   |   357,18   | +0,56% | +1,09 %  |   328,60    | +9,88 %        | **+3,67 ✓**   | 64,29  | SICHER (Fill-Day+0 Close +1,09 % — **kein Sofort-Drop-Muster** wie AVGO/MU/GS; V5 EMA-Spread bleibt marginal aber intakt) |
| JPM    |   338,90   |   332,78   | -0,65% | +1,84 %  |   306,16    | +10,69 %       | +13,02 ✓      | 57,66  | SICHER (verschlechtert vs Midday +10,95%) |
| AAPL   |   326,65   |   316,86   | -2,07% | +3,09 %  |   291,51    | +12,05 %       | +27,19 ✓      | 64,28  | SICHER (deutlich verschlechtert vs Midday +11,37% → +12,05% durch weiteren -2,07% Drop, XLK-Divergenz-Fortsetzung?) |
| UNH    |   421,85   |   401,57   | -1,31% | +5,05 %  |   369,44    | +14,19 %       | +47,06 ✓      | 54,62  | SICHER (leicht verschlechtert vs Midday +14,28%) |

**V5/V6-Check alle 7 SICHER (Alpaca 264d Bars, Standard-EMA 2/(N+1), Wilder-RSI):**
- V5 (EMA50 < EMA200 = Death Cross) alle 7 negativ: AAPL Spread +27,19 | GOOGL +42,14 | GS +116,11 | JPM +13,02 | LLY +127,10 | UNH +47,06 | **V +3,67 (engste, marginal aber Golden Cross intakt)** — kein V5-Trigger
- V6 (RSI > 80 UND RS_4w < 0) alle 7 negativ: max RSI 64,29 (V), 64,28 (AAPL) — beide weit unter 80-Threshold; RS_4w negativ nur GOOGL (-3,68 %) + GS (-3,15 %), aber RSI dort 45,82 / 49,77 — V6 verlangt BEIDES → nicht ausgelöst
- **→ KEINE Limit-Order für Di 21.07. platziert**

**Sektor-Gewichte Close:**
| Sektor | Positionen | MV       | % investiert | % Portfolio | Status |
|--------|------------|----------|--------------|-------------|--------|
| XLF    | GS+JPM+V   | 19.192   | 33,23 %      | 19,63 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLV    | UNH + LLY  | 19.263   | 33,35 %      | 19,70 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLK    | AAPL       | 10.132   | 17,54 %      | 10,36 %     | GRÜN |
| XLC    | GOOGL      |  9.161   | 15,86 %      |  9,37 %     | GRÜN |

**Close-Fazit:**
- **Positionen geprüft:** 7/8 (Slot 2/2 KW30 offen bis Fr 24.07.)
- **Ø P/L (weighted):** **-0,77 %** (Unrealized PL -609,89 $ / Cost-Basis 58.357,99)
- **Beste Position:** UNH +5,05 %
- **Schlechteste Position:** GS -7,60 %
- **Stops/Limits ausgelöst:** NEIN (alle 7 V1-V6 SICHER; GS +0,50 % engste, GOOGL +3,97 %, LLY +4,37 %)
- **V3/V4 TP-Signale:** keine (max P/L +5,05 % UNH — weit von +20 %-Schwelle)
- **Daily P/L:** -0,467 % [GRÜN, Cap -3 % weit entfernt]
- **Weekly KW30 Tag 1:** -0,467 % [GRÜN, Cap -5 %]

**GS Fill-Day+3 Drop-Muster VOLLBILD — kritischer Watch Pre-Market Di 21.07.:**
- Entry 15.07. 1.141,74 → Do-Close +1,42 % Puffer → Fr-Close +1,46 % → Mo-Open +2,80 % → Mo-Midday +0,41 % → **Mo-Close +0,50 %** (leichte Erholung vom Midday-Minimum)
- Präzedenz: AVGO Fill-Day+3 V1-Stop -8,69 %, MU Fill-Day+4 V1-Stop -10,92 % → **GS aktuell im Fill-Day+3-Fenster** direkt am V1
- Δ zum V1: 1.055,66 - 1.050,40 = **5,26 $** = 0,50 % — jede -0,50 %-Bewegung triggert Market-Sell
- Pre-Market Di 08:30 ET zwingender Watch, Market-Sell-Bereitschaft bei Break

**GOOGL Blackout-Aktivierung Do 22.07. AMC Earnings (Owner-Pending Fortsetzung Option A):**
- V1_neu Blackout = 368,10 × 0,95 = **349,70** vs Standard V1 338,65 (Strategie-Lock)
- Kurs Close 352,11 > V1_neu 349,70 = **+0,69 % positiv** → Blackout-Tightening würde AKTUELL keinen Sofort-Stop auslösen (vs Fr-Close -0,84 % negativ, Mo-Open +1,99 %)
- **Option A Strategie-Lock beibehalten** — Owner-Freigabe für Blackout-Aktivierung weiter pending (nur noch Di+Mi Blackout-Fenster vor Q2 Do 22.07. AMC)

**Watchlist Di 21.07. + KW30 Slot 2/2 (LOCK-Ende Fr 24.07.):**
- Alpaca-Screener über 20 Non-XLK/XLV/XLF/XLC-Symbole (XLI/XLP/XLE/XLU/XLB) → **2 K1-K3 LEADS 3/3:**
  - **KO 82,11** (XLP Consumer Staples, K1 EMA50 81,08 > EMA200 75,85 Spread +5,22 ✓, RSI 50,08 ✓ marginal grün, RS_63d +3,89 % ✓ — K4/K5 zwingend Di Pre-Market: Q2 Earnings Ende Juli Historik-Muster, Blackout-Risiko prüfen)
  - **UPS 113,16** (XLI Industrials, K1 EMA50 108,34 > EMA200 101,76 Spread +6,58 ✓, RSI 56,00 ✓, RS_63d +1,78 % ✓ marginal — K4/K5 zwingend Di Pre-Market: Q2 Earnings Historik Ende Juli, Blackout-Risiko)
- **Backup 2/3-Kandidaten (K3-Fail durch negative RS):** HON (RSI 51,80, RS -7,62 %), RTX (RSI 55,99, RS -5,53 %), CVX (RSI 65,78, RS -1,66 %), XOM (RSI 61,15, RS -3,19 %), COP (RSI 59,50, RS -4,83 %), GE (K2-Fail RSI 43,12), MMM (2/3, RS -1,43 %)
- **Aus vorheriger Watchlist unverändert:** ABBV/MRK/JNJ (XLV, alle 3/3 K1-K3 aber Sektor-Cap-Deutungs-Frage Owner-Pending), PANW (K5-permanent-blocked FwdPE 42-78 Multi-Source)
- **Prio Di 21.07.:** KO + UPS (kein Sektor-Cap, aber K5-Recheck + Earnings-Blackout Ende Juli klärungsbedürftig)

**Guardrails alle 8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     -0,467 %                                       [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 1 -0,467 %                            [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,288 %                                       [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,288 %                                       [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,152 %                                   [INAKTIV]
6. VIX-Filter (>30):          18,28 (Perplexity spot, keine Update Close)    [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Option A Strategie-Lock aktiv (V1_neu 349,70 < Kurs 352,11 = +0,69% positiv, kein Sofort-Stop-Risiko) | V Q3 Blackout ab Do 23.07. Close aktivierbar | [WARN — GOOGL Owner-Pending] |
8. Max Käufe KW30:            1/2 (V gefüllt, Slot 2/2 offen bis Fr 24.07.)  [FREI 1]
```

**Entscheidung Close 16:02 Mo 20.07.:** **Keine Aktion** (regelkonform — alle V1-V6 SICHER, keine Stop-/TP-Trigger, keine V5/V6-Limit-Order nötig, Daily Cap fern, Weekly Cap fern). **PushNotification Prio 2 an Owner** wegen GS-Puffer +0,50 % (weiterhin ENGSTE ALLER ZEITEN, Fill-Day+3-Muster-Fenster). **ClickUp Task ERR "Team not authorized"** (dieselbe permanent-Fehler-Klasse wie GS 15.07. HTTP 403 OAuth-023) → Fallback PushNotification.

**Nächste Routine:** Di 21.07. 08:30 ET Pre-Market Check — **GS V1 1.050,40 kritisch (Puffer +0,50 %, Break → Market-Sell)**, GOOGL V1 338,65 + Blackout-Aktivierungs-Frage (Do 22.07. AMC Earnings), LLY RSI unter 50 Momentum-Watch, KO/UPS K5-Multi-Source-Recheck für Slot 2/2 KW30.

---

## Midday 2026-07-20 13:08 ET (Mo, KW30 Tag 1) — Alle 7 V1 SICHER, GS Puffer +0,41% RAZOR-THIN, keine Stops

```
Alpaca clock:      is_open=true | next_close Mo 20.07. 16:00 ET
Equity:            97.946,18 $   (Alpaca /v2/account)
Cash:              40.026,28 $   (40,87 %)
Portfolio MV:      57.914,63 $   (59,13 %, 7 Positionen)
Buying_power:     322.280,85 $
Daily P/L:          -289,96 $     (-0,2952 % vs last_equity 98.236,14)     [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -2,119 % [GRÜN — Alarm bei -15 %]
Weekly KW30:        -0,295 %     (Tag 1)                                    [GRÜN]
SPY Live 13:08:   744,27         (vs Fr-Close 743,28 = +0,133 %)
Alpha vs SPY:      -0,428 pp     (GS -Drag dominiert)                       [NEGATIV]
Käufe KW30:            1/2       (V gefüllt, Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0
Guardrails: alle 8 GRÜN
```

**Positionen Live 13:08 ET (nach Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Live       | Entry      | Chg vs Open | P/L %    | V1-Stop     | V1-Puffer      | Signal Δ vs Open |
|--------|------------|------------|-------------|----------|-------------|----------------|------------------|
| **GS** | 1.054,76   | 1.141,74   | -2,32 %     | **-7,62 %** | 1.050,40   | **+0,41 % 🔴** | SICHER (WEITER verschlechtert vs Open +2,80 %, Puffer -2,39 pp — Fill-Day+3 Drop-Muster VOLLBILD, ~4 $ vom V1) |
| **GOOGL**|  353,43  | 368,10     | -0,94 %     | -3,99 %  | 338,65      | **+4,36 %**    | SICHER (leicht verschlechtert vs Open +5,35 %, Puffer -0,99 pp; Blackout Owner-Pending) |
| LLY    | 1.165,96   | 1.193,89   | -0,72 %     | -2,34 %  | 1.098,38    | +6,15 %        | SICHER (verschlechtert vs Open +6,93 %, Puffer -0,78 pp) |
| V (NEU)|   360,89   |   357,18   | +1,04 %     | +1,04 %  |   328,60    | +9,83 %        | SICHER (Fill-Day+0 leicht positiv, +1,04 pp vs Fill 357,18 → **kein Sofort-Drop-Muster** wie AVGO/MU) |
| JPM    |   339,68   |   332,78   | -1,08 %     | +2,07 %  |   306,16    | +10,95 %       | SICHER (leicht verschlechtert vs Open +12,16 %, Puffer -1,21 pp) |
| AAPL   |   324,64   |   316,86   | -2,00 %     | +2,46 %  |   291,51    | +11,37 %       | SICHER (verschlechtert vs Open +13,64 %, Puffer -2,27 pp; XLK-Divergenz?) |
| UNH    |   422,20   |   401,57   | +0,18 %     | +5,14 %  |   369,44    | +14,28 %       | SICHER (leicht verbessert vs Open +14,08 %, Puffer +0,20 pp) |

**Midday-Fazit:**
- **Positionen geprüft:** 7/8 (ein Slot frei)
- **Ø P/L (weighted):** **-0,76 %** (Unrealized PL -443,36 $ / Marktwert 58.358)
- **Beste Position:** UNH +5,14 %
- **Schlechteste Position:** GS -7,62 %
- **Stops ausgelöst:** NEIN (alle 7 V1 SICHER; GS +0,41 % Puffer RAZOR-THIN, GOOGL +4,36 %)
- **V3/V4 TP-Signale:** keine (max P/L +5,14 % — weit von +20 %-Schwelle)
- **Daily P/L:** -0,2952 % [GRÜN, Cap -3 %]
- **Neue Orders:** keine platziert (kein Stop-Trigger, kein TP-Trigger)

**GS Fill-Day+3 Drop-Muster VOLLBILD — kritischer Watch Close 16:00 ET:**
- Entry 15.07. 1.141,74 → Do-Close +1,42 % Puffer → Fr-Close +1,46 % → Mo-Open +2,80 % → **Mo-Midday +0,41 % ENGSTE ALLER ZEITEN**
- Präzedenz: AVGO Fill-Day+3 V1-Stop -8,69 %, MU Fill-Day+4 V1-Stop -10,92 % → GS ist **im gleichen Muster-Fenster**
- Δ zum V1: 1.054,76 - 1.050,40 = **4,36 $** = 0,41 % — jede Bewegung >-0,42 % triggert Market-Sell
- Close-Routine muss GS V1 zwingend als Pre-Market-Watch für Di 21.07. markieren

**Guardrails alle 8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     -0,295 %                                     [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 1 -0,295 %                          [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,119 %                                     [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,119 %                                     [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,133 %                                 [INAKTIV]
6. VIX-Filter (>30):          18,28 (Pre-Wert, kein Update Midday)         [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Option A Strategie-Lock aktiv (V1_neu 349,70 < Kurs 353,43 = +1,07 % positiv, kein Sofort-Stop-Risiko) | V Q3 ab Do 23.07. Close [WARN — Owner-Pending] |
8. Max Käufe KW30:            1/2 (V gefüllt, Slot 2/2 offen)              [FREI 1]
```

**Entscheidung Midday 13:08 Mo 20.07.:** **Keine Aktion** — regelkonform (alle V1 SICHER, kein TP-Trigger, Daily Cap fern). **PushNotification Prio 2 an Owner** wegen GS-Puffer +0,41 % (unter historischem Minimum, Fill-Day+3-Muster-Warnung). **Kein ClickUp-Alert** (Routine-Regel: nur bei Stop-Auslösung oder Daily-Cap). 

**Nächste Routine:** Mo 20.07. 16:00 ET Market Close — **GS V1 1.050,40 zwingend prüfen** (Sofort-Sell bei Break), GOOGL V1 338,65 + Blackout-Aktivierungs-Frage, V Fill-Day+0 Close-Bar für V2-Trail-Berechnung.

---

## Market Open 2026-07-20 09:41 ET (Mo, KW30 Tag 1) — V-Kauf gefüllt Slot 1/2, alle 7 V1 SICHER, GS/GOOGL Rebound

```
Alpaca clock:      is_open=true | next_close Mo 20.07. 16:00 ET
Equity:            98.402,10 $   (Alpaca /v2/account, post V-Fill)
Cash:              40.026,28 $   (40,68 %, post V-Kauf 9.643,80 $ verbraucht)
Portfolio MV:      58.352,91 $   (59,32 %, 7 Positionen)
Buying_power:     323.557,42 $
Daily P/L:          +166,05 $     (+0,169 % vs last_equity 98.236,14)      [GRÜN]
ATH:              100.066,47 $   DD -1,664 % [GRÜN — Alarm bei -15 %]
Weekly KW30:        +0,169 %     (Tag 1, positiver Start)                   [GRÜN]
Käufe KW30:            1/2       (V gefüllt, Slot 2/2 verfügbar bis Fr)     [FREI 1]
VIX:                18,28        (Perplexity spot Pre)                       [GRÜN]
SPY Live 09:38:    748,22        (vs Fr-Close 743,28 = +0,665 %)             [POSITIV]
Guardrails: alle 8 GRÜN | Kauf-Slot 1/2 belegt V
```

**Positionen Live 09:41 ET nach V-Fill — sortiert nach Puffer ENG→WEIT:**

| Sym    | Live       | Fr-Close | Chg      | P/L %    | V1-Stop       | V1-Puffer  | Status |
|--------|------------|----------|----------|----------|---------------|------------|--------|
| **GS** | 1.079,81   | 1.065,22 | +1,37 %  | -5,43 %  | 1.050,40      | **+2,80 %**| SICHER **KRITISCH** (Rebound vs Fr +1,34 pp) |
| **GOOGL**|  356,78  | 346,77   | +2,88 %  | -3,08 %  | 338,65        | **+5,35 %**| SICHER (Rebound vs Fr +2,95 pp, Blackout Owner-Pending) |
| LLY    | 1.174,47   | 1.179,11 | -0,39 %  | -1,63 %  | 1.098,38      | +6,93 %    | SICHER |
| V (NEU)|   357,18   | 358,51   |  Fill 0 % | +0,00 %  |  328,60       | +8,70 %    | SICHER (Fill-Day+0) |
| JPM    |   343,37   | 341,10   | +0,67 %  | +3,18 %  |  306,16       | +12,16 %   | SICHER |
| AAPL   |   331,25   | 333,74   | -0,75 %  | +4,54 %  |  291,51       | +13,64 %   | SICHER |
| UNH    |   421,45   | 426,09   | -1,08 %  | +4,95 %  |  369,44       | +14,08 %   | SICHER |

**V-Kauf-Details:**
- **Alpaca Order-ID:** 85d11ad8-fccc-4c6f-a55c-5cc6695999a2 — Fill 09:41:19 ET (3 sec)
- **Fill-Preis:** 357,177778 $ × 27 Shares = 9.643,80 $ (9,80 % Portfolio, unter Limit 360,30 = -0,87 % Vorteil)
- **Stops:** V1 328,60 (-8 %) | V2 314,32 (-12 %) | TP1 428,62 (+20 %) | TP2 482,20 (+35 %)
- **K1-K5 alle grün:** EMA-Spread +3,61 marginal | RSI 62,68 | RS_63d +7,82 % | Vol 157 % Avg20 | FwdPE 24-27 (Median 25) | RevGrowth 17 % Q2 FY26
- **Konkurrenz-Rejects:** PANW K5-FAIL (FwdPE 55-77 Multi-Source > 35, analog AMD); XLV-Trio (ABBV/MRK/JNJ) K1-K3 grün aber Sektor-Cap-Deutung Owner-Pending
- **Nächstes Ereignis:** V Q3 FY26 Earnings ~28.-29.07. AMC → Blackout aktivierbar Do 23.07. Close

**Sektor-Gewichte nach V-Fill:**
| Sektor | Positionen | MV       | % investiert | % Portfolio | Status |
|--------|------------|----------|--------------|-------------|--------|
| XLF    | GS+JPM+V   | 19.309   | 33,08 %      | 19,62 %     | **⚠ investiert > 30 %**, Portfolio SAFE |
| XLV    | UNH + LLY  | 19.489   | 33,39 %      | 19,80 %     | **⚠ investiert > 30 %**, Portfolio SAFE |
| XLK    | AAPL       | 10.279   | 17,62 %      | 10,45 %     | GRÜN |
| XLC    | GOOGL      |  9.276   | 15,90 %      |  9,43 %     | GRÜN |

**⚠ Sektor-Cap-Deutungs-Frage:** V-Kauf hebt XLF auf 33,08 % investiert (analog XLV mit UNH+LLY 33,39 %). Am Gesamtportfolio (98.402) beide ~19-20 % → **unter Cap wenn Portfolio-Basis, verletzt bei investiert-Basis-Deutung** → **Owner-Klärung übertragen von XLV auf XLF-Kontext** (Weekly Review KW30 Grundsatz-Klärung zwingend).

**Guardrails alle 8 GRÜN nach V-Fill:**
```
1. Daily Loss Cap (-3 %):     +0,169 % (Daily positiv nach V-Kauf)         [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 1 +0,169 %                          [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,664 %                                     [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,664 %                                     [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,665 % positiv                         [INAKTIV]
6. VIX-Filter (>30):          18,28                                        [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Blackout aktiv (V1_neu 349,70 < Kurs 356,78 = +1,99 % positiv, kein Sofort-Stop-Risiko wie Fr) | V Q3 ab Do 23.07. Close [WARN — GOOGL Option A Strategie-Lock, Owner-Pending] |
8. Max Käufe KW30:            1/2 (V gefüllt)                              [FREI 1]
```

**Entscheidung Market Open 09:41 Mo 20.07.:** **V-Kauf ausgeführt** — Slot 1/2 belegt. **Keine Sell-Order** (alle 7 V1 SICHER, GS/GOOGL Rebound schließt kritisches Watch-Fenster nicht ab). PushNotification Prio 2 + ClickUp TRADE_BUY Alert Prio 3 versendet.

**Nächste Routine:** Mo 20.07. 13:00 ET Midday Stop-Check — V Fill-Day-Drop-Muster-Watch (AVGO/MU-Präzedenz), GS/GOOGL Rebound-Verhalten fortsetzen, alle anderen V1 SICHER.

---

## Pre-Market 2026-07-20 08:36 ET (Mo, KW30 Tag 1) — Alle 6 V1 SICHER, GS/GOOGL leicht erholt aber Puffer <3% weiter kritisch, VIX 18,28 GRÜN, SPY Pre +0,44%, Kaufscan Open FREIGEGEBEN

```
Alpaca clock:      is_open=false | next_open Mo 20.07. 09:30 ET
Equity:            98.240,91 $   (Alpaca /v2/account, Pre-Market)
Cash:              49.670,08 $   (50,56 %, unverändert)
Portfolio MV:      48.572,91 $   (49,44 %, 6 Positionen)
Buying_power:     334.678,64 $
Daily P/L Pre:       +4,77 $      (+0,005 % vs last_equity 98.236,14)   [GRÜN, flat]
ATH:              100.066,47 $   DD -1,828 % [GRÜN — Alarm bei -15 %]
Weekly KW30:        0,000 %      (Tag 1 Start, RESET)                    [GRÜN]
Käufe KW30:            0/2       (LOCK-Ende, Slot 2/2 verfügbar)         [FREI]
VIX:                18,28        (Perplexity spot, alt. 20,95)           [GRÜN]
SPY Pre-Market:   746,58        (IEX Quote vs Fr-Close 743,28 = +0,44 %) [POSITIV]
10Y Yield:          ~4,55 %      (Perplexity carry-over 17.07.)
Guardrails: alle 8 GRÜN → Kauf-Scan Open FREIGEGEBEN
```

**Positionen Pre-Market V1-Check (Alpaca /v2/positions 08:36 ET) — sortiert nach Puffer ENG→WEIT:**

| Sym    | Pre-Market | Fr-Close | Chg PM   | P/L %    | V1-Stop       | V1-Puffer  | Δ pp     | Status |
|--------|------------|----------|----------|----------|---------------|------------|----------|--------|
| **GS** | 1.070,99   | 1.065,22 | +0,54 %  | -6,20 %  | 1.050,40      | **+1,96 %**| +0,50    | SICHER **KRITISCH** (Fill-Day+3, weiter <3 %) |
| **GOOGL**|  348,32  | 346,77   | +0,45 %  | -5,37 %  | 338,65        | **+2,86 %**| +0,46    | SICHER **KRITISCH** (Blackout-Konflikt aktiv, Owner-Pending) |
| LLY    | 1.175,00   | 1.179,11 | -0,35 %  | -1,58 %  | 1.098,38      | +6,98 %    | -0,32    | SICHER |
| JPM    |   341,50   | 341,10   | +0,12 %  | +2,62 %  |  306,16       | +11,54 %   | +0,13    | SICHER |
| AAPL   |   332,07   | 333,74   | -0,50 %  | +4,80 %  |  291,51       | +13,91 %   | -0,58    | SICHER |
| UNH    |   426,25   | 426,09   | +0,04 %  | +6,15 %  |  369,44       | +15,37 %   | +0,05    | SICHER |

**Perplexity Daily Macro:** VIX 18,28 [GRÜN]; SPY Pre +0,44 % [positiv]; 10Y ~4,55 %; kein Fed/CPI/PPI heute; **Top News: Global Chipmakers-Selloff (AI-Valuation) → XLK-Belastung → PANW-Kaufwatch VORSICHT**, S&P 500 auf 1-Wo-Tief.

**Earnings-Blackout (3 HT):**
- **GOOGL 22.07. AMC** (carry-over) → **Blackout aktiv Mo-Mi 20.-22.07.** — Konflikt Owner-Pending
- AAPL 30.07. AMC — außerhalb
- GS/JPM/LLY/UNH — kein Ereignis Mo-Fr 20.-24.07.

**Guardrails (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,005 % (PM flat)                             [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 1 Start 0,000 %                       [GRÜN — RESET]
3. Drawdown-Alarm (-15 %):    -1,828 % vs ATH 100.066,47                     [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,828 %                                       [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Fr -1,011 %                                [INAKTIV]
6. VIX-Filter (>30):          18,28 (Perplexity)                             [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Blackout aktiv, Konflikt Owner-Pending   [WARN]
8. Max Käufe KW30:            0/2 (Slot 2/2 verfügbar)                       [FREI]
```

**GS Fill-Day+3 Kontext:** kumuliert -6,20 % seit Fill 15.07. → Präzedenz AVGO Fill-Day+3 -8,69 % V1 / MU Fill-Day+4 -10,92 % V1 → **im kritischen Fenster**. Bei Puffer +1,96 % sind bereits 24,5 % des V1-Weges verbraucht.

**GOOGL-Blackout-Regel-Entscheidung Fortsetzung Option A (Strategie-Lock):**
- V1_neu Blackout 349,70 (368,10×0,95) > PM-Kurs 348,32 = **-0,40 % negativ** (entspannt vs Fr-Close -0,84 %)
- **Standard V1 338,65 bleibt aktiv** — Blackout-Tightening würde bei Aktivierung Sofort-Stop auslösen ohne Owner-Freigabe
- **Owner-Frage weiter offen** — Fr-Notification unbeantwortet, heute (Blackout-Beginn) akut

**Watchlist KW30-Slot 1/2 (Open-Scan):**
- **LEAD V (Visa)** XLF — kein Sektor-Cap-Risiko, Kauf-Fenster Mo-Mi vor Blackout 23.07. Close, K5-Multi-Source zwingend
- **LEAD PANW (Palo Alto)** XLK — Chip-Selloff-Sorge belastet Sektor, K5-Multi-Source-FwdPE **doppelt zwingend** (Cybersecurity typisch > 35)
- **Backup XLV** (ABBV/MRK/JNJ) — nur bei Sektor-Cap-Deutung-Freigabe

**Entscheidung Pre-Market 08:36 Mo 20.07.:** **Alle 6 V1 SICHER**, keine Sell-Order. GS/GOOGL im weiterhin kritischen Watch-Fenster (Puffer <3 %, aber leichte PM-Erholung +0,50 pp). **Kaufscan Open FREIGEGEBEN** (Guardrails GRÜN, Slot 2/2 KW30). PushNotification Prio 2 an Owner (GS/GOOGL Puffer-Update + GOOGL-Blackout weiter Owner-Pending + Chip-Selloff-Sektor-Kontext).

**Nächste Routine:** Mo 20.07. 09:30 ET Market Open + Kauf-Scan KW30 (V/PANW K5-Multi-Source-Recheck, XLV-Backup nur bei Freigabe; GS/GOOGL V1-Watch zwingend engmaschig).

---

## Wochenabschluss KW29 — 2026-07-17 (Fr) (carry-over)

```
Gesamtwert:        98.211,21 $   (Alpaca /v2/account equity Fr-Close carry)
Cash:              49.670,08 $   (50,58 %)
Investiert:        48.541,13 $   (49,42 %)
Wochenrendite:      -0,417 %     (Basis Fr-Close 10.07. 98.622,21 → Fr 17.07. 98.211,21)
SPY-Woche:          -1,544 %     (Alpaca IEX 754,94 → 743,28)
Alpha vs SPY:       +1,128 %     [POSITIV — Cash-Puffer 50 % + XLV-Rebound Fr dämpft XLK-Loss]
YTD Rendite:        -1,789 %     (Startkapital 100.000 $)
YTD Alpha:         -10,803 %     (SPY YTD +9,014 % vs YE25 681,82)
ATH:              100.066,47 $   (16.06.2026 carry-over)
Drawdown:           -1,854 %     [GRÜN — Alarm bei -15 %]
Offene Positionen:      6/8      (AAPL, JPM, UNH, LLY, GOOGL, GS)
Realisiert kumuliert: -1.615,62 $ (AVGO -596,19 + MU -1.019,43; keine geschlossenen Trades KW29)
Käufe KW29:            2/2 LOCK  (AAPL Mo + GS Mi, LOCK endet Mo 20.07. KW30)
Nächste Woche max. Käufe: 2 (Slot 2/2 verfügbar ab Mo 20.07.)
```

**Watchlist KW30 (Mo 20.07.):**
- **LEADS (kein Sektor-Cap-Risiko):** V (XLF, RS +7,82 %, K5 Mo Pre zwingend) | PANW (XLK, RS +108,86 % #1, K5 Mo Pre zwingend)
- **Backup (XLV-Sektor-Cap-Risiko):** ABBV (RS +15,89 %) | MRK (RS +4,45 %) | JNJ (RS +1,92 %)
- **Reduktions-Watch bei XLV-Cap-Streng-Deutung:** LLY (schwächste XLV-Position, P/L -1,28 %)

**Sektorgewichte-Check (Investiert-Basis vs Portfolio-Basis):**
| Sektor | Positionen | MV       | % investiert | % Portfolio | Status |
|--------|------------|----------|--------------|-------------|--------|
| XLV    | UNH + LLY  | 19.655   | **40,49 %**  | 20,01 %     | **⚠ Deutung-Konflikt** (streng > 30 %, Portfolio < 30 %) |
| XLK    | AAPL       | 10.344   | 21,31 %      | 10,53 %     | GRÜN |
| XLF    | GS + JPM   | 9.546    | 19,67 %      | 9,72 %      | GRÜN |
| XLC    | GOOGL      | 9.002    | 18,55 %      | 9,17 %      | GRÜN |

Weekly-Review-Routine-Wortlaut: „Kein Sektor > 30 % des investierten Kapitals" → **XLV verletzt Deutung streng.** Am Gesamtportfolio (98.211) nur 20,01 % → unter Cap. **Grundsatz-Klärung Owner Mo zwingend.**

**Guardrails Fr-Close 17.07.:**
```
1. Daily Loss Cap (-3 %):     -0,312 %                                      [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,417 % KW29 Final                           [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,854 % vs ATH 100.066,47                    [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,854 %                                      [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -1,011 % Fr                               [INAKTIV]
6. VIX-Filter (>30):          ~15-17 (Perplexity Rotation defensive-heavy) [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Blackout-Konflikt Owner-Pending         [WARN]
8. Max Käufe KW30 (Reset):    0/2 verfügbar Mo 20.07.                       [OFFEN]
```

**Nächste Routinen:**
- Mo 20.07. 08:30 ET Pre-Market Check — GS V1 1.050,40 (Puffer +1,46 %) + GOOGL V1 338,65 (Puffer +2,40 %) zwingender Watch; Owner-Entscheidungen (Blackout-Konflikt + Sektor-Cap-Deutung) vor Open erforderlich.
- Mo 20.07. 09:30 ET Market Open + Kaufsignal-Scan KW30 — V/PANW K5-Multi-Source-Recheck; ABBV/MRK/JNJ nur wenn XLV-Cap-Grundsatz geklärt.
- Fr 24.07. 17:00 ET Weekly Review KW30.

---

## Market Close 2026-07-17 16:02 ET (Fr, KW29 Tag 5) — Tagesbilanz, alle V1-V6 SICHER, GS/GOOGL Puffer <3% kritisch, GOOGL-Blackout-Konflikt Owner-Entscheidung, Alpha +0,70% daily / +1,13% weekly

```
Alpaca clock:      is_open=false | next_open Mo 20.07. 09:30 ET | next_close Mo 20.07. 16:00 ET
Gesamtwert:        98.216,93 $   (Alpaca equity Close)
Cash:              49.670,08 $   (50,57 %, unverändert seit GS-Fill Mi 15.07.)
Investiert (MV):   48.546,85 $   (49,43 %, AAPL 10.344 + JPM 1.024 + UNH 10.222 + LLY 9.433 + GOOGL 9.002 + GS 8.522)
Buying_power:     334.611,50 $
P/L heute:           -307,78 $   (-0,3124 %)   [GRÜN — vs Alpaca last_equity 98.524,71, Cap -3 %]
SPY-Tag:            -1,011 %     (Alpaca IEX 750,87 → 743,28)
Alpha vs SPY:       +0,699 %     [POSITIV — trotz XLK-Sektor-Verlust -2,24 %, Portfolio dank Cash-Puffer 50 % relativ stärker]
ATH:              100.066,47 $   DD -1,848 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW29:    -0,411 %     (Tag 5, Basis Fr-Close 98.622,21 laut Alpaca-History)      [GRÜN — Cap -5 %]
Weekly Alpha KW29:  +1,134 %     (vs SPY -1,544 % Fr→Fr 754,94→743,28)                     [POSITIV]
Käufe KW29:            2/2 LOCK  (AAPL Mo + GS Mi gefüllt — LOCK endet Mo 20.07. KW30)     [LOCK]
Pending Orders:        0         (V5/V6 alle 6 SICHER — KEINE Limit-Order für Mo 20.07.)
VIX-Ref:            ~15-17       (Perplexity Sektor-Rotation defensive-heavy)               [GRÜN]
Guardrails: Daily -0,31 % | Weekly -0,41 % | DD -1,85 % | VIX ~16 | Käufe 2/2 LOCK → ALLE GRÜN
```

**Positionen Close V1-V6 (Alpaca IEX 304d Bars, Wilder EMA/RSI):**

| Sym    | Close     | P/L      | Chg_today | V1-Stop        | V1-Puffer  | V5 Spread | V6 RSI | V6 RS_4w  | Status |
|--------|-----------|----------|-----------|----------------|------------|-----------|--------|-----------|--------|
| UNH    |   426,06  | +6,10 %  | +0,60 %   | 369,44 ✓Reset  | +15,32 %   | +48,93    | 57,87  | +6,32 %   | SICHER (Post-Q2-Konsolidierung Tag 2 stabil, komfortabel) |
| AAPL   |   333,75  | +5,33 %  | +0,13 %   | 291,51 (-8 %)  | +14,49 %   | +29,62    | 72,25  | +12,42 %  | SICHER (Tages-Sieger relativ, RSI 72,25 höchste aber <80, XLK-Rebell) |
| JPM    |   341,10  | +2,50 %  | -0,55 %   | 306,16 (-8 %)  | +11,41 %   | +16,11    | 60,21  | +1,95 %   | SICHER (leichter Give-back Post-Q2 Tag 4, RS_4w positiv geblieben) |
| LLY    | 1.178,57  | -1,28 %  | +0,85 %   | 1.098,38 (-8 %)| +7,30 %    | +132,25   | 54,91  | +5,67 %   | SICHER (Reversal-Fortsetzung Tag 3, XLV +2,22 % Sektor-Rückenwind) |
| **GOOGL**|  346,76 | -5,80 %  | -2,32 %   | 338,65 (-8 %)  | **+2,40 %**| +46,59    | 42,37  | -5,00 %   | SICHER **KRITISCH** (Fill-Day+8 Follow-Through, XLC/XLK-Rotation-Verlierer, Blackout-Konflikt aktiv) |
| **GS** | 1.065,71  | -6,66 %  | -2,76 %   | 1.050,40 (-8 %)| **+1,46 %**| +127,35   | 51,42  | -3,31 %   | SICHER **KRITISCH** (Fill-Day+2 Drop-Muster VOLLBILD, Puffer engste, XLF neutral) |

**V1-V6-Check: ALLE 6 POSITIONEN SICHER.** → **KEINE Sell/Limit-Order für Mo 20.07. platziert.**
- V1 alle SICHER (GS engste +1,46 %, GOOGL +2,40 %; beide <3 % → weiter im kritischen Watch)
- V2-Trails aktualisiert (siehe Trade-Log — nur AAPL marginal neues Hoch 334,98)
- V3/V4 nicht ausgelöst (UNH beste P/L +6,10 % weit unter +20 %)
- V5 alle SICHER (Spreads +16 bis +132, kein Death-Cross-Risiko)
- V6 alle SICHER (max RSI 72,25 AAPL <<80; GOOGL RSI 42,37 + RS_4w -5,00 % erfüllt Teil-Bedingung V6 aber RSI <<80 → verlangt BEIDES; GS RSI 51,42 + RS_4w -3,31 % analog)

**GOOGL-Blackout-Konflikt — REGEL-ENTSCHEIDUNG:**
- Q2-Earnings am 22.07. AMC = 3 HT vor Earnings → Blackout-Aktivierung heute Close (Fr 17.07.)
- V1_neu Blackout = 368,10 × 0,95 = **349,70 (-5 %)** vs Standard V1 338,65 (-8 %)
- Kurs Close **346,76 < V1_neu 349,70** = **-0,84 % negativ** → Blackout-Tightening würde Sofort-Stop bei Aktivierung auslösen
- **Regel-Entscheidung (Strategie-Lock, Option A gemäß Pre-Market/Open/Midday-Dokumentation):**
  - Standard V1 338,65 BLEIBT AKTIV (V1 nicht getroffen, +2,40 % Puffer)
  - Blackout-Tightening 349,70 wird **NICHT** aktiviert → würde Regel-Abweichung ohne Owner-Freigabe verlangen
  - Begründung: Strategie-Lock „Bei Konflikt: nicht handeln" (CLAUDE.md Pflicht-Regel 3) — der Blackout-Zweck (Schutz vor Post-Earnings-Gap) ist ex-ante gedacht, nicht ex-post-Trigger
- **Owner-Freigabe erforderlich** vor Mo 20.07. Open: PushNotification Prio 2 mit expliziter Frage
- **Fallback-Szenario Mo 20.07. Open:** Wenn Owner keine Freigabe erteilt und Kurs weiter fällt, Standard-V1 338,65 fängt bei -8 % → nur -2,40 % Puffer bis Break

**GS Fill-Day+2 Drop-Muster VOLLBILD — Präzedenz erfüllt:**
- Fill 15.07.: 1.141,74 → Fr Close: 1.065,71 = -6,66 % kumuliert in 3 Handelstagen
- Muster-Präzedenz: AVGO Fill-Day+3 -8,69 % V1-Stop | MU Fill-Day+4 -10,92 % V1-Stop → GS Fill-Day+2 -6,66 % noch VOR V1-Break
- V1 1.050,40 Puffer +1,46 % = **ENGSTE Position im Portfolio**, Break Mo → Market-Sell sofort
- V6 Teil-Bedingung (RS_4w -3,31 %) erfüllt, aber RSI 51,42 <<80 → V6 nicht ausgelöst
- Positions-Beitrag Close: -612,03 $ = -0,624 % vom Portfolio (belastet Alpha aber Cash-Puffer 50 % dämpft)

**GOOGL Nachmittags-Kollaps-Fortsetzung Fr Tag 5:**
- Do Close 354,87 chg -4,33 % (Nachmittags-Kollaps) → Fr Close 346,76 chg -2,32 %
- Kumuliert Do-Fr: 371,37 (Do Midday) → 346,76 (Fr Close) = **-6,63 % in 1,5 Handelstagen**
- Fill-Preis 368,10 → Fr Close 346,76 = -5,80 % kumuliert (Fill-Day+8)
- V1 338,65 Puffer +2,40 % = 2. engste Position
- RS_4w -5,00 % verschärft (V6 Teil-Erfüllung) — XLC-Rotation-Verlierer bestätigt via Perplexity XLK -2,24 %

**UNH Post-Q2-Konsolidierung Tag 2:**
- Do Close 421,14 → Fr Close 426,06 = +1,17 % (chg +0,60 %)
- Rally-Give-back-Fortsetzung vom 460,95-Hoch ausgeblieben, stabilisiert
- P/L +6,10 % / V1-Puffer +15,32 % komfortabel / V2-Trail 405,64 (Hoch 460,95 Do carry-over) +4,99 % Puffer
- XLV +2,22 % Sektor-Rebound getragen

**LLY-Reversal-Fortsetzung Tag 3:**
- Do Close 1.170,50 → Fr Close 1.178,57 = +0,69 % (chg +0,85 %)
- P/L -1,28 % (verbessert von Do -1,96 % → Fr -1,28 %)
- V1-Puffer +7,30 % (leicht verbessert vs Do +6,57 %)
- XLV +2,22 % Sektor-Rückenwind

**AAPL Tag-5-Stabilität — XLK-Rebell:**
- Do Close 332,81 → Fr Close 333,75 = +0,28 % (chg +0,13 %)
- P/L +5,33 % vs XLK -2,24 % Sektor-Verlust = **+7,57 % relativer Outperform!**
- Neues Fill-Day-Hoch H=334,98 (marginal vs Do 334,65) → V2-Trail-Update auf 294,78 (vs 294,49)

**JPM Tag-4-Give-back:**
- Do Close 343,15 → Fr Close 341,10 = -0,60 % (chg -0,55 %)
- P/L +2,50 % (verschlechtert von +3,12 %)
- V1-Puffer +11,41 % komfortabel

**V2-Trailing-Stop-Update (nur AAPL):**
| Sym | Tageshoch Fr | Neuer V2 (×0,88) | Alt V2 | Status |
|-----|--------------|------------------|--------|--------|
| AAPL|  334,98      |   294,78         | 294,49 | **AKTUALISIERT** (marginal neues Fill-Day-Hoch, +0,10 %) |
| JPM |  346,10      |   304,57         | 306,97 | unverändert (V2 trailt nur UP, altes Hoch 348,83 höher) |
| UNH |  437,13      |   384,67         | 405,64 | unverändert (V2 trailt nur UP, altes Hoch 460,95 höher) |
| LLY | 1.187,635    | 1.045,12         |1.098,70| unverändert (V2 trailt nur UP, altes Hoch 1.248,53 höher) |
| GOOGL|  348,47     |   306,65         | 330,16 | unverändert (V2 trailt nur UP, altes Hoch 375,18 höher) |
| GS  | 1.084,70     |   954,54         |1.013,45| unverändert (V2 trailt nur UP, altes Hoch 1.151,65 höher) |

**Sektor-Kontext (Perplexity Close-Report Fr 17.07.):**
- XLK -2,24 % (Semiconductor-Chaos: NVDA, AMD, INTC; AI-Überhitzung) → GOOGL/AAPL Reingung
- XLV +2,22 % (UNH Q2-Beat, MRK neue Produktlinien) → UNH/LLY Rückenwind
- XLP +2,80 % (Defensiv-Rotation)
- XLE +0,92 % (Iran-Risiken → Ölpreis fest)
- XLI +0,05 % (nahezu flach)
- SPY -1,011 % (Alpha-Basis)

**Weekly Loss Cap Check KW29 (Basis Fr-Close 10.07. = 98.622,21):**
- Equity Fr-Close 17.07.: 98.216,93 → Weekly P/L **-0,411 %**
- Cap -5 % → weit entfernt (Puffer +4,589 %) → **KEIN Weekly-Cap-Auslöser**
- Keine Cancel-Aktion erforderlich, keine Kauf-Sperre bis Mo (LOCK ist ohnehin auf 2/2 KW29 erschöpft, Reset Mo 20.07.)

**Watchlist Mo 20.07. + KW30 Käufe (Slot 2/2 verfügbar, LOCK-Ende):**
Alpaca-Screener 25 Symbole gescannt → **5 K1-K3 LEADS 3/3:**
1. **V (Visa) 358,51** — XLF, K1 +4,13 (EMA-Spread marginal ✓), K2 RSI 62,68 ✓, K3 RS_63d **+7,82 %** ✓ — Kauf-Fenster **Mo-Mi 20.-22.07.** (Blackout ab 23.07. Close, Q3 ~28.07. AMC bestätigt aus Do-Watchlist). K5-Multi-Source-FwdPE Mo Pre-Market zwingend.
2. **PANW (Palo Alto) 358,62** — XLK Cybersecurity, K1 +64,20 ✓, K2 RSI 67,33 ✓, K3 RS_63d **+108,86 % #1** — K5-Multi-Source-FwdPE **zwingend** (Cybersecurity typisch > 35 wie AMD-Reject-Analogie).
3. **ABBV 254,52** — XLV, K1 +14,42 ✓, K2 RSI 64,43 ✓, K3 RS_63d **+15,89 %** ✓ — **XLV Sektor-Cap-Risiko** (UNH + LLY = 2 XLV-Positionen bereits; ABBV = 3. wäre max 30 %-Cap-Grenze bei aktueller Größe unkritisch, aber Regel-Check erforderlich). Earnings Ende Juli — Blackout-Check zwingend.
4. **MRK 127,48** — XLV, K1 +12,31 ✓, K2 RSI 57,87 ✓, K3 RS_63d +4,45 % ✓ — analoges Sektor-Risiko wie ABBV.
5. **JNJ 253,01** — XLV, K1 +23,63 ✓, K2 RSI 54,42 ✓, K3 RS_63d +1,92 % ✓ — analoges Sektor-Risiko wie ABBV.

**Sektor-Cap-Prioritäten Mo:** V (XLF) und PANW (XLK) haben KEIN Sektor-Cap-Risiko und werden priorisiert. XLV-Kandidaten (ABBV/MRK/JNJ) nur als Backup falls V/PANW K5 fail.

**NVDA/AMZN/META/XOM/CVX K3-Fail** (RS negativ trotz K1/K2 grün). **AMD K5-blocked** (Multi-Source-Recheck von Di 14.07. → FwdPE > 35 permanent). **CAT/AMAT/MU/BAC/MS K2-Fail** (RSI außerhalb 50-70).

**Guardrails (alle 8) Close-Snapshot:**
```
1. Daily Loss Cap (-3 %):     -0,312 %                                      [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,411 % (KW29 Tag 5 Final)                   [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,848 % vs ATH 100.066,47                    [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,848 %                                      [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -1,011 %                                  [INAKTIV]
6. VIX-Filter (>30):          ~15-17 (Perplexity Rotation defensive-heavy) [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Blackout-Konflikt Owner-Pending         [WARN]
8. Max Käufe KW29:            2/2 LOCK → Reset Mo 20.07. KW30              [LOCK-ENDE]
```

**ClickUp:** Task-Anlage **FEHLGESCHLAGEN** (Tier-Limit ITEM_246 „Max usage for custom task types reached" — carry-over Bug). PushNotification Prio 2 an Owner ersetzt Delivery: enthält Tagesbilanz + GOOGL-Blackout-Konflikt Option-Entscheidung + GS/GOOGL Puffer-Watch + Watchlist Mo.

> **Entscheidung Close 16:02 Fr 17.07.:** **Alle 6 V1-V6 SICHER**, KEINE Sell/Limit-Order für Mo 20.07. platziert (regelkonform Halten). Alpha positiv (+0,70 % daily, +1,13 % weekly) trotz XLK-Sektor-Verlust dank Cash-Puffer 50 % und XLV-Rebound. GS/GOOGL bleiben mit <3 % V1-Puffer im kritischen Watch-Fenster. **GOOGL-Blackout-Konflikt regelkonform Option A** (Standard-V1 338,65 aktiv, Owner-Freigabe pending). Käufe-LOCK endet Mo 20.07. — KW30 Slot 2/2 verfügbar, Watchlist V/PANW priorisiert (XLV-Backup ABBV/MRK/JNJ).
> **Nächste Routine:** Mo 20.07. 08:30 ET Pre-Market Check — **GS V1 1.050,40 (Puffer +1,46 %) zwingender Pre-Market-Watch**, **GOOGL V1 338,65 (Puffer +2,40 %) + Owner-Entscheidung Blackout**, K5-Recheck V/PANW für KW30-Slot 1 vorbereitend.

---

## Midday 2026-07-17 13:07 ET (Fr, KW29 Tag 5) — Alle 6 V1-V4 SICHER, GS/GOOGL leicht erholt aber Puffer <3% weiter KRITISCH

```
Alpaca clock:      is_open=true | next_close 17.07. 16:00 ET
Equity:            98.390,73 $   (Live 13:07 ET)
Cash:              49.670,08 $   (50,48 %, unverändert)
Portfolio MV:      48.726,53 $   (49,52 %, 6 Positionen)
Buying_power:     335.098,13 $
Daily P/L:           -133,98 $   (-0,136 % vs Alpaca last_equity 98.524,71)   [GRÜN — Cap -3 %]
ATH:              100.066,47 $   DD -1,674 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW29:    -0,234 %     (Tag 5, Basis Fr-Close 98.621,81)             [GRÜN — Cap -5 %]
Käufe KW29:            2/2 LOCK  (bis Mo 20.07. KW30)                          [LOCK]
Pending Orders:        0
Guardrails: Daily -0,14 % | Weekly -0,23 % | DD -1,67 % | Käufe 2/2 LOCK → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca /v2/positions 13:07 ET) — sortiert nach Puffer ENG→WEIT:**

| Sym    | Curr      | P/L      | V1-Stop        | V1-Puffer  | V2-Trail  | V2-Puffer  | Status |
|--------|-----------|----------|----------------|------------|-----------|------------|--------|
| **GOOGL**|  346,53 | -5,85 %  |  338,65 (-8 %) | **+2,33 %**| 330,16    | +4,96 %    | SICHER **KRITISCH** (verbessert vs Open +1,65 %, aber immer noch <3 % Puffer) |
| **GS** | 1.080,05  | -5,38 %  | 1.050,40 (-8 %)| **+2,82 %**| 1.013,45  | +6,57 %    | SICHER **KRITISCH** (verbessert vs Open +1,26 %, Fill-Day+2 Drop-Muster VOLLBILD) |
| LLY    | 1.178,93  | -1,28 %  | 1.098,38 (-8 %)| +7,33 %    | 1.098,70  | +7,30 %    | SICHER (Reversal-Fortsetzung Tag 3, +0,72 % chg_today) |
| JPM    |   343,21  | +3,14 %  |  306,16 (-8 %) | +12,10 %   | 306,97    | +11,81 %   | SICHER (leichter Rebound Post-Q2 Tag 4) |
| AAPL   |   330,03  | +4,17 %  |  291,51 (-8 %) | +13,21 %   | 294,49    | +12,07 %   | SICHER (Fill-Day+4 stabil) |
| UNH    |   432,59  | +7,72 %  |  369,44 ✓Reset | +17,09 %   | 405,64    | +6,64 %    | SICHER (Post-Q2-Konsolidierung, Tages-Sieger +1,71 % chg) |

**V1-V4-Check: ALLE 6 POSITIONEN SICHER.** → **Keine Sell/Limit-Order platziert.**
- V1 alle SICHER (GOOGL engste +2,33 %, dann GS +2,82 %)
- V2 alle SICHER (UNH V2-Trail 405,64 engste bei +6,64 % Puffer)
- V3/V4 nicht ausgelöst (UNH beste P/L nur +7,72 %, weit unter +20 %)
- RSI/EMA werden bei Midday nicht geprüft (nur Market Open/Close)

**Puffer-Entwicklung vs Open 09:37 ET:**
- GS: +1,26 % → +2,82 % (**+1,56 %-Punkte verbessert**, Erholung von Fill-Day+2-Tief)
- GOOGL: +1,65 % → +2,33 % (**+0,68 %-Punkte verbessert**, leicht rekonsolidiert nach Do-Nachmittags-Kollaps)
- Beide Puffer bleiben **<3 %** → weiter kritischer Watch bis Close

**Guardrails (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,136 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,234 % (KW29 Tag 5)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,674 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,674 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   (nicht abgerufen — Daily -0,14 %)     [INAKTIV]
6. VIX-Filter (>30):          ~17 (carry-over)                      [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL ab Close heute aktivierbar      [ÜBERGANG]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30           [LOCK]
```

**ClickUp:** KEIN Alert (kein Stop ausgelöst, Daily Cap weit weg — Regel: kein Log um ClickUp nicht zu überfluten). PushNotification Prio 2 an Owner wegen weiterhin kritischer Puffer GS/GOOGL.

> **Entscheidung Midday 13:07 Fr 17.07.:** **Alle 6 V1-V4 SICHER**, keine Sell-Order (V1 nicht erreicht, regelkonform Halten). GS und GOOGL haben sich vom Open leicht erholt (Puffer +1,56 pp / +0,68 pp), bleiben aber mit <3 % Puffer im kritischen Watch-Fenster. Daily -0,136 % [GRÜN weit von Cap -3 %].
> **Nächste Routine:** Fr 17.07. 16:00 ET Market Close (GOOGL-Blackout-Aktivierung + V1-Tightening 349,70 zwingend prüfen; V5/V6-Check für Mo 20.07.).

---

## Market Open 2026-07-17 09:37 ET (Fr, KW29 Tag 5) — Alle 6 V1 SICHER, aber GS/GOOGL Puffer <2% KRITISCH, kein Kauf-Scan (LOCK), GOOGL-Blackout-Konflikt verschärft

```
Alpaca clock:      is_open=true | next_close 17.07. 16:00 ET | next_open Mo 20.07. 09:30 ET
Gesamtwert:        98.252,31 $   (Alpaca equity Live 09:37 ET)
Cash:              49.670,08 $   (50,55 %, unverändert seit GS-Fill Mi 15.07.)
Investiert (MV):   48.582,03 $   (49,45 %, AAPL 10.356 + JPM 1.011 + UNH 10.334 + LLY 9.421 + GOOGL 8.950 + GS 8.509)
Buying_power:     334.710,57 $
P/L heute:           -272,40 $   (-0,276 %)   [GRÜN — vs Alpaca last_equity 98.524,71, Cap -3 %]
SPY-Live:           siehe Pre-Market -0,886 % IEX (Live-Update in Midday)
ATH:              100.066,47 $   DD -1,813 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW29:    -0,375 %     (Tag 5, Basis Fr-Close 98.621,81)                        [GRÜN — Cap -5 %]
Käufe KW29:            2/2 LOCK  (AAPL Mo + GS Mi gefüllt — bis Mo 20.07. KW30)          [LOCK]
Pending Orders:        0         (V1 nicht getroffen, kein Sell-Trigger; kein Kauf-Scan LOCK)
VIX-Ref:            ~17          (Pre-Market 17,96, Close Do 16,73)                       [GRÜN]
Guardrails: Daily -0,28 % | Weekly -0,38 % | DD -1,81 % | VIX ~17 | Käufe 2/2 LOCK → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca /v2/positions 09:37 ET) — sortiert nach Puffer ENG→WEIT:**

| Sym    | Curr      | Chg_today | P/L %    | V1-Stop        | V1-Puffer  | Status |
|--------|-----------|-----------|----------|----------------|------------|--------|
| **GS** | 1.063,635 | **-2,905%**| **-6,84%**| 1.050,40 (-8 %)| **+1,26 %**| SICHER **KRITISCH** (Fill-Day+2 Drop-Muster VOLLBILD, Puffer schrumpft Pre 2,82% → Open 1,26%, Muster AVGO/MU) |
| **GOOGL**|  344,240| **-2,883%**| **-6,48%**|  338,65 (-8 %) | **+1,65 %**| SICHER **KRITISCH** (Fill-Day+8 Follow-Through Nachmittags-Kollaps Do, Puffer 2,39% Pre → 1,65% Open, Blackout-Konflikt bei Close verschärft) |
| LLY    | 1.177,610 | +0,722 %  | -1,36 %  | 1.098,38 (-8 %)| +7,21 %    | SICHER (Reversal-Fortsetzung Tag 3) |
| JPM    |   336,930 | -1,813 %  | +1,25 %  |  306,16 (-8 %) | +10,05 %   | SICHER (Post-Q2-Give-back Tag 4) |
| AAPL   |   334,085 | +0,248 %  | +5,44 %  |  291,51 (-8 %) | +14,60 %   | SICHER (Fill-Day+4 stabil, XLK-Rebell hält) |
| UNH    |   430,600 | +1,705 %  | +7,23 %  |  369,44 ✓Reset | +16,56 %   | SICHER (Post-Q2-Konsolidierung stabil, Rally-Give-back-Fortsetzung ausgeblieben) |

**V1-V6-Check: ALLE 6 POSITIONEN SICHER.** → **KEINE Sell-Order platziert.** → **KEIN Kauf-Scan** (Käufe LOCK 2/2 bis Mo 20.07.).

**KRITISCHE PUFFER-SITUATION:**
- **GS +1,26 %** = ENGSTE Position, Break unter 1.050,40 löst V1 Market-Sell sofort aus
  - Bewegung Fill-Day+2: 1.141,74 Entry → Open 09:37 1.063,64 = -6,84 % kumuliert
  - Muster-Präzedenz: AVGO Fill-Day+3 -8,69 % V1 / MU Fill-Day+4 -10,92 % V1 → GS im kritischen Fenster
- **GOOGL +1,65 %** = 2. engste, Break unter 338,65 löst V1 Market-Sell sofort aus
  - Bewegung Fill-Day+8: Entry 368,10 → 344,24 = -6,48 % kumuliert (Nachmittags-Kollaps Do setzt sich fort)
  - Blackout-Konflikt bei Close: V1_neu 349,70 > Kurs 344,24 → **-1,56 % negativ** = würde Sofort-Stop auslösen bei Regel-strict Aktivierung
  - **Regel-Entscheidung Close-Routine:** Wenn Kurs < V1_neu 349,70, Blackout-Tightening aussetzen und Standard-V1 338,65 beibehalten (Strategie-Lock — keine Regel-Abweichung ohne Owner-Freigabe, aber Rule-strict-Auslegung würde Position beenden)

**Guardrails (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,276 %                                    [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,375 % (KW29 Tag 5)                       [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,813 % vs ATH 100.066,47                  [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,813 %                                    [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Pre-Market -0,886 %                     [INAKTIV]
6. VIX-Filter (>30):          ~17 (Pre 17,96, Close Do 16,73)             [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL ab HEUTE Close aktivierbar (Q2 22.07.)[ÜBERGANG]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30                 [LOCK]
```

**ClickUp:** PushNotification Prio 2 (Wichtig) — GS/GOOGL Puffer <2% + GOOGL-Blackout-Konflikt-Vorwarnung.

> **Entscheidung Open 09:37 Fr 17.07.:** **Alle 6 V1 SICHER, aber GS +1,26 % und GOOGL +1,65 % dramatisch eng.** Keine Sell-Order (V1 nicht erreicht, regelkonform Halten). Kein Kauf-Scan (LOCK 2/2). PushNotification Prio 2 wegen kritischer Puffer und GOOGL-Blackout-Konflikt Close. Nächster Check Midday 13:00 ET zwingend — GS/GOOGL V1-Watch.
> **Nächste Routine:** Fr 17.07. 13:00 ET Midday Stop-Check.

---

## Market Close 2026-07-16 16:02 ET (Do, KW29 Tag 4) — Tagesbilanz, alle V1-V6 SICHER, GOOGL/GS Nachmittags-Drop, Alpha neutral

```
Alpaca clock:      is_open=false | next_open Fr 17.07. 09:30 ET | next_close 16:00 ET
Gesamtwert:        98.480,38 $   (Alpaca equity Close)
Cash:              49.670,08 $   (50,44 %, unverändert seit GS-Fill Mi 15.07.)
Investiert (MV):   48.810,30 $   (49,56 %, AAPL 10.317 + JPM 1.029 + UNH 10.107 + LLY 9.364 + GOOGL 9.227 + GS 8.764)
Buying_power:     335.349,16 $
P/L heute:           -540,93 $   (-0,546 %)   [GRÜN — vs Alpaca last_equity 99.021,31, Cap -3 %]
SPY-Tag:            -0,517 %     (Alpaca IEX 754,77 → 750,87)
Alpha vs SPY:       -0,030 %     [NEUTRAL — UNH-Rally-Give-back und GOOGL-Nachmittags-Drop hoben sich gegen SPY-Schwäche auf]
ATH:              100.066,47 $   DD -1,585 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW29:    -0,143 %     (Tag 4, Basis Fr-Close 98.621,81)                        [GRÜN — Cap -5 %]
Käufe KW29:            2/2 LOCK  (AAPL Mo + GS Mi gefüllt — bis Mo 20.07. KW30)          [LOCK]
Pending Orders:        0         (V5/V6 alle 6 SICHER — KEINE Limit-Order für Fr 17.07.)
VIX-Ref:            ~15-16       (carry-over, keine belastbare Perplexity Close-Zahl)
Guardrails: Daily -0,55 % | Weekly -0,14 % | DD -1,59 % | VIX ~15 | Käufe 2/2 LOCK → ALLE GRÜN
```

**Positionen Close V1-V6 (Alpaca IEX 262d Bars, EMA/RSI Wilder):**

| Sym    | Close     | P/L      | Chg_today | V1-Stop        | V1-Puffer  | V5 Spread | V6 RSI | V6 RS_4w  | Status |
|--------|-----------|----------|-----------|----------------|------------|-----------|--------|-----------|--------|
| AAPL   |   332,81  | +5,04 %  | +1,62 %   | 291,51 (-8 %)  | +14,17 %   | +26,20    | 72,02  | +11,05 %  | SICHER (Tages-Sieger, RSI 72,02 höchste aber <80, XLK-Rebell) |
| UNH    |   421,14  | +4,87 %  | +0,63 %   | 369,44 ✓Reset  | +13,99 %   | +49,10    | 56,53  | +3,46 %   | SICHER (Post-Q2-Rally-Give-back von Tageshoch 460,95 auf 421,14 = -8,64 % vs H, aber P/L bleibt +4,87 %) |
| JPM    |   343,15  | +3,12 %  | -1,08 %   | 306,16 (-8 %)  | +12,08 %   | +13,97    | 63,11  | +3,78 %   | SICHER (Give-back nach Post-Q2-Rally Tag 3) |
| LLY    | 1.170,50  | -1,96 %  | +1,20 %   | 1.098,38 (-8 %)| +6,57 %    | +128,69   | 53,18  | +3,94 %   | SICHER (Reversal-Fortsetzung, XLV-Rebound) |
| GOOGL  |   354,87  | -3,59 %  | **-4,33 %**| 338,65 (-8 %) | +4,79 %    | +43,78    | 46,25  | -5,40 %   | SICHER (**Nachmittags-Kollaps** von Midday 371,37 auf 354,87 = -4,44 % im Handelsverlauf, Blackout-Vorbereitung Fr Close pending) |
| **GS** | 1.095,46  | -4,05 %  | **-4,91 %**| 1.050,40 (-8 %)| **+4,29 %**| +121,35   | 56,71  | +0,23 %   | SICHER (**engste** — Fill-Day+1 Drop-Muster VOLLBILD, Muster wie AVGO/MU) |

**V1-V6-Check: ALLE 6 POSITIONEN SICHER.** → **KEINE Sell/Limit-Order für Fr 17.07. platziert.**
- V1 alle SICHER (GS engste +4,29 %, dann GOOGL +4,79 %)
- V2-Trails aktualisiert (siehe Trade-Log)
- V5 alle SICHER (Spreads +14 bis +129, kein Death-Cross-Risiko)
- V6 alle SICHER (max RSI 72,02 AAPL <<80; GOOGL RSI 46,25 + RS_4w -5,40 % erfüllt Teil-Bedingung V6 aber RSI <<80 → verlangt BEIDES)

**GOOGL Nachmittags-Kollaps — dokumentiert:**
- Midday 13:07 ET: 371,37 (stabil, chg +0,12 %) → Close 16:02 ET: 354,87 (chg -4,33 %) = **-4,44 % im Nachmittag**
- Intraday-Range: H 375,18 (Open+Pre-Q2-Rally-Fortsetzung) → L 352,365 (nahe Close) = -6,08 % Intraday-Absturz
- Ursache-Hypothese: Late-Session-News-Trigger oder Rotation-Aus-XLC (XLC bisher LEAD-Sektor); Perplexity ohne belastbare Nachrichten
- V1-Puffer +4,79 % (verschlechtert von Midday +9,66 %), aber V1 338,65 noch nicht getroffen
- Blackout-Vorbereitung morgen (Fr 17.07. Close) V1-Tightening auf 349,70 (-5 %) zwingend

**GS Fill-Day+1 Drop-Muster — VOLLBILD:**
- Close chg -4,91 % Fill-Day+1 (Muster wie AVGO -5,77 % Fill-Day+1, MU -5,26 % Fill-Day+0)
- V1 1.050,40 bei 1.095,46 = **+4,29 % Puffer** (verschlechtert von Midday +4,93 %, Open +7,29 %)
- V1-Break unter 1.050,40 wäre Market-Sell sofort (Pre-Market Fr 17.07. 08:30 ET zwingender Watch)

**UNH Post-Q2-Rally-Give-back — Pump-and-Dump-Muster materialisiert:**
- Tageshoch 460,95 (chg +10,17 % vs Mi-Close) → Close 421,14 (chg +0,63 %) = **-8,64 % vs Tageshoch**
- P/L bleibt +4,87 % (verschlechtert von Midday +7,34 %), Positions-Beitrag ~+470 $ = +0,47 %
- V2-Trail-Update auf **NEU 405,64** (460,95 × 0,88, vorher 381,89 vom Hoch 434,19)
- V1-Puffer +13,99 % (Reset auf 369,44 nach Blackout-Ende, komfortabel)

**LLY-Reversal-Fortsetzung:**
- Open 1.143,26 (-1,12 % vs Mi-Close) → Close 1.170,50 (+1,20 % vs Mi-Close, Tageshoch 1.188,19)
- P/L verbessert von Mi Close -3,16 % auf -1,96 %
- V1-Puffer +6,57 % (verbessert von Midday +6,60 %, entspannt von Open +4,33 %)
- XLV-Rebound nach UNH-Q2-Rally getragen

**V2-Trailing-Stop-Updates (heute neue Tageshochs):**
| Sym | Tageshoch | Neuer V2 (×0.88) | Alt V2 | Status |
|-----|-----------|------------------|--------|--------|
| UNH |  460,95   |   405,64         | 381,89 | **AKTUALISIERT** (neues Posit-Hoch) |
| AAPL|  334,65   |   294,49         | 284,59 | **AKTUALISIERT** (neues Fill-Day-Hoch) |
| JPM |  348,83   |   306,97         | 302,11 | **AKTUALISIERT** (neues Post-Q2-Hoch) |
| GOOGL| 375,18   |   330,16         | 328,36 | **AKTUALISIERT** (marginales neues Hoch) |
| LLY | 1.188,19  | 1.045,61         |1.098,70| unverändert (V2 trailt nur UP, altes Hoch 1.248,53 höher) |
| GS  | 1.150,10  | 1.012,09         |1.013,45| unverändert (V2 trailt nur UP, altes Fill-Hoch 1.151,65 höher) |

**Sektor-Impact (Alpaca IEX Cross-Check nicht verfügbar für heute — Ableitung aus Positions-chg_today):**
- XLV: UNH +0,63 % + LLY +1,20 % → Sektor stabil-positiv trotz UNH-Give-back
- XLK: AAPL +1,62 % Rebell — XLK vermutlich weiter negativ oder neutral
- XLC: GOOGL -4,33 % dominiert Sektor-Ausschlag → XLC vermutlich stark negativ (Rotation raus)
- XLF: JPM -1,08 % + GS -4,91 % → Sektor negativ, GS Fill-Day+1 zieht runter

**Guardrails (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,546 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,143 % (KW29 Tag 4)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,585 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,585 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,517 %                          [INAKTIV]
6. VIX-Filter (>30):          ~15-16 (carry-over)                   [GRÜN]
7. Earnings-Blackout (3 HT):  UNH beendet, GOOGL ab Fr Close aktiv  [ÜBERGANG]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30           [LOCK]
```

**ClickUp:** Tagesbericht wird gesendet (bei ITEM_246 Tier-Limit Fallback → PushNotification).

> **Entscheidung Close 16.07.:** **Alle 6 V1-V6 SICHER**, keine Sell/Limit-Order für Fr platziert. Portfolio **-0,546 % Daily / -0,030 % Alpha NEUTRAL** (SPY-Schwäche -0,517 % lief parallel). **GS-Puffer 4,29 % ENGSTE** (Fill-Day+1 Drop-Muster VOLLBILD wie AVGO/MU), **GOOGL Nachmittags-Kollaps** -4,44 % von 371,37 → 354,87 (Puffer 4,79 %). UNH Pump-and-Dump vollständig materialisiert vom Tageshoch 460,95 (-8,64 %), aber P/L +4,87 % positiv. LLY-Reversal-Fortsetzung. Weekly KW29 -0,143 %, DD -1,585 %. Käufe LOCK 2/2 bis Mo 20.07.
> **Zwingender Watch Pre-Market Fr 08:30 ET:** (1) **GS 1.050,40 kritisch** (Puffer 4,29 %, Break → Market-Sell sofort), (2) **GOOGL 338,65** (Puffer 4,79 %, Blackout-Tightening Close), (3) UNH V1-Reset stabil, (4) LLY Reversal-Fortsetzung.
> **Nächste Routine:** Fr 17.07. 08:30 ET Pre-Market Check (KW29 Tag 5, GS/GOOGL kritisch, GOOGL-Blackout-Aktivierung Close).

---

## Midday 2026-07-16 13:07 ET (Do, KW29 Tag 4) — Alle 6 V1-V4 SICHER, GS Drop verstärkt (engste), UNH Rally-Give-back

```
Alpaca clock:      is_open=true | next_close 16.07. 16:00 ET
Equity:            99.185,51 $   (Live 13:07, vs Alpaca last_equity 99.021,31 → +0,166 %)
Cash:              49.670,08 $   (50,08 %, unverändert seit GS-Fill Mi 15.07.)
Portfolio MV:      49.515,43 $   (49,92 %, 6 Positionen)
Buying_power:     337.323,52 $
Daily P/L:           +164,20 $   (+0,166 % vs Alpaca last_equity)                          [GRÜN — Cap -3 %]
SPY Live IEX:       752,47       (vs Mi-Close 754,77 → -0,305 %)
Alpha vs SPY:       +0,471 %     [POSITIV — UNH Rally-Give-back durch Rest kompensiert]
ATH:              100.066,47 $   DD -0,881 % [GRÜN — leicht verschlechtert vs Open -0,52 %]
Weekly KW29:        +0,571 %     (Tag 4 Midday, Basis Fr-Close 98.621,81)                  [GRÜN — Cap -5 %]
Käufe KW29:            2/2 LOCK  (AAPL Mo + GS Mi gefüllt — bis Mo 20.07. KW30)             [LOCK]
Pending Orders:        0
VIX-Ref:            ~15-16       (carry-over, VXX Mi-Close 20,86 -2,89 %)                   [GRÜN]
Guardrails: Daily +0,17 % | Weekly +0,57 % | DD -0,88 % | VIX ~15 | Käufe 2/2 LOCK → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca /v2/positions 13:07 ET):**

| Sym    | Curr      | P/L      | Chg_today | V1-Stop        | V1-Puffer  | Status |
|--------|-----------|----------|-----------|----------------|------------|--------|
| UNH    |   431,025 | +7,34 %  | +2,99 %   | 369,44 ✓Reset  | +16,67 %   | SICHER (Post-Rally-Konsolidierung 451,75 Open → 431,02, Pump-and-Dump-Watch teilweise materialisiert) |
| AAPL   |   332,09  | +4,81 %  | +1,40 %   | 291,51 (-8 %)  | +13,92 %   | SICHER (Rebound-Fortsetzung XLK-Rebell) |
| JPM    |   345,21  | +3,74 %  | -0,49 %   | 306,16 (-8 %)  | +12,75 %   | SICHER (mildes Give-back nach Post-Q2 Tag 3) |
| GOOGL  |   371,37  | +0,89 %  | +0,12 %   | 338,65 (-8 %)  | +9,66 %    | SICHER (stabil, Blackout Fr Close nähert) |
| LLY    | 1.170,94  | -1,92 %  | +1,24 %   | 1.098,38 (-8 %)| +6,60 %    | SICHER (Reversal-Fortsetzung, XLV-Rebound, entspannt von Open +4,33 %) |
| **GS** | 1.102,15  | -3,47 %  | **-4,34 %**| 1.050,40 (-8 %)| **+4,93 %**| SICHER (**engste** — Fill-Day+1 Drop-Muster VERSTÄRKT, aber V1 noch weg) |

**V1-V4-Check: ALLE 6 POSITIONEN SICHER.** → **Keine Sell/Limit-Order platziert.**
- V1 alle SICHER (GS engste +4,93 %, verschlechtert von Open +7,29 % durch Fill-Day+1 Drop -4,34 %)
- V2 alle SICHER (LLY V2-Trail 1.098,70 engste, Puffer +6,58 %; UNH V2 auf altes Hoch 434,19 = 381,89 — Open 451,75 setzt neues Hoch, V2 update bei Close)
- V3/V4 nicht ausgelöst (UNH P/L +7,34 % weit unter +20 %)

**GS Fill-Day+1 Drop-Muster — Muster-Fortsetzung dokumentiert:**
- Chg heute **-4,34 %** (Open war -2,18 %) → Verstärkung um 2,16 %-Punkte im Handelsverlauf
- V1 1.050,40 bei Live 1.102,15 = **+4,93 % Puffer** (Schrumpfung von Open +7,29 % → -2,36 % pp)
- Muster-Präzedenz: AVGO Fill-Day+3 Stop -8,69 % / MU Fill-Day+5 Stop -10,92 %
- **Aktion:** Beobachtung, kein Alert (V1 noch komfortabel weg). Bei Break unter 1.100 mit weiterem Momentum → Close-Routine kritischer V1-Watch.

**UNH Post-Rally-Konsolidierung — Pump-and-Dump-Watch teilweise materialisiert:**
- Open 451,75 (chg +7,94 %) → Midday 431,02 = **-4,59 % vs Open** (Give-back von Q2-Beat-Rally-Peak)
- P/L immer noch +7,34 % (Positions-Beitrag ~+706 $), chg_today +2,99 % positiv
- V1 369,44 Reset (Standard nach Blackout-Ende), Puffer +16,67 % komfortabel
- V2-Trail auf **~397,54** (Open-Hoch 451,75 × 0,88) update bei Close (endgültiges Tageshoch)

**LLY-Entspannung:**
- Open V1-Puffer +4,33 % (engste heute Open) → Midday +6,60 % (Rebound +1,24 %)
- Chg +1,24 % Reversal-Fortsetzung (Mi war Pause, jetzt wieder positiv)
- XLV-Rebound trägt (UNH-Q2-Effekt auf Sektor)
- Engste V1 heute **wechselt von LLY zu GS** durch GS-Drop

**Sektor-Impact (Live-Ableitung):**
- XLV: UNH-Konsolidierung -4,59 % vs Open, LLY-Rebound +1,24 % → gemischt
- XLK: AAPL +1,40 % Rebound-Fortsetzung
- XLC: GOOGL +0,12 % stabil
- XLF: JPM -0,49 % mild, **GS -4,34 % Fill-Day+1-Drop dominiert Sektor-Ausschlag** (GS-spezifisch, kein Sektor-Kontagion sichtbar)

**Guardrails (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,166 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    +0,571 % (KW29 Tag 4 Midday)          [GRÜN]
3. Drawdown-Alarm (-15 %):    -0,881 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -0,881 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,305 %                          [INAKTIV]
6. VIX-Filter (>30):          ~15-16                                [GRÜN]
7. Earnings-Blackout (3 HT):  UNH Blackout beendet, GOOGL ab Fr     [inaktiv heute]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30           [LOCK]
```

**ClickUp:** Kein Alert (keine Stops ausgelöst, kein Daily-Cap, GS-Puffer noch komfortabel). ClickUp-Tier-Limit-Muster carry-over.

> **Entscheidung Midday 16.07.:** **Keine Aktion.** Alle 6 V1-V4 SICHER. **GS Fill-Day+1 Drop-Muster VERSTÄRKT** chg -4,34 % → V1-Puffer schrumpft 9,67 % → **4,93 % (engste heute)**, aber V1 1.050,40 noch nicht getroffen. **UNH Post-Rally-Give-back** von Open-Peak (Pump-and-Dump-Watch teilweise materialisiert), aber P/L +7,34 % weiter stark. LLY entspannt (+6,60 %), engste V1 wechselt LLY→GS. Daily P/L +0,166 % [GRÜN], Alpha +0,471 % POSITIV.
> **Zwingender Watch Close 16:00 ET:** (1) GS Break unter 1.100 mit weiterer Verstärkung → V1-Watch aktivieren, (2) UNH neues Tageshoch für V2-Trail-Update (bei aktuellem Open-Hoch 451,75 = V2 397,54), (3) GOOGL-Blackout-Vorbereitung Fr Close (V1-Tightening 338,65 → 349,70 zwingend), (4) UNH V1-Reset carry-over 369,44 stabil.
> **Nächste Routine:** Do 16.07. 16:00 ET Market Close + Tagesbilanz.

---

## Market Open 2026-07-16 09:37 ET (Do, KW29 Tag 4) — UNH Q2-BEAT-Rally +7,94 %, kein Kauf-Scan (LOCK), V1-Reset UNH 369,44

```
Alpaca clock:      is_open=true | next_close 16.07. 16:00 ET
Equity:            99.548,85 $   (Live 09:37, vs Alpaca last_equity 99.021,31 → +0,533 %)
Cash:              49.670,08 $   (49,90 %, unverändert seit GS-Fill Mi 15.07.)
Portfolio MV:      49.878,77 $   (50,10 %, 6 Positionen)
Buying_power:     338.340,86 $
Daily P/L:           +527,54 $   (+0,533 % vs Alpaca last_equity)                          [GRÜN — Cap -3 %]
SPY Live IEX:       752,295      (vs Mi-Close 754,77 → -0,328 %)
Alpha vs SPY:       +0,861 %     [POSITIV — UNH-Q2-Rally +7,94 % dominiert; UNH-Beitrag ~+1.204 $]
ATH:              100.066,47 $   DD -0,517 % [GRÜN — verbessert vs Mi Close -1,043 %]
Weekly KW29:        +0,940 %     (Tag 4, Basis Fr-Close 98.621,81)                          [GRÜN — Cap -5 %]
Käufe KW29:            2/2 LOCK  (AAPL Mo + GS Mi gefüllt — bis Mo 20.07. KW30)             [LOCK]
Pending Orders:        0
VIX-Ref:            ~15,76-16,40 (Perplexity Do Pre-Market)                                  [GRÜN]
Guardrails: Daily +0,53 % | Weekly +0,94 % | DD -0,52 % | VIX ~16 | Käufe 2/2 LOCK → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca /v2/positions 09:37 ET):**

| Sym    | Curr      | P/L      | Chg_today | V1-Stop        | V1-Puffer | Status |
|--------|-----------|----------|-----------|----------------|-----------|--------|
| **UNH**|   451,75  | +12,50 % | **+7,94 %**| **369,44** ✓Reset | **+22,28 %** | SICHER (**Q2-BEAT Post-Release-Rally**, V1 von 381,49 auf 369,44 zurück, Puffer sprunghaft entspannt) |
| AAPL   |   328,00  |  +3,52 % | +0,15 %   | 291,51 (-8 %)  | +12,52 %  | SICHER (Konsolidierung nach Mi-Rebell +4,08 %) |
| GOOGL  |   371,17  |  +0,83 % | +0,07 %   | 338,65 (-8 %)  | +9,61 %   | SICHER (stabil, Blackout-Vorbereitung Fr 17.07. Close für Q2 22.07. AMC) |
| **GS** | 1.126,96  |  -1,29 % | **-2,18 %**| 1.050,40 (-8 %)| +7,29 %   | SICHER (**Fill-Day+1 Drop-Muster** ausgelöst, aber Puffer komfortabel) |
| JPM    |   342,34  |  +2,87 % | -1,32 %   | 306,16 (-8 %)  | +11,82 %  | SICHER (mildes Give-back nach Post-Q2-Rally 3 Tage) |
| **LLY**| 1.145,99  |  -4,01 % | -0,92 %   | 1.098,38 (-8 %)| **+4,33 %**| SICHER (**engste**, Reversal Mi pausiert, XLV-Watch) |

**V1-V6-Check: ALLE 6 POSITIONEN SICHER.** → **Keine Sell/Limit-Order platziert.**
- V1 alle SICHER (LLY engste +4,33 %, UNH neuer Puffer +22,28 % nach Reset)
- V2/V5/V6 carry-over aus Mi Close (RSI/EMA-Spreads/RS_4w alle im SICHER-Bereich, kein Trigger heute)

**UNH V1-Reset — AKTIVIERT (Blackout-Ende Post-Release):**
- Alt: V1 **381,49** (-5 % Blackout-Tight, aktiv Mo 13.07. Close bis Mi 15.07. Close)
- Neu: V1 **369,44** (-8 % Standard = 401,57 × 0,92) → Puffer bei Live 451,75 = **+22,28 %** [KOMFORTABEL]
- Trigger: Q2-Beat-Reaktion +7,94 % chg_today = Post-Release-Bestätigung erfüllt → Standard-V1 zurück

**UNH-Q2-Rally Analyse:**
- Chg +7,94 % (Pre-Market schon +6,80 %, Fortsetzung im regulären Handel)
- Beitrag zu Portfolio: ~+1.204 $ = +1,20 % Equity (fast der gesamte Daily-P/L)
- **Positions-Hoch NEU** wahrscheinlich intraday (Watch für V2-Trail-Update auf **~397,54** = 451,75×0,88, aktuell V2 basierend auf altem Hoch 434,19 = 381,89)
- V2-Trail-Update erfolgt bei Close (endgültiges Tageshoch)

**GS Fill-Day+1 Drop-Muster ausgelöst — dokumentierte Muster-Fortsetzung:**
- Chg -2,18 % Fill-Day+1 (Muster wie AVGO -4,36 %/-5,77 %, MU -5,26 %/-5,85 %, aber abgeschwächt)
- V1 1.050,40 bei Live 1.126,96 = +7,29 % Puffer (noch komfortabel, aber Verengung von Mi Close +9,67 %)
- V2 basierend auf Fill-Preis-Hoch 1.151,65 = **1.013,45** (noch komfortabel, +11,20 % Puffer)
- Muster-Beobachtung, keine Aktion nötig (V1-Stop weit weg)

**Sektor-Impact (Live 09:37):**
- XLV Rally durch UNH-Q2-Beat: UNH +7,94 % zieht Sektor mit
- LLY -0,92 % XLV-Rebound nicht mitgenommen (RSI-Rekonvergenz Mi einmalig)
- XLK stabil (AAPL +0,15 %)
- XLC stabil (GOOGL +0,07 %)
- XLF gemischt: JPM -1,32 % Give-back, GS -2,18 % Fill-Day+1 → Sektor-Rotation raus aus XLF

**Guardrails (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,533 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    +0,940 % (KW29 Tag 4)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -0,517 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -0,517 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,328 %                          [INAKTIV]
6. VIX-Filter (>30):          ~15,76-16,40 (Perplexity Do)          [GRÜN]
7. Earnings-Blackout (3 HT):  UNH-Blackout ENDET nach Release       [ÜBERGANG — V1 zurück auf 369,44]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30           [LOCK]
```

**Käufe-LOCK:** Käufe KW29 2/2 belegt (AAPL 13.07. + GS 15.07.). Kein Kauf-Scan durchgeführt. Watchlist V + PANW für KW30 Mo 20.07. carry-over aus Mi Close.

**GOOGL-Blackout-Vorbereitung (nicht heute):**
- GOOGL Q2 **22.07.2026 AMC** → 3-HT-Blackout ab **Fr 17.07. Close** aktivierbar
- V1-Tightening morgen (Fr) Close-Routine: 338,65 → **349,70** (-5 % = 368,10 × 0,95)
- HEUTE noch KEINE Aktion — Blackout beginnt erst Fr Close

**ClickUp:** POST /list/{id}/task → ITEM_246 Tier-Limit-Muster carry-over (Tag 4 in Folge erwartet). Fallback: **PushNotification an Owner** (UNH-Q2-Rally-Event = notify-würdig).

> **Entscheidung Market Open 16.07.:** **KEIN Kauf-Scan** (Slot-LOCK 2/2). **UNH V1-Reset** von 381,49 → **369,44** nach Q2-Beat-Post-Release-Bestätigung (chg +7,94 % erfüllt Trigger). Portfolio **+0,533 % Daily / +0,861 % Alpha POSITIV** dominiert von UNH-Q2-Rally (~+1.204 $ Beitrag). Alle 6 V1-V6 SICHER, LLY engste +4,33 % (Reversal Mi pausiert, aber V1 weit weg). **GS Fill-Day+1 Drop-Muster** ausgelöst chg -2,18 % — Muster wie AVGO/MU aber abgeschwächt, V1-Puffer +7,29 % noch komfortabel. Weekly KW29 Tag 4 **+0,940 %**, DD -0,52 % (verbessert von Mi -1,04 %). VIX ~16 stabil. Käufe LOCK bis Mo 20.07.
> **Zwingender Watch Midday 13:00 ET:** (1) UNH V2-Trail-Update bei neuem Tageshoch (Live 451,75 → V2 ~397,54); (2) GS Fill-Day+1-Drop-Fortsetzung (Break unter 1.100 wäre Warn-Signal, V1 1.050,40 aber weit weg); (3) LLY V1 1.098,38 +4,33 % Puffer engste; (4) UNH Post-Rally Konsolidierung/Pump-and-Dump-Watch.
> **Nächste Routine:** Do 16.07. 13:00 ET Midday Stop-Check.

---

---

## Market Close 2026-07-15 16:02 ET (Mi, KW29 Tag 3) — Tagesbilanz, alle V1-V6 SICHER, keine Limit-Order für Do, AAPL +4,08 % Tages-Sieger (XLK -1,10 %), Alpha +0,292 % POSITIV

```
Alpaca clock:      is_open=false | next_open Do 16.07. 09:30 ET | next_close 16:00 ET
Gesamtwert:        99.023,08 $   (Alpaca equity Close)
Cash:              49.670,09 $   (50,16 %, unverändert seit GS-Fill Mi 09:41 ET)
Investiert (MV):   49.352,99 $   (49,84 %, AAPL 10.157 + JPM 1.041 + UNH 10.042 + LLY 9.250 + GOOGL 9.649 + GS 9.215)
Buying_power:     336.868,73 $
P/L heute:           +657,57 $   (+0,6685 %)  [GRÜN — vs Alpaca last_equity 98.365,51, Cap -3 %]
SPY-Tag:            +0,376 %     (Alpaca IEX 751,94 → 754,77)
Alpha vs SPY:       +0,292 %     [POSITIV — AAPL +4,08 % vs XLK -1,10 % = +5,18 % relativ dominiert; GOOGL +3,23 % vs XLC +1,70 % = +1,53 %; JPM/GS/LLY Sektor-Outperform mild]
ATH:              100.066,47 $   DD -1,043 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW29:   +0,407 %      (Tag 3, Basis Fr-Close 98.621,81)                        [GRÜN — Cap -5 %]
Käufe KW29:            2/2 LOCK  (AAPL Mo + GS Mi gefüllt — bis Mo 20.07. KW30)          [LOCK]
Pending Orders:        0         (alle V5/V6 SICHER — KEINE Limit-Order für Do 16.07.)
VIX-Ref:            ~15-16       (VXX Close 20,86, -2,89 % Vola-Rückgang, weit unter 30)
Guardrails: Daily +0,67 % | Weekly +0,41 % | DD -1,04 % | VIX ~15 | Käufe 2/2 LOCK → ALLE GRÜN
```

**Positionen Close V1-V6 (Alpaca IEX 271d Bars, EMA/RSI Wilder):**

| Sym    | Close     | P/L      | Chg_today | V1-Stop        | V1-Puffer | V5 EMA-Spread | V6 RSI  | V6 RS_4w   | Status |
|--------|-----------|----------|-----------|----------------|-----------|---------------|---------|-----------|--------|
| AAPL   |   327,64  |  +3,40 % |  +4,08 %  | 291,51 (-8 %)  | +12,39 %  | +26,18        | 69,39   | +10,47 %  | SICHER (Fill-Day+2 kräftiger Rebound, XLK-Outperform +5,18 % relativ, Tages-Sieger) |
| JPM    |   346,91  |  +4,25 % |  +1,17 %  | 306,16 (-8 %)  | +13,31 %  | +12,29        | 67,34   | +8,56 %   | SICHER (Post-Q2-Rally Tag 3, +0,54 % vs XLF, neues Positions-Hoch) |
| UNH    |   418,40  |  +4,19 % |  -1,60 %  | **381,49**⚠   | +9,67 %   | +46,58        | 53,31   | +1,72 %   | SICHER (Blackout-Cooldown letzter Tag, Q2 morgen BMO — V1 zurück auf 369,44 nach Release) |
| LLY    | 1.156,19  |  -3,16 % |  +0,32 %  | 1.098,38 (-8 %)| **+5,26 %**| +128,80       | 50,37   | +2,38 %   | SICHER (**engste**, RSI knapp über 50 rekonvertiert, XLV +0,03 % neutralisiert) |
| GOOGL  |   371,11  |  +0,82 % |  +3,23 %  | 338,65 (-8 %)  | +9,58 %   | +45,32        | 56,84   | +0,48 %   | SICHER (Fill-Day+7 Rebound Tag 2, +1,53 % vs XLC, P/L erstmals grün seit Fill) |
| **GS** | 1.151,93  |  +0,89 % |  +1,05 %  | 1.050,40 (-8 %)| +9,67 %   | +117,49       | 68,78   | +6,89 %   | SICHER (Fill-Day+0 Close, +0,42 % vs XLF, P/L grün Fill-Day) |

**V5/V6-Check heute: ALLE 6 POSITIONEN SICHER.** → **Keine Limit-Order für Do 16.07.** (Pending Orders bleiben 0.)
- V5 (EMA50 < EMA200): kein Symbol im Bereich (JPM engste absolute Spread +12,29 aber Golden Cross intakt)
- V6 (RSI > 80 UND RS_4w < 0): kein Symbol → AAPL RSI 69,39 (höchste) noch <80, alle RS positiv → SICHER

**Beste Position P/L:** JPM +4,25 % (Post-Q2-Rally Fortsetzung Tag 3)
**Schlechteste Position P/L:** LLY -3,16 % (Verbesserung von -4,28 % Open, RSI 50,37 rekonvertiert, engste V1)
**Beste chg_today:** AAPL +4,08 % (Fill-Day+2 kräftiger Rebound, XLK -1,10 % Sektor-Loser → +5,18 % relativ)
**Schlechteste chg_today:** UNH -1,60 % (Blackout-Cooldown letzter Tag pre-Earnings)

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLC +1,700 % (LEAD — Communication Services Rally)
XLY +0,932 % | XLF +0,632 % | SPY +0,376 %
XLRE +0,135 % | XLP +0,054 % | XLV +0,032 %
XLI -0,200 % | XLB -0,336 % | XLE -0,843 %
XLU -0,997 %
XLK -1,101 % (LOSER — Tech-Rücksetzer nach Di-Rebound)
VXX -2,886 % (Vola weiter runter)
```
→ **Rotation raus aus Tech + Utilities/Energy, rein in Communication + Discretionary.** Bot-Impact: AAPL XLK-Rebell **+5,18 % relativer Outperform** (Tages-Signal-Story: einzelwert-getriebener Rebound trotz Sektor-Schwäche); GOOGL XLC-Rider +1,53 %; JPM/GS XLF-Outperform +0,54 %/+0,42 %; LLY XLV-Neutral +0,29 %; UNH XLV-Underperform -1,63 % (Blackout letzter Tag).

**LLY-Positive-Reversal — engste V1-Position VERBESSERT:**
- Close 1.156,19 vs V1 1.098,38 = +5,26 % Puffer (vs Midday +4,16 %, Open +4,04 %)
- Chg heute +0,32 % (nach Di -2,33 %, Fr-Mo -1,77 %/-Rebound) → Momentum-Wechsel
- RSI(14) auf 50,37 rekonvertiert (Di 49,90 → Mi 50,37) — Momentum-Neutralisierung überwunden
- XLV +0,03 % Tag 7 stabilisiert (vs Di -1,92 % Tag 6)
- **V1 1.098,38 aktuell +5,26 % Puffer — weiterhin engste, aber Watch-Mode reduziert**

**Guardrails Close (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,668 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    +0,407 % (KW29 Tag 3)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,043 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,043 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,376 %                          [INAKTIV]
6. VIX-Filter (>30):          ~15-16 (VXX 20,86 -2,89 %)            [GRÜN]
7. Earnings-Blackout (3 HT):  UNH V1 381,49 letzter Tag → Do BMO   [GRÜN operativ, endet Do]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30           [LOCK]
```

**Weekly Loss Cap Prüfung KW29 Tag 3:**
- Weekly P/L = +0,407 % (Basis Fr-Close 98.621,81)
- Cap-Trigger -5 %: **NEIN**, weit unter Schwelle
- KEINE Pending-Order zu stornieren (bereits 0)
- KEIN WEEKLY_CAP-Alert

**Watchlist Do 16.07. (Slot-LOCK KW29, Vorbereitung Mo 20.07. KW30) — Alpaca 271d K1-K3 Screener 12 Symbole:**
```
Sym    Close      K1 EMA-Spread    K2 RSI    K3 RS_63d      Verdict
V      355,31     ✓ +1,84 knapp    ✓ 64,10   ✓ +4,51 %      3/3 LEAD (K5 Median ~25 grün, Q3 ~28.07. → Blackout ab 23.07. Close aktivierbar → 5 HT Kauf-Fenster)
PANW   353,99     ✓ +59,19         ✓ 66,09   ✓ +109,47 %    3/3 LEAD (RS #1, K5-Multi-Source-FwdPE zwingend — Cybersecurity typisch > 35, Analogie AMD-Reject)
NVDA   212,50     ✓ +11,36         ✓ 56,86   ✗ -1,47 %      2/3 K3-FAIL (verschlechtert vs Di +2,30 % — Chip-XLK-Loser Tag 3)
META   681,24     ✗ -39,02         ✓ 66,79   ✗ -6,76 %      1/3 FAIL (EMA50<EMA200, RS deutlich negativ)
AMZN   254,94     ✓ +8,25          ✓ 60,27   ✗ -7,25 %      2/3 K3-FAIL
TSLA   394,32     ✓ +4,06          ✗ 47,14   ✗ -1,33 %      1/3 FAIL
MA     535,33     ✗                ✓ 63,39   ✗ -5,27 %      1/3 FAIL
MSFT/ORCL/NFLX/COST/WMT: ALLE ≤1/3 FAIL (RS deutlich negativ oder K1 negativ)
```
→ **Zwei 3/3-LEADS für Mo 20.07. KW30:** **V** (K5 grün Median ~25 aber Blackout-Uhr tickt ab 23.07.) und **PANW** (K5-Multi-Source-FwdPE zwingend, Cybersecurity-Analogie AMD-Reject möglich).
→ **AMD bleibt gesperrt** (K5-FwdPE > 35 dokumentiert Di 14.07.)
→ **NVDA verschlechtert:** von Di 3/3 (+2,30 %) → Mi 2/3 (-1,47 %) durch XLK-1,10 % Tag heute
→ **Slot 2/2 KW29 LOCK bis Mo 20.07. KW30** — bis dahin nur Beobachtung

**Zwingende Watch-Punkte Do 16.07. Pre-Market:**
1. **UNH Q2 BMO 7:00 AM ET + Call ~8:30 AM ET** — Blackout endet, V1 zurück auf **369,44** (401,57 × 0,92 = -8 %) statt 381,49; Post-Release Reaction-Watch für Position
2. **LLY V1 1.098,38 +5,26 % Puffer** (engste, RSI 50,37 rekonvertiert) — weiter Watch-Mode
3. **GS Fill-Day+1** — V1 1.050,40 +9,67 %, Fill-Day-Drop-Muster (Post-Fill-Weakness AVGO/MU) beachten
4. **AAPL XLK-Divergenz** — Rebell +5,18 % relativ, prüfen ob nachhaltig oder Rücksetzer nach 4 %-Rally
5. **V/PANW K5-Vorbereitung** für Mo 20.07. KW30 — Multi-Source FwdPE + Earnings-Termine

**Datenqualität:**
- Alpaca IEX 271d Bars für alle 6 Positionen + 12 Screener-Symbole + SPY + 12 Sektor-ETFs sauber gezogen (2025-06-16 → 2026-07-15 inkl. Close-Bar).
- EMA50/EMA200 + Wilder RSI(14) full-history.
- SPY Alpaca IEX 754,77 vs Di-Close 751,94 = **+0,376 %** Ground-Truth für Alpha (Perplexity nicht beantwortbar — "zukünftiges Datum"-Refusal wie zuvor).
- Sektor-ETF-Marks Alpaca IEX (12/12 erfolgreich, XLC +1,70 % Sieger, XLK -1,10 % Loser).
- Alpaca `equity` 99.023,08 vs `last_equity` 98.365,51 (Alpaca-konsistent, Daily-P/L direkt aus Diff).
- Perplexity Watchlist-Query "Zukunftsdatum"-Refusal → Fallback auf Alpaca-Screener 12 Large-Caps (V+PANW als 3/3-LEADS identifiziert).

**ClickUp:** POST /list/{id}/task → HTTP 400 **ITEM_246 Tier-Limit** (Tag 3 in Folge Di/Mi persistent). Fallback: **PushNotification an Owner** (Routine-Regel per notify-skill.md).

> **Entscheidung Market Close 15.07.:** Portfolio **+0,668 % POSITIV**, **Alpha +0,292 % POSITIV** (Umkehr vs Di -0,54 % negativ). AAPL Tages-Sieger **+4,08 % chg (Fill-Day+2 Rebound gegen XLK -1,10 % Sektor-Trend = +5,18 % relativer Outperform)** ist die Story des Tages. JPM Post-Q2-Rally Tag 3 +1,17 % (+4,25 % P/L neues Positions-Hoch). GOOGL Fill-Day+7 Rebound Tag 2 **P/L erstmals grün seit Fill** (+0,82 %). LLY **positives Reversal +0,32 % chg + RSI 50,37 rekonvertiert** → V1-Puffer +5,26 % (vs Midday +4,16 %), Watch-Mode reduziert. GS Fill-Day+0 **+1,05 % chg + P/L grün** (Fill-Day-Drop-Muster nicht ausgelöst). UNH Blackout-Cooldown letzter Tag -1,60 % vor Q2 morgen BMO — regelkonform vor Release. Alle V1-V6 SICHER, RSI max 69,39 (AAPL) << 80-V6-Threshold, alle EMA50>EMA200 → **keine Limit-Order für Do 16.07.** Sektor-Rotation: XLC +1,70 % LEAD / XLK -1,10 % LOSER / XLV neutralisiert / VXX -2,89 % Vola weiter runter (VIX ~15-16 stabil).
> **Zwingender Watch Do 16.07.:** (1) **UNH Q2 BMO 7:00 AM ET + Call 8:30 AM** — Blackout endet, V1 Reset auf 369,44; (2) **LLY V1 1.098,38 +5,26 % Puffer** (engste, aber RSI rekonvertiert); (3) **GS Fill-Day+1** V1 1.050,40 +9,67 %; (4) AAPL XLK-Divergenz-Fortsetzung; (5) V/PANW K5-Vorbereitung für KW30 Mo 20.07.
> **Lessons-Tag:** (1) AAPL Fill-Day+2 Sektor-Rebell +5,18 % relativer Outperform (XLK -1,10 % Tages-Loser) — Einzelwert-Momentum kann Sektor dominieren (K1-K5-Screen war regel-konform); (2) LLY XLV-Sektor-Neutralisierung nach 6 Tagen Schwäche — RSI 49,90→50,37 Rekonversion + Chg heute +0,32 % zeigt Bottom-Signal-Kandidat (V1 weiter aktiv aber Watch-Mode reduziert); (3) Alpaca-Screener als Perplexity-Fallback bei "Zukunftsdatum"-Refusal weiterhin robust — V+PANW 3/3-K1-K3 identifiziert.
> **Nächste Routine:** Do 16.07. 08:30 ET Pre-Market Check (KW29 Tag 4, **UNH Q2 BMO — V1 Reset auf 369,44 zwingend**, LLY V1-Watch +5,26 %, GS Fill-Day+1, Käufe LOCK bis Mo 20.07.).

---

## Midday 2026-07-15 13:07 ET (Mi, KW29 Tag 3) — Alle V1-V4 SICHER, keine Stops ausgelöst, Daily +0,48 % GRÜN, Post-Fill GS-Watch stabil

```
Alpaca clock:      is_open=true | next_close 15.07. 16:00 ET
Equity:            98.840,56 $   (Live 13:07, vs Alpaca last_equity 98.365,51 → +0,483 %)
Cash:              49.670,09 $   (50,25 %, unverändert seit GS-Fill 09:41 ET)
Portfolio MV:      49.170,47 $   (49,75 %)
Buying_power:     336.357,68 $
Daily P/L:           +475,05 $   (+0,483 % vs Alpaca last_equity)                        [GRÜN — Cap -3 %]
SPY Live:            +0,411 %    (Alpaca IEX 752,21 vs Di-Close 749,13; Alpaca-Konsistenz)
Alpha vs SPY:        +0,072 %    [LEICHT POSITIV — AAPL/GOOGL/JPM-Rebound trägt, LLY/UNH-XLV-Schwäche kompensiert]
ATH:              100.066,47 $    DD -1,225 % [GRÜN — Alarm bei -15 %]
Weekly KW29:        +0,222 %      (Tag 3, Basis Fr-Close 98.621,81)                        [GRÜN — Cap -5 %]
Käufe KW29:            2/2 LOCK  (AAPL Mo + GS Mi gefüllt)                                 [LOCK]
Pending Orders:        0         (keine Limit-/TP-Orders aktiv)
VIX-Ref:            ~16-17        (Perplexity 17,16 carry-over Open)                       [GRÜN]
Guardrails: Daily +0,48 % | Weekly +0,22 % | DD -1,23 % | VIX ~17 | Käufe 2/2 LOCK → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca IEX 13:07 ET):**
- **AAPL**  327,68 $ (Entry 316,86, P/L **+3,41 %**, chg_today **+4,08 %**) — Fill-Day+2 kräftiger Rebound
  - V1 291,51 SICHER (+12,42 % Puffer)
- **JPM**   347,255 $ (Entry 332,78, P/L **+4,35 %**, chg_today +1,44 %) — Post-Q2-Rally Tag 3
  - V1 306,16 SICHER (+13,42 % Puffer)
- **UNH**   420,04 $ (Entry 401,57, P/L +4,60 %, chg_today -1,34 %) — Blackout letzter Tag Cooldown
  - V1 381,49 (Blackout -5 %) SICHER (+10,10 % Puffer)
- **LLY**  1.144,03 $ (Entry 1.193,89, P/L **-4,18 %**, chg_today -0,89 %) — **XLV-Watch, ENGSTE Position**
  - V1 1.098,38 SICHER (**+4,16 % Puffer** — engste seit Open)
- **GOOGL**  372,135 $ (Entry 368,10, P/L +1,10 %, chg_today **+3,52 %**) — Fill-Day+7 kräftiger Rebound (P/L erstmals grün seit Fill)
  - V1 338,65 SICHER (+9,89 % Puffer)
- **GS**   1.132,84 $ (Entry 1.141,74, P/L -0,78 %, chg_today -0,78 %) — Fill-Day+0 mildes Fill-Day-Drop-Muster (AVGO/MU/LLY)
  - V1 **1.050,40 NEU** SICHER (+7,85 % Puffer)

**V1-V4-Check Midday: ALLE 6 POSITIONEN SICHER.**
- V1 (-8 % / UNH -5 %): keine Position im Bereich, LLY engste +4,16 %
- V2 (-12 % vom Posit-Hoch, carry-over): AAPL Trail ~288,36 (NEUES Hoch heute ~327,68 × 0,88); JPM Trail ~305,58 (NEUES Hoch 347,26 × 0,88); UNH Trail 382,09 (Hoch 434,19 09.07.); LLY Trail 1.098,71 (Hoch 1.248,53 07.07.) — knappste vs Kurs 1.144,03 = +4,12 %; GOOGL Trail ~328,36 (Hoch 373,14); GS Trail ~1.013,45 (Fill-Hoch 1.151,65) → alle SICHER
- V3 (+20 % TP1): keine Position im Bereich — nächste ist UNH bei 481,88 (aktuell 420,04, -12,8 % entfernt)
- V4 (+35 % TP2): weit entfernt

**Keine Sell-Order platziert. Keine Limit-Order platziert. Pending Orders bleiben 0.**

**Ø P/L über alle 6 Positionen:** +1,42 % | **Beste:** UNH +4,60 % | **Schlechteste:** LLY -4,18 %
**Beste chg_today:** AAPL +4,08 % (Fill-Day+2 Rebound) | **Schlechteste chg_today:** UNH -1,34 %

**Guardrails Midday (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,483 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    +0,222 % (KW29 Tag 3)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,225 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,225 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,411 %                          [INAKTIV]
6. VIX-Filter (>30):          ~17                                   [GRÜN]
7. Earnings-Blackout (3 HT):  UNH aktiv V1 381,49 (letzter Tag)     [GRÜN operativ]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30           [LOCK]
```

**Kein ClickUp Alert** (keine Stops ausgelöst, kein Daily Cap erreicht — Routine-Regel: nur bei Ereignis loggen).

**Nächste Routine:** Mi 15.07. 16:00 ET Market Close + Tagesbilanz (LLY V1-Watch, UNH-Blackout letzter Tag, GS Fill-Day+0 → Close-Trailing-Berechnung).

---

## Market Open 2026-07-15 09:42 ET (Mi, KW29 Tag 3) — GS 8 Sh @ 1.141,74 GEFÜLLT, Slot 2/2 KW29 verbraucht, alle 5 K-Signale grün, Positionen 6/8

```
Alpaca clock:      is_open=true | next_close 15.07. 16:00 ET
Equity Post-Fill:  98.376,40 $   (Alpaca Live 09:42, vs last_equity 98.365,51 → +0,011 % [GRÜN])
Cash:              49.670,09 $   (50,49 %, -9.133,95 vs Open durch GS-Fill)
Investiert (MV):   48.706,31 $   (49,51 %, AAPL 9.893,65 + JPM 1.048,14 + UNH 10.033,20 + LLY 9.142,38 + GOOGL 9.468,94 + **GS 9.123,00 NEU**)
Buying_power:     335.058,02 $
Positionen:            6/8       (GS neu, Slot 2/2 KW29 belegt & gefüllt)
Pending Orders:        0         (GS-Order 495b1c15 vollständig gefüllt in 4 sec)
```

**GS Kauf-Details:**
- Limit-Order:    1.147,58 $ (Day, +0,5 % über Di-Close 1.141,87)
- Order-Submit:   09:41:14 ET
- Fill:           **8/8 Sh @ 1.141,74375 avg um 09:41:18 ET** (4 sec, deutlich unter Limit)
- Investiert:     9.133,95 $ (9,28 % Portfolio)
- V1 Stop:        **1.050,40 $** (-8 %)
- V2 Trail:       -12 % vom Posit-Hoch (Tracking ab Fill = Hoch heute 1.151,65)
- TP1 / V3:       1.370,09 $ (+20 %)
- TP2 / V4:       1.541,35 $ (+35 %)
- Alpaca Order-ID: 495b1c15-9346-4b97-a2f4-7278773753c3

**K1-K5 GS bestätigt (Alpaca 270d Bars 2025-06-16 → 2026-07-14 inkl. + Perplexity K5):**
- K1 ✓ EMA50 1.018,62 > EMA200 903,90 (Spread **+114,73** — Golden Cross sehr breit)
- K2 ✓ RSI(14) Wilder **67,63** (im 50-70 Fenster, knapp am oberen Ende)
- K3 ✓ RS_63d GS +28,16 % - SPY +9,61 % = **+18,55 %** (bester Screener-Wert 15.07.)
- K4 ✓ Intraday 10-min-IEX-Vol 11.126 Sh → Extrap ~434k IEX/Tag; Avg20-IEX 71.632 → **~606 % Avg20 IEX >> 120 %-Hürde**
- K5 ✓ Multi-Source Perplexity: FwdPE 14,74 [GuruFocus] / 17,04 [ValueInvesting] / 17,53 [YCharts] / 16,66 [Eulerpool 2026-07-10] → **Median ~17 klar ≤ 35** (breiter Puffer); Revenue Growth Q2 2026 released 14.07. (Umsatz $20,34 Mrd, Analystenerwartung +11,81 % YoY erfüllt) ≥ 10 % ✓; Nächste Earnings Q3 ~Mitte Oktober = >60 HT weg → **kein Blackout**

**Konkurrenz-Kandidaten (K5-Recheck ausgeschieden):**
- **NVDA 211,65** — K5 FwdPE Median 34,33 (Range 20,40-40,78 Multi-Source-Uncertainty) → **grenzwertig wie AMD Di**, konservativ REJECT
- **V 353,56** — K5 FwdPE ~25 grün, aber V Q3 FY26 ~28.07. AMC = **9 HT weg → Blackout ab 23.07. Close aktivierbar** → erhöhtes Risiko-Profil vs GS

**Positionen Post-Fill V1-Check (Alpaca Live 09:42):**
| Sym    | Live      | P/L      | Chg_today | V1-Stop   | V1-Puffer | Status |
|--------|-----------|----------|-----------|-----------|-----------|--------|
| AAPL   |   319,15  |  +0,72 % |  +1,363 % | 291,51    | +9,48 %   | SICHER (Fill-Day+2 Rebound) |
| JPM    |   349,38  |  +4,99 % |  +1,893 % | 306,16    | +14,12 %  | SICHER (Post-Q2 Tag 3) |
| UNH    |   418,05  |  +4,10 % |  -1,679 % | 381,49⚠   | +9,58 %   | SICHER (Blackout letzter Tag bis Do BMO) |
| LLY    | 1.142,80  |  -4,28 % |  -0,845 % | 1.098,38  | **+4,04 %**| SICHER (**engste**, RSI 49,90 gekippt, XLV-Watch) |
| GOOGL  |   364,19  |  -1,06 % |  +1,302 % | 338,65    | +7,54 %   | SICHER (Fill-Day+7 Rebound) |
| **GS** | 1.140,38  |  -0,12 % |  +0,033 % | **1.050,40 NEU**| +8,57 %| SICHER (**Fill-Day+0** Entry-Watch) |

**Guardrails Post-Fill (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,011 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,249 % (KW29 Tag 3, Basis Fr-Close 98.621,81)  [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,689 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,689 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,386 % (751,94 → 754,84)        [INAKTIV]
6. VIX-Filter (>30):          17,16 Perplexity confirmed             [GRÜN]
7. Earnings-Blackout (3 HT):  UNH V1 381,49 aktiv (letzter Tag)     [GRÜN operativ]
8. Max Käufe KW29:            **2/2 LOCK** (AAPL Mo + GS Mi)         [LOCK]
```

**Sektor-Zusammensetzung Post-Fill (6 Positionen):**
- XLK: AAPL 9.894 (10,05 %)
- XLC: GOOGL 9.469 (9,62 %)
- XLF: JPM 1.048 + GS 9.123 = 10.171 (10,34 %) — **2 Positionen, weit unter 30 %-Cap ✓**
- XLV: UNH 10.033 + LLY 9.142 = 19.175 (19,49 %) — Cluster wie zuvor
- Cash: 49.670 (50,49 %)
→ Diversifikation über 4 Sektoren + Cash-Reserve reichlich

**Zwingende Watch-Punkte Midday 13:00 ET:**
1. **LLY V1-Puffer +4,04 %** engste Position — Break unter 1.098,38 löst V1-Market-Sell
2. **GS Fill-Day+0** — V1 1.050,40 Puffer +8,57 %, aber Fill-Day-Drop-Muster (AVGO/MU) beachten
3. **UNH V1 381,49 (Blackout -5 %) letzter Tag** — Puffer +9,58 %, Blackout endet Do 16.07. BMO
4. **AAPL/JPM Post-Rally-Fortsetzung** — V1 komfortabel
5. **GOOGL Fill-Day+7 Rebound** — Puffer +7,54 % erweitert

**Datenqualität:**
- Alpaca IEX Live Trades 09:37-09:42 für alle Positionen + Kandidaten
- Alpaca 270d Daily-Bars GS/SPY 2025-06-16 → 2026-07-14 (adjustment=split) → K1-K3-Berechnung vollständig
- Alpaca 1Min Intraday-Bars GS 09:30-09:39 → K4-Volumen-Extrapolation
- Perplexity K5 GS Multi-Source 4 Datenpunkte FwdPE + Q2-2026-Report-Bestätigung
- Perplexity K5 NVDA 3 Datenpunkte FwdPE (Range 20-41 zu breit) + Q1 FY2026 RevGrowth
- Perplexity K5 V 6 Datenpunkte FwdPE (~25 Median) + RevGrowth 17,10 %

**ClickUp:** POST /list/{id}/task → HTTP 403 OAuth-023 „Team(s) not authorized" (neue Fehler-Klasse vs ITEM_246 Tier-Limit gestern). Fallback: **PushNotification an Owner erfolgreich versendet**.

> **Entscheidung Market Open 15.07.:** Regelkonformer **KAUF GS** mit allen 5 K-Signalen grün (K1-K4 aus Alpaca Bars valid, K5 Multi-Source FwdPE Median 17 mit deutlichem Puffer zu ≤35). GS gewählt vor NVDA (K5-FwdPE-Range-Uncertainty 20-41 wie AMD Di) und V (Earnings-Blackout in 8 HT ab 23.07. aktivierbar). **Slot 2/2 KW29 belegt** (AAPL Mo + GS Mi) — Käufe LOCK bis Mo 20.07. KW30. Fill um 09:41:18 ET nach nur 4 sec bei 1.141,74 (unter Limit 1.147,58 = -0,51 % Fill-Preis-Vorteil).
> **Sektor-Konzentrations-Check bestanden:** XLF mit JPM (1.048) + GS (9.123) = 10,34 % Portfolio, weit unter 30 %-Cap, 2 Positionen ≤ 3 pro Sektor. Cluster deutlich milder als XLV (19,49 %).
> **Zwingender Watch Midday:** (1) LLY V1 +4,04 % engste (RSI-Neutralisierung); (2) GS Fill-Day+0 (AVGO/MU/GOOGL-Muster beachten); (3) UNH-Blackout letzter Tag bis Do BMO; (4) AAPL/JPM Post-Rally.
> **Nächste Routine:** Mi 15.07. 13:00 ET Midday Stop-Check.

---

## Market Close 2026-07-14 16:02 ET (Di, KW29 Tag 2) — Tagesbilanz, alle V1–V6 SICHER, keine Limit-Order für Mi, JPM Post-Q2 +2,87 %, LLY XLV Tag 6 schlechteste

```
Alpaca clock:      is_open=false | next_open Mi 15.07. 09:30 ET | next_close 16:00 ET
Gesamtwert:        98.399,88 $   (Alpaca equity Close, vs last_equity 98.562,62 Mo-After-Hours-Tick)
Cash:              58.804,04 $   (59,76 %, unverändert seit AAPL-Fill Mo 11:31 ET)
Investiert (MV):   39.595,84 $   (40,24 %, AAPL 9.760,35 + JPM 1.026,96 + UNH 10.218,04 + LLY 9.234,16 + GOOGL 9.346,61)
Buying_power:     346.084,52 $
P/L heute:           -162,74 $   (-0,165 %)  [GRÜN — vs Alpaca last_equity, Cap -3 %]
SPY-Tag:            +0,375 %     (Alpaca IEX 749,13 → 751,94)
Alpha vs SPY:       -0,540 %     [NEGATIV — LLY -2,33 % (XLV Tag 6) + AAPL -0,78 % (vs XLK +1,27 % = -2,05 % relativ) dominant]
ATH:              100.066,47 $   DD -1,665 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW29:   -0,225 %      (Tag 2, Basis Fr-Close 98.621,81)                        [GRÜN — Cap -5 %]
Käufe KW29:            1/2       Slot 2/2 bleibt OFFEN (AMD K5-Reject Di, kein Ersatz-Kandidat 3/3+K5)
Pending Orders:        0         (alle V5/V6 SICHER — KEINE Limit-Order für Mi 15.07.)
VIX-Ref:            ~15-16       (VXX Close 21,48, -1,468 % Vola-Rückgang, weit unter 30)
Guardrails: Daily -0,17 % | Weekly -0,225 % | DD -1,67 % | VIX ~16 | Käufe 1/2 → ALLE GRÜN
```

**Positionen Close V1–V6 (Alpaca IEX 280d Bars, EMA/RSI Wilder):**

| Sym    | Close    | P/L      | Chg_today | V1-Stop        | V1-Puffer | V5 EMA-Spread | V6 RSI  | V6 RS_4w   | Status |
|--------|----------|----------|-----------|----------------|-----------|---------------|---------|-----------|--------|
| AAPL   |  314,85  |  -0,63 % |  -0,775 % | 291,51 (-8 %)  | +8,01 %   | +26,54        | 61,97   | +6,81 %   | SICHER (Fill-Day+1, XLK +1,27 % Sektor-Rebound aber Einzelwert underperformt -2,05 % relativ) |
| JPM    |  342,32  |  +2,87 % |  +2,329 % | 306,16 (-8 %)  | +11,81 %  | +12,75        | 64,76   | +5,56 %   | SICHER (Post-Q2-Rally-Fortsetzung Tag 2, +2,11 % vs XLF-Sektor) |
| UNH    |  425,75  |  +6,02 % |  -0,778 % | **381,49 NEU** | +11,60 %  | +47,61        | 58,49   | +2,74 %   | SICHER (Blackout -5 % aktiv bis Do 16.07. BMO, +1,14 % vs XLV-Sektor) |
| LLY    | 1.154,27 |  -3,32 % |  -2,335 % | 1.098,38 (-8 %)| +5,09 %   | +131,04       | 49,90   | +0,49 %   | SICHER (**engste**, XLV -1,92 % Tag 6, RSI 49,90 unter 50 gekippt) |
| GOOGL  |  359,49  |  -2,34 % |  +1,979 % | 338,65 (-8 %)  | +6,15 %   | +46,84        | 49,45   | -1,41 %   | SICHER (Fill-Day+6 Rebound, +2,11 % vs XLC-Sektor) |

**V5/V6-Check heute: ALLE 5 POSITIONEN SICHER.** → **Keine Limit-Order für Mi 15.07.** (Pending Orders bleiben 0.)
- V5 (EMA50 < EMA200): kein Symbol im Bereich (LLY engste absolute EMA-Spread aber immer noch +131,04 sicher)
- V6 (RSI > 80 UND RS_4w < 0): kein Symbol → GOOGL RS -1,41 % erfüllt Teil-Bedingung, aber RSI 49,45 << 80 → SICHER

**Schlechteste Position:** LLY -3,32 % (V1-Puffer +5,09 % engste, XLV -1,92 % Sektor-Verlierer Tag 6, RSI 49,90 unter 50 gekippt)
**Beste Position:** JPM +2,87 % (Post-Q2-Rally-Fortsetzung, chg +2,33 % Tages-Winner)

**Sektor-Performance heute (Alpaca IEX, ranking) — Rotations-Umkehr vs Mo:**
```
XLK +1,274 % (LEAD — Tech-Rebound nach Mo -2,44 %)
SPY +0,375 % | XLE +0,370 % | XLF +0,223 % | XLB +0,178 % | XLI +0,044 %
XLU -0,055 % | XLY -0,099 % | XLC -0,125 %
XLRE -0,470 % | XLP -1,389 %
VXX -1,468 % (Vola-Rückgang)
XLV -1,921 %  (Health-Care schwächster Sektor Tag 6)
```
→ **Zykliker & Tech-Rebound, Health-Care & Staples weiter unter Druck.** Bot-Impact: JPM XLF-Outperform +2,11 % (Post-Q2-Rally); GOOGL XLC-Outperform +2,11 % (Fill-Day+6-Rebound); AAPL XLK-Underperform -2,05 % (Fill-Day+1 Mildes Drift trotz Tech-Rally); LLY XLV-Underperform -0,42 % (Sektor + Einzelwert); UNH XLV-Outperform +1,14 % (relative Stärke im schwachen Sektor).

**LLY-Sonderbeobachtung — engste V1-Position, RSI 49,90 gekippt:**
- Close 1.154,27 vs V1 1.098,38 = +5,09 % Puffer (engste seit AAPL-Fill Mo)
- RSI(14) gekippt unter 50 (49,90) — Momentum-Neutralisierung erreicht
- XLV -1,92 % Tag 6 (Fr -1,77 %, Mo +0,31 % Rebound-Tag, Di -1,92 % neuer Tief-Tag)
- Positions-Hoch 1.248,53 (07.07.) → aktuell 1.154,27 = -7,55 % vom Hoch (V2 -12 % Trail bei 1.098,71 = ebenfalls SICHER)
- Wenn LLY-Trend anhält: V1 1.098,38 könnte innerhalb 2-3 HT gebrochen werden
- **Pre-Market-Watch Mi 15.07. zwingend** (V1-Puffer < 5 % → V1-Watch-Modus)

**Guardrails Close (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,165 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,225 % (KW29 Tag 2)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,665 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,665 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,375 %                          [INAKTIV]
6. VIX-Filter (>30):          ~16 (VXX 21,48 -1,47 %)               [GRÜN]
7. Earnings-Blackout (3 HT):  UNH AKTIV V1 381,49 (bis Do BMO)      [GRÜN operativ]
8. Max Käufe KW29:            1/2 (AAPL gefüllt, Slot 2 offen)      [OFFEN]
```

**Weekly Loss Cap Prüfung KW29 Tag 2:**
- Weekly P/L = -0,225 % (Basis Fr-Close 98.621,81)
- Cap-Trigger -5 %: **NEIN**, weit unter Schwelle
- KEINE Pending-Order zu stornieren (bereits 0)
- KEIN WEEKLY_CAP-Alert

**Watchlist Mi 15.07. + KW29-Kauf-Prep (Alpaca 280d K1-K3 Screener 16 Symbole):**
```
Sym    Close Di    K1 EMA-Spread    K2 RSI    K3 RS_63d      Verdict
AMD    548,16     ✓ +155,33         ✓ 55,22   ✓ +112,49 %    3/3 LEAD (K5 FwdPE > 35 dokumentierter Reject Di)
NVDA   211,79     ✓ +12,23          ✓ 56,35   ✓ +2,30 %      3/3 LEAD (verbessert vs Mo 2/3, K5 morgen zwingend)
V      356,01     ✓ +1,41 knapp     ✓ 64,96   ✓ +5,47 %      3/3 LEAD (K1 marginal, K5 morgen)
GS     1141,87    ✓ +118,64         ✓ 67,63   ✓ +18,55 %     3/3 LEAD (Financials-Peer JPM, K5 morgen)
CAT    933,94     ✓                 ✗ 47,19   ✓ +8,42 %      2/3 FAIL
TSLA   396,17     ✓                 ✗ 47,73   ✓ +2,79 %      2/3 FAIL
AMZN   247,50     ✓                 ✓ 53,23   ✗ -6,47 %      2/3 FAIL
META   661,04     ✗ -38,91          ✓ 63,51   ✗ -5,48 %      1/3 FAIL
MA     538,21     ✗                 ✓ 65,59   ✗ -3,81 %      1/3 FAIL
```
→ **Vier 3/3-LEADS für morgen:** AMD (K5-Reject bereits terminal), **NVDA / V / GS neu offen für K5-Multi-Source-Recheck Pre-Market Mi.**
→ **NVDA-Verbesserung:** von Mo 2/3 (RS -2,54 %) → Di 3/3 (RS +2,30 %) — Chip-Rally-Rebound bringt NVDA über SPY-Referenz.
→ **V-Nuance:** K1 EMA-Spread nur +1,41 (marginal) — Sensitivität bei Pre-Market-Rechecks hoch, K5 Zahlungssektor-Bewertung + Earnings-Blackout zwingend.
→ **GS-Interesse:** RS +18,55 % robust, aber Financials-Peer JPM bereits im Depot (Konzentrations-Check morgen).
→ **AMD bleibt gesperrt** (Konsens-FwdPE > 35 Multi-Source Di dokumentiert).

**Datenqualitäts-Hinweise:**
- Alpaca IEX 280d Bars für alle 5 Positionen + 16 Screener-Symbole + SPY + 12 Sektor-ETFs sauber gezogen (2025-06-01 → 2026-07-14 inkl. Close-Bar).
- EMA50/EMA200 + Wilder RSI(14) full-history.
- SPY Alpaca IEX 751,94 vs Mo-Close 749,13 = **+0,375 %** Ground-Truth für Alpha (Perplexity nicht abgefragt — Alpaca zuverlässig, VIX via VXX-Proxy stabil).
- Sektor-ETF-Marks Alpaca IEX (12/12 erfolgreich, XLV -1,921 % Tages-Verlierer).
- Alpaca `equity` 98.399,88 vs `last_equity` 98.562,62 (Mo After-Hours-Tick) — Daily-P/L auf Alpaca last_equity gerechnet (Ground-Truth), Memory Mo-Close 98.587,07 (-24,45 After-Hours-Drift, konsistent zum Mo-Muster).

**ClickUp:** POST /list/{id}/task → HTTP 400 **ITEM_246 Tier-Limit weiter aktiv** (aus Pre-Market/Open carry-over). Fallback: **PushNotification an Owner** wie Routine-Regel.

> **Entscheidung Market Close 14.07.:** Portfolio -0,165 % moderat negativ, **Alpha -0,540 % NEGATIV** (LLY XLV-Tag-6-Underperform + AAPL XLK-Fill-Day+1-Underperform dominant, teilweise kompensiert durch JPM Post-Q2 +2,33 % und GOOGL Fill-Day+6-Rebound +1,98 %). **LLY neu engste V1-Position +5,09 %** (RSI 49,90 unter 50 gekippt, XLV -1,92 % Tag 6 → Watch-Modus für Mi Pre-Market). **UNH-Blackout-V1 381,49 weiter aktiv** bis Do 16.07. BMO. **JPM-Blackout beendet** post-Release (V1 306,16 komfortabel +11,81 %). Alle V1–V6 SICHER → **keine Limit-Order für Mi 15.07.** Sektor-Rotations-Umkehr: XLK-Rebound (+1,27 % nach Mo -2,44 %), XLV weiter schwach (-1,92 %), XLP -1,39 % ungewöhnlich, VXX -1,47 % Vola-Reduktion (VIX-Umfeld stabil ~16).
> **Zwingender Watch Mi 15.07.:** (1) **LLY V1 1.098,38 aktiv +5,09 % Puffer** (engste, RSI 49,90 gekippt, XLV-Tag-6-Trend) — Pre-Market Live-Watch, Break unter 1.098,38 löst V1-Market-Sell; (2) UNH-Blackout weiter aktiv V1 381,49 +11,60 %; (3) GOOGL V1 338,65 +6,15 %; (4) **NVDA/V/GS K5-Multi-Source-Recheck Pre-Market Mi** für Slot 2/2 KW29 (Konzentrationscheck GS vs JPM); (5) AAPL Fill-Day+1 XLK-Divergenz-Monitoring.
> **Lessons-Tag:** (1) JPM Post-Q2-Rally Tag 2 (+2,33 % Di nach +1,90 % Mo Midday) — Blackout-Auslauf-Trade regel-konform und deutlich alpha-generierend; (2) LLY XLV-Sektor-Tag-6 zeigt Sektor-Rotation-Effekt: 5 Positionen aus 4 Sektoren (XLK/XLC/XLF/XLV/XLV) mit XLV-Cluster (LLY+UNH) trägt Alpha-Verlust — LLY einzelwert-schwach + Sektor-schwach kombiniert; (3) GOOGL Fill-Day+6-Rebound +1,98 % nach Mo -1,32 % Fill-Day+5-Divergenz — Muster: Fill-Day-Drop kann sich innerhalb 6 HT umkehren (kein Stop bei GOOGL notwendig).
> **Nächste Routine:** Mi 15.07. 08:30 ET Pre-Market Check (KW29 Tag 3, **LLY V1-Watch +5,09 % Puffer engste**, UNH-Blackout V1 381,49 bis Do BMO, NVDA/V/GS K5-Recheck für Slot 2/2).

---

## Midday 2026-07-14 13:07 ET (Di, KW29 Tag 2) — Alle V1-V4 SICHER, keine Stops ausgelöst, Daily -0,29 % GRÜN

```
Alpaca clock:      is_open=true | next_close 14.07. 16:00 ET
Equity:            98.279,39 $   (Live 13:07, vs Alpaca last_equity 98.562,62 → -0,287 %)
Cash:              58.804,04 $   (59,83 %, unverändert seit AAPL-Fill Mo)
Portfolio MV:      39.475,35 $   (40,17 %, AAPL 9.739,58 + JPM 1.022,67 + UNH 10.211,28 + LLY 9.224,96 + GOOGL 9.277,19)
Buying_power:     345.747,13 $
Daily P/L:           -283,23 $   (-0,287 % vs Alpaca last_equity)                        [GRÜN — Cap -3 %]
SPY Live:            +0,357 %    (Alpaca IEX 751,805 vs Mo-Close 749,13)
Alpha vs SPY:        -0,644 %    [NEGATIV — LLY -2,43 % XLV-Schwäche Tag 5 dominierend]
ATH:              100.066,47 $    DD -1,786 % [GRÜN — Alarm bei -15 %]
Weekly KW29:        -0,347 %      (Tag 2, Basis Fr-Close 98.621,81)                       [GRÜN — Cap -5 %]
Käufe KW29:            1/2       Slot 2/2 bleibt OFFEN (AMD K5-Fail Open)                 [OFFEN]
Pending Orders:        0         (keine Limit-/TP-Orders aktiv)
VIX-Ref:            ~16-17        (VXX carry-over)                                        [GRÜN]
Guardrails: Daily -0,29 % | Weekly -0,35 % | DD -1,79 % | VIX ~16 | Käufe 1/2 → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca IEX 13:07 ET):**
- **AAPL**  314,18 $ (Entry 316,86, P/L -0,85 %, chg_today -0,99 %) — Fill-Day+1, mild negativ
  - V1 291,51 SICHER (+7,78 % Puffer)
- **JPM**   340,89 $ (Entry 332,78, P/L +2,44 %, chg_today **+1,90 %**) — **Post-Q2-Rally Fortsetzung**, +2,44 % Tages-Reaction
  - V1 306,16 (post-Blackout Reset) SICHER (+11,34 % Puffer)
- **UNH**   425,47 $ (Entry 401,57, P/L +5,95 %, chg_today -0,84 %) — Cooldown, Blackout aktiv
  - V1 381,49 (Blackout -5 %) SICHER (+11,53 % Puffer)
- **LLY**  1.153,12 $ (Entry 1.193,89, P/L -3,42 %, chg_today **-2,43 %**) — **XLV-Verkaufsdruck Tag 5, ENGSTE Position**
  - V1 1.098,38 SICHER (+4,98 % Puffer — knappste, aber Puffer minimal aufgeholt vs Open +4,80 %)
- **GOOGL**  356,82 $ (Entry 368,10, P/L -3,07 %, chg_today +1,22 %) — **Fill-Day+5 Rebound**, Puffer erweitert
  - V1 338,65 SICHER (+5,36 % Puffer, vs Open +4,17 % deutlich verbessert)

**V1-V4-Check Midday: ALLE 5 POSITIONEN SICHER.**
- V1 (-8 % / -5 % bei UNH-Blackout): keine Position im Bereich
- V2 (-12 % vom Posit-Hoch, carry-over): LLY 1.098,71 (Hoch 1.248,53 × 0,88) engste, aktueller Kurs 1.153,12 → SICHER
- V3 (+20 % TP1): keine Position im Bereich — beste ist UNH bei 481,88 (aktuell 425,47, -11,7 % entfernt)
- V4 (+35 % TP2): weit entfernt

**Keine Sell-Order platziert. Keine Limit-Order platziert. Pending Orders bleiben 0.**

**Ø P/L über alle 5 Positionen:** +0,21 % | **Beste:** UNH +5,95 % | **Schlechteste:** LLY -3,42 %

**Guardrails Midday (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,287 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,347 % (KW29 Tag 2)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,786 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,786 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,357 %                          [INAKTIV]
6. VIX-Filter (>30):          ~16-17                                [GRÜN]
7. Earnings-Blackout (3 HT):  UNH aktiv (V1 381,49)                 [GRÜN operativ]
8. Max Käufe KW29:            1/2 → Slot 2/2 bleibt OFFEN           [OFFEN]
```

**Kein ClickUp Alert** (keine Stops ausgelöst, kein Daily Cap erreicht — Routine-Regel: nur bei Ereignis loggen).

**Nächste Routine:** Di 14.07. 16:00 ET Market Close + Tagesbilanz.

---

## Market Open 2026-07-14 09:37 ET (Di, KW29 Tag 2) — Guardrails GRÜN, AMD K5-Reject FwdPE > 35, KEIN Kauf, JPM V1-Reset 306,16 post-Release

```
Alpaca clock:      is_open=true | next_close 14.07. 16:00 ET
Equity:            98.281,72 $   (Live 09:37, vs Mo-Close 98.587,07 → -0,310 %)
Cash:              58.804,04 $   (59,83 %, unverändert)
Portfolio MV:      39.477,68 $   (40,17 %, AAPL 9.752,60 + JPM 1.011,36 + UNH 10.335,96 + LLY 9.208,72 + GOOGL 9.172,02)
Buying_power:     345.753,66 $
Daily P/L:           -280,90 $   (-0,285 % vs Alpaca last_equity 98.562,62)                [GRÜN — Cap -3 %]
SPY Live:            +0,180 %    (Alpaca IEX 750,48 Live vs Mo-Close 749,13)
Alpha vs SPY:        -0,465 %    [LEICHT NEGATIV — LLY -2,79 % Tages-Drift dominierend, JPM +0,75 % Post-Earnings]
ATH:              100.066,47 $    DD -1,781 % [GRÜN — Alarm bei -15 %]
Weekly KW29:        -0,345 %      (Tag 2, Basis Fr-Close 98.621,81)                        [GRÜN — Cap -5 %]
Käufe KW29:            1/2       Slot 2/2 bleibt OFFEN — AMD K5-Fail, kein Ersatz-Kandidat [OFFEN]
Pending Orders:        0
VIX-Ref:            ~16-17        (VXX Mo-Close 21,79 carry-over)                          [GRÜN]
Guardrails: Daily -0,28 % | Weekly -0,35 % | DD -1,78 % | VIX ~16 | Käufe 1/2 → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca IEX 09:37 ET):**
- **AAPL**  314,60 $ (Entry 316,86, P/L -0,71 %, chg_today -0,904 %) — Fill-Day+1 mildes Drift
  - V1 291,51 SICHER (+7,92 % Puffer)
- **JPM**   337,12 $ (Entry 332,78, P/L +1,30 %, chg_today **+0,753 %**) — **Post-Q2-Release POSITIV, Pre-Market-Dip +2,26 %-Loss vollständig aufgeholt**
  - V1 **306,16 NEU** (Blackout ENDET nach 8:30 AM Call, Reset -8 %) SICHER (+10,11 % Puffer)
- **UNH**   430,67 $ (Entry 401,57, P/L +7,25 %, chg_today +0,380 %) — Blackout aktiv
  - V1 381,49 (Blackout -5 %) SICHER (+12,89 % Puffer)
- **LLY**  1.151,09 $ (Entry 1.193,89, P/L -3,58 %, chg_today **-2,780 %**) — **XLV-Verkaufsdruck Tag 5, engste Position mit GOOGL**
  - V1 1.098,38 SICHER (+4,80 % Puffer, deutlich verengt von PM +7,43 %)
- **GOOGL**  352,77 $ (Entry 368,10, P/L -4,16 %, chg_today +0,065 %) — Fill-Day+5, stabil
  - V1 338,65 SICHER (+4,17 % Puffer)

**V1-V6-Check Open: ALLE 5 POSITIONEN SICHER. Keine Sell-Order platziert. Pending Orders bleiben 0.**

**Kandidaten-Scan K1-K5 (Slot 2/2 KW29):**

| Sym  | K1 EMA-Spread | K2 RSI | K3 RS_63d   | K4 Vol             | K5 FwdPE / RevGrw     | Verdict     |
|------|---------------|--------|-------------|--------------------|-----------------------|-------------|
| **AMD** | ✓ +153,00 | ✓ 52,97 | ✓ +107,54 % | ✓ ~2,7× Avg20 (extrap.) | ✗ **35,72-68,65 / +34,1 %** | **4/5 K5-FAIL** |
| CAT  | ✓             | ✗ 46,87 knapp | ✓  | —                 | —                     | 2/3 FAIL     |
| NVDA | ✓             | ✗ 49,93 knapp | ✗ -2,54 % | —              | —                     | 2/3 FAIL     |

**K5-Detail AMD Multi-Source-Recheck (Perplexity 09:38 ET):**
- Forward P/E NTM: GuruFocus 35,72 (grenzwertig) / GuruFocus term-page 36,98 / StockAnalysis 59,82 / ValueInvesting.io 68,65 / MarketBeat-Snapshot 59,82
- → **Konsens > 35, sogar strengste Quelle 35,72 verletzt Threshold** → **K5 FAIL**
- Trailing P/E: 101,79-173,93 (Hyper-Premium nach +117 % 63d Rally)
- Revenue Growth Q4 CY2025: +34,1 % YoY (10,27 Mrd $) — K5-Wachstum ✓, aber Bewertung Fail dominiert
- AMD Q2 2026 Earnings: **04.08.2026** (15 HT weg → kein Blackout)

**Entscheidung KEIN KAUF:**
- Nur AMD war 3/3 K1-K3 LEAD → K5-Reject regelkonform (FwdPE-Cap 35 ist absolute Grenze der Strategie).
- Backup-Kandidaten CAT/NVDA/TSLA scheiterten bereits Mo Close an K2/K3.
- Kein Sektor-Rotation-Ersatz identifiziert (Sektor-Perplexity-Query nicht durchgeführt, da AMD K5-Fail vor Sektor-Wechsel — 2/2-Käufe-Regel würde ohnehin keine sofortige Alternative erzwingen).
- **Slot 2/2 KW29 bleibt OFFEN** — Prüfung Mi-Fr 15.-17.07. bei neuer Signal-Konstellation.

**JPM V1-Reset (post-Blackout):**
- Q2-Release ist erfolgt (BMO 7:00 AM ET + Call 8:30 AM ET) → Blackout-Ende
- V1 alt (Blackout -5 %): 316,14 → V1 **NEU (-8 %): 306,16** (332,78 × 0,92)
- Puffer aktuell: 337,12 vs 306,16 = **+10,11 % SICHER**

**Guardrails Market Open (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,285 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,345 % (KW29 Tag 2)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,781 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,781 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY-Live +0,180 %                     [INAKTIV]
6. VIX-Filter (>30):          ~16-17 (VXX 21,79 carry-over)         [GRÜN]
7. Earnings-Blackout (3 HT):  JPM ENDET post-Release, UNH aktiv      [GRÜN operativ, 1 Position -5 %-Tightening]
8. Max Käufe KW29:            1/2 → Slot 2/2 bleibt OFFEN            [OFFEN]
```

**Earnings-Blackouts KW29 (nach Post-Release-Update):**
- **JPM Q2 heute BMO RELEASED** — Blackout **beendet**, V1 zurück auf -8 % (306,16), Puffer +10,11 % SICHER
- **UNH Q2 Do 16.07.2026 BMO** — 3-HT-Blackout **aktiv** bis Do BMO, V1 381,49 SICHER +12,89 %
- **GOOGL Q2 22.07.** — 6 HT — 3-HT-Blackout aktivierbar ab Fr 17.07. Close (V1-Task Fr-Close)
- **AAPL Q3 30.07.** — 12 HT — 3-HT-Blackout ab Fr 24.07. Close (fern)
- **LLY Q2 05.08.** — 16 HT — weit weg
- **AMD Q2 04.08.2026** — 15 HT — weit weg (Blackout kein Faktor bei Kauf, aber K5-Fail dominant)

**Zwingende Watch-Punkte Midday 13:00 ET:**
1. **LLY V1-Puffer +4,80 %** engste Position — XLV-Verkaufsdruck Tag 5 überwachen, Break unter 1.098,38 löst V1-Market-Sell
2. **GOOGL V1-Puffer +4,17 %** eng zweitplatziert, Fill-Day+5
3. **JPM Post-Earnings-Reaction Weiterverlauf** (V1 306,16 sehr komfortabel, aber Reaction-Fade möglich)
4. **UNH V1 381,49 aktiv** (+12,89 % Puffer, Blackout bis Do 16.07. BMO)
5. **Keine Kauf-Kandidaten aktiv** — Slot 2/2 KW29 bleibt bis Signal-Wechsel offen

**Datenqualität:**
- Alpaca IEX Live-Trades ts 13:37 UTC (=09:37 ET) für alle 6 Symbole (5 Positionen + AMD + SPY)
- AMD Bars 259d 2025-07-01 → 2026-07-13 EMA/RSI/RS sauber berechnet (Wilder RSI, adjustment=split)
- Perplexity K5 AMD FwdPE Multi-Source Cross-Check (5 Datenpunkte: 35,72 / 36,98 / 59,82 / 59,82 / 68,65)
- Perplexity JPM Q2-Result: Date-Bug — offizielle 8-K/Transcript noch nicht indiziert; Alpaca-Price-Action als Ground-Truth (+0,75 % Post-Release = positive Reaction)
- Alpaca last_equity 98.562,62 (Mo After-Hours-Tick) vs Memory Mo-Close 98.587,07 (-24,45 Drift akzeptabel)

**ClickUp:** ITEM_246 Tier-Limit weiter aktiv → Fallback PushNotification an Owner erfolgreich versendet.

**Nächste Routine:** Di 14.07. 13:00 ET Midday Stop-Check (LLY/GOOGL V1-Puffer < 5 % beide beobachten, JPM Post-Earnings-Verlauf, UNH-Blackout aktiv).

---

## Pre-Market 2026-07-14 08:35 ET (Di, KW29 Tag 2) — Guardrails GRÜN, JPM Q2 BMO TODAY, JPM-Puffer VERENGT +3,43 %, AMD Kauf-Kandidat für Slot 2/2

```
Alpaca clock:      is_open=false | next_open Di 14.07. 09:30 ET | next_close 16:00 ET
Equity:            98.529,29 $   (Pre-Market Live, vs Mo-Close 98.587,07 → -0,059 %)
Cash:              58.804,04 $   (59,68 %, unverändert seit AAPL-Fill Mo 11:31 ET)
Portfolio MV:      39.725,25 $   (40,32 %, AAPL 9.794,76 + JPM 980,91 + UNH 10.335,36 + LLY 9.440,00 + GOOGL 9.174,88)
Buying_power:     346.446,86 $
Daily P/L:            -57,78 $   (-0,059 %)                                            [GRÜN — Cap -3 %]
SPY Pre-Market:     +0,410 %     (Alpaca IEX 752,21 Live vs Mo-Close 749,13)
VXX Live:            21,79 (thin, bid-only) → VIX ~16-17 impliziert                     [GRÜN]
ATH:              100.066,47 $    DD -1,536 % [GRÜN — Alarm bei -15 %]
Weekly KW29:       -0,096 %       (Tag 2, Basis Fr-Close 98.621,81)                    [GRÜN — Cap -5 %]
Käufe KW29:            1/2       Slot 2/2 VERFÜGBAR — Kauf-Scan im Market Open 09:30 ET [OFFEN]
Pending Orders:        0
Guardrails: Daily -0,06 % | Weekly -0,10 % | DD -1,54 % | VIX ~16 | Käufe 1/2 → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca 08:35 ET):**
- **AAPL**  315,96 $ (Entry 316,86, P/L -0,28 %, chg_today -0,425 %) — Fill-Day+1 mildes Pre-Market-Drift
  - V1 291,51 SICHER (+8,39 % Puffer)
- **JPM**   326,97 $ (Entry 332,78, P/L -1,75 %, chg_today **-2,260 %**) — **Pre-Earnings-Drift vor Q2 BMO 7:00 AM ET**
  - V1 **316,14** (Blackout LAST DAY) SICHER (+3,43 % Puffer, **VERENGT** von Mo Close +5,84 %)
  - Post-Release 8:30 AM ET Call → V1 zurück auf -8 % (306,16)
- **UNH**   430,64 $ (Entry 401,57, P/L +7,24 %, chg_today +0,361 %) — XLV-Rebound-Fortsetzung
  - V1 **381,49 NEU** (Blackout -5 % aktiv Mo Close AKTIVIERT) SICHER (+12,88 % Puffer)
- **LLY**  1.180,00 $ (Entry 1.193,89, P/L -1,16 %, chg_today -0,158 %) — XLV milder
  - V1 1.098,38 SICHER (+7,43 % Puffer)
- **GOOGL**  352,88 $ (Entry 368,10, P/L -4,13 %, chg_today +0,105 %) — Fill-Day+5, engste Position
  - V1 338,65 SICHER (+4,20 % Puffer, minimal weiter aufgeholt vs Mo Close +4,10 %)

**V1-V6-Check Pre-Market: ALLE 5 POSITIONEN SICHER. Keine Sell-Order platziert. Pending Orders bleiben 0.**

**Guardrails Pre-Market (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,059 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,096 % (KW29 Tag 2)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,536 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,536 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY-PM +0,410 %                       [INAKTIV]
6. VIX-Filter (>30):          ~16-17 (VXX 21,79 thin)               [GRÜN]
7. Earnings-Blackout (3 HT):  JPM RELEASE TODAY, UNH aktiv          [GRÜN operativ, 2 Positionen -5 %-Tightening]
8. Max Käufe KW29:            1/2 → SLOT 2/2 VERFÜGBAR              [OFFEN]
```

**Earnings-Blackouts KW29:**
- **JPM Q2 Di 14.07. BMO 7:00 AM ET / Call 8:30 AM ET CONFIRMED** — Blackout **letzter Tag** (V1 316,14, +3,43 % Puffer PM); **Post-Release-Update Pre-Market ZWINGEND** → V1 zurück auf -8 % (306,16) nach 8:30 AM Call
- **UNH Q2 Do 16.07. BMO** — 3-HT-Blackout **aktiv** ab Mo 13.07. Close, V1 **381,49 SICHER +12,88 %** — endet nach Do BMO
- **GOOGL Q2 22.07.** — 6 HT — 3-HT-Blackout ab Fr 17.07. Close
- **AAPL Q3 30.07.** — 12 HT — 3-HT-Blackout ab Fr 24.07. Close (fern)
- **LLY Q2 05.08.** — 16 HT — weit weg

**Watchlist Kauf-Prep KW29 Slot 2/2 (Kauf-Scan im Market Open 09:30 ET):**
- **AMD 533,69** LEAD-Kandidat (3/3 K1-K3, RS_63d +107,26 %) — K5-Recheck + AMD-Q2-Earnings-Blackout-Check **ZWINGEND** im Open (AMD-Q2 typisch Anfang August)
- **CAT 931,96** Backup — 2/3 K2-Fail (RSI 46,87 knapp), K2-Recheck im Open
- **NVDA 203,49** Backup — 2/3 K3-Fail (RS -2,54 %), RS-Watch
- **TSLA 394,86** 2/3 K2-Fail — Backup-only

**Entscheidung Pre-Market:** No-Op-Positionsseite (alle 5 V1 SICHER). **Kauf-Scan AKTIV im Market Open** (Slot 2/2, alle Guardrails GRÜN, AMD K5-Multi-Source-Recheck + Earnings-Blackout-Check entscheidet LEAD-Kauf).

**Zwingende Watch-Punkte Market Open:**
1. **JPM Q2 Earnings-Reaction post-8:30 AM Call** — PM-Puffer nur +3,43 %, Break unter 316,14 löst V1-Market-Sell
2. **JPM Post-Release V1-Update 316,14 → 306,16** (Blackout endet nach Call)
3. **AMD K5-Multi-Source-Recheck + Earnings-Blackout-Check** ZWINGEND vor Kauf-Order
4. **GOOGL V1-Puffer +4,20 %** engste Position, Fill-Day+5
5. **UNH V1 381,49 aktiv** (+12,88 % Puffer, Blackout-Aktivierung erfolgreich Mo Close)

**Datenqualität:**
- Alpaca IEX SPY 752,21 Pre-Market als Ground-Truth
- VXX bid-only 21,79 im Pre-Market (thin, ap=0) → VIX-Referenz aus Mo-Close ~16-17 gehalten
- Perplexity Date-in-Future-Bug bei Live-Werten reproduziert — Alpaca-Fallback erfolgreich
- Perplexity Earnings-Multi-Query: JPM Q2 Di 14.07. BMO 7:00 AM ET CONFIRMED (Perplexity + JPM IR), andere Symbole NOT_FOUND → Memory-Carry-Over
- Alpaca last_equity 98.562,62 vs Memory Mo-Close 98.587,07 (-24,45 After-Hours-Drift, akzeptabel)

**Nächste Routine:** Di 14.07. 09:30 ET Market Open (KW29 Tag 2, JPM Q2-Post-Release-Reaction + V1-Reset, AMD K5-Scan + Kauf-Slot 2/2).

**ClickUp:** ITEM_246 Tier-Limit weiter aktiv (Fallback PushNotification an Owner erfolgreich versendet).

---

## Market Close 2026-07-13 16:02 ET (Mo, KW29 Tag 1) — Tagesbilanz, UNH-Blackout AKTIVIERT V1→381,49, AAPL 5/5-Signal validiert (Alpha +0,73 % trotz XLK -2,44 %)

```
Alpaca clock:      is_open=false | next_open Di 14.07. 09:30 ET | next_close 16:00 ET
Gesamtwert:        98.587,07 $   (Alpaca equity Close, vs last_equity 98.622,21 Fr-After-Hours)
Cash:              58.804,05 $   (59,65 %, unverändert seit AAPL-Fill)
Investiert (MV):   39.784,84 $   (40,35 %, AAPL 9.840,74 + JPM 1.003,59 + UNH 10.299,36 + LLY 9.476,72 + GOOGL 9.164,43)
P/L heute:            -35,14 $   (-0,036 %)  [GRÜN — vs Alpaca last_equity 98.622,21, Cap -3 %]
SPY-Tag:           -0,770 %      (Alpaca IEX 754,94 → 749,13)
Alpha vs SPY:      +0,734 %      [DEUTLICH POSITIV — AAPL +0,673 % / UNH +1,064 % / JPM -0,577 % / LLY -0,336 % / GOOGL -1,316 %]
ATH:              100.066,47 $   DD -1,479 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW29:  -0,036 %       (Tag 1, Basis Fr-Close 98.621,81)                       [GRÜN — Cap -5 %]
Käufe KW29:            1/2       (AAPL gefüllt 11:31 ET, 1 Slot noch offen bis Fr-Close)
Pending Orders:        0         (alle V5/V6 SICHER — KEINE Limit-Order für Di 14.07.)
VIX-Ref:            ~15-17       (VXX +3,171 % Vola-Tick, aber weit unter 30)
Guardrails: Daily -0,04 % | Weekly -0,04 % | DD -1,48 % | VIX ~16 | Käufe 1/2 → ALLE GRÜN
```

**Positionen Close V1–V6 (Alpaca IEX 259d Bars, EMA/RSI Wilder):**
| Sym    | Close    | P/L      | Chg_today | V1-Stop        | V1-Puffer | V5 EMA-Spread | V6 RSI  | V6 RS_4w   | Status |
|--------|----------|----------|-----------|----------------|-----------|---------------|---------|-----------|--------|
| AAPL   |  317,47  |  +0,19 % |  +0,673 % | 291,51 (-8 %)  | +8,90 %   | +24,41        | 64,92   | +5,63 %   | SICHER (Fill-Day+0, V2-Trail 284,58) |
| JPM    |  334,60  |  +0,53 % |  -0,577 % | **316,14 NEU** | +5,84 %   | +12,19        | 59,30   | +5,38 %   | SICHER (Blackout -5 % LETZTER Tag vor Q2 Di 14.07. BMO) |
| UNH    |  429,04  |  +6,87 % |  +1,064 % | **381,49 NEU** | +12,47 %  | +48,15        | 61,70   | +4,65 %   | SICHER (**Blackout AKTIVIERT ab HEUTE**, V1 -5 %) |
| LLY    | 1.183,95 |  -0,78 % |  -0,336 % | 1.098,38 (-8 %)| +7,79 %   | +128,16       | 56,39   | +0,20 %   | SICHER (XLV +0,31 % Rebound) |
| GOOGL  |  352,54  |  -4,24 % |  -1,316 % | 338,65 (-8 %)  | +4,10 %   | +44,89        | 44,02   | -3,31 %   | SICHER (**engste**, Fill-Day+4, XLC -0,02 %) |

**V5/V6-Check heute: ALLE 5 POSITIONEN SICHER.** → **Keine Limit-Order für Di 14.07.** (Pending Orders bleiben 0.)

**Schlechteste Position:** GOOGL -4,24 % (V1-Puffer +4,10 % engste Position, Fill-Day+4 Divergenz zu XLC -0,02 % verstärkt, EMA50 gedreht knapp unter Close 352,54 vs 358,95)
**Beste Position:** UNH +6,87 % (change_today +1,064 % XLV-Rebound-Winner)

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLE +3,041 % (LEAD)
XLU +0,683 % | XLF +0,628 % | XLRE +0,574 % | XLP +0,541 % | XLV +0,311 %
XLC -0,022 % | XLB -0,590 % | XLI -0,901 % | XLY -0,986 %
XLK -2,438 %  (Tech-Sell-off)
VXX +3,171 % (Vola-Tick)
```
→ **Klare Defense-Rotation (XLU/XLF/XLP/XLV grün, Zykliker & Tech rot).** Bot-Positionen: JPM XLF +0,628 % Sektor, aber JPM -0,577 % Einzelwert-schwach (letzter Blackout-Tag Positioning); UNH+LLY XLV +0,311 % Sektor grün (Rebound nach 3 Tagen raus, UNH +1,06 % Sektor-Winner); GOOGL XLC -0,02 % + eigenwert-schwach; **AAPL XLK -2,44 % → AAPL +0,673 % = MASSIVES OUTPERFORM (+3,11 % vs Sektor!)** → 5/5-Kaufsignal validiert.

**⚠ UNH V1-Stop-Tightening AKTIVIERT ab jetzt (Close 16:02 ET):**
- V1 alt (-8 %): 369,44 → V1 **NEU (-5 %): 381,49**
- Gilt bis Q2 16.07.2026 BMO (Blackout-Ende = Earnings-Tag Do 16.07.)
- Puffer aktuell: 429,04 vs 381,49 = **+12,47 % SICHER**
- Di 14.07. Pre-Market ZWINGEND: UNH < 381,49 → V1-Market-Sell

**⚠ JPM V1-Blackout LETZTER Tag:** V1 316,14 (-5 %), Puffer +5,84 %. Endet Di 14.07. nach Q2-Release (BMO 8:30 AM ET) → V1 zurück auf -8 % (306,16). Zwingender Mi 15.07. Pre-Market-Task.

**Guardrails Close (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,036 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,036 % (KW29 Tag 1)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,479 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,479 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,770 %                          [INAKTIV]
6. VIX-Filter (>30):          ~16 (VXX +3,17 %)                     [GRÜN]
7. Earnings-Blackout (3 HT):  JPM letzter Tag AKTIV, UNH AKTIVIERT  [GRÜN operativ, 2 Positionen -5 %-Tightening]
8. Max Käufe KW29:            1/2 (AAPL gefüllt, 1 Slot offen)      [OFFEN]
```

**Weekly Loss Cap Prüfung KW29 Tag 1:**
- Weekly P/L = -0,036 % (Basis Fr-Close 98.621,81)
- Cap-Trigger -5 %: **NEIN**, weit unter Schwelle
- KEINE Pending-Order zu stornieren (bereits 0)
- KEIN WEEKLY_CAP-Alert

**Watchlist Di 14.07. + KW29-Kauf-Prep (Alpaca 259d K1-K3 Screener):**
```
Sym    Close Mo    K1 EMA-Spread    K2 RSI    K3 RS_63d      Verdict
AMD    533,69     ✓ +152,60         ✓ 52,97   ✓ +107,26 %    3/3 LEAD (K5 morgen Pre-Market zwingend)
CAT    931,96     ✓ +196,39         ✗ 46,87   ✓ +7,50 %      2/3 FAIL (K2 knapp unter 50 — Recheck möglich)
NVDA   203,49     ✓ +10,56          ✗ 49,93   ✗ -2,54 %      2/3 FAIL (RS weiter negativ, RSI unter 50)
TSLA   394,86     ✓ +1,78           ✗ 47,30   ✓ +2,63 %      2/3 FAIL
META   656,87     ✗ (EMA50 unter EMA200 nach Split-Adj) ✓ 62,83 ✗ -6,17 %  FAIL
AMZN   247,32     ✓ +8,00           ✓ 53,05   ✗ -6,82 %      2/3 FAIL
```
→ **AMD einziger 3/3-LEAD** (XLK — Chip-Rally hat AMD-RS auf +107 % vs SPY 63d katapultiert). **K5-Recheck Multi-Source zwingend Di Pre-Market** (FwdPE ≤ 35? RevGrowth ≥ 10 %? Earnings-Blackout?).
→ **Backup:** CAT (K2 nur 3,13 Punkte unter 50 — Recheck bei möglicher Erholung).
→ **Sektor-Kontext:** XLK -2,44 % Down-Day → AMD-Kauf antizyklisch, aber K3 RS +107 % dominiert.

**Datenqualitäts-Hinweise:**
- Alpaca IEX 259d Bars für alle 5 Positionen (Fr 2025-07 → Mo 2026-07-13 inklusive Heute-Close-Bar) — EMA50/EMA200 + Wilder RSI(14) full-history.
- SPY Alpaca IEX 749,13 vs Fr-Close 754,94 = **-0,770 %** Ground-Truth für Alpha (Perplexity nicht abgefragt — Alpaca zuverlässiger, VIX ohnehin via VXX-Proxy stabil).
- Sektor-ETF-Marks Alpaca IEX (12/12 erfolgreich).
- Alpaca `equity` 98.587,07 vs `last_equity` 98.622,21 (Fr-After-Hours-Tick) — Daily-P/L auf Alpaca last_equity gerechnet (Ground-Truth), Memory Fr-Close 98.621,81 (+0,40 After-Hours-Drift, konsistent).

**ClickUp:** [CLOSE] Tagesbilanz Task Prio 4 (Portfolio -0,036 % marginal aber **Alpha +0,734 % stark positiv** → Priorität Low). Bei Tier-Limit Fallback auf PushNotification.

> **Entscheidung Market Close 13.07.:** Portfolio -0,036 % marginal negativ, aber **Alpha +0,734 % DEUTLICH POSITIV** dank AAPL-Outperform gegen XLK-Sell-off (+0,67 % vs Sektor -2,44 % = +3,11 % relativ) — 5/5-Kaufsignal validiert. UNH-XLV-Rebound +1,06 % (Sektor +0,31 %) und JPM -0,58 % Blackout-Positioning erwartbar. GOOGL Fill-Day+4-Divergenz zu XLC verstärkt (-1,32 % vs -0,02 %) → V1-Puffer schmilzt auf +4,10 % (engste). Alle V1-V6 SICHER → keine Limit-Order für Di 14.07. **UNH-Blackout AKTIVIERT: V1 auf 381,49 (-5 %) — gilt bis Q2 Do 16.07. BMO.** **JPM-Blackout LETZTER Tag vor Q2 Di 14.07. BMO** — endet nach Release, V1 zurück auf 306,16 dann.
> **Zwingender Watch Di 14.07.:** (1) JPM Q2-Earnings BMO 8:30 AM ET — Post-Release Pre-Market-V1-Update auf 306,16 sowie Reaction-Watch; (2) UNH V1 381,49 aktiv, Puffer +12,47 %; (3) GOOGL V1-Puffer +4,10 % **engste Position** — Break unter 338,65 löst V1-Market-Sell; (4) AMD K5-Multi-Source-Recheck Pre-Market für Kauf-Slot 2/2 (Earnings-Blackout Check zwingend).
> **Lessons-Tag:** (1) AAPL 5/5-Kaufsignal Fr → Fill Mo 11:31 → Close +0,19 % vs SPY -0,77 % = **+3,11 % Alpha vs XLK-Sell-off**. Sequenz K1-K5 all-green + Regel-konformer Limit-Buy (+0,5 %-Cap) hat Fill-Day-Drop-Muster (AVGO/MU) durchbrochen. (2) UNH-Blackout-Aktivierungs-Task 100 % planmäßig ausgeführt (V1 369,44 → 381,49). (3) GOOGL Fill-Day+4-Verengung — Muster jetzt eindeutig: AVGO-Stop, MU-Stop, GOOGL post-Fill-Divergenz mildester Form (kein Stop, aber -4,24 % nach 5 Handelstagen).
> **Nächste Routine:** Di 14.07. 08:30 ET Pre-Market Check (KW29 Tag 2, **JPM Q2-Earnings-Reaction-Watch BMO 8:30 AM ET**, UNH-V1 381,49 aktiv, GOOGL-V1-Puffer +4,10 % engste, AMD K5-Recheck für Slot 2/2).

---

## Midday 2026-07-13 13:00 ET (Mo, KW29 Tag 1) — AAPL FILL 11:31 ET, alle Stops regulär

```
Alpaca account:    equity 98.675,56 $ | last_equity (Fr-Close) 98.622,21 $
Daily P/L:         +53,35 $  (+0,054 %)                                  [GRÜN — Cap -3 %]
Cash:              58.804,05 $   (59,59 %, -9.822,55 vs Open durch AAPL-Fill)
Portfolio MV:      39.875,08 $   (40,41 %; AAPL 9.811,66 + JPM 1.003,25 + UNH 10.302,48 + LLY 9.511,32 + GOOGL 9.246,38)
Buying_power:     346.856,41 $
Positionen:            5/8 (AAPL neu, Kauf-Slot KW29 1/2 belegt & gefüllt)
Pending Orders:        0 (AAPL-Order-ID dba7bc05 vollständig gefüllt)
```

**Positionen-Check (Alpaca 13:00 ET Live):**
| Symbol | Qty | Entry $     | Curr $   | UPnL %  | V1-Stop  | V1-Puffer | V2-Trail (max_high×0,88) | V2-Puffer |
|--------|-----|-------------|----------|---------|----------|-----------|--------------------------|-----------|
| AAPL   | 31  | 316,86      | 316,51   |  -0,11 % | 291,51 (-8 %) | +8,58 % | 284,59 (max 323,39 heute) | +11,22 % |
| JPM    | 3   | 332,78      | 334,42   |  +0,49 % | **316,14** (Blackout -5 %) | +5,78 % | 302,11 (max 343,31 25.06.) | +10,70 % |
| UNH    | 24  | 401,57      | 429,27   |  +6,90 % | 369,44 (-8 %) | +16,20 % | 382,09 (max 434,19 09.07.) | +12,35 % |
| LLY    | 8   | 1.193,89    | 1.188,92 |  -0,42 % | 1.098,38 (-8 %) | +8,25 % | 1.098,70 (max 1.248,53 07.07.) | +8,22 % |
| GOOGL  | 26  | 368,10      | 355,63   |  -3,39 % | 338,65 (-8 %) | +5,03 % | 328,36 (max 373,14 07.07.) | +8,30 % |

**V1/V2-Check:** ALLE 5 POSITIONEN SICHER (kein Stop ausgelöst, keine Market-Sell platziert).
**V3/V4-Check (TP1 +20 % / TP2 +35 %):** Kein Symbol nahe TP → keine Limit-Sell platziert.

**Guardrails Midday:**
```
1. Daily Loss Cap (-3 %):     +0,054 %                                [GRÜN]
2. Weekly Loss Cap (-5 %):    +0,054 % (KW29 Tag 1)                   [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,39 % vs ATH 100.066,47              [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,39 %                                 [GRÜN]
5. Crash-Filter (SPY -5 %):   (nicht gemessen bei Midday)             [INAKTIV-Default]
6. VIX-Filter (>30):          Carry-over ~15                          [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIV (V1 316,14 +5,78 % SICHER)    [GRÜN operativ]
8. Max Käufe KW29:            1/2 gefüllt (Kauf-Slot 1 verbraucht)    [GRÜN]
```

**Best/Worst:**
- Beste Position: **UNH +6,90 %** (Ø-Trailing V2 +12,35 %)
- Schlechteste Position: **GOOGL -3,39 %** (V1-Puffer +5,03 % — engste Position, Fill-Day+4)
- Ø P/L 5 Positionen: **+0,69 %**

**Zwingende Watch-Punkte Market Close 16:00 ET:**
1. **UNH-Blackout-Aktivierung** (Q2 Do 16.07. BMO) → V1-Tightening 401,57 × 0,95 = **381,49 $** statt 369,44 ZWINGEND
2. **JPM Blackout letzter Tag** vor Q2 Di 14.07. BMO — V1 316,14 aktiv bis Post-Release
3. **GOOGL V1-Puffer +5,03 %** engste Position weiter monitoren
4. **AAPL Fill-Day+0** — heutiger Bar 323,39 max_high → V2-Trail 284,59 (wird morgen Close überprüft)

**ClickUp:** Kein Alert (per Midday-Regel: nur bei Stop-Trigger oder Daily-Cap). Routine-Log unterdrückt.

---


## Market Open 2026-07-13 09:37 ET (Mo, KW29 Tag 1) — AAPL 5/5 LEAD, Limit-Buy 316,90 x 31 platziert (kein Sofort-Fill)

```
Alpaca clock:      is_open=true | next_close 13.07. 16:00 ET
Equity:            98.525,80 $   (Live 09:37, vs Fr-Close 98.621,81 → -0,097 %)
Cash:              68.626,60 $   (69,66 %, unverändert)
Portfolio MV:      29.888,17 $   (30,34 %, JPM 1.004,46 + UNH 10.253,64 + LLY 9.374,72 + GOOGL 9.255,34)
Buying_power:     358.224,17 $
Daily P/L:            -96,01 $   (-0,097 %)                                             [GRÜN — Cap -3 %]
SPY Live:           -0,258 %     (Alpaca IEX 752,99 Live vs Fr-Close 754,94)
Alpha vs SPY:       +0,161 %     [LEICHT POSITIV — UNH +0,62 % / GOOGL -0,34 % / JPM -0,49 % / LLY -1,41 %]
ATH:              100.066,47 $    DD -1,540 % [GRÜN — Alarm bei -15 %]
Weekly KW29:       -0,097 %       (Tag 1, Basis Fr-Close 98.621,81)                     [GRÜN — Cap -5 %]
Käufe KW29:            0/2       (Kauf-Slot 1 mit Pending-Order belegt, kein Fill bislang)
Pending Orders:        1          (AAPL Limit-Buy 316,90 x 31 Day)
VIX-Ref:            ~15           (VXX carry-over Fr-Close 21,13 → GRÜN)
Guardrails: Daily -0,10 % | Weekly -0,10 % | DD -1,54 % | VIX ~15 | Käufe 0/2 (1 Pending) → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca 09:37 ET):**
- **JPM**   334,82 $ (Entry 332,78, P/L +0,61 %, chg_today -0,49 %) — XLF neutral
  - V1 **316,14** SICHER (+5,88 % Puffer, Blackout -5 % AKTIV vorletzter Tag bis Q2 Di 14.07. BMO)
- **UNH**   427,235 $ (Entry 401,57, P/L +6,39 %, chg_today +0,62 %) — XLV milde Erholung
  - V1 369,44 SICHER (+15,65 %), V2 381,89 SICHER (+11,86 %)
  - **⚠ Blackout-Aktivierung ab Mo Close ZWINGEND → V1 auf -5 % (381,49) für Do 16.07. BMO**
- **LLY**  1.171,84 $ (Entry 1.193,89, P/L -1,85 %, chg_today -1,41 %) — **XLV-Schwäche 4. Tag intraday verstärkt**
  - V1 1.098,38 SICHER (+6,69 % Puffer, verengt von Pre-Market +7,89 %)
  - V2 1.098,70 SICHER (+6,66 %)
- **GOOGL**  355,97 $ (Entry 368,10, P/L -3,29 %, chg_today -0,34 %) — **engste Position, Fill-Day+4**
  - V1 338,65 SICHER (+5,12 % Puffer, marginal verengt vs PM +5,03 %)
  - V2 328,36 SICHER (+8,41 %)

**V1-V6-Check Open: ALLE 4 POSITIONEN SICHER. Keine Sell-Order platziert.**

**Kandidaten-Scan (K1-K5 alle Live via Alpaca 240d Bars + Perplexity K5):**

| Sym    | K1 EMA Spread | K2 RSI  | K3 RS_63d    | K4 Vol*     | K5 FwdPE/RevGrw | Verdict     |
|--------|---------------|---------|--------------|-------------|-----------------|-------------|
| **AAPL** | ✓ +21,65    | ✓ 63,57 | ✓ +12,40 %   | ✓ ~172 % pj | ✓ 31-34 / +17 % | **5/5 LEAD** |
| NVDA   | ✓ +10,97      | ✓ 57,00 | ✗ **-0,19 %** | —           | —               | 2/3 FAIL   |
| CAT    | ✓ +180,52     | ✗ **49,65** | ✓ +7,93 %  | —           | —               | 2/3 FAIL   |
| AMZN   | ✓ +6,86       | ✓ 51,08 | ✗ **-7,07 %** | —           | —               | 2/3 FAIL   |

*K4 aus 9-min-Extrapolation, avg_vol20 AAPL = 2.112.565 Sh

**Signal-Nuance:** NVDA Memory-Pre-Market-Erwartung "3/3 K1-K3" widerlegt — der Fr-Sprung +4,09 % reichte nicht, um die 63-Tage-Underperformance vs SPY auszugleichen (RS -0,19 % marginal negativ). **AAPL einziger 5/5-LEAD.**

**Position-Sizing AAPL (VIX ~15 < 25 → 10 %):**
- Budget = 98.525,80 × 0,10 = 9.852,58 $
- Prev-Close Fr 10.07. IEX (verifiziert): 315,32 $
- Limit = round(315,32 × 1,005; 2) = **316,90 $** (max +0,5 %)
- Shares = floor(9.852,58 / 316,90) = **31 Sh** (Max-Invest 9.823,90 $ = 9,97 %)

**Order platziert (Alpaca 09:41:00 ET):**
- Order-ID: dba7bc05-4c6d-4380-bed8-3e3c4fd842e4
- Limit-Buy AAPL 31 Sh @ 316,90 $ Day
- Status: `new` (accepted, working)
- **Kein Sofort-Fill**: AAPL Live bid 321,20 / ask 321,48 gappte +1,93 % über Fr-Close → über Limit-Cap; regelkonform (Strategie +0,5 %-Deckel)
- Fill nur bei Intraday-Pullback unter 316,90; sonst Expiry EOD ohne Kauf
- **Käufe KW29:** 0/2 gefüllt, aber Kauf-Slot 1 durch Pending-Order operativ belegt

**K5 AAPL (Perplexity Multi-Source):**
- Forward P/E Konsens ~32,45 (GuruFocus 32,45 / StockAnalysis 34,61 / TIKR 31,44) → ≤ 35 ✓
- Umsatzwachstum YoY: +17 % (Q2 FY26 gemeldet 30.04.2026 via SEC 8-K) → ≥ 10 % ✓
- Nächstes Earnings: 30.07.2026 (17:00 ET) → 13 HT weg, kein 3-HT-Blackout

**Guardrails Market Open (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,097 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,097 % (KW29 Tag 1)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,540 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,540 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY-Live -0,258 %                     [INAKTIV]
6. VIX-Filter (>30):          ~15 (Fr-Close carry-over)             [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIV (V1 316,14 SICHER)          [GRÜN operativ]
8. Max Käufe KW29:            0/2 (1 Pending)                       [OFFEN]
```

**Earnings-Blackouts KW29 (unverändert):**
- **JPM Q2 Di 14.07. BMO** — Blackout vorletzter Tag (V1 316,14, +5,88 % Puffer); Auslauf morgen Post-Release → V1 zurück auf -8 % (306,16)
- **UNH Q2 Do 16.07. BMO** — 3-HT-Blackout aktivierbar **ab Mo 13.07. Close** → V1-Tightening 401,57 × 0,95 = **381,49 $** statt 369,44. **ZWINGENDER Close-Routine-Task Mo.**
- **AAPL Q3 Do 30.07.** — 13 HT — 3-HT-Blackout ab Fr 24.07. Close (fern) → kein Blockade beim heutigen Kauf
- **GOOGL Q2 22.07.** / **LLY Q2 05.08.** — weit weg

**ClickUp:** ITEM_246 Tier-Limit weiter carry-over → PushNotification als Fallback für Owner-Info.

**Zwingende Watch-Punkte Midday 13:00 ET:**
1. **AAPL Pending-Order Fill-Check** bei Pullback < 316,90; bei Fill → Cash/Positionen-Update + BUY-Alert
2. **JPM Live-Watch bei < 316,14** (Blackout-V1, Puffer +5,88 %) — vorletzter Blackout-Tag vor Q2 Di 14.07. BMO
3. **GOOGL Live-Watch** — Fill-Day+4, V1-Puffer +5,12 % engste Position
4. **LLY XLV-Schwäche verstärkt intraday** (-1,41 % vs PM -0,30 %) — V1-Puffer +6,69 % noch komfortabel

**Datenqualität:**
- Alpaca IEX 240d Bars K1-K4 sauber (heutiger Partial-Bar aus EMA/RSI/Vol-Berechnung ausgeschlossen via `end=2026-07-11`)
- Perplexity K5 AAPL Multi-Source konsistent (3 Quellen FwdPE, SEC-8K für RevGrowth) — Date-Bug diesmal umgangen
- Alpaca `equity` = 98.525,80 (Live 09:37); `last_equity` = 98.622,21 (Fr After-Hours-Tick)
- SPY IEX Live 752,99 vs Fr-Close 754,94 = -0,258 % (Ground-Truth)

**Nächste Routine:** Mo 13.07. 13:00 ET Midday Stop-Check (KW29 Tag 1, JPM-Blackout-V1-Watch 316,14 vorletzter Tag, AAPL-Pending-Fill-Check, GOOGL/LLY-Live-Watch, UNH-Blackout-Vorbereitung).

---

## Pre-Market 2026-07-13 08:35 ET (Mo, KW29 Tag 1) — Guardrails alle GRÜN, Kauf-Slot 2/2 OFFEN

```
Alpaca clock:      is_open=false | next_open Mo 13.07. 09:30 ET | next_close 16:00 ET
Equity:            98.587,61 $   (Pre-Market Live, vs Fr-Close Memory 98.621,81 → -0,035 %)
Cash:              68.626,60 $   (69,61 %, unverändert)
Portfolio MV:      29.961,01 $   (30,39 %, JPM 1.013,40 + UNH 10.218,96 + LLY 9.480,19 + GOOGL 9.248,46)
Buying_power:     358.397,22 $
Daily P/L:            -34,20 $   (-0,035 %)                                             [GRÜN — Cap -3 %]
SPY Pre-Market:     -0,440 %     (Alpaca IEX 751,62 Live vs Fr-Close 754,94)
VXX Live:           -0,014 %     (21,17 vs Fr-Close 21,13; VIX ~15,03 Fr Perplexity)    [GRÜN]
ATH:              100.066,47 $    DD -1,479 % [GRÜN — Alarm bei -15 %]
Weekly KW29:       -0,035 %       (Tag 1, Basis Fr-Close 98.621,81)                     [GRÜN — Cap -5 %]
Käufe KW29:            0/2       SLOT VERFÜGBAR — Kauf-Scan im Market Open 09:30 ET     [OFFEN]
Pending Orders:        0
Guardrails: Daily -0,03 % | Weekly -0,03 % | DD -1,48 % | VIX ~15 | Käufe 0/2 offen → ALLE GRÜN
```

**Positionen Live V1-Check (Alpaca 08:35 ET):**
- **JPM**   337,80 $ (Entry 332,78, P/L +1,51 %, chg_today +0,40 %) — XLF-stabil
  - V1 **316,14** SICHER (+6,84 % Puffer, Blackout -5 % AKTIV letzter Tag bis Q2 Di 14.07. BMO)
- **UNH**   425,79 $ (Entry 401,57, P/L +6,03 %, chg_today +0,28 %) — XLV milde Erholung
  - V1 369,44 SICHER (+15,25 %), V2 381,89 SICHER (+11,50 %)
  - **⚠ Blackout-Aktivierung ab Mo Close ZWINGEND → V1 auf -5 % (381,49) für Do 16.07. BMO**
- **LLY**  1.185,02 $ (Entry 1.193,89, P/L -0,74 %, chg_today -0,30 %) — XLV-Schwäche 4. Tag milder
  - V1 1.098,38 SICHER (+7,89 %), V2 1.098,70 SICHER (+7,87 %)
- **GOOGL**  355,71 $ (Entry 368,10, P/L -3,37 %, chg_today -0,41 %) — **engste Position, Fill-Day+4 Verengung**
  - V1 338,65 SICHER (+5,03 % Puffer, verengt von Fr +5,19 %)
  - V2 328,36 SICHER (+8,33 %)

**V1-V6-Check Pre-Market: ALLE 4 POSITIONEN SICHER. Keine Sell-Order platziert. Pending Orders bleiben 0.**

**Guardrails Pre-Market (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,035 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,035 % (KW29 Tag 1)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,479 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,479 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY-PM -0,44 %                        [INAKTIV]
6. VIX-Filter (>30):          ~15 (VXX flat 21,17)                  [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIV (V1 316,14 SICHER)          [GRÜN operativ]
8. Max Käufe KW29:            0/2 → SLOT VERFÜGBAR                  [OFFEN]
```

**Earnings-Blackouts KW29:**
- **JPM Q2 Di 14.07. BMO** — Blackout **letzter Tag** (V1 316,14, +6,84 % Puffer); Auslauf morgen Post-Release → V1 zurück auf -8 % (306,16)
- **UNH Q2 Do 16.07. BMO** — 3-HT-Blackout aktivierbar **ab Mo 13.07. Close** → V1-Tightening -5 % (401,57 × 0,95 = **381,49 $** statt 369,44). ZWINGENDER Close-Routine-Task Mo.
- **GOOGL Q2 22.07.** — 7 HT — 3-HT-Blackout ab Fr 17.07. Close
- **LLY Q2 05.08.** — 17 HT — weit weg

**Watchlist Kauf-Prep KW29 (Kauf-Scan im Market Open 09:30 ET):**
- **NVDA 210,99** LEAD-Kandidat (+4,09 % Fr-Sprung, 3/3 K1-K3) — K5-Recheck zwingend
- **AAPL 315,32** LEAD-Kandidat (-0,27 % Fr, 3/3 K1-K3, RS +10,33 % carry) — K5-Recheck zwingend
- **CAT 951,67** Backup — 2/3 K2-Fail RSI 48,93 (Recheck möglich)
- **AMZN 245,35** Backup — 2/3 K2-Fail, K1-Spread eng

**Entscheidung Pre-Market:** No-Op-Positionsseite (alle V1 SICHER). **Kauf-Scan AKTIV im Market Open** (Slot 2/2, alle Guardrails GRÜN, NVDA/AAPL K5-Multi-Source-Recheck entscheidet LEAD).

**Zwingende Watch-Punkte Market Open:**
1. NVDA/AAPL K1-K5-Live-Recheck (Alpaca Bars + Perplexity K5)
2. JPM Live-Watch bei < 316,14 (Blackout-V1, Puffer +6,84 %)
3. GOOGL Live-Watch — Fill-Day+4 Verengung (V1-Puffer +5,03 %, engste Position)
4. LLY XLV-Schwäche-4.-Tag-Fortsetzung — V1 +7,89 % Puffer noch reichlich

**Datenqualität:**
- Alpaca IEX SPY 751,62 Pre-Market als Ground-Truth
- Perplexity Daily-Macro Date-in-Future-Bug (kein Live-VIX/News); Alpaca-VXX-Fallback erfolgreich
- Perplexity Earnings JPM CONFIRMED; UNH-Suchergebnis-Lücke → Memory-Carry-Over Fr 10.07. genutzt
- Alpaca last_equity 98.622,21 vs Memory Fr-Close 98.621,81 (+0,40 After-Hours-Drift)

**Nächste Routine:** Mo 13.07. 09:30 ET Market Open (KW29 Tag 1, NVDA/AAPL K5-Scan + Kauf-Entscheidung).

---

## Wochenabschluss KW28 — 2026-07-10 (Fr, Weekly Review 17:00 ET)

```
Gesamtwert:        98.621,81 $   (Fr 10.07. Close, Alpaca IEX Ground-Truth)
Cash:              68.626,60 $   (69,59 %)
Investiert:        29.993,80 $   (30,41 %)
Depot Wochenstart: 99.420,34 $   (Mo-Basis 06.07. = Fr-Close 03.07. NYSE-Feiertag = Do 02.07. Close)
Wochenrendite:      -0,803 %     (-798,53 $)
SPY-Wochenrendite:  +1,353 %     (Alpaca IEX 744,86 Do 02.07. → 754,94 Fr 10.07.)
Alpha vs SPY:       -2,156 %     [DEUTLICH NEGATIV — XLV-Overweight + XLK-Rally-Miss]
YTD Depot:          -1,378 %     ((98.621,81 - 100.000) / 100.000)
YTD SPY:            +10,724 %    (Alpaca IEX 681,82 YE25 → 754,94)
YTD Alpha:          -12,10 %     [DEUTLICH NEGATIV — Bot lebt 40 Tage, ~70 % Cash + Selektions-Verluste]
ATH:              100.066,47 $   (30.06.2026)
Drawdown:            -1,444 %    [GRÜN — Alarm bei -15 %]
Offene Positionen:      4/8      (JPM XLF / UNH XLV / LLY XLV / GOOGL XLC)
Nächste Woche max Käufe: 2/2     verfügbar (KW28-LOCK endet Fr Close, KW29-Slot ab Mo 13.07.)
Watchlist KW29:  AAPL (LEAD XLK), NVDA (LEAD XLK), CAT (Backup XLI), AMZN (Backup XLY)
```

**Trade-Analyse KW28:**
- Käufe: 2 → LLY Mo 06.07. (9.551,10 $ @ 1.193,89), GOOGL Di 07.07. (9.570,57 $ @ 368,10)
- Verkäufe: 1 → MU V1-Stop Di 07.07. (Erlös 8.320,05 $ @ 924,45; realisierter Verlust -1.019,43 $ = -10,92 %)
- Stop-Loss-Trigger: 1 (MU V1 -8 % → Gap-Open erhöhte Realized-Loss auf -10,92 %)
- Ø Haltedauer geschlossen: 3 HT (MU 02.07. → 07.07.)
- Win-Rate KW28: 0/1 (0 %) — 2. V1-Stop nach AVGO KW26

**Sektor-Ranking KW28 (Alpaca IEX Do 02.07. → Fr 10.07., Ground-Truth):**
```
XLE +3,447 %  ← LEAD (kein Bot-Exposure)
XLK +2,942 %  ← LEAD (kein Bot-Exposure nach MU-Sell)
XLC +1,829 %  ← Bot 9,42 % via GOOGL
SPY +1,353 %
XLF +0,162 %  ← Bot 1,02 % via JPM
XLY +0,077 %
XLRE -0,559 %
XLU -0,776 %
XLP -1,029 %
XLI -1,049 %
XLV -1,765 %  ← Bot 19,97 % via UNH+LLY [SEKTOR-ROTATION-VERLIERER — Alpha-Killer]
XLB -2,154 %
VXX -4,259 %  (Vola stark entspannt, VIX-Woche 16-19 → 15-16)
```
→ **Top-3-Ranking KW29-Prep:** 1. XLE +3,45 % | 2. XLK +2,94 % | 3. XLC +1,83 %.
→ **Bot-Portfolio strukturell im schwächsten Sektor (XLV) übergewichtet** — 2/3 XLV-Slot-Belegung durch UNH+LLY.

**Sektorgewichtung Portfolio (Fr 10.07. Close, alle < 30 %-Cap):**
```
XLF  1,02 %  (JPM 1.009,14 $)
XLV  19,97 % (UNH 10.189,68 $ + LLY 9.508,56 $)  ← 2/3 Sektor-Slots, aber unter Cap
XLC  9,42 %  (GOOGL 9.286,42 $)
Cash 69,59 %
Total investiert: 30,41 %
```
→ Kein Cap-Verstoß, keine Reduktion nötig. Nur BEOBACHTUNG: XLV-Overweight zerrt an Alpha strukturell → KW29 XLK-Kauf würde Sektor-Balance verbessern.

**Guardrails Wochenschluss (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,374 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,803 %                              [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,444 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,444 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +1,353 % KW28                     [INAKTIV]
6. VIX-Filter (>30):          ~15-16 (VXX 21,13 KW28-Close)          [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIV bis Q2 14.07. BMO           [GRÜN operativ]
8. Max Käufe KW28:            2/2 abgeschlossen, KW29 Slot ab Mo    [KW29 offen]
```

**Blackout-Roadmap KW29:**
- **JPM Q2 14.07.2026 BMO** — Blackout weiter aktiv Mo (V1 316,14, +6,02 % Puffer). Ende Di 14.07. → V1 zurück auf -8 % (306,16) nach Earnings-Release.
- **UNH Q2 16.07.2026 BMO** — 3-HT-Blackout aktivierbar ab **Mo 13.07. Close** → V1-Tightening auf -5 % (401,57 × 0,95 = **381,49 $** statt 369,44). ZWINGENDER Close-Routine-Task Mo.
- **LLY Q2 05.08.2026 BMO** — 17 HT, weit weg.
- **GOOGL Q2 22.07.2026** — 7 HT, 3-HT-Blackout aktivierbar ab **Fr 17.07. Close** → V1-Tightening auf -5 % (368,10 × 0,95 = 349,70 $ statt 338,65). Close-Routine-Task Fr.

**Strategie-Status:** **STABIL** — Alle Regeln (K1-K5 Kaufsignale, V1-V6 Verkaufssignale, Blackout, Cap, Trailing) laufen wie designed. Zwei offene Beobachtungspunkte für Diskussion in nächsten Reviews (KW29/KW30): Fill-Day-Drop-Muster n=4 (3 von 4 letzten Käufen -Post-Fill-Selloff) und Sektor-Rotation-Anpassung. **KEINE Regel-Änderung KW29** — Sample zu klein.

**Wochenschluss-Entscheidung:** No-Op für Mo 13.07. Pre-Market. AAPL/NVDA K5-Recheck Mo Pre-Market entscheidet Kauf-Order (Slot 2/2 verfügbar). UNH-Blackout-V1-Tightening zur Mo-Close-Routine vorbereitet.

**Nächste Routine:** Mo 13.07. 08:30 ET Pre-Market Check (KW29 Tag 1, JPM-Blackout-V1-Watch 316,14, NVDA/AAPL K5-Recheck, UNH-Blackout-Vorbereitung).

---

## Market Close 2026-07-10 16:02 ET (Fr, KW28 Tag 5) — Tagesbilanz, KW28 abgeschlossen, alle V1-V6 SICHER

```
Alpaca clock:      is_open=false | next_open Mo 13.07. 09:30 ET | next_close 16:00 ET
Gesamtwert:        98.621,81 $   (Alpaca equity Close, vs last_equity 99.060,07 = Do After-Hours-Tick)
Cash:              68.626,60 $   (69,59 %, unverändert)
Investiert (MV):   29.993,80 $   (30,41 %, JPM 1.009,14 + UNH 10.189,68 + LLY 9.508,56 + GOOGL 9.286,42)
P/L heute:            -370,32 $   (-0,374 %)  [GRÜN — vs Memory Do-Close 98.992,13, Cap -3 %]
SPY-Tag:           +0,451 %       (Alpaca IEX 751,55 → 754,94)
Alpha vs SPY:      -0,825 %       [NEGATIV — LLY -2,225 % + UNH -1,641 % XLV -0,780 % Rotation-raus 3. Tag]
ATH:              100.066,47 $    DD -1,444 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,803 %        (Mo-Basis 99.420,34 = Fr-Close 03.07.) [GRÜN — Cap -5 %]
Käufe KW28:            2/2        (LOCK abgeschlossen — nächster Kauf Mo 13.07.)
Pending Orders:        0          (V5/V6 alle SICHER — KEINE Limit-Order für Mo 13.07.)
VIX-Ref:            ~15-16        (VXX -2,221 % → Vola-Entspannung fortgesetzt)
Guardrails:  Daily -0,37 % | Weekly -0,80 % | DD -1,44 % | VIX ~15 | Käufe 2/2 (LOCK-Ende Fr) → ALLE GRÜN
```

**Positionen Close V1–V6 (Alpaca IEX 210d Bars, EMA/RSI inkrementell Wilder aus Do-Close):**
- **JPM**  336,38 $ (Entry 332,78, P/L +1,08 %, change_today +0,288 %) — XLF +0,306 % Sektor-support
  - V1 **316,14** SICHER (Blackout -5 % AKTIV bis Q2 14.07. BMO, +6,02 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06., kein neues Hoch heute) SICHER (+10,19 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 ~318,04 > EMA200 ~306,99 ✓ (Spread +11,05 stabil weiter)
  - V6 RSI(14) ~62 / RS_4w vs SPY ~+5,0 % → SICHER (RSI <80, RS positiv)
- **UNH**  424,57 $ (Entry 401,57, P/L +5,73 %, change_today -1,641 %) — XLV -0,780 % Rotations-Verlierer 3. Tag
  - V1 369,44 SICHER (+12,98 % Puffer, gefallen von Do +16,84 %)
  - V2 Stop 381,89 (Posit-Hoch 434,19 carry-over Do 09.07., Tageshoch 432,75 kein neues Hoch) SICHER (+10,06 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 ~392,44 > EMA200 ~338,37 ✓ (Spread +54,07 sehr komfortabel)
  - V6 RSI(14) ~64 / RS_4w vs SPY ~+3,8 % → SICHER
- **LLY**  1.188,57 $ (Entry 1.193,89, P/L -0,45 %, change_today -2,225 %) — **XLV-Rotations-Verlierer 3. Tag** (schwächste heute)
  - V1 1.098,38 SICHER (+7,59 % Puffer, gefallen von Do +10,67 %)
  - V2 Stop 1.098,70 (Posit-Hoch 1.248,53 carry-over 07.07., kein neues Hoch) SICHER (+7,55 %)
  - V3 1.432,66 / V4 1.611,75 — nicht erreicht
  - V5 EMA50 ~1.105,81 > EMA200 ~993,65 ✓ (Spread +112,16 komfortabel)
  - V6 RSI(14) ~60 / RS_4w vs SPY ~+3,5 % → SICHER
- **GOOGL**  357,17 $ (Entry 368,10, P/L -2,97 %, change_today -0,476 %) — **XLC +0,968 % Divergenz fortgesetzt**, Fill-Day+3 Close
  - V1 338,65 SICHER (+5,19 % Puffer, weiter engste Position aber SICHER)
  - V2 Stop 328,36 (Posit-Hoch 373,14 carry-over 07.07.) SICHER (+8,07 %)
  - V3 441,72 / V4 496,93 — nicht erreicht
  - V5 EMA50 ~359,24 > EMA200 ~317,97 ✓ (Spread +41,27)
  - V6 RSI(14) ~47 / RS_4w vs SPY ~-2,5 % → NICHT ausgelöst (V6 verlangt BEIDES RSI>80 UND RS<0; RSI weit unter 80)

**V5/V6-Check heute: ALLE 4 POSITIONEN SICHER.** → **Keine Limit-Order für Mo 13.07. vorbereitet.** Pending Orders bleiben 0.

**Schlechteste Position:** GOOGL -2,97 % (Fill-Day+3, Divergenz zu XLC +0,97 % verstärkt; V1-Puffer +5,19 % weiter engste aber sicher)
**Beste Position:** UNH +5,73 % (trotz Tages-Rot -1,64 %; V2-Trail 381,89 hält +10,06 % Puffer)

**Sektor-Update:** JPM XLF 1,02 % + UNH XLV 10,33 % + LLY XLV 9,64 % + GOOGL XLC 9,42 % = **30,41 % investiert**. XLV Total 19,97 % (unter 30 %-Cap ✓, 2/3 XLV). 4/8 Positions-Slots belegt.

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLB +1,193 % | XLP +1,100 % | XLC +0,968 % | XLU +0,632 % | XLE +0,502 % | XLRE +0,498 %
XLI +0,472 % | XLF +0,306 % | XLY +0,278 % | XLK +0,267 %
XLV -0,780 %  (Rotations-Verlierer 3. Tag in Folge)
VXX -2,221 % (Vola-Entspannung fortgesetzt, VIX ~15-16 GRÜN)
```
→ **Breit grüner Tag, aber XLV klar der Rotations-Verlierer.** Bot-Positionen: UNH+LLY beide XLV -0,780 % (UNH -1,64 % / LLY -2,23 % einzelwert-schwächer als Sektor); GOOGL divergiert (XLC +0,97 %, GOOGL -0,48 % — Fill-Day+3 setzt sich fort); JPM +0,29 % XLF-konsistent.
→ **XLV-Rotation-raus 3. Tag zerdrückt Alpha strukturell** (-0,825 %). AAPL/NVDA-KW29-Prep validiert weiter (NVDA +4,09 % heute!).

**Daily Loss Cap (-3 %):** -0,374 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,803 % → GRÜN, keine Stornierungen (auch keine Pending-Orders zu stornieren).
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -1,444 % → GRÜN.
**Käufe KW28:** 2/2 → KW28 abgeschlossen. **Neuer Kauf-Slot ab Mo 13.07.** (2/Woche max).

**⚠ JPM V1-Blackout AKTIV weiter:** V1 316,14 (-5 % vom Entry) → Puffer +6,02 % SICHER. Bleibt aktiv bis Q2-Earnings 14.07.2026 BMO (Mo 13.07. + Di 14.07. = 2 HT bis Earnings).

**⚠ UNH-Blackout-Vorbereitung Mo 13.07. Close ZWINGEND:** UNH Q2 16.07.2026 BMO → 3-HT-Blackout aktivierbar ab Mo 13.07. Close → V1-Stop-Tightening auf -5 % vom Entry (401,57 × 0,95 = **381,49 $**, statt heutiger 369,44). Fr 10.07. Close 424,57 → +11,29 % Puffer geplant. **Zwingender Vorbereitungs-Task für Market-Close-Routine Mo 13.07.**

**Watchlist Mo 13.07. + KW29-Kauf-Prep (Alpaca K1-K3 carry-over aus Mi 08.07. + heutige Sektor-Bewegung):**
```
Sym    Close Fr    Chg Fr        Ranking KW29                              Kommentar
NVDA   210,99     +4,092 %      LEAD-Kandidat KW29 — 3/3 K1-K3            Massiver Tages-Sprung, K5-Recheck Mo Pre-Market zwingend; XLK +0,27 % Support-Sektor
AAPL   315,32     -0,266 %      LEAD-Kandidat KW29 — 3/3 K1-K3            Underperformt heute (SPY +0,45 % vs AAPL -0,27 % = -0,72 % Alpha); K5-Recheck Mo
CAT    951,67     +1,461 %      Backup — 2/3 K2-Fail                       XLI-Rebound +0,47 %; K2-RSI-Recheck (war 48,93) Mo
AMZN   245,35     -0,652 %      Backup — 2/3 K2-Fail, K1-Spread eng        XLY +0,28 % OK, aber AMZN individuell schwach
```
→ **NEUES LEAD-Ranking KW29:** NVDA (Tages-Momentum-Sprung) auf Augenhöhe mit AAPL — K5-Recheck beider Mo 13.07. Pre-Market entscheidet
→ CAT/AMZN bleiben Backup

**Datenqualitäts-Hinweise:**
- Alpaca IEX-Bars 210d verfügbar für alle 4 Positionen — EMA50/200 + RSI(14) Wilder inkrementell (Do-Close + Fr-Close-Update)
- SPY IEX 754,94 vs 751,55 (Do-Close) = +0,451 % Ground-Truth für Alpha (Perplexity nicht abgefragt — Alpaca IEX zuverlässiger)
- Sektor-ETF-Marks über Alpaca IEX (12/12 erfolgreich, inkl. VXX-Vola-Proxy)
- Alpaca last_equity 99.060,07 (Do After-Hours-Tick) vs Memory Do-Close 98.992,13 (+67,94 $ After-Hours-Drift) — Ground-Truth Memory-Close verwendet (Konvention)

**ClickUp:** [CLOSE] Tagesbilanz Task Prio 3 (Portfolio-Performance leicht negativ UND Alpha -0,825 % → Priorität Normal).

> **Entscheidung Market Close 10.07.:** Portfolio -0,374 %, aber Alpha stark negativ -0,825 % durch **XLV-Rotation-raus 3. Tag** (UNH -1,64 %, LLY -2,23 %). GOOGL Fill-Day+3-Divergenz zu XLC-Sektor verstärkt (-0,48 % vs +0,97 %). JPM +0,29 % einziger im Grünen. Alle V1-V6 SICHER → keine Limit-Order für Mo 13.07. **KW28 Käufe 2/2 abgeschlossen — LOCK endet Mo 13.07., Kauf-Slot resetet auf 2/2 verfügbar.** **UNH-Blackout-Aktivierung Mo 13.07. Close ZWINGEND vorzubereiten** (V1 → -5 % = 381,49).
> **Zwingender Watch Mo 13.07.:** (1) NVDA-Massives-Tages-Sprungs-Followthrough (+4,09 % Fr) → K5-Recheck Pre-Market, (2) AAPL-Underperformance-Followthrough vs SPY, (3) UNH-Blackout-Vorbereitung V1 auf 381,49 zur Close-Routine, (4) JPM Blackout-V1 316,14 (Puffer +6,02 %) — vorletzter Blackout-Tag.
> **Lessons-Tag:** (1) XLV-Rotation raus 3. Tag in Folge (Fr -0,78 %, Do -0,10 %, Mi -1,34 %) macht UNH+LLY strukturell schwach — Portfolio-Alpha wird gefressen; V1-Puffer schmilzt aber noch weit über Trigger. (2) NVDA +4,09 % vs AAPL -0,27 % zeigt Momentum-Shift innerhalb XLK — NVDA könnte AAPL als LEAD ablösen, Mo K5-Recheck entscheidend. (3) GOOGL Fill-Day+3-Muster nun eindeutig AVGO/MU-Fill-Day-Drop-Muster in mildester Form (kein V1-Trigger, aber Divergenz zu Sektor).
> **Nächste Routine:** Mo 13.07. 08:30 ET Pre-Market Check (KW29 Tag 1, JPM-Blackout-V1-Watch 316,14, NVDA/AAPL K5-Recheck, UNH-Blackout-Vorbereitung).

---

## Midday 2026-07-10 13:07 ET (Fr, KW28 Tag 5) — Stop-Check, alle SICHER

```
Alpaca clock:      is_open=true | next_close 10.07. 16:00 ET
Positionen:        4/8 (JPM/UNH/LLY/GOOGL)
Ø P/L (einfach):   +0,54 % (JPM +1,14 % / UNH +5,58 % / LLY -0,98 % / GOOGL -3,57 %)
Schlechteste:      GOOGL -3,57 % (V1-Puffer +4,81 % — engste Position, Fill-Day+3 weiter verengt, aber SICHER)
Beste:             UNH +5,58 % (V1-Puffer +14,77 %, Tagesroten -1,78 % vom Do-Hoch)
Stops:             alle regulär — kein V1/V2/V3/V4-Trigger
Daily P/L:           -493,37 $   (-0,498 %)  [GRÜN — vs Memory Do-Close 98.992,13]
Equity:            98.498,76 $   (Cash 68.626,60 / MV 29.871,87)
Buying_power:     358.148,45 $
Weekly KW28 P/L:  -0,927 %        (Mo-Basis 99.420,34 = Fr-Close 03.07.) [GRÜN]
DD vs ATH:        -1,567 %        (ATH 100.066,47) [GRÜN]
SPY-Live:         +0,302 %        (751,55 Do-Close → 753,82 Live 13:07)
Alpha vs SPY:     -0,800 %        [NEGATIV — LLY -2,85 % + UNH -1,78 % + GOOGL -1,10 % trotz SPY +0,30 %]
```

**Live-Check V1–V4 (Alpaca IEX 13:07 ET):**
- **JPM**  336,5705 $ (Entry 332,78, P/L +1,14 %, chg_today +0,33 %, MV 1.009,71)
  - **V1 316,14** (Blackout -5 % AKTIV bis Q2 14.07. BMO) SICHER (+6,46 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+11,41 %)
  - V3 399,34 / V4 449,25 — weit entfernt
- **UNH**  423,99 $ (Entry 401,57, P/L +5,58 %, chg_today -1,78 %, MV 10.175,76)
  - V1 369,44 SICHER (+14,77 % Puffer)
  - V2 Stop 381,89 (Posit-Hoch 434,19 carry-over Do 09.07.) SICHER (+11,02 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
- **LLY**  1.182,245 $ (Entry 1.193,89, P/L -0,98 %, chg_today -2,85 %, MV 9.457,96) — **XLV-Sektor-Rotation raus setzt sich fort**
  - V1 1.098,38 SICHER (+7,64 % Puffer)
  - V2 Stop 1.098,70 (Posit-Hoch 1.248,53 carry-over 07.07., kein neues Hoch) SICHER (+7,60 %)
  - V3 1.432,66 / V4 1.611,75 — nicht erreicht
- **GOOGL**  354,94 $ (Entry 368,10, P/L -3,57 %, chg_today -1,10 %, MV 9.228,44) — **Fill-Day+3 Verengung fortgesetzt** (Open -3,07 % → Midday -3,57 %)
  - V1 338,65 SICHER (+4,81 % Puffer, weiter engste Position aber SICHER — verengt von +5,08 % Open → +4,81 % Midday)
  - V2 Stop 328,36 (Posit-Hoch 373,14 carry-over 07.07.) SICHER (+8,09 %)
  - V3 441,72 / V4 496,93 — nicht erreicht

→ **Keine Verkaufsorder.** Alle 4 V1–V4 regulär SICHER — Puffer +4,81 % (GOOGL) bis +14,77 % (UNH).
→ **Daily Loss Cap (-3 %) nicht erreicht** (-0,498 %). Keine Order-Stornierung nötig (keine Pending-Orders).

**Guardrails-Status:**
```
1. Daily Loss Cap (-3 %):    -0,498 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):   -0,927 % (KW28 Mo-Basis 99.420,34)    [GRÜN]
3. Drawdown-Alarm (-15 %):   -1,567 % vs ATH 100.066,47            [GRÜN]
4. Käufe KW28:                2/2 (LOCK bis Mo 13.07.)             [KEIN weiterer Kauf KW28]
```

**Alpha-Kontext:** Bot underperformt SPY um -0,800 % durch **LLY -2,85 %** (XLV-Rotation raus, 2. Tag in Folge Schwäche), **UNH -1,78 %** (Cooldown vom Do-Hoch 434,19 → 423,99), **GOOGL -1,10 %** (Fill-Day+3 setzt sich fort). Nur JPM +0,33 % positiv (XLF-stabil). XLK/XLY-Rally von Do ohne Bot-Exposure setzt sich strukturell fort → AAPL/NVDA-KW29-Prep validiert (Kauf-Fenster Mo 13.07.).

**JPM V1-Blackout AKTIV:** V1 316,14 (-5 % vom Entry) → Puffer +6,46 % SICHER. Bleibt aktiv bis Q2-Earnings 14.07.2026 BMO.

**ClickUp:** kein Alert (keine Stops, kein Cap → Logging-Disziplin gewahrt).

> **Entscheidung:** No-Op — alle 4 Positionen halten. GOOGL Fill-Day+3 verengt sich weiter (-3,57 %), V1-Puffer +4,81 % weiterhin engste Position aber SICHER; V2-Trail 328,36 komfortabel. LLY -2,85 % 2. Tag Sektor-Rotations-Verlierer (XLV weiter raus) — V1 +7,64 % Puffer noch reichlich, aber Watch Close. UNH -1,78 % Cooldown vom Do-Hoch, V2 381,89 unverändert. JPM stabil im Blackout. Daily -0,498 % vs Memory Do-Close GRÜN.
> **Zwingender Watch bis Close:** (1) GOOGL V1-Puffer +4,81 % → Break unter 338,65 löst V1-Market-Sell aus, (2) LLY XLV-Rotations-Fortsetzung → V1 1.098,38 zu watchen, (3) JPM Blackout-V1 316,14 (Puffer +6,46 %).
> **Nächste Routine:** Fr 10.07. 16:00 ET Market Close (Tagesbilanz + V5/V6-Check aller 4 Positionen + Limit-Order für Mo 13.07. falls V5/V6-Trigger + KW29-Kauf-Prep AAPL/NVDA).

---

## Market Open 2026-07-10 09:37 ET (Fr, KW28 Tag 5) — No-Op, Käufe-Slot LOCK 2/2, alle V1 SICHER

```
Alpaca clock:      is_open=true | next_close 10.07. 16:00 ET | next_open Mo 13.07. 09:30 ET
Gesamtwert:        98.675,68 $   (Alpaca equity Live 09:37, vs Memory Do-Close 98.992,13)
Cash:              68.626,60 $   (69,55 %, unverändert)
Investiert (MV):   30.058,10 $   (30,46 %, JPM 1.013,25 + UNH 10.261,92 + LLY 9.506,00 + GOOGL 9.276,93)
Buying_power:     358.643,82 $
P/L heute:           -316,45 $   (-0,320 %)  [GRÜN — Cap -3 %]
SPY-Live:          +0,187 %       (Alpaca IEX 751,55 Do-Close → 752,955 Live 09:37)
Alpha vs SPY:      -0,507 %       [NEGATIV — GOOGL/LLY beide -Tagesroten trotz SPY-Plus]
ATH:              100.066,47 $    DD -1,390 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,749 %        (Mo-Basis 99.420,34)                  [GRÜN — Cap -5 %]
Käufe KW28:            2/2        (LOCK bis Mo 13.07.)                  [GESPERRT]
Pending Orders:        0          (keine Sell-Trigger, kein Kauf-Scan)
VIX-Ref:            ~16           (VXX Live 21,43 vs 22,03 Do-Close = -2,72 %)
Guardrails:  Daily -0,32 % | Weekly -0,75 % | DD -1,39 % | VIX ~16 | Käufe 2/2 LOCK → GRÜN + Slot-Lock
```

**Positionen Live (Alpaca 09:37 ET, V1-Puffer):**
- **JPM**   337,75 $ (Entry 332,78, P/L +1,49 %, chg_today +0,68 %)
  - V1 **316,14** SICHER (+6,84 % Puffer, Blackout -5 % AKTIV bis Q2 14.07. BMO)
  - V2/V3/V4/V5/V6 alle SICHER (carry-over Do-Close, keine Neuberechnung nötig)
- **UNH**   427,58 $ (Entry 401,57, P/L +6,48 %, chg_today -0,95 %)
  - V1 369,44 SICHER (+15,74 % Puffer), V2 381,89 SICHER (+11,96 %)
  - Rückgang -0,95 % Tageshoch 434,19 nicht wieder erreicht → V2-Trail bleibt 381,89
- **LLY**  1.188,25 $ (Entry 1.193,89, P/L -0,47 %, chg_today -2,36 %)
  - V1 1.098,38 SICHER (+8,18 % Puffer), V2 1.098,70 SICHER (+8,15 %)
  - **⚠ LLY schwächste Tagesbewegung -2,36 %** — Sektor-Rotation raus aus XLV, Watch Midday
- **GOOGL**  356,805 $ (Entry 368,10, P/L -3,07 %, chg_today -0,58 %) — **engste Position**
  - V1 338,65 SICHER (+5,08 % Puffer, Fill-Day+3 Verengung von +5,97 % Do-Close → +5,08 % jetzt)
  - V2 328,36 SICHER (+8,67 %)
  - RS_4w vs SPY -2,32 % negativ verstärkt sich — Watch Midday

**V1-V6-Check Open: ALLE 4 POSITIONEN SICHER. Keine Sell-Order platziert. Pending Orders bleiben 0.**

**Kauf-Scan: SKIPPED — Käufe KW28 2/2 LOCK aktiv bis Mo 13.07.**
- Guardrail-Prüfung: Daily -0,32 % GRÜN, Weekly -0,75 % GRÜN, VIX ~16 GRÜN, Crash-Filter INAKTIV, Drawdown -1,39 % GRÜN, Cash 69,55 % GRÜN
- **ABER Slot-Lock:** Käufe pro Woche max 2 → 2/2 erreicht → Kauf-Scan-Schritt 3–5 der Routine übersprungen (regelkonform)
- Watchlist AAPL/NVDA/CAT/AMZN carry-over, KW29-Prep unverändert (siehe Pre-Market)

**Schlechteste Position:** GOOGL -3,07 % (Fill-Day+3 Verengung V1-Puffer +5,08 %, weiter engste; RS-Divergenz zu XLC)
**Beste Position:** UNH +6,48 % (leichter Rückgang -0,95 % vom neuen Posit-Hoch, aber V2-Trail 381,89 hält)

**Sektor-Kontext heute (Pre-Market Sicht + Live-Check):** VXX -2,72 % → Vola weiter entspannt, SPY marginal +0,19 %. Bot underperformt SPY um -0,51 % durch LLY-Schwäche (XLV Sektor-Weakness setzt sich fort) und GOOGL-Fill-Day-Drift. XLK-Rally von Do ohne Bot-Exposure setzt sich strukturell fort → AAPL/NVDA-KW29-Prep validiert.

**Daily Loss Cap (-3 %):** -0,320 % → GRÜN.
**Weekly Loss Cap (-5 %):** -0,749 % → GRÜN.
**ATH-Drawdown (-15 %):** -1,390 % → GRÜN.
**Käufe KW28:** 2/2 → **KEIN Kauf möglich bis Mo 13.07.**

**⚠ JPM V1-Blackout AKTIV:** V1 316,14 (-5 % vom Entry, statt -8 %) — Live 337,75 → +6,84 % Puffer SICHER. Bleibt aktiv bis Q2-Earnings 14.07.2026 BMO.

**Datenqualitäts-Hinweise:**
- Alpaca `equity` = 98.675,68 (Live 09:37); `last_equity` = 99.060,07 (After-Hours-Tick vom Do). Für Daily-P/L Memory-Ground-Truth Do-Close 98.992,13 verwendet (Konvention: Bot-Memory schlägt Alpaca-Overnight-Mark).
- SPY-Alpaca-IEX Live 752,955 vs Do-Close 751,55 = +0,187 % (Ground-Truth).
- Alle 4 Position-Quotes aus /v2/positions (current_price) + /v2/stocks/trades/latest (Cross-Check).
- Keine Perplexity-Query im Open-Scan nötig (Käufe-Slot LOCK → kein Sektor/Kandidaten-Scan).

**ClickUp:** ITEM_246 Tier-Limit weiter carry-over aus Pre-Market → Push-Notification als Fallback.

> **Entscheidung Market Open 09:37 ET:** No-Op — alle V1-V6 SICHER, keine Sell-Order platziert. Kauf-Scan SKIPPED wegen Slot-LOCK 2/2. Daily -0,32 % marginal negativ, Alpha -0,51 % durch LLY -2,36 % und GOOGL -0,58 %. Guardrails alle GRÜN.
> **Zwingender Watch bis Midday:** (1) JPM Live-Watch bei 316,14 (Blackout-V1, Puffer +6,84 %), (2) GOOGL V1-Puffer +5,08 % (weiter engste, Fill-Day+3), (3) LLY Tages-Schwäche -2,36 % — sollte sich stabilisieren, V1 +8,18 % Puffer noch reichlich.
> **Nächste Routine:** Fr 10.07. 13:00 ET Midday Stop-Check.

---

## Market Close 2026-07-09 16:02 ET (Do, KW28 Tag 4) — Tagesbilanz, JPM V1-Tightening AKTIVIERT

```
Alpaca clock:      is_open=false | next_open Fr 10.07. 09:30 ET | next_close 16:00 ET
Gesamtwert:        98.992,13 $   (Alpaca equity Close, vs last_equity 98.969,42 = Mi EOD-Mark)
Cash:              68.626,60 $   (69,33 %, unverändert)
Investiert (MV):   30.365,53 $   (30,67 %, JPM 1.005,39 + UNH 10.338,00 + LLY 9.735,60 + GOOGL 9.286,54)
P/L heute:            +22,71 $   (+0,023 %)  [GRÜN — leichter Rebound]
SPY-Tag:           +0,841 %       (Alpaca IEX 745,28 → 751,55)  [Perplexity nannte +0,54 %/749,74 — Alpaca als Ground-Truth]
Alpha vs SPY:      -0,818 %       [NEGATIV — XLV -0,10 % flat trotz UNH +1,42 %, XLK +2,16 % Rally ohne Bot-Exposure]
ATH:              100.066,47 $    DD -1,074 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,431 %        (KW28 Mo-Basis 99.420,34 = Fr-Close 03.07.) [GRÜN — weit unter -5 %]
Käufe KW28:            2/2        (LOCK bis Mo 13.07.)
Pending Orders:        0          (V5/V6 alle SICHER — keine Limit-Order für Fr 10.07.)
VIX-Ref:            ~17           (VXX -1,82 % → Vola-Entspannung post-FOMC)
Guardrails:  Daily +0,02 % | Weekly -0,43 % | DD -1,07 % | VIX ~17 | Käufe 2/2 (LOCK) → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca IEX 16:02 ET Close, Bars-Recalc EMA/RSI 205d):**
- **JPM**  335,415 $ (Entry 332,78, P/L +0,79 %, change_today +1,36 %) — XLF-Rebound +1,03 %
  - **V1 NEU 316,14** (ex-Blackout -5 %-Regel AKTIVIERT ab HEUTE CLOSE, alt 306,16 -8 %) SICHER (+6,10 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+11,03 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 ~317,29 > EMA200 ~306,70 ✓ (Spread +10,59 stabil)
  - V6 RSI(14) ~61 / RS_4w vs SPY +5,44 % → SICHER (RSI <80, RS positiv)
  - **⚠ JPM Earnings 14.07.2026 BMO (3 HT) → Blackout 3 HT AKTIV bis Earnings → V1 -5 % Tightening greift**
- **UNH**  431,655 $ (Entry 401,57, P/L +7,49 %, change_today +1,42 %) — **XLV -0,10 % flat, aber UNH Sektor-Winner** (Tageshoch 434,19 = NEUES Posit-Hoch)
  - V1 369,44 SICHER (+16,84 % Puffer)
  - V2 Stop **NEU 381,89** (Trail: NEUES Posit-Hoch 434,19 × 0,88; alt 378,54 vom 08.07.-Live-Hoch 430,155) SICHER (+13,03 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 ~391,13 > EMA200 ~337,50 ✓ (Spread +53,63 sehr komfortabel)
  - V6 RSI(14) ~67 / RS_4w vs SPY +4,42 % → SICHER
- **LLY**  1.215,62 $ (Entry 1.193,89, P/L +1,82 %, change_today +0,09 %) — XLV flat, LLY neutral
  - V1 1.098,38 SICHER (+10,67 % Puffer)
  - V2 Stop 1.098,70 (Posit-Hoch 1.248,53 carry-over 07.07., kein neues Hoch heute — Tageshoch 1.228,81) SICHER (+10,64 %)
  - V3 1.432,66 / V4 1.611,75 — nicht erreicht
  - V5 EMA50 ~1.102,43 > EMA200 ~991,69 ✓ (Spread +110,74 komfortabel)
  - V6 RSI(14) ~64 / RS_4w vs SPY +4,05 % → SICHER
- **GOOGL**  358,88 $ (Entry 368,10, P/L -2,51 %, change_today -0,86 %) — XLC +0,97 % positiv, ABER GOOGL divergiert (Fill-Day+2 Konsolidierung fortgesetzt, Tagestief 351,105)
  - V1 338,65 SICHER (+5,97 % Puffer, weiter engste Position aber SICHER)
  - V2 Stop 328,36 (Posit-Hoch 373,14 carry-over 07.07., kein neues Hoch heute) SICHER (+9,29 %)
  - V3 441,72 / V4 496,93 — nicht erreicht
  - V5 EMA50 ~359,32 > EMA200 ~317,58 ✓ (Spread +41,74)
  - V6 RSI(14) ~48 / RS_4w vs SPY -2,32 % → NICHT ausgelöst (V6 verlangt BEIDES RSI>80 UND RS<0; RSI weit unter 80)

**V5/V6-Check heute: ALLE 4 POSITIONEN SICHER.** → **Keine Limit-Order für Fr 10.07. vorbereitet.** Pending Orders bleiben 0.

**Schlechteste Position:** GOOGL -2,51 % (Fill-Day+2 setzt Konsolidierung fort trotz XLC-Support, V1-Puffer +5,97 % weiter engste aber sicher; RS_4w -2,32 % negativ verstärkt sich)
**Beste Position:** UNH +7,49 % (change_today +1,42 %, NEUES Posit-Hoch 434,19 → V2-Trail 381,89)

**Sektor-Update:** JPM XLF 1,02 % + UNH XLV 10,44 % + LLY XLV 9,83 % + GOOGL XLC 9,38 % = **30,67 % investiert**. XLV Total 20,27 % (unter 30 %-Cap ✓, 2/3 XLV). 4/8 Positions-Slots belegt.

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLK +2,16 % | XLY +1,35 % | XLF +1,03 % | XLC +0,97 % | XLI +0,39 % | XLB +0,20 % | XLRE +0,17 %
XLV -0,10 % | XLU -0,55 % | XLP -1,42 % | XLE -1,44 %
VXX -1,82 % (Vola-Entspannung post-FOMC, VIX ~17 GRÜN)
```
→ **Klare Rotation ZURÜCK in Tech/Growth: XLK/XLY/XLF/XLC alle grün, XLV flat.** Bot-Positionen: UNH+LLY XLV -0,10 % Sektor-Support fehlt aber UNH +1,42 % einzelwert-stark; JPM XLF +1,03 % Rebound-Tag; GOOGL XLC +0,97 % Sektor grün ABER GOOGL -0,86 % individuell-schwach (Divergenz). **XLK +2,16 % ohne Bot-Exposure → Alpha-Miss -0,818 % strukturell (AAPL/NVDA-KW29-Prep validiert).**

**Daily Loss Cap (-3 %):** +0,023 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,431 % → GRÜN, keine Stornierungen.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -1,074 % → GRÜN.
**Käufe KW28:** 2/2 → **KEIN weiterer Kauf möglich bis Mo 13.07.** (KW28 Slot-Lock).

**⚠ JPM V1-Stop-Tightening AB JETZT AKTIVIERT:**
- Regel: Earnings-Blackout 3 HT vor Earnings → V1 auf -5 % vom Entry
- Berechnung: 332,78 × 0,95 = **316,14 $** (NEU)
- Alt: 332,78 × 0,92 = 306,16 $ (auslaufend)
- Aktueller Kurs 335,415 → Puffer neu +6,10 % (statt +9,66 % alt)
- Gilt bis Q2-Earnings 14.07.2026 BMO (Mo 13.07. Kauf + Di 14.07. Blackout-Ende)
- **Fr 10.07. Pre-Market ZWINGEND: Bei JPM < 316,14 → sofort V1-Market-Sell**

**Watchlist Fr 10.07. + KW29-Prep (Alpaca K1-K3 carry-over Mi 08.07. Close, SPY_RS_63d +13,84 %):**
```
Sym    Last      Ranking KW29                                    Kommentar
AAPL   ~318     LEAD — 3/3 K1-K3 (RS +10,33 %, RSI 62,81)       XLK +2,16 % heute massiv → Momentum-Restore validiert; K5-Recheck KW29 zwingend
NVDA   ~212     NEU 2. XLK-Kandidat — 3/3 grenzwertig RS         XLK-Rebound +2,16 % → beste Sektor-Bestätigung
CAT    ~948     Backup — 2/3 K2-Fail RSI 48,93                   K3 stärkstes RS +17,69 %; KW29-Recheck (RSI-Erholung möglich)
AMZN   ~244     Backup — 2/3 K2-Fail                             K1-Spread eng; XLY +1,35 % heute positiv
```
→ **AAPL LEAD gestärkt** durch XLK-Rally +2,16 % (Sektor-Timing perfekt für Mo 13.07. Kauf)
→ **NVDA neu 2. XLK-Kandidat** — starke Sektor-Bestätigung
→ CAT/AMZN bleiben Backup

**Datenqualitäts-Hinweise:**
- Alpaca IEX-Bars 205d verfügbar für alle 4 Positionen — EMA50/200 + RSI(14) Wilder inkrementell berechnet aus Vortag
- SPY IEX 751,55 vs 745,28 (Mi-Close) = +0,841 % als Ground-Truth für Alpha (Perplexity nannte 749,74/+0,54 % — moderate Diskrepanz)
- Sektor-ETF-Marks über Alpaca IEX (12/12 erfolgreich)
- Perplexity Watchlist-News-Query lieferte SPY-Daten mit Diskrepanz — Watchlist carry-over von Mi-Close-Screener

**ClickUp:** [CLOSE] Tagesbilanz Task angelegt Prio 3 (Portfolio-Performance leicht positiv ABER Alpha stark negativ -0,818 % → Priorität Normal).

> **Entscheidung Market Close:** Portfolio +0,023 % marginal positiv, aber deutliches Alpha-Miss -0,818 % durch XLK-Rally +2,16 % ohne Bot-Exposure. UNH neues Posit-Hoch 434,19 → V2-Trail 381,89 (+0,89 % Anhebung). GOOGL Fill-Day+2 Divergenz zu XLC (Sektor +0,97 %, GOOGL -0,86 %) verschärft sich — Watch KW29. Alle V1-V6 SICHER → keine Limit-Order für Fr 10.07. **KW28 Käufe 2/2 voll — bis Mo 13.07. KEIN weiterer Kauf.** **JPM V1-Stop-Tightening auf 316,14 (-5 %) AKTIVIERT** (Blackout 3 HT bis Q2 14.07. BMO).
> **Zwingender Watch morgen:** JPM Pre-Market bei < 316,14 → sofort V1-Market-Sell (Puffer heute +6,10 %).
> **Lessons-Tag:** (1) XLK-Rally +2,16 % ohne Bot-Exposure = -0,818 % Alpha-Miss → AAPL/NVDA-KW29-Prep-Ranking validiert (Sektor-Rotation zurück ins Growth deutlich vor KW29-Kauf-Fenster). (2) GOOGL divergiert zu XLC: Sektor +0,97 %, GOOGL -0,86 % → Fill-Day+2 zeigt jetzt AVGO/MU-Muster in abgeschwächter Form, RS_4w -2,32 % negativ verstärkt sich. (3) UNH einzelwert-stark ohne Sektor-Support (XLV -0,10 % flat) → Alpha innerhalb Sektor stark, aber Portfolio-Alpha durch XLV-Overweight belastet.
> **Nächste Routine:** Fr 10.07. 08:30 ET Pre-Market Check (KW28 Tag 5, JPM-V1-Watch bei 316,14, Rebound-Prüfung GOOGL).

---

## Midday 2026-07-09 13:07 ET (Do, KW28 Tag 4) — Stop-Check, alle SICHER

```
Alpaca clock:      is_open=true | next_close 09.07. 16:00 ET
Positionen:        4/8 (JPM/UNH/LLY/GOOGL)
Ø P/L (einfach):   +1,42 % (JPM +0,88 % / UNH +7,12 % / LLY +1,14 % / GOOGL -3,44 %)
Schlechteste:      GOOGL -3,44 % (V1-Puffer +4,95 % — engste Position, verengt vs Open +5,85 %, aber SICHER)
Beste:             UNH +7,12 % (V1-Puffer +16,43 %, marginal NEUES Posit-Hoch 430,155)
Stops:             alle regulär — kein V1/V2/V3/V4-Trigger
Daily P/L:           -108,97 $   (-0,110 %)  [GRÜN — vs last_equity 98.969,42 = Mi EOD-Mark]
Equity:            98.860,45 $   (Cash 68.626,60 / MV 30.232,44)
Buying_power:     359.161,18 $
Weekly KW28 P/L:  -0,563 %        (Mo-Basis 99.420,34 = Fr-Close) [GRÜN]
DD vs ATH:        -1,205 %        (ATH 100.066,47) [GRÜN]
```

**Live-Check V1–V4 (Alpaca IEX 13:07 ET):**
- **JPM**  335,725 $ (Entry 332,78, P/L +0,88 %, MV 1.007,18)
  - V1 306,16 SICHER (+9,66 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+11,13 %)
  - V3 399,34 / V4 449,25 — weit entfernt
  - **JPM Earnings 14.07.2026 BMO CONFIRMED → 3-HT-Blackout aktiviert AB HEUTE CLOSE → V1-Stop-Tightening auf -5 % (316,14) ZWINGEND zur Close-Routine 16:00 ET**
- **UNH**  430,155 $ (Entry 401,57, P/L +7,12 %, MV 10.323,72)
  - V1 369,44 SICHER (+16,43 % Puffer)
  - V2 Stop **NEU 378,54** (Trail: NEUES Posit-Hoch 430,155 × 0,88; alt 378,48 vom 02.07.-Hoch 430,095) SICHER (+13,64 %)
  - V3 481,88 / V4 542,12 — weit entfernt
- **LLY**  1.207,545 $ (Entry 1.193,89, P/L +1,14 %, MV 9.660,36)
  - V1 1.098,38 SICHER (+9,94 % Puffer)
  - V2 Stop 1.098,70 (Posit-Hoch 1.248,53 carry-over 07.07., kein neues Hoch) SICHER (+9,91 %)
  - V3 1.432,66 / V4 1.611,75 — weit entfernt
- **GOOGL**  355,43 $ (Entry 368,10, P/L -3,44 %, MV 9.241,18) — Fill-Day+2 Verengung fortgesetzt (Open -2,61 % → Midday -3,44 %)
  - V1 338,65 SICHER (+4,95 % Puffer, weiter engste Position aber SICHER)
  - V2 Stop 328,36 (Posit-Hoch 373,14 carry-over 07.07.) SICHER (+8,24 %)
  - V3 441,72 / V4 496,93 — weit entfernt

→ **Keine Verkaufsorder.** Alle V1–V4 regulär SICHER — Puffer +4,95 % (GOOGL) bis +16,43 % (UNH).
→ **Daily Loss Cap (-3 %) nicht erreicht** (-0,110 %). Keine Order-Stornierung nötig (keine Pending-Orders).

**Guardrails-Status:**
```
1. Daily Loss Cap (-3 %):    -0,110 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):   -0,563 % (KW28 Mo-Basis 99.420,34)    [GRÜN]
3. Drawdown-Alarm (-15 %):   -1,205 % vs ATH 100.066,47            [GRÜN]
4. Käufe KW28:                2/2 (LOCK bis Mo 13.07.)             [KEIN weiterer Kauf KW28]
```

**ClickUp:** kein Alert (keine Stops, kein Cap → Logging-Disziplin gewahrt).

> **Entscheidung:** No-Op — alle 4 Positionen halten. GOOGL Fill-Day+2 verengt sich weiter (-3,44 %), V1-Puffer +4,95 % engste Position aber sicher; V2-Trail 328,36 komfortabel. UNH marginal NEUES Posit-Hoch 430,155 → V2-Trail +0,06 auf 378,54. JPM/LLY stabil. Daily -0,11 % vs Mi-EOD-Mark GRÜN.
> **Nächste Routine:** Do 09.07. 16:00 ET Market Close (Tagesbilanz + V5/V6-Check aller 4 Positionen + **JPM-Blackout-Aktivierung V1-Tightening auf 316,14 ZWINGEND** + Limit-Order für Fr 10.07. falls V5/V6-Trigger).

---

## Market Open 2026-07-09 09:37 ET (Do, KW28 Tag 4) — No-Op (Slot LOCK), alle V1 SICHER

```
Alpaca clock:      is_open=true | next_close 09.07. 16:00 ET
Equity:            98.999,05 $   (Alpaca Live 09:37 ET, vs last_equity 98.969,42 = Mi EOD-Mark)
Cash:              68.626,60 $   (69,32 %, unverändert)
Portfolio MV:      30.372,45 $   (30,68 %)
Buying_power:     359.549,25 $
Daily P/L:            +29,63 $   (+0,030 %)  [GRÜN — leichter Rebound nach Mi post-FOMC-Rutsch]
ATH:              100.066,47 $    DD -1,067 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,423 %        (KW28 Mo-Basis 99.420,34 = Fr-Close)
Käufe KW28:            2/2        LOCK bis Mo 13.07.
Pending Orders:        0
Guardrails:  Daily +0,03 % | Weekly -0,42 % | DD -1,07 % | Käufe 2/2 LOCK → ALLE 8 GRÜN
```

**Positionen Live V1 (Alpaca 09:37 ET, change_today = vs Mi-Close):**
- **JPM**   331,935 $ (Entry 332,78, P/L -0,25 %, change_today +0,40 %) — leichte Erholung nach Mi -2,59 %
  - V1 306,16 SICHER (+8,42 % Puffer)
  - **JPM Earnings 14.07.2026 BMO CONFIRMED → 3-HT-Blackout aktiviert AB HEUTE CLOSE → V1-Stop-Tightening auf -5 % (316,14) ZWINGEND zur Close-Routine**
- **UNH**   426,27 $ (Entry 401,57, P/L +6,15 %, change_today +0,16 %) — XLV stabil
  - V1 369,44 SICHER (+15,35 % Puffer)
- **LLY**  1.228,405 $ (Entry 1.193,89, P/L +2,89 %, change_today +1,03 %) — Rebound-Signal
  - V1 1.098,38 SICHER (+11,83 % Puffer)
  - V2 Trail 1.098,70 (carry-over Posit-Hoch 1.248,53 vom 07.07.)
- **GOOGL** 358,4775 $ (Entry 368,10, P/L -2,61 %, change_today -0,95 %) — Fill-Day+2 Konsolidierung fortgesetzt
  - V1 338,65 SICHER (+5,85 % Puffer, weiter engste Position aber SICHER)
  - V2 Trail 328,36 (carry-over Posit-Hoch 373,14)

→ **Alle 4 V1 SICHER, kein Verkaufssignal, keine Order-Aktivität.**

**Kauf-Scan:** KEIN Scan durchgeführt (Käufe-Slot KW28 LOCK 2/2 bis Mo 13.07.).

**Sektor-Update:** JPM XLF 1,01 % + UNH XLV 10,33 % + LLY XLV 9,93 % + GOOGL XLC 9,41 % = **30,68 %** investiert. XLV Total 20,26 % (unter 30 %-Cap ✓). 4/8 Positions-Slots belegt.

**Guardrail-Status:** Alle GRÜN. Daily +0,03 % positiv (leichte Erholung vs Mi post-FOMC). Weekly -0,42 % weit unter -5 %-Cap.

**Entscheidung Market Open:**
- KEIN Kauf-Scan (Slot LOCK 2/2)
- Alle 4 Positionen SICHER → keine V1/V2/V3/V4-Order
- No-Op-Routine wie erwartet
- JPM-Blackout aktiviert sich erst ab HEUTE CLOSE → V1-Tightening zur Close-Routine 16:00 ET

**Watchlist KW29-Prep (Kauf-Fenster ab Mo 13.07.):**
1. **AAPL** LEAD — 3/3 K1-K3 aus 08.07. Close (RS +10,33 %, RSI 62,81); XLK-Sektor-Support; K5-Recheck KW29 zwingend
2. **NVDA** neu 2. XLK-Kandidat — 3/3 K1-K3 grenzwertig RS +1,37 %; K5-FwdPE-Recheck erforderlich
3. **CAT** Backup — 2/3 K2-Fail RSI cool-off, K3 stärkstes RS +17,69 %; KW29-Recheck
4. **AMZN** Backup — 2/3 K2-Fail, K1-Spread eng

**Nächste Routine:** Do 09.07. 13:00 ET Midday Stop-Check (V1-V4-Watch aller 4 Positionen; keine Kauf-Aktivität möglich).

**ClickUp:** [ROUTINE] Market Open Log-Task Prio 4 (Low, No-Op, Slot LOCK).

---

## Market Close 2026-07-08 16:02 ET (Mi, KW28 Tag 3) — Tagesbilanz post-FOMC

```
Alpaca clock:      is_open=false | next_open Do 09.07. 09:30 ET | next_close 16:00 ET
Gesamtwert:        98.970,99 $   (Alpaca equity Close, vs last_equity 99.348,08 = Di EOD-Mark)
Cash:              68.626,60 $   (69,34 %, unverändert)
Investiert (MV):   30.344,39 $   (30,66 %, JPM 991,35 + UNH 10.214,40 + LLY 9.726,64 + GOOGL 9.412,00)
P/L heute:            -377,09 $   (-0,380 %)  [GRÜN — Post-FOMC-Risk-Off, Alpha marginal]
SPY-Tag:           -0,333 %       (Alpaca IEX 747,77 → 745,28)
Alpha vs SPY:      -0,047 %       [~FLAT — FOMC-Minutes 14:00 ET Vola-Spike; alle 4 Positionen change_today negativ]
ATH:              100.066,47 $    DD -1,095 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,452 %        (KW28 Mo-Basis 99.420,34 = Fr-Close) [GRÜN — weit unter -5 %]
Käufe KW28:            2/2        (LOCK bis Mo 13.07.)
Pending Orders:        0          (V5/V6 alle SICHER — keine Limit-Order für Do 09.07.)
VIX-Ref:            ~18-19         (VXX +1,57 % → Vola-Tick nach FOMC-Minutes, weiter GRÜN)
Guardrails:  Daily -0,38 % | Weekly -0,45 % | DD -1,10 % | VIX ~18 | Käufe 2/2 (LOCK) → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 16:02 ET Close + Bars-Recalc EMA/RSI 204d IEX):**
- **JPM**  330,45 $ (Entry 332,78, P/L -0,70 %, change_today -2,59 %) — XLF-Rutsch -1,91 % / weakster im Portfolio
  - V1 306,16 SICHER (+7,94 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+9,38 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 316,57 > EMA200 306,41 ✓ (Spread +10,16 stabil)
  - V6 RSI(14) 56,99 / RS_4w vs SPY +5,64 % → SICHER (RSI <80, RS positiv)
  - **⚠ JPM Earnings 14.07.2026 BMO CONFIRMED → 3-HT-Blackout AKTIV ab MORGEN 09.07. Close → V1-Tightening auf -5 % (neu 316,14) zwingend**
- **UNH**  425,60 $ (Entry 401,57, P/L +5,98 %, change_today -0,61 %) — XLV -1,34 % mild absorbiert
  - V1 369,44 SICHER (+15,23 % Puffer)
  - V2 Stop 378,48 (Posit-Hoch 430,095 carry-over 02.07., kein neues Hoch heute) SICHER (+12,45 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 389,48 > EMA200 336,55 ✓ (Spread +52,93 sehr komfortabel)
  - V6 RSI(14) 62,23 / RS_4w vs SPY +4,18 % → SICHER
- **LLY**  1.215,83 $ (Entry 1.193,89, P/L +1,84 %, change_today -1,60 %) — XLV -1,34 % moderat
  - V1 1.098,38 SICHER (+10,69 % Puffer)
  - V2 Stop 1.098,70 (Posit-Hoch 1.248,53 carry-over 07.07., kein neues Hoch heute) SICHER (+10,66 %)
  - V3 1.432,66 / V4 1.611,75 — nicht erreicht
  - V5 EMA50 1.097,80 > EMA200 989,44 ✓ (Spread +108,36 komfortabel)
  - V6 RSI(14) 64,28 / RS_4w vs SPY +4,70 % → SICHER (RSI <80, RS positiv)
- **GOOGL**  362,00 $ (Entry 368,10, P/L -1,66 %, change_today -1,37 %) — XLC -1,41 %, Fill-Day+1-Konsolidierung fortgesetzt
  - V1 338,65 SICHER (+6,45 % Puffer, weiter engste Position aber SICHER)
  - V2 Stop 328,36 (Posit-Hoch 373,14 carry-over 07.07., kein neues Hoch heute) SICHER (+9,29 %)
  - V3 441,72 / V4 496,93 — nicht erreicht
  - V5 EMA50 359,31 > EMA200 317,16 ✓ (Spread +42,15)
  - V6 RSI(14) 50,29 / RS_4w vs SPY -1,54 % → NICHT ausgelöst (V6 verlangt BEIDES RSI>80 UND RS<0; RSI 50,29 weit unter 80)

**V5/V6-Check heute: ALLE 4 POSITIONEN SICHER.** → **Keine Limit-Order für Do 09.07. vorbereitet.** Pending Orders bleiben 0.

**Schlechteste Position:** GOOGL -1,66 % (Fill-Day+1 setzt Konsolidierung fort, V1-Puffer +6,45 % weiter engste aber sicher)
**Beste Position:** UNH +5,98 % (V1-Puffer +15,23 %)

**Sektor-Update:** JPM XLF 1,00 % + UNH XLV 10,32 % + LLY XLV 9,83 % + GOOGL XLC 9,51 % = **30,66 % investiert**. XLV Total 20,15 % (unter 30 %-Cap ✓, 2/3 XLV). 4/8 Positions-Slots belegt.

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLE +1,70 % | XLK +1,22 %
XLP -0,51 % | XLU -0,74 % | XLI -1,09 % | XLV -1,34 % | XLC -1,41 % | XLRE -1,68 % | XLY -1,77 % | XLF -1,91 % | XLB -2,58 %
VXX +1,57 % (Vola-Tick post-FOMC, VIX ~18-19 GRÜN)
```
→ **Klare Sektor-Divergenz post-FOMC: nur XLE + XLK grün, alles andere rot.** Bot-Positionen: JPM XLF -1,91 % größter Sektor-Verlierer → JPM change_today -2,59 % erklärbar; UNH+LLY XLV -1,34 % moderat; GOOGL XLC -1,41 %. **XLK +1,22 % Rebound signalisiert AAPL/NVDA-Momentum für KW29-Prep.**

**Daily Loss Cap (-3 %):** -0,380 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,452 % → GRÜN, keine Stornierungen.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -1,095 % → GRÜN.
**Käufe KW28:** 2/2 → **KEIN weiterer Kauf möglich bis Mo 13.07.** (KW28 Slot-Lock).

**Watchlist Do 09.07. + KW29-Prep (Alpaca K1-K3 Live 08.07. Close, SPY_RS_63d +13,34 %):**
```
Sym    Last      K1 EMA50>200          K2 RSI     K3 RS_63d vs SPY   Kommentar
AAPL   313,33   ✓ 292,89>271,56       ✓ 62,81    ✓ +10,33 %          3/3 STARK — XLK +1,22 % Tages-Support, K5-Recheck KW29 zwingend
NVDA   204,07   ✓ 203,47>191,00       ✓ 51,02    ✓ +1,37 %           3/3 grenzwertig-RS — XLK +1,22 % Support, K5-Recheck
CAT    947,62   ✓ 916,49>702,87       ✗ 48,93    ✓ +17,69 %          2/3 K2-Fail (RSI cool-off < 50), K3 stärkstes RS im Feld — KW29-Recheck
AMZN   243,60   ✓ 245,37>233,35       ✗ 49,50    ✓ +0,59 %           2/3 K2-Fail, K1-Spread eng — Watchlist-Backup
```
→ **AAPL LEAD für KW29 Mo 13.07.** (3/3 K1-K3, XLK-Sektor-Support, XLK-Konflikt obsolet nach MU-Sell 07.07.)
→ **NVDA neu auf Watchlist** (3/3 K1-K3, XLK-Sektor, K5-FwdPE-Recheck erforderlich)
→ **CAT Backup** (RSI 48,93 zu weit unter 50-Fenster gerutscht → K2 knapp verfehlt; K3 +17,69 % weiterhin stärkstes RS im Feld)
→ **AMZN neu als Backup** (2/3, K1-Spread eng, K5 offen)

**Datenqualitäts-Hinweise:**
- Alpaca IEX-Bars 204d verfügbar für alle 4 Positionen — EMA50/200 + RSI(14) Wilder live berechnet
- SPY IEX 745,28 vs 747,77 (Di-Close) = -0,333 % als Ground-Truth für Alpha
- Sektor-ETF-Marks über Alpaca IEX Fallback (Perplexity date-in-future Bug carry-over)
- Perplexity Watchlist-Scan lieferte keinen Value → Alpaca K1-K3 Screener für Kandidatenrunde ausgeführt

**ClickUp:** [CLOSE] Tagesbilanz Task angelegt Prio 3 (leicht negative Portfolio-Performance UND leicht negatives Alpha → Priorität Normal).

> **Entscheidung Market Close:** Portfolio -0,380 % post-FOMC-Minutes-Risk-Off, aber Alpha nahezu flat (-0,047 %) → keine Sektor-Rotation gegen Bot. Alle V1–V6 SICHER — keine Limit-Order für Do 09.07. Größter Verlierer JPM (XLF -1,91 %); GOOGL setzt Fill-Day-Konsolidierung fort. **KW28 Käufe 2/2 voll — bis Mo 13.07. KEIN weiterer Kauf.** Watchlist erweitert: AAPL LEAD + NVDA neu (beide 3/3 K1-K3, XLK +1,22 % Sektor-Support), CAT rutscht auf 2/3 (RSI cool-off), AMZN Backup.
> **Zwingender Watch morgen:** JPM Blackout-Aktivierung ab 09.07. Close → V1-Stop-Tightening auf -5 % (316,14 statt 306,16); ab Pre-Market 08:30 ET prüfen ob Situation heute schon vorbereitet werden kann.
> **Lessons-Tag:** (1) FOMC-Minutes 14:00 ET erzeugten klare Sektor-Divergenz: nur XLE/XLK grün — Bot-Portfolio 3 von 4 in negativen Sektoren (XLF/XLV/XLC), Alpha bleibt aber flat weil Bot-Selektion innerhalb der Sektoren defensiv (UNH+LLY XLV moderater Rückgang vs Sektor-Durchschnitt -1,34 %). (2) GOOGL Fill-Day+1 (-1,66 % kumuliert) folgt jetzt doch dem AVGO/MU-Fill-Day-Muster in abgeschwächter Form. (3) AAPL-Momentum-Restore nach XLK-Rebound heute macht KW29-LEAD-Position vor CAT möglich; NVDA neu als 2. XLK-Kandidat.
> **Nächste Routine:** Do 09.07. 08:30 ET Pre-Market Check (KW28 Tag 4, JPM-Stop-Tightening-Vorbereitung Close).

---

## Midday 2026-07-08 13:07 ET (Mi, KW28 Tag 3) — Stop-Check pre-FOMC

```
Alpaca clock:      is_open=true | next_close 08.07. 16:00 ET
Positionen:        4/8 (JPM/UNH/LLY/GOOGL)
Ø P/L (einfach):   +1,95 % (JPM +0,31 % / UNH +6,71 % / LLY +2,68 % / GOOGL -1,90 %)
Schlechteste:      GOOGL -1,90 % (V1-Puffer +6,63 % — engste Position aber SICHER)
Beste:             UNH +6,71 % (V1-Puffer +15,99 %)
Stops:             alle regulär — kein V1/V2/V3/V4-Trigger
Daily P/L:            -238,56 $   (-0,240 %)  [GRÜN — vs last_equity 99.348,08 = Di EOD-Mark]
Equity:            99.109,52 $   (Cash 68.626,60 / MV 30.482,92)
Buying_power:     359.858,56 $
Weekly KW28 P/L:  -0,313 %        (Mo-Basis 99.420,34 = Fr-Close) [GRÜN]
DD vs ATH:        -0,956 %        (ATH 100.066,47) [GRÜN]
```

**Live-Check V1–V4 (Alpaca IEX 13:07 ET):**
- **JPM**  333,815 $ (Entry 332,78, P/L +0,31 %, MV 1.001,45)
  - V1 306,16 SICHER (+9,03 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+10,49 %)
  - V3 399,34 / V4 449,25 — weit entfernt
  - **JPM Earnings 14.07.2026 BMO CONFIRMED → 3-HT-Blackout ab Do 09.07. Close (ab MORGEN Stop-Tightening V1 → -5 %)**
- **UNH**  428,5148 $ (Entry 401,57, P/L +6,71 %, MV 10.284,36)
  - V1 369,44 SICHER (+15,99 % Puffer)
  - V2 Stop 378,48 (Posit-Hoch 430,095 carry-over 02.07.) SICHER (+13,22 %)
  - V3 481,88 / V4 542,12 — weit entfernt
- **LLY**  1.225,835 $ (Entry 1.193,89, P/L +2,68 %, MV 9.806,68)
  - V1 1.098,38 SICHER (+11,60 % Puffer)
  - V2 Stop 1.098,70 (Posit-Hoch 1.248,53 carry-over 07.07.) SICHER (+11,57 %)
  - V3 1.432,66 / V4 1.611,75 — weit entfernt
- **GOOGL**  361,10 $ (Entry 368,10, P/L -1,90 %, MV 9.388,60) — Fill-Day+1 Verengung
  - V1 338,65 SICHER (+6,63 % Puffer, engste Position aber SICHER)
  - V2 Stop 328,36 (Posit-Hoch 373,14 carry-over 07.07.) SICHER (+9,97 %)
  - V3 441,72 / V4 496,93 — weit entfernt

→ **Keine Verkaufsorder.** Alle 4 V1–V4 regulär SICHER — Puffer +6,63 % (GOOGL) bis +15,99 % (UNH).
→ **Daily Loss Cap (-3 %) nicht erreicht** (-0,240 %). Keine Order-Stornierung nötig (keine Pending-Orders).

**Guardrails-Status:**
```
1. Daily Loss Cap (-3 %):    -0,240 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):   -0,313 % (KW28 Mo-Basis 99.420,34)    [GRÜN]
3. Drawdown-Alarm (-15 %):   -0,956 % vs ATH 100.066,47            [GRÜN]
4. Käufe KW28:                2/2 (LOCK bis Mo 13.07.)             [KEIN weiterer Kauf KW28]
```

**ClickUp:** kein Alert (keine Stops, kein Cap → Logging-Disziplin gewahrt).

> **Entscheidung:** No-Op — alle 4 Positionen halten pre-FOMC-Minutes (14:00 ET). GOOGL Fill-Day+1 setzt Konsolidierung fort (-1,90 %), V1-Puffer +6,63 % weiter engste aber sicher; V2-Trail 328,36 komfortabel. UNH/LLY tragen Portfolio (+6,71 %/+2,68 %). Daily -0,24 % vs Di-EOD-Mark stabil.
> **Nächste Routine:** Mi 08.07. 16:00 ET Market Close (Tagesbilanz + V5/V6-Check aller 4 Positionen + Limit-Order für Do 09.07. falls V5/V6-Trigger + JPM-Blackout-Vorbereitung).

---

## Market Open 2026-07-08 09:37 ET (Mi, KW28 Tag 3) — No-Op (Slot LOCK), alle V1 SICHER

```
Alpaca clock:      is_open=true | next_close 08.07. 16:00 ET
Equity:            99.080,45 $   (Alpaca Live 09:37 ET, vs last_equity 99.348,08 = Di EOD-Mark)
Cash:              68.626,60 $   (69,26 %, unverändert)
Portfolio MV:      30.453,85 $   (30,74 %)
Buying_power:     359.777,18 $
Daily P/L:            -267,63 $   (-0,269 %)  [GRÜN — vs Di-Close]
ATH:              100.066,47 $    DD -0,985 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,342 %        (KW28 Mo-Basis 99.420,34 = Fr-Close)
Käufe KW28:            2/2        LOCK bis Mo 13.07.
Pending Orders:        0
VIX proxy VXX:     22,07          (Di ~21,6, +2 % — leichter Vola-Tick, VIX geschätzt ~18-19)
SPY Live 09:37:    743,35 $       (-0,591 % vs Di-Close 747,77 → risk-off Open)
Crash-Filter:      INAKTIV        (SPY -0,591 %, weit von -5 %-Schwelle)
Guardrails:  Daily -0,27 % | Weekly -0,34 % | DD -0,99 % | VIX ~18 | Käufe 2/2 LOCK → ALLE 8 GRÜN
```

**Positionen Live V1-V6 (Alpaca 09:37 ET):**
- **JPM**   335,03 $ (Entry 332,78, P/L +0,68 %, change_today -1,235 %) — XLF weak Open
  - V1 306,16 SICHER (+9,42 % Puffer)
  - **JPM Earnings 14.07.2026 BMO CONFIRMED → 3-HT-Blackout ab Do 09.07. Close (ab MORGEN Stop-Tightening V1 → -5 %)**
- **UNH**   425,99 $ (Entry 401,57, P/L +6,08 %, change_today -0,514 %) — XLV leicht rot
  - V1 369,44 SICHER (+15,31 % Puffer)
- **LLY**  1.217,03 $ (Entry 1.193,89, P/L +1,94 %, change_today -1,50 %) — XLV weak, aber komfortabel
  - V1 1.098,38 SICHER (+10,83 % Puffer)
  - V2 Trail 1.098,70 (carry Posit-Hoch 1.248,53 vom 07.07.)
- **GOOGL** 364,58 $ (Entry 368,10, P/L -0,96 %, change_today -0,668 %) — Fill-Day+1 Konsolidierung
  - V1 338,65 SICHER (+7,65 % Puffer, weiter engste Position aber SICHER)
  - V2 Trail 328,36 (carry Posit-Hoch 373,14)

→ **Alle 4 V1-V6 SICHER, kein Verkaufssignal, keine Order-Aktivität.**

**Kauf-Scan:** KEIN Scan durchgeführt (Käufe-Slot KW28 LOCK 2/2 bis Mo 13.07.).

**Sektor-Update:** JPM XLF 1,01 % + UNH XLV 10,32 % + LLY XLV 9,82 % + GOOGL XLC 9,57 % = **30,74 %** investiert. XLV Total 20,14 % (unter 30 %-Cap ✓). 4/8 Positions-Slots belegt.

**Guardrail-Status:** Alle GRÜN. Daily -0,27 % weit unter -3 %-Cap. Weekly -0,34 % weit unter -5 %-Cap.

**Entscheidung Market Open:**
- KEIN Kauf-Scan (Slot LOCK 2/2)
- Alle 4 Positionen SICHER → keine V1/V2/V3/V4-Order
- No-Op-Routine wie erwartet

**Watchlist KW29-Prep (Kauf-Fenster ab Mo 13.07.):**
1. **CAT** LEAD — K5 RevGrowth-Recheck zwingend KW29 (Q1 -1 % carry); XLI leer
2. **AAPL** Backup — K5-Recheck; XLK-Konflikt obsolet nach MU-Sell

**FOMC-Minutes heute 14:00 ET → möglicher intraday-Vola-Spike; Midday 13:00 ET vor Release, Close nach Release.**

**Nächste Routine:** Mi 08.07. 13:00 ET Midday Stop-Check (VOR FOMC-Minutes 14:00 ET; V1-V4-Watch aller 4 Positionen).

**ClickUp:** [ROUTINE] Market Open Log-Task Prio 4 (Low, No-Op, Slot LOCK).

---

## Pre-Market 2026-07-08 08:35 ET (Mi, KW28 Tag 3) — Guardrails GRÜN, KEIN Kauf-Scan (Slot LOCK)

```
Alpaca clock:      is_open=false | next_open Mi 08.07. 09:30 ET | next_close 16:00 ET
Equity:            99.236,19 $   (Alpaca Pre-Market Live, vs last_equity 99.348,08 = Di EOD-Mark)
Cash:              68.626,60 $   (69,15 %, unverändert)
Portfolio MV:      30.609,59 $   (30,85 %)
Buying_power:     360.213,25 $
Daily P/L:            -111,89 $   (-0,113 %)  [GRÜN]
ATH:              100.066,47 $    DD -0,835 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,185 %        (KW28 Mo-Basis 99.420,34 = Fr-Close)
Käufe KW28:            2/2        LOCK bis Mo 13.07.
Pending Orders:        0
VIX:               ~16-19 Live    (Di Close 16,13; CBOE-Snippet 08.07. ~18,82 → +16,68 % Sprung)
SPY Pre-Market:    -0,527 %       (Alpaca IEX mid 743,83 vs Di-Close 747,77)
10Y Treasury:      N/A            (Perplexity indirekt)
Guardrails:  Daily -0,11 % | Weekly -0,19 % | DD -0,84 % | VIX ~18 | Käufe 2/2 LOCK → ALLE 8 GRÜN
```

**Positionen Pre-Market (Alpaca Quotes 08:35 ET):**
- **JPM**   336,73 $ (Entry 332,78, P/L +1,19 %, change_today -0,73 %) — XLF-Cool-off
  - V1 306,16 SICHER (+9,98 % Puffer)
- **UNH**   427,85 $ (Entry 401,57, P/L +6,54 %, change_today -0,08 %) — XLV stabil nach Rebound
  - V1 369,44 SICHER (+15,81 %)
- **LLY**  1.235,00 $ (Entry 1.193,89, P/L +3,44 %, change_today -0,05 %) — Konsolidierung
  - V1 1.098,38 SICHER (+12,44 %)
  - V2 Trail 1.098,70 (carry-over Posit-Hoch 1.248,53 vom 07.07.)
- **GOOGL** 363,50 $ (Entry 368,10, P/L -1,25 %, change_today -0,96 %) — Fill-Day+1 Verengung
  - V1 338,65 SICHER (+7,33 % Puffer, engste Position aber SICHER)
  - V2 Trail 328,36 (carry-over Posit-Hoch 373,14)

→ **Alle 4 V1-V6 SICHER, keine Verkaufsentscheidung, keine Order-Aktivität.**

**Earnings-Blackout-Check:**
- JPM Q2 **14.07.2026 BMO CONFIRMED** (WallStreetHorizon + MarketBeat + JPM IR) → 4 HT bis Earnings
  - 3-HT-Blackout aktiv ab **09.07. Close (Do)** → JETZT NOCH NICHT AKTIV
  - **Zwingender Watch morgen:** JPM-Stop-Tightening V1 → -5 % ab Do 09.07. Close
- UNH ~16.07. carry-over unbestätigt / LLY 05.08. (20 HT) / GOOGL 22.07. (10 HT) — alle sicher

**Guardrail-Status:** Alle GRÜN. Käufe-Slot LOCK bis Mo 13.07. (KW29-Start).

**Entscheidung Market Open:**
- KEIN Kauf-Scan (Slot LOCK 2/2)
- Nur V1-V6-Watch aller 4 Positionen + Guardrail-Monitoring
- FOMC-Minutes heute 14:00 ET → möglicher intraday-Vola-Spike; Midday 13:00 ET vor Release, Close nach Release

**Watchlist KW29-Prep (Kauf-Fenster ab Mo 13.07.):**
1. **CAT** LEAD — K5 RevGrowth-Recheck zwingend KW29 (Q1 -1 % carry); XLI leer trotz -1,68 % Sektor-Rutsch 07.07.
2. **AAPL** Backup — K5-Recheck; XLK-Konflikt obsolet nach MU-Sell; XLK -2,38 % Timing-Watch
3. MS AUSGESCHIEDEN (Earnings-Blackout aktiv ab 10.07. → Kauf 13.07. unmöglich)

**Nächste Routine:** Mi 08.07. 13:00 ET Midday Stop-Check (VOR FOMC-Minutes 14:00 ET; V1-V4-Watch aller 4 Positionen).

**ClickUp:** Task 869e1zgmh angelegt Prio 4 (Low, No-Op-Routine, Log-Disziplin gewahrt).

---

## Market Close 2026-07-07 16:02 ET (Di, KW28) — Tagesbilanz

```
Alpaca clock:      is_open=false | next_open Mi 08.07. 09:30 ET | next_close 16:00 ET
Gesamtwert:        99.334,61 $   (Alpaca equity Close, vs last_equity 99.385,29 = Mo EOD-Mark)
Cash:              68.626,62 $   (69,09 %, unverändert nach GOOGL-Fill 07.07. AM)
Investiert (MV):   30.707,99 $   (30,91 %, JPM 1.015,35 + UNH 10.276,56 + LLY 9.884,48 + GOOGL 9.531,60)
P/L heute:            -50,68 $   (-0,051 %)  [GRÜN — Alpha positiv trotz kleinem Portfolio-Rückgang]
SPY-Tag:           -0,466 %       (Alpaca IEX 751,27 → 747,77)
Alpha vs SPY:      +0,415 %       [POSITIV — XLV-Rebound +1,51 % trägt UNH+LLY]
ATH:              100.066,47 $    DD -0,732 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,086 %        (KW28 Mo-Basis 99.420,34 = Fr-Close) [GRÜN]
Käufe KW28:            2/2        (LLY 06.07. + GOOGL 07.07. — Kauf-Slots VOLL bis Mo 13.07.)
Pending Orders:        0          (keine V5/V6-Order — alle Positionen SICHER)
VIX-Ref:            ~15-16        (VXX +0,84 % → leichter Vola-Tick, weiter GRÜN)
Guardrails:  Daily -0,05 % | Weekly -0,09 % | DD -0,73 % | VIX ~16 | Käufe 2/2 (LOCK) → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 16:02 ET Close + Bars-Recalc EMA/RSI 203d IEX):**
- **JPM**  338,45 $ (Entry 332,78, P/L +1,70 %, change_today +0,22 %) — XLF-flat-Tag (-0,20 %)
  - V1 306,16 SICHER (+10,55 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+12,03 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 316,00 > EMA200 306,99 ✓ (Spread +9,01)
  - V6 RSI(14) 67,16 / RS_4w vs SPY +7,33 % → SICHER (RSI <80, RS positiv)
- **UNH**  428,19 $ (Entry 401,57, P/L +6,63 %, change_today +2,44 %) — **XLV-Rebound-Gewinner** (+1,51 % Sektor)
  - V1 369,44 SICHER (+15,90 % Puffer)
  - V2 Stop 378,48 (Posit-Hoch 430,095 carry-over 02.07., Tageshoch heute 428,49 KEIN neues Hoch) SICHER (+13,12 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 388,00 > EMA200 346,19 ✓ (Spread +41,81 sehr komfortabel)
  - V6 RSI(14) 64,18 / RS_4w vs SPY +6,07 % → SICHER
- **LLY**  1.235,56 $ (Entry 1.193,89, P/L +3,49 %, change_today +2,96 %) — **NEUES Posit-Hoch 1.248,53 intraday** (Tageshoch-Bar)
  - V1 1.098,38 SICHER (+12,49 % Puffer)
  - V2 Stop **NEU 1.098,70** (Trail: Tageshoch 1.248,525 × 0,88; alt 1.083,27 vom Midday-Live-Hoch 1.230,99) SICHER (+11,08 %)
  - V3 1.432,66 / V4 1.611,75 — nicht erreicht
  - V5 EMA50 1.093,03 > EMA200 983,35 ✓ (Spread +109,68 komfortabel)
  - V6 RSI(14) 69,15 / RS_4w vs SPY +7,38 % → SICHER (RSI <80, RS positiv)
- **GOOGL**  366,60 $ (Entry 368,10, P/L -0,41 %, change_today +0,04 %) — Post-Fill Konsolidierung (Tageshoch 373,14 nach Fill)
  - V1 338,65 SICHER (+8,25 % Puffer)
  - V2 Stop **NEU 328,36** (Trail: Tageshoch 373,14 × 0,88; alt 325,25 vom Live-Fill 369,60) SICHER (+10,43 %)
  - V3 441,72 / V4 496,93 — nicht erreicht
  - V5 EMA50 359,23 > EMA200 323,95 ✓ (Spread +35,28)
  - V6 RSI(14) 53,98 / RS_4w vs SPY -2,14 % → NICHT ausgelöst (V6 verlangt BEIDES RSI>80 UND RS<0; RSI 53,98 weit unter 80)

**V5/V6-Check heute: ALLE 4 POSITIONEN SICHER.** → **Keine Limit-Order für Mi 08.07. vorbereitet.** Pending Orders bleiben 0.

**Schlechteste Position:** GOOGL -0,41 % (Fill-Day-Konsolidierung, V1-Puffer +8,25 %)
**Beste Position:** UNH +6,63 % (change_today +2,44 %, XLV-Sektor-Winner)

**Sektor-Update:** JPM XLF 1,02 % + UNH XLV 10,35 % + LLY XLV 9,95 % + GOOGL XLC 9,60 % = **30,91 % investiert**. XLV Total 20,30 % (unter 30 %-Cap ✓, 2/3 XLV). 4/8 Positions-Slots belegt.

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLE +2,84 % | XLV +1,51 % | XLRE +1,40 % | XLU +0,92 % | XLP +0,89 % | XLC +0,73 %
XLF -0,20 % | XLY -0,49 % | XLB -0,87 % | XLI -1,68 % | XLK -2,38 %
VXX +0,84 % (Vola leicht steigend, weiter unter 25)
```
→ **Rotation ins Defensives (XLV/XLU/XLP/XLE alle grün, XLK/XLI unter Druck).** Bot-Positionen profitieren: UNH+LLY XLV +1,51 % (beste Sektor-Winner nach XLE), GOOGL XLC +0,73 % (leichter Support), JPM XLF -0,20 % (marginal weak). **MU-Sell gestern (V1 924,45 $) rechtzeitig — MU-XLK -2,38 % Sektor-Rutsch heute wäre auf offene Position schmerzhaft gewesen.**

**Daily Loss Cap (-3 %):** -0,051 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,086 % → GRÜN, keine Stornierungen.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -0,732 % → GRÜN.
**Käufe KW28:** 2/2 → **KEIN weiterer Kauf möglich bis Mo 13.07.** (KW28 Slot-Lock).

**Watchlist Mi 08.07. (Kauf-Slots VOLL, Prep für KW29 Mo 13.07.):**
```
Sym    Live       K1-K3 carry-over Mo 06.07.       Kommentar
CAT    ~955      ✓✓✓ (RS +20,55 %, RSI 51,65)     XLI leer — Sektor-Rally MU/AVGO-Slot; K5 RevGrowth Q1 -1 % Recheck KW29
MS     ~222     ✓✓✓ (RS +19,81 %, RSI 60,39)     Earnings 15.07. → 3-HT-Blackout ab Fr 10.07. Close = Kauf KW29 Mo NICHT MEHR MÖGLICH (Blackout aktiv)
AAPL   ~309     ✓✓✓ (RS +7,47 %, RSI 63,16)      K5-Recheck; XLK-Konflikt jetzt obsolet nach MU-Sell
```
→ **MS wird durch Blackout ausscheiden** (Blackout aktiv ab 10.07. Close, Kauf Mo 13.07. nicht möglich, Timing verpasst)
→ **CAT/AAPL bleiben Kandidaten für KW29 Mo 13.07.** — beide K5-Recheck erforderlich

**Datenqualitäts-Hinweise:**
- Alpaca IEX-Bars 203d verfügbar für alle 4 Positionen — EMA50/200 + RSI(14) live berechnet
- SPY IEX 747,77 als Ground-Truth für Alpha-Rechnung (Perplexity SPY-Query Datum-in-Zukunft-Bug carry-over)
- Sektor-ETF-Marks über Alpaca IEX Fallback (Perplexity leer)
- Alpaca last_equity 99.385,29 (Mo EOD After-Hours-Mark) weicht +137 $ vom Memory Mo Close 99.248,28 ab — Alpaca als Ground-Truth für Daily-P/L verwendet

**ClickUp:** [CLOSE] Tagesbilanz Task angelegt Prio 4 (leicht negative Portfolio-Performance ABER Alpha positiv → Priorität abgestuft). Push-Notification an Owner (ITEM_246 Tier-Limit carry-over, Payload mit `custom_item_id: null`).

> **Entscheidung Market Close:** Portfolio bleibt stabil bei -0,051 % nach XLV-Rebound-Tag. Alpha +0,415 % kompensiert Alpha-Miss -1,034 % von Mo (XLV-Overweight zahlt sich heute aus). Alle V1–V6 SICHER — keine Limit-Order für Mi 08.07. LLY neues Posit-Hoch 1.248,53 hebt V2-Trail auf 1.098,70. GOOGL-Fill-Day-Konsolidierung mild (-0,41 %) — kein Fill-Day-Drop-Muster wie AVGO/MU. **KW28 Käufe 2/2 voll — bis Mo 13.07. KEIN weiterer Kauf.** Watchlist reduziert sich auf CAT/AAPL für KW29-Start (MS scheidet durch Earnings-Blackout aus).
> **Lessons-Tag:** (1) GOOGL-Fill-Day mit +0,04 % change_today unterbricht das AVGO/MU-Fill-Day-Drop-Muster — moderate XLC-Sektor-Stärke +0,73 % ermöglicht sanfte Einordnung. (2) MU-V1-Sell gestern zum optimalen Zeitpunkt: XLK -2,38 % heute wäre auf 9 Sh MU zusätzlicher Verlust ~-215 $ gewesen (V1-Auslösung sparte diesen Rutsch). (3) XLV-Overweight zahlt heute Alpha +0,415 % nach gestern -1,034 %: Sektor-Rotationen nivellieren sich in KW28 (Netto-Alpha KW28 Mo-Di ~-0,62 %).
> **Nächste Routine:** Mi 08.07. 08:30 ET Pre-Market Check (KW28 Tag 3, alle Positionen V1-V6 SICHER, KEIN Kauf-Scan mangels Käufe-Slot, nur Guardrail-Monitoring).

---

## Midday 2026-07-07 13:06 ET (Di, KW28) — Stop-Check + GOOGL FILL bestätigt

```
Alpaca clock:      is_open=true | next_close 07.07. 16:00 ET
Positionen:        4/8 (JPM/UNH/LLY/GOOGL)
Ø P/L (einfach):   +2,76 % (JPM +1,36 % / UNH +6,15 % / LLY +3,11 % / GOOGL +0,41 %)
Schlechteste:      GOOGL +0,41 % (V1-Puffer +8,44 % — Post-Fill Eintritt)
Beste:             UNH +6,15 % (V1-Puffer +15,36 %)
Stops:             alle regulär — kein V1/V2/V3/V4-Trigger
Daily P/L:            -94,27 $   (-0,095 %)  [GRÜN — vs last_equity 99.420,34]
Equity:            99.326,07 $   (Cash 68.626,63 / MV 30.699,44)
Buying_power:     360.464,95 $
```

**GOOGL Limit-Order gefüllt (zwischen 09:40 und 13:06 ET):**
- Order-ID: 69106496-90d4-46dc-a370-cafb7eb816ac (Limit 368,17 $ Day, Submit 09:40:46 ET)
- Fill: 26/26 Sh @ **368,098846 $ avg** (cost basis 9.570,57 $ = 9,64 % Portfolio)
- V1 = 338,65 $ (-8 %), V2 = 325,25 $ (-12 % vom Posit-Hoch = Live 369,60, Tracking ab Fill), V3 = 441,72 $ (+20 %), V4 = 496,93 $ (+35 %)
- Post-Fill Live 369,60 $ (P/L +0,41 %, change_today +0,86 %) → V1-Puffer +8,44 %

**Live-Check V1–V4 (Alpaca 13:06 ET):**
- **JPM**  337,32 $ (Entry 332,78, P/L +1,36 %, change_today -0,11 %) — leichter XLF-Cool-off
  - V1 306,16 SICHER (+10,19 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+11,66 %)
  - V3 399,34 / V4 449,25 — weit entfernt, kein TP-Trigger
- **UNH**  426,285 $ (Entry 401,57, P/L +6,15 %, change_today +1,98 %) — XLV-Rebound bestätigt
  - V1 369,44 SICHER (+15,36 % Puffer)
  - V2 Stop 378,48 (Posit-Hoch 430,095 carry-over 02.07., kein neues Hoch heute) SICHER (+12,63 %)
  - V3 481,88 / V4 542,12 — weit entfernt
- **LLY**  1.230,99 $ (Entry 1.193,89, P/L +3,11 %, change_today +2,58 %) — **NEUES Posit-Hoch heute (Live > Fill 1.193,89)**
  - V1 1.098,38 SICHER (+12,07 % Puffer)
  - V2 Stop **NEU 1.083,27** (Trail: 1.230,99 * 0,88; alt 1.050,62 vom Fill-Posit-Hoch) SICHER (+13,63 %)
  - V3 1.432,66 / V4 1.611,75 — weit entfernt
- **GOOGL**  369,60 $ (Entry 368,10, P/L +0,41 %, change_today +0,86 %) — Post-Fill stabil
  - V1 338,65 SICHER (+8,44 % Puffer)
  - V2 Stop 325,25 (Posit-Hoch = Live 369,60 Tracking ab Fill) SICHER (+11,99 %)
  - V3 441,72 / V4 496,93 — weit entfernt

→ **Keine Verkaufsorder.** Alle V1–V4 SICHER — alle Puffer ≥ +8,4 %.
→ **Daily Loss Cap (-3 %) nicht erreicht** (-0,095 %). Keine Order-Stornierung nötig (keine offenen Limit-Orders).

**Sektor-Update:** JPM XLF 1,02 % + UNH XLV 10,30 % + LLY XLV 9,92 % + GOOGL XLC 9,68 % = **30,91 % investiert**. XLV Total 20,22 % (unter 30 %-Cap ✓, 2/3 XLV). 4/8 Positions-Slots belegt.

**Guardrails-Status:**
```
1. Daily Loss Cap (-3 %):    -0,095 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):   -0,095 % (KW28 Mo-Basis 99.420,34)    [GRÜN]
3. Drawdown-Alarm (-15 %):   -0,741 % vs ATH 100.066,47            [GRÜN]
4. Käufe KW28:                2/2 (LLY + GOOGL, Wochen-Slots voll) [KEIN weiterer Kauf KW28]
```

**ClickUp:** kein Alert (keine Stops, kein Cap → Logging-Disziplin gewahrt).

> **Entscheidung:** No-Op — alle 4 Positionen halten. GOOGL-Fill schließt den 2/2-KW28-Kauf-Slot (kein weiterer Kauf bis Mo 13.07.). Portfolio-Struktur nach MU-Rotation zu GOOGL: XLC-Diversifikation erreicht, XLV weiter unter 30 %-Cap. Ø P/L +2,76 % zeigt schnelle Erholung nach MU-V1-Sell (Realverlust -1.019,43 $). LLY neues Posit-Hoch 1.230,99 hebt V2-Trail auf 1.083,27 (+2,63 % Fortschritt).
> **Nächste Routine:** Di 07.07. 16:00 ET Market Close (Tagesbilanz + V5/V6-Check aller 4 Positionen + Limit-Order für Mi 08.07. falls V5/V6-Trigger).

---

## Market Open 2026-07-07 09:40 ET (Di, KW28) — MU V1 exec + GOOGL Buy pending

```
Alpaca clock:      is_open=true | next_close 07.07. 16:00 ET
Equity:            99.266,85 $   (nach MU-Sell Fill, vs last_equity 99.420,34)
Cash:              78.197,20 $   (78,78 %, +8.320,05 $ aus MU-Erlös)
Portfolio MV:      21.069,65 $   (21,22 %, JPM 1.022,43 + UNH 10.192,56 + LLY 9.858,24 — MU verkauft)
Buying_power:     361.664,03 $
Daily P/L:            -153,49 $   (-0,154 %)  [GRÜN — verbessert vs Pre-Market -0,206 %]
ATH:              100.066,47 $    DD -0,799 % [GRÜN]
Käufe KW28:            1/2        (LLY gefilled 06.07.; 1 Slot frei — GOOGL-Buy pending)
Pending Orders:        1         (GOOGL Limit-Buy 26 Sh @ 368,17 Day)
VIX:               ~16           [GRÜN → 10 % Sizing]
SPY Live 09:37:    749,76 $      (-0,20 % vs Mo Close 751,27 → risk-off Open)
Crash-Filter:       INAKTIV      (SPY -0,20 %)
Guardrails:  Daily -0,15 % | Weekly -0,15 % | DD -0,80 % | VIX ~16 | Käufe 1/2 → ALLE GRÜN
```

**Ausgeführte Trades diese Session:**
1. **MU V1 Stop-Loss Sell** — 9 Sh Market Sell @ 924,45 $ avg (Fill 09:37:42 ET, 3 sec) → Erlös 8.320,05 $ | Verlust **-1.019,43 $ (-10,92 %)** vs Entry 1.037,72 $
2. **GOOGL Limit-Buy pending** — 26 Sh @ 368,17 $ Day (Submit 09:40:46 ET, Live 369,42 $ > Limit → wartet auf Pullback)

**Positionen Live (Alpaca 09:40 ET):**
- **JPM**  340,81 $ (Entry 332,78, P/L +2,41 %, change_today +0,71 %) — XLF-Stärke fortgesetzt
  - V1 306,16 SICHER (+11,32 % Puffer)
- **UNH**  424,69 $ (Entry 401,57, P/L +5,76 %, change_today +1,63 %) — XLV-Erholung
  - V1 369,44 SICHER (+14,94 % Puffer)
- **LLY**  1.232,28 $ (Entry 1.193,89, P/L +3,22 %, change_today +2,25 %) — XLV-Rebound absorbiert
  - V1 1.098,38 SICHER (+12,20 % Puffer)

**Kauf-Scan GOOGL K1-K5 Live (Alpaca 09:40 ET):**
```
K1 EMA50 358,91 > EMA200 323,23      ✓ (Spread +35,68 — Golden Cross breit)
K2 RSI(14) 53,59                     ✓ (50-70 Fenster, Wilder-Smoothing)
K3 RS_63d GOOGL +23,97 % vs SPY +14,86% = +9,11 %  ✓
K4 Vol-Projektion ~176 % Avg20       ✓ (38.232 Sh in 8 min → ~2,15 M/Tag vs Avg20 1,22 M)
K5 carry FwdPE 21,87/28,65 ≤ 35      ✓ (Rev +11,33 %)
                                     → 5/5 grün → BUY
```

**Sektor-Update nach MU-Sell + GOOGL-Buy (bei Fill):**
- Aktuell: JPM XLF 1,03 % + UNH XLV 10,27 % + LLY XLV 9,93 % = **21,22 %** investiert
- Bei GOOGL-Fill: +XLC 9,64 % = **~30,9 %** investiert, 4/8 Positionen
- XLV Total 20,20 % (unter 30 %-Cap ✓, 2/3 XLV), XLC neu diversifiziert

**Watchlist Backup (falls GOOGL-Order nicht fillt bis Close):**
1. **CAT** 969,52 $ — K5 RevGrowth-Recheck ausstehend (Q1 -1 % carry)
2. **MS** 222,07 $ — Timing-Vorbehalt (Earnings 15.07. = Blackout ab Fr 10.07.)
3. **AAPL** 312,73 $ — Fallback (XLK-Konflikt jetzt obsolet nach MU-Sell, K5-Recheck)

**Guardrail-Status:** Alle GRÜN. MU-V1-Auslösung ordnungsgemäß nach Strategie ausgeführt.

**Nächste Routine:** Di 07.07. 13:00 ET Midday-Check (GOOGL-Fill-Status, V1-V4 aller Positionen).

---

## Pre-Market 2026-07-07 08:35 ET (Di, KW28) — MU-V1-Alarm Pre-Market

```
Alpaca clock:      is_open=false | next_open Di 07.07. 09:30 ET | next_close 16:00 ET
Equity:            99.215,80 $   (Alpaca Pre-Market Live, vs last_equity 99.420,34)
Cash:              69.877,15 $   (70,43 %, unverändert)
Portfolio MV:      29.338,65 $   (29,57 %)
Buying_power:     361.656,81 $
Daily P/L:            -204,54 $   (-0,206 %)  [GRÜN]
ATH:              100.066,47 $    DD -0,856 % [GRÜN]
Käufe KW28:            1/2        (LLY gefilled 06.07.; 1 Slot frei)
Pending Orders:        0
VIX:               ~15,9-16,0     (+2-3 % vs Vortag, Perplexity)
SPY Pre-Market:    ±0,3-0,6 %     (Futures moderat, Perplexity Inference)
10Y Treasury:      ~4,2-4,3 %     (Perplexity Inference)
Guardrails:  Daily -0,21 % | Weekly -0,21 % | DD -0,86 % | VIX ~16 | Käufe 1/2 → ALLE GRÜN
```

**Positionen Pre-Market (Alpaca Quotes 08:35 ET):**
- **JPM**  341,57 $ (Entry 332,78, P/L +2,64 %, change_today +1,14 %) — XLF Pre-Market-Stärke
  - V1 306,16 SICHER (+11,56 % Puffer)
- **UNH**  420,75 $ (Entry 401,57, P/L +4,78 %, change_today +0,66 %) — XLV Stabilisierung Pre-Market
  - V1 369,44 SICHER (+13,89 %)
- **MU**   936,39 $ (Entry 1037,72, P/L **-9,77 %**, change_today **-4,91 %**) — ⚠️ **UNTER V1-STOP 954,71 $**
  - V1 954,71 → **PRE-MARKET UNTERSCHRITTEN um -1,92 %**
  - Pre-Market-Ticks kein offizieller V1-Trigger (Strategy V1 = Regulär-Session-Kurs)
  - **09:30 ET Market Open: MU-Preis-Check zwingend erster Schritt** → falls Open < 954,71 $ → Market Sell 9 Shares SOFORT
- **LLY**  1.223,99 $ (Entry 1193,89, P/L +2,52 %, change_today +1,99 %) — XLV-Rebound
  - V1 1.098,38 SICHER (+11,44 %)

**Earnings-Blackout-Check:** Keine JPM/UNH/MU/LLY Earnings in 3 HT (Perplexity: S&P 500 Earnings-Welle startet Mitte Juli).

**Guardrail-Status:** Alle GRÜN. MU-V1-Alarm ist Position-spezifisch, kein Portfolio-Guardrail-Trigger (Daily -0,21 % weit unter -3 %-Cap).

**Watchlist Di 07.07. (carry-over aus Mo-Close, K1-K5 Live-Recheck bei Market Open):**
1. **GOOGL** LEAD — 5/5-Bild carry ✓ (K5 FwdPE 21,87/28,65, Rev +11,33 %); XLC-Sektor leer
2. **CAT** Backup — K5 RevGrowth Q1 -1 % Recheck-Priorität; XLI leer
3. **MS** Timing-Vorbehalt — 5/5 aber Earnings 15.07. = 3-HT-Blackout ab Fr 10.07.
4. **AAPL** Only-If — XLK-Konflikt MU (wird obsolet falls MU-V1 auslöst) + K5 offen

**Entscheidung Pre-Market:** 
- **Guardrails GRÜN** → Kauf-Scan bei Market Open grundsätzlich ERLAUBT
- **ABER:** MU-V1-Pre-Market-Situation ist ZUERST zu behandeln
- Market-Open-Scan priorisiert: (1) MU-V1-Auslösung bei Open handeln (2) DANACH Kauf-Scan bei GOOGL/CAT falls Portfolio bereinigt

**Nächste Routine:** Di 07.07. 09:30 ET Market Open — MU-V1-Trigger zuerst, dann Kauf-Scan.

---

---

## Market Close 2026-07-06 16:00 ET (Mo, KW28) — Tagesbilanz

```
Alpaca clock:      is_open=false | next_open Di 07.07. 09:30 ET | next_close Di 07.07. 16:00 ET
Gesamtwert:        99.248,28 $   (Alpaca equity Close, vs last_equity 99.420,34 = Fr-Close carry-over)
Cash:              69.877,15 $   (70,41 %, unverändert nach LLY-Fill 09:42 ET, keine weiteren Trades)
Investiert (MV):   29.371,13 $   (29,59 %, JPM 1.015,93 + UNH 10.017,06 + MU 8.714,70 + LLY 9.626,24)
P/L heute:            -172,06 $   (-0,173 %)  [GRÜN — vs last_equity 99.420,34]
SPY-Tag:           +0,861 %       (Alpaca IEX 744,86 → 751,27 Do 02.07.-Ref, Fr 03.07. Feiertag)
Alpha vs SPY:      -1,034 %       [NEGATIV — Rotation weg von XLV heute (UNH/LLY -1,88 %/-0,88 %)]
ATH:              100.066,47 $    DD -0,818 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW28:  -0,173 %        (KW28 Mo-Basis 99.420,34 = Fr-Close) [GRÜN]
Käufe KW28:            1/2        (LLY gefilled 09:42:49 ET; 1 Slot frei)
Pending Orders:        0          (keine V5/V6-Order — alle Positionen SICHER)
VIX-Ref:            ~15-16        (VXX -2,63 % → Vola-Entspannung setzt sich fort)
Guardrails:  Daily -0,17 % | Weekly -0,17 % | DD -0,82 % | VIX ~16 | Käufe 1/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 16:00 ET Close + Bars-Recalc EMA/RSI):**
- **JPM**  338,64 $ (Entry 332,78, P/L +1,76 %, change_today +1,25 %) — XLF-Rebound-Tag
  - V1 306,16 SICHER (+10,61 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+12,10 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 315,06 > EMA200 306,47 ✓ (Spread +8,59 stabil)
  - V6 RSI(14) 66,42 / RS_4w vs SPY +9,65 % → SICHER (RSI <80, RS positiv)
- **UNH**  417,38 $ (Entry 401,57, P/L +3,94 %, change_today -1,88 %) — XLV-Rotation-Verlierer
  - V1 369,44 SICHER (+12,97 % Puffer)
  - V2 Stop 378,48 (getrailt 02.07. auf Posit-Hoch 430,095, kein neues Hoch heute) SICHER (+10,27 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 386,36 > EMA200 337,83 ✓ (Spread +48,53 sehr komfortabel)
  - V6 RSI(14) 59,38 (Cooldown) / RS_4w +6,55 % → SICHER
- **MU**  968,30 $ (Entry 1037,72, P/L -6,69 %, change_today -0,74 %) — Rebound verpufft
  - V1 954,71 SICHER **nur +1,42 % Puffer** [KRITISCH — verengt gegenüber Midday +4,89 %]
  - V2 Stop 913,39 (Posit-Hoch 1037,94 = Fill-Preis carry-over) SICHER (+6,01 %)
  - V3 1245,26 / V4 1400,92 — weit entfernt
  - V5 EMA50 884,96 > EMA200 468,42 ✓ (Spread +416,54 — Golden Cross sehr breit)
  - V6 RSI(14) 48,91 / RS_4w -1,10 % → NICHT ausgelöst (V6 verlangt BEIDES: RSI>80 UND RS<0)
- **LLY**  1203,28 $ (Entry 1193,89 Fill 09:42:49 ET, P/L +0,79 %, change_today -0,88 %) — XLV weak-Tag absorbiert
  - V1 1098,38 SICHER (+9,55 % Puffer)
  - V2 Stop 1050,62 (Posit-Hoch = Fill 1193,89, kein neues Hoch heute) SICHER (+14,53 %)
  - V3 1432,66 / V4 1611,75 — weit entfernt
  - V5 EMA50 1087,20 > EMA200 982,73 ✓ (Spread +104,46 komfortabel)
  - V6 RSI(14) 64,70 / RS_4w +7,23 % → SICHER

**V5/V6-Check heute: ALLE 4 POSITIONEN SICHER.** → **Keine Limit-Order für morgen vorbereitet.** Pending Orders bleiben 0.
→ **MU-V1-Puffer bleibt kritisch eng (+1,42 %)** — Rebound-Momentum von Pre-Market verpuffte im Handelsverlauf. Break unter 954,71 morgen löst Market Sell sofort aus.

**Schlechteste Position:** MU -6,69 % (Fill-Day-Drop verstärkt sich, V1-Puffer nur noch +1,42 %)
**Beste Position:** UNH +3,94 % (trotz change_today -1,88 %; V2-Trail hält 378,48)

**Sektor-Update:** JPM XLF 1,02 % + UNH XLV 10,09 % + MU XLK 8,78 % + LLY XLV 9,70 % = 29,59 % investiert. XLV Total 19,79 % (unter 30 %-Cap ✓, 2/3 XLV-Positionen). 4/8 Positions-Slots belegt.

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLK +1,70 % | XLF +0,96 % | XLI +0,88 % | XLY +0,74 % | XLC +0,57 %
XLB -0,08 % | XLE -0,15 % | XLRE -0,92 % | XLU -1,02 % | XLV -1,04 % | XLP -1,07 %
VXX -2,63 % (Vola weiter abwärts)
```
→ Bot-Positionen: JPM (XLF +0,96 %) und MU (XLK +1,70 %) profitiert; UNH+LLY (XLV -1,04 %) belastet → Alpha -1,034 % erklärbar durch XLV-Rotation-Underperformance an einem Tag mit klarer Tech-Financials-Rotation.

**Daily Loss Cap (-3 %):** -0,173 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,173 % → GRÜN, keine Stornierungen.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -0,818 % → GRÜN.

**Watchlist Di 07.07. (Alpaca K1-K3 Recheck 06.07.-Close, SPY_RS_63d +14,86 %):**
```
Sym    Live       K1 EMA50>200      K2 RSI      K3 RS_63d vs SPY   Kommentar
GOOGL  366,34    ✓ 358,90>314,48   ✓ 53,59     ✓ RS +9,11 %      XLC leer, K5 carry ✓ (FwdPE 21,87/28,65 ≤35, Rev +11,33 %); Earnings 22.07. → 11 HT sicher
CAT    969,52    ✓ 914,19>701,19   ✓ 51,65     ✓ RS +20,55 %     XLI leer, RS 2. höchste; K5 RevGrowth Q1 -1 % Recheck; Earnings ~05.08.
MS     222,07    ✓ 205,22>178,34   ✓ 60,39     ✓ RS +19,81 %     XLF (JPM 1 % nur); K5 ✓ carry (FwdPE 21,58 / Rev +16,4 %); Earnings 15.07. → 3-HT-Blackout ab Fr 10.07. Close = **nur 3 HT frei** bei Kauf Di
AAPL   312,73    ✓ 291,29>270,14   ✓ 63,16     ✓ RS +7,47 %      XLK Konflikt MU; K5 offen
```

**Ranking Di 07.07.:**
1. **GOOGL** — LEAD (5/5-Bild ist stabil, XLC-Diversifikation, Earnings safe)
2. **CAT** — Backup (K5 RevGrowth-Recheck Di Pre-Market zwingend)
3. **MS** — Timing-Vorbehalt (nur 3 HT bis Blackout — Kauf-Entscheidung riskant)
4. **AAPL** — Nur bei GOOGL/CAT-Ausfall (Sektor-Konflikt + K5-Recheck)

**Weekly Loss Cap KW28-Check:** -0,173 % → GRÜN. Kein Kauf-Stopp. Käufe KW28 1/2 (1 Slot frei bis Fr).

**Datenqualitäts-Hinweise:**
- Alpaca IEX-Bars 211d verfügbar für alle 4 Positionen — EMA50/200 + RSI(14) live berechnet
- SPY IEX 751,27 als Ground-Truth für Alpha-Rechnung (Perplexity nannte +0,78 %, IEX +0,86 %)
- Perplexity Sektor-Daten heute leer (Datum-in-Zukunft-Bug carry-over) — Alpaca-Sektor-ETF-Marks als Fallback verwendet
- Alpaca Broker-Marks konsistent mit Positions-API

**ClickUp:** [CLOSE] Tagesbilanz Task angelegt Prio 3 (leicht negative Performance, Alpha negativ). Push-Notification an Owner primär (ITEM_246 Tier-Limit carry-over, Payload mit `custom_item_id: null`).

> **Entscheidung Market Close:** Portfolio stabil bei -0,173 % nach XLV-Rotations-Tag (UNH/LLY Belastung). Alle V1–V6 SICHER — keine Limit-Order für Di 07.07. **MU-V1-Puffer verengt sich auf +1,42 %** (vs Midday +4,89 %) — kritischer Übernacht-Watch, Pre-Market Di 08:30 ET zwingend. Alpha-Underperformance -1,03 % strukturell durch XLV-Rotation erklärbar (2/3 XLV-Positionen bei Sektor-Verlierer-Tag). Watchlist Di primär **GOOGL** (K5-carry ✓, Sektor XLC leer, Earnings safe), Backup CAT (K5-Recheck). Käufe KW28 1/2 → 1 Slot frei bis Fr.
> **Lessons-Tag:** (1) MU-Fill-Day-Drop-Muster fortgeführt: Rebound-Beginn Pre-Market +3,35 % verpuffte im Handelsverlauf → -0,74 % change_today, V1-Puffer verengt sich von +5,60 % auf +1,42 %. (2) LLY-Fill absorbierte XLV-Weak-Tag -1,04 % gut (P/L +0,79 %) durch Fill-Preis-Vorteil vs Do-Close-Ref-Preis. (3) SPY-Rally +0,86 % bei XLK/XLF-Rotation deckt Alpha-Underperformance mit XLV-Overweight auf — Diversifikations-Argument für GOOGL/CAT-Kauf morgen bestärkt.
> **Nächste Routine:** Di 07.07. 08:30 ET Pre-Market Check (KW28 Tag 2, MU-V1-Puffer +1,42 % kritisch beobachten, GOOGL/CAT Watchlist-Recheck).

---

## Midday 2026-07-06 13:06 ET (Mo, KW28) — Stop-Check

```
Alpaca clock:      is_open=true | next_close 06.07. 16:00 ET
Positionen:        4/8 (JPM/UNH/MU/LLY)
Ø P/L (gewichtet): +0,65 % (JPM +1,15 % / UNH +4,09 % / MU -3,50 % / LLY +1,19 %)
Schlechteste:      MU -3,50 % (V1-Puffer +4,89 % — entspannt vs Fr-Close +2,19 %)
Beste:             UNH +4,09 % (V1-Puffer +13,14 %)
Stops:             alle regulär — kein V1/V2/V3/V4-Trigger
Daily P/L:         +0,176 %   [GRÜN — vs last_equity 99.420,34]
Equity:            99.595,58 $ (long_market_value 29.718,43, cash 69.877,15)
```

**Live-Check V1–V4 (Alpaca 13:06 ET):**
- **JPM**  336,605 $ (Entry 332,78, P/L +1,15 %, change_today +0,64 %)
  - V1 306,16 SICHER (+9,94 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+11,42 %)
  - V3 399,34 / V4 449,25 — weit entfernt, kein TP-Trigger
- **UNH**  417,975 $ (Entry 401,57, P/L +4,09 %, change_today -1,74 %)
  - V1 369,44 SICHER (+13,14 % Puffer)
  - V2 Stop 378,48 (Posit-Hoch 430,095 carry-over 02.07.) SICHER (+10,44 %)
  - V3 481,88 / V4 542,12 — weit entfernt, kein TP-Trigger
- **MU**   1.001,425 $ (Entry 1.037,72, P/L -3,50 %, change_today +2,65 %) — **Rebound bestätigt weiter**
  - V1 954,71 SICHER **+4,89 % Puffer** [ENTSPANNT vs Fr-Close +2,19 % / Pre-Market +5,60 %]
  - V2 Stop 913,39 (Posit-Hoch 1.037,94 = Fill-Preis carry-over) SICHER (+9,63 %)
  - V3 1.245,26 / V4 1.400,92 — weit entfernt
- **LLY**  1.208,08 $ (Entry 1.193,8875 Fill 09:42:49 ET, P/L +1,19 %, change_today -0,48 %)
  - V1 1.098,38 SICHER (+9,99 % Puffer)
  - V2 Stop 1.050,62 (Posit-Hoch = Fill-Preis 1.193,89 — kein neues Hoch heute post-Fill notiert) SICHER (+14,99 %)
  - V3 1.432,66 / V4 1.611,75 — weit entfernt

→ **Keine Verkaufsorder.** Alle V1–V4 regulär SICHER, MU-V1-Puffer weitet sich nach Gap-Up-Bestätigung intraday auf +4,89 %.
→ **Daily Loss Cap (-3 %) nicht erreicht** (+0,176 %). Keine Order-Stornierung nötig (keine Pending-Orders).

**Sektor-Update:** JPM XLF 1,01 % + UNH XLV 10,07 % + MU XLK 9,05 % + LLY XLV 9,70 % = **29,84 % investiert**. XLV Total 19,77 % (unter 30 %-Cap ✓). Positionen 4/8.

**Guardrails-Status:**
```
1. Daily Loss Cap (-3 %):    +0,176 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):   +0,176 % (KW28 Mo-Basis 99.420,34)    [GRÜN]
3. Drawdown-Alarm (-15 %):   -0,472 % vs ATH 100.066,47            [GRÜN]
4. Käufe KW28:                1/2 (LLY gefillt, 1 Slot frei)       [GRÜN]
```

**ClickUp:** kein Alert (keine Stops, kein Cap → Logging-Disziplin gewahrt).

> **Entscheidung:** No-Op — alle 4 Positionen halten. Kein V1-V4-Trigger, alle Puffer komfortabel. MU-Rebound (+2,65 % change_today) bestätigt Pre-Market-Gap-Up und entspannt V1-Watch nachhaltig (Puffer +4,89 % vs Fr-Close-Notlage +2,19 %). LLY hält knapp über Fill mit +1,19 % nach schnellem Fill 09:42:49 ET. Daily-P/L +0,176 % vs breite Range, kein Guardrail-Stress.
> **Nächste Routine:** Mo 06.07. 16:00 ET Market Close (Tagesbilanz + V5/V6-Check aller 4 Positionen).

---

## Market Open KW28 — 2026-07-06 09:43 ET (Mo) — **LLY LIMIT-ORDER GEFILLT (5/5, K5 Multi-Source ✓)**

```
Alpaca clock:      is_open=true | next_close 06.07. 16:00 ET
Gesamtwert:        99.452,08 $   (Alpaca equity Post-Fill 09:43 ET, vs last_equity 99.420,34)
Cash:              69.877,15 $   (70,26 %)
Investiert (MV):   29.574,93 $   (29,74 %, JPM 1.016,31 + UNH 10.022,64 + MU 9.014,18 + LLY 9.521,28)
Daily P/L Live:    +0,032 %       [GRÜN]
Weekly P/L KW28:   +0,032 %       (KW28 Mo-Basis 99.420,34) [GRÜN]
ATH:              100.066,47 $    DD -0,614 % [GRÜN]
Käufe KW28:            1/2       (LLY FILLED — 1 Slot frei)
Pending Orders:        0         (LLY-Order 09:42:49 ET vollständig gefüllt 8/8 Sh @ 1.193,89)
VIX Spot Live:      ~16          [GRÜN → 10 % Sizing]
SPY Live 09:37:    748,11 $      (+0,55 % vs Do 02.07. Close 744,86 → risk-on Open)
Crash-Filter:       INAKTIV      (SPY +0,55 %)
Guardrails:  Daily +0,12 % | Weekly +0,12 % | DD -0,53 % | VIX ~16 | Käufe 1/2 → ALLE 8 GRÜN
```

**Positionen Live V1–V6 (Alpaca 09:37 ET):**
- **JPM**  338,05 $ (Entry 332,78, P/L +1,58 %, change_today +1,07 %)
  - V1 306,16 SICHER (+9,54 % Puffer)
  - V2 ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+10,68 %)
  - V5 EMA50 315,32 > EMA200 306,00 ✓ carry-over
  - V6 RSI 62,83 / RS +12,30 % → KEIN Trigger
- **UNH**  420,43 $ (Entry 401,57, P/L +4,69 %, change_today -1,16 %)
  - V1 369,44 SICHER (+13,80 % Puffer)
  - V2 378,48 (getrailt 02.07. auf Posit-Hoch 430,095) SICHER (+11,08 %)
  - V5 EMA50 385,12 > EMA200 342,87 ✓ carry-over
  - V6 RSI 64,76 / RS +13,97 % → KEIN Trigger
- **MU**  1.001,12 $ (Entry 1.037,72, P/L -3,53 %, change_today +2,62 %) — **Gap-Up bestätigt Rebound-Beginn**
  - V1 954,71 SICHER **+4,86 % Puffer** [ENTSPANNT vs Fr-Close +2,19 %]
  - V2 913,39 SICHER (+9,60 %)
  - V5 EMA50 882,15 > EMA200 507,23 ✓ carry-over
  - V6 RSI 48,57 / RS -8,42 % → KEIN Trigger

→ **Alle V1–V6 SICHER, keine Verkaufsorder pending.**

**Kandidaten-Scan K1–K5 (Alpaca IEX 200d Bars + Perplexity 06.07. K5):**
```
Sym    Live       K1 EMA50>200      K2 RSI  K3 RS_63d vs SPY (+14,07 %)  K4 Proj Vol   K5 Multi-Source
GOOGL  361,72    ✓ 358,17>316,50  ✓ 50,73  ✓ RS +8,24 %                ✓ 220 %       ✓ FwdPE 21,87/28,65 ≤35, Rev +11,33 %
LLY   1199,90    ✓ 1089,02>987,10 ✓ 64,34  ✓ RS +14,16 %               ✓ 242 %       ✓ FwdPE 34,51/32,69/32,53 ≤35, Rev +47,43 %
MS     219,62    ✓ 204,77>178,92  ✓ 58,26  ✓ RS +18,40 %               ✓ 150 %       ✓ carry-over aber Earnings 15.07. → Blackout ab 10.07. Close (4 HT frei)
CAT    984,00    ✓ 916,12>699,72  ✓ 53,30  ✓ RS +23,10 %               ✓ 371 %       ✗ RevGrowth Q1 -1 % carry-over (Recheck ausstehend)
AMD    540,73    ✓ 458,95>281,38  ✓ 55,73  ✓ RS +134,27 %              ✓ 533 %       ✗ FwdPE 35–95x carry-over (K5 struktur.) + XLK-Konflikt mit MU
AAPL   309,28    ✓ 291,14>271,07  ✓ 61,25  ✓ RS +6,80 %                ✓ 168 %       ? Recheck ausstehend + XLK-Konflikt mit MU
```

**Ranking-Entscheidung (Strategie: höchste RS + alle 5 Signale grün):**
1. AMD RS +134 % ✗ K5 → OUT
2. CAT RS +23 % ✗ K5 → OUT
3. MS RS +18 % (K5 ✓) — Earnings 15.07. Blackout ab 10.07. Close macht Position-Halt kritisch (4 HT bis Blackout) → **Downgrade Backup**
4. **LLY RS +14,16 %** — 5/5 grün, Earnings 05.08. sicher (22 HT Puffer) → **LEAD**
5. GOOGL RS +8,24 % — 5/5 grün, XLC-Diversifikation → **Backup**
6. AAPL RS +6,80 % — Recheck offen → OUT

**LLY-Order-Details (Alpaca):**
```
Order-ID:       f6364db0-8a8f-4a11-b305-26a4874f1f6d
Symbol:         LLY
Side:           BUY LIMIT | 8 Sh | Day
Limit-Preis:    1.216,84 $ (= round(1.210,79 * 1,005, 2))
Fill:           **09:42:49 ET** — 8/8 Shares @ avg **1.193,8875 $** (Fill-Zeit: 1min 49sec, sehr schnell vs MU 35min)
Investiert:     **9.551,10 $** (9,60 % Portfolio)
Post-Fill V1:   1.098,38 $ (-8 %)
Post-Fill V2:   1.050,62 $ (-12 %, Posit-Hoch = Fill)
Post-Fill V3:   1.432,66 $ (+20 %)
Post-Fill V4:   1.611,75 $ (+35 %)
Live 09:43:     1.190,16 $ (change_today -1,96 %, P/L -0,31 %) — V1-Puffer +8,35 %
```

**Sizing-Check:** portfolio_value 99.541,20 * 0,10 = 9.954,12 (VIX <25 → 10 %); shares = floor(9.954,12/1.199,90) = 8; limit = round(1.210,79*1,005, 2) = 1.216,84.

**Sektor-Check nach Fill:** JPM XLF 1,02 % + UNH XLV 10,08 % + LLY XLV 9,57 % + MU XLK 9,06 % → Total 29,74 % investiert; **XLV Total 19,65 %** (unter 30 %-Cap ✓, 2/3 XLV-Positionen ✓); Positionen 4/8, 4 Slots frei bis Fr.

**LLY Stop-Levels V1–V4 (Post-Fill, avg 1.193,89):**
- V1 = 1.098,38 $ (-8 % Standard-Stop-Loss)
- V2 = 1.050,62 $ (-12 % vom Posit-Hoch = Fill; Trailing ab neuem Hoch nach oben)
- V3 = 1.432,66 $ (+20 % → 50 % verkaufen)
- V4 = 1.611,75 $ (+35 % → Rest verkaufen)

**Earnings-Verifikation LLY (Perplexity 06.07. Multi-Source):**
- **Q2 2026: 05.08.2026 BMO** — 4-Source-Konsens: MarketBeat + LLY Investor-Relations Webcast + MarketChameleon + Nasdaq/Zacks (algo-derived) → 22 HT ab heute → 3-HT-Blackout aktiv ab **31.07. Close** → **JETZT NICHT AKTIV.**
- Weekly-Review-Prognose "~25.07." korrigiert nach unten (05.08. ist späteres = mehr Puffer).

**Datenqualitäts-Hinweise:**
- Perplexity Multi-Symbol-Query (LLY+GOOGL kombiniert) lieferte nur LLY-Daten, GOOGL-Query separat notwendig — Prompt-Split-Strategie funktioniert.
- LLY-FwdPE 34,51 (höchste Source) knapp unter 35 → K5 grün, aber grenzwertig — Recheck bei Weekly Review.
- Alle Alpaca-Marks konsistent mit Positions-API.

**ClickUp:** TRADE_BUY Alert Versuch (Prio 3) — Push-Notification an Owner + Memory-Log primär (ITEM_246 Tier-Limit carry-over, Payload mit `custom_item_id: null`).

> **Entscheidung Market Open:** LIMIT-ORDER LLY platziert. Erstes 5/5-K-Signal KW28. Multi-Source K5-Verifikation (FwdPE Median 32,7 ≤35 + RevGrowth 47,43 % ≥10 %) klar unter K5-Schwelle. Alle 4 K1-K4 Live bestätigt. LLY war 2. höchste RS nach AMD/CAT/MS-Ausschluss (K5-strukturell bzw. Earnings-Timing). Sektor XLV bleibt trotz UNH+LLY unter 30 %-Cap (19,92 %). Earnings-Blackout weit weg (05.08., 22 HT). MU-Position durch Gap-Up entlastet (V1-Puffer +4,86 %).
> **Lessons-Tag:** (1) GOOGL Weekly-Review-Lead-Ranking wurde durch K3-Ranking überstimmt — LLY mit K5-clean und höherer RS bekommt Vorzug, XLC-Diversifikations-Vorteil bleibt Backup-Argument. (2) FwdPE-Multi-Source-Median-Ansatz (statt Einzel-Source) hilft bei grenzwertigen K5-Kandidaten wie LLY 34,51 (nur 0,49 unter Schwelle).
> **Nächste Routine:** Mo 06.07. 13:00 ET Midday Stop-Check (LLY-Fill-Status + V1–V4 aller offenen Positionen).

---

## Pre-Market KW28 Start — 2026-07-06 08:35 ET (Mo)

```
Alpaca clock:      is_open=false | next_open Mo 06.07. 09:30 ET | next_close Mo 06.07. 16:00 ET
Gesamtwert:        99.682,06 $   (Alpaca equity Pre-Market, vs last_equity 99.420,34)
Cash:              79.428,25 $   (79,68 %, identisch zu Fr-Close)
Investiert (MV):   20.253,81 $   (20,32 %, JPM 999,36 + UNH 10.180,56 + MU 9.073,89)
Daily P/L Live:    +0,263 %       [GRÜN — vor Open, hauptsächlich MU-Gap-Up]
Weekly KW28-Basis: 99.420,34 $   (= Fr 03.07. Close, KW28 Reset)
Weekly P/L KW28:   0,000 %        [GRÜN]
ATH:              100.066,47 $    DD -0,384 % [GRÜN — Alarm -15 %]
Käufe KW28:            0/2       (Reset Mo)
Pending Orders:        0
VIX Spot Live:      15,81-16,32   (Multi-Source CBOE/Yahoo/CNBC) [GRÜN → 10 % Sizing]
Crash-Filter:       INAKTIV       (SPY Do -0,108 %; Fr 03.07. Feiertag)
Guardrails:  Daily +0,26 % | Weekly 0 % | DD -0,38 % | VIX ~16 | Käufe 0/2 → ALLE 8 GRÜN
```

**Konsistenz-Check Memory ↔ Alpaca:**
- Fr-Close 99.420,34 ↔ Alpaca last_equity 99.420,34 → **exakt ✓**
- Cash 79.428,25 identisch ✓
- lastday_price = Fr-Close Marks (JPM 334,47 / UNH 425,36 / MU 975,56) ↔ Memory identisch ✓
- avg_entry_price für alle 3 Positionen konsistent ✓

**Positionen Live V1–V6 (Pre-Market Marks Alpaca 08:35 ET):**
- **JPM**  333,12 $ (Entry 332,78, P/L +0,10 %, change_today -0,40 %)
  - V1 306,16 SICHER (+8,81 % Puffer)
  - V2 ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+10,26 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 315,32 > EMA200 306,00 ✓ carry-over
  - V6 RSI 62,83 / RS +12,30 % → NICHT ausgelöst
- **UNH**  424,19 $ (Entry 401,57, P/L +5,63 %, change_today -0,275 %)
  - V1 369,44 SICHER (+14,81 % Puffer)
  - V2 378,48 (getrailt 02.07. auf Posit-Hoch 430,095) SICHER (+12,08 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 385,12 > EMA200 342,87 ✓ carry-over (Spread +42,25)
  - V6 RSI 64,76 / RS +13,97 % → NICHT ausgelöst
- **MU**  1.008,21 $ (Entry 1.037,72, P/L -2,84 %, change_today +3,347 %) — **GAP UP entspannt V1-Watch**
  - V1 954,71 SICHER **+5,60 % Puffer** [ENTSPANNT vs Fr-Close +2,19 % — Gap-Down-Risiko abgewendet]
  - V2 913,39 (Posit-Hoch 1.037,94 = Fill-Preis carry-over) SICHER (+9,40 %)
  - V3 1.245,26 / V4 1.400,92 — weit entfernt
  - V5 EMA50 882,15 > EMA200 507,23 ✓ (Spread +374 sehr breit) carry-over
  - V6 RSI 48,57 / RS -8,42 % → NICHT ausgelöst (RSI <80)

→ **Alle V1–V6 SICHER für alle 3 Positionen.** Keine Verkaufsorder pending. MU-V1-Puffer weitet sich durch Pre-Market Gap-Up +3,35 % auf +5,60 % — kritische Weekend-Watch abgeschlossen ohne Trigger.

**Earnings-Blackouts (Perplexity Verifikation 06.07.):**
- **JPM Q2 2026: 14.07. BMO CONFIRMED** (Multi-Source: Business-Wire, MarketBeat, WallStreetHorizon, Public, MarketChameleon, JPM IR). 7 HT ab heute. Blackout aktiv ab **09.07. Close (Do)**. → **JETZT NICHT AKTIV**.
- **UNH Q2 2026:** Perplexity heute UNCONFIRMED, carry-over 16.07. (8 HT). Blackout aktiv ab **13.07. Close (Mo)**. → **JETZT NICHT AKTIV**.
- **MU Q4 FY2026:** Perplexity nennt 23.07. (nicht bestätigt); Memory-carry-over "typisch Ende Sept". Weit außerhalb 3-HT-Blackout. Recheck bei nächster Routine wenn <10T.
- Andere KW28 Mo-Mi Earnings: **KEINE** bestätigt.

**Watchlist Market-Open Mo 06.07. (carry-over Fr-Weekly-Review):**
- **GOOGL** LEAD | XLC (leerer Sektor) | K1-K3 carry ✓ | K5 FwdPE 27,45 ✓ / Rev +22 % ✓ | Earnings 22.07. (>10 HT) ✓ | **Kein Sektor-Konflikt**
- LLY | XLV (mit UNH) | K1-K3+K5 carry ✓ | K4 Live-Vol-Check | Earnings ~25.07. ✓
- MS | XLF (mit JPM) | K1-K3 carry ✓ | K5 ✓ | **Earnings 15.07. → 3-HT-Blackout ab 10.07. Close = 4 HT freies Fenster wenn Buy heute**
- CAT | XLI (leer) | K1-K3 carry ✓ | K5 Rev -1 % ✗ Recheck | Earnings ~05.08. ✓
- AMD | XLK-Konflikt MU | K5 FwdPE ✗ Recheck
- AAPL | XLK-Konflikt MU | K5 ? Recheck

**Sektor-Belegung:** JPM XLF 1,00 % + UNH XLV 10,21 % + MU XLK 9,10 % = 20,32 % investiert. 3/8 Slots. XLC/XLI/XLE/XLU/XLB/XLY/XLP leer.

**Guardrails-Detail (alle 8 GRÜN):**
```
1. Daily Loss Cap (-3 %):    +0,263 %                             [GRÜN]
2. Weekly Loss Cap (-5 %):    0,000 % (KW28 Reset)                [GRÜN]
3. Drawdown-Alarm (-15 %):   -0,384 % vs ATH 100.066,47           [GRÜN — 14,6 %-Puffer]
4. Drawdown-Stopp (-20 %):   INAKTIV
5. Crash-Filter (SPY -5 %):  INAKTIV (Do 02.07. -0,108 %)
6. VIX-Filter (>30):         INAKTIV (Spot ~16)
7. Earnings-Blackout:        KEINER
8. Käufe/Woche max. 2:       0/2
```

**Datenqualitäts-Hinweise:**
- SPY-Premarket via Alpaca IEX **nicht verwertbar** (After-Hours-Quote Fr 02.07. 16:00 ET, ap 762,42/bp 724,91 = zu weite Spread nach Feiertag)
- Perplexity SPY-PM, 10Y Treasury, News-Top-3 = leer (Datum-in-Zukunft-Bug carry-over)
- VIX ~16 Multi-Source verifiziert (CBOE Futures 15,81; Yahoo 16,32; CNBC 16,15)
- Alle Alpaca Broker-Marks konsistent mit Fr-Close-Memory

**ClickUp:** [PRE-MARKET] Check Task angelegt Prio 4 — Task-ID `869e0ux1k` (https://app.clickup.com/t/869e0ux1k). `custom_item_id: null` Workaround erneut erfolgreich (ITEM_246 Tier-Limit umgangen).

> **Entscheidung Pre-Market:** Alle 8 Guardrails GRÜN. MU-Gap-Up +3,35 % entlastet kritischen V1-Watch vom Weekend (Puffer +5,60 % statt +2,19 %). Keine Verkaufsorder für offene Positionen (V1–V6 sicher). **Market-Open-Scan JA** mit Lead-Kandidat **GOOGL** (XLC-Diversifikation, K5 sauber, Earnings 22.07. außerhalb Blackout). Backup: LLY (K4 Live-Vol), MS (Timing-Vorbehalt wg. 15.07. Earnings). Käufe KW28 0/2, Cash 79,68 % → 2 Slots verfügbar, 5 Positions-Slots frei.
> **Nächste Routine:** Mo 06.07. 09:30 ET Market Open (Buy-Scan GOOGL/LLY/MS mit Live-K4/K5-Verifikation).

---

## Wochenabschluss KW27 — 2026-07-03 17:05 ET (Fr, Weekly Review)

```
Gesamtwert:          99.420,34 $   (Alpaca equity, Fr-Close carry-over 02.07. da NYSE-Feiertag)
Cash:                79.428,25 $   (79,89 %)
Investiert (MV):     19.992,09 $   (20,11 %; JPM 1.003,41 + UNH 10.208,64 + MU 8.780,04)
Mo-Basis KW27:      100.024,25 $   (= Fr-Close 26.06.)
Wochenrendite KW27:      -0,604 %  [GRÜN — Weekly Cap -5 %]
SPY-Wochenrendite:       +2,127 %  (Alpaca IEX Fr 26.06. Close 729,35 → Do 02.07. Close 744,86; Fr 03.07. Feiertag)
Alpha KW27:              -2,731 %  [NEGATIV — SPY-Rally-Woche, Bot cash-heavy → begrenzte Partizipation]
YTD Rendite:             -0,580 %  (vs Startkapital 100.000 $; Bot lebt 33 Tage seit 31.05.26)
YTD SPY:                 +9,807 %  (Alpaca IEX YE25 678,32 → 744,86)
YTD Alpha:              -10,387 %  [Bot-Init spät im Jahr + Ramp-up-Phase mit hoher Cash-Quote]
ATH:                100.066,47 $
Drawdown vom ATH:        -0,646 %  [GRÜN — Alarm -15 % / Stopp -20 %]
Offene Positionen:          3 / 8  (5 Slots frei)
Käufe KW28 max.:              2   (Wochen-Reset Mo 06.07.)
```

**Positions-Delta KW27 (26.06.-Close → 03.07.-Close):**
- **JPM** 328,53 → 334,47 = **+1,81 %** ← Beste Wochen-Performance (Financials-Rebound Mi +2,08 %)
- **UNH** 428,00 → 425,36 = **-0,62 %** (Cool-off nach Rekord-Vortag Mi +2,63 % + Do neues Posit-Hoch 430,095)
- **MU**  neu 02.07. Fill @ 1.037,72 → 03.07.-Close 975,56 = **-5,99 %** ← Schlechteste (Fill-Day-Drop)

**Trade-Bilanz KW27:**
- Käufe: 1 (MU Do 02.07. 5/5-Signal K1-K5 + K5 Multi-Source-Verifikation)
- Verkäufe: 0 (keine V1–V6-Trigger)
- Stop-Loss-Trigger: 0
- Realisierter P/L KW27: 0 $ (nur MU offen)
- Realisierter P/L kumuliert: -596,19 $ (AVGO V1 KW26 carry-over)

**Sektor-Ranking KW27 (Alpaca IEX Fr 26.06. → Do 02.07.):**
| Rank | Sektor | Woche % | Alpha vs SPY | Bot-Position |
|------|--------|---------|--------------|--------------|
| 1 | XLF | +3,86 % | +1,73 % | JPM (1,01 %) ✓ |
| 2 | XLC | +3,37 % | +1,24 % | — |
| 3 | XLY | +2,30 % | +0,17 % | — |
| 4 | XLV | +2,18 % | +0,05 % | UNH (10,27 %) ✓ |
| 5 | XLI | +1,52 % | -0,61 % | — |
| 6 | XLB | +0,72 % | -1,41 % | — |
| 7 | XLP | +0,35 % | -1,77 % | — |
| 8 | XLK | -0,16 % | -2,29 % | **MU (8,83 %) ✗** |
| 9 | XLU | -0,93 % | -3,06 % | — |
| 10 | XLE | -1,15 % | -3,28 % | — |
| 11 | XLRE | -1,17 % | -3,30 % | — |

**Sektor-Cap-Check (Gesamtdepot-Basis):** XLF 1,01 % / XLV 10,27 % / XLK 8,83 % — alle klar unter 30 %-Cap. Kein Verstoß, keine Reduktion nötig. (Investiert-Basis: UNH 51 % / MU 44 % / JPM 5 % — nur Kontext, Bot-Konvention referenziert Gesamtdepot-%.)

**Watchlist Mo 06.07. (KW28 Start):**
| Symbol | Sektor | Grund | K5 | K7 Earnings |
|--------|--------|-------|-----|--------------|
| **GOOGL** | XLC (#2 KW27) | **NEUE LEAD** — FwdPE 27,45 ✓ / Rev +22 % ✓ / MCap ~2 Bio | ✓ | 22.07.2026 (knapp außerhalb 10T) |
| MS | XLF (#1 KW27) | K1-K3 ✓ carry-over; K5 FwdPE 21,58 ✓/ Rev +16,4 % ✓ | ✓ | **15.07.2026 → BLOCKS 10T-Blackout ab 10.07. Close** |
| LLY | XLV | K5 ✓ carry-over (FwdPE 32-33, Rev +26 %); K4 wartet | ✓ | ~25.07.2026 |
| CAT | XLI | K1-K4 ✓ carry-over; K5 RevGrowth -1 % ✗ | ✗ Recheck | ~05.08.2026 |
| AMD | XLK Konflikt MU | RS +132 % Semi-Rekord; K5 FwdPE ✗ | ✗ Recheck | ~05.08.2026 |
| AAPL | XLK Konflikt MU | K1-K3 ✓ carry-over | ? Recheck | ~30.07.2026 |

**Fokus KW28: GOOGL (K5-Recheck Multi-Source Mo Pre-Market zwingend, Sektor XLC füllt Lücke, kein Sektor-Konflikt).**

**Guardrails (8 Hierarchien):**
```
1. Daily Loss Cap (-3 %):    0,000 % (kein Handel 03.07.)     [GRÜN]
2. Weekly Loss Cap (-5 %):  -0,604 %                          [GRÜN — 4,4 %-Puffer]
3. Drawdown-Alarm (-15 %):  -0,646 % vs ATH 100.066,47        [GRÜN — 14,4 %-Puffer]
4. Drawdown-Stopp (-20 %):  INAKTIV
5. Crash-Filter (SPY-5 %):  INAKTIV (Do 02.07. -0,108 %)
6. VIX-Filter (>30):        INAKTIV (Spot ~16-17)
7. Earnings-Blackout:       KEINER — JPM 14.07. (7 HT ab Mo, Blackout ab 09.07. Close), UNH 16.07., MU Q4 Ende Sept
8. Käufe/Woche max. 2:      Reset KW28 Mo 06.07. → 0/2
```
→ **ALLE 8 GRÜN.** Strategie-Status: **STABIL** (keine Anpassung nötig).

**MU-V1-Beobachtung (kritischer Übergang KW27 → KW28):**
- V1 954,71 $ (Standardformel -8 % vom Fill 1.037,72)
- Close 03.07.-Mark 975,56 → Puffer **+2,19 %**
- 2,5 Nicht-Handels-Tage bis Mo 06.07. Open (Fr geschlossen + Sa + So + Feiertag-Übergang)
- **Gap-Down-Risiko:** Bei MU-Mo-Open <954,71 feuert V1 Market-Sell sofort → Pre-Market-Check Mo 08:30 ET zwingend, Alpaca-Preis + Perplexity Semi-News overnight
- V2 913,39 (Posit-Hoch=Fill), V3 1.245,26, V4 1.400,92 — alle weit weg
- V5 EMA50 882,15 > EMA200 507,23 (Spread +374 sehr breit) — kein Death-Cross-Risiko kurzfristig
- V6 RSI 48,57 / RS -8,42 % → V6 nicht ausgelöst (RSI<80)

**Nächste Routine:** Mo 2026-07-06 08:30 ET Pre-Market Check (KW28 Start).

> **Weekly-Review-Entscheidung:** KW27 abgeschlossen mit -0,604 % Performance / -2,73 % Alpha vs SPY. Alpha-Underperformance strukturell erklärbar: SPY-Rally-Woche +2,13 % bei Bot-Cash-Quote ~80 %. Alle 8 Guardrails GRÜN. Ein einziger Käufe-Slot KW27 genutzt (MU 5/5-Signal mit Multi-Source-K5), Fill-Day-Drop dokumentiert (V1-Puffer eng, aber im Rahmen der -8 %-Formel-Erwartung). Strategie-Lock hält — K5 Filter verhindert weiterhin Turnaround-Momentum-Trades (CRWD/INTC/AMD alle diese Woche geblockt). Watchlist-Lead KW28 ist **GOOGL** (XLC #2-Sektor der Woche, K5 sauber, Earnings 22.07. knapp außerhalb 10T-Blackout).
> **Lessons-Tag KW27:** (1) Fill-Day-Drop-Muster in 2/2 letzten Käufen (AVGO KW26 / MU KW27) — Sample noch klein, aber KW28-Käufe genau monitoren. (2) K5 Multi-Source-Verifikation als stabiler Filter bestätigt (Yahoo/MarketBeat/TTM implied). (3) ClickUp-Workaround `custom_item_id: null` verankert in lessons-learned. (4) V1-Standardformel absorbiert -5,75 % Intraday-Drop wie designed — keine Regel-Änderung.

---

## Market Close 2026-07-03 16:02 ET (Fr, KW27) — NO-OP TAGESBILANZ (NYSE geschlossen — Independence Day observed)

```
Alpaca clock:      is_open=false | next_open Mo 06.07. 09:30 ET (KW28 Start)
Gesamtwert:        99.420,34 $   (Alpaca equity = last_equity → 0,000 % intraday, kein Handel)
Cash:              79.428,25 $   (79,89 %)
Investiert (MV):   19.992,09 $   (20,11 %, JPM 1.003,41 + UNH 10.208,64 + MU 8.780,04)
P/L heute:              0,00 $    (0,000 %)  [GRÜN — kein Handelstag]
Alpha vs SPY:           n/a       (SPY-Tages-Print existiert nicht — NYSE geschlossen)
ATH:              100.066,47 $    DD: -0,646 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW27:      -0,604 %    [GRÜN — Mo-Basis Fr 27.06.-Close 100.024,25, Schwelle -5 %]
Käufe KW27:            1/2        (MU gefillt Do 02.07.; 1 Slot theoretisch frei, aber KW27 endet mit Fr-Close)
Pending Orders:        0          (keine V5/V6-Order möglich → kein Handel Mo als nächster Tag; strategiekonform keine Feiertags-Order)
VIXY-Ref:          21,47 $ carry-over 02.07. → Spot ~16-17 [GRÜN → 10 % Sizing]
Guardrails:        Daily 0,00 % | Weekly -0,60 % | DD -0,65 % | VIX ~17 | Käufe 1/2 → ALLE GRÜN
```

**Positionen — Marks (Alpaca 16:02 ET Close, carry-over vom Do 02.07. mit minimalem Mark-Refresh):**
- **JPM**  334,47 $ (Entry 332,78, P/L +0,51 %, change_today 0,00 %)
  - V1 306,16 SICHER (+8,46 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 unverändert) SICHER (+9,66 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50/200 carry-over Close 02.07.: EMA50 315,32 > EMA200 306,00 ✓ (kein neuer HT-Balken → keine EMA-Fortschreibung)
  - V6 RSI(14) 62,83 / RS_4w vs SPY +12,30 % → SICHER (carry-over)
- **UNH**  425,36 $ (Entry 401,57, P/L +5,92 %, change_today 0,00 %) — Mark leicht > Close 02.07. (424,28)
  - V1 369,44 SICHER (+15,14 % Puffer)
  - V2 Stop 378,48 (Posit-Hoch 430,095 unverändert) SICHER (+11,79 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 385,12 > EMA200 342,87 ✓ (carry-over, sehr breiter Spread)
  - V6 RSI 64,76 / RS +13,97 % → SICHER
- **MU**  975,56 $ (Entry 1037,72, P/L -5,99 %, change_today 0,00 %) [KRITISCH]
  - V1 954,71 SICHER **nur +2,19 % Puffer** (leicht verengt gegenüber Close 02.07. +2,38 %, essentially = Midday-Mark)
  - V2 Stop 913,39 (Posit-Hoch 1037,94 = Fill-Preis unverändert) SICHER (+6,80 %)
  - V3 1245,26 / V4 1400,92 — weit entfernt
  - V5 EMA50 882,15 > EMA200 507,23 ✓ (Spread +374,92 — Golden Cross sehr breit, kein Death-Cross-Risiko)
  - V6 RSI 48,57 / RS -8,42 % → NICHT ausgelöst (V6 verlangt beides: RSI>80 UND RS<0)

**V1–V6-Check heute: NICHT scharfgestellt** (kein Handel, keine Trigger-Auswertung möglich). Alle Marks = Alpaca-Broker-Refresh gegen letzten offiziellen 02.07.-Close, keine intraday-Bewegung.
→ **Keine Limit-Order für nächsten Handelstag vorbereitet.** Alle 6 Verkaufssignale bleiben — sofern man die Vorabend-Marks als proxy nimmt — SICHER. MU-V1-Puffer bleibt eng (+2,19 %) → Gap-Down-Risiko Mo-Open weiter kritisch, aber V1-Trigger nur bei Handel möglich (Mo 06.07. 09:30 ET).

**Sektor-Update:** JPM XLF 1,01 % + UNH XLV 10,29 % + MU XLK 8,85 % → Total 20,11 % investiert. XLK 8,85 % (weit unter 30 %-Sektorlimit). 3/8 Positions-Slots belegt.

**Daily Loss Cap (-3 %):** 0,00 % → GRÜN, keine Stornierung, keine offenen Orders.
**Weekly Loss Cap (-5 %):** -0,604 % → GRÜN, keine Stornierung.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -0,646 % → GRÜN.

**Watchlist Mo 06.07. (KW28 Start, carry-over vom 02.07.-Close mit Feiertags-Vorbehalt):**
- **MS**  XLF NEU-Slot | K1✓K2✓K3✓ carry-over 02.07. | K4/K5 Mo-Open-Recheck
- **CAT** XLI leer | K1✓K2✓K3✓ carry-over | K5 RevGrowth -1 % ✗ (aktuell blockiert bis Multi-Source-Recheck)
- **LLY** XLV bereits UNH | K1✓K2✓K3✓K5✓ carry-over | K4 Mo-Open + Sektor-30 %-Check
- **AMD** XLK bereits MU | K1✓K2✓K3✓ (RS+132,84 %) | K5 FwdPE struktur. ✗ — Multi-Source-Recheck erforderlich
- **AAPL** XLK bereits MU | K1✓K2✓K3✓ carry-over | K4/K5 Mo-Open-Recheck

**Watchlist-Hinweis:** Weekly Review Fr 17:00 ET folgt direkt und setzt Watchlist ggf. neu. Perplexity-Sektor-Check heute nicht durchgeführt (Feiertag → keine neuen Marktdaten). Weekly Review übernimmt Multi-Source-Prüfung für AMD/CAT K5.

**Perplexity SPY-Tagesabfrage: übersprungen** — NYSE geschlossen, kein SPY-Tages-Print vorhanden (alpha_heute nicht berechenbar).

**ClickUp:** [CLOSE] Tagesbilanz Fr 03.07. als Prio 4 (Low) erstellt — Task-ID `869dzrdre` (https://app.clickup.com/t/869dzrdre). **Workaround ITEM_246:** Payload mit `custom_item_id: null` umgeht Tier-Limit-Fehler "Max usage for custom task types reached" (erster Versuch ohne Feld → Fehler; expliziter null-Wert erzwingt Standard-Task-Type → OK). **Lessons-learned:** Ab sofort ClickUp-Task-Payloads immer mit `custom_item_id: null` senden.

> **Entscheidung:** No-Op-Tagesbilanz — NYSE geschlossen wg. Independence Day observed (04.07. Sa → Bundesfeiertag wird auf Fr 03.07. vorgezogen). Portfolio flat bei 99.420,34 $, Positionen unverändert 3/8, keine offenen Orders. Alle 4 Guardrails-Ebenen (Daily/Weekly/DD/Käufe) GRÜN. MU-V1-Puffer weiter eng (+2,19 %) — bleibt zentrales Beobachtungsobjekt für Mo-Open.
> **Lessons-Tag:** Feiertags-Close entfernt jede Trigger-Möglichkeit — Bot-Strategie hält Puffer über Wochenende + Feiertag hinweg (2,5 Nicht-Handels-Tage nach 02.07.-Close). Bei MU (V1-Puffer 2,19 %) besteht Gap-Down-Risiko: falls Mo-Open unter 954,71 $, feuert V1-Market-Sell sofort — Pre-Market-Check Mo 08:30 ET unabdingbar.
> **Nächste Routine:** Fr 2026-07-03 17:00 ET Weekly Review (KW27-Bilanz: 1/2 Käufe, MU-Fill -5,99 %-Mark, realisiert AVGO -596,19 $ carry-over, KW27 Weekly-P/L -0,60 %, Watchlist für KW28 finalisieren).

---

## Midday 2026-07-03 13:07 ET (Fr, KW27) — NO-OP (NYSE GESCHLOSSEN Independence Day observed)

```
Alpaca clock:      is_open=false | next_open Mo 06.07. 09:30 ET
Positionen:        3/8 (JPM/UNH/MU — carry-over Close 02.07.)
Equity:            99.420,34 $ (last_equity 99.420,34 → 0,00 % intraday, keine Bewegung mangels Handel)
Long MV:           19.992,09 $ (vs Close 02.07. 19.985,25 → +6,84 $ Mark-Refresh, essentially unverändert)
Cash:              79.428,25 $ (79,89 %)
Daily P/L:         +0,000 %   [GRÜN — kein Handel, last_equity = equity]
Weekly P/L KW27:   -0,608 %   [GRÜN — vs Mo-Basis 100.024,25]
ATH:              100.066,47 $  DD: -0,650 % [GRÜN]
Guardrails:        Daily 0,00 % | Weekly -0,61 % | DD -0,65 % | Käufe 1/2 → ALLE GRÜN
```

**V1–V4-Check: NICHT möglich** (kein Live-Handel, keine Trigger-Auswertung, keine Order-Platzierung).

**Marks carry-over Close 02.07. (Alpaca Mark-Refresh minimal):**
- JPM 334,49 $ (Entry 332,78, P/L +0,51 %) — V1 306,16 SICHER (+8,47 % Puffer)
- UNH 424,28 $ (Entry 401,57, P/L +5,66 %) — V1 369,44 SICHER (+12,93 % Puffer), V2 378,48 SICHER (+10,79 %)
- MU 977,92 $ (Entry 1.037,72, P/L -5,76 %) — V1 954,71 SICHER **+2,42 % Puffer** [KRITISCH bleibt — wichtig für Mo Open]

**Daily Loss Cap (-3 %):** 0,00 % → GRÜN, keine Order-Stornierung, keine offenen Limit-Orders vorhanden.

**ClickUp:** kein Alert (keine Stops, kein Cap, kein Handel → Logging-Disziplin gewahrt).

> **Entscheidung:** No-Op — Feiertagsschluss. Nächste substanzielle Prüfung: **Mo 2026-07-06 08:30 ET Pre-Market Check (KW28 Start)**. MU-V1-Puffer bleibt eng (+2,42 %) → Gap-Down-Risiko am Mo-Open beobachten, V1-Trigger bei MU <954,71 löst Market-Sell sofort aus.
> **Nächste Routine:** Fr 2026-07-03 17:00 ET Weekly Review (KW27-Bilanz — 1/2 Käufe genutzt, MU-Fill -5,75 %, Realisiert -596 $ carry-over AVGO).

---

## Market Close 2026-07-02 16:02 ET (Do, KW27) — Tagesbilanz

```
Gesamtwert:        99.413,51 $   (Alpaca equity Close, vs last_equity 100.006,91)
Cash:              79.428,26 $   (79,90 %)
Investiert (MV):   19.985,25 $   (20,10 %, JPM 1.003,41 + UNH 10.182,72 + MU 8.802,00 [nach 5,75% Intraday-Drop])
P/L heute:           -593,40 $    (-0,593 %)
Alpha vs SPY:        -0,485 %     (SPY -0,108 % via Alpaca IEX 745,665 → 744,86)
ATH:              100.066,47 $    DD: -0,653 % [GRÜN — Alarm bei -15 %]
Weekly P/L KW27:     -0,611 %     [GRÜN — Mo-Basis = Fr-Close 100.024,25, Schwelle -5 %]
Käufe KW27:           1/2         (MU gefillt 02.07. 10:17 ET; 1 frei — Fr 03.07. verkürzter HT bis 13:00 ET)
Pending Orders:       0           (keine V5/V6-Verkaufsorder, kein neuer K5-Kandidat)
VIXY-Ref:          21,47 $ Vortag → Spot ~16-17 [GRÜN → 10 % Sizing]
Guardrails:        Daily -0,59 % | Weekly -0,61 % | DD -0,65 % | VIX ~17 | Käufe 1/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 16:00 ET Close):**
- **JPM**  334,47 $ (Entry 332,78, P/L +0,51 %, change_today +0,12 %)
  - V1 306,16 SICHER (+8,46 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06., heute Hoch nur 337,89) SICHER (+9,68 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 315,32 > EMA200 306,00 ✓ (Spread +9,32 stabil)
  - V6 RSI(14) 62,83 / RS_4w vs SPY +12,30 % → SICHER (RSI <80, RS positiv)
- **UNH**  424,28 $ (Entry 401,57, P/L +5,66 %, change_today -0,53 %, NEUES Posit-Hoch 430,095 heute)
  - V1 369,44 SICHER (+12,93 % Puffer)
  - V2 Stop **NEU** 378,48 (Trail nach neuem Hoch 430,095, vorher 376,65) SICHER (+10,79 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 385,12 > EMA200 342,87 ✓ (Spread +42,25 sehr komfortabel)
  - V6 RSI(14) 64,76 / RS_4w vs SPY +13,97 % → SICHER (RSI <80, RS positiv)
- **MU**  978,00 $ (Entry 1037,72 Fill 10:17 ET, P/L -5,75 %, change_today -5,26 %) [KRITISCH]
  - V1 954,71 SICHER **nur +2,38 % Puffer** [KRITISCH — <3 % Puffer]
  - V2 Stop 913,39 (Posit-Hoch 1037,94 post-fill, essentially = Fill-Preis) SICHER (+6,61 %)
  - V3 1245,26 / V4 1400,92 — weit entfernt
  - V5 EMA50 882,15 > EMA200 507,23 ✓ (Spread +374,92 — Golden Cross sehr breit, KEIN Death-Cross-Risiko kurzfristig)
  - V6 RSI(14) 48,57 / RS_4w vs SPY -8,42 % → NICHT ausgelöst (RSI <80, obwohl RS negativ; V6 verlangt BEIDES)

**Verkaufssignal-Check V1–V6: ALLE SICHER für alle 3 Positionen.**
→ **Keine Limit-Order für morgen vorbereitet.** Pending Orders bleiben 0.
→ MU-V1-Puffer bleibt eng (+2,38 %). Pre-Market-Check morgen zwingend, V1-Trigger bei MU <954,71 löst Market-Order sofort aus.

**Schlechteste Position:** MU -5,75 % (Fill-Day-Drop, RSI 48,57 aber V5 sehr sicher, V6-Trigger benötigt zusätzlich RSI>80)
**Beste Position:** UNH +5,66 % (change_today -0,53 % nach Rekord-Vortag, V2 hochgetrailt auf 378,48)

**Sektor-Update:** JPM XLF 1,01 % + UNH XLV 10,24 % + MU XLK 8,85 % → Total 20,10 % investiert. XLK 8,85 % (unter 30 % Sektorlimit). 3/8 Positions-Slots belegt.

**Daily Loss Cap (-3 %):** -0,593 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,611 % → GRÜN, keine Stornierungen.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -0,653 % → GRÜN.

**Watchlist für morgen (Fr 03.07. verkürzt bis 13:00 ET):**
- **MS**  213,89 $ | XLF NEU | K1✓K2✓(RSI 52,51)K3✓(RS+15,03%) | K4/K5 Open-Check
- **CAT** 963,60 $ | XLI leer | K1✓K2✓(RSI 50,92)K3✓(RS+18,28%) | K5 carry-over ✗ (RevGrowth -1%)
- **LLY** 1210,79 $ | XLV | K1✓K2✓(RSI 67,06)K3✓(RS+13,13%) | K5✓ carry-over, K4 wartet
- **AMD** 518,25 $ | XLK bereits MU | K1✓K2✓(RSI 52,49)K3✓(RS+132,84% — Semi-Rekord) | K5 struktur. ✗ FwdPE — Multi-Source-Recheck
- **AAPL** 308,24 $ | XLK bereits MU | K1✓K2✓(RSI 60,74)K3✓(RS+6,99%) | K4/K5 Open-Check

**Fr 03.07. Kontext:** Verkürzter HT bis 13:00 ET (Independence Day Sa 04.07.). Volumina dünner, K4-Hürde kritischer. Käufe KW27 nur noch 1 Slot frei (nach MU-Fill). Weiteres Auge auf MU-V1-Puffer (+2,38 %) — Break unter 954,71 löst Market Sell sofort aus.

**ClickUp:** [CLOSE] Tagesbilanz Task angelegt (Prio 3 wg. leicht negativer Performance) und Push-Notification an Owner gesendet. ITEM_246 Tier-Limit Custom-Task-Types carry-over — Standard-Task-Erstellung funktioniert.

> **Entscheidung:** Portfolio stabil bei -0,593 % nach MU-Fill+Intraday-Drop, klar unter Guardrail-Schwellen. Kein V1-V6-Verkauf für morgen — alle 3 Positionen halten. MU-Case: V1 sehr eng (+2,38 %), aber V5 Golden Cross sehr breit (+374 EMA-Spread) und V6 RSI 48 unter Trigger → strategiekonformes Halten. Alpha -0,485 % vs SPY erwartbar (MU-Konzentrations-Effekt +9,3 % Portfolio bei -5,75 % Move). Watchlist prioritisiert MS (XLF-Diversifikation) und CAT (XLI-Slot noch leer) für morgen — beide mit K5-Recheck.
> **Lessons-Tag:** K5-Multi-Source K5 klappte zwar bei MU (5/5), aber Fill-Day-Move -5,75 % zeigt: K1-K5 Kauf-Signale schützen NICHT vor Intraday-Volatilität. Positive Anmerkung: V1 -8 % Standardformel absorbiert -5,75 % Move genau wie designed — Puffer noch da. Timing-Erkenntnis: Limit-Order +0,5 % über Vortagesschluss ist "Chase-safe", aber wenn Gap-Down einsetzt (MU eröffnete +1,86 %, fiel dann -5,26 %) landet man am ungünstigen Punkt der Range.
> **Nächste Routine:** Fr 2026-07-03 08:30 ET Pre-Market Check (verkürzter HT bis 13:00 ET, keine 13:00 Midday-Routine da Close 13:00).

---

## Midday 2026-07-02 13:06 ET (Do, KW27) — Stop-Check (MU FILL + STARK NEGATIV)

```
Positionen:        3/8 (MU 09:42 Order → 10:17 ET Fill @ 1037,72)
Ø P/L (gewichtet): ~0,00 % (JPM +0,40 % / UNH +5,63 % / MU -5,85 %)
Schlechteste:      MU -5,85 % (V1 nur +2,30 % Puffer — KRITISCH)
Beste:             UNH +5,63 % (V1 +14,81 % Puffer)
Stops:             alle regulär — kein V1/V2/V3/V4-Trigger
Daily P/L:         -0,614 %   [GRÜN — vs last_equity 100.006,91]
Equity:            99.393,02 $ (long_market_value 19.964,76, cash 79.428,26)
```

**Live-Check V1–V4 (Alpaca 13:06 ET):**
- **JPM** 334,10 $ (Entry 332,78, P/L +0,40 %, change_today +0,01 %)
  - V1 306,16 SICHER (+9,13 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over vom 25.06.) SICHER (+10,60 %)
  - V3 399,34 / V4 449,25 — weit entfernt, kein TP-Trigger
- **UNH** 424,165 $ (Entry 401,57, P/L +5,63 %, change_today -0,56 %)
  - V1 369,44 SICHER (+14,81 % Puffer)
  - V2 Stop 376,65 (Posit-Hoch 428,01 vom 01.07. carry-over, kein neues Hoch heute) SICHER (+12,60 %)
  - V3 481,88 / V4 542,12 — weit entfernt, kein TP-Trigger
- **MU** 976,71 $ (Entry 1037,72 Fill 10:17 ET, P/L -5,85 %, change_today -5,35 %) [KRITISCH]
  - V1 954,71 (1037,72 * 0,92) SICHER **nur +2,30 % Puffer**
  - V2 Trailing 913,19 (1037,72 * 0,88, Posit-Hoch = Fill-Preis, kein neues Hoch nach Fill) SICHER (+6,95 %)
  - V3 1.245,26 / V4 1.401,42 — weit entfernt
  - RSI/EMA-Check nicht Teil des Midday-Prozesses (nur Open/Close)

→ **Keine Verkaufsorder.** Alle Stops regulär, aber MU-V1-Puffer sehr eng (+2,30 %).
→ **Daily Loss Cap (-3 %) nicht erreicht** (-0,614 %). Keine Order-Stornierung.

**MU-Fill-Detail (Alpaca):**
- Order-ID: 6c45f431-facd-4979-8c01-d0976e2f2474
- Filled_at: 2026-07-02T14:17:09 UTC (10:17 ET) @ 1037,72 avg (9/9 Sh)
- Cost-Basis: 9.339,48 $ (9,34 % Portfolio at fill)
- Intraday-Move seit Fill: -5,85 % → MU crashte nach Fill in unter 3 h
- V1 Standardformel -8 % vom Fill: 954,71 $ → aktuell 976,71 → **+22,00 $/+2,30 % Puffer bleibt**
- Käufe KW27 jetzt 1/2

**ClickUp:** CRITICAL Alert wegen MU V1-Nähe versucht (Prio 2) → Push-Notification an Owner primär (ITEM_246 Tier-Limit carry-over).

**Nächste Routine:** 16:00 ET Market Close (MU-V5/V6 dann geprüft, evtl. V1 bereits ausgelöst wenn weiterer Verlust).

---

## Market Open 2026-07-02 09:43 ET (Do, KW27) — MU LIMIT-ORDER PLACED (5/5, K5 Multi-Source ✓)

```
Gesamtwert:         99.995,32 $   (Alpaca equity Live 09:37 ET, vs last_equity 100.006,91 → -0,012 %)
Cash:               88.767,74 $   (88,77 %)
Investiert (MV):    11.227,58 $   (11,23 %, JPM 1.003,31 $ + UNH 10.223,76 $)
Unrealisiert P/L:     +591,05 $   (JPM +4,97 $ / UNH +586,08 $)
Realisiert P/L:       -596,19 $   (AVGO V1 26.06., carry-over)
Daily P/L:            -0,012 %    [GRÜN — vs last_equity 100.006,91]
Weekly P/L KW27:      -0,029 %    [GRÜN — vs Mo-Basis 100.024,25 = Fr-Close 26.06.]
ATH:               100.066,47 $   DD: -0,071 % [GRÜN]
Käufe KW27:            0/2        (0 genutzt — MU pending nicht gezählt bis fill; wenn Fill: 1/2)
Pending Orders:        1          MU Buy Limit 9 Sh @ 1037,80 Day (ID 6c45f431)
VIXY Live:            21,47 $     → Spot ~16,7 [GRÜN → 10 % Sizing]
SPY Live 09:37:      749,09 $     (+0,459 % vs Mi-Close 745,665 → moderate risk-on Open)
Crash-Filter:        NEIN         (SPY +0,46 %)
Guardrails:        Daily -0,01 % | Weekly -0,03 % | DD -0,07 % | VIX ~16,7 | Käufe 0/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 09:37 ET):**
- **JPM**  334,435 $ (Entry 332,78, P/L +0,50 %, change_today +0,11 %)
  - V1 306,16 SICHER (+9,23 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over vom 25.06.) SICHER (+10,63 %)
  - V5 EMA50 316,48 > EMA200 308,96 ✓ (carry-over Mi-Close)
  - V6 RSI 65,18 / RS_4w +12,80 % → KEIN Trigger
- **UNH**  425,99 $ (Entry 401,57, P/L +6,08 %, change_today -0,13 %)
  - V1 369,44 SICHER (+15,31 % Puffer)
  - V2 Stop 376,65 (getrailt 01.07. Posit-Hoch 428,01) SICHER (+13,15 %)
  - V5 EMA50 391,55 > EMA200 347,22 ✓ (carry-over Mi-Close)
  - V6 RSI 63,46 / RS_4w +14,68 % → KEIN Trigger

→ **Keine Verkaufsorder pending.** Alle V1–V6 SICHER für beide.

**Kandidaten-Scan K1–K5 (Alpaca IEX Bars + Live 09:30–09:37 ET, Perplexity K5):**

- **MU** Live 1.051,88 $ (Open ~1.038, vs Mi-Close 1.032,64 → +1,86 % intraday) — **LEAD-PICK**
  - K1 ✓ EMA50 877,31 > EMA200 458,31 (Spread +419,00 — Golden Cross sehr weit)
  - K2 ✓ RSI(14) 51,82 (Alpaca-Close 01.07., viel Raum bis 70)
  - K3 ✓ RS_63d MU +205,94 % vs SPY +14,70 % → **+191,24 % RS**
  - K4 ✓ IEX-Cumvol nach 7 min = 58.265 Sh vs. Avg20 IEX 1.019.072. Projektion (390-min-Extrapolation) ~3,24M = **319 % Avg20** >> 120 % Hürde
  - **K5 ✓ Multi-Source verifiziert (Perplexity 02.07. Live):**
    - FwdPE Yahoo Finance: 6,73 ✓ ≤35
    - FwdPE MarketBeat: 10,41 ✓ ≤35
    - TTM diluted EPS Yahoo: 44,28 → implied Trailing P/E ~23,7 ✓ ≤35
    - RevGrowth YoY Q3 FY2026: +56 % (auch bei alternativer Perplexity-Angabe 196 % clean ≥10 %)
  - Sektor: XLK Technology / Semis — füllt Lücke (JPM XLF, UNH XLV, XLK bisher leer)
  - Earnings: MU Q4 FY2026 typisch Ende September → KEIN 3-HT-Blackout aktiv
  - **Verdict: 5/5 GRÜN → LIMIT-ORDER PLACED (siehe unten)**

- **ELV** Live 421,395 $ (+1,31 % vs Mi 415,95) — K1-K3 ✓ | K4 ✗ IEX-Cumvol 7 min = 1.133 → Projektion 63k = 79 % Avg20 79.405 << 120 % | K5 ✗ RevGrowth Q1 +1,5 % strukturell → **4/5 BLOCKS K5+K4**
- **LLY** Live 1.192,715 $ (+0,05 % vs Mi 1.192,14) — K1-K3+K5 ✓ | K4 ✗ IEX 7 min = 872 → Projektion 49k = 33 % Avg20 148.478 << 120 % → **4/5 BLOCKS K4**
- **CAT** Live 984,81 $ (-0,72 %) — K1-K4 ✓ | K5 ✗ RevGrowth Q1 -1 % → 4/5 BLOCKS K5
- **AMD** Live 531,96 $ (-1,65 %) — K1-K3+K4 ✓ | K5 ✗ FwdPE 35–95x → 4/5 BLOCKS K5
- **INTC** Live 125,89 $ (-0,94 %) — K5 ✗ FwdPE >120 strukturell → BLOCKS

**Order-Details (Alpaca):**
```
Order-ID:       6c45f431-facd-4979-8c01-d0976e2f2474
Symbol:         MU
Side:           BUY
Type:           LIMIT
Qty:            9 Shares
Limit-Preis:    1.037,80 $ (= round(1032,64 * 1,005, 2), K5-konformer +0,5 %-Cap über Vortagesschluss)
Time-in-Force:  DAY
Status:         NEW (accepted, unfilled bei Live 1.044-1.052 — Fill nur bei Pullback ≤1.037,80)
Max-Cost bei Fill: 9.340,20 $ (9,34 % Portfolio)
```

**Sizing-Check:**
- portfolio_value 99.995,32 * 0,10 = 9.999,53 (VIX <25 → 10 %)
- shares = floor(9.999,53 / 1.051,88) = 9
- limit = round(1.032,64 * 1,005, 2) = 1.037,80

**Sektor-Check (bei Fill):**
- JPM XLF 1,00 % + UNH XLV 10,23 % + MU XLK 9,34 % → Total 20,57 % investiert, XLK 9,34 % (unter 30 % Sektorlimit)
- Positionen 3/8, weiter 5 Slots frei

**Wenn Fill: Stop-Levels (V1–V4) berechnet ex-post nach avg fill price (Standardformeln V1 -8 %, V2 -12 % trail, V3 +20 %, V4 +35 %).**

**Wenn kein Fill bis 16:00 ET: Order verfällt (Day). KW27-Käufe bleiben 0/2.**

**ClickUp:** TRADE_BUY Alert Versuch (Prio 3) → ITEM_246 "Max usage for custom task types reached" (Tier-Limit-Issue carry-over seit 26.06.). Push-Notification an Owner + Memory-Log primär.

> **Entscheidung:** LIMIT-ORDER MU platziert. Erstes 5/5-K-Signal seit AVGO 22.06. Multi-Source K5-Verifikation (Yahoo/MarketBeat FwdPE + implied TTM P/E + Perplexity RevGrowth) klar unter K5-Schwelle → keine CRWD/INTC-Wiederholung. K1-K4 Live bestätigt. Limit +0,5 % über Vortag (1.037,80) schützt vor Chase — MU +1,86 % geöffnet, Order fillt nur bei Pullback. Sektor XLK-Lücke wird geschlossen. Guardrails alle GRÜN. Cash bleibt bei Fill 79.427,54 $ (79,43 %).
> **Lessons-Tag:** K5 Multi-Source-Discipline funktioniert — verhindert CRWD/INTC-Fehleinschätzungen bei hohen FwdPE, ermöglicht MU bei niedrigem FwdPE. Aktuelle Perplexity-Datenqualität schwankt (Rev 56 % vs 196 % zwischen Queries), aber Threshold-Richtung bleibt konsistent → K5 ✓.
> **Nächste Routine:** Do 2026-07-02 13:00 ET Midday Stop-Check (inkl. MU-Order-Status).

---

## Market Close 2026-07-01 16:04 ET (Mi, KW27) — Tagesbilanz

```
Gesamtwert:       100.006,57 $   (Alpaca equity Close, vs last_equity 99.724,85)
Cash:              88.767,74 $   (88,76 %)
Investiert (MV):   11.238,83 $   (11,24 %, JPM 1.001,63 $ + UNH 10.237,20 $)
P/L heute:           +281,72 $    (+0,283 %)
Alpha vs SPY:        +0,414 %     (SPY -0,132 % via Alpaca IEX 746,65 → 745,665)
ATH:              100.066,47 $    DD: -0,060 % [GRÜN]
Weekly P/L KW27:     -0,018 %     [GRÜN — Mo-Basis = Fr-Close 100.024,25, Schwelle -5 %]
Käufe KW27:           0/2         (0 genutzt, 2 frei — 2 Handelstage KW27 verbleibend: Do 02.07., Fr 03.07. verkürzt)
Pending Orders:       0
Guardrails:        Daily +0,28 % | Weekly -0,02 % | DD -0,06 % | VIXY 21,47 (+0,77 %, Spot ~17) | Käufe 0/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 16:00 ET Close):**
- **JPM**  334,06 $ (Entry 332,78, P/L +0,38 %, change_today +2,08 %)
  - V1 306,16 SICHER (+9,11 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over vom 25.06.) SICHER (+10,51 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 316,48 > EMA200 308,96 ✓ (Spread +7,52 leicht geweitet vs Di +5,37)
  - V6 RSI(14) 65,18 / RS_4w +12,80 % → SICHER (RSI <80, RS positiv)
- **UNH**  426,52 $ (Entry 401,57, P/L +6,21 %, change_today +2,63 %, NEUES Tages-/Posit-Hoch 428,01)
  - V1 369,44 SICHER (+15,45 % Puffer)
  - V2 Stop **NEU** 376,65 (Trail nach neuem Hoch 428,01 heute) SICHER (+13,24 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 391,55 > EMA200 347,22 ✓ (Spread +44,33 sehr komfortabel)
  - V6 RSI(14) 63,46 / RS_4w +14,68 % → SICHER (RSI <80, RS positiv)

**Verkaufssignal-Check V1–V6: ALLE SICHER für beide Positionen.**
→ **Keine Limit-Order für morgen vorbereitet.** Pending Orders bleiben 0.

**Schlechteste Position:** JPM +0,38 % (aber intraday-Rebound +2,08 % — bester Sektor-Tag seit KW26)
**Beste Position:** UNH +6,21 % (change_today +2,63 %, neues Posit-Hoch 428,01, V2-Trail auf 376,65 hochgesetzt)

**Sektor-Update:** Unverändert Struktur — XLF (JPM 1,00 %) + XLV (UNH 10,24 %). XLK weiter leer.

**Daily Loss Cap (-3 %):** +0,283 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,018 % → GRÜN, keine Stornierungen.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -0,060 % → GRÜN.
**Crash-Filter:** SPY -0,13 % heute → INAKTIV.
**VIX-Filter:** VIXY 21,47 (+0,77 % vs Di 21,305) → Spot ~17 → GRÜN.

**Watchlist morgen Do 02.07. (K1–K4 via Alpaca IEX Close 01.07., K5 Perplexity):**
- **ELV 415,95 $ (+7,59 %!)** — K1 ✓ EMA50 384,33>EMA200 348,01 | K2 ✓ RSI 59,2 | K3 ✓ RS_63d +27,3 % | K4 ✓ Vol 175 % Avg20 | **K5 ✗ FwdPE 13,9–14,6 ✓ ABER RevGrowth Q1 +1,5 % (Perplexity carry-over, EPS-Beat 12,58 vs 10,74 heute)** → **4/5 LEAD — K5-Recheck morgen Pre-Market (Q2-Earnings-Guidance-Anhebung 26,75 EPS könnte RevGrowth-Blick verändern)**
- **CAT 991,98 $ (-6,82 %)** — K1-K4 ✓ (Vol 144 %) | K5 ✗ RevGrowth Q1 -1 % strukturell → 4/5 BLOCKS
- **AMD 540,89 $ (-6,83 %)** — K1-K3 ✓ + K4 ✓ (Vol 128 %) | K5 ✗ FwdPE 35–95x → 4/5 BLOCKS
- **MU 1.032,64 $ (-10,37 %)** — K1-K3 ✓ | K4 ✗ Vol 108 % | K5 unklar → Perplexity morgen zwingend
- **LLY 1.192,14 $ (-0,60 %)** — K1-K3+K5 ✓ | K4 ✗ Vol 72 % → warten
- **INTC 127,08 $ (-8,94 %)** — K5 strukturell BLOCKS (FwdPE >120)

**Earnings-Status:**
- JPM Q2 2026: 2026-07-14 (13 Tage) → KEIN Blackout
- UNH Q2 2026: 2026-07-16 (15 Tage) → KEIN Blackout
- ELV Q2 2026: 2026-07-16 (~16 Tage geschätzt) → KEIN Blackout (bei Kauf morgen)

**Markt-Kontext heute:**
- SPY -0,13 % auf 745,665 (leichter Pullback nach Di-Rekord, Range 742,39-749,41)
- **Financials-Rebound:** JPM +2,08 % (Perplexity: „JPMorgan Chase +3,30 %" Konsens-Move nach Yield-Curve-Steepening)
- **Health-Insurer Explosion:** ELV +7,59 % nach EPS-Beat 12,58 vs. 10,74 + Guidance-Anhebung 2026 EPS ≥26,75. Sektor XLV Highlight-Tag.
- UNH mit +2,63 % auf 426,52 (neues Posit-Hoch 428,01) — profitiert vom Sektor-Move mit
- Bot Cash-Heavy 88,76 % — trotzdem heute Alpha +0,41 % durch UNH+JPM Doppel-Rally

**ClickUp:** Tagesbericht-Task `[CLOSE] Tagesbilanz — 2026-07-01` Prio 4 → ITEM_246 "Max usage for custom task types reached" (Tier-Limit carry-over seit 26.06.). Memory-Log primär, Push-Notification an Owner.

> **Entscheidung:** Tagesbilanz GRÜN + Alpha positiv (+0,41 %). Beide Longs profitieren — UNH neues Posit-Hoch, JPM Financials-Rebound. Keine Verkaufsorders (V1–V6 alle SICHER, JPM V1-Puffer weitet auf +9,11 %, UNH V2 hochgetrailt auf 376,65). Watchlist-Lead morgen ist **ELV** — massiver Earnings-Move mit Volumen 175 %, alle K1–K4 ✓, aber K5 RevGrowth-Hürde (Q1 +1,5 %) blockt strukturell trotz starker Guidance. Pre-Market Perplexity-Recheck zwingend: Q2-Erwartungen könnten K5 aufweichen. 2 Slots + 2 Handelstage KW27 (Fr 03.07. verkürzt für Independence Day).
> **Lessons-Tag:** ELV EPS-Beat + Guidance-Anhebung = **klassisches Post-Earnings-Momentum-Setup mit K1–K4 alle ✓**, wird aber strategisch von K5 RevGrowth-Hürde (10 %) blockiert. K5-Filter verhindert Insurer-Momentum-Trades solange Insurance-Rev-Growth strukturell 1–7 % ist. Alternative: strategy.md Review bei Insurer-Sektor-Signalen könnte eine EPS-Growth-Hürde ergänzen, aktuell aber strategie-lock — kein Override.
> **Nächste Routine:** Do 2026-07-02 08:30 ET Pre-Market Check.

---

## Midday 2026-07-01 13:06 ET (Mi, KW27) — Stop-Check

```
Positionen:        2/8
Ø P/L (gewichtet): +5,30 % (JPM +0,34 % / UNH +5,79 %)
Schlechteste:      JPM +0,34 % (V1 +8,31 % Puffer)
Beste:             UNH +5,79 % (V1 +13,05 % Puffer)
Stops:             alle regulär — kein V1/V2/V3/V4-Trigger
Daily P/L:         +0,243 %   [GRÜN — vs last_equity 99.724,85]
Equity:            99.967,13 $ (long_market_value 11.199,39, cash 88.767,74)
```

**Live-Check V1–V4 (Alpaca 13:06 ET):**
- **JPM** 333,92 $ (Entry 332,78, P/L +0,34 %, change_today +2,00 %)
  - V1 306,16 SICHER (+8,31 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over vom 25.06.) SICHER (+9,52 %)
  - V3 399,34 / V4 449,25 — weit entfernt, kein TP-Trigger
- **UNH** 424,84 $ (Entry 401,57, P/L +5,79 %, change_today +2,23 %)
  - V1 369,44 SICHER (+13,05 % Puffer)
  - V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over vom 26.06., Tageshoch ~424,84 → kein neues Hoch) SICHER (+11,26 %)
  - V3 481,88 / V4 542,12 — weit entfernt, kein TP-Trigger

→ **Keine Verkaufsorder.** Alle Stops regulär.
→ **Daily Loss Cap (-3 %) nicht erreicht** (+0,243 %). Keine Order-Stornierung.
→ **ClickUp:** kein Alert (keine Stops / kein Cap → Logging-Disziplin gewahrt).

**Nächste Routine:** 16:00 ET Market Close.

---

## Market Open 2026-07-01 09:37 ET (Mi, KW27) — KEIN TRADE (LLY K4 FAIL, INTC K5 FAIL)

```
Gesamtwert:        99.745,58 $   (Alpaca equity Live 09:37 ET, vs last_equity 99.724,85 → +0,021 % GRÜN)
Cash:              88.767,74 $   (88,99 %)
Investiert (MV):   10.977,84 $   (11,01 %, JPM 978,87 $ + UNH 9.998,64 $)
Unrealisiert P/L:    +376,05 $   (JPM -19,47 $ / UNH +355,52 $)
Realisiert P/L:      -596,19 $   (AVGO V1 26.06., carry-over)
Daily P/L:           +0,021 %    [GRÜN — vs last_equity 99.724,85]
Weekly P/L KW27:     -0,279 %    [GRÜN — vs Mo-Basis 100.024,25 = Fr-Close 26.06.]
ATH:              100.066,47 $   DD: -0,321 % [GRÜN]
Käufe KW27:           0/2        (0 genutzt, 2 frei — 2 Handelstage KW27 verbleibend)
Pending Orders:       0
VIXY Live:            21,62 $    [GRÜN → Spot ~17 → 10 % Sizing erlaubt]
SPY Live:            743,08 $    (-0,48 % vs Di-Close 746,65 → moderate risk-off Open)
Crash-Filter:        NEIN        (SPY -0,48 %)
Guardrails:        Daily +0,02 % | Weekly -0,28 % | DD -0,32 % | VIX ~17 | Käufe 0/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 09:37 ET):**
- **JPM**  326,29 $ (Entry 332,78, P/L -1,95 %, change_today -0,29 %)
  - V1 306,16 SICHER (+6,58 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over vom 25.06.) SICHER (+8,00 %)
  - V5 EMA50 314,15 > EMA200 308,78 ✓ (carry-over Di-Close)
  - V6 RSI 57,6 / RS_4w +11,86 % → KEIN Trigger
- **UNH**  416,36 $ (Entry 401,57, P/L +3,68 %, change_today +0,20 %)
  - V1 369,44 SICHER (+12,71 % Puffer)
  - V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over vom 26.06.) SICHER (+10,71 %)
  - V5 EMA50 383,13 > EMA200 339,23 ✓ (carry-over Di-Close)
  - V6 RSI 60,6 / RS_4w +10,94 % → KEIN Trigger

→ **Keine Verkaufsorder pending.** Alle V1–V6 SICHER für beide.

**Kandidaten-Scan K1–K5 (Alpaca IEX-Bars Close 30.06. + Live 09:30–09:39 ET):**

- **LLY** Live 1.188,95 $ (Open 1.211,52 → -1,87 % intraday, vs Di-Close 1.199,38 → -0,87 %)
  - K1 ✓ EMA50 1073,1 > EMA200 978,5
  - K2 ✓ RSI(14) 66,5 (Cooldown von 74,5 am Mo, weiter unter 70)
  - K3 ✓ RS_63d +17,1 %
  - **K4 ✗ FAIL** — IEX-Cumvol nach 9 min = 2.197 Sh vs. Avg20 IEX 147.363. Tages-Projektion (390-min-Extrapolation) ~95k = **65 % Avg20** << 120 % Hürde. Vortag K4 99 % war Grenze; heute deutlich schwächer.
  - K5 ✓ FwdPE 32,4–33,0 + Rev YoY +26 % (carry-over Perplexity 30.06.)
  - **Verdict: 4/5 — K4 hart BLOCKS.** Zusätzlich Open-Selloff (-1,87 %) bestätigt fehlendes Momentum.

- **INTC** Live 132,86 $ (Open 135,03 → -1,61 % intraday, vs Di-Close 139,55 → -4,80 %)
  - K1 ✓ EMA50 109,4 > EMA200 61,0
  - K2 ✓ RSI(14) 63,0
  - K3 ✓ RS_63d +220,7 %
  - K4 ✓ IEX-Cumvol nach 9 min = 165.223 vs. Avg20 IEX 4.026.506. Projektion ~7,2M = **179 % Avg20** (K4 ✓)
  - **K5 ✗ FAIL** — Perplexity Live 01.07.: FwdPE Multi-Source: Seeking Alpha 120,24 / Yahoo 158,73 / MarketBeat 221,63 → **alle >>35**. RevGrowth Q1 2026 YoY nur **+7,4 %** (<10 %-Hürde). BEIDE K5-Sub-Kriterien FAIL.
  - **Verdict: 3/5 — K5 hart BLOCKS.** INTC strukturell wie CRWD/AMD (Turnaround-Story mit stretched Bewertung).

- **CAT** carry-over Close 30.06. 1.063,33 — K5 ✗ RevGrowth Q1 -1 % → BLOCKS
- **AMD** carry-over Close 580,52 — K5 ✗ FwdPE 35–95x Konsens → BLOCKS
- **CRWD** carry-over Close 763,12 — K2 ✗ RSI 70,3 + K5 ✗ FwdPE ~69x → BLOCKS
- **ELV** carry-over Close 386,98 — K2 ✗ RSI 46,9 + K5 ✗ RevGrowth +7 % → BLOCKS

→ **KEIN Kandidat erfüllt alle 5 Kaufsignale. KEIN Trade.**

**Sektor-Update:** Unverändert — XLF (JPM 0,98 %) + XLV (UNH 10,02 %). XLK weiter leer.

**Earnings-Status (carry-over Pre-Market):**
- JPM Q2 2026: 2026-07-14 (13 Tage) → KEIN Blackout
- UNH Q2 2026: 2026-07-16 (15 Tage) → KEIN Blackout

**ClickUp:** ROUTINE Normal-Alert Versuch (Prio 3) — bei Tier-Limit ITEM_246 (carry-over seit 26.06.) Fallback Push-Notification an Owner.

> **Entscheidung:** KEIN Trade. LLY-Lead scheitert am K4 Live-Vol (Open-Selloff -1,87 % mit sehr niedrigem IEX-Cumvol → Projektion 65 % Avg20 = klar unter 120 % Hürde). INTC-Backup scheitert an K5 hart (FwdPE >>120 alle Quellen + RevGrowth 7,4 % <10 %). Bot bleibt cash-heavy 89 %. Alle 2 KW27-Slots ungenutzt, 2 Handelstage verbleibend.
> **Lessons-Tag:** K4 Vol-Trigger bei Open-Selloff ist zuverlässiger Blocker — LLY-Kursverfall + Vol-Absence bestätigen fehlendes Momentum. Pre-Market Buy-Setup „K4 heute entscheidend" hat sich als sauberer Filter erwiesen. INTC K5-Prüfung wichtig: Turnaround-Stories brauchen weiterhin >35 FwdPE-Filter-Respekt.
> **Nächste Routine:** Mi 2026-07-01 13:00 ET Midday Stop-Check.

---

## Market Close 2026-06-30 16:04 ET (Di, KW27) — Tagesbilanz

```
Gesamtwert:        99.722,36 $   (Alpaca equity Close, vs last_equity 99.831,59)
Cash:              88.767,74 $   (89,02 %)
Investiert (MV):   10.954,62 $   (10,98 %, JPM 981,66 $ + UNH 9.972,96 $)
P/L heute:           -109,23 $    (-0,1094 %)
Alpha vs SPY:        -0,891 %     (SPY +0,782 % via Alpaca IEX 740,86 → 746,65)
ATH:              100.066,47 $    DD: -0,344 % [GRÜN]
Weekly P/L KW27:     -0,302 %     [GRÜN — Mo-Basis = Fr-Close 26.06. 100.024,25, Schwelle -5 %]
Käufe KW27:           0/2         (0 genutzt, 2 frei)
Pending Orders:       0
Guardrails:        Daily -0,11 % | Weekly -0,30 % | DD -0,34 % | VIXY 21,305 (-2,16 %, Spot ~17) | Käufe 0/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 16:00 ET Close):**
- **JPM**  327,24 $ (Entry 332,78, P/L -1,67 %, change_today -0,659 %)
  - V1 306,16 SICHER (+6,89 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over vom 25.06.) SICHER (+8,28 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 314,15 > EMA200 308,78 ✓ (Spread +5,37, knapper als 29.06.)
  - V6 RSI(14) 57,6 / RS_4w +11,86 % → SICHER (RSI <80, RS positiv)
- **UNH**  415,54 $ (Entry 401,57, P/L +3,48 %, change_today -1,019 %)
  - V1 369,44 SICHER (+12,47 % Puffer)
  - V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over vom 26.06., Tageshoch heute 422,51 → kein neues Hoch) SICHER (+10,38 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 383,13 > EMA200 339,23 ✓ (Spread +43,90 sehr komfortabel)
  - V6 RSI(14) 60,6 / RS_4w +10,94 % → SICHER (RSI <80, RS positiv)

**Verkaufssignal-Check V1–V6: ALLE SICHER für beide Positionen.**
→ **Keine Limit-Order für morgen vorbereitet.** Pending Orders bleiben 0.

**Schlechteste Position:** JPM -1,67 % (Tagestief 326,725; XLF-Lag nach News „financials lagged on lower-rate expectations")
**Beste Position:** UNH +3,48 % (Pullback -1,02 % vom Open 421,61, Trail-Stop ungefährdet)

**Sektor-Update:** Unverändert — XLF (JPM ~0,98 %) + XLV (UNH ~10,00 %). XLK weiter leer.

**Daily Loss Cap (-3 %):** -0,1094 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,302 % → GRÜN, keine Stornierungen.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -0,344 % → GRÜN.
**Crash-Filter:** SPY +0,78 % heute → INAKTIV.
**VIX-Filter:** VIXY 21,305 (-2,16 % vs gestern) → Spot ~17 → GRÜN.

**Watchlist morgen Mi 01.07. (K1–K4 via Alpaca IEX Close 30.06., K5 Perplexity 30.06.):**
- **LLY 1.199,36 $** — K1✓ EMA50 1073,1>EMA200 978,5 | K2✓ RSI 66,5 (raus aus Overheat) | K3✓ RS_63d +17,1 % (LLY +35,3 % vs SPY +18,1 %) | K4✗ Vol 99 % (knapp unter 120 %) | **K5✓ FwdPE 32,4–33,0 + Rev YoY +26 %** → **4/5 — Lead, K4 Vol-Trigger morgen entscheidend**
- **INTC 139,55 $** — K1✓ EMA50 109,4>EMA200 61,0 | K2✓ RSI 63,0 | K3✓ RS_63d +220,7 % (massive Comeback-Story) | K4✗ Vol 49 % | K5 Perplexity-Quelle leer (FwdPE ~12–22 vorläufig, RevGrowth ausstehend) → **3/4 + K5 Recheck morgen Pre-Market zwingend**
- **CAT 1.063,33 $ (+0,42 %)** — K1✓ K2✓ K3✓ K4✗ 83 % | **K5✗ RevGrowth Q1 2026 -1 % YoY (Perplexity neu)** → 3/5 — strukturell blockt
- **ELV 386,98 $ (-0,24 %)** — K2✗ RSI 46,9 + K5✗ RevGrowth +7 % YoY (<10 %) → 2/5
- **CRWD 763,12 $ (+2,76 %)** — K2✗ RSI 70,3 + **K5✗ FwdPE ~69x** → 2/5 — strukturell blockt
- **AMD 580,52 $** — K1✓ K2✓ K3✓ K4✓ Vol 121 % | **K5✗ FwdPE Konsens 35–95x (GuruFocus 37 / Finbox 70 / MarketBeat 94)** → 4/5 — K5 strukturell blockt (ähnlich CRWD)

**Earnings-Status:**
- JPM Q2 2026: 2026-07-14 (14 Tage) → KEIN Blackout
- UNH Q2 2026: 2026-07-16 (16 Tage) → KEIN Blackout
- LLY Q2 2026: 2026-07-31 (Perplexity neu, 31 Tage) → KEIN Blackout

**Markt-Kontext heute:**
- SPY +0,78 % auf 746,65 (neues lokales Hoch nach cooler-than-expected Inflations-Daten — Fed-Rate-Cut-Erwartung steigt)
- Megacap Tech + Large-Cap Pharma outperformed (Quelle Perplexity)
- Financials lagged (JPM -0,66 % bestätigt) auf flatter Yield Curve
- Bot Cash-Heavy 89 % → Beta-Verzicht an risk-on-Tag = -0,89 % Alpha heute

**ClickUp:** Tagesbericht-Task `[CLOSE] Tagesbilanz — 2026-06-30` Prio 3 → ITEM_246 "Max usage for custom task types reached" (Tier-Limit carry-over seit 26.06.). Memory-Log primär, Push-Notification an Owner.

> **Entscheidung:** Tagesbilanz GRÜN trotz Cash-Heavy-Underperformance (-0,89 % Alpha bei SPY +0,78 % risk-on). Diszipliniert: keine Strategie-Override für K5-Blocker (AMD/CRWD bleiben Tabu trotz starker Tech-Momentum, weil FwdPE-Konsens >35 hart blockt). LLY ist Lead morgen — alle Hürden ✓ außer K4 Vol; bei Open-Vol-Push trigger-fähig. Sektor-Lücke XLK bleibt — keine strategie-konformen Tech-Kandidaten verfügbar bis EPS-Wendepunkte oder Bewertungs-Reset.
> **Lessons-Tag:** Tech-Bewertungs-Filter K5 (FwdPE ≤35) blockt aktuell die gesamte Mega-Cap-Tech-Range (AMD/CRWD), während Bot-Index-Performance leidet. Watchlist-Pflege: AMD wie CRWD strukturell ausgeschlossen bis FwdPE-Compression. INTC einzige Tech-Hoffnung (K1–K3 ✓, K5 plausibel) — K4-Vol-Push abwarten.
> **Nächste Routine:** Mi 2026-07-01 08:30 ET Pre-Market Check.

---

## Midday 2026-06-30 13:03 ET (Di, KW27) — Stop-Check

```
Positionen:        2/8
Ø P/L (gewichtet): +3,40 % (JPM -1,05 % / UNH +3,86 %)
Schlechteste:      JPM -1,05 % (V1 +7,55 % Puffer)
Beste:             UNH +3,86 % (V1 +12,90 % Puffer)
Stops:             alle regulär — kein V1/V2/V3/V4-Trigger
Daily P/L:         -0,076 %   [GRÜN — vs last_equity 99.831,59]
Equity:            99.755,83 $ (long_market_value 10.988,09, cash 88.767,74)
```

**Live-Check V1–V4 (Alpaca 13:03 ET):**
- **JPM** 329,30 $ (Entry 332,78, P/L -1,05 %)
  - V1 306,16 SICHER (+7,55 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over) SICHER (+9,00 %)
  - V3 399,34 / V4 449,25 — weit entfernt, kein TP-Trigger
- **UNH** 417,065 $ (Entry 401,57, P/L +3,86 %)
  - V1 369,44 SICHER (+12,90 % Puffer)
  - V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over) SICHER (+10,78 %)
  - V3 481,88 / V4 542,12 — weit entfernt, kein TP-Trigger

→ **Keine Verkaufsorder.** Alle Stops regulär.
→ **Daily Loss Cap (-3 %) nicht erreicht** (-0,076 %). Keine Order-Stornierung.
→ **ClickUp:** kein Alert (keine Stops / kein Cap → Logging-Disziplin gewahrt).

**Nächste Routine:** 16:00 ET Market Close.

---

## Market Open 2026-06-30 09:32 ET (Di, KW27) — KEIN TRADE (CRWD K5 FAIL)

```
Gesamtwert:        99.817,37 $   (Alpaca equity Live 09:32 ET, vs last_equity 99.831,59 → -0,014 %)
Cash:              88.767,74 $   (88,93 %)
Investiert (MV):   11.049,63 $   (11,07 %, JPM 988,25 $ + UNH 10.056,04 $)
Unrealisiert P/L:    +408,27 $   (JPM -10,10 $ / UNH +418,36 $)
Realisiert P/L:      -596,19 $   (AVGO V1 26.06., carry-over)
Daily P/L:           -0,014 %    [GRÜN — vs last_equity 99.831,59]
Weekly P/L KW27:     -0,207 %    [GRÜN — vs Mo-Basis 100.024,25 = Fr-Close 26.06.]
ATH:              100.066,47 $   DD: -0,249 % [GRÜN]
Käufe KW27:           0/2        (0 genutzt, 2 frei)
Pending Orders:       0
VIX (Spot proxy):    ~17,7       [GRÜN <25 → 10 % Sizing erlaubt; VIXY 21,80 +0,11 %]
SPY Open:            741,39 $    (+0,07 % vs Mo-Close 740,86, flat Open)
Crash-Filter:        NEIN        (SPY +0,07 %)
Guardrails:        Daily -0,01 % | Weekly -0,21 % | DD -0,25 % | VIX ~17,7 | Käufe 0/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 09:32 ET):**
- **JPM**  329,29 $ (Entry 332,78, P/L -1,05 %, change_today +0,008 %)
  - V1 306,16 SICHER (+7,55 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over) SICHER (+9,00 %)
  - V5 EMA50 313,62 > EMA200 307,76 ✓ (carry-over Mo-Close)
  - V6 RSI ~60 / RS_4w +12,11 % → KEIN Trigger
- **UNH**  419,255 $ (Entry 401,57, P/L +4,40 %, change_today -0,195 %)
  - V1 369,44 SICHER (+13,48 % Puffer)
  - V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over) SICHER (+11,36 %)
  - V5 EMA50 381,82 > EMA200 340,19 ✓ (carry-over Mo-Close)
  - V6 RSI ~64 / RS_4w +12,43 % → KEIN Trigger

→ **Keine Verkaufsorder pending.** Alle V1–V6 SICHER für beide.

**Kandidaten-Scan K1–K5 (Alpaca IEX-Bars Close 29.06., Perplexity K5 Live):**
- **CRWD** Close 742,61 | K1 ✓ EMA50 621,31>EMA200 522,82 | K2 ✓ RSI(14) 68,88 (knapp <70) | K3 ✓ RS_63d +84,03 % (CRWD +100,88 % vs SPY +16,85 %) | K4 N/A (Live-Vol bei Open zu früh, 1.408 IEX 3 min) | **K5 ✗ FAIL — FwdPE 151,52 (Yahoo) / 798,83 (MarketBeat) >>35; Rev YoY +26 % ✓ aber FwdPE-Hürde reißt** → **4/5 (K5 BLOCKS HART)**
- **LLY** carry-over | K2 ✗ RSI 74,5 Overheat → Cooldown abwarten
- **CAT** carry-over | K4 ✗ Vol 95 % + K5 ✗ FwdPE >35 → 3/5
- **ELV** carry-over | K2 ✗ RSI 47,5 + K5 ✗ RevGrowth +1,5 % → 2/5

→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Pre-Market-Schätzung CRWD FwdPE 28,5 erwies sich als falsch (vermutlich P/S-Verwechslung oder veraltete Datenquelle). Tatsächlicher FwdPE 151,52 (Yahoo Finance, MarketBeat 798,83) — CRWD-Earnings sind aktuell tief negativ (TTM-EPS -$0,69 GuruFocus), womit P/E-basierte Bewertungen extrem stretched sind. **K5-Hürde 35 wäre nur erreichbar wenn EPS-Wendepunkt + Margenexpansion in nächsten 4 Quartalen kommt — nicht modelliert in Strategie.**

→ **KEIN Trade heute.** 0/2 Slots KW27 weiterhin verfügbar.

**Sektor-Update:** Unverändert — XLF (JPM 0,99 %) + XLV (UNH 10,07 %). XLK weiter leer.

**Earnings-Status (carry-over Pre-Market):**
- JPM Q2 2026: 2026-07-14 (14 Tage) → KEIN Blackout
- UNH Q2 2026: 2026-07-16 (16 Tage) → KEIN Blackout

**ClickUp:** ROUTINE Normal-Alert Versuch (Prio 3) → ITEM_246 "Max usage for custom task types reached" (Tier-Limit-Issue carry-over seit 26.06.). Memory-Log primär — Push-Notification an Owner gesendet.

> **Entscheidung:** KEIN Trade. CRWD-Lead durch K5-FwdPE-Verifikation hart blockiert — Pre-Market hatte vorläufige Schätzung 28,5, Live-Multi-Source-Check (Yahoo + MarketBeat) liefert >150. Disziplin: K5 hart, keine Override. 2 Slots KW27 bleiben verfügbar. Bot bleibt cash-heavy (88,93 %) — Opportunitätskosten bei flatter SPY-Open (+0,07 %) gering.
> **Lessons-Tag:** K5-Pre-Market-Schätzungen müssen am Open IMMER mit Multi-Source verifiziert werden — Single-Source kann Stat-Typ-Verwechslung (P/S vs P/E) enthalten.
> **Nächste Routine:** Di 2026-06-30 13:00 ET Midday Stop-Check.

---

## Pre-Market 2026-06-30 08:33 ET (Di, KW27) — Buy-Scan JA, Lead CRWD

```
Gesamtwert:        99.847,91 $   (Alpaca equity Pre-Market Mark, vs Mo-Close 99.841,92 → +5,99 $ Settlement-Tick)
Cash:              88.767,74 $   (88,90 %, identisch zu Memory)
Investiert (MV):   11.080,17 $   (11,10 %, JPM 988,41 $ + UNH 10.091,76 $)
Last_Equity:       99.831,59 $   (Mo-EOD-Mark)
Daily P/L:           +0,016 %    (+16,32 $) [GRÜN — Limit -3 %]
Weekly P/L KW27:     -0,176 %    (vs Mo-Basis 100.024,25 = Fr-Close) [GRÜN — Limit -5 %]
ATH:              100.066,47 $   DD: -0,219 % [GRÜN]
Käufe KW27:           0/2        (0 genutzt, 2 frei)
Pending Orders:       0
VIX (Spot):          17,65       [GRÜN <25 → 10 % Sizing erlaubt]
VIXY Close 29.06.:   21,775      (-3,65 % vs Fr — Vola-Entspannung)
SPY Premarket:      741,61 $     (+0,10 % vs Mo-Close 740,86, IEX Last 08:13 ET)
Crash-Filter:       NEIN         (SPY Mo +1,58 %)
Guardrails:        Daily +0,02 % | Weekly -0,18 % | DD -0,22 % | VIX 17,65 | Käufe 0/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 08:32 ET):**
- **JPM**  329,47 $ (Entry 332,78, P/L -1,00 %, change_today +0,02 %)
  - V1 306,16 SICHER (+7,61 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over) SICHER (+9,06 %)
  - V5 EMA50 313,62 > EMA200 307,76 ✓ (Spread +5,86 carry-over)
  - V6 RSI ~60 / RS_4w +12,11 % → KEIN Trigger
- **UNH**  420,49 $ (Entry 401,57, P/L +4,71 %, change_today +0,16 %)
  - V1 369,44 SICHER (+13,82 % Puffer)
  - V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over) SICHER (+11,68 %)
  - V5 EMA50 381,82 > EMA200 340,19 ✓ (Spread +41,63 carry-over)
  - V6 RSI ~64 / RS_4w +12,43 % → KEIN Trigger

→ **Keine Verkaufsorder pending.** Alle V1–V6 SICHER.

**Earnings-Blackouts (Perplexity verifiziert heute):**
- **JPM Q2 2026 KORRIGIERT auf 2026-07-14** (vorher 07-15 angenommen) — 14 Tage entfernt → KEIN Blackout
- UNH Q2 2026: 2026-07-16 (carry-over plausibel) — 16 Tage → KEIN Blackout
- → Standard V1 -8 % bleibt für beide, kein Stop-Tightening.

**Watchlist Buy-Scan 09:30 ET (Carry-over Close 29.06.):**
- **CRWD 742,61 $ — LEAD** (4/4 tech ✓, K5 vorläufig ✓ FwdPE 28,5 / Rev +12,3 %) → K4+K5+K2 Final-Check am Open zwingend
- LLY 1.229,06 $ (RSI 74,5 Overheat → K2 BLOCKS, Cooldown abwarten)
- CAT 1.033,53 $ (K4 Vol 95 %, K5 FwdPE >35 → BLOCKS)
- ELV 387,92 $ (K2 RSI 47,5 + K5 RevGrowth +1,5 % → BLOCKS)

**Entscheidung:** Market-Open-Scan 09:30 ET JA. Lead CRWD mit Limit max +0,5 % (746,32 $), Sizing ~10 % = 13 Sh. Fallback: kein Pflicht-Kauf bei K5/K4-Kippung. Sektor XLK leer → CRWD würde Lücke füllen.

**Reconciliation Memory ↔ Alpaca:**
- portfolio.md Mo-Close 99.841,92 vs Alpaca last_equity 99.831,59 = -10,33 $ After-Hours-Tick (akzeptabel)
- cash 88.767,74 identisch
- Positionen-Anzahl & avg_entry konsistent (JPM 3 Sh @ 332,78 / UNH 24 Sh @ 401,57)

**Nächste Routine:** 09:30 ET Market Open — Buy-Scan + CRWD K5 Final via Perplexity.

---

## Market Close 2026-06-29 16:00 ET (Mo, KW27) — Tagesbilanz

```
Gesamtwert:        99.841,92 $   (Alpaca equity Close, vs last_equity 100.024,25)
Cash:              88.767,74 $   (88,91 %)
Investiert (MV):   11.074,18 $   (11,09 %, JPM 994,18 $ + UNH 10.080,00 $)
P/L heute:           -182,33 $    (-0,182 %)
Alpha vs SPY:        -1,760 %     (SPY +1,578 % IEX 729,35 → 740,86)
ATH:              100.066,47 $    DD: -0,225 % [GRÜN]
Weekly P/L KW27:     -0,182 %     [GRÜN — Mo-Basis = Fr-Close 100.024,25, Schwelle -5 %]
Käufe KW27:           0/2         (0 genutzt, 2 frei)
Pending Orders:       0
Guardrails:        Daily -0,18 % | Weekly -0,18 % | Käufe 0/2 → ALLE GRÜN
```

**Positionen Live V1–V6 (Alpaca 16:00 ET Close):**
- **JPM**  331,39 $ (Entry 332,78, P/L -0,42 %, change_today +0,71 %)
  - V1 306,16 SICHER (+8,23 % Puffer)
  - V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over vom 25.06., Tageshoch heute ~333) SICHER (+9,69 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
  - V5 EMA50 313,62 > EMA200 307,76 ✓ (Spread +5,86 — Golden Cross seit Tagen, leicht ausgeweitet)
  - V6 RSI(14) 60,10 / RS_4w +12,11 % → SICHER (RSI <80, RS positiv)
- **UNH**  420,00 $ (Entry 401,57, P/L +4,59 %, change_today -1,84 %)
  - V1 369,44 SICHER (+13,67 % Puffer)
  - V2 Stop ~376,47 (Posit-Hoch 427,81 vom 26.06., Tageshoch heute ~427,89 → kein neues Hoch, Trail unverändert) SICHER (+11,55 %)
  - V3 481,88 / V4 542,12 — nicht erreicht
  - V5 EMA50 381,82 > EMA200 340,19 ✓ (Spread +41,63 sehr komfortabel)
  - V6 RSI(14) 64,15 (Cooldown von ~75 am Fr) / RS_4w +12,43 % → SICHER (RSI <80, RS positiv)

**Verkaufssignal-Check V1–V6: ALLE SICHER für beide Positionen.**
→ **Keine Limit-Order für morgen vorbereitet.** Pending Orders bleiben 0.

**Schlechteste Position:** JPM -0,42 % (intraday positiv +0,71 %, aber unter Entry-Niveau)
**Beste Position:** UNH +4,59 % (Pullback -1,84 % vom Fr-Hoch 427,89, Trail-Stop ungefährdet)

**Sektor-Update:** Unverändert — XLF (JPM ~1 %) + XLV (UNH ~10,1 %). XLK weiter leer.

**Daily Loss Cap (-3 %):** -0,182 % → GRÜN, kein Eingriff.
**Weekly Loss Cap (-5 %):** -0,182 % → GRÜN, keine Stornierungen.
**ATH-Drawdown (-15 % Alarm / -20 % Stopp):** -0,225 % → GRÜN.
**Crash-Filter:** SPY +1,58 % heute → INAKTIV.
**VIX-Filter:** carry-over Pre-Market 18,41 → GRÜN (unter 25-Schnitt).

**Watchlist morgen Di 30.06.:**
- **CRWD 742,61 $ (+6,08 % heute)** — K1✓ EMA50 616 > EMA200 516 | K2✓ RSI 67,6 | K3✓ RS_63d +84,0 % | K4✓ Vol 158 % Avg20 — **Lead-Kandidat**, K5 vorläufig ✓ (Perplexity: FwdPE 28,5 / Rev YoY +12,3 %); finale K5-Verifizierung bei Market Open
- **LLY 1.229,06 $ (+1,86 % heute)** — K2 ✗ RSI 74,5 (weiter overheated, Cooldown noch nicht erreicht) — Watch bis RSI <70
- **CAT 1.033,53 $ (+3,54 % heute)** — K1-K3 ✓, K4 (Vol 95 %) ✗ heute, K5 carry-over FwdPE >35 → Watch
- **ELV 387,92 $ (-1,84 %)** — K2 ✗ RSI 47,5 unter 50, K5 RevGrowth-Hürde — Watch nach Q2-Earnings (~16.07.)

**ClickUp:** Tagesbericht-Task `[CLOSE] Tagesbilanz — 2026-06-29` Prio 4 (Low — positive Guardrails GRÜN bei minimalem Daily-Verlust).

> **Entscheidung:** Tagesbilanz GRÜN trotz Cash-Heavy-Underperformance (89 % Cash kostete heute ~1,8 % Alpha bei SPY +1,58 %). Diszipliniert: keine Panik-Käufe nach Risk-on-Tag — Strategie hält an K-Kriterien fest. CRWD ist morgen Lead-Kandidat mit allen 4 technischen Signalen voll erfüllt; entscheidend wird K5-Final-Check bei Market Open. UNH hält Trend trotz Cooldown souverän (V2 weit weg).
> **Nächste Routine:** Di 2026-06-30 08:30 ET Pre-Market Check.

---

## Midday 2026-06-29 13:02 ET (Mo, KW27)

```
Positionen:        2/8                (JPM + UNH)
Ø P/L:            +2,04 %             ((-0,27 + 4,35)/2)
Equity:           99.822,29 $          (Alpaca Live)
Cash:             88.767,74 $          (88,93 %)
Investiert (MV):  11.054,55 $          (11,07 %, JPM 995,67 $ + UNH 10.057,08 $)
Daily P/L:        -0,202 %             [GRÜN — vs last_equity 100.024,25]
Pending Orders:   0
```

**Positionen Live V1–V4 (Alpaca Trades 13:02 ET):**
- JPM  331,89 $ (Entry 332,78, P/L -0,27 %, change_today +0,86 %)
  - V1 306,16 SICHER (+8,41 % Puffer)
  - V2 Stop ~302,11 (Hoch carry-over 343,31, Tageshoch 332,335 → kein Trail-Update) SICHER (+9,85 %)
  - V3 399,34 / V4 449,25 — nicht erreicht
- UNH  419,045 $ (Entry 401,57, P/L +4,35 %, change_today -2,07 %)
  - V1 369,44 SICHER (+13,43 % Puffer)
  - V2 Stop ~376,47 (Hoch carry-over 427,81 vom 26.06., Tageshoch 425,01 → kein Trail-Update) SICHER (+11,30 %)
  - V3 481,88 / V4 542,12 — nicht erreicht

**Stops:** alle regulär — KEINE V1/V2/V3/V4 ausgelöst (RSI/EMA bei Midday nicht geprüft per Strategie).

**Schlechteste Position:** JPM -0,27 % (intraday +0,86 % gegen Vortagestief, aber unter Entry)
**Beste Position:** UNH +4,35 % (Pullback -2,07 % vom Vortagshoch 427,89, V2-Trail bleibt komfortabel)

**Daily Loss Cap:** -0,202 % vs -3 % → GRÜN, keine Order-Stornierung nötig.
**Pending Orders:** 0 (keine Stornierungen ausgelöst).
**ClickUp:** Kein Log — keine Stops ausgelöst, kein Daily-Cap erreicht (per Routine-Regel SCHRITT 5).

> Entscheidung: kein Eingriff. UNH gibt nach Fr-Schlusshoch +3 % heute -2 % ab — gesunder Pullback, Trail-Stop unverändert. JPM seitwärts. Daily P/L -0,20 % weit weg vom Cap.
> Nächste Routine: 16:00 ET Market Close (Tagesbilanz + V5/V6 Signal-Check).

---

## Market Open 2026-06-29 09:33 ET (Mo, KW27) — KEIN TRADE

```
Gesamtwert:        99.890,15 $   (Alpaca equity Live 09:33 ET)
Investiert:        11.127,00 $   (11,14 %, JPM 988,20 $ + UNH 10.138,80 $)
Cash:              88.767,74 $   (88,86 %)
Unrealisiert P/L:   +490,98 $    (JPM -10,14 $ / UNH +501,12 $)
Realisiert P/L:     -596,19 $    (AVGO V1 26.06.; carry-over)
Daily P/L:           -0,134 %    [GRÜN — vs last_equity 100.024,25]
Weekly P/L:          -0,134 %    [GRÜN — KW27 Mo-Basis = Fr-Close 100.025,35]
ATH:              100.066,47 $   DD: -0,176 % [GRÜN]
Käufe KW27:         0/2          (0 genutzt, 2 frei)
Pending Orders:     0
VIX (Spot):         18,41        [GRÜN <25 → 10 % Sizing erlaubt]
Crash-Filter:       NEIN         (SPY +1,16 % vs Fr-Close 729,35 → 737,80)
```

**Guardrails-Status alle 8 Hierarchien: GRÜN.**

**Positionen Live V1–V6 (Alpaca 09:33 ET):**
- JPM  329,31 $ (Entry 332,78, P/L -1,04 %, change_today +0,11 %) — V1 306,16 SICHER +7,53 % | V5 EMA50>EMA200 ✓ | V6 RSI ~55 / RS_4w ~+8 % → ALLE SICHER
- UNH  422,43 $ (Entry 401,57, P/L +5,20 %, change_today -1,27 %) — V1 369,44 SICHER +14,28 % | V2 Stop ~376,47 SICHER +12,21 % | V5 EMA50>EMA200 ✓ | V6 RSI ~73 / RS_4w ~+12 % → ALLE SICHER (RSI <80, RS positiv)

→ Keine Verkaufsorder. EMA50>EMA200 für beide intakt.

**Kandidaten-Scan K1–K5 (Alpaca IEX Close 26.06., Perplexity K5):**
- **LLY  Close 1.206,57** | K1 ✓ EMA50 1061,41>EMA200 973,76 | **K2 ✗ RSI 72,16 (>70 Overheat)** | K3 ✓ RS_63d +21,40 % (LLY +34,46 % vs SPY +13,06 %) | K4 ✓ Vol 222 % Avg20 | K5 ✓ FwdPE 32,39 + RevGrowth +55,5 % → **4/5 — K2 BLOCKS**
- **ELV  Close 395,20** | K1 ✓ EMA50 380,31>EMA200 343,77 | K2 ✓ RSI 51,93 | K3 ✓ RS_63d +21,28 % | K4 ✓ Vol 138 % Avg20 | **K5 ✗ FwdPE 14,8 ✓ aber RevGrowth Q1 2026 nur +1,5 % YoY (Perplexity, <10 %)** → **4/5 — K5 RevGrowth BLOCKS**
- **CAT  Close 998,18** | K1 ✓ K2 ✓ RSI 58,67 | K3 ✓ RS_63d +15,88 % | K4 ✓ Vol 220 % Avg20 | **K5 ✗ FwdPE 38,87–42,19 > 35 carry-over** → 4/5
- **CI   Close 282,39** | K1 ✓ knapp | K2 ✗ RSI 47,27 | K3 ✗ RS_63d -9,25 % | K4 ✓ → 2/4
- **COR  Close 286,08** | K1 ✗ EMA50<EMA200 | K2 ✓ | K3 ✗ RS_63d -23,10 % | K4 ✓ → 2/4
- **CRWD Close 700,04** | K1 ✓ | K2 ✓ RSI 60,50 | K3 ✓ RS_63d +52,13 % | K4 ✗ Vol 78 % | K5 vermutlich FAIL → 3/5

→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Lead-Kandidat LLY scheitert an K2 (RSI nach +7 % Gap-up und +0,84 % Folgetag im Overheat-Bereich). Backup ELV scheitert an K5 (RevGrowth Q1 2026 nur 1,5 % YoY — Health-Insurer-Sektor strukturell langsam). Pre-Market-Notiz "Falls LLY K5/K2 kippt: keine Pflicht zum Kauf" greift.

→ **KEIN Kauf heute.** 0/2 Slots KW27 genutzt. Watchlist Midday/Di: LLY (RSI-Cooldown abwarten), CAT (K5 Block), ELV (Watch — Earnings ~Mitte Juli könnte Wachstumsbild ändern), CRWD (Vol-Trigger).

**Sektor-Update:** Unverändert — XLF (JPM 0,99 %) + XLV (UNH 10,15 %). XLK weiter leer.

**ClickUp:** ROUTINE Normal-Alert Versuch (Prio 3 — alle GRÜN, kein Trade) — Tier-Limit-Issue bleibt möglich (carry-over von 26.06.).

> Entscheidung: KEIN Trade. Markt risk-on (SPY +1,16 %) bestätigt UNH-Trend. LLY-Setup ist fundamental top (K1/K3/K4/K5 alle ✓), aber RSI 72 = Overheat → diszipliniertes Warten. 2 Slots KW27 bleiben verfügbar.

---

### Wochenabschluss KW26 — 2026-06-26 (Fr)

```
Gesamtwert:       100.025,35 $   (Alpaca equity Fr-Close 16:00 ET)
Cash:              88.767,76 $   (88,75 %)
Investiert:        11.257,59 $   (11,25 %, JPM 985,59 $ + UNH 10.272,00 $)
Wochenrendite:    +0,063 %       (Mo-Basis 99.962,66 $ → Fr-Close 100.025,35 $; +62,69 $)
SPY Wochenrendite: -2,005 %      (Mo-Close 744,27 → Fr-Close 729,35 Alpaca IEX)
Alpha vs SPY:     +2,068 %       [POSITIV STARK — Cash-Schutz + UNH-Outperformance]
YTD Rendite:      +0,025 %       (vs Bot-Init 100.000 $ vom 31.05.26; nur 26 Kalendertage live)
SPY YTD 2026:    +7,523 %        (31.12.25 678,32 $ → 26.06.26 729,35 $)
YTD Alpha:        -7,498 %       (Bot 26 Tage live, Cash-Quote ~89 % verzichtet auf Marktbeta)
ATH:              100.066,47 $   (intraday 22.06. 09:37 ET, unverändert)
Drawdown vom ATH: -0,041 %       [GRÜN — Schwelle -15 % bei 85.057 $]
Offene Positionen: 2 / 8         (JPM XLF + UNH XLV)
Nächste Woche max. Käufe: 2  (Reset Mo 29.06.)
Watchlist KW27: LLY (Lead — K4 +217 %, K5-Recheck nach +7 %-Gap), ELV, CI, COR (XLV-Diversifikation), CAT (XLI — K5 bleibt blockierend)
```

**Trade-Aktivität KW26:**
- Käufe: 1 (AVGO Mo 22.06., partial 17/24 Sh @ 403,41 $)
- Verkäufe: 1 (AVGO V1-Stop Fr 26.06. @ 368,34 $)
- Stop-Loss-Trigger: 1 (AVGO V1 -8 %, Realisierter Verlust -596,19 $)
- Geschlossene Trades: 1 | Win-Rate: 0/1 (0 %) | Ø Haltedauer: 4 Handelstage
- Käufe-Limit: 1/2 genutzt (Slot ungenutzt nach AVGO-Stop, Markt risk-off → defensive Pause)

**Sektor-Check (Max 30 % vom investierten Kapital UND Gesamtdepot):**
- XLF (JPM):    985,59 $ →  8,76 % invest. /  0,99 % Gesamt → 1 Position [OK]
- XLV (UNH): 10.272,00 $ → 91,24 % invest. / 10,27 % Gesamt → 1 Position [OK auf Gesamtbasis]
- Hinweis: XLV-Schwergewicht entsteht durch kleine Sample-Größe (2 Positionen). Auf Gesamtdepot-Basis bleibt UNH unter 30 %. Bei LLY-Kauf nächste Woche würde XLV auf ~20 % Gesamtdepot steigen (UNH 10 % + LLY ~10 %) — innerhalb der 30 %-Grenze.

**Signal-Status Wochenschluss (V1–V6, Close 26.06.):**
- JPM 328,53 $ — V1 306,16 SICHER (+7,31 %) | V2 ~302,11 SICHER (+8,75 %) | V5 EMA50 ~312,1>EMA200 ~301,8 ✓ | V6 RSI ~55 / RS_4w ~+8,6 % → nicht ausgelöst
- UNH 428,00 $ — V1 369,44 SICHER (+15,85 %) | V2 ~376,47 SICHER (+13,68 %) | V5 EMA50 ~377,6>EMA200 ~334,1 ✓ | V6 RSI ~75 / RS_4w ~+12 % → nicht ausgelöst (RSI <80, RS positiv)
- Keine Verkaufsorder für Mo 29.06. vorbereitet.

**Sektor-Performance KW26 (Alpaca IEX 22.06.→26.06., vs SPY -2,01 %):**
- XLV: +6,79 % [Alpha +8,79 %] ← TOP-1 (Risk-off Health-Care Run, Versicherer-Schub)
- XLU: +3,28 % [Alpha +5,28 %] ← TOP-2 (Utilities defensiv)
- XLP: +3,08 % [Alpha +5,08 %] ← TOP-3 (Consumer Staples defensiv)
- XLRE: +2,73 % | XLB: +0,04 % | XLF: -0,24 % | XLI: -0,35 % | XLY: -0,39 % | XLE: -0,39 % | XLC: -0,78 %
- **XLK: -5,97 %** [Alpha -3,96 %] ← FLOP (Tech-Selloff — bestätigt AVGO V1-Stop-Logik)

**Strategie-Status:** STABIL — V1-Hard-Stop hat sauber gegriffen, keine Strategie-Anpassung. Sample-Size 26 Tage zu klein für Parameter-Adjust.

---

## Aktueller Stand (Close 16:00 ET 2026-06-26 Fr)

```
Gesamtwert:       100.025,35 $   (Alpaca equity Close)
Investiert:        11.257,59 $   (11,25 %, JPM 985,59 $ + UNH 10.272,00 $)
Cash:              88.767,76 $   (88,75 %)
Unrealisiert P/L:   +621,57 $    (JPM -12,75 $ / UNH +634,32 $)
Realisiert P/L:     -596,19 $    (AVGO V1 26.06.: 17 Sh × ($368,34 - $403,41) = -596,19 $)
Offene Positionen:      2 / 8
Pending Orders:         0
```

## Vor-Close-Stand (Midday 13:02 ET 2026-06-26 Fr)

```
Gesamtwert:        99.970,05 $   (Alpaca equity Live)
Investiert:        11.202,29 $   (11,21%, JPM 992,10 $ + UNH 10.210,80 $)
Cash:              88.767,76 $   (88,79%)
Unrealisiert P/L:   +566,88 $    (JPM -6,24 $ / UNH +573,12 $)
Realisiert P/L:     -596,19 $    (AVGO V1: 17 Sh × ($368,34 - $403,41) = -596,19 $)
Offene Positionen:      2 / 8
Pending Orders:         0
```

## Vor-Midday-Stand (Market Open 09:34 ET 2026-06-26 Fr — nach V1 AVGO Sell)

```
Gesamtwert:        99.817,78 $   (Alpaca equity Live)
Investiert:        11.050,02 $   (11,07%, JPM 1.004,85 $ + UNH 10.030,80 $ + AVGO 17 Sh verkauft)
Cash:              88.767,76 $   (88,92%)
Unrealisiert P/L:   +399,63 $    (JPM +6,51 $ / UNH +393,12 $)
Realisiert P/L:     -596,19 $    (AVGO V1: 17 Sh × ($368,34 - $403,41) = -596,19 $)
Offene Positionen:      2 / 8
Pending Orders:         0
```

## Vor-Sell-Stand (Close 16:00 ET 2026-06-25 Do)

```
Gesamtwert:        99.972,12 $   (Alpaca equity Close)
Investiert:        17.466,14 $   (17,47%, JPM 1.005,45 $ + UNH 9.983,52 $ + AVGO 6.477,17 $ Marktwert)
Cash:              82.505,98 $   (82,53%)
Unrealisiert P/L:    -27,85 $    (JPM +7,11 $ / UNH +345,84 $ / AVGO -380,80 $)
Realisiert P/L:         0,00 $
Offene Positionen:      3 / 8
Pending Orders:         0
```

## Vortags-Stand (Close 16:00 ET 2026-06-24 Mi) — Referenz

```
Gesamtwert:        99.772,92 $   (Alpaca equity Close)
Investiert:        17.266,94 $   (17,31%, JPM 1.003,44 $ + UNH 9.744,00 $ + AVGO 6.519,50 $ Marktwert)
Cash:              82.505,98 $   (82,69%)
Unrealisiert P/L:    -227,05 $   (JPM +5,10 $ / UNH +106,32 $ / AVGO -338,47 $)
```

---

## Performance-Tracking

```
Startkapital:     100.000,00 $  (2026-05-29 Alpaca / 2026-05-31 Bull Init)
All-Time-High:    100.066,47 $  (intraday 2026-06-22 09:37 ET — Open-Hoch)
Aktueller DD:        -0,041%    (100.025,35 vs ATH 100.066,47)
DD-Alarm bei:        -15,00%  → 85.057 $
DD-Stopp bei:        -20,00%  → 80.053 $

Performance heute:   +0,0999%  (equity 100.025,35 / last_equity 99.925,53 → +99,82 $)
SPY heute:           -0,5427%  (733,33 Do-Close → 729,35 Fr-Close, Alpaca IEX-Bar)
Alpha heute:         +0,6426%  [POSITIV — UNH +3,00 % treibt stark, JPM -1,97 % Tagesverlust kompensiert]
```

---

## Offene Positionen (Detail Close 16:00 ET 2026-06-26 Fr)

| Symbol | Qty | Entry    | Close 26.06.| Unreal. P/L | %      | Stop-Loss V1 | TP1/V3   | TP2/V4   |
|--------|-----|----------|-------------|-------------|--------|--------------|----------|----------|
| JPM    | 3   | 332,78 $ | 328,53 $    | -12,75 $    | -1,28% | 306,16 $     | 399,34 $ | 449,25 $ |
| UNH    | 24  | 401,57 $ | 428,00 $    | +634,32 $   | +6,58% | 369,44 $     | 481,88 $ | 542,12 $ |

---

## Risiko-Status (Close 16:00 ET 2026-06-26 Fr — Tagesabschluss KW26)

```
Daily P/L:            +0,0999%   [GRÜN — Limit: -3%]   (equity 100.025,35 / last 99.925,53)
Weekly P/L:           +0,0627%   [GRÜN — Limit: -5%]   (Mo-Basis 99.962,66 → +62,69 $ inkl. realisiertem AVGO-Verlust)
Käufe diese Woche:    1 / 2      (AVGO 22.06., gestoppt 26.06. — 1 Slot ungenutzt, KW26 abgeschlossen)
Verkäufe KW26:        1          (AVGO V1 26.06.)
VIX (Proxy VIXY):     22,60      (+0,49 % vs 22,49; Spot ~21,6 → <25 → 10 % Sizing, Filter inaktiv)
Crash-Filter aktiv:   NEIN       (SPY -0,54 % > -5 %)
VIX-Filter aktiv:     NEIN
Drawdown vom ATH:     -0,041%    [GRÜN] (ATH 100.066,47 $ vom 22.06.)
```

---

## Pending Orders

_Keine — AVGO V1-Sell (Order c5b9adf0) am 26.06. 09:33 ET 17/17 filled @ $368,34, Realisierter Verlust -596,19 $. JPM und UNH V1–V6 alle SICHER. Keine offenen Orders._

---

## Signal-Check Close 16:00 ET 2026-06-25 (V1–V6, kompletter Stand)

```
JPM @ 335,15 $  Close (Entry 332,78 $, P/L +0,71 %, change_today +0,51 %)
V1 Stop-Loss   -8%:   Trigger 306,16 $ — Close 335,15 → SICHER (+9,47 % Puffer)
V2 Trailing  -12%:    Hoch heute 343,31 → Stop ~302,11 → SICHER (+10,93 %)
V3 TP1      +20%:    Trigger 399,34 $ — nicht erreicht
V4 TP2      +35%:    Trigger 449,25 $ — nicht erreicht
V5 EMA50 > EMA200:    ~311,5 > ~301,5 → KEIN Death Cross (Spread ~+10,0 — Roll setzt sich fort)
V6 RSI>80 UND RS4w<0: RSI ~67 | RS_4w +10 % → NICHT ausgelöst

UNH @ 415,98 $  Close (Entry 401,57 $, P/L +3,59 %, change_today +2,51 %)
V1 Stop-Loss   -8%:   Trigger 369,44 $ — Close 415,98 → SICHER (+12,60 % Puffer)
V2 Trailing  -12%:    Hoch heute 417,54 → Stop ~367,43 → SICHER (+13,21 %)
V3 TP1      +20%:    Trigger 481,88 $ — nicht erreicht (+15,84 % bis Trigger)
V4 TP2      +35%:    Trigger 542,12 $ — nicht erreicht
V5 EMA50 > EMA200:    ~375,5 > ~333,2 → KEIN Death Cross (Spread ~+42,3 — komfortabel)
V6 RSI>80 UND RS4w<0: RSI ~70 (steigt nach +2,51 %) | RS_4w +>8 % → NICHT ausgelöst (RSI knapp unter 80, RS positiv)

AVGO @ 381,01 $  Close (Entry 403,41 $, P/L -5,55 %, change_today -0,28 %)
V1 Stop-Loss   -8%:   Trigger 371,14 $ — Close 381,01 → SICHER (+2,66 % Puffer) [KRITISCH — wieder enger vs. Mi]
V2 Trailing  -12%:    Hoch 414,63 (22.06. intraday) → Stop ~364,87 → SICHER (+4,42 %)
V3 TP1      +20%:    Trigger 484,09 $ — nicht erreicht
V4 TP2      +35%:    Trigger 544,61 $ — nicht erreicht
V5 EMA50 > EMA200:    ~397,4 > ~356,2 → KEIN Death Cross (Spread ~+41,2 — leicht enger, weiter intakt)
V6 RSI>80 UND RS4w<0: RSI ~46 | RS_4w ~-6 % → NICHT ausgelöst (RSI viel zu niedrig)
```

→ Keine Verkaufsorder für morgen. Alle 3 Positionen V1–V6 GRÜN.
→ AVGO V1-Puffer von 24.06.-Close +3,33 % auf +2,66 % zurück — change_today nur -0,28 %, aber Annäherung an Stop bleibt Watch-kritisch (Stop bei Last ≤ 371,14 automatisch).
→ UNH +2,51 % auf neues Posit-Hoch 417,54, Close 415,98 — Trailing-Stop ratscht auf 367,43 nach. P/L +3,59 % komfortabel.
→ JPM solide +0,51 %, intraday-Spike auf 343,31 deutlich über Close (Tagesvolatilität), schließt aber im Plus.

---

## Tagesbilanz-Log

**Close 2026-06-26 16:00 ET — Tagesbilanz KW26 Fr (Wochenabschluss):**
Gesamtwert:    100.025,35 $
Cash:           88.767,76 $  (88,75 %)
Investiert:     11.257,59 $  (11,25 %, MV)
P/L heute:        +99,82 $   (+0,0999 %)
Alpha vs SPY:   +0,6426 %     (SPY -0,5427 %; 733,33 Do-Close → 729,35 Fr-Close Alpaca IEX-Bar)
ATH:           100.066,47 $  (unverändert, intraday 22.06.)
Drawdown:        -0,041 %    [GRÜN]
Guardrails:     Daily +0,10 % | Weekly +0,063 % | Käufe 1/2 KW26 (1 ungenutzt) | Verkäufe 1 (AVGO V1) | VIXY 22,60 (Spot ~21,6, GRÜN) | Crash-Filter NEIN
Signal-Check Close (V1–V6 für JPM/UNH): alle SICHER, KEINE Verkaufsorder pending.
- JPM 328,53 (P/L -1,28 %, change_today -1,97 %): V1 306,16 SICHER +7,31 % | V2 Stop ~302,11 (Hoch 343,31) SICHER +8,75 % | V5 EMA50 ~312,1>EMA200 ~301,8 ✓ (Spread ~+10,3) | V6 RSI ~55 / RS_4w ~+8,6 % → NICHT ausgelöst
- UNH 428,00 (P/L +6,58 %, change_today +3,00 %, NEUES Posit-Hoch 427,81): V1 369,44 SICHER +15,85 % | V2 Stop ~376,47 SICHER +13,68 % | V5 EMA50 ~377,6>EMA200 ~334,1 ✓ (Spread ~+43,5 komfortabel) | V6 RSI ~75 (steigt) / RS_4w ~+12 % → NICHT ausgelöst (RSI <80)
Weekly Loss Cap geprüft: +0,063 % vs Mo-Basis 99.962,66 → weit über -5 %. Kein Sperrauslöser.
Kandidaten-Scan Watchlist Mo (K1–K4 via Alpaca IEX-Bars Close 26.06., K5 carry-over):
- LLY  Close 1.206,57 (+7,00 %!) | RS_63d ~+25–30 % stark | Vol 305,6k vs Avg20 ~141k = ~217 % [K4 STARK ✓] | K5 ✓ grenzwertig (34,91 carry-over) → 5/5 möglich (K2 RSI nach Gap-up ~67–70 prüfen), **LEAD-KANDIDAT MO**
- CAT  Close 998,18 (-5,53 % Pullback nach +6,28 % Do) | RS_63d weiter stark ~+30 % | Vol 294,8k vs Avg20 ~127k = ~232 % [K4 ✓] | K5 FAIL (FwdPE 38,87–42,19 > 35 carry-over) → 4/5 (K5 blockt)
- ANET Close 157,71 (-4,74 % Selloff) | RS_63d ~+3 % schwächer | Vol 560,5k = ~154 % aber Negativ-Vol [K4 grenzwertig] | K5 FAIL (44,13) → 3/5
- CRWD Close 700,04 (+3,16 % Bounce) | RS_63d ~+55 % stark | Vol 89,9k vs Avg20 ~117k = ~77 % FAIL [K4] | K5 vermutlich FAIL → 3/5
→ **LLY = Lead** für Pre-Market 29.06. Vol-Explosion 217 % deutlich >120 %, K5 carry-over grenzwertig OK. Earnings 07.08. → 42 Tage entfernt (kein Blackout).
→ Slot KW26 (1) verfällt heute (letzter Handelstag). KW27 Mo: 2 neue Slots.
Watchlist Mo (29.06.): LLY (Lead — K4 Vol +217 %, K5 Recheck am Open), CAT (K5 Block bleibt), CRWD (K4 schwach), ANET (Selloff, K5 FAIL).
Sektor-Lücke: XLK komplett leer nach AVGO-Stop (war 6,28 %). Bei nächstem Kauf XLK/Industrials/XLE-Diversifikation priorisieren — LLY würde 2. XLV nach UNH (OK ≤ 3 pro Sektor).
ClickUp TRADE_DAILY (Prio 4 wegen positivem P/L) — Versuch trotz heutiger Tier-Limit-Issues.

**Midday 13:02 ET 2026-06-26 (Fr, KW26):**
Positionen: 2/8 | Ø P/L: +2,66 % | Equity 99.970,05 $ (Cash 88.767,76 $ / Investiert MV 11.202,29 $)
Schlechteste Position: JPM -0,63 % (Last 330,70 $, V1 306,16 Puffer +8,01 % [SICHER], change_today -1,32 %)
Beste Position:        UNH +5,95 % (Last 425,45 $, V1 369,44 Puffer +15,17 % [SICHER], change_today +2,39 % — NEUES Posit-Hoch ≥425,45)
Stops: alle regulär — V1–V4 für JPM/UNH nicht ausgelöst (RSI/EMA bei Midday nicht geprüft).
V2 Trailing UNH: neues Hoch 425,45 → Stop ratscht auf ~374,40 (+13,57 % Puffer); JPM Hoch carry-over 343,31 → Stop ~302,11 (+9,47 %).
Daily P/L: +0,045 % [GRÜN — Limit -3 %] (equity 99.970,05 / last_equity 99.925,53)
Pending Orders: 0 | Käufe KW26: 1/2 (1 Slot ungenutzt — letzter Handelstag KW26)
> Kein ClickUp-Log (keine Stops, kein Daily-Cap). UNH zieht intraday +2,39 % auf neues Posit-Hoch; JPM gibt change_today -1,32 % ab, aber V1 weit weg. Nächste Routine: 16:00 ET Market Close.

**Market Open 2026-06-26 09:34 ET (Fr, KW26) — V1 STOP AVGO ausgelöst, KEIN Trade-Buy:**
Gesamtwert: 99.817,78 $ | Cash: 88.767,76 $ (88,92 %) | Investiert (MV): 11.050,02 $ (11,07 %)
Alpaca equity 99.817,78 vs. last_equity 99.925,53 → Daily P/L -0,108 % [GRÜN — Limit -3 %]
Weekly P/L: -0,145 % vs. Mo-Basis 99.962,66 [GRÜN — Limit -5 %] | ATH 100.066,47 | DD -0,249 % [GRÜN]
VIX (Proxy VIXY 09:33 ET): 23,36 → Spot ~22,3 [GRÜN <25 → 10 % Sizing erlaubt] | Crash-Filter NEIN (SPY 727,42 = -0,80 % vs Close 733,33)
Käufe KW26: 1/2 (AVGO 22.06. gestoppt heute — 1 Slot frei, aber Risk-off Pause) | Cash-Quote 88,92 % > 20 % Mindestreserve

**V1 STOP-LOSS — AVGO (Realisierter Verlust -596,19 $):**
- Trigger: Last $370,13 < V1 Stop $371,14 (Pre-Market-Puffer war bereits nur +0,16 %)
- Order: SELL 17 Sh AVGO @ Market → FILLED @ $368,34 avg, 09:33:28 ET (Order c5b9adf0)
- Entry $403,41 → Exit $368,34 = -35,07 $/Share × 17 = -596,19 $ (-8,69 %)
- Earnings-Blackout NEIN | V5 EMA50>EMA200 ✓ war zwar intakt, aber V1 ist hard-stop (kein Override)

**Positionen Live nach Sell (Alpaca 09:34 ET):**
- JPM  334,95 $ (Entry 332,78, P/L +0,65 %, V1 306,16 Puffer +9,48 %, change_today -0,05 %) [SICHER]
- UNH  417,95 $ (Entry 401,57, P/L +4,08 %, V1 369,44 Puffer +13,12 %, change_today +0,58 %) [SICHER — neues Posit-Hoch]
- AVGO 0 Sh — VERKAUFT V1 Stop

V1–V6 Live-Check für JPM/UNH: alle SICHER. EMA50>EMA200 carry-over. RSI/RS_4w unauffällig — kein V6-Trigger. Keine weitere Verkaufsorder.

**Kandidaten-Scan K1–K5 (Watchlist KW26, Live-Preise 09:33 ET):**
- CAT  Live 1.018,71 (-3,59 % vs Close 1.056,65 — Pullback nach Vortags-Vol-Explosion) | K5 carry-over FAIL (FwdPE >35) → 4/5 max, **K5 blockt**
- LLY  Live 1.145,81 (+1,61 % vs Close 1.127,63) | K4 gestern 83 % FAIL (Live-Vol erst spät belastbar) | K5 ✓ grenzwertig (34,91) → 4/5 (K4 schwach)
- ANET Live 157,09 (-5,11 % — Selloff nach gestern +2,29 %) | K5 carry-over FAIL (44,13) → 3/5
- CRWD Live 678,29 (-0,05 % flach) | K4 carry-over schwach (51 %) | K5 vermutlich FAIL → 3/5
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Plus: Markt risk-off (SPY -0,80 %, VIX +3,87 %) + frischer V1-Stop-Out AVGO → defensive Haltung.
→ **KEIN Kauf heute.** 1 Slot KW26 bleibt ungenutzt (letzter Handelstag KW26).

**Sektor-Update:** XLK (AVGO) jetzt 0 % → nur XLF (JPM 1,01 %) und XLV (UNH 10,05 %) belegt.
**ClickUp-Alert:** Critical Alert TRADE_SELL V1 STOP versucht — beide Lists 901218902459 und 901218902364 → "Max usage for custom task types reached" (ITEM_246). Mobile Push-Notification an User gesendet (Routine-Owner-Pfad).
**Lessons-Tag:** AVGO-Loss = erster realisierter Verlust seit Bot-Init 31.05. V1 hat sauber gegriffen — Pre-Market-Warnung +0,16 % Puffer trat exakt ein.
> Entscheidung: V1 vollzogen, KEIN Trade-Buy. Risk-off + frische Realisierung → Pause bis Pre-Market Mo 29.06. (oder MidDay 13:00 ET wenn Markt dreht). Watchlist Mo: CAT (K5-Block), LLY (K4 + Live-Vol), Sektor-Lücke XLK ggf. neu denken.

**Pre-Market 2026-06-26 08:30 ET (Fr, KW26):**
Gesamtwert: 99.819,55 $ | Cash: 82.505,98 $ (82,66 %) | Investiert (MV): 17.313,57 $ (17,34 %)
Alpaca equity 99.819,55 vs. last_equity 99.925,53 → Daily P/L -0,106 % [GRÜN — Limit -3 %]
ATH: 100.066,47 $ | DD vs. ATH: -0,247 % [GRÜN]
Weekly P/L: -0,143 % (vs. Mo-Basis 99.962,66) [GRÜN — Limit -5 %] | Käufe KW26: 1/2 (1 Slot frei — letzter Handelstag KW26)
VIX: 20,29 (+7,41 % vs Vortag — Vola steigt, aber <25 → 10 % Sizing erlaubt) | SPY Pre-Market: 730,32 $ Mid = -0,41 % vs Close 733,33 | 10Y: n/a (Perplexity)
Guardrails: alle GRÜN. Crash-Filter NEIN (SPY gestern +0,001 %). VIX-Filter NEIN (<25). DD-Alarm NEIN.
Positionen Live (Alpaca 08:32 ET):
- JPM  336,00 $   (Entry 332,78, P/L +0,97 %, V1 306,16 Puffer +9,75 %, change_today +0,26 %) [SICHER]
- UNH  416,10 $   (Entry 401,57, P/L +3,62 %, V1 369,44 Puffer +12,63 %, change_today +0,14 %) [SICHER]
- AVGO 371,72 $   (Entry 403,41, P/L -7,86 %, V1 371,14 Puffer +0,16 %, change_today -1,90 %) [KRITISCH HÖCHSTSTUFE — V1-Schwelle praktisch erreicht]
Earnings-Blackouts (Perplexity): keine (JPM 14.07., UNH ~Mitte Juli, AVGO ~Aug — alle carry-over) — kein Stop-Tightening.
Reconciliation: last_equity 99.925,53 vs. portfolio.md Close 25.06. 99.972,12 = -46,59 $ Settlement-Tick.
Makro 26.06.: U-Michigan Consumer Sentiment Final 10:00 ET (Perplexity); keine FOMC/PCE/GDP-Releases bestätigt.
> Entscheidung: Market-Open-Scan 09:30 ET JA — alle Guardrails GRÜN. ABER erhöhte Vorsicht wegen AVGO V1-Schwelle (+0,16 %) und SPY Pre-Market -0,41 %.
> Priorität HÖCHSTE Stufe: AVGO-V1-Stop-Watch. Bei Open ≤ 371,14 $ wird V1 Market-Order automatisch ausgelöst (17 Shares Verkauf).
> Watchlist KW26 (1 Slot, letzter Tag KW26): CAT (Lead — gestern Vol-Explosion 237 % +6,28 %, K5 FwdPE-Recheck Open zwingend), ANET (K4 nahe Trigger 111 %, K5 FAIL), LLY (K4 schwach 83 %), CRWD (K4 sehr schwach 51 %). Kauf nur bei vollem K1–K5.

**Close 2026-06-25 16:00 ET — Tagesbilanz KW26 Do:**
Gesamtwert:     99.972,12 $
Cash:           82.505,98 $  (82,53 %)
Investiert:     17.466,14 $  (17,47 %, MV)
P/L heute:       +231,40 $   (+0,232 %)
Alpha vs SPY:   +0,231 %     (SPY +0,001 %; 733,32 Mi-Close → 733,33 Do-Close Alpaca IEX-Bar)
ATH:           100.066,47 $  (unverändert, intraday 22.06.)
Drawdown:        -0,094 %    [GRÜN]
Guardrails:     Daily +0,23 % | Weekly +0,01 % | Käufe 1/2 KW26 | VIXY 22,49 (Spot ~21,5, GRÜN) | Crash-Filter NEIN
Signal-Check Close (V1–V6 für JPM/UNH/AVGO): alle SICHER, KEINE Verkaufsorder pending.
- JPM 335,15 (P/L +0,71 %, change_today +0,51 %): EMA50>EMA200 ✓ carry-over Roll | RSI ~67 | RS_4w +10 %; intraday-Hoch 343,31
- UNH 415,98 (P/L +3,59 %, change_today +2,51 %): EMA50>EMA200 ✓ | RSI ~70 (steigt) | RS_4w +>8 %; neues Posit-Hoch 417,54, Trailing-Stop rückt nach
- AVGO 381,01 (P/L -5,55 %, change_today -0,28 %): EMA50>EMA200 ✓ (Spread ~+41,2) | RSI ~46 | RS_4w ~-6 % [V1 Puffer +2,66 % — KRITISCH]
Weekly Loss Cap geprüft: +0,0095 % vs Mo-Basis 99.962,66 → weit über -5 %. Kein Sperrauslöser.
Kandidaten-Scan Watchlist morgen (K1–K4 via Alpaca IEX-Bars Close 25.06., K5 carry-over):
- CAT  Close 1.056,65 (+6,28 % — Vol-Explosion) | RS_63d Schub ~+34 % | Vol 296,3k vs Avg20 ~125k = ~237 % ✓ [K4 stark] | K5 FAIL carry-over (FwdPE 38,87–42,19 > 35) → 4/5 (K5 blockiert)
- LLY  Close 1.127,63 (+0,92 %) | RS_63d ~+12 % ✓ | Vol 117,3k vs Avg20 ~141k = ~83 % FAIL [K4] | K5 ✓ grenzwertig (FwdPE 34,91) → 3/5 (K4 schwach)
- ANET Close 165,56 (+2,29 %) | RS_63d ~+8 % ✓ | Vol 404,1k vs Avg20 ~364k = ~111 % grenzwertig [K4 nahe Trigger] | K5 FAIL carry-over (FwdPE 44,13) → 3/5
- CRWD Close 678,62 (+0,88 %) | RS_63d ~+50 % ✓ | Vol 59,2k vs Avg20 ~117k = ~51 % FAIL stark [K4] | K5 vermutlich FAIL → 3/5
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Slot KW26 bleibt 1 frei für Fr.
Watchlist morgen (26.06.): CAT (Lead — heute Vol-Explosion +237 %, K5 FwdPE-Recheck via Perplexity am Open zwingend), ANET (K4 nahe Trigger, K5 FAIL), LLY (K4 schwach), CRWD (K4 sehr schwach).
Perplexity SPY-Realtime: +0,77 % gemeldet (Pre-Market-Quelle inkonsistent — Datum-in-Zukunft-Problem). Alpaca IEX +0,001 % = Source of Truth.
ClickUp TRADE_DAILY (Prio 4 wegen positivem P/L) — Task wird angelegt.

**Midday 13:02 ET 2026-06-25:**
Positionen: 3/8 | Ø P/L: -0,38 % | Equity 99.942,90 $ (Cash 82.505,98 $ / Investiert MV 17.436,92 $)
Schlechteste Position: AVGO -5,64 % (Last 380,67 $, V1 371,14 Puffer +2,57 % [KRITISCH — Watch wieder verschärft vs. Open +3,62 %])
Beste Position:        UNH  +3,29 % (Last 414,76 $, V1 369,44 Puffer +12,27 %)
Mittel:                JPM  +1,21 % (Last 336,79 $, V1 306,16 Puffer +10,00 %)
Stops: alle regulär — V1–V4 für JPM/UNH/AVGO nicht ausgelöst (RSI/EMA bei Midday nicht geprüft).
Daily P/L: +0,203 % [GRÜN — Limit -3 %] (equity 99.942,90 / last_equity 99.740,72)
Pending Orders: 0 | Käufe KW26: 1/2
> Kein ClickUp-Log (keine Stops, kein Daily-Cap). AVGO V1-Puffer von Open +3,62 % auf jetzt +2,57 % verschlechtert (Last 380,67 vs. Open 384,57) — automatischer V1-Stop bei 371,14 $ greift bei Last ≤. UNH zieht intraday +2,21 % (414,76 vs lastday 405,80) — stärkster Tageswert. Nächste Routine: 16:00 ET Market Close.

**Market Open 2026-06-25 09:33 ET (Do, KW26) — KEIN TRADE:**
Gesamtwert: 99.924,28 $ | Cash: 82.505,98 $ (82,57 %) | Investiert (MV): 17.418,30 $ (17,43 %)
Alpaca equity 99.924,28 vs. last_equity 99.740,72 → Daily P/L +0,184 % [GRÜN — Limit -3 %]
Weekly P/L: -0,038 % vs. Mo-Basis 99.962,66 [GRÜN — Limit -5 %] | ATH 100.066,47 | DD -0,142 % [GRÜN]
VIX (Proxy VIXY 09:32 ET): 22,10 → Spot ~20,9 [GRÜN <25 → 10 % Sizing erlaubt] | Crash-Filter NEIN (SPY 737,54 = +0,576 % vs Close 733,32)
Käufe KW26: 1/2 (1 Slot frei, NICHT genutzt) | Cash-Quote 82,57 % > 20 % Mindestreserve
Positionen Live (Alpaca 09:32 ET):
- JPM  335,96 $ (Entry 332,78, P/L +0,96 %, V1 306,16 Puffer +9,73 %, change_today +0,75 %) [SICHER]
- UNH  411,37 $ (Entry 401,57, P/L +2,44 %, V1 369,44 Puffer +11,35 %, change_today +1,37 %) [SICHER]
- AVGO 384,57 $ (Entry 403,41, P/L -4,67 %, V1 371,14 Puffer +3,62 %, change_today +0,66 %) [ENTSPANNT — Erholung]
V1–V6 Live-Check für alle 3 Positionen: alle SICHER. EMA50>EMA200 carry-over (JPM ~311,3>~301,4; UNH ~375,1>~332,8; AVGO ~397,7>~355,8). RSI/RS_4w unauffällig — kein V6-Trigger. Keine Verkaufsorder platziert.
Kandidaten-Scan K1–K5 (Watchlist KW26 via Alpaca IEX-Bars Close 24.06., K5 carry-over verifiziert):
- CAT  Close 994,18 | EMA50 883,81>EMA200 684,07 (Spread +199,74) | RSI 62,61 | RS_63d +38,74 % vs SPY +12,27 % = +26,48 % | Vol 136,8k/Avg20 123,4k = 110,9 % | K1✓K2✓K3✓K4 ✗ (110,9 %) K5 FAIL (FwdPE 38,87/42,19 > 35 carry-over) → 3/5
- LLY  Close 1.117,35 | EMA50 1052,56>EMA200 962,58 | RSI 57,99 | RS_63d +23,73 % - SPY +12,27 % = +11,47 % | Vol 111,7k/Avg20 137,4k = 81,3 % | K1✓K2✓K3✓K4 ✗ K5 ✓ grenzwertig (FwdPE 34,91) → 4/5
- CRWD Close 672,72 | EMA50 604,23>EMA200 510,43 | RSI 54,74 | RS_63d +71,25 % - SPY +12,27 % = +58,98 % | Vol 37,7k/Avg20 116,9k = 32,3 % | K1✓K2✓K3✓K4 ✗ K5 vermutlich FAIL (Cloud-SaaS >35) → 3/5
- ANET Close 161,87 | EMA50 156,64>EMA200 144,03 | RSI 50,95 | RS_63d +23,76 % - SPY +12,27 % = +11,49 % | Vol 250,8k/Avg20 364,4k = 68,8 % | K1✓K2✓K3✓K4 ✗ K5 FAIL (FwdPE 44,13) → 3/5
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Slot KW26 (1/2) bleibt frei für Fr.
Markt-Kontext: SPY +0,576 % intraday (Risk-on, Pre-Market +0,78 % bestätigt sich teils), VIXY -3,24 % vs Close → Spot ~20,9 (entspannt). Intraday-Pops bei CAT +3,59 %, ANET +3,20 %, CRWD +2,02 % — Vol-Bilanz wird erst über volle Session belastbar.
Priorität bis 13:00 Midday-Check: AVGO Erholung weiter beobachten (V1 371,14 Puffer +3,62 % komfortabel). Kein manueller Eingriff.
ClickUp ROUTINE-Task wird gesendet (Prio 3 Normal — alle GRÜN, kein Stop-Alert).
> Entscheidung: KEIN Trade. AVGO-Erholung positiv. 1 Slot KW26 bleibt für Fr (letzter Handelstag KW26).

**Pre-Market 2026-06-25 08:30 ET (Do, KW26):**
Gesamtwert: 99.840,20 $ | Cash: 82.505,98 $ (82,64 %) | Investiert (MV): 17.334,22 $ (17,36 %)
Alpaca equity 99.840,20 vs. last_equity 99.740,72 → Daily P/L +0,0997 % [GRÜN — Limit -3 %]
ATH: 100.066,47 $ | DD vs. ATH: -0,226 % [GRÜN]
Weekly P/L: -0,123 % (vs. Mo-Basis 99.962,66) [GRÜN — Limit -5 %] | Käufe KW26: 1/2 (1 Slot frei)
VIX: 17,93 (-3,76 % vs 18,63 — deutlich entspannter vs Vortag 19,49 Spot) | SPY Pre-Market: 739,04 $ Mid = +0,78 % vs Close 733,32 | 10Y: n/a (Perplexity)
Guardrails: alle GRÜN. Crash-Filter NEIN. VIX-Filter NEIN (<25 → 10 % Sizing erlaubt). DD-Alarm NEIN.
Positionen Live (Alpaca 08:32 ET):
- JPM  334,02 $  (Entry 332,78, P/L +0,37 %, V1 306,16 Puffer +9,10 %, change_today +0,17 %) [SICHER]
- UNH  405,05 $  (Entry 401,57, P/L +0,87 %, V1 369,44 Puffer +9,64 %, change_today -0,18 %) [SICHER]
- AVGO 388,88 $  (Entry 403,41, P/L -3,60 %, V1 371,14 Puffer +4,78 %, change_today +1,78 %) [ENTSPANNT — Erholung gegenüber Close +3,33 %]
Earnings-Blackouts (Perplexity): keine (JPM 14.07. CONFIRMED, UNH 16.07., AVGO 29.08.) — kein Stop-Tightening.
Reconciliation: last_equity 99.740,72 vs. portfolio.md Close 24.06. 99.772,92 = -32,20 $ Settlement-Tick.
> Entscheidung: Market-Open-Scan 09:30 ET JA — alle Guardrails GRÜN, SPY Pre-Market +0,78 %, VIX 17,93 entspannt.
> Priorität: AVGO Erholungs-Watch (V1 371,14 $ Puffer +4,78 % komfortabel; Stop automatisch bei Last ≤).
> Watchlist KW26 (1 Slot): CAT (Lead-Kandidat K1–K4 ✓, K5 FwdPE >35 Block — Perplexity-Recheck am Open), LLY (K4 Vol-Trigger), CRWD (K4 schwach), ANET (K5 FAIL bleibt). Kauf nur bei vollem K1–K5.

**Close 2026-06-24 16:00 ET — Tagesbilanz KW26 Mi:**
Gesamtwert:     99.772,92 $
Cash:           82.505,98 $  (82,69 %)
Investiert:     17.266,94 $  (17,31 %, MV)
P/L heute:        -20,03 $   (-0,0201 %)
Alpha vs SPY:   +0,021 %     (SPY -0,041 %; 733,62 Di-Close → 733,32 Mi-Close Alpaca IEX-Bar)
ATH:           100.066,47 $  (unverändert, intraday 22.06.)
Drawdown:        -0,293 %    [GRÜN]
Guardrails:     Daily -0,02 % | Weekly -0,19 % | Käufe 1/2 KW26 | VIXY 22,84 (Spot ~21,6, GRÜN) | Crash-Filter NEIN
Signal-Check Close (V1–V6 für JPM/UNH/AVGO): alle SICHER, KEINE Verkaufsorder pending.
- JPM 334,48 (P/L +0,51 %, change_today +0,10 %): EMA50>EMA200 ✓ carry-over Roll | RSI ~66 | RS_4w +9,9 % (geschätzt)
- UNH 406,00 (P/L +1,10 %, change_today -0,79 %): EMA50>EMA200 ✓ | RSI ~61 (Cooldown) | RS_4w +6,5 %
- AVGO 383,50 (P/L -4,94 %, change_today +0,88 %): EMA50>EMA200 ✓ (Spread ~+41,9) | RSI ~45 | RS_4w ~-6 % [V1 Puffer +3,33 % — WATCH]
Weekly Loss Cap geprüft: -0,190 % vs Mo-Basis 99.962,66 → weit über -5 %. Kein Sperrauslöser.
Kandidaten-Scan Watchlist morgen (K1–K4 via Alpaca IEX-Bars Close 24.06., K5 carry-over):
- CAT  Close 994,18 (+0,99 %) | RS_63d weiter ~+29 % | Vol 136,8k vs Avg20 ~120k = 114 % ✓ | K5 FAIL (FwdPE 38,87–42,19 > 35 carry-over) → 4/5
- LLY  Close 1.117,35 (+0,86 %) | RS_63d ~+10 % ✓ | Vol 111,7k vs Avg20 ~141k = 79 % FAIL | K5 ✓ grenzwertig (FwdPE 34,91) → 3/5
- CRWD Close 672,72 (-1,15 %) | RS_63d ~+50 % ✓ | Vol 37,7k vs Avg20 ~144k = 26 % FAIL stark | K5 vermutlich FAIL → 3/5
- ANET Close 161,87 (-0,21 %) | RS_63d ~+7 % ✓ | Vol 250,7k vs Avg20 ~400k = 63 % FAIL | K5 FAIL (FwdPE 44,13) → 3/5
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Slot KW26 bleibt 1 frei für Do/Fr.
Watchlist morgen (25.06.): CAT (K4 weiter ≥120 %, K5 bleibt blockierend), LLY (K4 muss >120 % anziehen), CRWD (K4 sehr schwach).
Perplexity SPY-Realtime: +0,29 % gemeldet (Quelle inkonsistent — Datum-in-Zukunft-Problem). Alpaca IEX -0,04 % = Source of Truth.
ClickUp TRADE_DAILY (Prio 3 wegen negativem P/L) — Task wird angelegt.

**Midday 13:03 ET 2026-06-24:**
Positionen: 3/8 | Ø P/L: -1,19 % | Equity 99.778,01 $ (Cash 82.505,98 $ / Investiert MV 17.272,03 $)
Schlechteste Position: AVGO -4,70 % (Last 384,44 $, V1 371,14 Puffer +3,58 % [ENTSPANNT vs. 23.06.])
Beste Position:        UNH  +1,03 % (Last 405,72 $, V1 369,44 Puffer +9,84 %)
Mittel:                JPM  +0,11 % (Last 333,13 $, V1 306,16 Puffer +8,82 %)
Stops: alle regulär — V1–V4 für JPM/UNH/AVGO nicht ausgelöst (RSI/EMA bei Midday nicht geprüft).
Daily P/L: -0,015 % [GRÜN — Limit -3 %] (equity 99.778,01 / last_equity 99.792,95)
Pending Orders: 0 | Käufe KW26: 1/2
> Kein ClickUp-Log (keine Stops, kein Daily-Cap). AVGO-Erholung setzt sich fort (Puffer +3,58 % vs. +2,42 % Close 23.06.). Nächste Routine: 16:00 ET Market Close.

**Market Open 2026-06-24 09:33 ET (Mi, KW26) — KEIN TRADE:**
Gesamtwert: 99.936,82 $ | Cash: 82.505,98 $ (82,56 %) | Investiert (MV): 17.430,84 $ (17,44 %)
Alpaca equity 99.936,82 vs. last_equity 99.792,95 → Daily P/L +0,144 % [GRÜN — Limit -3 %]
Weekly P/L: -0,0258 % vs. Mo-Basis 99.962,66 [GRÜN — Limit -5 %] | ATH 100.066,47 | DD -0,130 % [GRÜN]
VIX (Proxy VIXY 09:32 ET): 22,80 → Spot ~21,8 [GRÜN <25 → 10 % Sizing erlaubt] | Crash-Filter NEIN (SPY 736,17 = +0,35 % vs Close 733,62)
Käufe KW26: 1/2 (1 Slot frei, NICHT genutzt) | Cash-Quote 82,56 % > 20 % Mindestreserve
Positionen Live (Alpaca 09:33 ET):
- JPM  333,69 $ (Entry 332,78, P/L +0,27 %, V1 306,16 Puffer +9,00 %, change_today -0,14 %) [SICHER]
- UNH  411,15 $ (Entry 401,57, P/L +2,39 %, V1 369,44 Puffer +11,28 %, change_today +0,46 %) [SICHER]
- AVGO 386,05 $ (Entry 403,41, P/L -4,30 %, V1 371,14 Puffer +4,02 %, change_today +1,55 %) [ENTSPANNT — Erholung aus KRITISCH]
V1–V6 Live-Check für alle 3 Positionen: alle SICHER. EMA50>EMA200 carry-over (JPM 310,36>301,07; UNH 373,84>332,04; AVGO 398,25>355,49). RSI/RS_4w unauffällig — kein V6-Trigger. Keine Verkaufsorder platziert.
Kandidaten-Scan K1–K5 (Watchlist KW26 via Alpaca-Bars bis Close 23.06., K5 carry-over verifiziert 23.06.):
- CAT  K1✓ K2✓ K3✓ (RS+28,34 %) K4✓ (Vol 175 % Avg20=112,6k) K5 FAIL (FwdPE 38,87/42,19 > 35 bestätigt) → 4/5
- LLY  K1✓ K2✓ K3✓ (RS+9,66 %)  K4 FAIL (Vol 134,6k vs Avg20 ~140,8k = 96 %) K5 ✓ grenzwertig (FwdPE 34,91) → 4/5
- CRWD K1✓ K2✓ K3✓ (RS+52,49 %) K4 FAIL (Vol 68,5k vs Avg20 ~144k = 48 %) K5 vermutlich FAIL (Cloud-SaaS >35) → max 3/5
- ANET K1✓ K2✓ K3✓ (RS+7,09 %) K4 FAIL (Vol 328k vs Avg20 ~400k = 82 %) K5 FAIL (FwdPE 44,13) → 3/5
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Slot KW26 (1/2) bleibt frei für Do/Fr.
Markt-Kontext: SPY +0,35 % intraday (Risk-on Erholung), VIXY -0,87 % → Spot ~21,8 (entspannt) → kein Aufrücken eines Kandidaten erwartet.
Priorität bis 13:00 Midday-Check: AVGO weiter beobachten (V1 371,14 $ Puffer +4,02 % — entspannter als 23.06., aber RS_4w noch -6,68 %). Kein manueller Eingriff.
ClickUp ROUTINE-Task gesendet (Prio 3 Normal — alle GRÜN, kein Stop-Alert).
> Entscheidung: KEIN Trade. AVGO-Erholung positiv. 1 Slot KW26 bleibt für besseres Setup Do/Fr.

**Pre-Market 2026-06-24 08:30 ET (Mi, KW26):**
Gesamtwert: 99.844,39 $ | Cash: 82.505,98 $ (82,63 %) | Investiert (MV): 17.338,41 $ (17,37 %)
Alpaca equity 99.844,39 vs. last_equity 99.792,95 → Daily P/L +0,0515 % [GRÜN — Limit -3 %]
ATH: 100.066,47 $ | DD vs. ATH: -0,222 % [GRÜN]
Weekly P/L: -0,118 % (vs. Mo-Basis 99.962,66) [GRÜN — Limit -5 %] | Käufe KW26: 1/2 (1 Slot frei)
VIX: ~19,3 (Spot Carry-over Perplexity; Close 23.06. 19,49) | SPY Pre-Market: 736,625 $ Mid = +0,41 % vs Close 733,62 | 10Y: n/a (Perplexity)
Guardrails: alle GRÜN. Crash-Filter NEIN. VIX-Filter NEIN (<25 → 10 % Sizing erlaubt). DD-Alarm NEIN.
Positionen Live (Alpaca 08:32 ET):
- JPM  334,40 $  (Entry 332,78, P/L +0,49 %, V1 306,16 Puffer +9,22 %) [SICHER]
- UNH  410,10 $  (Entry 401,57, P/L +2,12 %, V1 369,44 Puffer +11,01 %) [SICHER]
- AVGO 381,93 $  (Entry 403,41, P/L -5,33 %, V1 371,14 Puffer +2,90 %) [KRITISCH — V1-nah, change_today +0,47 %]
Earnings-Blackouts (Perplexity): keine (JPM 14.07., UNH 16.07., AVGO 29.08.) — kein Stop-Tightening.
Reconciliation: last_equity 99.792,95 vs. portfolio.md Close 23.06. 99.782,07 = +10,88 $ Settlement-Tick.
> Entscheidung: Market-Open-Scan 09:30 ET JA — alle Guardrails GRÜN, SPY Pre-Market positiv (+0,41 %), VIX <25.
> Priorität: AVGO-Stop-Watch (V1 371,14 $ wird automatisch ausgelöst bei Last ≤). Leichte Pre-Market-Erholung change_today +0,47 %.
> Watchlist KW26 (1 Slot): CAT (K5 Block FwdPE >35), LLY (Vol-Trigger-Watch), CRWD (Vol-Trigger-Watch). Kauf nur bei vollem K1–K5.

**Close 2026-06-23 16:00 ET — Tagesbilanz KW26 Di:**
Gesamtwert:     99.782,07 $
Cash:           82.505,98 $  (82,69 %)
Investiert:     17.276,09 $  (17,31 %, MV)
P/L heute:        -144,88 $  (-0,145 %)
Alpha vs SPY:   +1,286 %      (SPY -1,431 %; 744,27 Mo-Close → 733,62 Di-Close)
ATH:           100.066,47 $  (unverändert, intraday 22.06.)
Drawdown:        -0,284 %    [GRÜN]
Guardrails:     Daily -0,15 % | Weekly -0,18 % | Käufe 1/2 KW26 | VIXY 23,00 (Spot ~22, GRÜN) | Crash-Filter NEIN
Signal-Check Close (V1–V6 für JPM/UNH/AVGO): alle SICHER, KEINE Verkaufsorder pending.
- JPM 334,185 (P/L +0,41 %, intraday +0,80 %): EMA50 310,36 > 200 301,07 ✓ | RSI 67,53 | RS_4w +10,45 %
- UNH 409,65 (P/L +1,91 %, intraday +0,63 %): EMA50 373,84 > 200 332,04 ✓ | RSI 64,84 | RS_4w +7,40 %
- AVGO 380,13 (P/L -5,77 %, intraday -3,22 %): EMA50 398,25 > 200 355,49 ✓ | RSI 43,61 | RS_4w -6,68 % [V1 Puffer nur +2,42 % — KRITISCH]
Weekly Loss Cap geprüft: -0,181 % vs Mo-Basis 99.962,66 → weit über -5 %. Kein Sperrauslöser.
Kandidaten-Scan Watchlist morgen (K1–K4 via Alpaca IEX-Bars bis Close 23.06., K5 carry-over/Perplexity):
- CAT  K1✓ K2✓ K3✓ (RS_63d +28,34 %) K4✓ (Vol 175 %)  K5 FAIL (FwdPE 38,87–42,19 > 35 bestätigt) → 4/5
- LLY  K1✓ K2✓ K3✓ (RS_63d +9,66 %)  K4 FAIL (Vol 96 %) K5 ✓ grenzwertig (FwdPE 34,91) → 4/5
- CRWD K1✓ K2✓ K3✓ (RS_63d +52,49 %) K4 FAIL (Vol 56 %) K5 vermutlich FAIL (Cloud-SaaS typ. >35) → max 3/5
- ANET K1✓ K2✓ K3✓ (RS_63d +7,09 %)  K4 FAIL (Vol 84 %) K5 FAIL bestätigt (FwdPE 44,13) → 3/5
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Slot KW26 bleibt 1 frei.
Watchlist morgen (24.06.): CAT (K4 stark, K5 weiter blockierend), LLY (Vol-Trigger abwarten), CRWD (Vol-Trigger).
Perplexity SPY/VIX-Realtime nicht verfügbar (Datum in Zukunft) → Alpaca IEX als Quelle of Truth.
ClickUp TRADE_DAILY (Prio 3 wegen negativem P/L) — Task wird angelegt.

**Midday 13:03 ET 2026-06-23:**
Positionen: 3/8 | Ø P/L: -1,06 % | Equity 99.800,28 $ (Cash 82.505,98 $ / Investiert MV 17.294,30 $)
Schlechteste Position: AVGO -4,97 % (Last 383,35 $, V1 371,14 Puffer +3,19 % [knapp])
Beste Position:        UNH  +1,43 % (Last 407,315 $, V1 369,44 Puffer +9,30 %)
Mittel:                JPM  +0,35 % (Last 333,94 $,  V1 306,16 Puffer +8,32 %)
Stops: alle regulär — V1–V4 für JPM/UNH/AVGO nicht ausgelöst (RSI/EMA bei Midday nicht geprüft).
Daily P/L: -0,127 % [GRÜN — Limit -3 %] (equity 99.800,28 / last_equity 99.926,95)
Pending Orders: 0 | Käufe KW26: 1/2
> Kein ClickUp-Log (keine Stops, kein Daily-Cap). AVGO weiterhin priorisiert für Close-Check. Nächste Routine: 16:00 ET Market Close.

**Market Open 2026-06-23 09:36 ET (Di, KW26) — KEIN TRADE:**
Gesamtwert: 99.710,67 $ | Cash: 82.505,98 $ (82,75 %) | Investiert (MV): 17.204,69 $ (17,25 %)
Alpaca equity 99.710,67 vs. last_equity 99.926,95 → Daily P/L -0,216 % [GRÜN — Limit -3 %]
Weekly P/L: -0,252 % vs. Mo-Basis 99.962,66 [GRÜN — Limit -5 %] | ATH 100.066,47 | DD -0,356 % [GRÜN]
VIX (Carry-over PreMarket): 19,81 [GRÜN <30; <25 → 10 % Sizing erlaubt] | Crash-Filter NEIN (SPY -1,57 % > -5 %)
Käufe KW26: 1/2 (1 Slot frei, NICHT genutzt) | Cash-Quote 82,75 % > 20 % Mindestreserve
Positionen Live (Alpaca 09:33 ET):
- JPM  327,75 $ (Entry 332,78, P/L -1,45 %, V1 306,16 Puffer +7,05 %) [SICHER]
- UNH  405,29 $ (Entry 401,57, P/L +0,93 %, V1 369,44 Puffer +9,71 %) [SICHER]
- AVGO 382,06 $ (Entry 403,41, P/L -5,30 %, V1 371,14 Puffer +2,94 %) [KRITISCH — knapp über Stop]
V1–V6 Live-Check für alle 3 Positionen: alle SICHER. EMA50>EMA200 für alle 3 (JPM 309,56>304,91 Spread schmal). RSI/RS_4w unauffällig (kein V6 mit RSI>80 + RS<0). Keine Verkaufsorder platziert.
Kandidaten-Scan K1–K5 (Watchlist KW26 mit Alpaca-Bars bis Mo 22.06.):
- LLY  K1✓ K2✓ K3✓ (RS+6,77 %) K4 92 % FAIL  K5✓ grenzwertig → 4/5
- ANET K1✓ K2✓ K3✓ (RS+18,25 %) K4 109 % FAIL  K5 offen → max 4/5
- CRWD K1✓ K2✓ K3✓ (RS+50,37 %) K4 95 % FAIL  K5 offen → max 4/5
- CAT  K1✓ K2✓ K3✓ (RS+35,37 %) K4 136 % ✓  K5 FAIL (FwdPE 38,87 > 35 carry-over) → 4/5
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Kein Kauf ausgeführt.
Markt-Kontext: SPY -1,57 % intraday (Risk-off), VIX im Anstieg → "Kauf nur bei sehr starkem Setup"-Bedingung aus PreMarket bestätigt nicht erfüllt.
Priorität bis 13:00 Midday-Check: AVGO-Stop-Watch. V1 371,14 $ wird automatisch ausgelöst — kein manueller Eingriff.
ClickUp ROUTINE-Task gesendet (Prio 2 High wegen AVGO-Stop-Nähe): 869duymnz.
> Entscheidung: KEIN Trade. Beobachtung AVGO. 1 Slot KW26 bleibt für besseres Setup Mi/Do/Fr.

**Pre-Market 2026-06-23 08:30 ET (Di, KW26):**
Gesamtwert: 99.660,80 $ | Cash: 82.505,98 $ (82,79 %) | Investiert (MV): 17.155,39 $ (17,21 %)
Alpaca equity 99.660,80 vs. last_equity 99.926,95 → Daily P/L -0,266 % [GRÜN — Limit -3 %]
ATH: 100.066,47 $ | DD vs. ATH: -0,406 % [GRÜN]
Weekly P/L: -0,302 % (vs. Mo-Basis 99.962,66) [GRÜN — Limit -5 %] | Käufe KW26: 1/2 (1 Slot frei)
VIX: 19,81 (steigend von 16,8) | SPY Pre-Market: 733,98 $ = -1,40 % vs. Mo-Close 744,27 | 10Y: 4,488 %
Guardrails: alle GRÜN. Crash-Filter NEIN. VIX-Filter NEIN (<25 → 10 % Sizing erlaubt). DD-Alarm NEIN.
Positionen Live (Alpaca):
- JPM  331,00 $  (Entry 332,78, P/L -0,54 %, V1 306,16 Puffer +8,11 %) [SICHER]
- UNH  407,60 $  (Entry 401,57, P/L +1,50 %, V1 369,44 Puffer +10,32 %) [SICHER]
- AVGO 375,29 $  (Entry 403,41, P/L -6,97 %, V1 371,14 Puffer +1,12 %) [KRITISCH — knapp über Stop]
Earnings-Blackouts: keine (JPM 14.07., UNH 16.07., AVGO 03.09.) — kein Stop-Tightening.
Reconciliation: last_equity 99.926,95 vs. portfolio.md Close 22.06. 99.935,22 = -8,27 $ Settlement-Tick.
> Entscheidung: Market-Open-Scan 09:30 ET JA — alle Guardrails GRÜN, ABER erhöhte Vorsicht wegen SPY-Premarket -1,40 % und VIX-Anstieg.
> Priorität: AVGO-Stop-Watch. Bei Last ≤ 371,14 $ wird V1-Market-Order ausgelöst (kein manueller Eingriff).
> Watchlist KW26 (1 Slot): LLY, ANET, CRWD, CAT — Kauf nur bei sehr starkem Setup. K5-Fundamentals teils noch zu verifizieren.

**Close 2026-06-22 16:00 ET — Tagesbilanz KW26 Mo:**
Gesamtwert:     99.935,22 $
Cash:           82.505,99 $  (82,56%)
Investiert:     17.429,23 $  (17,44%)
P/L heute:        -27,44 $   (-0,0275%)
Alpha vs SPY:   +0,304%       (SPY -0,331%; Fr Juneteenth → Vergleich Do-Close 746,74 → Mo-Close 744,27)
ATH:           100.066,47 $   (intraday-Open 22.06. 09:37 ET, unverändert)
Drawdown:        -0,131%      [GRÜN]
Guardrails:     Daily -0,03% | Weekly -0,03% | Käufe 1/2 KW26 | VIX ~16,8 | Crash-Filter NEIN
Signal-Check Close (V1–V6 für alle 3 Positionen): alle SICHER, keine Verkaufsorder pending.
- JPM 331,92 (P/L -0,26%): EMA50 309,57>200 307,40 | RSI 66,15 | RS_4w +9,34%
- UNH 406,07 (P/L +1,12%): EMA50 374,21>200 334,49 | RSI 61,90 | RS_4w +5,96%
- AVGO 393,40 (P/L -2,48%, -4,36% intraday): EMA50 399,74>200 358,71 | RSI 46,63 | RS_4w -5,32% (negativ → Watch)
Weekly Loss Cap geprüft: -0,028% vs Mo-Basis 99.962,66 → weit über -5%. Kein Sperrauslöser.
Watchlist Di 23.06.: LLY (XLV, K1–K5 ✓ grenzwertig, RS +6,56%) | ANET (XLK, K1–K3 ✓ RSI 58,9 RS+11,3%) | CRWD (XLK, K1–K3 ✓ RSI 58,2 RS+46,8%, K5 prüfen) | CAT (XLI, K1–K4 ✓, K5 FwdPE alt 38,87 → verifizieren).
ClickUp TRADE_DAILY (Prio 3 wegen negativem P/L) — Task wird angelegt.

**Midday 13:03 ET 2026-06-22:**
Positionen: 3/8 | Ø P/L: -0,09 % | Equity 100.050,51 $ (Cash 82.505,99 $ / Investiert 17.544,52 $)
Schlechteste Position: AVGO -1,59 % (Last 396,98 $, V1 371,14 Puffer +6,96 %)
Beste Position:        UNH +1,73 % (Last 408,52 $, V1 369,44 Puffer +9,57 %)
Mittel:                JPM -0,40 % (Last 331,465 $, V1 306,16 Puffer +8,26 %)
Stops: alle regulär — V1–V4 für JPM/UNH/AVGO nicht ausgelöst (RSI/EMA bei Midday nicht geprüft).
Daily P/L: +0,088 % [GRÜN — Limit -3 %] (equity 100.050,51 / last_equity 99.962,66)
Pending Orders: 0 | Käufe KW26: 1/2
> Kein ClickUp-Log (keine Stops, kein Daily-Cap). Nächste Routine: 16:00 ET Market Close.

**Market Open 2026-06-22 09:34 ET — KAUF AVGO:**
Gesamtwert: 100.066,47 $ | Cash: 82.505,99 $ (82,5%) | Investiert: 17.560,48 $ (17,5%)
Equity 100.066,47 / last_equity 99.962,66 → Intraday P/L +0,104% [GRÜN]
Positionen: 3/8 (JPM 3 Sh, UNH 24 Sh, AVGO 17 Sh) | Käufe KW26: 1/2
ATH: 100.012,97 $ → neuer Hoch-Aspirant (Equity 100.066 leicht über ATH; ATH-Update separat im Close-Eintrag)
Guardrails: Daily +0,10% | Weekly +0,10% | VIX 16,8 (<25 → 10% Sizing) | Crash-Filter NEIN | DD GRÜN
Scan-Ergebnis: AVGO (XLK, RS+15,4%, K1–K5 ✓) gekauft; CAT K5 FAIL (FwdPE 38,87 > 35); LLY K5 grenzwertig (FwdPE 34,91) aber RS schwächer (+6,56%).
Order: Limit $413.41 → Fill 17/24 @ $403.41 avg (Partial), 7 verbleibende Shares nach 2 Min canceled (Alpaca-Simulator stuck).
Stop V1 AVGO: $371,14 (-8%) | V3 $484,09 (+20%) | V4 $544,61 (+35%).
ClickUp TRADE_BUY (Prio 3): 869duc9ne.

**Signal-Check Live 09:37 ET (V1–V6 für alle 3 Positionen):**
- JPM 327,76 $ (+0,78% intraday): V1 306,16 SICHER | V2 SICHER | V3/V4 nicht erreicht
- UNH 406,09 $ (+1,28% intraday): V1 369,44 SICHER | V2 SICHER | V3/V4 nicht erreicht
- AVGO 402,03 $ (-2,27% vs Vortag, -0,34% vs Entry): V1 371,14 SICHER | V2 SICHER (Hoch=Entry, kein Trailing-Trigger) | V3/V4 nicht erreicht
→ Keine Verkaufsorder offen.

**Pre-Market 2026-06-22 08:30 ET:**
Gesamtwert: 99.959,81 $ | Cash: 89.363,96 $ (89,4 %) | Investiert: 10.595,85 $ (10,6 %)
Alpaca equity 99.959,81 vs. last_equity 99.962,66 → Daily P/L -0,003 % [GRÜN]
ATH: 100.012,97 $ | DD: -0,053 % [GRÜN]
Guardrails: Daily -0,003 % | Weekly Reset (KW26 startet, neue Mo-Basis 99.962,66 $) | Käufe 0/2 | VIX ~17,4 Spot (16,78 Fr Close) | Crash-Filter NEIN | DD-Alarm NEIN
SPY Pre-Market 747,80 $ Mid (+0,14 % vs Fr 746,74) | 10Y Treasury n/a (Perplexity-Realtime unzureichend)
JPM 326,19 $ (-2,03 % vs Entry 332,78, V1 306,16 Puffer +6,2 %) | UNH 400,72 $ (-0,21 % vs Entry 401,57, V1 369,44 Puffer +8,5 %)
Earnings-Blackouts: keine (JPM 14.07., UNH 16.07. — kein Stop-Tightening)
> Entscheidung: Market-Open-Scan JA — alle Guardrails GRÜN. Watchlist KW26: AVGO (Top), CAT (Vol-Trigger), LLY (XLV-Konflikt UNH).

### Wochenabschluss KW25 — 2026-06-19 (Fr, Juneteenth Holiday)

```
Gesamtwert:        99.962,66 $   (Alpaca equity, = last_equity, kein Trade-Tick)
Cash:              89.363,96 $   (89,4 %)
Investiert:        10.598,70 $   (10,6 %  — JPM 975,66 $ + UNH 9.623,04 $)
Wochenrendite:     -0,037 %      (Mo 100.000,00 → Fr 99.962,66)
SPY Wochenrendite: -1,003 %      (Mo 15.06. 754,31 → Do 18.06. 746,74; Fr Holiday)
Alpha vs SPY:      +0,966 %      [POSITIV — getragen von 89 % Cash bei schwacher Marktwoche]
"YTD" Rendite:     -0,037 %      (Bot lebt seit 31.05.; volle YTD-Zahl nicht vergleichbar)
SPY YTD 2026:     +10,09 %       (31.12.25 678,32 → 18.06.26 746,74)
ATH:              100.012,97 $   (intraday Open 2026-06-18)
Drawdown vom ATH: -0,050 %       [GRÜN — Schwelle -15 % bei 85.011 $]
Offene Positionen: 2 / 8
Nächste Woche max. Käufe: 2  (Reset Mo 22.06.)
Watchlist KW26: AVGO (Top-Pick), CAT (Trigger-Watch), evtl. LLY (XLV-Konflikt UNH beachten)
```

**Trade-Aktivität KW25:**
- Käufe: 2 (JPM Mi 17.06., UNH Do 18.06.) — Wochen-Limit 2/2 erreicht
- Verkäufe: 0 | Stop-Loss-Trigger: 0 | Death-Cross-Trigger (V5): 0 | RSI-Überkauft (V6): 0
- Geschlossene Trades: 0 | Win-Rate diese Woche: n/a | Ø Haltedauer geschlossen: n/a
- Handelstage: 3 von 5 (Fr Juneteenth)

**Sektor-Check (Max 30 % vom investierten Kapital, Max 3 Pos./Sektor):**
- XLF (JPM):  975,66 $ → 9,21 % invest. / 0,98 % Gesamt   → 1 Position    [OK]
- XLV (UNH): 9.623,04 $ → 90,79 % invest. / 9,63 % Gesamt → 1 Position    [OK]
- Hinweis: Schwergewicht XLV (90,79 % invest.) entsteht durch nur 2 Positionen und
  unterschiedliche Sizing-Skalen — bei wachsendem Portfolio normalisiert sich das.
  Kein Verstoß gegen 30 %-Regel auf Gesamtdepot-Basis.

**Signal-Status Wochenschluss (carry-over aus Do 18.06. Close, V1–V6):**
- JPM Close 326,02 $ — V1 306,16 SICHER | V2 SICHER | V3/V4 nicht erreicht | V5 EMA50>EMA200 ✓ | V6 RSI 62,1 / RS+6,96 % → nicht ausgelöst
- UNH Close 400,96 $ — V1 369,44 SICHER | V2 SICHER | V3/V4 nicht erreicht | V5 EMA50>EMA200 ✓ | V6 RSI 58,7 / RS+3,95 % → nicht ausgelöst
- Keine Verkaufsorder für Mo 22.06. vorbereitet.

**Strategie-Status:** STABIL — keine Anpassung nötig (Sample-Size erst 19 Tage).

---

**Close 2026-06-19 16:00 ET — HANDELSFEIERTAG (Juneteenth), No-Op:**
NYSE/Nasdaq geschlossen ganztägig (Alpaca clock: is_open=false, next_open Mo 2026-06-22 09:30 ET).
Equity 99.962,66 $ = last_equity (kein Trade-Tick seit Vortags-Close). Cash 89.363,96 $ (89,4%) | Investiert 10.598,70 $ (10,6%).
JPM 3 Sh @ 325,22 $ (-22,68 $ / -2,27% — change_today 0,00%) | UNH 24 Sh @ 400,96 $ (-14,64 $ / -0,15% — change_today 0,00%).
Daily P/L: 0,00% [GRÜN] | Weekly P/L: -0,037% [GRÜN] | DD vs. ATH 100.012,97 $: -0,050% [GRÜN] | Käufe 2/2 (LIMIT).
SPY/VIX/Alpha: nicht erhebbar (Markt zu, keine Daily-Bar). Alpha-Berechnung übersprungen.
V1–V6 Live-Check übersprungen — letzter belastbarer Stand vom 18.06. Close: alle SICHER, EMA50>EMA200 für JPM und UNH, RSI 62,1 / 58,7. Keine Limit-Order vorbereitet.
Watchlist Mo 22.06. (Carry-over): AVGO (Top-Pick K1–K4 ✓), CAT (Industrials, RS+30), NVDA (Tech), LLY (XLV — bereits UNH gehalten), GS (XLF — Konflikt JPM).
Weekly Loss Cap geprüft: -0,037 % vs. Mo-Basis 100.000 $ → weit über -5 %. Kein Sperrauslöser.
ClickUp-Report: übersprungen (Holiday — Pre-Market-Notification 869dtg866 bereits abgesetzt; CLICKUP_LIST_ID-Bug-Workaround dokumentiert).
> Entscheidung: Keine Order, keine Memory-Migration über Holiday-Snapshot hinaus. Nächste echte Routine: Pre-Market Mo 2026-06-22 08:30 ET.

**Market Open 2026-06-19 09:30 ET — HANDELSFEIERTAG (Juneteenth):**
NYSE/Nasdaq geschlossen (Alpaca clock: is_open=false, next_open 2026-06-22 09:30 ET).
Alpaca-Kalender 18.06.→22.06.→23.06., 19.06. nicht enthalten → kein Handelstag.
Snapshot (kein Trade möglich): Gesamt 99.962,66 $ | Cash 89.363,96 $ (89,4%) | Investiert 10.598,70 $ (10,6%)
JPM: 3 Sh, current 325,22 $, unreal -22,68 $ (-2,27%) | UNH: 24 Sh, current 400,96 $, unreal -14,64 $ (-0,15%)
Daily P/L 0,00% [GRÜN] | Weekly -0,037% [GRÜN] | DD -0,050% [GRÜN] | Käufe 2/2
Schritt 2 Guardrail-Check obsolet (Markt zu) — kein Stop-Check live möglich, V1/V2 anhand Last Trade (Vortagsschluss): JPM 306,16 $ SICHER (+6,2%), UNH 369,44 $ SICHER (+8,5%).
> Entscheidung: Keine Order. Routine pausiert bis Mo 22.06. Pre-Market 08:30 ET.

**Midday 13:02 ET 2026-06-19 — HANDELSFEIERTAG (Juneteenth):**
NYSE/Nasdaq geschlossen (Alpaca clock: is_open=false, next_open Mo 2026-06-22 09:30 ET).
Positionen: 2/8 | Ø P/L: -1,21 % | Equity 99.962,66 $ = last_equity (kein Trade-Tick).
Schlechteste Position: JPM -2,27 % (Last 325,22 $, V1-Puffer +6,2 %)
Beste Position:        UNH -0,15 % (Last 400,96 $, V1-Puffer +8,5 %)
Stops: alle SICHER — V1–V4 nicht prüfbar live (Markt zu), Last-Trade-Basis OK.
Daily P/L: 0,00 % [GRÜN — Limit -3 %] | Pending Orders: 0 | Cash 89.363,96 $
> No-Op-Routine: kein Live-Check, kein ClickUp-Log, keine Order. Nächste echte Stop-Prüfung Mo 22.06. 09:30 ET.

**Pre-Market 2026-06-19 08:30 ET:**
Gesamtwert: 99.962,66 $ | Cash: 89.363,96 $ (89,4%) | Investiert: 10.598,70 $ (10,6%)
Alpaca equity = last_equity (kein Trade seit Close) → Daily P/L 0,00 % [GRÜN]
ATH: 100.012,97 $ | DD: -0,050 % [GRÜN]
Guardrails: Daily 0,00 % | Weekly -0,037 % | Käufe 2/2 (LIMIT) | VIX 16,4–17,0 | Crash-Filter: NEIN
SPY: 746,75 Close, After-Hours-Tick 748,46 (+0,23%)
JPM 325,22 (-2,27 % vs Entry, V1 Puffer +6,2%) | UNH 400,96 (-0,15 %, V1 Puffer +8,5%)
Earnings-Blackouts: keine (JPM 14.07., UNH 16.07.)
> Entscheidung: KEIN Kaufscan heute (2/2). Nur Stop-Check & Halten bis Mo 22.06.

**Close 2026-06-18 16:00 ET:**
Gesamtwert: 99.965,07 $ | Cash: 89.363,97 $ (89,4%) | Investiert: 10.601,10 $ (10,6%)
P/L heute: -36,96 $ (-0,0370%) | Alpha vs. SPY: -0,810% (SPY +0,773%)
ATH: 100.012,97 $ | DD: -0,0479% [GRÜN]
Guardrails: Daily -0,037% | Weekly -0,035% | Käufe 2/2 | VIX (Open) 17,10 | Crash-Filter: NEIN
Signal-Check: V1–V6 für JPM und UNH unauffällig — keine Verkaufsorder pending.
Watchlist 19.06.: AVGO (Tech, K1–K4 ✓), GS (Fin, RS+22), CAT (Indust., RS+30), NVDA (Tech), LLY (Health)
> Käufe 2/2 erreicht → morgen KEINE Käufe, nur Beobachtung & Stop-Check.

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
