# Trade Log

**Bot:** Bull | **Startkapital:** 100.000 $ | **Modus:** Paper Trading (Alpaca)

---

## Offene Positionen

| Symbol | Kaufdatum  | Kaufkurs    | Live-Mark 06.07. 09:43 | Gewinn/Verlust      | Stop-Loss   | TP1         | TP2         | Signale         |
|--------|------------|-------------|------------------------|---------------------|-------------|-------------|-------------|-----------------|
| JPM    | 2026-06-17 | 332,78 $    | 338,77 $               | +17,97 $ (+1,80%)   | 306,16 $    | 399,34 $    | 449,25 $    | K1✓K2✓K3✓K4✓K5✓ |
| UNH    | 2026-06-18 | 401,57 $    | 417,61 $               | +384,96 $ (+3,99%)  | 369,44 $    | 481,88 $    | 542,12 $    | K1✓K2✓K3✓K4✓K5✓ |
| MU     | 2026-07-02 | 1.037,72 $  | 1.001,58 $             | -325,31 $ (-3,48%)  | 954,71 $    | 1.245,26 $  | 1.400,92 $  | K1✓K2✓K3✓K4✓K5✓ |
| LLY    | 2026-07-06 | 1.193,89 $  | 1.190,16 $             | -29,82 $ (-0,31%)   | 1.098,38 $  | 1.432,66 $  | 1.611,75 $  | K1✓K2✓K3✓K4✓K5✓ |

**Gesamt investiert:** 29.574,93 $ (Marktwert Alpaca 06.07. 09:43 ET) | **Cash:** 69.877,15 $ | **Positionen:** 4/8 | **Käufe KW28:** 1/2 (LLY FILLED)

---

## Offene Orders (pending)

| Symbol | Side | Type | Qty | Limit | TIF | Status | Placed | Order-ID |
|--------|------|------|-----|-------|-----|--------|--------|----------|
| —      | —    | —    | —   | —     | —   | —      | —      | —        |

_LLY-Limit-Order **GEFILLT 09:42:49 ET** (8/8 Sh @ avg 1.193,89 $, Fill-Zeit nur 1:49 min nach Order-Submit vs MU 35 min). Investiert 9.551,10 $ (9,60 % Portfolio). Stop-Loss V1 auf 1.098,38 gesetzt (-8 % vom Fill). Sektor XLV Total 19,65 % (UNH 10,08 % + LLY 9,57 %) unter 30 %-Cap. Guardrails alle GRÜN._

_Nächster Check: 13:00 ET Midday Stop-Check (V1–V4 alle 4 offenen Positionen). Käufe KW28 1/2 → 1 Slot frei bis Fr._

---

## Geschlossene Trades

| Symbol | Kauf       | Verkauf    | Einstieg | Ausstieg | Ergebnis $ | Ergebnis % | Grund          |
|--------|------------|------------|----------|----------|------------|------------|----------------|
| AVGO   | 2026-06-22 | 2026-06-26 | 403,41 $ | 368,34 $ | -596,19 $  | -8,69 %    | V1 Stop-Loss   |

**Realisierter Gewinn/Verlust:** -596,19 $ | **Win-Rate:** 0/1 (0 %) | **Avg. Gewinn:** — | **Avg. Verlust:** -596,19 $

---

## Trades

