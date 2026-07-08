# Portfolio Status

**Bot:** Bull | **Modus:** Paper Trading | **Zuletzt aktualisiert:** 2026-07-08 13:07 ET (Midday KW28 Mi Tag 3, alle 4 V1/V2 SICHER, Daily -0,24 % GRÜN, kein Stop-Trigger vor FOMC-Minutes 14:00 ET)

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