### KAUF (filled): LLY am 2026-07-06
- Limit-Order:    $1.216,84 (Day, +0,5 % über Vortagesschluss $1.210,79 = Do 02.07. Close; Fr 03.07. NYSE-Feiertag)
- Order-Submit:   09:41 ET, Fill 09:42:49 ET (**1 min 49 sec — sehr schneller Fill**, vs MU 02.07. 35min)
- Fill:           8/8 Shares @ **$1.193,8875 avg** (deutlich unter Limit — Aggressiv-Ask war 1.199,52 auf IEX, tatsächliche Ausführung besser)
- Menge:          8 Shares
- Investiert:     **9.551,10 $** (9,60 % Portfolio bei Fill)
- Stop-Loss V1:   **$1.098,38** (-8 % vom Fill 1193,89)
- Trailing V2:    **$1.050,62** (-12 % vom Posit-Hoch = Fill-Preis, kein neues Hoch nach Fill)
- TP1 / V3:       **$1.432,66** (+20 % → 50 % verkaufen)
- TP2 / V4:       **$1.611,75** (+35 % → Rest verkaufen)
- Kaufsignale (Alpaca Bars + Perplexity 06.07.):
  - K1 ✓ EMA50 1.089,02 > EMA200 987,10 (Spread +101,92 — Golden Cross breit)
  - K2 ✓ RSI(14) 64,34 (Wilder-Smoothing volle 200d-History, im 50–70-Fenster)
  - K3 ✓ RS_63d LLY +28,22 % vs SPY +14,07 % → **+14,16 % RS** (2. höchste RS unter allen K5-grünen Kandidaten)
  - K4 ✓ Live-Vol 09:37 ET 6.451 Sh / Avg20 148.232 → 7-min-Projektion 242 % Avg20 >> 120 % Hürde
  - K5 ✓ Multi-Source Perplexity 06.07.:
    - FwdPE 34,51 [intellectia.ai 04.07.] / 32,69 [valueinvesting.io] / 32,53 [finbox] → **Median ~32,7 ≤ 35 ✓**
    - RevGrowth Q1 2026 YoY: **+47,43 %** [Perplexity source 8] → ≥ 10 % ✓
- Sektor:         XLV Healthcare — 2. XLV-Position mit UNH; Sektor-Gewicht nach Fill **19,65 %** (UNH 10,08 % + LLY 9,57 %) unter 30 %-Cap, 2/3 XLV-Positionen
- Earnings:       Q2 2026 **05.08.2026 BMO** Multi-Source verifiziert (MarketBeat + LLY Investor-Relations Webcast + MarketChameleon + Nasdaq/Zacks) → 22 HT ab heute → 3-HT-Blackout erst ab 31.07. Close → **KEIN Blackout aktiv**
- Status nach Fill 09:43 ET: Live 1.190,16 $ (P/L -0,31 %, change_today -1,96 %); V1 1.098,38 SICHER (+8,35 % Puffer); V2 1.050,62 (Posit-Hoch = Fill 1.193,89) SICHER (+13,28 %); V3/V4 weit entfernt
- Alpaca Order-ID: f6364db0-8a8f-4a11-b305-26a4874f1f6d

### KAUF (filled): MU am 2026-07-02
- Limit-Order:    $1.037,80 (Day, +0,5 % über Vortagesschluss $1.032,64)
- Fill:           9/9 Shares @ $1.037,72 avg um 10:17:09 ET (Fill 4h35m nach Order-Submit 09:42 ET; Pullback ins Limit erfolgt)
- Menge:          9 Shares
- Investiert:     9.339,48 $ (~9,34 % Portfolio)
- Stop-Loss V1:   $954,71 (-8 % vom Fill)
- Trailing V2:    $913,39 (-12 % vom Posit-Hoch 1.037,94 = Fill-Preis, kein neues Hoch nach Fill)
- TP1 / V3:       $1.245,26 (+20 % → 50 % verkaufen)
- TP2 / V4:       $1.400,92 (+35 % → Rest verkaufen)
- Kaufsignale:    K1✓ EMA50 877,31 > EMA200 458,31 | K2✓ RSI 51,82 | K3✓ RS_63d +191,24 % vs SPY | K4✓ IEX-Cumvol-Projektion 319 % Avg20 | K5✓ FwdPE Yahoo 6,73 / MarketBeat 10,41 / TTM 23,7 (alle ≤35) + RevGrowth Q3 FY2026 +56 % (≥10 %)
- Sektor:         XLK Technology / Semiconductors — füllt Lücke (JPM XLF, UNH XLV, XLK vorher leer)
- Earnings:       Q4 FY2026 typisch Ende September 2026 → KEIN 3-HT-Blackout aktiv
- Status Fill:    Live nach Fill 10:17 ET: sofortiger Intraday-Drop, 13:06 ET 976,71 $ (-5,85 % Position-PnL)
- Status Close 02.07.: 978,00 $ Close (change_today -5,26 %, P/L -5,75 % vs Entry, Tagestief 950,31 / Tageshoch 1.064,59); V1 954,71 SICHER **nur +2,38 % Puffer** [KRITISCH]; V2 Stop 913,39 (Posit-Hoch 1.037,94 post-fill) SICHER (+6,61 %); V5 EMA50 882,15 > EMA200 507,23 ✓ (Spread +374,92 — Golden Cross sehr breit, kein Death-Cross-Risiko kurzfristig); V6 RSI(14) 48,57 / RS_4w vs SPY -8,42 % → NICHT ausgelöst (V6 benötigt BEIDES: RSI>80 UND RS<0; RS ist negativ, RSI aber weit unter 80)
- Alpaca Order-ID: 6c45f431-facd-4979-8c01-d0976e2f2474
- ClickUp Task:   nicht angelegt (Tier-Limit ITEM_246 carry-over) — Push-Notification an Owner gesendet

### VERKAUF (V1 Stop-Loss filled): AVGO am 2026-06-26
- Trigger:        Last $370,13 < V1 Stop $371,14 um 09:32 ET (Pre-Market-Puffer war bereits nur +0,16 %)
- Order:          Market Order Sell 17 Sh Day, eingereicht 09:32:36 ET
- Fill:           17/17 Sh @ $368,34 avg um 09:33:28 ET (~1 min nach Order)
- Erlös:          6.261,78 $
- Entry:          $403,41 (Kauf 22.06.) → Exit $368,34 = -35,07 $/Share
- Ergebnis:       **-596,19 $ realisiert (-8,69 %)**
- Grund:          V1 Stop-Loss -8 % vom Entry (Schwelle $371,14, durchbrochen Open Fr 26.06.)
- Markt-Kontext: SPY -0,80 % intraday, VIXY +3,87 %, Risk-off-Open nach Risk-on-Vortag
- Begleitwerte:   V5 EMA50 ~397>EMA200 ~356 ✓ (intakt — V1 ist hard-stop, kein Override durch V5)
- Earnings:       2026-09-03 (>2 Monate entfernt — kein Blackout-Effekt)
- Alpaca Order-ID: c5b9adf0-229d-4330-9f75-9672674b946f
- ClickUp Task:   nicht angelegt (Tier-Limit ITEM_246 "Max usage for custom task types reached") — Push-Notification an Owner gesendet

### KAUF (partial filled): AVGO am 2026-06-22
- Limit-Order:    $413.41 (Day, +0,5% über Vortagesschluss $411.35)
- Fill:           17/24 Shares @ $403.41 avg (09:36 ET, Tail nach 2 min steckend → 7 Shares manuell canceled)
- Investiert:     6.857,97 $ (~6,85% Portfolio — unter 10%-Ziel wegen Partial-Fill)
- Stop-Loss V1:   $371.14 (-8% vom Fill 403,41)
- Trailing V2:    -12% vom Hoch (Tracking ab heute)
- TP1 / V3:       $484.09 (+20% → 50% verkaufen)
- TP2 / V4:       $544.61 (+35% → Rest verkaufen)
- Kaufsignale:    K1✓ EMA50 400.00 > EMA200 360.25 | K2✓ RSI 51.33 | K3✓ RS_63d +15.43% vs SPY | K4✓ Vol 130% Avg20 | K5✓ FwdPE 34.0–35.6 (Median ~34.2) + Rev YoY +51.47%
- Sektor:         XLK Technology / Semiconductors — kein Konflikt mit JPM (XLF) / UNH (XLV)
- Earnings:       2026-09-03 (73 Tage entfernt, kein Blackout)
- Live 09:37 ET:  current 402,03 $, P/L -0,34%, V1–V4 nicht ausgelöst
- Status Close 22.06.: 393,40 $ (intraday -4,36%, -2,48% vs Entry); V1 371,14 SICHER +6,00% Puffer; V2 Stop ~364,87 (Hoch 414,63) SICHER; V5 EMA50 399,74>EMA200 358,71 ✓; V6 RSI 46,63 / RS_4w -5,32% (negativ — Watch ab Di)
- Status Open 23.06. 09:33 ET: 382,06 $ Live, -5,30% Position-PnL; V1 371,14 SICHER nur +2,94% Puffer [KRITISCH]; V2 Stop ~364,87 SICHER (+4,71%); V5 EMA50 399,69>EMA200 362,55 ✓ (Spread schmaler); V6 RSI 46,42 / RS_63d +11,51%
- Status Close 23.06.: 380,13 $ Close (intraday -3,22 %, -5,77 % vs Entry); V1 371,14 SICHER +2,42 % Puffer [KRITISCH]; V2 Stop ~364,87 SICHER (+4,18 %); V5 EMA50 398,25>EMA200 355,49 ✓ (Spread +42,76); V6 RSI 43,61 / RS_4w -6,68 % (negativ — Watch bleibt)
- Status Open 24.06. 09:33 ET: 386,05 $ Live, -4,30 % Position-PnL (change_today +1,55 %); V1 371,14 SICHER +4,02 % Puffer [ENTSPANNT — Erholung]; V2 Stop ~364,87 SICHER (+5,82 %); V5/V6 carry-over (EMA50>EMA200 ✓)
- Status Close 24.06.: 383,50 $ Close (change_today +0,88 %, P/L -4,94 % vs Entry); V1 371,14 SICHER +3,33 % Puffer [WATCH — leichte Verschlechterung vs. Open]; V2 Stop ~364,87 SICHER (+5,11 %); V5 EMA50 ~397,7>EMA200 ~355,8 ✓ (Spread ~+41,9); V6 RSI ~45 / RS_4w ~-6 % → NICHT ausgelöst
- Status Close 25.06.: 381,01 $ Close (change_today -0,28 %, P/L -5,55 % vs Entry); V1 371,14 SICHER +2,66 % Puffer [KRITISCH — wieder verengt vs. 24.06.-Close +3,33 %]; V2 Stop ~364,87 SICHER (+4,42 %); V5 EMA50 ~397,4>EMA200 ~356,2 ✓ (Spread ~+41,2); V6 RSI ~46 / RS_4w ~-6 % → NICHT ausgelöst
- Alpaca Order-ID: ab4a9c16-3424-4721-b243-08328adaa341
- ClickUp Task:   869duc9ne

### KAUF (filled): UNH am 2026-06-18
- Limit-Order:    $401.57 (Day, +0,5% über Vortagesschluss $399.57)
- Fill:           $401.57 (vor Midday 13:02 ET; Retracement zum Limit erfolgt)
- Menge:          24 Shares
- Investiert:     9.637,68 $ (~9,6% Portfolio)
- Stop-Loss V1:   $369.44 (-8% vom Fill)
- Trailing V2:    -12% vom Hoch (Tracking ab heute)
- TP1 / V3:       $481.88 (+20% → 50% verkaufen)
- TP2 / V4:       $542.12 (+35% → Rest verkaufen)
- Kaufsignale:    K1✓ EMA50 370,76>EMA200 333,10 | K2✓ RSI 57,7 | K3✓ RS +28,57% vs SPY 63d | K4✓ Vol 135% Avg20 | K5✓ FwdP/E 30,63 + Rev+18,63% YoY
- Sektor:         Health Care (XLV) — kein Konflikt mit JPM (Financials/XLF)
- Earnings:       2026-07-16 (28 Tage entfernt, kein Blackout)
- Status Midday 18.06.: 402,07 $ Kurs, +0,12% Position-PnL, V1–V4 nicht ausgelöst
- Status Close 18.06.: 400,96 $ Close, -0,15% Position-PnL, V1–V6 nicht ausgelöst (EMA50 372,91 > EMA200 335,16; RSI 58,7; RS_4w +3,95%)
- Status Close 22.06.: 406,07 $ Close, +1,12% Position-PnL (+1,27% intraday); V1 369,44 SICHER +9,92%; V5 EMA50 374,21>EMA200 334,49 ✓; V6 RSI 61,90 / RS_4w +5,96%
- Status Open 23.06. 09:33 ET: 405,29 $ Live, +0,93% Position-PnL; V1 369,44 SICHER +9,71%; V5 EMA50 374,21>EMA200 329,25 ✓; V6 RSI 63,26 / RS_63d +32,79%
- Status Close 23.06.: 409,65 $ Close, +1,91 % Position-PnL (intraday +0,63 %); V1 369,44 SICHER +10,88 %; V5 EMA50 373,84>EMA200 332,04 ✓; V6 RSI 64,84 / RS_4w +7,40 %
- Status Open 24.06. 09:33 ET: 411,15 $ Live, +2,39 % Position-PnL (change_today +0,46 %); V1 369,44 SICHER +11,28 %; V5/V6 carry-over (EMA50>EMA200 ✓)
- Status Close 24.06.: 406,00 $ Close (change_today -0,79 %, P/L +1,10 % vs Entry); V1 369,44 SICHER +9,89 % Puffer; V2 Stop ~361,81 (Hoch ~411,15) SICHER; V5 EMA50 ~375,1>EMA200 ~332,8 ✓ (Spread ~+42,3); V6 RSI ~61 (Cooldown) / RS_4w ~+6,5 % → NICHT ausgelöst
- Status Close 25.06.: 415,98 $ Close (change_today +2,51 %, P/L +3,59 % vs Entry); V1 369,44 SICHER +12,60 % Puffer; V2 Stop ~367,43 (neues Posit-Hoch 417,54) SICHER (+13,21 %); V5 EMA50 ~375,5>EMA200 ~333,2 ✓ (Spread ~+42,3 komfortabel); V6 RSI ~70 (steigt) / RS_4w +>8 % → NICHT ausgelöst (RSI knapp unter 80)
- Status Close 26.06.: 428,00 $ Close (change_today +3,00 %, P/L +6,58 % vs Entry, NEUES Posit-Hoch 427,81); V1 369,44 SICHER +15,85 % Puffer; V2 Stop ~376,47 (Hoch heute 427,81) SICHER (+13,68 %); V5 EMA50 ~377,6>EMA200 ~334,1 ✓ (Spread ~+43,5 sehr komfortabel); V6 RSI ~75 (steigt nach +3 %) / RS_4w ~+12 % → NICHT ausgelöst (RSI <80, RS positiv)
- Status Close 29.06.: 420,00 $ Close (change_today -1,84 %, P/L +4,59 % vs Entry, Cooldown vom Fr-Hoch); V1 369,44 SICHER +13,67 % Puffer; V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over vom 26.06., kein neues Hoch heute) SICHER (+11,55 %); V5 EMA50 381,82 > EMA200 340,19 ✓ (Spread +41,63 sehr komfortabel); V6 RSI 64,15 (Cooldown von ~75) / RS_4w +12,43 % → NICHT ausgelöst (RSI <80, RS positiv)
- Status Open 30.06. 09:32 ET: 419,255 $ Live (change_today -0,195 %, P/L +4,40 % vs Entry); V1 369,44 SICHER +13,48 % Puffer; V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over, kein neues Hoch) SICHER (+11,36 %); V5 EMA50 381,82 > EMA200 340,19 ✓ (carry-over); V6 RSI ~64 / RS_4w +12,43 % → NICHT ausgelöst
- Status Close 30.06.: 415,54 $ Close (change_today -1,019 %, P/L +3,48 % vs Entry, Tagestief 413,385 / Tageshoch 422,51 → kein neues Posit-Hoch); V1 369,44 SICHER +12,47 % Puffer; V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over vom 26.06.) SICHER (+10,38 %); V5 EMA50 383,13 > EMA200 339,23 ✓ (Spread +43,90 sehr komfortabel); V6 RSI(14) 60,6 / RS_4w +10,94 % → NICHT ausgelöst (RSI <80, RS positiv)
- Status Open 01.07. 09:37 ET: 416,36 $ Live (change_today +0,20 %, P/L +3,68 % vs Entry); V1 369,44 SICHER +12,71 % Puffer; V2 Stop ~376,47 (Posit-Hoch 427,81 carry-over) SICHER (+10,71 %); V5 EMA50 383,13 > EMA200 339,23 ✓ (carry-over); V6 RSI 60,6 / RS_4w +10,94 % → NICHT ausgelöst
- Status Close 01.07.: 426,52 $ Close (change_today +2,63 %, P/L +6,21 % vs Entry, NEUES Posit-Hoch 428,01 heute — Tageshoch); V1 369,44 SICHER +15,45 % Puffer; V2 Stop **NEU 376,65** (Trail nach neuem Hoch 428,01) SICHER (+13,24 %); V5 EMA50 391,55 > EMA200 347,22 ✓ (Spread +44,33 sehr komfortabel, Golden Cross weiter ausgebaut); V6 RSI(14) 63,46 / RS_4w +14,68 % → NICHT ausgelöst (RSI <80, RS positiv). Sektor-Move XLV +2,6 % (ELV +7,6 % EPS-Beat).
- Status Close 02.07.: 424,28 $ Close (change_today -0,53 %, P/L +5,66 % vs Entry, NEUES Posit-Hoch 430,095 heute); V1 369,44 SICHER +12,93 % Puffer; V2 Stop **NEU 378,48** (Trail nach neuem Hoch 430,095, vorher 376,65) SICHER (+10,79 %); V5 EMA50 385,12 > EMA200 342,87 ✓ (Spread +42,25 sehr komfortabel); V6 RSI(14) 64,76 / RS_4w vs SPY +13,97 % → NICHT ausgelöst (RSI <80, RS positiv). Cooldown nach Rekord-Vortag, aber Posit-Hoch weiter hoch getrailt.
- Alpaca Order-ID: b9674f87-9cad-4ac0-a39f-756157f8b5ed

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
- Status Close 18.06.: $326,02 Tagesschluss, -2,03% Position-PnL, V1–V6 nicht ausgelöst (EMA50 308,67 > EMA200 307,35; RSI 62,1; RS_4w +6,96%)
- Status Close 22.06.: $331,9175 Tagesschluss, -0,26% Position-PnL (+2,06% intraday); V1 306,16 SICHER +8,42%; V5 EMA50 309,57>EMA200 307,40 ✓ (Spread schmal); V6 RSI 66,15 / RS_4w +9,34%
- Status Open 23.06. 09:33 ET: 327,75 $ Live, -1,45% Position-PnL; V1 306,16 SICHER +7,05%; V5 EMA50 309,56>EMA200 304,91 ✓ (Spread weiterhin schmal); V6 RSI 65,65 / RS_63d +0,90%
- Status Close 23.06.: 334,185 $ Close, +0,41 % Position-PnL (intraday +0,80 %); V1 306,16 SICHER +9,16 %; V5 EMA50 310,36>EMA200 301,07 ✓ (Spread +9,30 leicht weiter); V6 RSI 67,53 / RS_4w +10,45 %
- Status Open 24.06. 09:33 ET: 333,69 $ Live, +0,27 % Position-PnL (change_today -0,14 %); V1 306,16 SICHER +9,00 %; V5/V6 carry-over (EMA50>EMA200 ✓)
- Status Close 24.06.: 334,48 $ Close (change_today +0,10 %, P/L +0,51 % vs Entry); V1 306,16 SICHER +9,25 % Puffer; V5 EMA50 ~311,3>EMA200 ~301,4 ✓ (Spread ~+9,9); V6 RSI ~66 / RS_4w ~+9,9 % → NICHT ausgelöst
- Status Close 25.06.: 335,15 $ Close (change_today +0,51 %, P/L +0,71 % vs Entry); V1 306,16 SICHER +9,47 % Puffer; V2 Stop ~302,11 (Hoch heute 343,31) SICHER (+10,93 %); V5 EMA50 ~311,5>EMA200 ~301,5 ✓ (Spread ~+10,0 Roll setzt sich fort); V6 RSI ~67 / RS_4w ~+10 % → NICHT ausgelöst
- Status Close 26.06.: 328,53 $ Close (change_today -1,97 %, P/L -1,28 % vs Entry, Tagestief 327,50 nahe Schluss); V1 306,16 SICHER +7,31 % Puffer; V2 Stop ~302,11 (Posit-Hoch 343,31 vom 25.06.) SICHER (+8,75 %); V5 EMA50 ~312,1>EMA200 ~301,8 ✓ (Spread ~+10,3 stabil); V6 RSI ~55 (Drop nach -1,97 %) / RS_4w ~+8,6 % → NICHT ausgelöst
- Status Close 29.06.: 331,39 $ Close (change_today +0,71 %, P/L -0,42 % vs Entry, Erholung nach Fr-Schwäche); V1 306,16 SICHER +8,23 % Puffer; V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over) SICHER (+9,69 %); V5 EMA50 313,62 > EMA200 307,76 ✓ (Spread +5,86 leicht weiter); V6 RSI 60,10 / RS_4w +12,11 % → NICHT ausgelöst (RSI <80)
- Status Open 30.06. 09:32 ET: 329,29 $ Live (change_today +0,008 % flat, P/L -1,05 % vs Entry); V1 306,16 SICHER +7,55 % Puffer; V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over) SICHER (+9,00 %); V5 EMA50 313,62 > EMA200 307,76 ✓ (carry-over); V6 RSI ~60 / RS_4w +12,11 % → NICHT ausgelöst
- Status Close 30.06.: 327,24 $ Close (change_today -0,659 %, P/L -1,67 % vs Entry, Open 329,24 / Tageshoch 330,42 / Tagestief 326,725; XLF-Lag nach „financials lagged on lower-rate expectations"-News); V1 306,16 SICHER +6,89 % Puffer; V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over) SICHER (+8,28 %); V5 EMA50 314,15 > EMA200 308,78 ✓ (Spread +5,37, knapper als 29.06.); V6 RSI(14) 57,6 / RS_4w +11,86 % → NICHT ausgelöst (RSI <80, RS positiv)
- Status Open 01.07. 09:37 ET: 326,29 $ Live (change_today -0,29 %, P/L -1,95 % vs Entry, Intraday-Range 325,12 / 328,79); V1 306,16 SICHER +6,58 % Puffer; V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over) SICHER (+8,00 %); V5 EMA50 314,15 > EMA200 308,78 ✓ (carry-over); V6 RSI 57,6 / RS_4w +11,86 % → NICHT ausgelöst
- Status Close 01.07.: 334,06 $ Close (change_today +2,08 % Financials-Rebound, P/L +0,38 % vs Entry, Tageshoch 335,59 / Tagestief 325,12); V1 306,16 SICHER +9,11 % Puffer; V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over) SICHER (+10,51 %); V5 EMA50 316,48 > EMA200 308,96 ✓ (Spread +7,52 leicht geweitet); V6 RSI(14) 65,18 / RS_4w +12,80 % → NICHT ausgelöst (RSI <80, RS positiv). Perplexity: „JPMorgan Chase +3,30 %" Sektor-Rebound-Signal.
- Status Close 02.07.: 334,47 $ Close (change_today +0,12 %, P/L +0,51 % vs Entry, Tageshoch 337,89 / Tagestief 331,97 — kein neues Posit-Hoch vs 343,31); V1 306,16 SICHER +8,46 % Puffer; V2 Stop ~302,11 (Posit-Hoch 343,31 carry-over 25.06.) SICHER (+9,68 %); V5 EMA50 315,32 > EMA200 306,00 ✓ (Spread +9,32 stabil); V6 RSI(14) 62,83 / RS_4w vs SPY +12,30 % → NICHT ausgelöst (RSI <80, RS positiv).
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

| Woche | Depot-Start | Depot-Ende | Wochenergebnis | vs. SPY | Alpha | Käufe / Verkäufe / Stops |
|-------|-------------|------------|----------------|---------|-------|--------------------------|
| 2026-W25 | 100.000,00 $ (Mo 15.06.) | 99.962,66 $ (Fr 19.06. Holiday → Do 18.06. Close) | -0,037 % | -1,003 % | +0,966 % | 2 / 0 / 0 |
| 2026-W26 | 99.962,66 $ (Mo-Basis 22.06.) | 100.025,35 $ (Fr 26.06. Close) | +0,063 % | -2,007 % (SPY 744,27→729,35) | +2,070 % | 1 / 1 (AVGO V1) / 0 |
| 2026-W27 | 100.024,25 $ (Mo-Basis 29.06. = Fr-Close 26.06.) | 99.420,34 $ (Fr 03.07. NYSE-Feiertag → carry-over Do 02.07. Close) | -0,604 % | +2,127 % (SPY 729,35→744,86 Do 02.07.) | -2,731 % | 1 / 0 / 0 |
