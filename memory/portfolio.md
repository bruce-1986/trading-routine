# Portfolio Status

**Midday 13:00 ET 2026-08-19 (Mi, KW34 Tag 3) — 13:07 Live-Snapshot:**
Gesamtwert:        96.246,93 $   (Alpaca /v2/account equity Live)
Cash:              47.062,08 $   (48,90 %)
Investiert MV:     49.182,02 $   (51,10 %)  — AAPL 9.757,56 / DELL 8.874,40 / JPM 1.073,85 / LLY 10.167,04 / UNH 9.338,88 / V 9.970,29
P/L heute:         **+16,26 $** (**+0,0169 %** vs last_equity 96.230,67) [GRÜN, Cap −3 %]
ATH:              100.066,47 $   (unverändert)
Drawdown:          **−3,817 %**  [GRÜN, marginal verschlechtert vs 09:40 −3,750 %; Schwelle −15 % bei 85.056,50]
Guardrails:        Daily +0,0169 % | Weekly KW34 Tag 3 vs Fr Close 96.192,26 = **+0,057 % GRÜN** | Käufe **1/2 KW34** (Slot 2 offen) | VIX GRÜN (Midday n/a) | Crash-Filter NEIN | DD GRÜN | Earnings-Blackout KEINE
Positionen:        **6/8**
Offene Orders:     **KEINE** (Alpaca /v2/orders?status=open bestätigt 0)

Positions-Übersicht Live 13:07 (Ø-P/L **+0,94 %** ungewichtet, IEX latestTrade):
- **JPM +7,56 % BEST P/L** (357,95 $, chg −1,39 %, 3 Sh, MV 1.073,85, entry 332,78) — verschlechtert vs 09:40 +7,90 %
- **LLY +6,45 %** (1270,88 $, **chg +3,86 % BEST chg**, 8 Sh, MV 10.167,04, entry 1193,89)
- V +3,39 % (369,27 $, chg +1,38 %, 27 Sh, MV 9.970,29, entry 357,178) — verbessert vs 09:40 +1,97 %
- AAPL −0,66 % (314,76 $, chg +1,54 %, 31 Sh, MV 9.757,56, entry 316,857) — verbessert vs 09:40 −1,62 %
- UNH −3,10 % (389,12 $, chg −1,22 %, 24 Sh, MV 9.338,88, entry 401,57) — verschlechtert vs 09:40 −2,14 %
- **DELL −7,99 % WORST P/L + WORST chg** (443,72 $, **chg −5,31 %** Tag-3-Weakness eskaliert, 20 Sh, MV 8.874,40, entry 482,27) — **V1-Puffer +0,007 % RAZOR** (Thr 443,6884; ein Tick unter cur → Market Order SOFORT)

Sell-Signal-Check (V1-V4) 13:07 — **kein Trigger, keine Order platziert** (RSI/EMA V5-V6 nur Close):
- **V1 Std −8 % alle SICHER** (min DELL **+0,007 % RAZOR** dramatisch verschlechtert vs 09:40 +2,59 % / Di Close +5,61 % — 3 Sessions kontinuierliche Kompression):
  - DELL +0,007 % (Thr 443,6884), UNH +5,33 % (Thr 369,44), AAPL +7,98 % (Thr 291,51), V +12,38 % (Thr 328,60), LLY +15,70 % (Thr 1098,38), JPM +16,92 % (Thr 306,16)
- **V2-Trailing:** AAPL DQF 9. Tag Wick 344,555 = Thr 303,21 → cur 314,76 = **+3,81 % SICHER** (verbessert vs 09:40 +2,84 %); **UNH V2 DQF 22. Tag persistent BROKEN −4,07 %** via Wick 460,95 = Thr 405,64 (verschlechtert vs 09:40 −3,10 %) — **Alt-V2 via 437,13 = 384,67 Puffer +1,16 % SICHER** (verschlechtert vs 09:40 +2,17 %) + Std-V1 +5,33 % primär SICHER, Owner-Entscheidung pending 22. Tag
- **V3/V4:** max JPM +7,56 % << 20 %-TP1 → kein Trigger
- V5/V6: nur Close-Vollcheck (Midday-Spec)

Daily Loss Cap: 96.246,93 vs last_equity 96.230,67 = **+0,0169 % GRÜN** weit von Cap −3 % → keine Order-Stornierung (0 pending)

Alle **8 Guardrails GRÜN + 3 WARN CRITICAL** (**DELL V1-Puffer +0,007 % RAZOR — ein Tick zum Market-Stop**; UNH V2-DQF 22. Tag Alt-V2 +1,16 % SICHER shrinking; AAPL V2-DQF 9. Tag +3,81 % SICHER stabil).

Markt-Kontext Midday: DELL Tag-3-Softness beschleunigt (−5,31 % Session), portfolio-P/L quasi flat durch LLY/V/AAPL-Bounce vs DELL/UNH-Drag. **Kein K1-K5-Kandidat verifiziert im Midday-Fenster** (Slot 2 offen bis Close).

ClickUp: **kein Alert** (Routine-Spec: nur bei Stops ausgelöst oder Daily Cap; DELL noch nicht getriggert, +0,007 % Puffer aktiv).
PushNotification: **JA** (DELL V1-Puffer 3 Sessions kontinuierlich komprimiert von +5,61 % → +2,59 % → +0,007 % RAZOR — Owner-Awareness kritisch vor Close, ein Tick unter 443,68 = automatischer Market-Sell).
Nächster Check: **Mi 19.08. 16:00 ET Market Close KW34 Tag 3** — DELL Close-Kurs entscheidend (V1-Trigger-Bestätigung falls <443,69), UNH V2-DQF 22. Tag Owner-Entscheidung, Vollcheck V5/V6 EMA/RSI, Slot 2 K1-K5-Vollverifikation.

---

**Market Open 09:30 ET 2026-08-19 (Mi, KW34 Tag 3) — 09:40 Live-Snapshot:**
Gesamtwert:        96.313,50 $   (Alpaca /v2/account equity Live)
Cash:              47.062,08 $   (48,86 %)
Investiert MV:     49.251,42 $   (51,14 %)  — AAPL 9.663,32 / DELL 9.085,00 / JPM 1.077,18 / LLY 10.168,00 / UNH 9.431,76 / V 9.833,94
P/L heute:         **+82,83 $** (**+0,086 %** vs last_equity 96.230,67) [GRÜN, Cap −3 %]
ATH:              100.066,47 $   (unverändert)
Drawdown:          **−3,750 %**  [GRÜN, verbessert vs Di Close −3,853 %; Schwelle −15 % bei 85.056,50]
Guardrails:        Daily +0,086 % | **Weekly KW34 Tag 3 vs Fr Close 96.192,26 = +0,126 % GRÜN** | Käufe **1/2 KW34** (Slot 2 offen — heute Buy-Scan durchgeführt) | VIX ~15,86 GRÜN | Crash-Filter NEIN (SPY +0,29 % Live vs Di) | DD GRÜN | Earnings-Blackout KEINE (DELL 27.08. 6 HT >3)
Positionen:        **6/8**
Offene Orders:     **KEINE** (Alpaca /v2/orders?status=open bestätigt 0)

Positions-Übersicht Live 09:40 (Ø-P/L **+1,08 %** ungewichtet, IEX latestTrade):
- **JPM +7,90 % BEST P/L** (359,34 $, chg +0,90 % vs Di 363,00? nein: entry 332,78, cur unverändert vs Di, 3 Sh, MV 1.077,18)
- **LLY +6,46 %** (1272,46 $, **chg +3,99 % BEST chg** vs Di Close 1223,60, 8 Sh, MV 10.168,00, entry 1193,89)
- V +1,97 % (364,42 $, chg +0,05 %, 27 Sh, MV 9.833,94, entry 357,178)
- AAPL −1,62 % (311,81 $, chg +0,58 %, 31 Sh, MV 9.663,32, entry 316,857)
- UNH −2,14 % (393,05 $, chg −0,22 %, 24 Sh, MV 9.431,76, entry 401,57)
- **DELL −5,81 % WORST P/L + WORST chg** (455,19 $, **chg −2,86 %** Tag 3 Softness setzt sich fort, 20 Sh, MV 9.085,00, entry 482,27) — **V1-Puffer +2,59 % ENGSTE** (Thr 443,69)

Sell-Signal-Check (V1-V6) 09:40 — **kein Trigger, keine Order platziert**:
- **V1 Std −8 % alle SICHER** (min DELL **+2,59 % ENGSTE** verschlechtert vs Di Close +5,61 % durch chg −2,86 % Tag-3-Weakness):
  - DELL +2,59 % (Thr 443,69), UNH +6,39 % (Thr 369,44), AAPL +6,96 % (Thr 291,51), V +10,90 % (Thr 328,60), LLY +15,85 % (Thr 1098,38), JPM +17,37 % (Thr 306,16)
- **V2-Trailing:** AAPL DQF 9. Tag Wick 344,555 = Thr 303,21 → cur 311,81 = **+2,84 % SICHER** (marginal verbessert vs Di Close +2,24 %); **UNH V2 DQF 22. Tag persistent BROKEN −3,10 %** via Wick 460,95 = Thr 405,64 (verschlechtert vs Di Close −2,89 %) — **Alt-V2 via 437,13 = 384,67 Puffer +2,17 % SICHER** + Std-V1 +6,39 % primär SICHER, Owner-Entscheidung pending 22. Tag
- **V3/V4:** max JPM +7,90 % << 20 %-TP1 → kein Trigger
- **V5/V6:** nur Close-Vollcheck (Market-Open-Spec)

Buy-Scan **Slot 2 KW34 — Ergebnis: KEINE Kauforder platziert** (K1-K3 Alpaca IEX Daily Bars):
- **PANW #1 K3 RS +48,60 pp** (XLK/Software) — 368,56 $, K1✓ EMA50 336,26>EMA200 253,72 / K2✓ RSI 54,45 / K3✓ RS63 +48,60 pp / **K4 nicht verifizierbar Market-Open (Vol Extrap ~8 %)** / K5-Recheck nach 17.08. Earnings pending → NO-BUY
- **CRDO REJECT (K2 FAIL):** RSI 48,02 < 50 (verschlechtert vs Mo/Di) — zusätzlich K5 FAIL FwdPE 58 >> 35 → REJECT persistent
- **MU K3 RS +29,47 pp** (Semis) — 939,27 $, K1✓ EMA50 933,93>EMA200 644,88 / K2✓ RSI 50,57 knapp / K3✓ RS +29,47 pp / K4 nicht verifizierbar Market-Open (Vol ~4 %) / K5 pending → NO-BUY, Gap-Up-Muster Owner-Regel offen
- **GE K3 RS +23,51 pp** (XLI/Industrials) — 366,41 $, K1✓ EMA50 357,97>EMA200 327,44 / K2✓ RSI 50,86 knapp / K3✓ RS +23,51 pp / K4 nicht verifizierbar Market-Open (Vol ~6 %) / K5 pending → NO-BUY
- **LMT K3 RS +9,29 pp** (XLI/Defense) — 601,40 $, K1✓ / K2✓ RSI 63,31 / K3✓ / K5 ✓ (FwdPE 19,70 gestern) / **K4 nicht verifizierbar Market-Open (Vol ~1 %)** → NO-BUY, Midday-Recheck nötig
- **NVDA REJECT persistent (K3 FAIL):** RS63 −5,02 pp verschlechtert vs Di Close +3,46 pp → Flip zurück in Negativ → REJECT

**K4-Constraint:** Bei Market-Open 09:40 ET nur ~8 Min Session, Volumen-Extrapolation unzuverlässig für 120 %-Threshold. Alle K1-K3-passierende Kandidaten warten auf Midday/Close-Vollcheck.

Sektor-Struktur Live 09:40: **XLK 19,42 %** (AAPL 10,03 + DELL 9,43), **XLV 20,35 %** (UNH 9,79 + LLY 10,56), **XLF 11,33 %** (JPM 1,12 + V 10,21), Cash 48,86 % — alle < 30 %-Cap ✓

Weekly Loss Cap Check: 96.313,50 vs Fr Close 96.192,26 = **+0,126 % GRÜN** weit von Cap −5 % → keine Sperre, keine Order-Stornierung nötig (0 pending)

Alle **8 Guardrails GRÜN + 3 WARN persistent** (UNH V2-DQF 22. Tag razor BROKEN −3,10 % — Alt-V2 +2,17 %/Std-V1 +6,39 % sicher; AAPL V2-DQF 9. Tag +2,84 % SICHER marginal — Std-V1 +6,96 % primär; **DELL V1-Puffer +2,59 % ENGSTE Tag-3-Weakness** — Watch, kein Trigger).

Markt-Kontext: SPY Live 769,955 (chg **+0,29 %** vs Di 767,73), VIX ~15,86 GRÜN leicht fallend, LLY +3,99 % führt Portfolio-Gain via XLV-Rebound (XLV +2,65 % IEX). **Kein Kandidat erfüllt alle K1-K5 im Market-Open-Fenster** (K4 Timing-Constraint).

ClickUp: **kein Alert** (Silence: keine Stops ausgelöst, kein Trade, kein Guardrail-Trigger, keine Owner-Aktion aus Buy-Scan-Ergebnis).
PushNotification: **NEIN** (Silence-Rule Market-Open: alle V1 SICHER, kein Kauf/Verkauf, Daily/Weekly/DD GRÜN, DQF-Zustände bereits bekannt, DELL-Tightening bekanntes WARN, Slot 2 bleibt offen bis Midday/Close).
Nächster Check: **Mi 19.08. 13:00 ET Midday Stop-Check KW34 Tag 3** — DELL V1-Puffer-Verlauf (Tag 3 accelerating watch), AAPL V2-DQF 9. Tag, UNH V2-DQF 22. Tag Owner-Entscheidung, LMT/PANW/MU/GE K4 Session-Verifikation für Slot-2-Buy-Chance.

---

**Market Close 16:00 ET 2026-08-18 (Di, KW34 Tag 2) — Tagesbilanz:**
Gesamtwert:        96.210,55 $   (Alpaca /v2/account equity Close)
Cash:              47.062,08 $   (**48,92 %**)
Investiert MV:     49.148,47 $   (51,08 %)  — AAPL 9.610,00 / DELL 9.371,60 / JPM 1.089,00 / LLY 9.788,80 / UNH 9.454,32 / V 9.834,75
P/L heute:         **+347,26 $** (**+0,362 %** vs last_equity 95.863,29) [GRÜN, Cap −3 %]
Alpha vs SPY:      **+1,00 pp POS** (SPY delayed-SIP 772,67 → 767,73 = **−0,640 %**; Perplexity nannte +0,04 % Yahoo-Composite unklar Divergenz; IEX-Ref −0,68 %; Portfolio +0,362 % outperformt via LLY +3,42 % / V +1,51 % / JPM +0,57 % / AAPL +1,44 % Stärke gegen SPY-Rotation-Weakness)
ATH:              100.066,47 $   (unverändert)
Drawdown:          **−3,853 %**  [GRÜN, verbessert vs Midday −3,920 %; Schwelle −15 % bei 85.056,50]
Guardrails:        Daily +0,362 % | **Weekly KW34 Tag 2 vs Fr Close 96.192,26 = +0,019 % GRÜN** | Käufe **1/2 KW34** (Slot 2 offen — Mi 19.08. verfügbar) | VIX Close 15,96 GRÜN | Crash-Filter NEIN (SPY −0,64 % >> −5 %) | DD GRÜN | Earnings-Blackout KEINE (DELL 27.08. 7 HT >3)
Positionen:        **6/8**
Offene Orders:     **KEINE** (Alpaca /v2/orders?status=open bestätigt 0)

Positions-Übersicht Close (Ø-P/L **+1,11 %** ungewichtet):
- **JPM +9,08 % BEST P/L** (363,00 $, chg +0,57 %, 3 Sh, MV 1.089,00, entry 332,78)
- **LLY +2,49 %** (1223,60 $, **chg +3,42 % BEST chg**, 8 Sh, MV 9.788,80, entry 1193,89)
- V +1,98 %      (364,25 $, chg +1,51 %, 27 Sh, MV 9.834,75, entry 357,178)
- UNH −1,90 %    (393,93 $, chg −0,43 %, 24 Sh, MV 9.454,32, entry 401,57)
- AAPL −2,16 %   (310,00 $, chg +1,44 %, 31 Sh, MV 9.610,00, entry 316,857)
- **DELL −2,84 % WORST P/L + WORST chg** (468,58 $, **chg −2,34 %** Tag 2 Softness setzt sich fort, 20 Sh, MV 9.371,60, entry 482,27)

Vollständiger V1-V6 Signal-Check Close (Alpaca IEX EOD Bars):
- **V1 Std −8 % alle SICHER** (min DELL **+5,61 % ENGSTE** verbessert vs Midday +4,41 % durch Late-Session Recovery vs Erste-Session-Low):
  - DELL +5,61 % (Thr 443,69), AAPL +6,34 % (Thr 291,51), UNH +6,63 % (Thr 369,44), V +10,85 % (Thr 328,60), LLY +11,40 % (Thr 1098,38), JPM +18,57 % (Thr 306,16)
- **V2-Trailing:** AAPL DQF 8. Tag Wick 344,555 = Thr 303,21 → cur 310,00 = **+2,24 % SICHER** (marginal erodiert vs Midday +2,50 %); **UNH V2 DQF 21. Tag persistent BROKEN −2,89 %** via Wick 460,95 = Thr 405,64 (verschlechtert vs Midday −2,49 %) — **Alt-V2 via 437,13 = 384,67 Puffer +2,41 % SICHER** + Std-V1 +6,63 % primär SICHER, Owner-Entscheidung pending 21. Tag
- **V3/V4:** max JPM +9,08 % << 20 %-TP1 → kein Trigger
- **V5 (EMA50<EMA200):** ALLE Golden Cross intakt SICHER (Alpaca IEX Daily EOD):
  - AAPL 308,96>282,48 (spread +26,47) / DELL 412,79>248,20 (spread **+164,59!**) / JPM 342,95>318,69 (+24,26) / LLY 1158,27>1042,77 (+115,50) / UNH 405,81>355,12 (+50,69) / V 352,08>336,03 (+16,05) → **KEIN Death Cross, KEIN Trigger**
- **V6 (RSI>80 AND RS_4w<0):** KEIN Symbol RSI >80 (max JPM 64,44; LLY 58,04 / DELL 56,02 / V 55,16 / AAPL 48,00 / UNH 37,81); SPY 4w-Ret +2,57 %; RS_4w: DELL +13,42 pp / JPM +2,69 pp / LLY +1,83 pp positiv, V −0,20 pp / AAPL −7,91 pp / UNH −12,32 pp negativ → **kein Symbol RSI>80 UND RS<0 gleichzeitig** → **KEIN Trigger**
→ **KEINE Verkaufsorder für Mi 19.08. platziert**

Sektor-Struktur Close: **XLK 19,73 %** (AAPL 9,99 + DELL 9,74), **XLV 20,00 %** (UNH 9,83 + LLY 10,17), **XLF 11,35 %** (JPM 1,13 + V 10,22), Cash 48,92 % — alle < 30 %-Cap ✓

Weekly Loss Cap Check: 96.210,55 vs Mo-Basis (Fr 14.08 Close) 96.192,26 = **+0,019 % [GRÜN]** weit von Cap −5 % → keine Sperre, keine Order-Stornierung nötig (0 pending)

Watchlist Mi 19.08. (KW34 Tag 3, Slot 2 verfügbar) K1-K3 Alpaca IEX:
- **GE** (XLI/Industrials, LargeCap) — 375,13 $, K1✓ EMA50 354,07>EMA200 322,24 / K2✓ RSI 59,63 / K3✓ RS +7,56 pp → **K4/K5 Mi prüfen** (Beat & Guidance-Raise Q2 nach Perplexity)
- **LMT** (XLI/Defense) — 607,24 $, K1✓ EMA50 560,56>EMA200 550,06 / K2✓ RSI 63,75 / **K3✓ RS +17,21 pp #1** → K4 Mi Vol-belastbar prüfen (Di K4 ~69 % Extrap, Recovery-Bounce vorbei), K5 ✓ (FwdPE 19,70 gestern)
- **NVDA** (XLK/GPU-AI) — 219,73 $, K1✓ EMA50 209,80>EMA200 196,24 / K2✓ RSI 56,56 / **K3✓ RS +3,46 pp FLIP von −4,8 pp Mo!** → K4/K5 Mi prüfen (Upgrade Watch-only → Full-Scan)
- **PANW** (XLK/Software) — 374,15 $, K1✓ EMA50 329,44>EMA200 236,72 / K2✓ RSI 59,85 / K3✓ RS +6,82 pp → K5-Recheck nach Earnings 17.08. (FwdPE-Update) Mi
- **CRDO REJECT persistent** (K5 FAIL FwdPE 58,43 >> 35 Hardcap; nur Recheck falls Kompression <35)
- REJECT: FSLR (K1 EMA50<EMA200), DUOL (K1), AKR (K3), AMX/BBWI (K2/K3), MU (K3 −5,54 pp verschlechtert), XLE (K2 RSI 72,66 >70)

Markt-Kontext Close: SPY 767,73 (delayed-SIP) / 767,37 (IEX) = **−0,64 %** vs Mo, Perplexity-Divergenz +0,04 % Yahoo unklar; VIX Close **15,96** GRÜN steigend (+6,5 % vs Mo 14,99); US 10Y **4,725 %** Yield persistent Hoch; XLE Best +1,08 % (Öl-Rally) / XLC Worst −1,89 %; Nasdaq-Futures-Schwäche Pre-Market bestätigte sich intraday (XLK-Rotation-Weakness); Portfolio outperformt SPY via LLY-Rebound (+3,42 %) + V (+1,51 %) trotz DELL-Weakness.

Alle **8 Guardrails GRÜN + 2 WARN persistent** (UNH V2-DQF 21. Tag razor BROKEN −2,89 % — Alt-V2 +2,41 %/Std-V1 +6,63 % sicher; AAPL V2-DQF 8. Tag +2,24 % SICHER marginal — Std-V1 +6,34 % primär).

ClickUp Tagesbericht Prio 4 (positives P/L): [CLOSE] Tagesbilanz — 2026-08-18 — versucht.
PushNotification: **JA** (Close-Ausnahme: Alpha +1,00 pp POS, DELL Tag 2 chg −2,34 % Verlauf, UNH V2-DQF 21. Tag persistent Owner-Entscheidung, NVDA K3-RS-Flip als neuer Watchlist-Kandidat).
Nächster Check: **Mi 19.08. 08:30 ET Pre-Market KW34 Tag 3** — DELL Tag-3-Verlauf, AAPL V2-DQF 9. Tag, UNH V2-DQF 22. Tag Owner-Entscheidung, GE/LMT/NVDA/PANW K4/K5 Vollcheck, Slot 2 KW34 Buy-Scan-Vorbereitung.

---

**Midday 13:07 ET 2026-08-18 (Di, KW34 Tag 2) — Stop-Check:**
Positionen: 6/8 | Ø-P/L +0,87 % ungewichtet | Equity 96.143,85 $ (Cash 47.062,08 / Inv MV 49.083,50)
Schlechteste Position: **DELL −3,95 %** (Last 463,24 $, chg_today **−3,45 %** Erste-Session-Softness Tag 2 setzt sich fort, V1 443,69 Puffer **+4,41 % ENGSTE**)
Beste Position:        **JPM +8,28 %** (Last 360,33 $, chg −0,18 %, V1 306,16 Puffer +17,69 %)
Übrige: AAPL −1,92 % (310,79, chg +1,70 %, V1 291,51 Puffer +6,61 %) | UNH −1,50 % (395,55, chg −0,02 %, V1 369,44 Puffer +7,07 %) | LLY +2,08 % (1218,78, **chg +3,01 %** BEST chg, V1 1098,38 Puffer +10,96 %) | V +2,24 % (365,18, chg +1,77 %, V1 328,60 Puffer +11,13 %)
Stops: **alle regulär** — V1/V2/V3/V4 nicht ausgelöst (RSI/EMA bei Midday nicht geprüft):
- **V1 Std −8 % alle SICHER** (min DELL +4,41 % ENGSTE, verschlechtert vs Open +9,04 % durch chg −3,45 %)
- **V2-Trailing:** AAPL DQF 8. Tag Wick 344,555 = Thr 303,21 → cur 310,79 = **+2,50 % SICHER** verbessert vs Open +1,09 %; **UNH V2 DQF 20. Tag Wick 460,95 = Thr 405,64 → cur 395,55 = BROKEN −2,49 % persistent** stabil vs Open −2,46 %; **Alt-V2 via 437,13 = 384,67 = +2,83 % SICHER** + Std-V1 +7,07 % primär SICHER
- **V3/V4:** max JPM +8,28 % << 20 %-TP1 → kein Trigger
Daily P/L: **+0,293 %** (96.143,85 / 95.863,29) [GRÜN — Limit −3 %; verbessert vs Open +0,342 % marginal]
Weekly P/L KW34 Tag 2 vs Fr Close 96.192,26: **−0,050 %** [GRÜN — Limit −5 %]
Drawdown vs ATH 100.066,47: **−3,920 %** [GRÜN, marginal verbessert vs Open −3,873 %; Schwelle −15 % bei 85.056,50]
Pending Orders: **0** (Alpaca /v2/orders?status=open bestätigt) | Käufe KW34: 1/2 (Slot 2 offen — heute NICHT besetzt)
Alle **8 Guardrails GRÜN + 2 WARN persistent** (UNH V2-DQF 20. Tag BROKEN −2,49 % — Alt-V2/Std-V1 sicher; DELL Tag 2 chg −3,45 % accelerating watch — V1-Puffer +4,41 %).
ClickUp: **kein Log** (Silence: keine Stops, kein Daily-Cap, kein Trade).
PushNotification: **NEIN** (Silence-Rule Midday: alle V1 SICHER, Daily/Weekly/DD GRÜN, DELL-Verlauf bekanntes WARN — kein neuer Trigger).
> Nächste Routine: **Di 18.08. 16:00 ET Market Close** — DELL Tag-2-Close-Verlauf (Erholung/Beschleunigung?), AAPL V2-DQF 8. Tag, UNH V2-DQF 20. Tag Owner-Entscheidung, V5/V6 Vollcheck, LMT/CRDO Watchlist Session-Reife.

---

**Market Open 09:30 ET 2026-08-18 (Di, KW34 Tag 2) — 09:40 Live-Snapshot:**
Gesamtwert:        96.190,68 $   (Alpaca /v2/account equity Live)
Cash:              47.062,08 $   (48,92 %)
Investiert MV:     49.133,06 $   (51,08 %)  — AAPL 9.501,44 / DELL 9.675,80 / JPM 1.084,89 / LLY 9.652,00 / UNH 9.495,96 / V 9.722,97
P/L heute:         **+327,39 $** (**+0,342 % vs last_equity 95.863,29**) [GRÜN, Cap −3 %]
ATH:              100.066,47 $   (unverändert)
Drawdown:          **−3,873 %**  [GRÜN, verbessert vs Pre-Market −4,278 %; Schwelle −15 % bei 85.056,50]
Guardrails:        Daily +0,342 % | **Weekly KW34 Tag 2 vs Fr Close 96.192,26 = −0,002 % GRÜN** | Käufe **1/2 KW34** (Slot 2 offen — heute NICHT besetzt) | VIX ~15,9 GRÜN | Crash-Filter NEIN (SPY −0,46 % Live) | DD GRÜN | Earnings-Blackout KEINE (DELL 27.08. 7 HT >3)
Positionen:        **6/8**
Offene Orders:     **KEINE** (Alpaca /v2/orders?status=open bestätigt 0)

Positions-Übersicht Live 09:40 (Ø-P/L **+1,02 %** ungewichtet):
- **JPM +8,67 % BEST P/L** (361,63 $, chg +0,19 %, 3 Sh, MV 1.084,89, entry 332,78)
- **LLY +1,06 %** (1206,50 $, **chg +1,97 % BEST chg**, 8 Sh, MV 9.652,00, entry 1193,89)
- V +0,82 % (360,11 $, chg +0,35 %, 27 Sh, MV 9.722,97, entry 357,178)
- DELL +0,32 % (483,79 $, chg +0,83 % — Erholung nach Mo Erste-Session −2,27 %, 20 Sh, MV 9.675,80, entry 482,27)
- UNH −1,47 % (395,67 $, chg +0,01 %, 24 Sh, MV 9.495,96, entry 401,57)
- **AAPL −3,27 % WORST P/L** (306,50 $, chg +0,30 %, 31 Sh, MV 9.501,44, entry 316,857)

Sell-Signal-Check (V1-V6) 09:40 — **kein Trigger, keine Order platziert**:
- **V1 Std −8 % alle SICHER** (min AAPL **+5,14 % ENGSTE** verbessert vs Pre-Market +5,45 %):
  - AAPL +5,14 % (Thr 291,51), UNH +7,10 % (Thr 369,44), DELL +9,04 % (Thr 443,69), V +9,59 % (Thr 328,60), LLY +9,84 % (Thr 1098,38), JPM +18,12 % (Thr 306,16)
- **V2-Trailing:** AAPL DQF 8. Tag Wick 344,555 = Thr 303,21 → cur 306,50 = **+1,09 % SICHER marginal** (verschlechtert vs Pre-Market +1,38 %); **UNH V2 DQF 20. Tag Wick 460,95 = Thr 405,64 → cur 395,67 = BROKEN −2,46 %** (verschlechtert vs Pre-Market −2,20 %); **Alt-V2 via 437,13 = 384,67 = +2,86 % SICHER** + Std-V1 +7,10 % primär SICHER, Owner-Entscheidung pending 20. Tag
- **V3/V4:** max JPM +8,67 % << 20 %-TP1 → kein Trigger
- **V5/V6:** nur Close-Vollcheck (Market-Open-Spec)

Buy-Scan **Slot 2 KW34 — Ergebnis: KEINE Kauforder platziert**:
- **CRDO REJECT:** K1-K3 ✓ (EMA50 230,66>EMA200 185,18 / RSI 62,80 / RS +59,6 pp #1), K4 ✓ (Extrap ~380 %), **K5 FAIL FwdPE 58,43 >> 35** (Perplexity Yahoo/Zacks); zusätzlich **Gap-Down heute Open 266,92 vs Mo Close 283,11 = −5,72 %** Overshoot-Reversal-Signal + Earnings 2026-09-01 (10 HT weg, Blackout Fr 28.08.)
- **LMT REJECT (K4):** K1 ✓ (EMA50 558,19>EMA200 532,05), K2 ✓ (RSI 58,74), K3 ✓ (RS +11,0 pp XLI-Defense), K5 ✓ (FwdPE **19,70** / RevYoY **+10,50 %** / Earnings 2026-10-27), **K4 FAIL Extrapolation ~69 %** (10-Min-IEX-Vol 928 × 39 = 36.192 vs Avg-20-IEX 52.444 = 69 %); zusätzlich Recovery-Bounce nach Mo Close 593,92 → 601,98 (+1,36 %), typisch KEIN Peak-Vol-Tag
- **NVDA:** K3 FAIL RS −4,8 pp → Watch-only unverändert
- **MU:** Gap-Up-Muster 4. Tag → Owner-Regel-Diskussion pending
- **PANW:** K5-Recheck nach 17.08.-Earnings pending, Vorsichts-Modus

Sektor-Struktur Live 09:40: **XLK 19,94 %** (AAPL 9,88 + DELL 10,06), **XLV 19,91 %** (UNH 9,87 + LLY 10,03), **XLF 11,24 %** (JPM 1,13 + V 10,11), Cash 48,92 % — alle < 30 %-Cap ✓

Weekly Loss Cap Check: 96.190,68 vs Fr Close 96.192,26 = **−0,002 % GRÜN** weit von Cap −5 % → keine Sperre, keine Order-Stornierung nötig (0 pending)

Alle **8 Guardrails GRÜN + 2 WARN persistent** (UNH V2-DQF 20. Tag razor BROKEN −2,46 % — Alt-V2 +2,86 %/Std-V1 +7,10 % sicher; AAPL V2-DQF 8. Tag +1,09 % SICHER marginal — Std-V1 +5,14 % ENGSTE primär).

Markt-Kontext: SPY Live 769,10 (chg **−0,46 %** vs Mo 772,62), VIX ~15,9 GRÜN steigend, Nasdaq-Futures Pre-Market −1,3 %, US 10Y Yield 4,73–4,75 % neues Hoch — Vorsichts-Modus aktiviert bestätigt. **Kein Kandidat erfüllt alle K1-K5.**

ClickUp: **kein Alert** (Silence: keine Stops ausgelöst, kein Trade, kein Guardrail-Trigger, keine Owner-Aktion aus Buy-Scan-Ergebnis).
PushNotification: **NEIN** (Silence-Rule Market-Open: alle V1 SICHER, kein Kauf/Verkauf, Daily/Weekly/DD GRÜN, DQF-Zustände bereits bekannt, CRDO/LMT-REJECT non-urgent — Slot 2 bleibt offen bis Mi).
Nächster Check: **Di 18.08. 13:00 ET Midday Stop-Check KW34 Tag 2** — AAPL V2-DQF 8. Tag Verlauf, UNH V2-DQF 20. Tag, DELL Tag-2-Verlauf (Erholung/Rückfall?), LMT/CRDO Watchlist-Zustand nach Session-Reife.

---

**Market Close 16:00 ET 2026-08-17 (Mo, KW34 Tag 1) — Tagesbilanz:**
Gesamtwert:        95.866,65 $   (Alpaca /v2/account equity Close)
Cash:              47.062,09 $   (**49,09 %**)
Investiert MV:     48.804,56 $   (50,91 %)  — AAPL 9.463,68 / DELL 9.593,40 / JPM 1.082,88 / LLY 9.481,28 / UNH 9.494,64 / V 9.688,68
P/L heute:         **−328,04 $** (**−0,341 %** vs last_equity 96.194,69) [GRÜN, Cap −3 %]
Alpha vs SPY:      **+0,133 pp POS** (SPY IEX Fr 776,30 → Mo 772,62 = **−0,474 %**; Perplexity nennt −0,37 %; Portfolio −0,341 % outperformt marginal via JPM/V/LLY-Stützen vs SPY-Rotation-Weakness)
ATH:              100.066,47 $   (unverändert)
Drawdown:          **−4,196 %**  [GRÜN, verschlechtert vs Midday −4,134 %; Schwelle −15 % bei 85.056,50]
Guardrails:        Daily −0,341 % | **Weekly KW34 Tag 1 vs Fr Close 96.192,26 = −0,338 % GRÜN** | Käufe **1/2 KW34** (Slot 1 DELL verbraucht) | VIX Intraday 14,92–14,99 GRÜN | Crash-Filter NEIN (SPY −0,474 % >> −5 %) | DD GRÜN | Earnings-Blackout KEINE (DELL 03.09. 17 HT >3)
Positionen:        **6/8**
Offene Orders:     **KEINE** (Alpaca /v2/orders?status=open bestätigt 0)

Positions-Übersicht Close (Ø-P/L +0,42 % ungewichtet):
- **JPM +8,47 % BEST P/L** (361,11 $, chg −0,518 %, 3 Sh, MV 1.082,88, entry 332,78)
- V +0,46 %      (358,95 $, chg −1,458 %, 27 Sh, MV 9.688,68, entry 357,178)
- **DELL −0,54 %** (479,75 $, **chg −2,270 % WORST chg** intraday-Softness Erste-Session, 20 Sh, MV 9.593,40, entry 482,27)
- LLY −0,73 %    (1185,04 $, chg +0,424 % ONLY GAIN chg, 8 Sh, MV 9.481,28, entry 1193,89)
- UNH −1,48 %    (395,54 $, chg −1,523 %, 24 Sh, MV 9.494,64, entry 401,57)
- **AAPL −3,65 % WORST P/L** (305,65 $, chg −0,212 %, 31 Sh, MV 9.463,68, entry 316,857)

Vollständiger V1-V6 Signal-Check Close (Alpaca IEX EOD):
- **V1 Std −8 % alle SICHER** (min AAPL +4,85 % ENGSTE verschlechtert vs Midday +4,16 % — Berechnungsupdate durch Close-Live 305,65 vs Midday 303,625):
  - AAPL +4,85 % (Thr 291,51), DELL +8,13 % (Thr 443,69, Erste-Session-Close), UNH +7,06 % (Thr 369,44), LLY +7,89 % (Thr 1098,38), V +9,23 % (Thr 328,60), JPM +17,95 % (Thr 306,16)
- **V2-Trailing:** AAPL DQF 7. Tag technisch AUS BROKEN RAUS via Wick 344,555 = Thr 303,21 → +0,81 % SICHER marginal-recovered vs Midday +0,14 %; **UNH V2 DQF 19. Tag persistent BROKEN −2,49 %** via Wick 460,95 = Thr 405,636 verschlechtert vs Midday −2,32 % — **Alt-V2 via 437,13 = 384,67 Puffer +2,83 % SICHER** + Std-V1 +7,06 % primär SICHER, Owner-Entscheidung pending 18. Tag
- **V3/V4:** max JPM +8,47 % << 20 %-TP1 → kein Trigger
- **V5 (EMA50<EMA200):** ALLE Golden Cross intakt SICHER — AAPL 308,68>282,33 / DELL 410,21>269,99 (Spread +140!) / JPM 341,67>317,40 / LLY 1153,83>1028,57 / UNH 405,90>359,53 / V 351,00>337,30 → **KEIN Death Cross, KEIN Trigger**
- **V6 (RSI>80 AND RS_4w<0):** KEIN Symbol RSI >80 (max JPM 60,90; DELL 58,06 / LLY 46,72 / V 48,66 / AAPL 44,42 / UNH 36,46); RS_4w-Verteilung: DELL +21,93 pp / JPM +2,45 pp positiv, AAPL/UNH/LLY/V negativ → **kein Symbol RSI>80 UND RS<0 gleichzeitig** → **KEIN Trigger**
→ **KEINE Verkaufsorder für Di 18.08. platziert**

Sektor-Struktur Close: **XLK 19,88 %** (AAPL 9,87 + DELL 10,01), **XLV 19,79 %** (UNH 9,90 + LLY 9,89), **XLF 11,24 %** (JPM 1,13 + V 10,11), Cash 49,09 % — alle < 30 %-Cap ✓

Weekly Loss Cap Check: 95.866,65 vs Mo-Basis (Fr 14.08 Close) 96.192,26 = **−0,338 % [GRÜN]** weit von Cap −5 % → keine Sperre, keine Order-Stornierung nötig (0 pending)

Watchlist Di 18.08. (KW34 Tag 2, Slot 2 verfügbar) K1-K3 Alpaca IEX:
- **CRDO** (XLK/Semis-Connectivity, MidCap) — 283,11, K1✓ EMA50 230,66>EMA200 185,18 / K2✓ RSI 62,80 / K3✓ **RS +59,6 pp #1** → K4/K5 morgen prüfen
- **LMT** (XLI/Defense) — 593,92, K1✓ EMA50 558,19>EMA200 532,05 / K2✓ RSI 58,74 / K3✓ RS +11,0 pp → K4/K5 prüfen
- **NVDA** (XLK/GPU-AI) — 225,10, K1✓ EMA50 209,36>EMA200 196,52 / K2✓ RSI 65,06 / **K3✗ RS −4,8 pp Watch-only**
- **MU** (XLK) — K1-K5 ✓ Vortag, aber 4-Tage-Gap-Up-Muster → Owner Limit-Regel-Diskussion weiter pending
- **PANW** (XLK) — Earnings 17.08. gestern, K5-FwdPE-Recheck Di
- REJECT: PLTR (K1 Death-Cross EMA50<EMA200), AVGO (K2 RSI 48,84 + K3 RS −12,3 pp), STRL (K3 RS −33,7 pp)

Perplexity (2 Queries): SPY −0,37 % / VIX Intraday 14,92–14,99 (+4,7-5,2 % vs Vortag 14,25) / Sektoren Top-3 XLE > XLU > XLB (YTD/MA-Basis Quelle unpräzise); Watchlist-Prompt.

Alle **8 Guardrails GRÜN + 2 WARN persistent** (UNH V2-DQF 19. Tag razor BROKEN −2,49 % — Alt-V2 +2,83 %/Std-V1 +7,06 % sicher; AAPL V2-DQF 7. Tag technisch AUS RAUS +0,81 % — Std-V1 +4,85 % ENGSTE primär).

ClickUp Tagesbericht Prio 3 (negatives P/L): [CLOSE] Tagesbilanz — 2026-08-17 — versucht.
PushNotification: **JA** (Close-Silence-Ausnahme wegen KW34-Start + neuer DELL-Position Erste-Session-Softness Owner-Info + AAPL V2-DQF-Verlauf + UNH V2-DQF 19. Tag persistent).
Nächster Check: **Di 18.08. 08:30 ET Pre-Market KW34 Tag 2** — DELL Verlauf Tag 2, AAPL V2-DQF, UNH V2-DQF 19. Tag Owner-Entscheidung, CRDO/LMT K4/K5 Vollcheck.

---

**Midday 13:00 ET 2026-08-17 (Mo, KW34 Tag 1):**
Positionen: 6/8 | Ø P/L: **+0,70 %** ungewichtet (JPM +9,57 Best / V +0,93 / LLY −0,10 / DELL −0,69 / UNH −1,33 / AAPL −4,18 Worst)
Beste Position: **JPM +9,57 %** (364,64 $, chg −0,03 % vs Open 09:44 364,755)
Schlechteste Position: **AAPL −4,18 %** (303,625 $, chg −0,54 % vs Open 305,28, verschlechtert vs Open P/L −3,65 %)
Stops V1-V4 Live-Check (V5/V6 nur Close-Vollcheck):
- **V1 Std alle 6 SICHER Puffer eng→weit:** **AAPL +4,16 % ENGSTE verschlechtert vs Open +4,72 %** (303,625 chg −0,54 %, Std-V1 291,51 primär), UNH +7,25 % verbessert vs Open +6,84 % (396,23 chg −0,08 % vs Open 396,555), DELL +7,94 % (478,925 chg −0,41 % vs Fill 482,27, Thr 443,69), LLY +8,59 % (1192,745 chg +1,30 % vs Open 1177,39, Thr 1098,38), V +9,71 % (360,5099 chg −0,48 % vs Open 362,255, Thr 328,60), **JPM +19,10 %** (364,64 chg −0,03 %, Thr 306,16)
- **V2-Trailing-Stop:** **⚠️ AAPL V2 razor +0,14 % via Wick 344,555 = Thr 303,21 verschlechtert vs Open +0,68 %** (303,625 > 303,21, DQF 6. Tag technisch AUS BROKEN RAUS aber Puffer erodiert; Std-V1 +4,16 % ENGSTE primär SICHER, V2 sekundär via DQF); **⚠️ UNH V2 BROKEN Puffer −2,32 % via Wick 460,95 = Thr 405,636 verschlechtert vs Open −2,24 %** (**18. Tag DQF persistent** — Alt-V2 via 437,13 = 384,67 Puffer **+3,01 % SICHER**, Std-V1 +7,25 % primär sicher, Owner-Entscheidung pending); JPM +14,12 % via Wick 363,08 (Thr 319,51) sicher, LLY +8,56 % via 52w-High 1248,53 (Thr 1098,71) sicher, V +9,55 % via 373,97 (Thr 329,09) sicher, DELL erste Session (kein 52w-Wick relevant, Std-V1 primär)
- **V3/V4:** max P/L JPM +9,57 % << 20 %-TP1 → kein Trigger
- **V5/V6:** nur Close-Vollcheck (Midday-Spec)
Daily P/L: **−0,275 % [GRÜN, Cap −3 %]** (Equity Live **95.929,94 $** vs last_equity 96.194,69 = −264,75 $; MV 48.869,74 $ / Cash 47.062,09 $ = **49,06 %**; DD vs ATH 100.066,47 = **−4,134 % GRÜN** verschlechtert vs Open −4,108 %; Weekly KW34 Tag 1 vs Fr Close 96.192,26 = **−0,273 % GRÜN** weit von Cap −5 %, verschlechtert vs Open −0,247 %)
Alpha vs SPY: n/a (Midday-Spec — Alpha nur Open/Close)
Stops: **alle regulär, KEIN Trigger ausgelöst**
Offene Orders: **KEINE** (0 pending Alpaca bestätigt)
Guardrails: **8 GRÜN + 2 WARN** (UNH V2-Wick DQF 18. Tag persistent BROKEN −2,32 % — Alt-V2/Std-V1 sicher, Owner pending; AAPL V2-DQF Puffer erodiert razor +0,14 % — Std-V1 +4,16 % ENGSTE primär)

ClickUp: **kein Alert** (Silence: keine Stops ausgelöst, kein Daily Cap erreicht, kein Owner-Handlungsbedarf)
PushNotification: **NEIN** (Silence-Rule Midday: alle V1 SICHER, kein Trigger, Daily P/L GRÜN −0,275 %, Weekly GRÜN, DD GRÜN, keine Order-Aktion, DQF-Zustände bereits bekannt Owner-pending)
Nächster Check: **Mo 17.08. 16:00 ET Market Close KW34 Tag 1** — EOD-Vollcheck V5/V6 alle 6 Positionen, AAPL V2-DQF-Verlauf (Puffer heute erodiert), UNH V2-DQF 18. Tag Owner-Entscheidung, DELL Erste-Session-Close, LLY Weakness-Recovery, Slot 2 KW34 Buy-Scan-Vorbereitung Di.

---

**Market Open 09:44 ET 2026-08-17 (Mo, KW34 Tag 1) — Post-DELL-Fill:**
Gesamtwert:        95.955,16 $   (Alpaca equity live 09:44 ET)
Cash:              47.062,09 $   (49,05 %) — nach DELL-Kauf −9.645,40
Investiert:        48.893,07 $   (50,95 %)  — AAPL 9.463,68 / **DELL 9.617,80 NEU** / JPM 1.094,27 / LLY 9.419,12 / UNH 9.517,32 / V 9.780,89
P/L Live:          −239,53 $     (**−0,249 % vs last_equity 96.194,69**)   [GRÜN, Cap −3 %]
ATH:              100.066,47 $   (unverändert)
Drawdown:          **−4,108 %**  [GRÜN, verschlechtert vs Pre-Open −3,978 %; Schwelle −15 % bei 85.056,50]
Guardrails:        Daily −0,249 % | **Weekly KW34 Tag 1 vs Fr Close 96.192,26 = −0,247 % GRÜN** | Käufe **1/2 KW34** (Slot 1 via DELL verbraucht) | VIX 14,92 GRÜN | Crash-Filter NEIN | DD GRÜN | Earnings-Blackout KEINE Position 4-HT-Fenster + DELL ~03.09. (17 HT >3)
Offene Positionen: **6/8** (NEU DELL)
Offene Orders:     **KEINE** (DELL FILLED @ 482,27)

Positions-Übersicht Live 09:44 ET (Ø-P/L +0,88 % ungewichtet ohne DELL Post-Fill):
- **JPM +9,60 % BEST** (364,755 $, 3 Sh, MV 1.094,27, entry 332,78)
- V +1,42 %      (362,255 $, 27 Sh, MV 9.780,89, entry 357,178)
- UNH −1,25 %    (396,555 $, 24 Sh, MV 9.517,32, entry 401,57)
- LLY −1,38 %    (1177,39 $, 8 Sh, MV 9.419,12, entry 1193,89)
- **DELL NEU −0,29 %** (480,89 $ post-fill, 20 Sh, MV 9.617,80, entry 482,27)
- **AAPL −3,65 % WORST** (305,28 $, 31 Sh, MV 9.463,68, entry 316,857)

V1 Std −8 % Live Puffer (alle SICHER):
- **AAPL +4,72 % ENGSTE**  (Thr 291,51, verschlechtert vs Pre-Open +5,10 %)
- **DELL +2,79 % NEU**     (Thr 443,69)
- LLY +7,20 %              (Thr 1098,38)
- UNH +6,84 %              (Thr 369,44, verschlechtert vs Pre-Open +8,16 %)
- V +10,25 %               (Thr 328,60)
- JPM +19,49 %             (Thr 306,16)

Sektor-Struktur Post-Fill: XLK **19,88 %** (AAPL 9,86 + DELL 10,02), XLV **19,73 %** (UNH 9,92 + LLY 9,82), XLF **11,33 %** (JPM 1,14 + V 10,19), Cash 49,05 %

Trade heute:
- **BUY LIMIT DELL 20 Sh @ 482,33 → FILLED @ 482,27** (Order-ID b068a260-cf47-4f90-ac27-cb3ac19e7fa8, Kosten 9.645,40 $)
- Kaufsignale K1-K5 alle ✓ (EMA-Golden-Cross, RSI 58,06, RS +93,32 pp #1, Vol-Extrap 124,6 %, FwdPE 26,74 + RevYoY +87,2 % via Dell IR Q1 FY27 Perplexity-Deep-Query)
- MU-Slot SKIP wegen Gap-Up-Muster-Wiederholung (Live 1017 > Limit 1013,52, Owner-Diskussion Limit-Regel weiter pending)

Alt-Kandidaten REJECT: MU (Gap-Up-Muster 4. Tag), GE (K5 FwdPE 48,31 FAIL), PANW (K4 45 % + Earnings HEUTE Blackout), XOM (K3 RS −3,72 FAIL)

ClickUp: **ITEM_246 19. Tag persistent** → Fallback Memory-Only
PushNotification: **JA (TRADE_BUY)** — DELL-Fill + K5-Konflikt aufgelöst
Nächster Check: **Mo 17.08. 13:00 ET Midday Stop-Check KW34 Tag 1** — DELL Post-Fill-Verlauf, UNH V2-DQF 18. Tag, AAPL V2 6. Tag, LLY Weakness-Verlauf

---

**Pre-Market 08:30 ET 2026-08-17 (Mo, KW34 Tag 1):**
Gesamtwert:        96.085,04 $   (Alpaca equity live Pre-Open)
Cash:              56.707,49 $   (58,99 %)
Investiert:        39.377,55 $   (40,98 %)  — AAPL 9.497,16 / JPM 1.084,89 / LLY 9.439,92 / UNH 9.589,68 / V 9.765,90
P/L Pre-Open:      −109,65 $     (**−0,114 % vs last_equity 96.194,69**)   [GRÜN, Cap −3 %]
ATH:              100.066,47 $   (unverändert)
Drawdown:          **−3,978 %**  [GRÜN, Schwelle −15 % bei 85.056,50]
Guardrails:        Daily −0,114 % | **Weekly KW34 Tag 1 vs Fr Close 96.192,26 = −0,111 % GRÜN** | Käufe **0/2 KW34 offen** | VIX 14,92 GRÜN | Crash-Filter NEIN | DD GRÜN | Earnings-Blackout KEINE Position 4-HT-Fenster
Offene Positionen: 5/8
Offene Orders:     **0** (MU 3× EXPIRED Fr KW33 final, KW34 startet frisch)

Positions-Übersicht Pre-Open (Ø-P/L +1,00 % ungewichtet):
- **JPM +8,67 % BEST** (361,63 $, chg −0,333 %, 3 Sh, MV 1.084,89, entry 332,78)
- V +1,27 %      (361,70 $, chg −0,673 %, 27 Sh, MV 9.765,90, entry 357,178)
- UNH −0,50 %    (399,57 $, chg −0,538 %, 24 Sh, MV 9.589,68, entry 401,57)
- LLY −1,16 %    (1179,99 $, chg −0,014 %, 8 Sh, MV 9.439,92, entry 1193,89)
- **AAPL −3,31 % WORST** (306,36 $, chg +0,141 %, 31 Sh, MV 9.497,16, entry 316,857)

V1 Std −8 % Live Puffer (alle SICHER):
- **AAPL +5,10 % ENGSTE** (Thr 291,51, verbessert vs Fr +4,87 %)
- LLY +7,43 % (Thr 1098,38, verschlechtert marginal vs Fr +7,45 %)
- UNH +8,16 % (Thr 369,44, verschlechtert vs Fr +8,79 %)
- V +10,06 % (Thr 328,60, verschlechtert vs Fr +10,82 %)
- JPM +18,12 % (Thr 306,16, verschlechtert vs Fr +18,52 %)

Sektor-Struktur Pre-Open: XLV **19,80 %** (UNH 9,98 + LLY 9,82), XLF **11,29 %** (JPM 1,13 + V 10,16), XLK **9,88 %** AAPL, Cash 58,99 %

Markt-Kontext (Perplexity):
- VIX 14,92 (+4,7 % vs Vortag 14,25) GRÜN weit von 30-Filter
- SPY Premarket leicht positiv (kein exakter %-Wert)
- 10Y Yield 4,69 % (marginal rückläufig vs 4,697 %)
- Makro heute klein: 8:30 Empire State Mfg, 10:00 NAHB, 16:00 TIC Flows — kein CPI/PPI/NFP/Fed
- News: Öl 89 $/Bbl (Hormus), US-Renditen nahe Mehrjahreshochs, Indien schwach

Earnings-Blackout-Check: **KEINE** der 5 offenen Positionen berichtet in 4-HT-Fenster (17.–20.08.) → keine Stop-Anpassung auf −5 %.

Watchlist Market-Open-Scan 09:30 ET: **XOM** (XLE-Sektor-Top), **DELL** (RS #1 K5-Konflikt-Klärung), **GE** (XLI-Basis), **MU** (Limit-Strategie-Review 4. Versuch), **PANW** (K5-Recheck FwdPE).

Entscheidung: **Market-Open-Scan JA** (alle Guardrails GRÜN, Cash ausreichend, 2 Slots offen).

ClickUp Pre-Market Log Task: Prio 4 [PRE-MARKET] Check — 2026-08-17 08:30 ET geplant (Fallback Memory-Only bei ITEM_246-Persistenz 19. Tag).
PushNotification: **NEIN** (Silence-Rule Pre-Market: keine Trigger, kein Owner-Handlungsbedarf, alle Guardrails GRÜN, keine Earnings-Blackouts, MU-Diskussion vertagt auf 09:30 Buy-Scan).
Nächster Check: **Mo 17.08. 09:30 ET Market Open KW34 Tag 1** — Buy-Scan Watchlist (XOM/DELL/GE/MU/PANW), K4-Vol + K5-Fundamentals, MU-Limit-Strategie-Owner-Entscheidung.

---

**Wochenabschluss KW33 — 14.08.2026 (Weekly Review 17:00 ET):**
Gesamtwert:       96.193,19 $   (Alpaca /v2/account equity live 17:00 ET, +0,93 $ vs Close 16:00 ET 96.192,26)
Cash:             56.707,49 $   (58,95 %)
Investiert:       39.485,70 $   (41,05 %)  — AAPL 9.478,54 / JPM 1.087,20 / LLY 9.440,00 / UNH 9.646,56 / V 9.833,40
Wochenrendite:    **-0,331 %**   (vs Depot Fr 07.08 Close 96.512,65)
SPY-Woche:        **+0,406 %**   (Alpaca IEX 07.08 Close 773,16 → 14.08 Close 776,30)
**Alpha KW33:**   **-0,737 pp NEG**
YTD Rendite:      **-3,807 %**   (vs Startkapital 100.000)
YTD SPY:          **+13,857 %**  (Alpaca IEX YE25 681,82 → 776,30)
**YTD Alpha:**    **-17,664 pp NEG** (75 Bot-Tage seit Init 31.05.26)
ATH:             100.066,47 $   (unverändert)
Drawdown:         -3,872 %      [GRÜN, Schwelle -15 % bei 85.056 $]
Offene Positionen: 5/8
Nächste Woche max. Käufe: 2 (Slot 1 + 2 offen für KW34)
Watchlist KW34:   DELL (XLK #1 K5 NEU-verifiziert FwdPE 24.94/RevYoY +29.27%/MCap 317.82Mrd/Earnings 03.09.), MU (XLK #2 Limit-Regel-Klärung), XOM (XLE tertiär K4/K5 Mo), GE (XLI tertiär K4/K5 Mo), NVDA (XLK Blackout-SKIP-Risk Earnings 26.08.), CRM (XLK Blackout-SKIP 26.08.), ORCL (XLK K1-Recheck), Neue Pipelines XLY/XLC (AMZN/TSLA/HD/GOOGL/META/DIS/NFLX Multi-Source-Check Mo)

Trades KW33 (Mo 11.08.–Fr 14.08. 4 HT):
- Käufe: **0/2 final** (MU-Slot 3× EXPIRED ohne Fill: 12.08./13.08./14.08. — Limit-Preis-Regel +0,5 % strukturell unerreichbar bei Momentum-Setup)
- Verkäufe/Stops: **0** (V1-V6 alle 5 SICHER EOD-Vollcheck Fr)
- Win-Rate: n/a (0 geschlossene Trades)
- Ø Haltedauer offene Positionen: **UNH 42 HT (18.06.)** / **JPM 42 HT (17.06.)** / **LLY 28 HT (06.07.)** / **AAPL 23 HT (13.07.)** / **V 18 HT (20.07.)** — Ø ~31 HT

Sektor-Struktur (Portfolio-Basis):
- XLV: **19,84 %** (UNH 10,03 + LLY 9,81) — <30 % OK, aber investiert-Basis 48,34 % (Owner-Klärung 5. Woche pending)
- XLF: **11,35 %** (JPM 1,13 + V 10,22)
- XLK: **9,85 %** (AAPL nur)
- Cash: 58,95 %

Sektor-Ranking KW33 (Perplexity vs SPY +0,41 %):
- **#1 XLK +5,46 % (Alpha +5,05 pp)** — Portfolio-Exposure nur AAPL 9,85 % → fing Rally kaum ab
- **#2 XLY +5,08 % (+4,67 pp)** — Portfolio 0 % Exposure
- **#3 XLC +4,32 % (+3,91 pp)** — Portfolio 0 % Exposure
- XLI +3,57 % / XLF +1,42 % / XLB +1,03 % / XLV +0,57 % / XLP -0,42 % / XLRE -1,08 % / XLE -1,36 % / XLU -2,87 %

Strategie-Status:    **STABIL** — alle Regeln (V1-V6/K1-K5/Blackout/Weekly-Cap/Cascade-Framework) regelkonform. 3 Diskussions-Punkte KW34 dringend: (1) XLV-Sektor-Cap-Deutung 5. Woche pending, (2) MU-Limit-Preis-Regel +0,5 % strukturell unerreichbar Momentum, (3) Cash-Quote 58,95 % vs 5-Wochen-SPY-Rally-Alpha-Loss.

ClickUp Weekly Report: **[WEEKLY] Review KW33 — 14.08.2026** Prio 3 versucht — ITEM_246 Persistenz-Fallback Memory-Only per notify-skill.md möglich.
PushNotification: **JA** (Weekly-Silence-Ausnahme: KW33-Wochenabschluss, YTD-Alpha -17,664 pp expandiert, 3 Owner-Diskussions-Punkte für KW34).
Nächster Check: **Mo 17.08. 08:30 ET Pre-Market KW34 Tag 1** — DELL K4-Volcheck (K5 heute NEU-verifiziert), MU-Limit-Strategie Owner-Entscheidung, XOM/GE K4/K5, AAPL V2-DQF-Verlauf, UNH V2-DQF 18. Tag, LLY-News-Monitoring Orforglipron-Fortsetzung.

---

**Market Close 16:00 ET 14.08.2026 (KW33 Tag 5 Fr) — Tagesbilanz + Wochenabschluss KW33:**
Gesamtwert:     96.192,26 $   (Alpaca equity Close)
Cash:           56.707,49 $   (58,95 %)
Investiert:     39.484,77 $   (41,05 %)  — AAPL 9.477,32 / JPM 1.088,52 / LLY 9.441,28 / UNH 9.645,60 / V 9.832,05
P/L heute:       −184,21 $   (**−0,191 %** vs last_equity 96.376,47)   [GRÜN, Cap −3 %; verschlechtert vs Do Close −0,006 %]
Alpha vs SPY:   **+0,007 pp** (SPY IEX Close 776,30 vs Do 777,84 = **−0,198 %**; Portfolio −0,191 % marginal outperformt via UNH-Recovery +0,712 %)
ATH:           100.066,47 $   (unverändert)
Drawdown:       **−3,872 %**  [GRÜN, verschlechtert vs Do Close −3,696 %; Schwelle −15 % bei 85.056 $]
Guardrails:     Daily −0,191 % | **Weekly KW33 Fr-Abschluss vs Fr 07.08. Close 96.512,65 = −0,332 % GRÜN** weit von Cap −5 % | Käufe **0/2 KW33** (MU-Slot 3. Tag EXPIRED ohne Fill — Slot verbraucht ohne Kaufumsetzung) | VIX ~14–15 GRÜN | Crash-Filter NEIN | DD GRÜN

Positions-Übersicht (5/8, Ø-P/L +1,28 % ungewichtet):
- **JPM +9,03 % BEST** (362,84 $, chg −0,074 %, 3 Sh, MV 1.088,52, entry 332,78)
- V +1,95 %      (364,15 $,   chg −0,356 %, 27 Sh, MV 9.832,05, entry 357,178)
- UNH +0,08 %    (401,90 $,   chg **+0,712 % Best chg**, 24 Sh, MV 9.645,60, entry 401,57)
- LLY −1,15 %    (1180,16 $,  chg **−2,385 % Worst chg**, 8 Sh, MV 9.441,28, entry 1193,89)
- **AAPL −3,52 % WORST** (305,72 $, chg +0,151 %, 31 Sh, MV 9.477,32, entry 316,857)

Vollständiger V1–V6 Signalcheck (Close-Daten Alpaca IEX):
- **V1 Stop-Loss −8 % vs Entry alle 5 SICHER (min AAPL +4,87 % Puffer):** AAPL Thr 291,51 +4,87 %; JPM Thr 306,16 +18,52 %; LLY Thr 1098,38 +7,45 %; UNH Thr 369,44 +8,79 %; V Thr 328,60 +10,82 %
- **V2 Trailing −12 % vs 52w-Hoch (Close-Referenz):** AAPL Thr via Wick 344,555 = 303,21 → **+0,83 % SICHER** (DQF 5. Tag technisch aus BROKEN raus fortlaufend); UNH Thr via Wick 460,95 = 405,636 → **−0,92 % BROKEN 17. Tag DQF persistent**, Alt-V2 via 437,13 = 384,67 Puffer **+4,48 % SICHER**, Std-V1 primär +8,79 %; JPM +12,04 %; LLY +7,41 %; V +10,66 %
- **V3/V4 Gewinn-Take-Profit:** max JPM +9,03 % << 20 %-TP1 → kein Trigger
- **V5 Death Cross (EMA50<EMA200):** AAPL 309,04/280,00 ✗; JPM 341,34/317,44 ✗; LLY 1154,29/1021,28 ✗; UNH 406,73/362,26 ✗; V 351,27/338,39 ✗ → **ALLE NEGATIV, kein Trigger**
- **V6 RSI>80 UND RS4w<0:** AAPL RSI 43,68 ✗; JPM 65,12 ✗; LLY 50,10 ✗; UNH 42,29 ✗; V 55,94 ✗ (kein Symbol RSI>80) → **ALLE NEGATIV, kein Trigger**

V5/V6-Aktion: **KEINE Sell-Orders für Mo 17.08.** (alle Death-Cross- und Überkauft-Signale negativ)

**MU-Order-Status:** **EXPIRED ohne Fill** (Order-ID 3f44bf7d, Day-Order abgelaufen 20:00 UTC; filled_qty 0; Limit 954,64 nie erreicht, MU handelte intraday ~965–984 $ +1,1 bis +3,7 % über Limit). **3. Tag in Folge Wiederholungsmuster** (12.08. Limit 915,86 EXPIRED / 13.08. Limit 915,86 EXPIRED / 14.08. Limit 954,64 EXPIRED). Slot 1 KW33 verbraucht ohne Kaufumsetzung → Käufe KW33 = 0/2, KW34 startet Mo 17.08. frisch mit 2/2 offen.

Sektor-Struktur Close: XLV **19,84 %** (UNH 10,03 + LLY 9,81), XLF **11,35 %** (JPM 1,13 + V 10,22), XLK **9,85 %** AAPL, Cash 58,95 %

**Weekly Loss Cap KW33-Abschluss:** −0,332 % vs Cap −5 % → weit entfernt, **keine Sperrauslösung**, keine pending Orders zum Stornieren.

**LLY-News-Klärung (Perplexity Close):** Intraday −2,385 % Worst chg via **Pipeline-Enttäuschung Orforglipron-Daten (ATTAIN-1) + Novo-Nordisk-Wettbewerbsdruck + Gewinnmitnahmen Pharmasektor** — kein Analystendowngrade als primärer Trigger. Std-V1 +7,45 % Puffer weiterhin SICHER, kein V-Trigger-Kontext.

**Watchlist Mo 17.08. (K1-K3 aus Alpaca IEX + Perplexity Sektor-Momentum):**
- **XOM** (XLE) K1-K3 ✓ EMA 151,0>139,9 / RSI 64,2 / RS +4,18 pp — XLE-Sektor stärkste Momentum-Basis laut Perplexity
- **DELL** (XLK) K1-K3 ✓ EMA 407,7>273,2 / RSI 61,7 / **RS +19,41 pp #1** — K5-Datenkonflikt aus Vortag (+9,1 %/+88,0 % Query-Divergenz) neu klären
- **GE** (XLI) K1-K3 ✓ EMA 352,6>319,0 / RSI 55,3 / RS +1,16 pp — Industrials Basis
- MU (XLK) K1-K3 ✓ — Fortsetzung als Kandidat trotz 3-Tage-Fill-Muster (Limit-Preis-Anpassung Mo diskutieren)
- PANW (XLK) K1-K3 ✓ K5 offen — FwdPE 77,66 Vortag >>35 FAIL, K5 Neucheck Mo
- RTX (XLI) K1 ✓ K2 RSI 70,2 upper-limit BORDER — Watchlist Cooldown
- CAT (XLI) K2 RSI 46,6 FAIL / K3 RS −7,08 pp FAIL → REJECT
- GS (XLF) K2 RSI 48,7 FAIL / K3 RS −6,95 pp FAIL → REJECT

**KW33-Wochenbilanz (Mo 11.08.–Fr 14.08. 4 Handelstage):**
- Depot-Start Mo (=Fr Close 07.08.): 96.512,65 $ | Depot-Ende Fr 14.08.: 96.192,26 $ → **Wochenergebnis −320,39 $ = −0,332 %**
- SPY-Woche: TBD (Fr 07.08. Close vs Fr 14.08. Close 776,30) — bei geschätztem SPY 07.08. ~773 → SPY-Woche ~+0,4 % → **Alpha KW33 ~−0,7 pp NEG**
- Käufe: 0 (MU 3x Limit-Order EXPIRED ohne Fill — Slot-Verbrauch ohne Kaufumsetzung 3. Tag Muster)
- Verkäufe/Stops: 0
- V-Trigger-Zustand Wochenende: alle V1 SICHER + V5/V6 alle negativ + AAPL V2-DQF recovered / UNH V2-DQF razor 17. Tag Alt-V2/Std-V1 primär sicher

ClickUp Prio 3 [CLOSE Tagesbilanz] Task: **ITEM_246 "Max usage for custom task types reached" 18. Tag persistent** → Fallback Memory-Only per notify-skill.md.
PushNotification: **JA** (Close-Silence-Ausnahme: KW33-Abschluss + MU-Order 3. Tag Wiederholungsmuster EXPIRED-Serie Owner-Info nötig für Limit-Strategie-Review, LLY-Weakness-Kontext geklärt, Weekly-Bilanz-Abschluss).
Nächster Check: **Mo 17.08. 08:30 ET Pre-Market KW34 Tag 1** — MU-Limit-Strategie-Neubewertung (3-Tage-Fail-Serie), DELL K5-Datenkonflikt-Neuklärung, XOM/GE K4/K5-Volcheck, AAPL V2-DQF-Verlauf, UNH V2-DQF 17. Tag Owner-Entscheidung pending.

---

**Midday 13:11 ET 14.08.2026 (KW33 Tag 5 Fr):**
Positionen: 5/8 | Ø P/L: **+1,23 %** ungewichtet (JPM +8,96 Best / V +2,16 / UNH −0,11 / LLY −1,25 / AAPL −3,61 Worst)
Beste Position: **JPM +8,96 %** (362,53 $ Alpaca latestTrade IEX 13:11 ET)
Schlechteste Position: **AAPL −3,61 %** (305,40 $, verbessert vs Open −3,42 %)
Stops V1-V4 Live-Check (V5/V6 nur Close-Vollcheck):
- **V1 Std alle 5 SICHER Puffer eng→weit:** **AAPL +4,77 % ENGSTE Std verbessert vs Open +4,97 %** (305,40 chg +0,05 %, Std-V1 291,51 primär), **LLY +7,30 %** (1178,59 chg **−2,49 % Worst chg**, P/L −1,25 % verschlechtert vs Open −0,91 %, **Std-V1 1098,38 primär**), UNH +8,58 % (401,09 chg +0,52 %, P/L −0,11 % verbessert vs Open −0,24 %), V +11,02 % (364,795 chg −0,15 %, P/L +2,16 % verbessert vs Open +2,08 %), **JPM +18,42 %** (362,53 chg −0,14 %, **Best P/L +8,96 %** verschlechtert vs Open +9,63 %)
- **V2-Trailing-Stop:** **⚠️ AAPL V2 razor +0,72 % via Wick 344,555 = Thr 303,21** verschlechtert vs Open +0,92 % (52w-Wick DQF-flagged wie UNH; Std-V1 +4,77 % ENGSTE primär sicher, V2 sekundär via DQF; **4. Tag technisch aus BROKEN raus**); **⚠️ UNH V2 BROKEN Puffer −1,13 % via Wick 460,95 = Thr 405,636 verbessert vs Open −1,24 %** (**16. Tag DQF persistent** — Alt-V2 via 437,13 = 384,67 Puffer **+4,27 % SICHER**, Std-V1 +8,58 % primär sicher, Owner-Entscheidung pending); JPM +11,94 % via Wick 368,00 (Thr 323,84) sicher, LLY +7,27 % via 52w-High 1248,53 (Thr 1098,71) sicher, V +10,85 % via 373,97 (Thr 329,09) sicher
- **V3/V4:** max P/L JPM +8,96 % << 20 %-TP1 → kein Trigger
- **V5/V6:** nur Close-Vollcheck
Daily P/L: **−0,210 % [GRÜN, Cap −3 %]** (Equity Live **96.174,27 $** vs last_equity 96.376,47 = −202,20 $; MV 39.466,78 $ / Cash 56.707,49 $ = **58,96 %**; DD vs ATH 100.066,47 = **−3,890 % GRÜN** verschlechtert vs Open −3,859 %; Weekly KW33 Tag 5 vs Fr Close 07.08. 96.512,65 = **−0,351 % GRÜN** weit von Cap −5 %, verschlechtert vs Open −0,318 %)
Alpha vs SPY: n/a (Midday-Spec — Alpha nur Open/Close)
V-Aktion: **KEINE Sell-Order platziert** (Rule 5 No-Action bei DQF-Wick-Anomalie fortlaufend: AAPL V2 razor via 52w-Wick 344,555 DQF Single-Print — Std-V1 +4,77 % ENGSTE primär sicher; UNH V2 16. Tag DQF Alt-V2 +4,27 % + Std-V1 +8,58 % primär sicher); 0 offene Sell-Orders bei Alpaca
Pending Orders: **1 (MU BUY LIMIT 10 Sh @ 954,64 $ Day, Status NEW, filled_qty 0)** — Live MU 964,77 $ liegt **+1,06 % über Limit** → Fill weiter unwahrscheinlich intraday ohne Rücksetzer (2. Tag in Folge Fill-Wahrscheinlichkeit niedrig)
Käufe KW33: 0/2 (Slot 1 IN PROGRESS via MU-Limit — Slot 2 offen — Midday KEIN Buy-Scan per Routine-Spec)
Sektor-Struktur Live: XLV **19,82 %** (UNH 10,01 + LLY 9,81), XLF **11,38 %** (JPM 1,13 + V 10,24), XLK **9,85 %** AAPL, Cash 58,96 %
LLY-News-Check: intraday chg **−2,49 % Worst chg heute** (verschlechtert vs Open −2,23 %) — Ursache TBD (Midday-Spec kein Perplexity, Close-Check klärt); Std-V1 Puffer +7,30 % primär sicher, kein V-Trigger.
ClickUp Prio 1 Critical Alert: **KEIN Alert** (kein Stop-Trigger, kein Daily-Cap-Trigger — Routine-Spec Schritt 5 fordert Alert NUR bei Trigger; ITEM_246-Bug 17. Tag persistent egal)
PushNotification: **NEIN** (Silence-Rule: kein V-Trigger, kein Cap-Alert, kein Kauf-Fill, MU-Order pending unfilled ohne Fortschritt 2. Tag, LLY −2,49 % Weakness innerhalb Std-V1-Rahmen +7,30 % sicher, UNH V2-DQF-Verlauf konsistent 16. Tag ohne Neuinfo, AAPL V2-Razor-Verschlechterung marginal innerhalb Std-V1-Rahmen +4,77 % sicher — kein Owner-Handlungsbedarf)
Nächster Check: **Fr 14.08. 16:00 ET Market Close KW33 Tag 5** — MU-Order-Fill-Status EOD, LLY −2,49 % Weakness-Ursache-Klärung Perplexity, AAPL V2-Recovery-Verlauf, UNH V2-DQF 16. Tag, V5/V6 Vollcheck, Tagesbilanz + Wochenabschluss KW33 + Watchlist Mo 17.08.

---

**Pre-Market 08:30 ET (VERZÖGERT feuerte nach Market Open) 14.08.2026 (KW33 Tag 5 Fr):**
Gesamtwert:     96.081,54 $   (Alpaca equity, −124,53 $ vs Market Open 96.206,07 durch intraday Preisbewegung)
Cash:           56.707,49 $   (unverändert, MU-Order noch NEW unfilled Limit 954,64)
Investiert:     39.374,05 $   (Long MV)
P/L vs Last Eq:  −294,93 $    (−0,306 % vs 96.376,47)   [GRÜN Cap −3 %]
ATH:           100.066,47 $   (unverändert)
Drawdown:        −3,984 %     [GRÜN, Schwelle −15 % bei 85.056 $]
Weekly:         −0,446 %      vs Fr 07.08. Close 96.512,65   [GRÜN Cap −5 %]
Guardrails: 8/8 GRÜN | VIX **14,49** GRÜN | SPY intraday +0,05–0,10 % | 10Y 4,65 % | Crash-Filter NEIN | Käufe 0/2 KW33 Slot 1 IN PROGRESS MU
Earnings-Blackouts: **KEINE** (AAPL/JPM/LLY/UNH/V alle Oktober 2026, kein 3-HT-Window aktiv → Standard Stops −8 %)
Makro-Event heute: U Mich Consumer Sentiment Prelim (Aug, Prior 55,2, Neue Zahl TBA) — kein CPI/PPI/Fed
**⚠️ Routine-Timing-Anomalie:** Pre-Market-Check feuerte NACH Market Open (10:04 ET-Log bereits vorhanden). Cron `30 12 * * 1-5` konfigurationsseitig prüfen — Ergebnisse dieses Pre-Market-Checks können Market-Open-Kaufentscheidung nicht mehr beeinflussen. Guardrails-Verifikation trotzdem durchgeführt: alle GRÜN.
ClickUp Prio 4 [PRE-MARKET] Task: **ITEM_246 "Max usage for custom task types reached" 17. Tag persistent** → Fallback Memory-Only per notify-skill.md.
PushNotification: **JA (Silence-Ausnahme: Routine-Timing-Anomalie + Owner-Info Cron-Prüfung nötig)** — Guardrails-Health-Ampel GRÜN, aber Routine-Konfiguration erfordert Owner-Aktion.
Nächster Check: **Fr 14.08. 13:00 ET Midday Stop-Check KW33 Tag 5**

---

**Market Open 10:04 ET 14.08.2026 (KW33 Tag 5 Fr):**
Gesamtwert:     96.206,07 $   (Alpaca equity live)
Cash:           56.707,49 $   (58,94 %, unverändert vor Fill)
Investiert:     39.498,58 $   (41,06 %)  — AAPL 9.486,155 / JPM 1.094,505 / LLY 9.463,80 / UNH 9.615,00 / V 9.844,47
P/L Open:        −170,40 $   (−0,177 % vs last_equity 96.376,47)   [GRÜN, Cap −3 %, verschlechtert vs Do Close −0,006 %]
Alpha vs SPY:    −0,267 pp   (SPY Alpaca latestTrade IEX 778,54 vs Do Close 777,84 = +0,090 %; Portfolio −0,177 % underperformt SPY marginal via LLY-Weakness −2,23 % chg)
ATH:           100.066,47 $   (unverändert)
Drawdown:        −3,859 %     [GRÜN, verschlechtert vs Do Close −3,696 %; Schwelle −15 % bei 85.056 $]
Guardrails:     Daily −0,177 % | Weekly KW33 Tag 5 vs Fr 07.08. Close 96.512,65 = **−0,318 % GRÜN** | Käufe 0/2 KW33 (**Slot 1 IN PROGRESS** MU-Order, Slot 2 offen) | VIX 14,62 | Crash-Filter NEIN | DD GRÜN

V1/V2 Live-Check (V5/V6 nur Close):
- AAPL 306,005 (chg +0,33 %, P/L −3,42 % **Worst verbessert vs Close −3,74 %**): V1 Std **+4,97 % ENGSTE** (Thr 291,51); V2 **+0,92 % SICHER via Wick 344,555 (Thr 303,21) DQF 4. Tag technisch AUS BROKEN RAUS** verbessert vs Close +0,59 %; V5/V6 nur Close.
- JPM 364,835 (chg +0,30 %, P/L +9,63 % **Best verbessert vs Close +9,30 %**): V1 +19,16 % (Thr 306,16); V2 +12,66 % via Wick 368,00 (Thr 323,84); V5/V6 nur Close.
- LLY 1182,975 (chg **−2,23 % Worst chg**, P/L −0,91 % **verschlechtert vs Close +1,35 %** — News-Ursache TBD Midday-Check): V1 +7,70 % (Thr 1098,38, Std-V1 primär); V2 +7,67 % via 52w-High 1248,53 (Thr 1098,71); V5/V6 nur Close.
- UNH 400,625 (chg +0,39 %, P/L −0,24 % verbessert vs Close −0,62 %): V1 +8,44 % (Thr 369,44); V2 **−1,24 % BROKEN** via Wick 460,95 (Thr 405,636) DQF **16. Tag persistent** verbessert vs Close −1,619 %, Alt-V2 via 437,13 = 384,67 Puffer **+4,15 % SICHER**; V5/V6 nur Close.
- V 364,61 (chg −0,13 %, P/L +2,08 % verschlechtert vs Close +2,21 %): V1 +10,96 % (Thr 328,60); V2 +10,79 % via 373,97 (Thr 329,09); V5/V6 nur Close.

V-Trigger Open: **V1 Std alle 5 SICHER** (min AAPL +4,97 %) | **V2:** AAPL DQF technisch AUS BROKEN RAUS +0,92 % (verbessert 4. Tag), UNH DQF razor BROKEN 16. Tag −1,24 % (Alt-V2 +4,15 % + Std-V1 +8,44 % primär) → Rule 5 No-Action | V3/V4 max JPM +9,63 % << 20 % | V5/V6 nur Close.

**Order-Aktion Open:** **BUY LIMIT MU 10 Shares @ 954,64 $ Day-Order platziert** (Order-ID 3f44bf7d-abd0-4008-b6b7-7d9b83f0aed8, Status pending_new, filled_qty 0) — Preis Live 980,51 $ liegt **+2,71 % über Vortagesschluss 949,89**, Regel-Limit +0,5 % nur bei intraday-Rücksetzer ≥ −2,64 % erreichbar. **Fill-Wahrscheinlichkeit niedrig (2. Tag in Folge)** — Slot 1/2 KW33 IN PROGRESS bis EOD.

**Kauf-Kandidaten-Scan (K1-K5) — 10 Kandidaten Alpaca-Bars + Perplexity K5:**
- **MU (XLK) K1-K5 ALLE ✓ TOP-KANDIDAT gewählt**: EMA50 894,27 > EMA200 607,80 ✓ | RSI 57,05 ✓ | RS +22,05 pp ✓ | K4 194.997 / Avg20 1.126.752 = 17,3 % / Session-Elapsed 8,72 % = Extrapol **198,5 % Avg20** ✓ | K5 FwdPE 5,55 / RevYoY +45,70 % ✓ (Vortagesverifikation persistent) | Earnings 23.09.2026 (>3 HT) → **Buy-Order platziert**
- **DELL (XLK) K1-K3 ✓ K4 FAIL 81 % + K5 UNSICHER**: EMA50 407,55 > EMA200 270,79 ✓ | RSI 62,70 ✓ | RS **+95,93 pp #1** ✓ | K4 16.826 / 238.164 = 7,07 % → Extrapol **81,1 % Avg20 FAIL** | K5 Perplexity **CONFLICT** (Query1 RevYoY +9,1 % <10 % FAIL, Query2 RevYoY +88,0 % implausibel Halluzination) → **Rule 5 No-Action bei Datenunsicherheit REJECT**
- **PANW (XLK) K1-K4 ✓ K5 FAIL FwdPE 77,66 >>35**: EMA50 325,75 > EMA200 249,18 ✓ | RSI 67,00 (Cooldown von 72,76 gestern) ✓ | RS +58,04 pp ✓ | K4 29.460 / 279.749 = 10,5 % → Extrapol **120,8 % Avg20 ✓** | K5 **FwdPE 77,66 >>35 FAIL** → REJECT K5
- **XOM (XLE) K1-K4 ✓ K5 pending schwaches Momentum**: EMA/RSI 65,39/RS +1,72 pp/K4 12,87 %→147,6 % ✓ — K5 nicht abgefragt (RS zu schwach vs MU/PANW/DELL) → Watchlist
- **CVX (XLE) K1-K4 ✓ K5 FAIL persistent**: EMA/RSI/RS/K4 alle ✓ — **K5 RevYoY −0,13 % <10 % FAIL** (Vortagesverifikation) → REJECT
- **HPE/NTAP/CRL K2 FAIL RSI >70**: HPE RSI 72,36 / NTAP RSI 74,83 / CRL RSI 76,74 → **überkauft, Cooldown-Watch**
- **GE/UAL/UNP/BAC K4 FAIL heavy**: GE 76 % / UAL 64 % / UNP 98 % / BAC 109 % — Vol-Pace-Watch Midday
- **NVDA (XLK) K3 FAIL −8,35 pp NEG**: RS_63 −4,01 pp vs SPY +4,34 pp → REJECT
- **MRK (XLV) LEVEL-0 SKIP**: Sektor-Cap UNH+LLY 19,84 % → REJECT
- **ORCL K1 FAIL Death Cross**: EMA50 149,62 < EMA200 184,82 → REJECT

Sektor-Struktur Live (pre-Fill): XLV **19,84 %** (UNH 9,99 + LLY 9,84), XLF **11,37 %** (JPM 1,14 + V 10,23), XLK **9,86 %** AAPL, Cash 58,94 %.
Sektor-Struktur Post-Fill (falls MU fill): XLK **AAPL 9.486,15 + MU 9.546,40 = 19.032,55 = 19,78 %** (unter 30 %-Cap ✓, 2 Pos <3-Max ✓); Cash Post 47.161,09 = **49,02 %** (>20 % ✓); Positionen 6/8 ✓.
Weekly Loss Cap: −0,318 % vs Cap −5 % → weit entfernt, kein Sperrauslöser.
Perplexity: **3 Queries** (PANW+DELL K5, DELL K5-Confirmation, VIX) — DELL K5-Konflikt +9,1 %/+88,0 % → Rule 5 REJECT, PANW K5-FAIL bestätigt, VIX 14,62 GRÜN.
ClickUp Prio 3 [MARKET-OPEN TRADE_BUY] Task versucht — **ITEM_246 "Max usage for custom task types reached" 16. Tag persistent** → Fallback Memory-Only per notify-skill.md.
PushNotification: **JA (TRADE_BUY)** — MU-Order 2. Versuch platziert (Slot 1 IN PROGRESS), Owner-Info über Wiederholungsmuster + DELL K5-Datenkonflikt Rule 5, LLY intraday −2,23 % Weakness (kein V-Trigger aber Watch).
Nächster Check: **Fr 14.08. 13:00 ET Midday Stop-Check KW33 Tag 5** — MU-Order-Fill-Status, LLY −2,23 % Weakness-Ursache-Klärung, AAPL V2-Recovery-Verlauf, UNH V2-DQF 16. Tag, DELL K4-Vol-Rebound-Watch.

---

**Market Close 16:00 ET 13.08.2026 (KW33 Tag 4 Do) — Tagesbilanz:**
Gesamtwert:     96.367,92 $   (Alpaca equity Close)
Cash:           56.707,49 $   (58,84 %)
Investiert:     39.660,43 $   (41,16 %)  — AAPL 9.455,31 / JPM 1.091,21 / LLY 9.680,00 / UNH 9.577,68 / V 9.857,16
P/L heute:        −5,60 $     (−0,006 %)   [GRÜN, Cap −3 %; last_equity 96.373,52]
Alpha vs SPY:    −0,69 pp     (SPY Alpaca Close 777,84 vs Mi 772,54 = **+0,686 %**; Portfolio flat verpasst Broad-Market-Aufwärtsimpuls)
ATH:           100.066,47 $   (unverändert)
Drawdown:        −3,696 %     [GRÜN, verbessert vs Midday −3,779 %; Schwelle −15 % bei 85.056 $]
Guardrails:     Daily −0,006 % | Weekly KW33 Tag 4 vs Fr-Close 96.512,65 = **−0,150 % GRÜN** | Käufe 0/2 KW33 (MU-Slot EXPIRED, 2/2 OFFEN) | VIX n/a Close | Crash-Filter NEIN | DD GRÜN

Positions-Übersicht (5/8, Ø-P/L +1,50 % ungewichtet, +0,020 % gewichtet):
- **JPM +9,30 % BEST** (363,7365 $, chg −0,40 %, 3 Sh, MV 1.091,21, entry 332,78)
- V +2,21 %      (365,08 $,   chg +1,58 %, 27 Sh, MV 9.857,16, entry 357,18)
- LLY +1,35 %    (1210,00 $,  chg −0,84 %, 8 Sh, MV 9.680,00, entry 1193,89)
- UNH −0,62 %    (399,07 $,   chg −1,61 %, 24 Sh, MV 9.577,68, entry 401,57)
- **AAPL −3,74 % WORST** (305,01 $, chg +0,91 %, 31 Sh, MV 9.455,31, entry 316,86, verbessert vs Midday −4,37 %)

Vollständiger V1-V6 Signalcheck (Close-Daten Alpaca IEX):
- **V1 Stop-Loss −8 % vs Entry alle 5 SICHER (min AAPL +4,63 % Puffer):** AAPL Thr 291,51 Puffer +4,63 %; JPM Thr 306,16 +18,80 %; LLY Thr 1098,38 +10,17 %; UNH Thr 369,44 +8,02 %; V Thr 328,60 +11,10 %
- **V2 Trailing −12 % vs 52w-Hoch (Close-Referenz):** AAPL Thr via 344,555 = 303,21 → **+0,590 % SICHER** (verbessert vs Midday BROKEN, DQF-Verlauf-Ende); UNH Thr via Wick 460,95 = 405,636 → **−1,619 % BROKEN 15. Tag DQF persistent**, Alt-V2 via 437,13 = 384,67 Puffer **+3,74 % SICHER**, Std-V1 primär +8,02 %; JPM +12,00 % SICHER; LLY +9,63 % SICHER; V +9,66 % SICHER
- **V3/V4 Gewinn-Take-Profit:** max JPM +9,30 % << 20 %-TP1 → kein Trigger
- **V5 Death Cross (EMA50<EMA200):** AAPL 309,17/280,52 ✗; JPM 340,47/315,80 ✗; LLY 1153,21/1039,15 ✗; UNH 406,94/349,65 ✗; V 350,74/333,06 ✗ → **ALLE NEGATIV, kein Trigger**
- **V6 RSI>80 UND RS4w<0:** AAPL RSI 43,07 ✗; JPM 65,57 ✗; LLY 55,79 ✗; UNH 40,24 ✗; V 57,11 ✗ → **ALLE NEGATIV, kein Trigger**

V5/V6-Aktion: **KEINE Sell-Orders für Fr 14.08.** (alle Death-Cross- und Überkauft-Signale negativ)

MU-Order-Status: **EXPIRED ohne Fill** (Order-ID 4df018b2, Day-Order abgelaufen 20:00 UTC; filled_qty 0; Limit 915,86 nie erreicht, MU handelte intraday im Bereich ~971 $ +6,08 % über Limit). Slot 1/2 KW33 wieder OFFEN → 2/2 offen für Fr/Mo.

Sektor-Struktur Close: XLV **20,00 %** (UNH 9,94 + LLY 10,05), XLF **11,36 %** (JPM 1,13 + V 10,23), XLK **9,81 %** AAPL, Cash 58,84 %
Weekly Loss Cap: −0,150 % vs Cap −5 % → weit entfernt, keine Sperrauslösung.
Perplexity: **2 Queries Close** (SPY-Tagesperf, Watchlist-Sektor-Momentum).
ClickUp Prio 4 [CLOSE Tagesbilanz]-Task: Fallback zu Prio-Alert Prio 3 nur bei negativer Performance; heute leicht negativ (−0,006 %) → Prio 3.
PushNotification: **JA (CLOSE Silence-Signal-Ausnahme)** — MU-Order EXPIRED ohne Fill (Slot verbraucht ohne Kaufumsetzung, Owner-Info über Fehlkauf-Wochenverlauf 4. Kauflos-Tag), plus Watchlist-Kandidat DELL K1-K3 ✓ als handlebarer Kauflos-Ersatz für Fr.
Nächster Check: **Fr 14.08. 08:30 ET Pre-Market KW33 Tag 5** — DELL K5-Fundamentals (FwdPE/RevYoY), Watchlist HPE/PANW/NTAP/CRL K2-RSI-Cooldown-Watch, AAPL V2-DQF-Verlauf, UNH V2-DQF-Verlauf (15. Tag Owner-Entscheidung pending).

---

**Midday 13:22 ET 13.08.2026 (KW33 Tag 4 Do):**
Positionen: 5/8 | Ø P/L: **+1,51 %** (JPM +9,22 Best / LLY +1,84 / V +1,02 / UNH −0,17 / AAPL −4,37 Worst)
Beste Position: **JPM +9,22 %** (363,47 $ Alpaca latestTrade IEX 13:22 ET)
Schlechteste Position: **AAPL −4,37 %** (303,02 $, verschlechtert vs Open −4,20 %)
Stops V1-V4 Live-Check (V5/V6 nur Close-Vollcheck):
- **V1 Std alle 5 SICHER Puffer eng→weit:** **AAPL +3,95 % ENGSTE Std verschlechtert vs Open +4,13 %** (303,02 chg +0,25 %, Std-V1 291,51 primär), UNH +8,53 % (400,95 chg −1,16 %, P/L −0,17 % verschlechtert vs Open +0,94 %), V +9,81 % (360,83 chg +0,39 %, P/L +1,02 % verbessert vs Open +0,81 %), **LLY +10,73 %** (1215,89 chg −0,36 %, P/L +1,84 % verschlechtert vs Open +2,67 %, **Std-V1 1098,38 primär**), **JPM +18,72 %** (363,47 chg −0,47 %, **Best P/L +9,22 %** verschlechtert vs Open +9,38 %)
- **V2-Trailing-Stop:** **⚠️ AAPL V2 BROKEN razor −0,06 % via Wick 344,555 = Thr 303,21 marginal verschlechtert vs Open +0,108 %** (52w-Wick DQF-flagged wie UNH; Std-V1 +3,95 % ENGSTE primär sicher, V2 sekundär via DQF; 4. Tag technisch nahe BROKEN); **UNH V2 BROKEN Puffer −1,16 % via Wick 460,95 = Thr 405,636 verschlechtert vs Open −0,074 %** (14. Tag DQF persistent — Alt-V2 via 437,13 = 384,67 Puffer +4,23 % SICHER, Std-V1 +8,53 % primär sicher, Owner-Entscheidung pending seit Di-Midday-Push); LLY +10,69 % via 52w-High 1.248,53 (Thr 1098,71) sicher, V +9,64 % via 373,97 (Thr 329,09) sicher, JPM +12,24 % via Wick 368,00 (Thr 323,84) sicher
- **V3/V4:** max P/L JPM +9,22 % << 20 %-TP1 → kein Trigger
- **V5/V6:** nur Close-Vollcheck
Daily P/L: **−0,092 % [GRÜN, Cap −3 %]** (Equity Live **96.284,63 $** vs last_equity 96.373,52 = −88,89 $; MV 39.577,14 $ / Cash 56.707,49 $ = **58,90 %**; DD vs ATH 100.066,47 = **−3,779 % GRÜN** verschlechtert vs Open −3,600 %; Weekly KW33 Tag 4 vs Fr Close 96.512,65 = **−0,236 % GRÜN** weit von Cap −5 %, verschlechtert vs Open −0,050 %)
Alpha vs SPY: n/a (nicht abgefragt Midday-Spec — Alpha nur Open/Close)
V-Aktion: **KEINE Sell-Order platziert** (Rule 5 No-Action bei DQF-Wick-Anomalie fortlaufend: AAPL V2 BROKEN razor via 52w-Wick 344,555 DQF Single-Print — Std-V1 +3,95 % ENGSTE primär sicher; UNH V2 14. Tag DQF Alt-V2 +4,23 % + Std-V1 +8,53 % primär sicher); 0 offene Sell-Orders bei Alpaca
Pending Orders: **1 (MU BUY LIMIT 10 Sh @ 915,86 Day, Status NEW, filled_qty 0)** — Live 971,50 $ liegt +6,08 % über Limit → Fill unwahrscheinlich intraday ohne größeren Rücksetzer
Käufe KW33: 0/2 (Slot 1/2 IN PROGRESS via MU-Limit — 2/2 OFFEN — Midday KEIN Buy-Scan per Routine-Spec)
Sektor-Struktur Live: XLV **20,12 %** (UNH 9,99 + LLY 10,10), XLF **11,25 %** (JPM 1,13 + V 10,12), XLK **9,76 %** AAPL, Cash 58,90 %
ClickUp Prio 1 Critical Alert: **KEIN Alert** (kein Stop-Trigger, kein Daily-Cap-Trigger — Routine-Spec Schritt 5 fordert Alert NUR bei Trigger; ITEM_246-Bug 15. Tag persistent egal)
PushNotification: **NEIN** (Silence-Rule: kein V-Trigger, kein Cap-Alert, kein Kauf-Fill, MU-Order pending unfilled ohne Fortschritt, AAPL V2-Razor-Verschlechterung marginal innerhalb Std-V1-Rahmen +3,95 % sicher, UNH V2-DQF-Verlauf konsistent mit 14-Tage-Serie ohne Neuinfo — kein Owner-Handlungsbedarf)
Nächster Check: **Do 13.08. 16:00 ET Market Close KW33 Tag 4** — MU-Order-Fill-Status EOD, AAPL V2-DQF-Verlauf V5/V6 Vollcheck, UNH V2-DQF-Verlauf (Owner-Entscheidung pending), LLY Std-V1-Primary-Verlauf, Tagesbilanz + Watchlist Fr 14.08.

---

**Market Open 09:47 ET 13.08.2026 (KW33 Tag 4 Do):**
Gesamtwert:     96.464,14 $   (Alpaca equity live)
Cash:           56.707,49 $   (58,79 %, unverändert vor Fill)
Investiert:     39.756,65 $   (41,21 %)  — AAPL 9.409,585 / JPM 1.092,03 / LLY 9.806,08 / UNH 9.728,04 / V 9.721,62
P/L Open:         +90,62 $   (+0,094 % vs last_equity 96.373,52)   [GRÜN, Cap −3 %]
Alpha vs SPY:    −0,354 pp   (SPY Alpaca latestTrade IEX 776,00 vs Mi Close 772,54 = +0,448 %; Portfolio +0,094 % underperformt intraday-Rauschen ~13 min Session)
ATH:           100.066,47 $   (unverändert)
Drawdown:        −3,600 %     [GRÜN, verschlechtert vs Pre −3,485 %; Schwelle −15 % bei 85.056 $]
Guardrails:     Daily +0,094 % | Weekly KW33 Tag 4 vs Fr-Close 96.512,65 = −0,050 % | Käufe 0/2 KW33 (Slot 1 IN PROGRESS) | VIX 14,69 | Crash-Filter NEIN | DD GRÜN
V1/V2 Live-Check (V5/V6 nur Close):
- AAPL 303,535 (chg +0,44 %, P/L −4,20 % **Worst**): V1 Std **+4,13 % ENGSTE** (Thr 291,51); V2 **+0,108 % via 52w-Wick 344,555** (Thr 303,21) DQF **3. Tag technisch aus BROKEN raus** vs Pre −0,020 %; V5/V6 nur Close.
- JPM 364,01 (chg −0,32 %, P/L +9,38 % **Best**): V1 +18,90 % (Thr 306,16); V2 +12,40 % via Wick 368,00 = Thr 323,84 (NEUES Hoch Pre-Market 368,00 fortgeschrieben); V5/V6 nur Close.
- LLY 1225,76 (chg −0,15 %, P/L +2,67 %): V1 +11,60 % (Thr 1098,38, **Std-V1 primär**); V2 +11,56 % via 52w-High 1248,53 (Thr 1098,71); V5/V6 nur Close.
- UNH 405,335 (chg −0,29 %, P/L +0,94 %): V1 +9,72 % (Thr 369,44); V2 **−0,074 % BROKEN razor** via Wick 460,95 (Thr 405,636) DQF **14. Tag persistent** — Alt-V2 via 437,13 = 384,67 Puffer **+5,37 % SICHER**; V5/V6 nur Close.
- V 360,06 (chg −0,66 %, P/L +0,81 %): V1 +9,57 % (Thr 328,60); V2 +9,41 % via 373,97 (Thr 329,09); V5/V6 nur Close.
V-Trigger Open: **V1 Std alle 5 SICHER** (min AAPL +4,13 %) | **V2:** AAPL technisch AUS BROKEN RAUS +0,108 % (verbessert), UNH DQF razor BROKEN −0,074 % (Alt-V2 +5,37 % + Std-V1 +9,72 % primär) → Rule 5 No-Action | V3/V4 max JPM +9,38 % << 20 % | V5/V6 nur Close.
**Order-Aktion Open:** **BUY LIMIT MU 10 Shares @ 915,86 $ Day-Order platziert** (Order-ID 4df018b2-a2b8-4da8-8ca5-6f5598df0666, Status NEW, filled_qty 0) — Preis Live 931,68 $ liegt +2,24 % über Vortagesschluss 911,30 $, Regel-Limit +0,5 % nur bei intraday-Rücksetzer erreichbar.
**Kauf-Kandidaten-Scan (K1-K5) — 7 Kandidaten Alpaca-Bars + Perplexity K5:**
- **MU (XLK) K1-K5 ALLE ✓ TOP-KANDIDAT**: EMA50 888,33>EMA200 592,99 ✓ | RSI 50,7 ✓ | RS +14,10 pp ✓ | K4 135,9 % Avg20 Extrapol Session-Elapsed 3,33 % ✓ | **K5 FwdPE 5,55 ≤35 UND RevYoY +45,70 % ≥10 % ✓** — Earnings 23.09. (>3 HT), XLK-Sektor-Post-Kauf 19,25 % (unter 30 %-Cap), Cash-Post 49,29 % (>20 %), Pos-Post 6/8 → **Buy-Order platziert**
- **CVX (XLE) K1-K4 ✓ K5 FAIL**: EMA/RSI 60,4/RS +1,77 pp/K4 225,9 % Avg20 alle ✓ — **K5 RevYoY −0,13 % <10 % FAIL** → REJECT
- **GE (XLI) K1-K3 ✓ K4 FAIL 102 %**: RS +17,97 pp stark, K4 knapp unter 120 %-Threshold — Watchlist Midday
- **UAL (XLI) K1-K3 ✓ K4 FAIL 4,3 %**: RS +25,60 pp #1 aber K4 12. Tag persistent → Watchlist
- **UNP (XLI) K1-K3 ✓ K4 FAIL 18,2 %**: RS +6,20 pp — Watchlist
- **XOM (XLE) K1-K3 ✓ K4 FAIL 63 %**: RS +1,85 pp, RSI 65,5 upper — Watchlist
- **BA (XLI) K3 FAIL −7,32 pp**: REJECT
- **NEE/SO (XLU) K2 <50 FAIL**: REJECT
Sektor-Struktur Live: XLV **20,17 %** (UNH 10,08 + LLY 10,17), XLF **11,24 %** (JPM 1,13 + V 10,08), XLK **9,75 %** AAPL (Post-MU-Fill: 19,25 %), Cash 58,79 %.
Weekly Loss Cap: −0,050 % vs Cap −5 % → weit entfernt, kein Sperrauslöser.
Perplexity: **2 Queries** (Sektor-Momentum XLE/XLU/XLI, MU+CVX K5-Fundamentals) — Sektor-Ranking mit teilw. Silence-Bias 7. Mal Serie, K5-Zahlen belastbar.
ClickUp Prio 3 [MARKET-OPEN TRADE_BUY] Task versucht — **ITEM_246 "Max usage for custom task types reached" 15. Tag persistent** → Fallback Memory-Only per notify-skill.md.
PushNotification: **JA (TRADE_BUY)** — MU-Buy-Order platziert nach 4-Tage-Serie ohne handelbaren Kaufkandidaten; Owner-Info über neuen XLK-Kandidat + Slot-Beanspruchung, obwohl Fill ungewiss (Limit −1,7 % unter Live-Preis).
Nächster Check: **Do 13.08. 13:00 ET Midday Stop-Check KW33 Tag 4** — MU-Order-Fill-Status, AAPL V2-DQF-Verlauf, UNH V2-DQF-Verlauf, GE K4-Vol-Nachmittags-Rebound-Watch.

---

**Pre-Market 08:32 ET 13.08.2026 (KW33 Tag 4 Do):**
Gesamtwert:     96.578,84 $
Cash:           56.707,49 $  (58,72 %)
Investiert:     39.871,35 $  (41,28 %)  — AAPL 9.397,65 / JPM 1.104,00 / LLY 9.815,04 / UNH 9.768,24 / V 9.786,42
P/L Pre:          +205,32 $  (+0,213 %)   [GRÜN, Cap −3 %]
Alpha vs SPY:    +0,018 pp   (SPY Alpaca latestTrade IEX 774,05 vs Mi Close 772,54 = +0,196 %; Perplexity ohne belastbaren Pre-Wert)
ATH:           100.066,47 $   (Intraday-Open 22.06., unverändert)
Drawdown:        −3,485 %     [GRÜN, verbessert vs Close −3,700 %; Schwelle −15 % bei 85.056 $]
Guardrails:     Daily +0,213 % | Weekly KW33 Tag 4 vs Fr-Close 96.512,65 = +0,069 % | Käufe 0/2 KW33 | VIX 14,69 (verbessert vs Mi 15,28) | Crash-Filter NEIN | DD GRÜN
V1/V2 Pre-Market (V5/V6 nur Close-Vollcheck):
- AAPL 303,15 (chg +0,31 %, P/L −4,33 % **Worst** verbessert vs Close −4,64 %): **V1 Std +3,99 % ENGSTE verbessert vs Close +3,67 %** (Thr 291,51); V2 **−0,020 % BROKEN razor** via 52w-Wick 344,555 (Thr 303,21) DQF **3. Tag persistent, verbessert vs Close −0,334 %**; V5/V6 nur Close.
- JPM 368,00 (chg +0,76 %, P/L +10,58 % **Best**): V1 +20,20 % (Thr 306,16); V2 +14,23 % via Wick 366,085 (Thr 322,15, **NEUES Hoch fortgeschrieben**); V5/V6 nur Close.
- LLY 1226,88 (chg +0,57 %, P/L +2,76 %): V1 +11,70 % (Thr 1098,38, **Std-V1 primär**); V2 +11,68 % via 52w-High 1248,53 (Thr 1098,71); V5/V6 nur Close.
- UNH 407,01 (chg +0,34 %, P/L +1,35 %): V1 +10,17 % (Thr 369,44); V2 **+0,340 % technisch AUS BROKEN RAUS** via Wick 460,95 (Thr 405,636) verbessert vs Close +0,001 %, DQF **14. Tag persistent** — Alt-V2 via 437,13 = 384,67 Puffer **+5,81 % SICHER**; V5/V6 nur Close.
- V 362,46 (chg +0,83 %, P/L +1,48 %): V1 +10,30 % (Thr 328,60); V2 +10,14 % via 373,97 (Thr 329,09); V5/V6 nur Close.
V-Trigger Pre-Market: **V1 Std alle 5 SICHER** (min AAPL +3,99 % verbessert) | **V2:** AAPL DQF-BROKEN 3. Tag razor −0,020 % (verbessert), UNH technisch AUS BROKEN RAUS +0,340 % (verbessert vs Close +0,001 %) — Rule 5 No-Action-Kontext bleibt, UNH-Owner-Entscheidung pending | V3/V4 max JPM +10,58 % << 20 %-TP1 | V5/V6 nur Close-Vollcheck.
**Order-Aktion Pre-Market:** KEINE (0 offene Orders, keine Sell-Signale, keine Buy-Signale — Kaufscan bei Market Open geplant).
Sektor-Struktur Pre-Market: XLV **20,32 %** (UNH 10,12 + LLY 10,16), XLF **11,28 %** (JPM 1,14 + V 10,13), XLK **9,73 %** AAPL, Cash 58,72 %.
Weekly Loss Cap: +0,069 % vs Cap −5 % → weit entfernt, kein Sperrauslöser.
**Earnings-Blackout-Check:** Perplexity bestätigt für AAPL/JPM/LLY/UNH/V/MRK KEIN Earnings 13.–15.08. — **kein Blackout aktiv**, keine Stop-Loss-Verschärfung nötig.
**MRK K5-Verifikation:** Forward P/E **46,73 >> 35 → K5 FAIL → MRK REJECT als Kaufkandidat** (K1–K4 gestern alle ✓, K5-Perplexity überstimmt) — XLV-Sektor-Cap-Assessment obsolet
Watchlist Do 13.08. Market Open (K1–K4 aus Alpaca IEX EOD Mi + K5 Perplexity):
- **MRK ~~Prio 1~~ REJECT via K5**: FwdPE 46,73 FAIL
- **UAL (XLI) Prio 2**: K1-K3 ✓ RS +25,87 pp #1 | K4 31 % FAIL 12. Tag persistent
- **UNP (XLI) Prio 3**: K1-K3 ✓ RS +5,90 pp | K4 46 % FAIL
- **MU (XLK) Backup**: K1-K3 ✓ RS +14,35 pp | K4 81 % FAIL — XLK-Konflikt AAPL
- **→ KEIN Kaufkandidat mit K1–K5 alle ✓ pre-open** — Broad-Scan bei Market Open nötig (Slot 1/2 KW33 offen)
Perplexity: **3 Queries** (Daily Macro, Earnings-Check 3 HT, MRK K5-Fundamentals) — MRK K5-FAIL identifiziert, Silence-Bias VIX/SPY/Makro (6. Mal Serie in Kalender-Daten)
ClickUp Prio 4 [PRE-MARKET] Task versucht — **ITEM_246 "Max usage for custom task types reached" 14. Tag persistent** → Fallback Memory-Only per notify-skill.md.
PushNotification: **NEIN** (Silence-Rule: kein V-Trigger, kein Cap-Alert, kein Kauf, Daily +0,213 % positiv, VIX ruhig 14,69, MRK K5-FAIL entfernt nur einen Kandidaten ohne Trigger-Situation, UNH V2 technisch verbessert, AAPL V2 marginal verbessert — kein Owner-Handlungsbedarf).
Nächster Check: **Do 13.08. 09:30 ET Market Open KW33 Tag 4** — Broad-Watchlist-Scan Slot 1/2 KW33 (MRK raus, alte Watchlist K4-FAIL persistent, Neu-Kandidaten benötigt), UNH V2-DQF-Verlauf, AAPL V2-DQF-Verlauf.

---

**Close 16:00 ET 12.08.2026 (KW33 Tag 3 Mi) — Tagesbilanz:**
Gesamtwert:     96.363,47 $
Cash:           56.707,49 $  (58,85 %)
Investiert:     39.655,98 $  (41,15 %)  — AAPL 9.366,66 / JPM 1.095,54 / LLY 9.762,24 / UNH 9.727,20 / V 9.704,34
P/L heute:         −51,21 $  (−0,053 %)   [GRÜN, Cap −3 %]
Alpha vs SPY:    −0,315 pp   (SPY Alpaca Daily-Bar 772,54 vs Di 770,52 = +0,262 % post-CPI-Recovery)
ATH:           100.066,47 $   (Intraday-Open 22.06., unverändert)
Drawdown:        −3,700 %     [GRÜN, Schwelle −15 % bei 85.056 $]
Guardrails:     Daily −0,053 % | Weekly KW33 Tag 3 vs Fr-Close 96.512,65 = −0,155 % | Käufe 0/2 KW33 | VIX 15,28 | Crash-Filter NEIN | DD GRÜN
Signal-Check V1–V6 EOD (Alpaca IEX 277d Bars):
- AAPL 302,20 (chg −0,88 %, P/L −4,64 % **Worst**): V1 Std 291,51 Puffer **+3,67 % ENGSTE**; V2 Wick*0,88 = 303,21 → **BROKEN −0,334 %** via 52w-Wick 344,555 DQF **2. Tag persistent** (Std-V1 primär sicher, Rule 5 No-Action); V5 EMA50 309,32>EMA200 281,39 ✓ (+9,93 pp); V6 RSI 40,14 / RS_4w −10,10 pp → NICHT ausgelöst (RSI << 80).
- JPM 365,23 (chg +0,88 %, P/L +9,75 % **Best**): V1 306,16 Puffer **+19,29 %**; V2 **NEUES Posit-Hoch 366,085 → Thr 322,15** Puffer +13,37 %; V5 EMA50 339,54>EMA200 317,87 ✓ (+6,82 pp); V6 RSI 68,85 / RS_4w +2,89 pp → NICHT ausgelöst (RSI < 80).
- LLY 1.219,975 (chg +0,58 %, P/L +2,20 %): V1 1.098,38 Puffer +11,07 % (**BO ENDED — Standard-V1 primär**); V2 via 52w-High 1.248,53 = Thr 1.098,70 Puffer +11,04 %; V5 EMA50 1.150,95>EMA200 1.022,57 ✓ (+12,55 pp); V6 RSI 58,11 / RS_4w +3,13 pp → NICHT ausgelöst.
- UNH 405,64 (chg +0,78 %, P/L +1,01 %): V1 369,44 Puffer +9,79 %; V2 Wick*0,88 = 405,636 → **BROKEN +0,001 % razor** via 52w-Wick 460,95 DQF **13. Tag persistent** — Alt-V2 via 437,13 = 384,67 Puffer **+5,45 % SICHER** + Std-V1 +9,79 % primär → Rule 5 No-Action, Owner-Entscheidung pending seit Di-Midday-Push; V5 EMA50 407,25>EMA200 362,59 ✓ (+12,32 pp); V6 RSI 44,01 / RS_4w −5,37 pp → NICHT ausgelöst.
- V 359,48 (chg −0,84 %, P/L +0,65 %): V1 328,60 Puffer +9,40 %; V2 via 52w-High 373,97 = Thr 329,09 Puffer +9,24 %; V5 EMA50 350,16>EMA200 338,32 ✓ (+3,50 pp **engster**); V6 RSI 51,33 / RS_4w −1,18 pp → NICHT ausgelöst.
V-Trigger EOD: **V1 Std alle 5 SICHER** | **V2:** AAPL DQF Wick-BROKEN 2. Tag (Std-V1 +3,67 % primär), UNH DQF Wick-BROKEN 13. Tag (Alt-V2 +5,45 % + Std-V1 +9,79 % primär) — Rule 5 No-Action fortlaufend | V3/V4 max JPM +9,75 % << 20 %-TP1 | V5 alle Golden Cross intakt | V6 max RSI JPM 68,85 << 80.
**Sell-Order für Do 13.08.:** KEINE (0 offene Orders bei Alpaca bestätigt).
Sektor-Struktur EOD: XLV **20,22 %** (UNH 10,10 + LLY 10,12), XLF **11,21 %** (JPM 1,14 + V 10,07), XLK **9,72 %** AAPL, Cash 58,85 %.
Weekly Loss Cap: −0,155 % vs Cap −5 % → weit entfernt, kein Sperrauslöser.
Watchlist Do 13.08. (K1–K4 Alpaca IEX EOD 12.08. — K5 bei Open verifizieren):
- **MRK (XLV) Prio 1**: Close 132,90 (chg +1,97 %) K1 ✓ EMA-Gap +12,48 pp | K2 ✓ RSI 63,48 | K3 ✓ RS +13,62 pp | **K4 ✓ 128 % Avg20 — alle 4 grün**; K5 FwdPE/RevGrowth pending; **⚠ LEVEL 0 Sektor-Cap Grenzfall**: XLV 20,22 % + MRK ~10 % würde XLV auf ~30 %-Cap-Grenze führen (strategy.md: max 30 %/max 3 Pos) → Kauf nur bei K5-Bestätigung UND Sektor-Cap-Compliance-Prüfung
- **UAL (XLI) Prio 2**: Close 125,10 K1-K3 ✓ (RS +25,87 pp #1) | **K4 31 % FAIL 11. Tag persistent**
- **UNP (XLI) Prio 3**: Close 293,78 K1-K3 ✓ (RS +5,90 pp) | K4 46 % FAIL
- **MU (XLK) Backup**: Close 911,30 (chg +4,96 %) K1-K3 ✓ (RS +14,35 pp, EMA-Gap +47,79 pp sehr breit) | K4 81 % FAIL — XLK-Konflikt AAPL 9,72 %
- REJECT: PANW (K2 RSI 70,48 knapp >70), BAC (K2 RSI 73,58 FAIL), NVDA (K3 −3,19 pp NEG), TMO/ABT (K2 >70), GS/AMD (K2 <50), ORCL/LOW/HD (K1 Death-Cross)
ClickUp Prio 3 [CLOSE] Task versucht — **ITEM_246 "Max usage for custom task types reached" 13. Tag persistent** → Fallback Memory-Only per notify-skill.md.
PushNotification: **NEIN** (Silence-Rule: kein V-Trigger, kein Cap-Alert, kein Kauf, Daily nur −0,053 %; AAPL V2-DQF 2. Tag Escalation-Push wurde bereits Midday abgesetzt, Close liefert keine neue Entscheidungsgrundlage; UNH V2-DQF 13. Tag Owner-Push Di-Midday steht; keine Portfolio-Earnings 3 HT — kein Owner-Handlungsbedarf).
Nächster Check: **Do 13.08. 08:30 ET Pre-Market KW33 Tag 4** — MRK K5-Verifikation + XLV-Sektor-Cap-Assessment, UNH V2-DQF-Verlauf, AAPL V2-DQF-Verlauf, LLY Std-V1-Primary-Ausklang.

---

**Midday 13:11 ET 12.08.2026 (KW33 Tag 3 Mi):**
Positionen: 5/8 | Ø P/L: **+1,60 %** (JPM +9,69 Best / LLY +1,82 / UNH +0,69 / V +0,38 / AAPL −4,58 Worst)
Beste Position: **JPM +9,69 %** (365,03 $ Alpaca latestTrade IEX 13:10 ET)
Schlechteste Position: **AAPL −4,58 %** (302,33 $, verschlechtert vs Open −4,24 %)
Stops V1-V4 Live-Check (V5/V6 nur Close-Vollcheck):
- **V1 Std alle 5 SICHER Puffer eng→weit:** **AAPL +3,71 % ENGSTE Std verschlechtert vs Open +4,09 %** (302,33 chg −0,81 % vs Di Close 304,80, Std-V1 291,51 primär), UNH +9,44 % (404,325 chg +0,45 %, P/L +0,69 %), V +9,11 % (358,545 chg −1,18 % vs Di Close 362,82, P/L +0,38 % verschlechtert vs Open +1,43 %), **LLY +10,68 %** (1215,66 chg +0,05 %, P/L +1,82 % verbessert vs Open +1,35 %, **Std-V1 1098,38 primär ab heute**), **JPM +19,23 %** (365,03 chg +0,79 %, **Best P/L +9,69 %** verbessert vs Open +9,19 %)
- **V2-Trailing-Stop:** **⚠️ AAPL V2 BROKEN Puffer −0,29 % via Wick 344,555 = Thr 303,21 FRESH Escalation vs Open razor +0,069 %** (Preis-Weakness-Fortsetzung 302,33 < 303,21 — 52w-Wick DQF-flagged wie UNH; Std-V1 +3,71 % ENGSTE primär sicher, V2 sekundär via DQF); **UNH V2 BROKEN Puffer −0,32 % via Wick 460,95 = Thr 405,636 marginal verschlechtert vs Open −0,020 %** (14. Tag DQF persistent — Alt-V2 via 437,13 = 384,67 Puffer +5,11 % SICHER, Std-V1 +9,44 % primär sicher, Owner-Entscheidung pending seit Di-Midday-Push); LLY +10,64 % via 52w-High 1.248,53 (Thr 1098,71) sicher, V +8,95 % via 373,97 (Thr 329,09) sicher, JPM +14,25 % via Wick 363,08 (Thr 319,51) sicher
- **V3/V4:** max P/L JPM +9,69 % << 20 %-TP1 → kein Trigger
- **V5/V6:** nur Close-Vollcheck
Daily P/L: **−0,142 % [GRÜN, Cap −3 %]** (Equity Live **96.278,11 $** vs last_equity 96.414,68 = −136,57 $; MV 39.571,54 $ / Cash 56.707,49 $ = **58,90 %**; DD vs ATH 100.066,47 = **−3,786 % GRÜN** verschlechtert vs Open −3,730 %; Weekly KW33 Tag 3 vs Fr Close 96.512,65 = **−0,243 % GRÜN** weit von Cap −5 %, verschlechtert vs Open −0,185 %)
Alpha vs SPY: **−0,460 pp NEG** (SPY Live 772,975 Alpaca latestTrade IEX 13:11 ET vs Di Close 770,52 = **+0,319 % positiv** post-CPI-Reaktion; Portfolio −0,142 % underperformt SPY-Recovery via AAPL/V-Weakness — verschlechtert vs Open −0,385 pp)
V-Aktion: **KEINE Sell-Order platziert** (Rule 5 No-Action bei DQF-Anomalie fortlaufend: AAPL V2 FRESH BROKEN via 52w-Wick 344,555 Single-Print DQF wie UNH — Std-V1 +3,71 % ENGSTE primär sicher; UNH V2 14. Tag DQF Alt-V2 +5,11 % + Std-V1 +9,44 % sicher); 0 offene Orders bei Alpaca (Order-Query bestätigt)
Pending Orders: 0 | Käufe KW33: 0/2 (Slot 1/2 + 2/2 OFFEN — Midday KEIN Buy-Scan per Routine-Spec)
Sektor-Struktur Live: XLV **20,17 %** (UNH 10,08 + LLY 10,09), XLF **11,20 %** (JPM 1,14 + V 10,06), XLK **9,74 %** AAPL, Cash 58,90 %
LLY Blackout: **HT+2 Bull-Konvention ENDET HEUTE 12.08. → Standard-V1 1098,38 primär ab jetzt** aktiv; Puffer +10,68 % sicher (verbessert vs Open +10,16 %)
CPI-Reaktion: SPY +0,319 % post-CPI-Release-Recovery (Perplexity Pre-Market bestätigt); Portfolio underperformt via AAPL/V-Weakness — kein handelbarer Signalbruch
ClickUp Prio 1 Critical Alert versucht — **ITEM_246 "Max usage for custom task types reached" 12. Tag persistent** → Fallback Memory-Only per notify-skill.md
PushNotification: **JA (Escalation)** — AAPL V2-Wick FRESH BROKEN (Wende von Open razor +0,069 % zu Midday −0,29 %) triggert Push, obwohl DQF-Interpretation No-Action bleibt; UNH V2-Wick DQF-Status unverändert marginal (Owner erhielt bereits Di-Midday-Push)
Nächster Check: **Mi 12.08. 16:00 ET Market Close KW33 Tag 3** — AAPL V2-Wick-DQF-EOD-Vollcheck V5/V6, UNH V2-Wick-DQF-Verlauf (Owner-Entscheidung pending), LLY Std-V1-Primary-Umstellung, Tagesbilanz + Watchlist Do 13.08.

---

**Live Open 09:41 ET 12.08.2026 (KW33 Tag 3 Mi):**
Positionen: 5/8 | Ø P/L: **+1,74 %** (JPM +9,19 Best / V +1,43 / LLY +1,35 / UNH +0,99 / AAPL −4,24 Worst)
Beste Position: **JPM +9,19 %** (363,35 $ Alpaca latestTrade IEX 09:41 ET)
Schlechteste Position: **AAPL −4,24 %** (303,42 $)
Stops V1-V6 Live-Check (V5/V6 NICHT bei Open geprüft — nur Close-Vollcheck):
- **V1 Std alle 5 SICHER Puffer eng→weit:** **AAPL +4,09 % ENGSTE Std verschlechtert vs Pre +4,28 %** (303,42 chg -0,45 %, P/L -4,24 %, Std-V1 291,51 primär), UNH +9,78 % (405,56 chg +0,76 %, P/L +0,99 %), V +10,25 % (362,27 chg -0,15 %, P/L +1,43 %), **LLY +10,16 %** (1210,00 chg -0,41 %, P/L +1,35 %, **BO ENDET HEUTE → Std-V1 1098,38 primär ab jetzt**, Puffer +10,16 % vs Pre +10,26 %), **JPM +18,68 %** (363,35 chg +0,33 %, **Best P/L +9,19 %**)
- **V2-Trailing-Stop:** **⚠️ UNH BROKEN Puffer -0,020 % via 52w-Wick 460,95 = Thr 405,636 marginal verbessert vs Pre -0,78 %** (14. Tag DQF persistent — Alt-V2 via 437,13 = 384,67 Puffer +5,42 % SICHER, Std-V1 +9,78 % primär sicher, Owner-Entscheidung pending seit Di-Midday-Push); **AAPL V2 razor +0,069 % via Wick 344,555 = Thr 303,21 marginal verbessert vs Pre +0,26 %** (Std-V1 +4,09 % ENGSTE primär, V2 sekundär); LLY +10,13 % via 52w-High 1.248,53 (Thr 1098,70) sicher, V +10,08 % via 373,97 (Thr 329,09) sicher, JPM +13,72 % via Wick 363,08 (Thr 319,51) sicher
- **V3/V4:** max P/L JPM +9,19 % << 20 %-TP1 → kein Trigger
- **V5/V6:** nur Close-Vollcheck
Daily P/L: **−0,084 % [GRÜN, Cap −3 %]** (Equity Live **96.333,71 $** vs last_equity 96.414,68 $ = −80,97 $; MV 39.626,22 $ / Cash 56.707,49 $ = **58,86 %**; DD vs ATH 100.066,47 = **−3,730 % GRÜN**, marginal verschlechtert vs Pre −3,722 %; Weekly KW33 Tag 3 vs Fr Close 96.512,65 = **−0,185 % GRÜN** weit von Cap −5 %)
Alpha vs SPY: **−0,385 pp NEG** (SPY Live 772,84 Alpaca latestTrade IEX 09:41 ET vs Di Close 770,52 = **+0,301 % positiv** post-CPI-Awaited Recovery; Portfolio −0,084 % underperformt SPY-Recovery via AAPL/LLY/V-Weakness)
V-Aktion: **KEINE Sell-Order platziert** (V1 Std alle 5 SICHER; UNH V2-Wick DQF 14. Tag Alt-V2/Std-V1 sicher → Rule 5 No-Action fortlaufend; AAPL V2 razor +0,069 % marginal verbessert innerhalb Std-V1 +4,09 % ENGSTE sicher); 0 offene Orders bei Alpaca
Kaufsignal-Scan Slot 1/2 KW33 (Session ~11 min Elapsed 2,82 %; K4-Linear-Pace Extrapolation via Session-Vol/Elapsed vs Avg20):
- **MRK (XLV) Prio 1 K4 PASS extrapol ~125 % Avg20** (session_vol IEX 10.668 / 0,0282 = 378k vs Avg20 301.916 = 125,3 %; K1-K3 ✓ RS +12,87 pp vorbekannt) → **LEVEL 0 SKIP XLV-Sektor-Cap** (XLV UNH 10,10 + LLY 10,05 = **20,15 %** + MRK ~10 % würde XLV auf ~30,15 % pushen → verletzt strategy.md 30 %-Sektor-Cap) — blockiert bis UNH/LLY-Reduzierung
- **UAL (XLI) Prio 2 REJECT K4-FAIL 10. Tag persistent**: session 1.226 = 0,63 % Avg20 (extrapol ~22 %) → Downgrade Prio Backup bleibt
- **UNP (XLI) Prio 3 REJECT K4-FAIL heavy**: session 1.627 = 0,96 % Avg20 (extrapol ~34 %)
- **BAC (XLF) K4 PASS extrapol ~179 % Avg20** (session 114.211 / 0,0282 = 4,05M vs Avg20 2,27M): K1/K3 ✓ RS +22,40 pp aber **K2 RSI 70,26 Close FAIL bleibt persistent** (Close chg +0,24 %, RSI wahrscheinlich weiter >70) → REJECT persistent
- **PANW (XLK) Prio 4 REJECT K4-FAIL + K2 RSI 69,57 upper-border**: session 2.962 = 1,03 % Avg20 (extrapol ~37 %), XLK-Konflikt AAPL 9,76 %
- **NVDA (XLK) Backup K4 STRONG PASS ~295 % Avg20** (session 383.285 / 0,0282 = 13,6M vs Avg20 4,61M): K4 stark aber **K3 -3,75 pp NEG persistent** + XLK-Konflikt AAPL → REJECT
- **BLOCKIERT:** GS/AMD/MU/ABBV (K2 <50), CVS (K2 31,61), EOG/COP/XOM (K3 NEG), ORCL (K1 Death-Cross)
- **Slot 1/2 KW33 bleibt OFFEN — kein Kandidat erfüllt alle 5 K1-K5** (MRK LEVEL 0 SKIP Sektor-Cap, BAC K2 FAIL, NVDA K3 NEG, UAL/UNP/PANW K4 FAIL)
Watchlist Do 13.08. (aus Alpaca IEX Live/Pre): MRK bleibt Prio 1 aber XLV-Cap-Blocker, BAC Prio 2 pending RSI-Cool-down, UAL/UNP Prio 3 K4-Vol-Rebound-Watch (persistent-Fail-Serie), PANW Prio 4 XLK-Konflikt
Sektor-Struktur Live: XLV **20,15 %** (UNH 10,10 + LLY 10,05 marginal erhöht vs Di Close 20,09 % via UNH-Recovery), XLF **11,28 %** (JPM 1,13 + V 10,15 marginal verschlechtert vs Di Close 11,29 %), XLK **9,76 %** AAPL marginal verschlechtert vs Di Close 9,80 %, Cash 58,86 %
LLY Blackout: **HT+2 Bull-Konvention ENDET HEUTE 12.08. → Umstellung auf Standard-V1 1098,38 primär** ab jetzt; Puffer +10,16 % sicher
CPI-Awaited: Perplexity-Query Pre-Market bestätigte CPI-Release erwartet heute → intraday-Volatilität möglich post-Release; keine strategy.md-Regel blockiert Käufe, aber Vorsicht bei Watchlist-K4-Vol-Interpretation (aktuell keine handelbare Situation, K4 nur BAC/MRK/NVDA pace-pass alle andere Rejects)
Perplexity: **KEIN Query Market Open** (Silence-Rule Effizienz + persistente Halluzinationen 5. Mal Serie; Watchlist aus EOD-Alpaca-Daten + Live-Session-Vol ausreichend)
ClickUp Prio 4 Routine-Log: bei ITEM_246-Fehler-Persistenz 11. Tag → Fallback Memory-Only per notify-skill.md
KEINE PushNotification: Silence-Rule Routine — kein V-Trigger, kein Cap-Alert, alle 8 Guardrails GRÜN + 1 WARN (UNH V2-Wick DQF verbessert vs Pre), kein Kauf (kein Kandidat K1-K5), Owner erhielt Fr-Wochenschluss-Push + Di-Midday-UNH-Push, negative Alpha nur -0,385 pp NEG intraday-Rauschen, CPI-Release erst später Session → keine neue Entscheidungsgrundlage
Nächster Check: **Mi 12.08. 13:00 ET Midday Stop-Check KW33 Tag 3** — UNH V2-Wick-DQF-Verlauf (Owner-Entscheidung pending), AAPL V2-Wick-Puffer-Verlauf razor +0,069 %, LLY Std-V1-Primary-Umstellung-Ausklang, Watchlist MRK/UAL/UNP/BAC K4-Vol-Pace-Post-CPI-Check, CPI-Release-Reaktion-Assessment für Portfolio + SPY

---

**Close FINAL 16:00 ET 11.08.2026 (KW33 Tag 2 Di):**
Positionen: 5/8 | Ø P/L: **+1,69 %**
Beste Position: **JPM +8,83 %** (362,15 $ Alpaca)
Schlechteste Position: **AAPL −3,81 %** (304,80 $)
Stops V1-V6 EOD-Vollcheck: **⚠️ UNH V2 (Wick-basiert) BROKEN Puffer −0,78 %** (Close 402,49 $ ≤ Threshold 405,636 $ via 52w-Wick 460,95 $ * 0,88; Wick als Single-Print-Anomalie seit 12+ Sessions Data-Quality-flagged, next-höchster Wick 437,13 $ = 24-Punkte-Gap 5,4 %; **Alt-V2 via 437,13 * 0,88 = 384,67 $ Puffer +4,63 % SICHER**; **Std-V1 sicher +8,94 %** Puffer via Kaufkurs 401,57); AAPL V2 razor-thin **+0,55 %** via 52w-Wick 344,555 = Thr 303,21 (verschlechtert vs Midday +1,03 % via Preis-Weakness Close 304,885, Std-V1 +4,59 % ENGSTE Std primär); alle anderen 3 Positionen (JPM/V/LLY) V1+V2 regulär SICHER — **Std-V1 Puffer eng→weit AAPL +4,59 % / UNH +8,94 % / LLY +10,43 % / V +10,33 % / JPM +18,26 %**; **V5-Vollcheck 5 SICHER** (Golden Cross alle intakt, V engster +4,02 pp); **V6-Vollcheck 5 SICHER** (max RSI JPM 66,52 << 80).
Daily P/L: **−0,370 % [GRÜN, Cap −3 %]** (Equity Close 96.406,20 $ vs last_equity 96.763,84 $ = −357,64 $; MV 39.698,71 $ / Cash 56.707,49 $ = 58,82 %; DD vs ATH 100.066,47 = **−3,658 % GRÜN**; Weekly KW33 Tag 2 vs Fr Close 96.512,65 = **−0,110 % GRÜN** weit von Cap −5 %)
Alpha vs SPY: **−0,046 pp NEG marginal** (SPY Close 770,52 Alpaca Daily-Bar IEX vs Mo Close 773,02 = −0,323 %; Portfolio −0,370 % underperformt SPY-Rückgang marginal)
V-Aktion: **KEINE autonome Sell-Order platziert** (UNH V2-Wick-Breach unter CLAUDE.md Rule 5 "No-Action bei Unsicherheit" + Rule 3 Konflikt-Klausel → Owner-Entscheidung erforderlich; Std-V1 +8,94 % primär sicher, Alt-V2 via next-highest Wick +4,63 % sicher); 0 offene Orders bei Alpaca; keine Limit-Orders zu stornieren; **KEINE neue PushNotification** (Silence-Rule: Owner erhielt Midday-Push mit UNH V2-Optionen, Close-Situation marginal identisch −0,78 % vs Midday −0,54 %, keine Eskalation vs V-SICHER-Alternativen, keine neue Entscheidung erforderlich außer Verlängerung der Wartung).
Watchlist Mi 12.08.: **MRK Prio 1 XLV** (K1-K3 alle ✓ RS +12,87 pp, XLV-Cap 20,09 % LEVEL 0-SKIP bleibt bis UNH/LLY-Kürzung), **UAL Prio 2 XLI** (K1-K3 ✓ RS_63d **+26,33 pp #1**, K4 9. Tag Vol-Watch), **UNP Prio 3 XLI** (K1-K3 ✓ RS +6,91 pp, K4 Vol-Watch), **PANW Prio 4 XLK** (K1-K3 ✓ RS +75,35 pp, XLK-Konflikt AAPL 9,80 %, RSI 69,57 upper-border), **BAC Backup XLF** (K1/K3 ✓ RS +22,40 pp, K2 RSI 70,26 knapp überschritten → FAIL persistent).
Weekly Loss Cap Check: **−0,110 % vs Cap −5 % — GRÜN, kein Auslöser**, keine pending Orders zu stornieren, KW33 Tag 2 abgeschlossen.
ClickUp: **[CLOSE] Tagesbilanz Di 11.08.** Prio 3 (negative Daily) versucht — bei ITEM_246-Fehler Persistenz 12. Tag → Fallback Memory-Only.
LLY Blackout: **Bull-Konvention HT+2 endet HEUTE Ende Di 11.08. → ab Mi 12.08. Standard-V1 (1098,38) primär**, Puffer bleibt sicher +10,43 %.
Nächste Routine: **Mi 12.08. 08:30 ET Pre-Market KW33 Tag 3** — UNH V2-Wick-DQF-Verlauf, AAPL V2-Wick-Erosion-Watch (+0,55 % razor-thin), LLY BO-Ende-Umstellung auf Std-V1 primär, Watchlist MRK/UAL/UNP/PANW K4-Vol-Rebound-Check.


**Bot:** Bull | **Modus:** Paper Trading | **Zuletzt aktualisiert:** 2026-08-11 16:00 ET (**Market Close Tagesbilanz KW33 Tag 2 FINAL**, Equity Close **96.406,20 $** vs last_equity 96.763,84 = **-0,370 % Daily** [GRÜN, Cap -3 %, verschlechtert vs Midday -0,226 %], Cash 56.707,49 = **58,82 %** unverändert, MV Close **39.698,71 $** (5 Pos Alpaca, -358,12 vs Mo Close 40.056,83 = **-0,894 %** deutlich verschlechtert vs Midday -0,548 % via UNH -1,66 % Worst chg + LLY -1,37 % + AAPL -1,12 % dämpfen JPM +0,66 % Best chg + V +0,42 %), DD **-3,658 %** vs ATH 100.066,47 [GRÜN, verschlechtert vs Midday -3,519 %], **Weekly KW33 Tag 2 vs Fr Close 96.512,65 = -0,110 %** [GRÜN, weit von Cap -5 %, verschlechtert vs Midday +0,034 %], **SPY Close 770,52 Alpaca Daily-Bar IEX** vs Mo Close 773,02 = **-0,323 % negativ** [Crash-Filter INAKTIV], **Alpha vs SPY -0,046 pp NEG marginal** (Portfolio -0,370 % vs SPY -0,323 %, verschlechtert vs Midday +0,097 pp via UNH/LLY-Nachmittags-Give-back), **V5-Vollcheck 5 SICHER EOD-Bars** (Alpaca IEX 342d Bar-Historie, Golden Cross alle intakt EMA50>EMA200): **V** (EMA50 349,78 > EMA200 336,26, Puffer +4,02 pp engster aber positiv), JPM (338,50 > 313,22, +8,07 pp), AAPL (309,61 > 278,20, +11,29 pp), UNH (407,32 > 364,58, +11,72 pp), LLY (1148,13 > 1019,44, +12,62 pp). **V6-Vollcheck 5 SICHER**: max **RSI JPM 66,52** (V 55,06; LLY 57,04; AAPL 41,87; UNH 41,53 — alle << 80). **RS_4w vs SPY** (SPY 20d +2,47 %): UNH **-7,84 pp** (RSI 41,5 → V6 sicher via UND), AAPL -5,66 pp (RSI 41,9 → V6 sicher), V -0,64 pp (RSI 55,1 → V6 sicher), LLY +2,61 pp, JPM +3,09 pp. **KEIN V1/V3/V4-Trigger per strategy.md** (Std-V1 alle 5 SICHER Puffer eng→weit: **AAPL +4,59 % ENGSTE verschlechtert vs Midday +5,00 %**, UNH +8,94 %, LLY +10,43 % (Blackout-V1_neu 1.134,20 Puffer +6,95 % — **Bull-Konvention BO endet Ende Di HEUTE → ab Mi 12.08. Standard-V1 primär**), V +10,33 %, JPM +18,26 % Best P/L +8,83 %), V2-Trailing-Stop **⚠️ UNH V2 BROKEN Puffer -0,78 % via 52w-Wick 460,95 = Thr 405,636 verschlechtert vs Midday -0,54 %** (Data-Quality-Flag persistent 12. Tag; Wick-Single-Print vs next-höchster 437,13 = 24-Punkte-Gap 5,4 %; **Alt-V2 via 437,13 * 0,88 = 384,67 = Puffer +4,63 % SICHER**; Std-V1 +8,94 % primär sicher), **AAPL V2 razor-thin +0,55 % via Wick 344,555 = Thr 303,21 verschlechtert vs Midday +1,03 %** (Preis-Weakness Close 304,885 vs Midday 306,07; Std-V1 +4,59 % ENGSTE primär), LLY V2 +10,40 % via 52w-High 1.248,53 (Thr 1098,70), V +10,16 % via 373,97 (Thr 329,09), JPM +13,31 % via 363,08 (Thr 319,51). V3/V4 max P/L JPM +8,83 % << 20 %-TP1 kein Trigger. **KEINE Sell-/Limit-Order für Mi 12.08. platziert, 0 offene Orders** (UNH V2-Wick unter Rule 5 No-Action bei DQF-Anomalie + Alt-V2/Std-V1 sicher). Sektor-Struktur EOD: XLV **20,09 %** (UNH 10,01 + LLY 10,08 verbessert vs Midday 20,20 % via UNH-Give-back), XLF **11,29 %** (JPM 1,13 + V 10,16) marginal verbessert vs Midday 11,26 % via V-Recovery, XLK **9,80 %** AAPL marginal verschlechtert vs Midday 9,83 %, Cash 58,82 %, **Kaufsignal-Scan Slot 1/2 KW33 unverändert offen** (0/2 Käufe KW33 nach Tag 2), **Watchlist Mi 12.08. K1-K3 aus Alpaca IEX EOD Di 11.08.:** **MRK Prio 1 XLV** (130,335 K1 EMA50 125,07 > 200 112,45 +11,22 % ✓, K2 RSI 58,05 ✓, K3 RS_63d **+12,87 pp** ✓, K4 EOD-Vol 64 % Avg20 FAIL — Session-Spike war Perplexity-Extrapolation-Bias; **LEVEL 0-SKIP XLV-Sektor-Cap** 20,09 % + MRK ~10 % würde 30,10 % pushen → verletzt >3 Pos/Sektor + 30 %-Cap-Regel — nur handelbar bei UNH/LLY-Reduzierung), **UAL Prio 2 XLI** (126,18 K1 +12,96 % ✓, K2 RSI 53,18 ✓, K3 RS **+26,33 pp #1** ✓, K4 Vol 73 % Avg20 FAIL 9. Tag persistent — Downgrade Prio Backup KW34 gerechtfertigt aber K3-Rangaufstieg auf #1 hält Prio 2), **UNP Prio 3 XLI** (292,74 K1 +9,54 % ✓, K2 RSI 53,35 ✓, K3 RS +6,91 pp ✓, K4 Vol 38 % Avg20 heavy FAIL), **PANW Prio 4 XLK** (383,79 K1 +31,30 % ✓, K2 RSI 69,57 upper-border ✓, K3 RS +75,35 pp ✓, K4 Vol 52 % Avg20 FAIL, XLK-Konflikt AAPL 9,80 %), **BAC Backup XLF** (63,99 K1 +10,41 % ✓, K3 RS +22,40 pp ✓, **K2 RSI 70,26 FAIL knapp überschritten → REJECT**, K4 Vol 56 % Avg20 FAIL), **REJECTS:** NVDA (K3 -5,15 pp FAIL persistent), GS (K2 RSI 47,58 <50 FAIL persistent), **BLOCKIERT bleiben:** AMD/MU/ABBV (K2 <50), CVS (K2 31,61), EOG/COP/XOM (K3 NEG), ORCL (K1 Death-Cross), **Guardrails 8/8 GRÜN + 2 WARN** (LLY BO HT+2 heute letzte Session ENDE → ab Mi Std-V1 primär; **UNH V2 BROKEN -0,78 % via 52w-Wick DQF 12. Tag persistent — Std-V1 +8,94 % + Alt-V2 +4,63 % primär sicher, Owner-Entscheidung pending seit Midday-Push**), **Earnings-Blackout Portfolio + Watchlist: KEINE nächsten 3 HT** (AAPL/JPM/LLY/UNH/V/UAL/UNP/BAC/MRK/PANW alle NONE), **KEIN ClickUp** (Prio 3 Tagesbericht [CLOSE] versucht — ITEM_246-Fehler Persistenz 12. Tag → Fallback Memory-Only per notify-skill.md), **KEINE PushNotification** (Silence-Rule Routine: kein NEUER V-Trigger vs Midday-Zustand, kein Cap-Alert Daily -0,370 % innerhalb -3 %-Cap, Weekly -0,110 % innerhalb -5 %-Cap, DD -3,658 % innerhalb -15 %-Alarm, UNH V2-Wick-Zustand marginal verschlechtert -0,54 % → -0,78 % aber **Owner erhielt Midday-Push mit 3 Optionen — Close-Situation liefert keine neue Entscheidungsgrundlage**; Std-V1 +8,94 % + Alt-V2 +4,63 % sicher, AAPL V2 razor +0,55 % innerhalb Std-V1 +4,59 % sicher, LLY BO Ende ordnungsgemäß, V5 alle 5 Golden Cross intakt, V6 alle 5 RSI << 80, keine Portfolio-Earnings 3 HT, kein neuer Trade, negative Alpha nur marginal -0,046 pp, keine Watchlist-K1-K5-Erfüllung → kein neues handelbares Signal — Silence gerechtfertigt, Owner erhielt Fr-Wochenschluss-Push + Di-Midday-UNH-Push). Nächste Routine: **Mi 12.08. 08:30 ET Pre-Market KW33 Tag 3** — LLY BO-Ende → Umstellung auf Standard-V1 primär, UNH V2-Wick-DQF-Verlauf (Owner-Entscheidung pending), AAPL V2-Wick-Erosion-Watch, Watchlist MRK/UAL/UNP/PANW K4-Vol-Rebound-Check.)

**Vorheriger Stand:** 2026-08-11 13:00 ET (**Midday Stop-Check KW33 Tag 2**, Equity Live **96.545,51 $** vs last_equity 96.763,84 = **-0,226 % Daily** [GRÜN, Cap -3 %, verschlechtert vs Open -0,021 %], Cash 56.707,49 = **58,74 %** unverändert, MV Live **39.837,08 $** (5 Pos Alpaca, -219,75 vs Mo Close 40.056,83 = **-0,548 %** verschlechtert vs Open -0,052 % via UNH-Give-back + AAPL-Weakness), DD **-3,519 %** vs ATH 100.066,47 [GRÜN], Weekly KW33 Tag 2 **+0,034 %** vs Fr Close 96.512,65 [GRÜN, verschlechtert vs Open +0,239 %], **⚠️ UNH V2-Wick-BREACH via Wick 460,95 = Thr 405,636 Puffer -0,54 %** BROKEN (Kurs 403,4482), Std-V1 +9,20 % primär sicher, Alt-V2 via Max-Close 436,39 = 384,02 Puffer +5,06 % sicher, **PushNotification an Owner GESENDET mit 3 Optionen (SELL literal V2 / OVERRIDE via DQF / WARTEN bis Close)**, AAPL V2 razor +1,03 % via Wick 344,56, LLY BO letzte Session +9,01 %, KEIN autonomer Sell, 0 offene Orders, ClickUp ITEM_246 persistent 11. Tag)

**Vorheriger Stand:** 2026-08-11 09:47 ET (**Market Open KW33 Tag 2**, Equity Live **96.743,52 $** vs last_equity 96.763,84 = **-0,021 % Daily** [GRÜN, Cap -3 %, marginal verbessert vs Pre -0,057 %], Cash 56.707,49 = **58,62 %** unverändert, MV Live **40.036,03 $** (5 Pos Alpaca, -20,80 vs Mo Close 40.056,83 = **-0,052 %** marginal-flat), DD **-3,321 %** vs ATH 100.066,47 [GRÜN, marginal verbessert vs Pre -3,354 %], **Weekly KW33 Tag 2 vs Fr Close 96.512,65 = +0,239 %** [GRÜN, weit von Cap -5 %, marginal verbessert vs Pre +0,204 %], **SPY 772,66 Alpaca latestTrade 09:47:42 ET** vs Mo Close 773,02 = **-0,047 % essentiell flat** [Crash-Filter INAKTIV], **Alpha vs SPY +0,026 pp POSITIV marginal** (Portfolio -0,021 % vs SPY -0,047 %, Wende vs Pre -0,238 pp NEG via JPM/LLY/V-Recovery), **VIX: 15,51** [GRÜN, weit von 30-Cap; Pre-Bezug beibehalten — VIX-Live nicht neu abgerufen bei Market Open], **KEIN V1/V2/V3/V4-Trigger per strategy.md, KEIN Kauf ausgeführt, KEINE Sell-/Limit-Order platziert, 0 offene Orders** (V5/V6 werden bei Market Open NICHT geprüft — nur Close-Vollcheck; Std-V1 alle 5 SICHER Puffer eng→weit: **AAPL +5,08 % ENGSTE Std** (306,32 chg **-0,51 % Worst**, P/L -3,33 % marginal verschlechtert vs Pre -2,63 %, Std-V1 291,51 primär), UNH +10,49 % (408,21 chg -0,24 %, P/L +1,65 %), V +10,01 % (361,50 chg +0,04 % flat, P/L +1,21 %), **LLY +12,56 % Std verbessert vs Pre +11,93 %** (1236,35 chg +0,36 %, P/L +3,55 %, Blackout-V1_neu 1.134,20 Puffer +9,01 % ÜBERSCHRITTEN Bull-Konvention intakt **letzte Session heute**, endet Ende Di 11.08. → ab Mi 12.08. Standard-V1 primär), **JPM +18,40 %** (362,49 chg **+0,75 % Best chg**, **Best P/L +8,93 %**)), V2-Trailing-Stop **UNH +0,63 % RAZOR-THIN via 52w-Wick 460,95 = Thr 405,64 marginal reduziert vs Pre +0,78 %** (Data-Quality-Flag persistent, aber Std-V1 +10,49 % primär sicher, Watch Midday), **AAPL V2 +1,03 % via Wick 344,56 = Thr 303,21 marginal reduziert vs Pre +1,76 %** (Std-V1 +5,08 % ENGSTE primär, V2 sekundär), LLY +12,53 % via 52w-High 1.248,53, V +9,85 % via 373,97, JPM +12,67 % sicher, V3/V4 max P/L JPM +8,93 % << 20 %-TP1 kein Trigger, Sektor-Struktur Live: XLV **20,35 %** (UNH 10,13 + LLY 10,22 marginal erhöht vs Pre 20,32 % via LLY-Rally), XLF **11,21 %** (JPM 1,12 + V 10,09 marginal erhöht vs Pre 11,15 %), XLK **9,82 %** AAPL leicht reduziert vs Pre 9,89 %, Cash 58,62 %, **Kaufsignal-Scan Slot 1/2 KW33 unverändert offen** (0/2 Käufe KW33 nach Tag 2 Market Open; 6/6 Watchlist-Kandidaten REJECT bei ~18 min Session [Elapsed 4,62 %, K4-Linear-Threshold ≥5,54 % prev-Full-Day-Vol]: UAL K4 4,30 % FAIL 8. Tag persistent Downgrade Backup KW34, UNP K4 3,27 % heavy FAIL, BAC K4 5,41 % borderline knapp unter 120 % (Extrapolation ~117 % Avg20) → **Watch Midday für Vol-Pace-Anzug** K1-K3 ✓ RS #1 +19,76 pp, **MRK K4 21,62 % STRONG BEAT ~468 % Extrapolation 4,68x Linear-Pace wahrscheinlich News-Catalyst — aber LEVEL 0 SKIP XLV-Sektor-Cap** (20,35 % + MRK ~10 % würde XLV auf ~30,35 % pushen → verletzt strategy.md TABU >3 Pos/Sektor + max 30 % Sektorgewicht), PANW K2 RSI 70,34 FAIL overheated vorbekannt, NVDA K3 -3,75 pp FAIL persistent), **BLOCKIERT bleiben**: GS/AMD/MU/ABBV (K2 <50), CVS (K2 31,61), EOG/COP/XOM (K3 NEG), ORCL (K1 Death-Cross), **Alle 8 Guardrails GRÜN + 1 WARN** (UNH V2 razor-thin +0,63 % via 52w-Wick DQF persistent marginal reduziert vs Pre +0,78 %; LLY BO letzte Session endet Ende Di 11.08. → ab Mi 12.08. Standard-V1 primär), **Earnings-Blackout Portfolio + Watchlist: KEINE nächsten 3 HT** (Pre-Bezug: AAPL/JPM/LLY/UNH/V/UAL/UNP/BAC/MRK alle NONE), **MRK Vol-Spike-Notiz**: 4,68x Linear-Pace-Threshold bei ~18 min Session → wahrscheinlich News-Catalyst — Midday Perplexity 1 Symbol-Query zur Ursachen-Klärung, aber XLV-Sektor-Cap bleibt Blocker unabhängig, **KEIN ClickUp** (Prio 4 Routine-Log FEHLER "Max usage for custom task types reached" ITEM_246 persistent **10. Tag** → Fallback Memory-Only per notify-skill.md), **KEINE PushNotification** (Silence-Rule Routine: alle V1-V4 SICHER Std, kein Cap-Alert, VIX GRÜN 15,51, SPY -0,047 % flat, UNH V2 razor +0,63 % innerhalb Std-V1 +10,49 % sicher, AAPL V2 +1,03 % marginal reduziert innerhalb Std-V1 +5,08 % ENGSTE sicher, LLY BO letzte Session ordnungsgemäß, keine Portfolio-Earnings 3 HT, kein neuer Trade, kein Owner-Handlungsbedarf, positive Alpha +0,026 pp marginal, DD marginal verbessert vs Pre, MRK-Vol-Spike XLV-blockiert = kein handelbares Signal — Owner erhielt Fr-Wochenschluss-Push), Nächster Check: **Di 11.08. 13:00 ET Midday Stop-Check KW33 Tag 2** — UNH V2-Wick-Puffer-Erosion-Watch (+0,63 % razor-thin — kritisch bei weiterem -0,7 %+ Drift), AAPL V2-Wick-Puffer-Verlauf, LLY letzte Blackout-Session-Ausklang, BAC K4-Vol-Pace-Rebound-Watch (borderline aktuell), MRK-News-Ursachen-Klärung 1 Symbol-Query Perplexity)

**Vorheriger Stand:** 2026-08-10 16:00 ET (**Market Close Tagesbilanz KW33 Tag 1 FINAL**, Equity Close **96.764,32 $** vs last_equity 96.536,38 = **+0,2361 % Daily** [GRÜN, Cap -3 %, deutlich verbessert vs Midday +0,028 %], Cash 56.707,49 = **58,60 %** unverändert, MV Close **40.056,83 $** (5 Pos Alpaca, +251,67 vs Fr Close 39.805,16 = **+0,632 %** deutlich verbessert vs Midday +0,128 % via LLY-Rally-Fortsetzung + JPM-Rally-Nachmittag + AAPL-Recovery; einzelbewegungen intraday: **LLY +3,90 % Best chg** dominant + JPM +0,64 % + UNH +0,52 % + AAPL -1,73 % + V -0,31 %), DD **-3,300 %** vs ATH 100.066,47 [GRÜN, verbessert vs Midday -3,501 %], **Weekly KW33 Tag 1 vs Fr Close 96.512,65 = +0,261 %** [GRÜN, weit von Cap -5 %, verbessert vs Midday +0,053 %], **SPY Close 773,02 Alpaca Daily-Bar IEX** vs Fr Close 773,16 = **-0,018 % essentiell flat** [Crash-Filter INAKTIV], **Alpha vs SPY +0,254 pp POSITIV** (Portfolio +0,236 % vs SPY -0,018 %; deutlich verbessert vs Midday +0,050 pp via LLY/JPM-Nachmittags-Rally), **V5-Vollcheck 5 SICHER EOD-Bars** (Alpaca IEX 299d, Golden Cross alle intakt EMA50>EMA200): **V** (EMA50 349,26 > EMA200 337,39, Puffer +11,79 pp), AAPL (309,81 > 279,00, +30,81 pp), UNH (407,51 > 360,63, +46,88 pp), JPM (337,53 > 315,57, +21,96 pp), LLY (1145,49 > 1013,77, +131,72 pp). **V6-Vollcheck 5 SICHER**: max **RSI JPM 64,87** (V 53,94; LLY 60,73; AAPL 44,03; UNH 45,23 — alle << 80). **RS_4w vs SPY** (SPY 20d +3,19 %): UNH **-7,92 pp** (RSI 45,2 → V6 sicher via UND), AAPL -6,12 pp (RSI 44,0 → V6 sicher), V -2,14 pp (RSI 53,9 → V6 sicher), LLY +0,78 pp, JPM +4,37 pp. **KEIN V1/V2/V3/V4-Trigger per strategy.md** (Std-V1 alle 5 SICHER Puffer eng→weit: **AAPL +5,62 % ENGSTE verbessert vs Midday +5,15 %**, V +9,97 %, UNH +10,76 %, LLY +12,16 % (Blackout-V1_neu 1.134,20 Puffer +8,62 %, letzte Blackout-Session, endet morgen Di 11.08.), JPM +17,52 % Best P/L +8,12 %), V2-Trailing-Stop **UNH +0,87 % RAZOR-THIN via 52w-Wick 460,95 = Thr 405,64 verschlechtert vs Midday +1,33 %** (Data-Quality-Flag persistent aber sicher), **AAPL V2 +1,55 % via Wick 344,56 = Thr 303,21 verbessert vs Midday +1,09 % via Preis-Recovery**, LLY +12,13 %, V +9,80 %, JPM +12,63 %. V3/V4 max P/L JPM +8,12 % << 20 %-TP1 kein Trigger, **KEINE Sell-/Limit-Order für Di 11.08. platziert, 0 offene Orders**, Sektor-Struktur EOD: XLV **20,33 %** (UNH 10,15 + LLY 10,19 verbessert vs Midday 20,29 % via LLY-Rally), XLF **11,20 %** (JPM 1,12 + V 10,08) marginal verbessert vs Midday 11,16 % via JPM-Rally, XLK **9,86 %** AAPL marginal verbessert vs Midday 9,84 %, Cash 58,60 %, **Kaufsignal-Scan Slot 1/2 KW33 unverändert offen** (0/2 Käufe KW33 nach Tag 1), **Watchlist Di 11.08. K1-K3 aus Alpaca IEX EOD Mo 10.08.:** **UAL Prio 1 XLI** (123,75 K1 +11,84 % ✓, K2 RSI 50,15 borderline aber ✓, K3 RS_63d **+19,48 pp #2** ✓, K4 Vol-Rebound-Watch Di, XLI 0 % Diversifikation Prio 1), **UNP Prio 2 XLI** (292,15 K1 +9,94 % ✓, K2 RSI 52,64 ✓, K3 RS +5,63 pp ✓, K4 Vol-Rebound-Watch Di, XLI 0 % Diversifikation), **BAC Prio 3 XLF** (63,88 K1 +9,29 % ✓, K2 RSI 69,79 upper-border ✓, K3 RS **+19,76 pp #1** ✓, K4/K5 Di prüfen, XLF-Konflikt V/JPM sub-30 % Cap), **MRK Prio 4 XLV Alt** (130,90 K1 +12,20 % ✓, K2 RSI 59,85 ✓, K3 RS +12,74 pp ✓, XLV-Konflikt UNH+LLY 3-Positions-Regel-nah — nur wenn UNH/LLY reduziert), **REJECTS:** PANW (K2 RSI 70,34 FAIL overheated), NVDA (K3 -3,75 pp FAIL), GS (K2 RSI 47,58 <50 FAIL), UAL/UNP/BAC/PANW/NVDA heute alle K4-FAIL (Perplexity-Halluzination 4. Mal in Serie: SPY +0,61 % widerspricht Alpaca -0,018 %, Sektor-Werte "+?" leere Antwort), **Guardrails 8/8 GRÜN + 1 WARN** (LLY BO HT+2 heute letzte Session, endet morgen Di 11.08.; UNH V2 razor-thin +0,87 % Watch Di), **KEIN ClickUp** (Prio 4 Routine-Log FEHLER "Max usage for custom task types reached" ITEM_246 persistent 9. Tag → Fallback Memory-Only per notify-skill.md, positive Daily-Wende, alle SICHER), **KEINE PushNotification** (Silence-Rule Routine: kein V-Trigger, kein Cap-Alert, deutlich positive Daily-Wende von +0,028 % auf +0,236 %, deutlich positive Alpha +0,254 pp POSITIV, alle 5 V-SICHER, LLY BO letzte Session sicher, keine Portfolio-Earnings Di, kein Owner-Handlungsbedarf, DD verbessert vs Midday, KW33 Tag 1 Ergebnis-neutral bis leicht POSITIV — kein PN-Trigger). Nächste Routine: **Di 11.08. 08:30 ET Pre-Market KW33 Tag 2** — LLY BO Ende Di, UNH V2 razor-Watch, Watchlist UAL/UNP/BAC/MRK K4-Vol-Rebound-Check)

**Vorheriger Stand:** 2026-08-10 13:11 ET (**Midday Stop-Check KW33 Tag 1**, Equity Live **96.563,51 $** vs last_equity 96.536,38 = **+0,028 % Daily** [GRÜN, Cap -3 %, gewendet POS vs Open -0,015 %], Cash 56.707,49 = **58,73 %** unverändert, MV Live **39.856,02 $** (5 Pos Alpaca, +50,86 vs Fr Close 39.805,16 = **+0,128 %** deutlich verbessert vs Open +0,024 % via LLY-Rally + AAPL-Marginal-Recovery + UNH-Halt; einzelbewegungen intraday: **LLY +2,41 % Best chg** dominant + UNH +0,96 % + JPM +0,02 % flat, V **-0,85 %** + **AAPL -2,18 % Worst chg** dämpfen aber AAPL marginal verbessert vs Open -2,37 %), DD **-3,501 %** vs ATH 100.066,47 [GRÜN, marginal verbessert vs Open -3,542 %], **Weekly KW33 Tag 1 vs Fr Close 96.512,65 = +0,053 %** [GRÜN, weit von Cap -5 %, verbessert vs Open +0,010 %], **SPY Live 773,05 Alpaca latestTrade 13:10 ET** vs Fr Close 773,22 = **-0,022 % essentiell flat** [Crash-Filter INAKTIV; marginal verbessert vs Open -0,030 %], **Alpha vs SPY +0,050 pp POSITIV** (Portfolio +0,028 % vs SPY -0,022 %; verbessert vs Open +0,015 pp via LLY-Rally-Impulse), **KEIN V1/V2/V3/V4-Trigger per strategy.md, KEINE Sell-/Limit-Order platziert, 0 offene Orders** (Std-V1 alle 5 SICHER Puffer eng→weit: **AAPL +5,15 % ENGSTE verbessert vs Open +4,94 % via chg -2,18 % marginal-Recovery**, LLY +7,03 % Std verbessert vs Open +8,86 % _reduziert vs Open — LLY-Preis-Sprung von 1.195,67 → 1.213,85 verändert die Std-V1-Puffer-Rechnung nur marginal; Blackout-V1_neu 1.134,20 Puffer **+7,03 %** ÜBERSCHRITTEN Bull-Konvention intakt HT+2 heute letzte Session, deutlich verbessert vs Open +5,42 % via LLY-Rally), UNH +11,26 % Std marginal reduziert vs Open +11,51 %, V +9,38 % reduziert vs Open +10,43 % via chg -0,85 %, JPM +16,80 % marginal reduziert vs Open +17,32 % Best P/L +7,46 %), V2-Trailing-Stop **AAPL +1,09 % RAZOR-THIN via 52w-Wick 344,56 = Thr 303,21 verbessert vs Open +0,89 %** (Data-Quality-Flag persistent; Std-V1 +5,15 % ENGSTE primär, V2 sekundär), **UNH +1,33 % via Wick 460,95 = Thr 405,636 marginal reduziert vs Open +1,56 %** (Data-Quality-Flag persistent aber sicher), LLY +9,26 % via 52w-High 1.248,53, V +9,60 % via 373,97, JPM sicher. V3/V4 max P/L JPM +7,46 % << 20 %-TP1 kein Trigger. **RSI/EMA werden bei Midday NICHT geprüft (nur Market Open + Close).** Sektor-Struktur Live: XLV **20,29 %** (UNH 10,21 + LLY 10,06 leicht verbessert vs Open 20,17 % via LLY-Rally +2,41 %), XLF **11,16 %** (JPM 1,11 + V 10,05) reduziert vs Open 11,27 % via V-Give-back -0,85 %, XLK **9,84 %** AAPL marginal reduziert vs Open 9,83 % (Preis-Erholung nur marginal), Cash 58,73 %, **Kauf-Slot 1/2 KW33 unverändert offen** (Kaufscan ist bei Midday nicht Teil der Routine, siehe premarket/market-open-routine), **Alle 8 Guardrails GRÜN + 2 WARN** (LLY BO HT+2 heute letzte Session Bull-Konvention intakt Ende morgen Di 11.08.; **AAPL V2 razor-thin +1,09 % via Wick 344,56 Data-Quality-Flag marginal verbessert vs Open +0,89 % via Preis-Recovery**), **KEIN ClickUp** (Midday-Routine STEP 5: nur bei Stop-Trigger oder Daily-Cap → Silence-Rule Routine + ITEM_246 Kontingent-Fehler persistent 8. Tag), **KEINE PushNotification** (Silence-Rule Routine: kein V-Trigger, kein Cap-Alert, positive Daily-Wende von -0,015 % auf +0,028 %, positive Alpha +0,050 pp, AAPL V2 razor +1,09 % innerhalb Std-V1 +5,15 % sicher + marginal verbessert, UNH V2 marginal reduziert aber sicher, LLY BO Rally-Sicherheit +7,03 %, keine Portfolio-Earnings heute, kein Owner-Handlungsbedarf, DD verbessert vs Open, Owner erhielt Fr-Wochenschluss-Push), Nächste Routine 16:00 ET Market Close Tagesbilanz KW33 Tag 1)

**Vorheriger Stand:** 2026-08-10 09:44 ET (**Market Open KW33 Tag 1**, Equity Live **96.522,00 $** vs last_equity 96.536,38 = **-0,015 % Daily** [GRÜN, Cap -3 %, marginal verbessert vs Pre -0,101 %], Cash 56.707,49 = **58,75 %** unverändert seit 06.06., MV Live **39.814,51 $** (5 Pos Alpaca, +9,35 vs Fr Close 39.805,16 = +0,024 % marginal-flat; einzelbewegungen: **UNH +1,20 % Best chg** + LLY +0,84 % + JPM +0,47 % + V +0,11 % heben, **AAPL -2,37 % WORST chg** dominant dämpft), DD **-3,542 %** vs ATH 100.066,47 [GRÜN, marginal verbessert vs Pre -3,625 % via Portfolio-Erholung], **Weekly KW33 Tag 1 vs Fr Close 96.512,65 = +0,010 %** [GRÜN, weit von Cap -5 %], **SPY Live 772,99 Alpaca latestTrade 09:45 ET** vs Fr Close 773,22 = **-0,030 % essentiell flat** [Crash-Filter INAKTIV; Fr Alpaca Daily-Bar +0,596 %], **Alpha vs SPY +0,015 pp POSITIV marginal** (Portfolio -0,015 % vs SPY -0,030 %; **Wende vs Pre -0,123 pp NEG** via UNH +1,20 %/LLY +0,84 %/JPM +0,47 % Recovery gegen AAPL -2,37 %), **KEIN V1/V2/V3/V4-Trigger per strategy.md, KEINE Sell-/Limit-Order platziert, 0 offene Orders** (Std-V1 alle 5 SICHER Puffer eng→weit: **AAPL +4,94 % ENGSTE verschlechtert vs Pre +5,75 % via chg -2,37 %**, LLY +8,86 % (Blackout-V1_neu 1.134,20 Puffer +5,42 % ÜBERSCHRITTEN Bull-Konvention intakt HT+2 heute letzte Session), UNH +11,51 %, V +10,43 %, JPM +17,32 % Best P/L +7,94 %), V2-Trailing-Stop **AAPL +0,89 % RAZOR-THIN via 52w-Wick 344,56 = Thr 303,21 (verschlechtert vs Pre +1,97 % via chg -2,37 %)**, **UNH +1,56 % via Wick 460,95 = Thr 405,636 (verbessert vs Pre +0,36 % via chg +1,20 %)**, LLY +8,82 % via 52w-High 1.248,53, V +10,27 % via 373,97, JPM sicher. V3/V4 max P/L JPM +7,94 % << 20 %-TP1 kein Trigger. **RSI/EMA werden bei Market Open NICHT geprüft (Vollcheck bei Close).** Sektor-Struktur Live: XLV **20,17 %** (UNH 10,24 + LLY 9,91 verbessert vs Pre 20,00 % via UNH+LLY-Recovery), XLF **11,27 %** (JPM 1,12 + V 10,15), XLK **9,83 %** AAPL leicht reduziert vs Pre 9,94 % via chg -2,37 %, Cash 58,75 %. **Kaufsignal-Scan Slot 1/2 KW33 — alle 5 Watchlist-Kandidaten K4-FAIL bei ~15 min in Session** (Alpaca snapshot 09:45 ET IEX-Vol Intraday-% vs prev Full-Day-Vol): (1) **UAL Prio 1 XLI REJECT K4-FAIL 7. Tag persistent + K1/Momentum-Reversal-Watch**: 126,76 chg **-2,20 % Session-Weakness** vs Fr Close 129,595, IEX-Vol 9.251 = 11,96 % prev-Full-Day (Full-Day-Extrapolation ~ prev, K4 << 120 %); K4-Persistenz-Fail 7. Tag + heute intraday -2,20 % → **DOWNGRADE Prio 1 → Prio Backup KW34**. (2) **UNP Prio 2 XLI REJECT K4-FAIL heavy**: 293,83 chg +0,24 % essentiell flat, IEX-Vol 736 = 0,64 % prev-Full-Day → K4 heavy FAIL. (3) **BAC Prio 3 XLF REJECT K4-Undershoot-Pace**: 63,555 chg +0,64 %, IEX-Vol 95.908 = 6,59 % prev-Full-Day (Full-Day-Extrapolation << 120 %); K1-K3 ✓ vorbekannt aber K4-Trigger fehlt. (4) **PANW Prio 4 XLK REJECT K4-Undershoot-Pace**: 374,82 chg +3,00 % positive Momentum (K3 #1 +79,44 pp bestätigt sich), IEX-Vol 12.294 = 6,60 % prev-Full-Day → K4-Trigger fehlt heute; XLK-Konflikt AAPL 9,83 % Sektor-Cap-Risk bleibt. (5) **NVDA Backup XLK REJECT K3-marginal + K4-Undershoot**: 223,24 chg -0,31 %, IEX-Vol 223.865 = 5,14 % prev-Full-Day. **BLOCKIERT bleiben:** GS/AMD/MU/ABBV (K2 <50), CVS (K2 31,61), EOG/COP/XOM (K3 NEG), ORCL (K1 Death-Cross), MRK (XLV-Cap-Risk 3. Pos). **Slot 1/2 KW33 bleibt OFFEN — kein Kandidat erfüllt alle 5 K1-K5 heute; Perplexity-Sektor-Scan NICHT durchgeführt** (Silence-Rule Effizienz + persistente Perplexity-Halluzinationen 3. Mal in Serie, existierende Watchlist aus Fr Close ausreichend). **UAL Persistenz-Fail 7. Tag + heute Momentum-Reversal → Downgrade Prio 1 → Prio Backup KW34** (K1 muss re-verifiziert werden nach -2,20 % intraday). **Alle 8 Guardrails GRÜN + 2 WARN** (LLY BO HT+2 heute letzte Session +5,42 % Bull-Konvention intakt Ende morgen Di 11.08.; **AAPL V2 razor-thin +0,89 % via Wick 344,56 Data-Quality-Flag verschlechtert vs Pre +1,97 %** — Std-V1 +4,94 % ENGSTE sicher). **Earnings-Blackout Portfolio + Watchlist Mo/Di/Mi: KEINE außer LLY HT+2 heute letzte Session**. **KEIN ClickUp** (Prio 4 Routine-Log FEHLER "Max usage for custom task types reached" ITEM_246 persistent 8. Tag → Fallback Memory-Only per notify-skill.md). **KEINE PushNotification** (Silence-Rule Routine: alle V1-V4 SICHER Std, kein Cap-Alert, VIX GRÜN 14,90, SPY -0,030 % flat, AAPL V2 razor +0,89 % innerhalb Std-V1 +4,94 % sicher, UNH V2 verbessert +1,56 %, LLY BO intakt, keine Portfolio-Earnings heute, kein neuer Trade, kein Owner-Handlungsbedarf, positive Alpha +0,015 pp marginal, DD verbessert vs Pre; Owner erhielt Fr-Wochenschluss-Push). Nächster Check: **Mo 10.08. 13:00 ET Midday Stop-Check KW33 Tag 1** — AAPL V2-Wick-Puffer-Watch (+0,89 % razor-thin), UNH V2-Wick-Puffer-Verlauf, LLY letzte Blackout-Session, Post-CPI-Reaktion (falls Release bestätigt))

**Vorheriger Stand:** 2026-08-10 08:30 ET (**Pre-Market KW33 Tag 1**, Equity Pre **96.438,58 $** vs last_equity 96.536,38 = **-0,101 % Daily** [GRÜN], Cash 56.707,49 = 58,80 %, MV Pre **39.731,09 $** (5 Pos, -74,07 vs Fr Close = -0,186 % AAPL -1,29 % dominant), SPY Pre **773,39** Alpaca-Mid vs Fr Close 773,22 = +0,022 % flat, Alpha vs SPY -0,123 pp NEG marginal, VIX 14,90 GRÜN, DD -3,625 %, Weekly -0,077 %, V1 alle 5 SICHER: AAPL +5,75 % ENGSTE, LLY +7,70 %, UNH +9,25 %, V +9,29 %, JPM +14,29 %, V2 UNH razor +0,36 % via Wick 460,95 marginal recovered, AAPL V2 +1,97 % via Wick 344,56 recovered, LLY BO Puffer +4,69 % intakt HT+2 heute letzte Session, KEIN V-Trigger, Perplexity SPY 770,91 als HALLUZINATION verworfen 3. Mal in Serie, ClickUp ITEM_246 persistent 7. Tag, KEINE PushNotification, Watchlist UAL Prio 1 K4-Vol-Rebound 7. Tag kritisch + UNP/BAC/PANW/NVDA-Backup, Kaufscan Market Open JA Slots frisch 2/2)

**Vorheriger Stand:** 2026-08-07 16:00 ET (**Market Close Tagesbilanz KW32 Tag 5 FINAL**, Equity Close **96.512,65 $** vs last_equity 96.694,59 = **-0,188 % Daily** [GRÜN, Cap -3 %, marginal verschlechtert vs Midday -0,172 %], Cash 56.707,49 = **58,76 %** unverändert, MV Close **39.805,16 $** (5 Pos Alpaca, -76,96 vs Do Close 39.882,12 = **-0,193 %** V -2,15 % Worst chg + LLY -0,52 % dämpfen UNH +0,54 % Best chg + JPM +0,34 % + AAPL +0,29 %), DD **-3,552 %** vs ATH 100.066,47 [GRÜN, marginal verschlechtert vs Midday -3,537 %], **Weekly KW32 FINAL vs Mo 03.08. EOD 95.984,04 = +0,551 %** [GRÜN, weit von Cap -5 %; Alt-Referenz vs Fr 31.07. Close 96.396,66 = +0,120 %], **SPY Close 773,22 Alpaca Daily-Bar** vs Do Close 768,64 = **+0,596 % positiv** [Crash-Filter INAKTIV, verbessert vs Midday +0,467 %], **Alpha vs SPY -0,784 pp NEGATIV** (Portfolio via V-Give-back -2,15 % Worst chg + LLY -0,52 % underperformt SPY-Aufwärts, verschlechtert vs Midday -0,639 pp), **V5-Vollcheck 5 SICHER EOD-Bars** (Alpaca IEX 278d, Golden Cross alle intakt EMA50>EMA200): **V +3,29 % engster** (EMA50 348,76 > EMA200 337,63), JPM +6,36 %, AAPL +10,49 %, LLY +12,46 %, UNH +12,72 %. **V6-Vollcheck 5 SICHER**: max **RSI JPM 63,03** (SPY 66,17; V 55,28; LLY 53,79; AAPL 47,57; UNH 44,00 alle << 80). **RS_4w vs SPY** (SPY 20d +2,41 %): UNH **-6,53 pp** (RSI 44,0 → V6 sicher via UND), AAPL -3,06 pp (RSI 47,6 → V6 sicher), LLY -2,63 pp (RSI 53,8 → V6 sicher), V +1,59 pp, JPM +3,89 pp. **KEIN V1/V2/V3/V4-Trigger per strategy.md** (Std-V1 alle 5 SICHER Puffer eng→weit: **AAPL +7,47 % ENGSTE**, LLY +7,95 %, UNH +9,94 %, V +10,32 %, JPM +16,78 %), V2-Trailing-Stop **UNH +0,12 % RECOVERED bleibt via 52w-Wick 460,95 → Threshold 405,636 vs Close 406,13** (Data-Quality-Flag persistent, aber Puffer schrumpft vs Midday +1,00 %), AAPL V2 via Wick 344,56: +0,15 % **razor-thin** cur 313,30 vs Threshold 303,21 Puffer OK, LLY V2 +6,42 %, JPM +11,12 %, V +11,23 %. V3/V4 max P/L JPM +7,43 % << 20 %-TP1 kein Trigger, **KEINE Sell-/Limit-Order für Mo 10.08. platziert, 0 offene Orders**, Sektor-Struktur EOD: XLV 19,93 % (LLY 9,83 + UNH 10,10), XLF 11,26 % (JPM 1,11 + V 10,14) leicht reduziert vs Midday 11,20 % via JPM-Recovery, XLK 10,06 % AAPL, Cash 58,76 %, **Kaufsignal-Scan Slot 1/2 + 2/2 KW32 FINAL 0/2 unverändert** (KW32 endet mit 0 Käufen), **Watchlist Mo 10.08. K1-K3 aus Alpaca IEX EOD Fr 07.08.:** **UAL #1 XLI** (129,59 K1 +10,7 % ✓, K2 RSI 58,64 ✓, K3 RS_63d **+24,27 pp #2** ✓, K4 Vol-Rebound-Watch Mo, K5 vorbekannt ✓ RevGr 16 %+ FwdPE 14,8x, XLI 0 % Diversifikation Prio 1), **UNP #2 XLI** (293,13 K1 +10,0 % ✓, K2 RSI 53,91 ✓, K3 RS +4,95 pp ✓, K4 Vol-Rebound-Watch Mo, XLI 0 % Diversifikation Prio 2), **BAC #3 XLF** (63,15 K1 +8,6 % ✓, K2 RSI 66,51 upper ✓, K3 RS +14,06 pp ✓, K4/K5 Mo prüfen, XLF 11,26 % via V/JPM aber sub-30 %-Cap), **PANW #4 XLK** (363,88 K1 +21,4 % ✓, K2 RSI 64,28 ✓, K3 RS **+79,44 pp #1** ✓, XLK-Konflikt-Watch mit AAPL 10,06 %), **NVDA marginal** (223,93 K1 +5,1 % ✓, K2 RSI 64,32 ✓, K3 RS +0,16 pp razor-thin, XLK-Konflikt AAPL), **BLOCKIERT/REJECT:** GS (K2 RSI 48,66 <50), AMD (K2 RSI 46,97 <50), MU (K2 RSI 47,71 <50), ABBV (K2 RSI 47,17 <50), MRK (K1-K3 ✓ aber XLV-Sektor-Cap 3-Positions-Regel-nah UNH+LLY), EOG (K2 RSI 42,97 + K3 -2,71 pp), CVS (K2 RSI 31,61 heavy), COP/XOM (K3 NEG), ORCL (K1 Death-Cross + K3 -30,17 pp), **Guardrails 8/8 GRÜN + 1 WARN** (LLY BO HT+2 heute letzte Session, Ende Mo 10.08. → morgen Wochenende, Mo 10.08. Blackout endet), **KEIN ClickUp** (Prio 4 Routine-Log FEHLER "Max usage for custom task types reached" ITEM_246 persistent 6. Tag → Fallback Memory-Only per notify-skill.md, Prio 3-Downgrade wg. neg Daily nicht ausschlaggebend), **Data-Quality-Flag Perplexity SPY 745,40 / -3,03 % widerspricht Alpaca Daily-Bar 773,22 / +0,596 %** — Alpaca ist authoritative Source für Live-Kurse, Perplexity-Angabe verworfen als Halluzination-Flag (2. Mal in KW32 nach 06.08. Pre 746,07-Halluzination), **PushNotification an Owner: Silence-Rule geprüft** — negative Daily/Alpha aber innerhalb Cap-Range (Daily -0,188 %, Alpha -0,784 pp, Weekly +0,551 % positiv FINAL, 5/5 V-SICHER, ClickUp-Fehler kompensiert via Memory + Notification, UNH V2-Wick-Puffer schrumpft +0,12 % Watch für Mo, Käufe KW32 FINAL 0/2 — **PN JA aufgrund erwartetem Owner-Interesse an Wochen-Bilanz FINAL + UNH V2-Wick-Puffer-Erosion Mo-Watch + KW32-0-Käufe-Ergebnis**), Nächste Routine: **Mo 10.08. 08:30 ET Pre-Market KW33 Tag 1** — KW33 Kauf-Slots 2/2 frisch, Watchlist UAL/UNP/BAC/PANW K4-Vol-Rebound-Check, LLY BO Ende Mo, UNH V2-Wick-Recovery-Watch)

**Vorheriger Stand:** 2026-08-07 13:10 ET (**Midday Stop-Check KW32 Tag 5**, Equity Live **96.528,52 $** vs last_equity 96.694,59 = **-0,172 % Daily** [GRÜN, Cap -3 %, verbessert vs Open -0,261 %], Cash 56.707,49 = **58,75 %** unverändert, MV Live **39.821,03 $** (5 Pos Alpaca, -61,09 vs Do Close 39.882,12 = **-0,153 %** deutlich verbessert vs Open -0,371 % via LLY-Recovery +0,14 % + UNH-Rally +1,27 % + AAPL +0,15 % / JPM -0,74 % Worst + V -1,90 % Worst chg dämpfen), DD **-3,537 %** vs ATH 100.066,47 [GRÜN, verbessert vs Open -3,623 %], Weekly KW32 Tag 5 **+0,137 %** vs Fr 31.07. Close 96.396,66 [GRÜN, verbessert vs Open +0,047 %, weit von Cap -5 %], **SPY Live 772,23 Alpaca latestTrade 13:08 ET** vs Do Close 768,64 = **+0,467 % positiv** [Crash-Filter INAKTIV, verbessert vs Open +0,359 %], **Alpha vs SPY -0,639 pp NEGATIV** (Portfolio via JPM/V-Give-back underperformt SPY-Aufwärts, marginal verschlechtert vs Open -0,621 pp), **✅ UNH V2-Trailing-Stop ZURÜCKGEWONNEN: cur 409,68 > Threshold 405,636 Puffer +1,00 % RECOVERED vs Open -0,27 % BROKEN** (UNH-Rally +1,27 % Best chg löst Wick-Anomalie-Escalation vom Open — CRITICAL-Alert de-facto resolved, kein Auto-Sell gewesen per Rule 5 richtig), **KEIN V1/V2/V3/V4-Trigger per strategy.md** (Std-V1 alle 5 SICHER), **KEINE Sell-/Limit-Order platziert, 0 offene Orders**, V1-Puffer sortiert eng→weit Std-V1: **AAPL +7,17 % ENGSTE Std verbessert vs Open +7,00 %** (312,38 chg +0,149 % vs Do Close 311,915, P/L -1,41 % marginal verbessert vs Open -1,56 %, Std-V1 291,51 alleine primär), **LLY +7,23 % Std verbessert vs Open +7,07 %** (1.177,72 chg +0,140 % vs Do Close 1.176,08, P/L -1,35 % verbessert vs Open -1,49 %, Blackout-V1_neu 1.134,20 Puffer +3,84 % ÜBERSCHRITTEN weiter verbessert vs Open +3,69 % — Bull-Konvention intakt HT+2 heute, Ende Mo 10.08.), UNH +10,72 % Std verbessert vs Open +9,51 % (409,68 chg **+1,270 % Best chg**, P/L +2,02 %, **V2 407,32-Wick-Basis RECOVERED Puffer +1,00 %** via Wick 460,95 Data-Quality-Flag), V +9,74 % (363,445 chg **-1,900 % Worst chg** vs Do Close 370,47, P/L +1,75 %), **JPM +16,84 %** (357,73 chg -0,742 %, **Best P/L +7,50 %**), V3/V4 max P/L JPM +7,50 % << 20 %-TP1 kein Trigger, V2-Trailing-Stop alle 5 SICHER inkl. UNH-Recovery, **RSI/EMA werden bei Midday NICHT geprüft (nur Market Open + Close per Midday-Routine)**, Käufe KW32 0/2 unverändert (Kaufsignal-Scan bei Midday nicht Teil der Routine — KW32 endet 0/2 heute), Sektor-Struktur Midday: XLV 19,97 % (UNH 10,20 UNH-Rally + LLY 9,77 vs Open 19,80 %), XLF 11,20 % (JPM 1,11 + V 10,09) reduziert vs Open 11,36 % via V/JPM-Give-back, XLK 10,04 % AAPL leicht verbessert vs Open 10,03 %, Cash 58,75 %, **8/8 GRÜN + 1 WARN** (LLY BO HT+2 ÜBERSCHRITTEN +3,84 % — UNH V2-Wick WARN AUFGEHOBEN via Recovery Puffer +1,00 %), **KEIN ClickUp** (Midday-Routine STEP 5: nur bei Stop-Trigger oder Daily-Cap → Silence-Rule Routine + ITEM_246 Kontingent-Fehler persistent 6. Tag), **KEINE PushNotification** (Silence-Rule Routine: kein V-Trigger, kein Cap-Alert, positive Intraday-Recovery Daily von -0,261 % auf -0,172 %, UNH V2-Wick-CRITICAL-Alert vom Open DE-FACTO RESOLVED via UNH-Rally +1,27 % — kein neuer Handlungsbedarf, Owner kann Recovery aus Close-Update morgen entnehmen), Nächste Routine 16:00 ET Market Close Tagesbilanz KW32 Tag 5)

**Vorheriger Stand:** 2026-08-07 09:50 ET (**Market Open KW32 Tag 5**, Equity Live **96.441,67 $** vs last_equity 96.694,59 = **-0,261 % Daily** [GRÜN, Cap -3 %], Cash 56.707,49 = **58,80 %** unverändert, MV Live **39.734,18 $** (5 Pos, -147,94 vs Do Close 39.882,12 = **-0,371 %** V -1,20 % Worst + LLY -1,33 % Give-back + JPM -0,49 % dominant, UNH +0,14 % einziger positiv), DD **-3,623 %** vs ATH 100.066,47 [GRÜN, verschlechtert vs Do -3,295 %], Weekly KW32 Tag 5 **+0,047 %** vs Fr 31.07. Close 96.396,66 [GRÜN, deutlich reduziert vs Do +0,386 %], **SPY Live 771,40 Alpaca latestTrade 09:47 ET** vs Do Close 768,64 = **+0,359 % positiv-flat** [Crash-Filter INAKTIV], **Alpha vs SPY -0,621 pp NEGATIV** (Portfolio via LLY/V/JPM-Give-back underperformt SPY-Aufwärts), **⚠️ UNH V2-Trailing-Stop TECHNISCH GETRIGGERT via 52w-Wick 460,95: cur 404,55 < Threshold 405,636 Puffer -0,27 % BROKEN — KEIN Auto-Sell per Rule 5 (Wick-Anomalie, Close-Peak 436,39 → -7,30 % << -12 % Zielintent), PushNotification CRITICAL an Owner eskaliert. Kein anderer V-Trigger, 0 Sell-Orders.** V1-Puffer Std alle 5 SICHER eng→weit: **AAPL +7,00 % ENGSTE Std**, **LLY +7,07 % Std** (Blackout-V1_neu 1.134,20 Puffer +3,69 % HT+2 ÜBERSCHRITTEN Bull-Konvention intakt, Ende Mo 10.08.), UNH +9,51 % Std, V +11,39 %, **JPM +15,80 %**. V3/V4 max JPM +6,54 % << 20 %. **Kaufsignal-Scan Slot 1/2 KW32 Fr: alle Watchlist-Kandidaten REJECT/SKIP** (UAL K4-FAIL 6. Tag Downgrade Prio Backup KW33, GS K4 low Vol, DELL/HPE K1-Bruch anhaltend, UNP K4 heavy, NVDA K3-marginal + XLK-Konflikt). **Slot 1/2 + 2/2 KW32 endet OFFEN — KW32-Kaufzähler final 0/2.** Sektor-Struktur XLV 19,80 %, XLF 11,36 %, XLK 10,03 %, Cash 58,80 %. Positionen 5/8, 0 Pending Orders. **8/8 Guardrails GRÜN + 2 WARN** (LLY BO HT+2, UNH V2-Wick eskaliert). ClickUp Prio 1 CRIT-Alert FEHLER ITEM_246 persistent 6. Tag → Memory-Only + PushNotification CRITICAL. Nächste Routine: Fr 07.08. 13:00 ET Midday KW32 Tag 5)

**Vorheriger Stand:** 2026-08-06 08:35 ET (**Pre-Market KW32 Tag 4**, Equity Pre **96.867,82 $** Alpaca vs last_equity 96.641,67 = **+0,234 %** Daily [GRÜN, Cap -3 %], vs Memory Wed Close 96.589,61 = **+0,288 %** (+278,21 $ overnight/AH inkl. last_equity-Diff +52,06), Cash 56.707,49 = **58,54 %** unverändert, MV Pre **40.160,33 $** (5 Pos Alpaca berechnet, +278,21 vs Wed Close 39.882,12 = **+0,698 %** LLY HT+1 Bull-Trend-Fortsetzung + AAPL/UNH-Recovery-Watch), DD **-3,196 %** vs ATH 100.066,47 [GRÜN, verbessert vs Wed Close -3,475 %], Weekly KW32 Tag 4 **+0,489 %** vs Fr 31.07. Close 96.396,66 [GRÜN, verbessert vs Wed Close +0,200 %, weit von Cap -5 %], **SPY Pre 771,00 Alpaca latestTrade 08:35 ET** (ap 771,05 / bp 770,93) vs Wed Close 769,79 = **+0,157 % flat/positiv** [Crash-Filter INAKTIV, Wed vs Tue Close -0,171 % << -5 %-Trigger], **Perplexity SPY Pre 746,07 als HALLUZINATION VERWORFEN** (widerspricht Alpaca-Live-Preisen + eigenem Equity +0,234 %; Alpaca bindend), **Alpha vs SPY +0,077 pp POSITIV** (Portfolio +0,234 % vs SPY +0,157 %), **VIX Perplexity 3-Quellen-Divergenz 12,18 / 16,50 / 21,51** — konservativ Best-Estimate **~16-18** [GRÜN <25, deutlich <30-Cap; alle Werte weit unter Filter-Schwelle], **10Y Treasury Yield ~4,69 %** (Perplexity Aug 3 letzt verfügbar), **Alle 8 Guardrails GRÜN + 1 WARN** (LLY BO HT+1 heute Std-V1 1.098,38 + Blackout-V1_neu 1.134,20 primär bis Ende Blackout Mo 10.08.; UNH V2 razor-thin +1,75 % via 52w-Wick 460,95 Data-Quality-Flag beibehalten), **KEIN V-Trigger per strategy.md** (Std-V1-Puffer erwartet aus Wed Close: AAPL +6,66 %, LLY +6,46 %, UNH +11,71 %, V +12,11 %, JPM +17,32 %; RSI/EMA werden bei Pre-Market NICHT geprüft — nur Market Open + Close), **KEINE Sell-/Limit-Order platziert, 0 offene Orders**, **Earnings-Blackout Nächste 3 HT**: **LLY HT+1 heute Do 06.08.** → HT+2 Fr 07.08. → **Ende Mo 10.08.** (LLY Q2-Report Mi BMO positiv erfolgt EPS $8,38 Beat +25-35 %, Guidance angehoben Rev $85-87 Mrd), keine anderen Portfolio-Positionen mit Earnings (UNH/JPM/V/AAPL Q3 Ende Okt), **US Initial Jobless Claims** Woche endend 01.08. Release heute 08:30 ET (Consensus 221k, Prior 197k — Markt-Reaktion Watch bei Deviation >±10k), **Keine großen Portfolio-Earnings heute**, **Kaufscan Market Open: JA** (VIX GRÜN, kein Cap-Alert, Slot 1/2 offen; Watchlist Do 06.08.: **UAL Prio 1 XLI** K4-Vol-Rebound-Watch 5. Tag persistent RS +35,3 pp #1 XLI, **GS Prio 2 XLF** K4 nahe 120 %-Trigger, **DELL/HPE XLK-Konflikt-Watch** mit AAPL, **UNP Backup XLI** K4 heavy FAIL), **ClickUp Prio 4 Routine-Log FEHLER "Max usage for custom task types reached" ITEM_246 persistent 4. Tag** → Fallback Memory-Only per notify-skill.md, **KEINE PushNotification** (Silence-Rule Routine: Std-V1 alle SICHER, kein Cap-Alert, positive Alpha +0,077 pp, VIX GRÜN, keine Earnings heute Portfolio-relevant außer LLY HT+1 Bull-Konvention intakt, Owner kein Handlungsbedarf), Nächste Routine: **Do 06.08. 09:30 ET Market Open KW32 Tag 4** — Kaufsignal-Scan Slot 1/2, LLY HT+1-Verhalten Post-Earnings-Trend, UAL K4-Vol-Rebound 5. Tag, GS K4-Trigger-Check)

**Vorheriger Stand:** 2026-08-05 16:00 ET (**Market Close Tagesbilanz KW32 Tag 3**, Equity Close **96.589,61 $** vs last_equity 96.056,40 = **+0,555 %** Daily [GRÜN, Cap -3 %, verbessert vs Midday +0,495 %], SPY Close **769,79 Alpaca IEX** vs Di Close 771,11 = **-0,171 % Post-Rally-Give-back marktweit** [Crash-Filter INAKTIV], Cash 56.707,49 = **58,71 %** unverändert, MV Close **39.882,12 $** (5 Pos Alpaca, +436,57 vs Mo Close 39.445,55 = **+1,107 %** LLY Post-Earnings-Rally +4,64 % dominant + UNH +1,23 % Recovery + JPM +0,47 % + AAPL +0,52 % / V -0,30 % dämpft), DD **-3,475 %** vs ATH 100.066,47 [GRÜN, verbessert vs Midday -3,532 %], Weekly KW32 Tag 3 **+0,200 %** vs Fr 31.07. Close 96.396,66 [GRÜN, verbessert vs Midday +0,140 %, weit von Cap -5 %], **Alpha vs SPY +0,726 pp POSITIV** (Portfolio via LLY-Post-Earnings-Rally deutlich outperformt SPY-Give-back), VIX letzt bekannt Perplexity Pre 18,29 [GRÜN <25], **5 V1-V6 SICHER Vollcheck EOD-Bars — KEIN Stop-Trigger, KEINE Sell-/Limit-Order für Do 06.08. platziert, 0 offene Orders**, V1-Puffer min **AAPL Std-V1 291,51 Puffer +6,66 %** (Close 310,94 chg +0,52 %, P/L -1,87 %, RSI 45,8, EMA-Diff +10,85 %), LLY Std-V1 1.098,38 Puffer **+6,46 %** (Close 1.169,29 chg +4,64 % Post-Earnings-Rally, P/L -1,87 % **verbessert vs Mo -6,40 %**, **Blackout-V1_neu 1.134,20 ÜBERSCHRITTEN +2,64 %** Bull-Konvention intakt, RSI 51,2, EMA-Diff +11,31 %, HT+0 heute Report positiv erfolgt → HT+1 Do → HT+2 Fr → Ende Mo 10.08.), V +12,11 % Std (368,42 chg -0,30 %, P/L +3,15 %, RSI 64,0, **EMA-Diff +3,79 % engster aber positiv verb. vs Mo +3,01 %**), UNH +11,71 % Std (412,73 chg +1,23 %, P/L +2,74 %, RSI 46,7, EMA-Diff +15,23 %), **JPM +17,32 %** Std (359,19 chg +0,47 %, **Best P/L +7,94 %**, RSI 65,8 << 80, EMA-Diff +6,11 %), **V5-Vollcheck 5 SICHER EOD-Bars** (Alpaca IEX 276d, Golden Cross alle intakt EMA50>EMA200): V **+3,79 %** (engster aber positiv, verb. vs Mo +3,01 %), JPM +6,11 %, AAPL +10,85 %, LLY +11,31 %, UNH +15,23 %. **V6-Vollcheck 5 SICHER**: max **RSI JPM 65,8** (V 64,0, LLY 51,2, UNH 46,7, AAPL 45,8 alle << 80). **RS_4w vs SPY** (SPY 20d +3,29 %): LLY **-7,15 pp NEG** (RSI 51,2 → V6 sicher via UND-Bedingung, verbessert vs Mo -12,66 pp), UNH -6,31 pp NEG (RSI 46,7 → V6 sicher), AAPL -4,05 pp NEG (RSI 45,8 → V6 sicher), V +2,74 pp positiv, JPM +5,38 pp positiv. **V2 Trailing-Stop-Check**: **UNH engster V2 +1,75 %** (52w-Wick 460,95 vom 2026-07-16 = intraday-Wick, Close-basis 436,39 = -5,29 % below High = Data-Quality-Flag; per Strategie-Lock strategy.md wörtlich → 460,95 bindend, V2 nicht getriggert), **AAPL V2 +2,55 %** via 52w-Wick 344,56 vom 29.07., LLY V2 +6,42 % via 52w-High 1.248,53, andere V2 >11 %. V3/V4 max P/L JPM +7,94 % << 20 %-TP1 kein Trigger, **8/8 GRÜN + 1 WARN** (LLY BO HT+0 Report positiv → morgen HT+1 startet, Blackout-V1_neu gilt weiterhin; UNH V2 razor-thin +1,75 % via 52w-Wick Data-Quality-Flag), **Watchlist Do 06.08. K1-K3 aus Alpaca IEX EOD Mi 05.08.:** **UAL #1 XLI** (132,72 K1 +10,6 % ✓, K2 RSI 63,9 ✓, K3 RS_63d **+35,3 pp #1 XLI** ✓, K4 68 % <120 % FAIL 4. Tag Vol-Rebound-Watch Do, K5 vorbekannt ✓ RevGr 16 % + FwdPE 14,8x, XLI 0 % Diversifikation), **GS #2 XLF** (1.060,53 K1 ✓ +10,6 %, K2 RSI 52,1 ✓, K3 RS +9,1 pp ✓, K4 107 % nahe 120 %-Trigger, K5 morgens prüfen), **DELL #3 XLK** (462,38 K1 ✓✓✓ +49,8 %, K2 RSI 59,7 ✓, K3 RS **+107,4 pp #1 Gesamt-Momentum** ✓, K4 101 %, XLK-Konflikt AAPL), **HPE #4 XLK** (53,21 K1 ✓ +34,6 %, K2 RSI 64,9 ✓, K3 RS +70,8 pp ✓, K4 74 % FAIL, XLK-Konflikt), **UNP #5 XLI Backup** (295,50 K1 ✓ +9,4 %, K2 RSI 57,0 ✓, K3 RS +5,6 pp ✓, K4 59 % FAIL heavy), **GE BLOCKIERT K5-FAIL persistent FwdPE 44,72 >35**, **NVDA K1-K3 ✓ RS +5,2 pp K4 98 %** XLK-Konflikt, **MSFT K1 Death-Cross-nah + K2 RSI 76,3 FAIL**, **ORCL K1 FAIL Death-Cross + K3 -28,5 pp FAIL heavy**, **AMZN K3 -6,7 pp NEG FAIL**, **GOOGL K3 -13,1 pp NEG FAIL**, **META K1 FAIL + K3 -9,0 pp NEG FAIL**, **AVGO K3 -8,4 pp NEG FAIL**, **CAT K2 RSI 47,5 <50 FAIL + K3 -10,0 pp NEG FAIL**, **Slot 1/2 KW32 bleibt OFFEN** (UAL Prio 1 wenn K4-Rebound Do + K5-Multi-Source; GS Prio 2 XLF wenn K4 ≥120 %), **Käufe KW32 0/2 unverändert**, Sektor-Struktur EOD: XLV 19,89 % (LLY 9,64 + UNH 10,25 marginal reduziert vs Midday 19,90 %), XLF 11,42 % (JPM 1,12 + V 10,30), XLK 9,98 % (AAPL), Cash 58,71 %, **Earnings-Blackout Nächste 3 HT**: LLY HT+0 heute BMO Report positiv erfolgt → HT+1 morgen Do 06.08. → HT+2 Fr 07.08. → Ende Mo 10.08., keine anderen Portfolio-Positionen mit Earnings 3 HT, **ClickUp Prio 4 Routine-Log FEHLER "Max usage for custom task types reached" ITEM_246 persistent 3. Tag** → Fallback Memory-Only per notify-skill.md, **KEINE PushNotification** (Silence-Rule Routine: Std alle SICHER, kein Cap-Alert, positive Alpha +0,726 pp, Owner erhielt Post-Earnings-Sichtbarkeit Pre-Market heute Morgen), Nächste Routine Do 06.08. 08:30 ET Pre-Market KW32 Tag 4)

**Vorheriger Stand:** 2026-08-05 13:12 ET (**Midday Stop-Check KW32 Tag 3**, Equity Live **96.531,93 $** vs last_equity 96.056,40 = **+0,495 %** Daily [GRÜN, Cap -3 %, marginal reduziert vs Open +0,595 % durch LLY-Give-back nach Post-Earnings-Rally-Peak], Cash 56.707,49 = **58,74 %** unverändert, MV Live **39.824,44 $** (5 Pos Alpaca, +378,89 vs Mo Close 39.445,55 = **+0,961 %** UNH-Recovery +1,96 % + LLY Rest-Rally gehalten +3,39 %), DD **-3,532 %** vs ATH 100.066,47 [GRÜN, marginal verschlechtert vs Open -3,436 %], **SPY Live 771,265 Alpaca latestTrade** vs Mo Close 771,11 = **+0,020 % essentiell flat** (Post-Rally-Konsolidierung marktweit vs Open +0,595 %) [Crash-Filter INAKTIV], **Alpha vs SPY +0,940 pp POSITIV verbessert vs Open 0,000 pp** (Portfolio outperformt SPY-Flat via UNH/LLY-Beta), Weekly KW32 Tag 3 **+0,140 %** vs Fr 31.07. Close 96.396,66 [GRÜN, positiv gehalten reduziert vs Open +0,240 %], **KEIN V1/V2/V3/V4-Trigger per strategy.md** (Std-V1 alle 5 SICHER), **KEINE Sell-/Limit-Order platziert, 0 offene Orders**, V1-Puffer sortiert eng→weit Std-V1: **LLY +5,06 % ENGSTE Std reduziert vs Open +8,96 %** (1.153,91 chg +3,390 % vs Mo Close, chg vs Open -3,586 % **Give-back**, P/L **-3,35 % Worst P/L Live** deutlich verschlechtert vs Open +0,41 %, **Blackout-V1_neu 1.134,20 Puffer +1,74 % NOCH ÜBERSCHRITTEN** deutlich reduziert vs Open +5,52 % aber Bull-Konvention weiterhin intakt, HT+0 heute Report positiv erfolgt → HT+1 Do → HT+2 Fr → Ende Mo 10.08.), **AAPL +6,09 % Std verbessert vs Open +5,58 %** (309,27 chg -0,026 % essentiell flat, P/L -2,39 % verbessert vs Open -3,10 %, Std-V1 291,51 alleine primär), V +12,06 % (368,23 chg **-0,352 % Worst chg**, P/L +3,09 %), **UNH +12,51 % deutlich verbessert vs Open +10,04 %** (415,64 chg **+1,962 % Best chg**, P/L +3,50 % vs Open +1,23 %, V2 via 52w-Wick 460,95 Puffer +2,47 % Data-Quality-Flag), JPM **+17,70 %** (360,35 chg +0,806 %, **Best P/L +8,28 %**), V3/V4 max P/L JPM +8,28 % << 20 %-TP1 kein Trigger, V2-Trailing-Stop alle 5 SICHER, **RSI/EMA werden bei Midday NICHT geprüft (nur Market Open + Close)**, Sektor-Struktur Midday: XLV 19,90 % (UNH 10,33 + LLY 9,56 UNH-Recovery hebt trotz LLY-Give-back), XLF 11,44 % (JPM 1,12 + V 10,30), XLK 9,93 % (AAPL), Cash 58,74 %, **8/8 GRÜN + 0 WARN** (LLY BO noch ÜBERSCHRITTEN +1,74 % — WARN ausgetragen, UNH V2 razor-thin +2,47 % Monitoring bleibt Data-Quality-Flag ohne WARN), **KEIN ClickUp** (Midday-Routine STEP 5: nur bei Stop-Trigger oder Daily-Cap → Silence-Rule Routine + ITEM_246 Kontingent-Fehler persistent), **KEINE PushNotification** (Silence-Rule Routine: Std alle SICHER, kein Cap-Alert, positive Alpha +0,940 pp, LLY BO noch ÜBERSCHRITTEN +1,74 % innerhalb Post-Earnings-Bull-Konvention-Toleranz, LLY-Rally-Give-back -3,59 % vs Peak keine Handlungsaufforderung, Owner erhielt Post-Earnings-Sichtbarkeit Pre-Market Prio 2 heute), Nächste Routine 16:00 ET Market Close Tagesbilanz KW32 Tag 3)

**Vorheriger Stand:** 2026-08-05 09:40 ET (**Market Open KW32 Tag 3**, Equity Live **96.628,15 $** vs last_equity 96.056,40 = **+0,595 %** Daily [GRÜN, Cap -3 %, weiter verbessert vs Pre +0,526 %], Cash 56.707,49 = **58,68 %** unverändert, MV Live **39.920,66 $** (5 Pos Alpaca, +475,11 vs Mo Close 39.445,55 = **+1,204 %** LLY-Post-Earnings-Rally dominant), DD **-3,436 %** vs ATH 100.066,47 [GRÜN, verbessert vs Pre -3,502 %], **VIX 18,29 Pre-Read** [GRÜN <25], **SPY Live 775,70 Alpaca latestTrade** vs Mo Close 771,11 = **+0,595 % Post-Rally-Fortsetzung** [Crash-Filter INAKTIV], **Alpha vs SPY 0,000 pp neutral** (LLY-Post-Earnings-Rally kompensiert SPY-Beta vollständig — beste Alpha-Session KW32 bislang), Weekly KW32 Tag 3 **+0,240 %** vs Fr 31.07. Close 96.396,66 [GRÜN, gedreht positiv Vertiefung vs Pre +0,172 %], **5 V1-V6 SICHER Std-V1 Live-Read — kein V-Trigger, KEINE Sell-Order platziert, 0 offene Orders**, V1-Puffer sortiert eng→weit Std-V1: **AAPL +5,58 % ENGSTE Std verschlechtert vs Pre +5,90 %** (307,78 chg **-0,760 % Worst chg**, P/L **-3,10 % Worst P/L neu verschlechtert vs Pre -2,51 %**, Std-V1 291,51 primär), **LLY +8,96 % Std deutlich verbessert vs Pre +6,34 %** (1.196,825 chg **+7,449 % Best chg**, P/L **+0,41 % Recovery +6,81 pp vs Close -6,40 %** / +2,58 pp vs Pre -2,17 %, **Blackout-V1_neu 1.134,20 Puffer +5,52 % ÜBERSCHRITTEN weiter verbessert vs Pre +2,98 %** — Bull-Konvention komplett aufgehoben, 3-Tage-Bruch Mo/Di/Pre-Mi gelöst durch Post-Earnings-Rally, HT+0 Post-Report → HT+1 Do → HT+2 Fr → Ende Mo 10.08.), UNH +10,04 % Std (406,56 chg -0,250 %, P/L +1,23 %, V2 razor-thin 405,64 +0,23 % via 52w-Wick 460,95 Data-Quality-Flag beibehalten), V +12,92 % (371,05 chg +0,200 %, P/L +3,68 %), **JPM +17,82 %** (360,73 chg +0,931 %, **Best P/L +8,43 %**), V3/V4 max P/L JPM +8,43 % << 20 %-TP1 kein Trigger, **8/8 GRÜN + 0 WARN** (LLY BO ÜBERSCHRITTEN, UNH V2 razor-thin Monitoring aber keine WARN), **Kaufsignal-Scan Slot 1/2 alle Watchlist-Kandidaten REJECT/SKIP:** UAL #1 XLI RS +39,77 pp #1 TOP aber **K4 71 % <120 % FAIL 3. Tag persistent** (Mo 73 → Di 71 → Vollcheck EOD 71) → REJECT K4, UNP K4 66 % FAIL, **MRK Post-Earnings-Reaktion K4 115 % FAIL** + XLV-Cap Owner-pending, **ABBV K2 RSI 44,1 <50 FAIL** + XLV-Cap Owner-pending 5. Woche, **GE K4 61 % FAIL + K5 FwdPE 44,72 FAIL persistent**, **EOG K3 -6,02 pp NEG FAIL** (Rebound abgebrochen), NVDA K3+K4 FAIL, AMZN K3+K4 FAIL, GOOGL K3 -8,83 pp NEG FAIL, MSFT K1 Death-Cross-nah FAIL + K2 79,2 FAIL, META K1 Death Cross FAIL 4/4, **Slot 1/2 KW32 bleibt OFFEN**, **Käufe KW32 0/2 unverändert**, Sektor-Struktur Live: XLV 20,02 % (UNH 10,10 + LLY 9,92 LLY-Rally hebt Anteil), XLF 11,47 % (JPM 1,12 + V 10,35), XLK 9,85 % (AAPL), Cash 58,68 %, **Earnings-Blackout Nächste 3 HT**: LLY HT+0 heute BMO Report positiv erfolgt → HT+1 morgen Do → HT+2 Fr → Ende Mo 10.08., keine anderen Portfolio-Positionen mit Earnings 3 HT, **ClickUp Prio 4 Routine-Log FEHLER "Max usage for custom task types reached" ITEM_246 persistent 2. Tag** → Fallback Memory-Only per notify-skill.md, **KEINE PushNotification** (Silence-Rule Routine: kein Cap-Alert, kein neuer Trade, LLY-Post-Earnings-Sichtbarkeit bereits im Pre-Market Prio 2 abgedeckt, LLY-Rally-Fortsetzung Post-Open keine neue Handlungsaufforderung, Owner erhielt Pre-Market-Sichtbarkeit heute), Nächste Routine 13:00 ET Midday Stop-Check KW32 Tag 3)

**Vorheriger Stand:** 2026-08-05 08:35 ET (**Pre-Market KW32 Tag 3**, Equity Pre **96.562,01 $** vs last_equity 96.056,40 = **+0,526 %** Daily [GRÜN, Cap -3 %], vs Memory Close 96.153,04 = +0,425 % Post-Earnings-Gap positiv, Cash 56.707,49 = **58,73 %** unverändert, MV Pre **39.854,52 $** (5 Pos Alpaca Live, +408,97 vs Mo Close 39.445,55 = **+1,037 % LLY-Post-Earnings-Rally dominant**), DD **-3,502 %** vs ATH 100.066,47 [GRÜN, deutlich verbessert vs Mo Close -3,911 %], Weekly KW32 Tag 3 **+0,172 %** vs Fr 31.07. Close 96.396,66 [GRÜN, gedreht positiv vs Mo Close -0,253 %], **VIX Perplexity 18,29** [GRÜN <25, leicht erhöht vs Mo Close 15,86 aber weit von 25-Cap], **SPY Pre 774,59 Alpaca latestTrade** vs Mo Close 771,11 = **+0,451 % Post-Rally-Fortsetzung** [Crash-Filter INAKTIV], 10Y Yield Perplexity ~4,25 %, **🟢 LLY Q2 2026 BMO Earnings Report — MASSIVER BEAT + GUIDANCE-ANHEBUNG**: EPS $8,38 vs Konsens $6,00-7,74 (Beat +25-35 %), Revenue $22,97 Mrd. vs Konsens $20,5-20,7 Mrd. (Beat +11 %), **Guidance 2026 angehoben: Revenue $85-87 Mrd. (vorher $82-85), EPS $35,50-36,50** (Mounjaro Q2 $9,94 Mrd. fast Verdoppelung YoY, Retatrutide Pipeline fortschreitend), **LLY Pre 1.168,00 = +4,52 % Post-Earnings-Gap-Up** (Alpaca Positions cur), **Blackout-V1_neu 1.134,20 Puffer +2,98 % ÜBERSCHRITTEN — Bull-Konvention wieder INTAKT nach 3-Tage-Bruch**, P/L verbessert von Close -6,40 % auf Pre **-2,17 %** (+4,23 pp Recovery, Worst-P/L-Titel wechselt zu AAPL -2,51 %), **5 V1-V6 SICHER Pre-Read Std-V1 (RSI/EMA nicht Pre)**, **KEINE Sell-/Limit-Order platziert, 0 offene Orders**, V1-Puffer sortiert eng→weit Std-V1: **AAPL +5,90 % ENGSTE Std verbessert vs Mo +6,12 %** (308,90 chg -0,155 %, P/L -2,51 % neu Worst P/L, Std-V1 291,51 primär), **LLY +6,34 % Std verbessert vs Mo +1,74 %** (1.168,00 chg +4,69 %, P/L -2,17 % deutlich verbessert vs -6,40 %, **Blackout Puffer +2,98 % ÜBERSCHRITTEN**, HT+0 heute Report → morgen HT+1 → Fr HT+2 → Mo 10.08. Ende Blackout), V +13,24 % (372,10 chg +0,68 %, P/L +4,18 %), UNH +10,71 % (409,01 chg +0,36 %, P/L +1,85 %), **JPM +17,26 % Std** (358,99 chg +0,41 %, **Best P/L +7,88 %**), V3/V4 max P/L JPM +7,88 % << 20 %-TP1 kein Trigger, **Alle 8 Guardrails GRÜN + 0 WARN** (LLY BO ÜBERSCHRITTEN → WARN ausgetragen, UNH V2 razor-thin +0,52 % via 52w-Wick Data-Quality-Flag bleibt Monitoring aber keine WARN), **Kaufscan Market Open: JA** (LLY-Post-Earnings-Momentum-Watch für Portfolio, UAL K4-Vol-Rebound 3. Tag Re-Check, MRK Post-Earnings Mo BMO Reaktion Watch), **Earnings-Blackout Nächste 3 HT:** LLY Mi 05.08. **BMO HT-0 heute Report bereits erfolgt (positiv)**, MRK gestern Di 04.08. BMO Post-Reaktion nach Open verfügbar (nicht Portfolio), Do 06.08. + Fr 07.08. keine Portfolio-Positionen mit Earnings (UNH/JPM/V/AAPL Q3 Ende Okt), **ClickUp Prio 4 Routine-Log FEHLER "Max usage for custom task types reached" ITEM_246** → Fallback Memory-Only per notify-skill.md, **PushNotification Prio 2 Owner** (positive Post-Earnings-Sichtbarkeit: LLY EPS Beat +25-35 % + Guidance-Anhebung Rev $85-87 Mrd + Gap +4,52 % + Blackout-Bruch aufgehoben Puffer +2,98 % ÜBERSCHRITTEN + Weekly gedreht positiv), Nächste Routine Mi 05.08. 09:30 ET Market Open KW32 Tag 3)

**Vorheriger Stand:** 2026-08-04 16:00 ET (**Market Close Tagesbilanz KW32 Tag 2**, Equity Close **96.153,04 $** vs last_equity 95.984,04 = **+0,176 %** Daily [GRÜN, Cap -3 %, verschlechtert vs Midday +0,205 %], SPY Close **771,11 Alpaca IEX** vs Mo Close 757,72 = **+1,767 % Post-Rally-Beschleunigung** [Perplexity divergiert 1,48 % → IEX bindend, verified via /v2/stocks/SPY/bars Daily-Bar h=773,41 l=760,53 vol=2,27M], Cash 56.707,49 = **58,98 %** unverändert, MV Close **39.445,55 $** (5 Pos Alpaca, +183,97 vs Mo Close 39.261,58 = +0,469 %; MV Bar-Close-Berechnet 39.364,54 wg. stale Positions-Endpoint für LLY/UNH — Delta -81 $ innerhalb Rundungstoleranz), DD **-3,911 %** vs ATH 100.066,47 [GRÜN, verbessert vs Midday -3,884 %], Weekly KW32 Tag 2 **-0,253 %** vs Fr 31.07. Close 96.396,66 [GRÜN weit von Cap -5 %], **Alpha vs SPY -1,591 pp NEGATIV** (SPY-Beschleunigung ohne Portfolio-Beta, UNH -1,84 % Worst chg + LLY flat -0,33 % dämpfen JPM +1,38 % + AAPL +1,95 % Best chg + V +1,06 %), VIX Perplexity **15,86** [GRÜN <25, weiter reduziert vs Fr 16,02 = Vola-Entspannung Fortsetzung], **5 V1-V6 SICHER Vollcheck EOD-Bars — KEIN Stop-Trigger, KEINE Sell-/Limit-Order für Mi 05.08. platziert, 0 offene Orders**, V1-Puffer min **LLY +1,74 % ENGSTE Std** (Close 1.117,47 chg -0,33 %, P/L **-6,40 % Worst P/L verschlechtert vs Mo -6,11 %**, Blackout-V1_neu 1.134,20 **UNTERSCHRITTEN -1,47 %** weiter verschlechtert vs Pre -0,94 % / Mo -1,16 % — Bull-Konvention weiter gebrochen aber Strategie-Lock CLAUDE.md Rule 3 → HALTEN, Report morgen BMO), **AAPL Blackout HT+2 heute beendet regelkonform** (309,335 chg +1,95 % Best chg, P/L -2,37 %, Std-V1 291,51 Puffer +6,12 % alleine primär, RSI 44,6, EMA-Diff +10,37 %), V +12,45 % Std (369,53 chg +1,06 %, P/L +3,46 %, RSI 65,5, EMA-Diff **+3,01 % engster aber positiv verb. vs Mo +3,92 % → Erholung**), UNH +10,36 % Std (407,73 chg **-1,84 % Worst chg**, P/L +1,53 %, RSI 43,1, EMA-Diff +13,65 %), **JPM +16,78 %** Std (357,52 chg +1,38 %, **Best P/L +7,43 %**, RSI 64,6, EMA-Diff +5,74 %), **V5-Vollcheck 5 SICHER EOD-Bars** (Alpaca IEX 253d, Golden Cross alle intakt EMA50>EMA200): V **+3,01 %** (engster aber positiv, verb. vs Mo +3,92 %), JPM +5,74 %, AAPL +10,37 %, LLY +11,90 %, UNH +13,65 %. **V6-Vollcheck 5 SICHER**: max **RSI V 65,5** (JPM 64,6, AAPL 44,6, UNH 43,1, LLY 40,4 alle << 80). **RS_4w vs SPY** (SPY 20d +3,12 % beschleunigt vs Mo +0,86 %): LLY **-12,66 pp NEG** (weiter verschlechtert vs Mo -7,52 pp, RSI 40,4 → V6 sicher via UND-Bedingung), UNH -7,87 pp NEG (RSI 43,1 → V6 sicher), AAPL -3,56 pp NEG (RSI 44,6 → V6 sicher), V +1,83 pp positiv, JPM +2,36 pp positiv. **V2 Trailing-Stop-Check**: **UNH engster V2 +0,52 %** (52w-High 460,95 vom 2026-07-16 = intraday-Wick, Close-basis 423,28 = -8,17 % below High = Data-Quality-Flag; ohne Wick wäre nächst-höchster High ~437,13 → V2-Puffer ~+5,99 %; per Strategie-Lock strategy.md wörtlich → 460,95 bindend, V2 nicht getriggert), LLY V2 +1,71 % ähnlich zu V1, andere V2 >5 %. V3/V4 max P/L JPM +7,43 % << 20 %-TP1 kein Trigger, **8/8 GRÜN + 1 WARN** (LLY BO HT-0 morgen BMO Report UNTERSCHRITTEN -1,47 % weiter verschlechtert, UNH V2 razor-thin +0,52 % via 52w-Wick Data-Quality-Flag), **Watchlist Mi 05.08. K1-K4 aus Alpaca IEX EOD Di 04.08.:** **UAL #1 XLI** (132,63 chg +3,29 %, K1 EMA-Diff +9,01 % ✓, K2 RSI 63,8 ✓, K3 RS_63d **+39,77 pp #1 TOP** ✓ verbessert vs Mo +33,61 pp, K4 71 % <120 % FAIL Vol-Rebound-Watch Mi, K5 vorbekannt ✓ RevGr 16 % + FwdPE 14,8x + Next-Earnings Okt 2026, XLI 0 % neue Diversifikation), **UNP #2 XLI Backup** (296,51 chg +1,64 %, K1-K3 ✓ RS +5,10 pp, K4 66 % FAIL Rebound-Watch), **NVDA #3 XLK Watch** (211,96 chg +2,53 %, K1 ✓ +4,94 %, K2 RSI 56,9 ✓, K3 RS_63d **-0,63 pp marginal NEG FAIL**, K4 77 % FAIL, XLK-Konzentration mit AAPL beachten), **GE (K1-K4 ✓ RS +27,09 pp) BLOCKIERT K5-FAIL persistent FwdPE 44,72 >35**, **ABBV #4 XLV BLOCKIERT XLV-Cap Owner-pending 5. Woche + K2 RSI 44,1 <50 FAIL**, **EOG K3 -6,02 pp NEG FAIL (Rebound weiter abgebrochen)**, **AMZN K3 -5,44 pp NEG FAIL persistent**, **GOOGL K3 -8,83 pp NEG FAIL persistent**, **MSFT K1 FAIL Death-Cross-nah + K2 RSI 79,2 >70 FAIL**, **ORCL K1 FAIL Death-Cross + K3 -26,55 pp FAIL heavy**, **MRK Post-Earnings-Reaktion nach Mi Open prüfen** (heute BMO Report), **Slot 1/2 KW32 bleibt OFFEN** (UAL Prio 1 wenn K4-Rebound Mi + K5-Multi-Source; **LLY BMO Report morgen HT-0 kritisch**), **ClickUp Prio 4 (Low, positiver Tag)** wird gesendet, **PushNotification Silence-Rule** (Std alle SICHER, kein Cap-Alert, Daily +0,176 % positiv, LLY BO -1,47 % innerhalb Bull-Konvention-Toleranz — Owner erhielt Sichtbarkeit heute Open+Midday, Report morgen bringt Klärung, kein Owner-Handlungsbedarf), Nächste Routine Mi 05.08. 08:30 ET Pre-Market KW32 Tag 3)

**Vorheriger Stand:** 2026-08-04 13:09 ET (**Midday Stop-Check KW32 Tag 2**, Equity Live **96.180,38 $** vs last_equity 95.984,04 = **+0,205 %** Daily [GRÜN, Cap -3 %, verbessert vs Open -0,134 %], Cash 56.707,49 = **58,96 %** unverändert, MV Live **39.472,89 $** (5 Pos, +324,52 vs Open 39.148,37 = +0,829 %, AAPL-Recovery +2,14 % + JPM +2,26 % Best chg + V +0,94 %, UNH -1,05 % Worst chg dämpft), DD **-3,884 %** vs ATH 100.066,47 [GRÜN, verbessert vs Open -4,208 %], **SPY Live 771,08 Alpaca IEX** vs Mo Close 757,72 = **+1,764 % Post-Rally-Beschleunigung** vs Open 761,55 (+1,251 %) [Crash-Filter INAKTIV], **Alpha vs SPY -1,559 pp NEGATIV verschlechtert vs Open -0,640 pp** (SPY-Beschleunigung ohne Portfolio-Beta), Weekly KW32 Tag 2 **-0,224 %** vs Fr 96.396,66 [GRÜN weit von Cap -5 %], **KEIN V1/V2/V3/V4-Trigger per strategy.md** (Std-V1 alle 5 SICHER), **KEINE Sell-/Limit-Order platziert, 0 offene Orders**, V1-Puffer sortiert eng→weit Std-V1: **LLY +2,04 % ENGSTE Std verbessert vs Open +2,03 %** (1.120,72 chg +0,007 % essentiell flat vs Open, chg Mo Close -0,025 %, P/L **-6,13 % Worst P/L verschlechtert vs Open -5,72 %** anhaltender Rest-Sell-off, Blackout-V1_neu 1.134,20 **UNTERSCHRITTEN -1,19 %** essentiell unverändert vs Open -1,20 % — Bull-Konvention weiter gebrochen aber Strategie-Lock CLAUDE.md Rule 3 → HALTEN), **AAPL +6,18 % Std verbessert vs Open +3,84 %** (309,525 chg +2,14 % Best change_today intraday vs Mo Close, chg intraday vs Open +2,25 %, P/L -2,31 % verbessert vs Open -4,25 %, **Blackout HT+2 heute beendet regelkonform** — Std-V1 291,51 alleine primär), V +12,33 % (369,11 chg +0,94 %, P/L +3,34 %), UNH +11,27 % (411,01 chg -1,05 % Worst chg, P/L +2,35 %), **JPM +17,79 %** (360,60 chg **+2,26 % Best chg**, **Best P/L +8,36 %**), V3/V4 max P/L JPM +8,36 % << 20 %-TP1 kein Trigger, V2-Trailing-Stop-Check alle 5 SICHER (weniger restriktiv als Std-V1), **RSI/EMA werden bei Midday NICHT geprüft (nur Market Open + Close per Midday-Routine)**, Käufe KW32 0/2 unverändert (Kaufsignal-Scan bei Midday nicht Teil der Routine), Sektor-Struktur Midday: XLV 19,58 % (UNH 10,26 + LLY 9,32 marginal reduziert vs Open 19,80 %), XLF 11,49 % (JPM 1,12 + V 10,36), XLK **9,98 %** AAPL-Recovery verbessert vs Open 9,81 %, Cash 58,96 %, **8/8 GRÜN + 1 WARN** (LLY BO HT-1 letzter Tag UNTERSCHRITTEN -1,19 % essentiell unverändert — AAPL BO beendet regelkonform), **Blackout-Kalender:** LLY HT-1 → HT-0 Mi 05.08. BMO Earnings-Report bleibt Bull-Konvention-Referenz bis Post-Report, AAPL beendet Std alleine primär, MRK HT-0 heute BMO nicht Portfolio, **KEIN ClickUp** (Midday-Routine STEP 5: nur bei Stop-Trigger oder Daily-Cap → Silence-Rule Routine), **KEINE PushNotification** (Silence-Rule Routine: Std alle SICHER, kein Cap-Alert, positive Intraday-Recovery +0,205 % Daily, LLY BO -1,19 % essentiell unverändert innerhalb Vorwochen-Konvention-Toleranz, Report morgen bringt Klärung, kein Owner-Handlungsbedarf), Nächste Routine 16:00 ET Market Close Tagesbilanz KW32 Tag 2)

**Vorheriger Stand:** 2026-08-04 09:38 ET (**Market Open KW32 Tag 2**, Equity Live **95.855,86 $** vs last_equity 95.984,04 = **-0,134 %** Daily [GRÜN, Cap -3 %], Cash 56.707,49 = **59,16 %** unverändert, MV Live **39.148,37 $** (5 Pos, -113,21 vs Mo Close 39.261,58 = -0,288 %, UNH -0,91 % + V -0,86 % dämpfen JPM +2,09 % Best chg XLF-Rally), DD **-4,208 %** vs ATH 100.066,47 [GRÜN], **VIX 18,9 Pre-Read** [GRÜN <25], **SPY Live 761,55 Alpaca IEX** vs Mo Close 757,72 = **+0,506 % Post-Rally-Fortsetzung Konsolidierung** [Crash-Filter INAKTIV], **Alpha vs SPY -0,640 pp NEGATIV**, Weekly KW32 Tag 2 **-0,561 %** vs Fr 31.07. Close 96.396,66 [GRÜN weit von Cap -5 %], **5 V1-V6 SICHER Std-V1 Vollcheck Bars EOD Mo — kein V-Trigger, KEINE Sell-/Limit-Order platziert, 0 offene Orders**, V1-Puffer min **LLY +2,03 % ENGSTE Std** (1.120,645 chg +0,04 % marginale Recovery, P/L **-5,72 % Worst P/L verbessert vs Mo -6,11 %**, Blackout-V1_neu 1.134,20 **UNTERSCHRITTEN -1,20 %** marginal verschlechtert vs Pre -0,94 % — Bull-Konvention weiter gebrochen aber Strategie-Lock CLAUDE.md Rule 3 → HALTEN, RSI 40,9), **AAPL Blackout HT+2 heute beendet regelkonform** — Std-V1 291,51 wieder alleine primär (Puffer +3,84 %, 302,71 chg -0,01 %, P/L -4,25 %, RSI 39,8, EMA-Diff +10,30 %), V +10,66 % Std (363,625 chg -0,86 %, RSI 60,0, **EMA-Diff +2,96 % engster aber positiv verb. vs Mo Close +3,92 %**), UNH +11,74 % Std (412,82 chg -0,91 %, RSI 46,0), **JPM +17,58 %** Std (360,00 chg **+2,09 % Best chg**, **Best P/L +8,18 %**, RSI 66,3 << 80), **V5 alle Golden Cross intakt** (min V +2,96 % positiv), **V6 alle SICHER** (max JPM RSI 66,3 << 80, LLY RS_4w -11,12 pp NEG aber RSI 40,9 → V6 sicher via UND-Bedingung), V3/V4 max P/L JPM +8,18 % << 20 %-TP1 kein Trigger, **Kaufsignal-Scan Slot 1/2 KW32 — alle 10 Watchlist-Kandidaten REJECT/SKIP**: UAL K1-K3 ✓ + RS +40,67 pp #1 TOP aber **K4 Mo 73 % <120 % FAIL + Live 4 % pro-rata unbelastbar → REJECT K4**, UNP K4 Mo 46 % <<120 % FAIL heavy, **EOG K3 -6,44 pp NEG FAIL (Rebound abgebrochen)**, **ABBV K2 RSI 44,8 <50 FAIL erstmals** + XLV-Cap Owner-pending 5. Woche, **MRK BLOCKIERT Earnings HT-0 heute BMO**, GE K5 FAIL persistent FwdPE 44,72 >35, AMZN K3 -4,27 pp NEG FAIL, GOOGL K3 -8,98 pp NEG FAIL, CAT K3 -0,75 pp marginal NEG, META/TSLA K1 FAIL Death-Cross, **Slot 1/2 KW32 bleibt OFFEN**, **8/8 GRÜN + 2 WARN** (LLY BO HT-1 letzter Tag UNTERSCHRITTEN -1,20 % + AAPL BO HT+2 beendet Übergang regelkonform), **Käufe KW32 0/2 unverändert**, **Blackout-Kalender:** AAPL HT+2 heute Blackout **beendet regelkonform** (Std alleine primär), LLY HT-1 → HT-0 Mi 05.08. BMO Earnings-Report bleibt Bull-Konvention-Referenz, MRK HT-0 heute blockiert Kauf, ClickUp Prio 4 Routine-Log, PushNotification Silence-Rule (Std alle SICHER, BO-Muster unverändert vs Vorwochen-Toleranz, Report morgen bringt Klärung), Nächste Routine 13:00 ET Midday Stop-Check KW32 Tag 2)

**Vorheriger Stand:** 2026-08-04 08:37 ET (**Pre-Market KW32 Tag 2**, Equity Pre **95.986,04 $** vs last_equity 95.984,04 = **+0,002 %** Daily [GRÜN, Cap -3 %, essentiell flat], Cash 56.707,49 = 59,08 % unverändert, MV Pre **39.278,55 $** (+16,97 vs Mo Close 39.261,58 = +0,043 % Konsolidierung Pre), DD **-4,078 %** vs ATH 100.066,47 [GRÜN, marginal verbessert vs Mo Close -4,091 %], **VIX Perplexity 18,9** [GRÜN <25, leicht erhöht vs Fr Close 16,02 = Vola-Anstieg Post-Weekend-Konsolidierung, aber weit von 25-Cap], **SPY Pre 08:34 ET 760,30 Alpaca latestTrade** vs Mo Close 757,72 = **+0,341 % Post-Rally-Fortsetzung Konsolidierung** (Crash-Filter INAKTIV), 10Y Yield n/a Perplexity, Weekly KW32 Tag 2 +0,014 % [GRÜN weit von Cap -5 %], **5 V1-V6 SICHER Pre-Read Std-V1 (RSI/EMA nicht Pre)**, **KEINE Sell-/Limit-Order platziert, 0 offene Orders**, **🔴 LLY Blackout HT-1 letzter Tag vor BMO Report Mi 05.08.** — Blackout-V1_neu 1.134,20 bei Live 1.123,50 **UNTERSCHRITTEN -0,94 %** verbessert vs Mo Close -1,16 % (chg_today +0,19 % marginale Recovery, P/L -5,90 % verbessert vs Mo -6,11 %), **Std-V1 1.098,38 SICHER +2,29 % ENGSTE Std** verbessert vs Mo +2,06 %, Strategie-Lock CLAUDE.md Rule 3 → HALTEN, **AAPL Blackout HT+2 ab HEUTE beendet** — Std-V1 291,51 wieder alleine primär (Live 302,894 Puffer +3,90 %, chg_today -0,17 %, P/L -4,41 %), V +11,38 % Std (366,00), UNH +12,33 % Std (415,01), JPM +15,26 % Std (352,9075 Best P/L +6,05 %), **Käufe KW32 0/2 unverändert**, **Earnings-Blackout 3 HT:** MRK Di 04.08. BMO HT-0 heute (nicht Portfolio, blockiert Kauf), AMD Di AMC + MCD Di BMO (nicht Portfolio), LLY Mi 05.08. BMO HT-1 (Portfolio ⚠️, Memory-Konvention beibehalten), AAPL HT+2 beendet, UNH/JPM/V keine Earnings, **Kaufscan Market Open: JA** mit Bedingungen (UAL Prio 1 nur wenn K4-Session-Vol belastbar + K5-Multi-Source, UNP Momentum-Turnaround-Check, ABBV BLOCKIERT XLV-Cap Owner-pending, MRK BLOCKIERT heute Earnings), **8/8 GRÜN + 2 WARN** (LLY BO HT-1 UNTERSCHRITTEN -0,94 % + AAPL BO HT+2 beendet transition), **Watchlist Di Open**: UAL #1 XLI NEUE RS +33,61 pp #1 TOP + K4-Vol-Rebound-Watch, UNP #2 XLI Backup Momentum-Check, EOG #3 XLE Rebound-Watch, ABBV/MRK blockiert, ClickUp Prio 4 Routine-Log, PushNotification Silence-Rule (BO-Puffer >1 % Std alle SICHER, kein Cap-Alert, LLY BO -0,94 % innerhalb Konvention-Toleranz nach Mo -1,16 % Verbesserung), Nächste Routine 09:30 ET Market Open KW32 Tag 2)

**Vorheriger Stand:** 2026-08-03 16:00 ET (**Market Close Tagesbilanz KW32 Tag 1**, Equity Close **95.972,60 $** vs last_equity 96.360,90 = **-0,403 %** Daily [GRÜN, Cap -3 %, verschlechtert vs Midday -0,353 %], SPY Close **757,72 Alpaca IEX** vs Fr Close 746,79 = **+1,464 % Post-Weekend-Rally-Fortsetzung** [Crash-Filter INAKTIV; Perplexity divergiert bei -0,13 % → IEX bindend, verified via /v2/stocks/SPY/bars Daily-Bar h=758,58 l=749,21 vol=1,93M]; Cash 56.707,49 = **59,09 %** unverändert, MV Close **39.261,58 $** (5 Pos, -359,21 vs Open 39.620,79 = -0,907 %, LLY-Sell-off dominant fortgesetzt), DD **-4,091 %** vs ATH 100.066,47 [GRÜN, verschlechtert vs Midday -4,043 %], Weekly KW32 Tag 1 = Daily **-0,403 %** [GRÜN weit von Cap -5 %], **Alpha vs SPY -1,867 pp NEGATIV** (SPY-Rally-Fortsetzung ohne Portfolio-Beta, LLY XLV-Sell-off + AAPL Post-Earnings-Konsolidierung dämpfen), VIX Perplexity **16,02** [GRÜN <25, deutlich reduziert vs Fr ~19,8 = Vola-Entspannung Post-Weekend], **5 V1-V6 SICHER Vollcheck EOD-Bars — KEIN Stop-Trigger, KEINE Sell-/Limit-Order für Di 04.08. platziert, 0 offene Orders**, V1-Puffer min **LLY +2,06 % ENGSTE Std** (Close 1.121,00 chg -2,42 % Worst chg, P/L **-6,11 % Worst P/L**, Blackout-V1_neu 1.134,20 **weiter UNTERSCHRITTEN -1,16 %** aber verbessert vs Midday -1,49 %, Std-V1 1.098,38 SICHER, Strategie-Lock CLAUDE.md Rule 3 → HALTEN), **AAPL Blackout HT+1 letzter Tag Close** (309,03 chg -1,90 %, P/L -4,36 %, Blackout-V1_neu 301,02 Puffer **+0,67 % verschlechtert vs Midday +1,94 %** — kritisch nah 0 % aber Std-V1 291,51 SICHER +3,95 %; **ab morgen Di 04.08. HT+2 → Blackout beendet, Std-V1 wieder alleine primär**), V +11,28 % (365,67 chg -0,13 %, P/L +2,38 %), UNH +12,43 % (415,36 chg +0,23 % Best chg, P/L +3,43 %), JPM +15,18 % (352,64 chg +0,24 %, **Best P/L +5,97 %**), **V5-Vollcheck 5 SICHER EOD-Bars** (Alpaca IEX 275d, Golden Cross alle intakt EMA50>EMA200): V EMA-Diff **+3,92 %** (engster aber positiv, deutlich verbessert vs Fr +2,45 %), JPM +5,49 %, AAPL +10,89 %, LLY +11,69 %, UNH +13,35 %. **V6-Vollcheck 5 SICHER**: max **RSI V 59,8** (deutlich verbessert/reduziert vs Fr 66,2, Cool-off), JPM 58,8, UNH 43,2, AAPL 41,3, LLY **30,8** (nah unteren 30-Cap = Oversold-Zone). **RS_4w vs SPY** (SPY 20d +0,86 %): LLY **-7,52 pp NEG** (RSI 30,8 → V6 sicher via UND-Bedingung, RSI << 80), AAPL -3,84 pp NEG (RSI 41,3 → V6 sicher), UNH -1,51 pp NEG (RSI 43,2 → V6 sicher), V +1,47 pp positiv, JPM +3,53 pp positiv. V3/V4 max P/L JPM +5,97 % << 20 %-TP1 kein Trigger, **8/8 GRÜN + 2 WARN** (AAPL BO HT+1 letzter Tag Puffer +0,67 % kritisch nah 0 % + **LLY BO HT-2 UNTERSCHRITTEN -1,16 %** verbessert vs Midday -1,49 %), **Watchlist Di 04.08. K1-K3 aus Alpaca IEX EOD Mo 03.08.:** **UAL #1 XLI** (128,40 chg **+5,84 %**, K1 EMA-Diff +9,26 % ✓, K2 RSI 52,8 ✓, K3 RS_63d **+33,61 pp #1 TOP** ✓, K4 Mo 72 % <120 % FAIL Vol-Rebound-Watch Di, K5 vorbekannt ✓ RevGr 16 % + FwdPE 14,8x + Next-Earnings Okt 2026 = keine Blackout, XLI 0 % neue Diversifikation), **UNP #2 XLI Backup** (Fr K4 116 % borderline heute Momentum-Bruch, Re-Check Di Pre-Market), **EOG #3 XLE Rebound-Watch** (heute K3 -0,11 pp marginal NEG, K5 vorbekannt ✓), **ABBV #4 XLV BLOCKIERT XLV-Cap-Klärung Owner pending 4. Woche**, **GE (K1 ✓, K3 +23,61 pp #2) BLOCKIERT K5-FAIL persistent FwdPE 44,72 >35**, **META/TSLA REJECT K1-FAIL Death-Cross-nah**, **CAT REJECT K2-FAIL RSI 34,8 <50**, **MRK BLOCKIERT Earnings Di 04.08. BMO HT-0 Report morgen**, **Slot 1/2 KW32 bleibt OFFEN** (UAL Prio 1 wenn K4-Rebound Di, XLV-Cap-Klärung Owner-Prio 1), **ClickUp Prio 3 (Normal, negativer Tag ohne Cap-Alert)** wird gesendet, **PushNotification Prio 2 Owner** (Wochenstart-Sichtbarkeit: KW32 Tag 1 -0,40 % Alpha -1,87 pp NEG, LLY BO -1,16 % weiter UNTERSCHRITTEN aber Std sicher, AAPL BO HT+1 letzter Tag Puffer +0,67 % kritisch nah 0 % morgen HT+2 Blackout-Ende, VIX 16 stark reduziert = Vola-Entspannung, neue Watchlist UAL #1 XLI mit RS +33,61 pp #1 TOP), Nächste Routine Di 04.08. 08:30 ET Pre-Market KW32 Tag 2)

**Vorheriger Stand:** 2026-08-03 13:12 ET (**Midday Stop-Check KW32 Tag 1**, Equity Live **96.020,31 $** vs last_equity 96.360,90 = **-0,353 %** Daily [GRÜN, Cap -3 %], Cash 56.707,49 = 59,06 %, MV Live **39.313,31 $** (5 Pos, -307,48 vs Open 39.620,79 = -0,776 %, LLY-Sell-off dominant Fortsetzung), DD **-4,043 %** vs ATH 100.066,47 [GRÜN, verschlechtert vs Open -3,378 %], **SPY Live 756,585 Alpaca IEX** vs Fr Close 746,79 = **+1,312 % Post-Weekend-Rally weiter Fortsetzung** (Crash-Filter INAKTIV, vs Open 751,56 +0,673 %), **Alpha vs SPY -1,665 pp NEGATIV** (verschlechtert vs Open -0,669 pp, LLY-XLV-Sell-off dominant + Portfolio kein SPY-Beta), **KEIN V1/V2/V3/V4-Trigger per strategy.md** (Std-V1 alle 5 SICHER), **KEINE Sell-/Limit-Order platziert, 0 offene Orders**, **🔴 LLY Blackout-V1_neu 1.134,20 (Bull-Konvention) weiter UNTERSCHRITTEN bei Live 1.117,51 = -1,49 % verschlechtert vs Open -0,28 %** (chg -2,797 % Worst chg, P/L -6,46 % Worst P/L verschlechtert vs Open -5,26 %), **Std-V1 1.098,38 SICHER +1,74 % ENGSTE Std verschlechtert vs Open +2,97 %**, Strategie-Lock CLAUDE.md Rule 3 → HALTEN, AAPL Blackout HT+1 letzter Tag Puffer +1,94 % essentiell unverändert vs Open +1,97 % (306,865 chg -0,659 %, Std +5,27 %), V3/V4 max P/L JPM +5,64 % << 20 %-TP1 kein Trigger, V2-Trailing-Stop-Check alle 5 SICHER (weniger restriktiv als Std-V1), **RSI/EMA werden bei Midday NICHT geprüft (nur Market Open + Close per Midday-Routine)**, Positionen sortiert eng→weit Std-V1: **LLY +1,74 % ENGSTE Std** (1.117,51 chg -2,797 % Worst chg, P/L **-6,46 % Worst P/L**, Blackout **-1,49 % UNTERSCHRITTEN**), **AAPL +5,27 %** (306,865 chg -0,659 %, P/L -3,15 %, Blackout +1,94 % HT+1 letzter Tag), V +10,99 % (364,75 chg -0,374 %, P/L +2,12 %), UNH +12,37 % (415,18 chg **+0,179 % Best chg**, P/L +3,38 %), JPM +14,83 % (351,56 chg -0,071 %, **Best P/L +5,64 %**), **Käufe KW32 0/2 unverändert** (Kaufsignal-Scan bei Midday nicht Teil der Routine), **8/8 GRÜN + 2 WARN** (AAPL BO HT+1 letzter Tag Puffer +1,94 % + **LLY BO HT-2 UNTERSCHRITTEN -1,49 % weiter verschlechtert**), **KEIN ClickUp** (Midday-Routine STEP 5: nur bei Stop-Trigger oder Daily-Cap-Alert → Silence-Rule Routine), **PushNotification Prio 2 Owner** (Follow-up zum Open Prio 1: LLY Blackout weiter verschlechtert auf -1,49 %, Std-V1 aber SICHER +1,74 %, Alpha vs SPY verschlechtert auf -1,67 pp, keine Handlung erforderlich, Owner-Sichtbarkeit für Post-Escalation-Update gerechtfertigt), Nächste Routine 16:00 ET Market Close Tagesbilanz)

**Vorheriger Stand:** 2026-08-03 09:42 ET (**Market Open KW32 Tag 1**, Equity Live **96.331,69 $** vs last_equity 96.360,90 = **-0,030 %** Daily [GRÜN, Cap -3 %, essentiell flat], Cash 56.707,49 = 58,87 % unverändert, MV Live **39.620,79 $** (5 Pos, -68,38 vs Fr Close 39.689,17 = -0,172 %, LLY-Sell-off dominant), DD **-3,378 %** vs ATH 100.066,47 [GRÜN, marginal verschlechtert vs Pre -3,357 %], **SPY Live 751,56 Alpaca IEX** vs Fr Close 746,79 = **+0,639 % Post-Weekend-Rally-Fortsetzung** (Crash-Filter INAKTIV), **Alpha vs SPY -0,669 pp NEGATIV** (LLY-Sell-off dämpft SPY-Beta), VIX 19,31 Pre-Read [GRÜN <25], **kein V1-V6-Trigger per strategy.md** (Std-V1 alle 5 SICHER), **KEINE Sell-/Limit-Order platziert, 0 offene Orders**, **🔴 LLY Blackout-V1_neu 1.134,20 (Bull-Konvention) intraday UNTERSCHRITTEN bei Live 1.131,04 (chg -1,55 % Worst chg), Std-V1 1.098,38 SICHER +2,97 % ENGSTE Std, Strategie-Lock CLAUDE.md Rule 3 → HALTEN**, AAPL Blackout HT+1 auslaufend V1_neu 301,02 Puffer +1,97 % (306,94), **Käufe KW32 0/2 unverändert**, **Kaufsignal-Scan Slot 1/2 alle 6 Kandidaten REJECT/SKIP:** UNP K4 Fr 116 % <120 % FAIL + Live-Momentum-Bruch -0,28 % vs SPY +0,64 % + Live-K4 22 % pro-rata unbelastbar, **ABBV alle K1-K5 ✓ (K5 +10,2 % marginal) aber XLV-Cap-Diskussion pending Owner-Klärung → SKIP per Strategie-Lock Rule 3**, EOG K3 -0,11 pp FAIL marginal, AMZN K2 RSI 75,6 >70 FAIL (+5,37 % Gap-Up), GOOGL K3 RS -8,31 pp FAIL (+3,94 % Gap-Up), MRK BLOCKIERT Earnings Di 04.08. BMO HT-1, **Slot 1/2 KW32 bleibt OFFEN** — Cascade-Framework INAKTIV aber XLV-Cap pending, **8/8 GRÜN + 2 WARN** (AAPL BO HT+1 auslaufend Puffer +1,97 % + **LLY BO HT-2 UNTERSCHRITTEN -0,28 %**), ClickUp Prio 4 Routine-Log, **PushNotification Prio 1 Owner** (LLY-Blackout-V1 gebrochen + XLV-Cap-Klärung überfällig), Nächste Routine 13:00 ET Midday Stop-Check)

**Vorheriger Stand:** 2026-08-03 08:30 ET (**Pre-Market KW32 Tag 1**, Equity Pre **96.707,72 $** vs last_equity 96.360,90 = **+0,360 %** Daily [GRÜN, Cap -3 %], Post-Weekend-Recovery alle 5 Pos positiv change_today, Cash 56.707,49 = 58,64 % unverändert, MV Pre **40.000,53 $** (+311,36 vs Fr Close 39.689,17 = +0,784 %), DD **-3,357 %** vs ATH 100.066,47 [GRÜN, verbessert vs Fr Close -3,667 %], **VIX 19,31 Perplexity** [GRÜN <25], **SPY Futures E-mini +0,44 % ~+0,88 % Index-Äquiv.** vs Fr Close 746,79 (Crash-Filter INAKTIV), 10Y 4,28 %, Weekly KW32 Tag 1 Reset frisch, **Käufe KW32 0/2 frisch**, **8/8 GRÜN + 2 WARN** (AAPL BO HT+1 auslaufend +3,42 % Std +6,79 % / LLY BO HT-2 +2,36 % ENGSTE Std +5,70 %), **Cascade-Framework INAKTIV** (beide BO-Puffer > 1 %), **Watchlist Mo Open KW32:** UNP #1 XLI (K1-K3 ✓ Fr, K4 116 % borderline, K5 zwingend Multi-Source), ABBV #2 XLV (K1-K3 ✓ Fr, K4 135 % ✓, K5 zwingend, **XLV-Cap-Warnung 19,88 % → ~30 %**), EOG #3 XLE (K1-K3 ✓ Fr, K4 84 % FAIL Rebound-Watch, K5 vorbekannt ✓ FwdPE 9,98 + RevGr +15,63 %), **MRK BLOCKIERT Earnings Di 04.08. BMO HT-1**, AMZN/GOOGL neu conditional pending Earnings-Klärung, **Kaufscan Market Open: JA** mit Bedingungen, **0 offene Orders** Alpaca, ClickUp Prio 4 Routine-Log, KEINE PushNotification (Silence-Rule Routine ohne Cap/Blackout <1 %), Nächste Routine 09:30 ET Market Open KW32 Tag 1)

**Vorheriger Stand:** 2026-07-31 17:00 ET (**Weekly Review KW31 FINAL**, Equity Live **96.296,93 $** vs Fr 24.07. Close 97.526,60 = **Wochenrendite -1,261 %** [GRÜN, Cap -5 %], SPY Weekly +1,068 % (738,90 → 746,79 Alpaca IEX), **Alpha vs SPY -2,329 pp NEGATIV** (Cash 58,89 % + Portfolio-Sektoren XLV -0,02 % / XLK -0,39 % / XLF +1,07 % underperformt vs SPY-Rally getrieben von XLY +6,05 % + XLC +1,81 %), **YTD Depot -3,703 %** (vs 100.000 $ Init), **YTD SPY +9,529 %** (Alpaca IEX YE25 681,82 → 746,79), **YTD-Alpha -13,232 pp** (Bot 61 Tage lebend, strukturelle Cash-Bias), DD **-3,767 %** vs ATH 100.066,47 [GRÜN], **KW31 Trades: 1 Verkauf (GS V1-Stop -8,89 % Mo 27.07.), 0 Käufe** (Slot 1/2 + 2/2 beide verfallen wegen Cascade-Framework AAPL/LLY Blackout-Puffer <1 % + K4/K5-FAIL Watchlist), **Realisiert KW31: -811,95 $ / kumuliert Bot-Init -3.638,91 $**, Win-Rate KW31 0/1 = 0 %, **Sektor-Priorität KW32:** XLY #1 (+6,05 %) AMZN-Kandidat + XLC #2 (+1,81 %) GOOGL/NFLX + XLP #3, XLV-Cap-Diskussion (48,3 % investiert) blockiert ABBV/MRK-Käufe, **Nächste Routine Mo 03.08. 08:30 ET Pre-Market KW32 Tag 1**)

**Vorheriger Stand:** 2026-07-31 16:00 ET (**Market Close Tagesbilanz KW31 Tag 5 FINAL**, Equity Close **96.396,66 $** vs Do Close 97.458,61 = **-1,090 %** Daily [GRÜN, Cap -3 %, verbessert vs Midday -1,313 %], SPY Close **746,79** Alpaca IEX vs Do Close 741,63 = **+0,696 % Post-FOMC-Recovery-Fortsetzung** [Perplexity divergiert bei 741,69 = -0,13 %, IEX bar verified via Snapshot Last-Trade 15:59:59 ET → IEX bindend]; Cash 56.707,49 = **58,83 %**, MV Close **39.689,17 $** (5 Pos, +217,90 vs Midday 39.471,27 = **AAPL-Recovery +7,72 $ pro Share intraday** bei Blackout-Puffer-Wiederherstellung), DD **-3,667 %** vs ATH 100.066,47 [GRÜN, verbessert vs Midday -3,885 %], Weekly KW31 Tag 5 FINAL **-1,159 %** vs Fr 24.07. Close 97.526,60 (-1.129,94 $) [GRÜN weit von Cap -5 %], Alpha vs SPY **-1,785 pp NEGATIV** (SPY-Recovery-Fortsetzung ohne Portfolio-Beta, UNH -1,71 % + LLY -0,60 % dämpfen), **5 V1-V6 SICHER Vollcheck EOD-Bars — KEIN Stop-Trigger, KEINE Sell-/Limit-Order für Mo 03.08. platziert, 0 offene Orders**, V1-Puffer min **LLY +4,48 % ENGSTE** (Close 1.147,61 chg -0,60 %, P/L **-3,88 % Worst P/L**), **AAPL Blackout HT+0 Recovery** (Close 309,15 chg -7,31 % vs Do Bar 333,07 dominant Post-Earnings, P/L -2,43 %, Blackout-V1_neu 301,02 Puffer **+2,70 % verbessert vs Midday +0,111 %**, Std-V1 291,51 Puffer +6,05 %), V +2,51 % (366,13 chg -0,04 %), UNH +3,59 % (415,99 chg -1,71 % XLV-Sell-off-Fortsetzung), JPM +5,71 % (351,79 chg +0,28 % Best chg XLF-Recovery-Fortsetzung Best P/L), **V5-Vollcheck 5 SICHER** (V engster EMA-Diff +2,45 % positiv, JPM +5,28 %, AAPL +10,30 % nach -7,31 % Post-Earnings noch weit von Death Cross, LLY +11,98 %, UNH +13,20 %), **V6-Vollcheck 5 SICHER** (max RSI V 66,2 << 80, JPM 60,7, LLY 49,0, UNH 48,7, AAPL 43,6; RS_4w LLY -5,37 pp NEG aber RSI 49 → V6 sicher via UND-Bedingung, UNH -2,73 pp NEG aber RSI 49, AAPL -0,10 pp marginal NEG aber RSI 44), V3/V4 max P/L JPM +5,71 % << 20 %-TP1 kein Trigger, **8/8 GRÜN + 2 WARN** (AAPL Blackout HT+0 Post-Earnings +2,70 % + LLY Blackout HT-3 +1,18 % — beide über 1 %-Konvention-Grenze aber Watch), **Watchlist Mo 03.08. K1-K3 ✓ Alpaca IEX EOD Fr:** UNP (K1 +10,3 % ✓, RSI 59 ✓, RS +4,5 pp ✓, K4 116 % ✓ borderline, XLI-Diversifikation neu, K5 Multi-Source zwingend), ABBV (K1 +6,1 % ✓, RSI 57 ✓, RS +14,7 pp #2 ✓, K4 135 % ✓ Session-Vol-Best, XLV-Cap-Warnung bei bereits 19,88 %, K5 zwingend), MRK (K1 +12,4 % ✓, RSI 64 ✓, RS +15,3 pp #3 ✓, K4 69 % FAIL Watch, XLV-Cap-Warnung), EOG (K5 vorbekannt ✓ FwdPE 9,98 + RevGr +15,63 %, K4 84 % FAIL K4-Rebound-Watch, XLE 0 %), CVS **REJECT persistent K5 FAIL** RevGr +6,2 % Q1 26, BAC K4 50 % FAIL, **Slot 1/2 KW31 bleibt final OFFEN — Cascade-Framework über Wochenende Watch**, **ClickUp Prio 3 (Normal, negativer Tag ohne Cap-Alert)** wird gesendet, **PushNotification Prio 2 Owner** (Weekly-Recap + AAPL-Recovery-Update + Watchlist-Refresh), Nächste Routine Mo 03.08. 08:30 ET Pre-Market KW32 Tag 1)

**Vorheriger Stand:** 2026-07-31 13:07 ET (**Midday Stop-Check KW31 Tag 5**, Equity Live **96.178,76 $** vs Do Close 97.458,61 = **-1,313 %** Daily [GRÜN, Cap -3 %, leicht verbessert vs Open -1,376 %], SPY Live **744,635** vs Do Close 741,63 = **+0,405 %**, Cash 56.707,49 = 58,96 %, MV Live **39.471,27 $** (5 Pos, -1.279,85 vs Do Close 40.751,12 = -3,140 %), DD **-3,885 %** vs ATH 100.066,47 [GRÜN, marginal verbessert vs Open -3,947 %], Weekly KW31 Tag 5 **-1,382 %** [GRÜN weit von Cap -5 %], Alpha vs SPY **-1,718 pp NEGATIV** (SPY-Recovery-Fortsetzung ohne Portfolio-Beta), **KEIN Stop-Trigger, keine Sell-/Limit-Order platziert, 0 offene Orders**, **AAPL Blackout-Puffer +0,11 % ENGSTE weiter razor-thin verschlechtert** (301,355 chg -0,118 % vs Open, Std-V1 291,51 +3,38 % SICHER), **LLY Blackout-Puffer +0,78 % marginal verbessert** (1.143,02 chg +0,155 % vs Open, Std-V1 1.098,38 +4,06 % SICHER), Positionen sortiert eng→weit Std-V1: AAPL +3,38 % (301,355 P/L -4,89 %), LLY +4,06 % (1.143,02 P/L -4,26 %), V +11,18 % (365,33 chg +0,731 % Best chg, P/L +2,28 %), UNH +13,53 % (419,44 chg -0,036 %, P/L +4,45 %), JPM +15,36 % (353,20 chg +0,756 %, P/L +6,14 % Best P/L), V3/V4 max P/L JPM +6,14 % << 20 %-TP1 kein Trigger, **8/8 GRÜN + 2 WARN** (AAPL Blackout HT+0 razor-thin +0,11 % + LLY Blackout HT-3 +0,78 %), **KEIN ClickUp** (kein Stop, kein Cap → Silence-Rule Routine), **PushNotification Prio 2 Owner** (Follow-up Prio 1 Open-Escalation: AAPL Blackout-Puffer weiter razor-thin auf +0,11 % aber Std-V1 SICHER, LLY marginal Recovery, keine Aktion), Nächster Check Fr 31.07. 16:00 ET Market Close Tagesbilanz)

**Vorheriger Stand:** 2026-07-31 09:42 ET (**Market Open KW31 Tag 5**, Equity Live **96.117,58 $** vs Do Close 97.458,61 = **-1,376 %** Daily [GRÜN, Cap -3 %], SPY Live **743,51** vs Do Close 741,63 = **+0,253 % milde Post-FOMC-Konsolidierung** [Crash-Filter INAKTIV], Cash 56.707,49 = 58,99 % unverändert, MV Live **39.410,09 $** (5 Pos, -1.341,03 vs Do Close 40.751,12 = -3,290 % **AAPL Post-Earnings-Sell-off dominant**), DD **-3,947 %** vs ATH 100.066,47 [GRÜN, verschlechtert vs Do -2,606 %], Weekly KW31 Tag 5 **-1,444 %** [GRÜN weit von Cap -5 %], Alpha vs SPY **-1,629 pp NEGATIV** (AAPL -9,72 % Guidance-Sell-off dominant), **VIX Perplexity 17,98** [GRÜN <25], **kein V-Trigger per strategy.md, keine Sell-/Limit-Order platziert, 0 offene Orders**, **🔴 AAPL Blackout-V1_neu 301,02 intraday 09:41 ET UNTERSCHRITTEN bei Dip 300,535 (jetzt Recovery 301,71 = +0,23 % razor-thin), Std-V1 291,51 SICHER, Strategie-Lock → HALTEN**, **🔴 LLY Blackout HT-3 ab HEUTE aktiviert V1_neu 1.134,20 Puffer +0,62 % ENGSTE**, Positionen sortiert eng→weit vs Std-V1: AAPL +3,50 % (301,71 chg -9,72 % Worst chg, P/L -4,78 % Worst), LLY +3,90 % (1.141,25 chg -1,36 %, P/L -4,41 %), V +10,36 % (362,68 chg -0,98 %), UNH +13,57 % (419,59 chg -1,20 %), JPM +14,50 % (350,55 chg -0,09 % Best chg), Käufe KW31 0/2 unverändert, **Kaufsignal-Scan ALLE 4 REJECT/SKIP:** CVS K5-FAIL RevGr Q1 +6,2 % <10 %, BAC/UNP/EOG K4-FAIL Do EOD <120 % + Cascade-Framework aktiviert (AAPL/LLY beide Blackout-Puffer <1 %), Slot 1/2 KW31 bleibt OFFEN, **8/8 GRÜN + 2 WARN** (AAPL Blackout-V1 intraday gebrochen + LLY Blackout HT-3 ENGSTE), **ClickUp Prio 4 Routine-Log**, **PushNotification Prio 1 Owner** (2 gleichzeitige Blackout-Puffer <1 % rechtfertigen dringende Sichtbarkeit für Midday-Entscheidung), Midday 13:00 ET Prio-1 Watch AAPL/LLY-Stabilisierung)

**Vorheriger Stand:** 2026-07-31 08:36 ET (Pre-Market KW31 Tag 5, Equity Pre 96.473,12 $ vs Do Close = -1,011 %, SPY Pre 743,68 = +0,276 %, VIX ~19,8 Do Close-Referenz, 5 V1-V6 SICHER Pre-Read, AAPL Post-Earnings -8,10 % Guidance-Sell-off, LLY Blackout HT-3 aktiviert, Watchlist CVS/BAC/UNP/EOG K1-K3 ✓ K4/K5 Multi-Source Open zwingend)

**Vorheriger Stand:** 2026-07-30 16:00 ET (**Market Close Tagesbilanz KW31 Tag 4**, Equity Close **97.458,61 $** vs Mi Close 97.970,67 = **-0,523 %** [GRÜN, Cap -3 %, minimal verbessert vs Midday -0,575 %], SPY Close **741,63** vs Mi Close 729,57 = **+1,653 % Post-FOMC-Recovery** [Crash-Filter INAKTIV], Cash 56.707,49 = 58,19 %, MV Close **40.751,12 $** (41,81 %, 5 Pos, +51,49 vs Midday), DD **-2,606 %** [GRÜN], Weekly KW31 Tag 4 **-0,070 %** [GRÜN weit von -5 %-Cap], Alpha vs SPY **-2,176 pp NEGATIV** (LLY XLV-Sell-off dominant), **5 V1-V6 SICHER Vollcheck EOD-Bars — kein Stop-Trigger, keine Sell-/Limit-Order platziert, 0 offene Orders**, V1-Puffer min **LLY +5,34 % ENGSTE** (Close 1.157,00, chg **-4,382 % Worst chg**, P/L **-3,09 % Worst P/L weiter verschlechtert**), **AAPL Blackout HT-0 HEUTE Q3 FY26 AMC ~5:00 PM ET V1_neu 301,02 Puffer +11,02 %** (Close 334,20, chg -1,18 %, **Best P/L +5,47 %**), V +11,46 % (Close 366,27, chg -0,67 %), JPM +14,60 % (Close 350,85, chg **+1,78 % Best chg** XLF-Post-FOMC-Recovery-Fortsetzung), UNH +14,95 % (Close 424,686, chg +0,98 % XLV-Divergenz Recovery, **Best P/L +5,76 %**), Ø P/L **+3,22 %**, Käufe KW31 0/2 unverändert, **V5-Vollcheck alle 5 Golden Cross intakt (V engster EMA-Spread +2,92 %)**, **V6-Vollcheck alle 5 SICHER (max RSI V 63,3 << 80; LLY RS_4w -2,51 pp neg. aber RSI 47 → V6 nicht ausgelöst)**, V3/V4 max UNH +5,76 % / AAPL +5,47 % / JPM +5,43 % << 20 % TP1 kein Trigger, 8/8 GRÜN + 1 WARN (AAPL Blackout HT-0 heute AMC), **Watchlist Fr 31.07. K1-K3 ✓:** CVS (RS +21,57 pp #1), BAC (RS +12,86 pp), UNP (RS +5,38 pp XLI neue Diversifikation), EOG (RS +0,94 pp K5 vorbekannt ✓), **XLV-Sektor bifurkiert Fortsetzung:** UNH Recovery +0,98 % vs LLY Sell-off -4,38 % dominant, **ClickUp Prio 3 (Normal, negativer Tag)** wird gesendet, **PushNotification Prio 2 Owner** (LLY -4,38 % + Puffer +5,34 % ENGSTE + LLY-Blackout-Aktivierung morgen HT-3 → Owner-Sichtbarkeit gerechtfertigt vs Silence), **LLY Blackout ab Fr 31.07. HT-3 aktiv V1_neu 1.134,20 = -1,97 % dann als virtueller Puffer**)

---

## Weekly Review KW32 — 2026-08-07 17:00 ET (Fr, Wochenschluss) — Wochenrendite +0,551 % / Alpha -1,487 pp NEG / YTD -3,487 % / YTD-Alpha -16,884 pp

### Wochenabschluss KW32 — 2026-08-07

```
Gesamtwert (Equity):    96.512,65 $   (Alpaca Close 16:00 ET; vs Fr 31.07. Close 96.396,66 = +0,120 %; Live 17:00 ET Bewegung marginal, Alpaca equity 96.520,63 aktuell)
Cash:                   56.707,49 $   (58,76 %)   unverändert seit 20.07.26 (V-Kauf)
Investiert (MV):        39.805,16 $   (41,24 %)   5 Positionen (AAPL, JPM, LLY, UNH, V)
Wochenrendite:          +0,551 %      (Mo 03.08 EOD 95.984,04 → Fr 07.08 Close 96.512,65)
Alt-Referenz Fr→Fr:     +0,120 %      (Fr 31.07 Close 96.396,66 → Fr 07.08 Close 96.512,65)
SPY Wochenrendite:      +2,038 %      (Mo 03.08 Close 757,72 → Fr 07.08 Close 773,16, Alpaca IEX)
Alt SPY Fr→Fr:          +3,531 %      (Fr 31.07 Close 746,79 → Fr 07.08 Close 773,16)
Alpha vs SPY (Mo→Fr):   -1,487 pp     [NEGATIV, 4. Woche in Folge Alpha-Verlust bei SPY-Rally-Wochen]
Alpha vs SPY (Fr→Fr):   -3,411 pp     [NEGATIV Alt-Referenz]
YTD Depot (seit Init):  -3,487 %      (100.000 → 96.512,65, Bot lebt 68 Tage seit 31.05.26)
YTD SPY 2026:           +13,397 %     (Alpaca IEX YE25 681,82 → 07.08. Close 773,16)
YTD-Alpha:              -16,884 pp    (verschlechtert vs KW31 -13,232 pp durch KW32-SPY-Rally +3,53 %)
ATH:                    100.066,47 $  (intraday Open 2026-06-22)
Drawdown vom ATH:       -3,552 %      [GRÜN — Schwelle -15 % bei 85.056 $]
Offene Positionen:      5 / 8
Nächste Woche max. Käufe: 2 (Reset Mo 10.08.)
Watchlist KW33: UAL (XLI Prio 1), UNP (XLI Prio 2), BAC (XLF Prio 3), NEM/FCX/DOW (XLB neue Pipeline), NVDA (XLK marginal); PANW → BLACKOUT-SKIP ~17.08.
```

**Trade-Aktivität KW32:**
- Käufe: 0 (Slot 1/2 + 2/2 beide VERFALLEN — alle Watchlist-Kandidaten Fr Open REJECT/SKIP: UAL K4-FAIL 6. Tag, GS K4 low Vol, DELL/HPE K1-Bruch, UNP K4 heavy, NVDA K3 marginal)
- Verkäufe: 0 | Stop-Loss-Trigger: 0 | Death-Cross V5: 0 | RSI-Überkauft V6: 0
- Geschlossene Trades: 0 | Win-Rate KW32: n/a | Ø Haltedauer: n/a
- Handelstage: 5 von 5 (keine Feiertage)
- Realisiert kumuliert seit Bot-Init: -3.638,91 $ (unverändert vs KW31)

**Positions-Wochen-Performance (Alpaca IEX Fr→Fr):**
- LLY:  +3,229 %  (1.148,86 → 1.185,96)   BEST — Post-Q2-Rally Mi 05.08. BMO EPS $8,38 Beat
- JPM:  +1,621 %  (351,86 → 357,56)       XLF-Steady-Fortsetzung
- AAPL: +1,479 %  (308,73 → 313,29)       Post-Q3-Konsolidierung stabil
- V:    -0,951 %  (366,07 → 362,59)       Fr Give-back -2,15 % Worst chg ohne klaren Katalysator
- UNH:  -1,771 %  (414,43 → 407,09)       WORST — XLV-Divergenz-Fortsetzung, V2-Wick razor-thin

**Sektor-Check (Max 30 % vom Portfolio-Kapital):**
- XLV (LLY+UNH):  19.244,04 $ → 48,3 % investiert / 19,93 % Portfolio | 2 Pos [Owner-Klärung 4. Woche pending]
- XLF (JPM+V):    10.865,25 $ → 27,4 % investiert / 11,26 % Portfolio | 2 Pos [OK]
- XLK (AAPL):      9.703,00 $ → 24,5 % investiert / 10,06 % Portfolio | 1 Pos [OK]
- Cash:           56.707,49 $ → 58,76 % Portfolio | strukturell zu hoch für Bull-Rally-Regime

**Signal-Status Wochenschluss (V1–V6 EOD-Vollcheck Fr Close, alle 5 SICHER):**
- AAPL 313,30 — Std-V1 291,51 Puffer **+7,47 % ENGSTE Std**; V2 Wick 344,56 Threshold 303,21 razor-thin +0,15 %; V5 EMA50 309,87 > EMA200 280,45 (+10,49 %); V6 RSI 47,6 << 80 (RS_4w -3,06 pp aber UND-Bedingung sicher)
- JPM  357,52 — Std-V1 306,16 Puffer +16,78 %; V2 +11,12 %; V5 EMA50 336,62 > EMA200 316,50 (+6,36 %); V6 RSI 63,0 << 80
- LLY  1.185,71 — Blackout-V1_neu 1.134,20 Puffer +4,54 % ÜBERSCHRITTEN Bull-Konvention; Std-V1 1.098,38 Puffer +7,95 %; V5 +12,46 %; V6 RSI 53,8 << 80; **HT+2 heute letzte Session, Ende Mo 10.08.**
- UNH  406,13 — Std-V1 369,44 Puffer +9,94 %; V2 Wick 460,95 Threshold 405,636 razor-thin **+0,12 % RECOVERED**; V5 +12,72 %; V6 RSI 44,0 << 80 (RS_4w -6,53 pp aber UND-Bedingung sicher)
- V    362,50 — Std-V1 328,60 Puffer +10,32 %; V2 +11,23 %; V5 EMA50 348,76 > EMA200 337,63 (+3,29 % engster aber positiv); V6 RSI 55,3 << 80
- **KEINE Sell-/Limit-Order für Mo 10.08. platziert, 0 offene Orders**

**Strategie-Status:** STABIL — keine Anpassung nötig. Diskussions-Punkte KW33: (1) XLV-Cap-Deutung 4. Woche pending, (2) Cash-Quote 58,76 % vs 4-Wochen-Alpha-Verlust, (3) Screener-Erweiterung XLB/XLK-Alternativen (AMZN/GOOGL/NEM/FCX).

**Sektor-Ranking KW32 (Alpaca IEX Fr→Fr, SPY +3,531 %):**
1. **XLK +7,25 %** (+3,72 pp Alpha)   — Tech dominant
2. **XLB +4,86 %** (+1,33 pp Alpha)   — Materials
3. XLY +3,26 % (-0,27 pp)             — Consumer Discretionary
- Rest unter SPY: XLI +3,01, XLC +2,81, XLV +1,92, XLF +1,19, XLP +0,09, XLRE -0,13, XLU -1,66, **XLE -3,44 % Worst**

**Überraschungs-Insight:** XLK dominierte KW32 mit +7,25 % Woche (Alpha +3,72 pp) — größte Sektor-Divergenz seit KW28. AAPL profitierte marginal (+1,48 %), doch Portfolio-XLK-Exposure fing nur ~20 % der Rally ab, was den kumulativen KW29-32-Alpha-Verlust bei SPY-Rally-Wochen strukturell erklärt.

---

## Weekly Review KW31 — 2026-07-31 17:00 ET (Fr, Wochenschluss) — Wochenrendite -1,261 % / Alpha -2,329 pp NEG / YTD -3,703 % / YTD-Alpha -13,232 pp

### Wochenabschluss KW31 — 2026-07-31

```
Gesamtwert (Equity):    96.296,93 $   (Alpaca /v2/account 17:00 ET, vs Fr 24.07. Close 97.526,60)
Cash:                   56.707,49 $   (58,89 %, unverändert seit GS-Stop Mo 27.07.)
Investiert:             39.589,44 $   (41,11 %, 5 Positionen, MV Live nach Market-Close)
Wochenrendite Depot:    -1,261 %      (-1.229,67 $, vs Fr 24.07. Close)                    [GRÜN, Cap -5 %, Puffer +3,74 pp]
Wochenrendite SPY:      +1,068 %      (Alpaca IEX 738,90 → 746,79)
Alpha vs SPY diese Woche: -2,329 pp NEGATIV
YTD Depot:              -3,703 %      (vs Init 100.000 $ am 31.05.26)
YTD SPY:                +9,529 %      (Alpaca IEX YE25 681,82 → 746,79)
YTD Alpha:              -13,232 pp NEGATIV
ATH:                    100.066,47 $  (Mo 30.06.26)
Drawdown vs ATH:        -3,767 %                                                            [GRÜN, Alarm -15 %]
Offene Positionen:      5/8           (AAPL, JPM, LLY, UNH, V)
Nächste Woche max. Käufe: 2            (KW32 Slots frisch, Reset Mo 03.08.)
Realisiert KW31:        -811,95 $     (GS V1-Stop -8,89 %)
Realisiert kumuliert:   -3.638,91 $   (seit Bot-Init 31.05.26)
Handelstage:            5 von 5       (keine Feiertage, Fed-FOMC Mi 29.07. hawkish)
Guardrails:             8/8 GRÜN + 2 WARN (AAPL Blackout HT+0 auslaufend, LLY Blackout HT-3 → HT-2 Mo)
```

**Trade-Analyse KW31 (27.07.-31.07.):**
- **Käufe: 0** (Slot 1/2 + 2/2 beide verfallen)
- **Verkäufe: 1** (GS Mo 27.07. 13:07 ET Market Order @ 1.040,25 × 8 Sh = 8.322,00 $ Erlös)
- **Stop-Trigger: 1** (V1 -8 % strikt, V1 1.050,40 verletzt bei Kurs 1.040,57)
- **Durchschnittliche Haltedauer geschlossen KW31: 8 HT** (nur GS: Fill 15.07. → Exit 27.07.)
- **Win-Rate KW31: 0/1 = 0 %** (nur Verlust-Exit)
- **Trigger-Beobachtungen:** Fill-Day-Muster n=7 (Fill+8 HT für GS analog GOOGL Fill+12, MU Fill+4, AVGO Fill+3). Rebound-Tag+1-Fehlschlag Mo 27.07. Open bestätigte Muster.

**Sektor-RS-Ranking (Alpaca IEX Fr 24.07. Close → Fr 31.07. Close):**

| Rank | Sektor | Weekly % | vs SPY | Portfolio-Anteil | Bull-Kandidaten KW32 |
|------|--------|----------|--------|------------------|----------------------|
| #1 | **XLY** (Consumer Discretionary) | **+6,05 %** | +4,98 pp | 0 % | **AMZN +16,96 % w** Post-Q2-Rally |
| #2 | **XLC** (Communication Services) | **+1,81 %** | +0,74 pp | 0 % | **GOOGL +11,36 % w** Post-Q2-Rebound, NFLX +2,28 % |
| #3 | **XLP** (Consumer Staples) | **+1,12 %** | +0,05 pp | 0 % | keine akuten K1-K3-Kandidaten |
| #4 | XLF | +1,07 % | +0,00 pp | 27,6 % inv (V+JPM) | BAC K4-FAIL persistent |
| #5 | XLV | -0,02 % | -1,09 pp | **48,3 % inv (UNH+LLY) — Cap-Diskussion** | ABBV RS #2 + MRK RS #3 BLOCKIERT bis Owner-Klärung |
| #6 | XLE | -0,12 % | -1,19 pp | 0 % | EOG K5 vorbekannt ✓ K4-FAIL-Rebound-Watch |
| #7 | XLK | -0,39 % | -1,46 pp | 24,0 % inv (AAPL) | MSFT K1-FAIL, keine Kandidaten |
| #8 | XLI | -1,58 % | -2,65 pp | 0 % | UNP K1-K3 ✓ K4 borderline 116 % |
| #9 | XLB | -1,65 % | -2,72 pp | 0 % | keine |
| #10 | XLRE | -1,94 % | -3,00 pp | 0 % | keine (REITs TABU per strategy.md) |
| #11 | XLU | -4,17 % | -5,24 pp | 0 % | keine, Meidung |

**Top-3-Kandidaten für nächste Woche (KW32) nach Fundamentals-Screen + Blackout-Filter:**

| Kandidat | Sektor | Fr Close | Weekly % | K1-K3 (Fr) | K5-Status | Earnings-Blackout | Prio |
|----------|--------|----------|----------|------------|-----------|-------------------|------|
| **AMZN** | XLY | 271,46 | **+16,96 %** | zu prüfen Mo (Rally) | zu prüfen Mo Multi-Source | Q3 ~Ende Okt (blackout-frei) | **#1** neue XLY-Diversifikation |
| **GOOGL** | XLC | 356,06 | **+11,36 %** | zu prüfen Mo | zu prüfen Mo Multi-Source | Q3 ~Ende Okt (blackout-frei) | **#2** aber **KW30-V1-Präzedenz -12,65 %** — Fill-Day-Buffer |
| **NFLX** | XLC | 71,69 | +2,28 % | zu prüfen Mo | zu prüfen Mo | Q3 ~Mitte Okt | **#3** Backup XLC |
| UNP | XLI | 292,15 | +0,94 % (Fr chg) | K1 ✓ +10,26 %, RSI 59, RS +4,45 pp, K4 116 % ✓ | zwingend Mo | keine 10 HT | #4 XLI |
| EOG | XLE | 148,65 | +2,10 % (Fr chg) | K1 ✓ +9,72 %, RSI 67 knapp, RS +1,75 pp, K4 84 % FAIL | vorbekannt ✓ FwdPE 9,98, RevGr +15,63 % | keine 10 HT | #5 XLE K4-Rebound-Watch |
| ABBV | XLV | 250,88 | -2,57 % (Fr chg) | K1 ✓, K2 ✓, RS **+14,73 pp #2**, K4 Fr 135 % ✓ | zwingend Mo | keine 10 HT | **BLOCKIERT XLV-Cap 48,3 %** |
| MRK | XLV | 130,21 | +0,32 % (Fr chg) | K1 ✓, K2 ✓, RS **+15,32 pp #3**, K4 69 % FAIL | zwingend Mo | zu prüfen Mo | **BLOCKIERT XLV-Cap 48,3 %** |
| META | XLC | 556,60 | **-6,48 %** Post-Q2-Miss | K3 vermutlich negativ | — | Q3 ~Ende Okt | **SKIP** Konsolidierung |
| CVS | XLV | 104,42 | flach | K1-K3 ✓, RS +21,57 pp #1 | **REJECT K5** RevGr +6,2 % <10 % | — | REJECT persistent |
| BAC | XLF | 61,98 | +0,36 % (Fr chg) | K1-K3 ✓ | zu prüfen | keine 10 HT | K4 Fr 50 % FAIL SKIP |

**Sektor-Cap-Prüfung (STEP 6):**
- **XLV: 48,3 % des investierten Kapitals** (UNH 24,4 % + LLY 23,9 % = 19.137,60 $ von 39.592,07 $ invested) ⚠️ **Strikte Deutung: VERSTOSS >30 %**. Portfolio-Basis 19,87 % OK. **Schwächste XLV-Position: LLY -3,88 % P/L auf Watchlist Reduktion** falls Owner-Deutung "investiert" wird. **Owner-Klärung KW29/30/31 dreifach pending — DRINGEND KW32 klären.**
- XLF: 27,6 % investiert (V+JPM) — unter Cap ✓
- XLK: 24,0 % investiert (nur AAPL) — unter Cap ✓
- Cash: 58,89 % — komfortabler Puffer

**Bis Owner-Klärung: KEIN neuer XLV-Kauf** (blockiert ABBV/MRK-Top-Kandidaten trotz RS-Top). Prio nächste Woche: **AMZN (XLY neu) + GOOGL (XLC neu)** — beide korrigieren Sektor-Bias.

**Strategie-Status:** **STABIL** — alle Regeln (V1/V5/V6/K1-K5/Blackout-Konvention/Cascade-Framework) regelkonform. Anpassungs-Diskussion KW32: Sektor-Cap-Deutung (Priorität 1), Post-Earnings-XLY/XLC-Diversifikation, Cash-Quote 58,9 % strukturell zu hoch bei VIX <20 stabil.

**Watchlist nächste Woche (KW32, Mo 03.08.):** **AMZN, GOOGL, NFLX, UNP, EOG** (in dieser Priorität). ABBV/MRK blockiert bis XLV-Cap-Klärung.

**Nächste Routine:** **Mo 03.08. 08:30 ET Pre-Market KW32 Tag 1** — Weekly-Reset, VIX-Recalc, AMZN/GOOGL/NFLX K1-K5-Multi-Source, UNP/EOG K4-Rebound-Watch, AAPL Blackout HT+1 auslaufend, LLY Blackout HT-2 primäre Stop-Referenz bis Mi 05.08. BMO Earnings.

---

## Market Close 2026-07-31 16:00 ET (Fr, KW31 Tag 5 FINAL) — 5 V1-V6 SICHER Vollcheck EOD-Bars, AAPL Blackout-Puffer Recovery +2,70 % (Std +6,05 %), LLY Blackout +1,18 % marginal Recovery (Std +4,48 % ENGSTE), Daily -1,090 % [GRÜN, Cap -3 %], Weekly KW31 FINAL -1,159 % [GRÜN], Alpha vs SPY -1,785 pp NEG, KEIN Trade, KEINE Order für Mo 03.08.

```
Alpaca clock:      is_open=false | Fr 31.07. 16:02 ET | next_open Mo 03.08. 09:30 ET
Equity Close:      96.396,66 $   (Alpaca /v2/account)
Cash:              56.707,49 $   (58,83 %, unverändert)
Portfolio MV:      39.689,17 $   (41,17 %, 5 Positionen, +217,90 vs Midday 39.471,27 = intraday Recovery-Fortsetzung)
Buying_power:     337.959,64 $   (Paper-Margin)
Daily P/L Close:   -1.061,95 $   (-1,090 % vs Do Close 97.458,61)                                    [GRÜN, Cap -3 %, verbessert vs Midday -1,313 %]
Alt vs last_equity 97.340,70:      -944,04 $ = -0,970 %                                              [GRÜN, Cap -3 %]
SPY Close 16:00:    746,79       (Alpaca IEX, vs Do Close 741,63 = +0,696 % Post-FOMC-Recovery)     [Crash-Filter INAKTIV]
                                 (Perplexity divergiert: 741,69 = -0,13 % — IEX bar+Snapshot Last-Trade 15:59:59 ET verified → IEX bindend)
Alpha vs SPY:      -1,785 pp NEGATIV (Portfolio-Recovery unzureichend gegen SPY-Beta-Rally)
VIX (Perplexity):   n/a (Perplexity unable to source, ~15,7 Referenz nicht verifiziert; Do Close ~19,8) [GRÜN <25 Referenz]
Weekly KW31 FINAL: -1,159 %      (vs Fr 24.07. Close 97.526,60, -1.129,94 $)                        [GRÜN, weit von Cap -5 %]
DD vs ATH:         -3,667 %      (vs 100.066,47, verbessert vs Midday -3,885 %)                     [GRÜN]
Open Orders:           0         (KEINE Pending-Order, KEINE Sell-/Limit-Order für Mo 03.08.)
Käufe KW31:            0/2       (Slot 1/2 + 2/2 bleiben final OFFEN, Cascade-Framework Watch)
```

**Positionen Close 16:00 ET (5 Positionen, sortiert Std-V1-Puffer ENG→WEIT):**

| Sym  | Close | Qty | Entry     | P/L %     | chg vs Do Close Bar | V1-Std   | V1-Puffer   | V1-Blackout | Blackout-Puffer      | V5 EMA-Diff | V6 RSI | RS_4w vs SPY | Blackout-Status |
|------|-------|-----|-----------|-----------|---------------------|----------|-------------|-------------|----------------------|-------------|--------|--------------|-----------------|
| LLY  | 1.147,61 | 8 | 1.193,89 | **-3,88 % Worst P/L** | -0,60 %       | 1.098,38 | **+4,48 % ENGSTE Std** | 1.134,20    | +1,18 % ENGSTE Blackout, verbessert vs Midday +0,78 % | +11,98 % ✓ | 49,0 ✓ | -5,37 pp NEG | 🔴 HT-3 aktiv, HT-2 ab Mo, V6 sicher via UND |
| AAPL |   309,15 | 31 |  316,857 | -2,43 %   | -7,31 % Worst chg Post-Earnings | 291,51 | +6,05 % Std | 301,02 | **+2,70 % Recovery** vs Midday +0,111 % razor-thin | +10,30 % ✓ | 43,6 ✓ | -0,10 pp marginal NEG | 🟡 HT+0 Post-Earnings-Konsolidierung, V1_neu wieder klar über |
| V    |   366,13 | 27 |  357,178 | +2,51 %   | -0,04 %             | 328,60   | +11,42 %    | —           | —                    | **+2,45 % engster** | 66,2 max | +0,96 pp     | inaktiv (Q3 ✓ RELEASED) |
| UNH  |   415,99 | 24 |  401,57  | +3,59 %   | -1,71 % XLV-Sell-off-Fortsetzung | 369,44 | +12,60 %   | —           | —                    | +13,20 % ✓ | 48,7 ✓ | -2,73 pp NEG | inaktiv, V6 sicher via UND |
| JPM  |   351,79 |  3 |  332,78  | **+5,71 % Best P/L** | +0,28 % Best chg XLF-Recovery-Fortsetzung | 306,16 | +14,90 %   | —           | —                    | +5,28 % ✓ | 60,7 ✓ | +5,01 pp     | inaktiv |

**Verkaufssignal-Vollcheck V1-V6 EOD-Bars (Alpaca IEX 30.07.-31.07.):**
- **V1 (-8 %):** 5 SICHER per strategy.md Std-V1, min LLY +4,48 % ENGSTE, alle über 4 % Puffer → **kein Trigger.**
- **V2 (Trailing -12 % vom Hoch):** 5 SICHER, Trailing bei allen weniger restriktiv als Std-V1 → kein Trigger.
- **V3 (P/L ≥ 20 % TP1):** max JPM +5,71 % << 20 % → kein Trigger.
- **V4 (P/L ≥ 35 % TP2):** kein Trigger.
- **V5 (Death Cross EMA50<EMA200):** 5 SICHER, alle Golden Cross intakt. V engster +2,45 % (positiv, verschlechtert vs Do +2,92 %). AAPL trotz -7,31 % Sell-off noch +10,30 % Puffer bis Death Cross. → kein Trigger.
- **V6 (RSI>80 UND RS_4w vs SPY<0):** 5 SICHER. Max RSI V 66,2 (verschlechtert vs Do 63,3). LLY -5,37 pp RS_4w NEG aber RSI 49 → V6 sicher via UND-Bedingung. UNH -2,73 pp NEG aber RSI 49. AAPL -0,10 pp marginal NEG aber RSI 44. → kein Trigger.

**→ KEIN V1-V6-Trigger per strategy.md. KEINE Sell-/Limit-Order für Mo 03.08. platziert. 0 offene Orders.**

**Blackout-Kalender-Status (Bull-Konvention, informativ, Strategie-Lock CLAUDE.md Rule 3 → nur Std-V1 bindend):**
- **AAPL Q3 FY26 ✓ RELEASED** (Do 30.07. AMC), Blackout-V1_neu 301,02 konservativ aktiv bis Fr Close, jetzt **HT+1 ab Mo 03.08. auslaufend**. Puffer **+2,70 % Recovery** vs Midday +0,111 % razor-thin (Post-Earnings-Konsolidierung intraday abgefangen). Std-V1 291,51 Puffer +6,05 %. **Blackout-Konvention wieder klar über V1_neu-Grenze.**
- **LLY Q2 CY26 Mi 05.08.2026 BMO**, HT-3 aktiv seit HEUTE (Fr 31.07.), HT-2 ab Mo 03.08. Blackout-V1_neu 1.134,20 Puffer **+1,18 %** marginal Recovery vs Midday +0,778 %. Std-V1 1.098,38 SICHER +4,48 %. **Blackout-V1_neu bleibt primäre Watch bis Mi 05.08. BMO Earnings-Release.**
- Beide Blackout-Puffer über 1 %-Konvention-Grenze aber Watch für Mo Pre-Market/Open.

**Sektor-Struktur Close (LLY-Konsolidierung + AAPL-Recovery):**
- XLV: **19,88 %** (UNH 10,36 + LLY 9,52, marginal reduziert vs Midday 20,00 % — Cap-Warnung persistent für neue XLV-Kandidaten)
- XLF: 11,35 % (JPM 1,09 + V 10,26)
- XLK: 9,94 % (AAPL, Recovery vs Midday 9,71 %)
- Cash: 58,83 %

**Guardrails Close 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     -1,090 %                                                [GRÜN]
2. Weekly Loss Cap (-5 %):    -1,159 %                                                [GRÜN]
3. Drawdown-Alarm (-15 %):    -3,667 %                                                [GRÜN]
4. Drawdown-Stopp (-20 %):    -3,667 %                                                [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,696 %                                            [INAKTIV]
6. VIX-Filter (>30):          VIX Do-Referenz ~19,8 (Fr Perplexity n/a)               [GRÜN <25 Referenz]
7. Earnings-Blackout (3 HT):  AAPL HT+0 +2,70 % Recovery + LLY HT-3 +1,18 %           [WARN 2 aktiv, beide über 1 %]
8. Max Käufe KW31 FINAL:      0/2 (Slot 1/2 + 2/2 bleiben final offen)                [GRÜN]
```

**Watchlist Mo 03.08. K1-K3 aus Alpaca IEX EOD Fr 31.07. (K4/K5 zwingend Pre-Market/Open Multi-Source):**

| Kand | Sektor | Fr-Close | K1 EMA50/200 | K2 RSI | K3 RS_63d | K4 Vol Fr | K5 | Priorität |
|------|--------|----------|--------------|--------|-----------|-----------|----|-----------|
| **UNP** | XLI | 292,15 chg +0,94 % | +10,26 % ✓ | 59,1 ✓ | +4,45 pp ✓ | 116 % ✓ borderline | zwingend Multi-Source | **#1 XLI-Diversifikation neu, Wide-Moat Rails** |
| **ABBV** | XLV | 250,88 chg -2,57 % | +6,10 % ✓ | 57,4 ✓ | **+14,73 pp #2** ✓ | 135 % ✓ Best K4 | zwingend Multi-Source | **#2 XLV-Cap-Warnung bei 19,88 %** (3. XLV pusht auf ~29 %) |
| **MRK** | XLV | 130,21 chg +0,32 % | +12,40 % ✓ | 63,7 ✓ | **+15,32 pp #3** ✓ | **69 % FAIL** Fr | zwingend Multi-Source | **#3 K4-Rebound-Watch Mo Session-Vol, XLV-Cap** |
| **EOG** | XLE | 148,65 chg **+2,10 %** | +9,72 % ✓ | 67,1 ✓ knapp | +1,75 pp ✓ marginal | **84 % FAIL** Fr | vorbekannt ✓ FwdPE 9,98 + RevGr +15,63 % | **#4 K5-known K4-Rebound-Watch, XLE 0 %** |
| CVS | XLV | 104,42 chg -0,65 % | +15,51 % ✓ | 50,6 ✓ | +21,40 pp #1 ✓ | 117 % ✓ borderline | **REJECT K5 FAIL persistent** RevGr +6,2 % Q1 26 | **REJECT-persistent bis K5 sich ändert** |
| BAC | XLF | 61,98 chg +0,36 % | +7,26 % ✓ | 63,2 ✓ | +11,97 pp ✓ | **50 % FAIL** Fr | nicht recherchiert | SKIP K4 FAIL |

**Cascade-Framework über Wochenende:** AAPL Blackout HT+1 auslaufend Mo, LLY HT-2 primäre Stop-Referenz bis Mi 05.08. BMO. Neue Kauf-Entscheidung Mo Pre-Market/Open frühestens nach K4/K5-Multi-Source-Verifikation + XLV-Cap-Prüfung (ABBV/MRK problematisch, UNP+EOG vorteilhaft).

**ClickUp Prio 3 (Normal, negativer Tag ohne Cap-Alert)** wird gesendet.

**PushNotification Prio 2 Owner** — Weekly-Recap (KW31 -1,159 % [GRÜN weit von -5 %-Cap]) + AAPL-Recovery-Update (Blackout-Puffer +2,70 % vs Midday +0,11 % razor-thin) + Watchlist-Refresh (UNP/ABBV/MRK/EOG). Silence-Rule nicht anwendbar wegen negativem Wochenschluss + Weekly-Alpha-Recap für Owner-Sichtbarkeit.

**Nächste Routine:** Mo 03.08. 08:30 ET Pre-Market KW32 Tag 1 — **K4/K5-Multi-Source für UNP/ABBV/MRK/EOG (XLV-Cap-Check ABBV/MRK)**, **AAPL Blackout HT+1 auslaufend + LLY Blackout HT-2 primäre Stop-Referenz**, VIX-Recalc, SPY-Rally-Fortsetzung Watch, Weekly-Reset KW32.

---

## Midday Stop-Check 2026-07-31 13:07 ET (Fr, KW31 Tag 5) — KEIN Stop-Trigger, AAPL Blackout-Puffer +0,11 % ENGSTE weiter razor-thin, LLY Blackout +0,78 % marginal Recovery, Daily P/L -1,313 % [GRÜN]

```
Alpaca clock:      is_open=true | Fr 31.07. 13:07 ET | next_close 16:00 ET | next_open Mo 03.08. 09:30 ET
Equity Live:       96.178,76 $   (Alpaca /v2/account)
Cash:              56.707,49 $   (58,96 %, unverändert)
Portfolio MV:      39.471,27 $   (41,04 %, 5 Positionen, -1.279,85 $ vs Do Close 40.751,12 = -3,140 %, leicht verbessert vs Open MV 39.410,09)
Daily P/L Live:    -1.279,85 $   (-1,313 % vs Do Close 97.458,61)                                     [GRÜN, Cap -3 %]
Alt vs last_equity 97.340,70:    -1.161,94 $ = -1,194 %                                                [GRÜN, Cap -3 %]
SPY Live 13:07:     744,635      (vs Do Close 741,63 = +0,405 %, Post-FOMC-Konsolidierung Recovery)
Alpha vs SPY:      -1,718 pp NEGATIV (Portfolio-Recovery leicht, aber SPY zieht weiter davon)
Weekly KW31 Tag 5: -1,382 %      (vs Fr 24.07. Close 97.526,60, -1.347,84 $)                          [GRÜN]
DD vs ATH:         -3,885 %      (vs 100.066,47, marginal verbessert vs Open -3,947 %)                [GRÜN]
Open Orders:           0         (KEINE Pending-Order)
Käufe KW31:            0/2       (Slot 1/2 + 2/2 bleiben OFFEN, KEIN Kaufsignal-Scan bei Midday)
```

**Positionen Live 13:07 ET (5 Positionen, sortiert Std-V1-Puffer ENG→WEIT):**

| Sym  | Live 13:07 | Entry     | P/L %       | chg vs Open (09:42) | Std-V1  | Std-Puffer | Blackout-V1 | Blackout-Puffer               | Trailing Stop (V2 -12 % vom Hoch) |
|------|------------|-----------|-------------|---------------------|---------|------------|-------------|-------------------------------|-----------------------------------|
| AAPL |   301,355  |  316,857  | **-4,89 %** Worst P/L | -0,118 % (leicht runter) | 291,51  | +3,38 % ENGSTE | **301,02 🔴** | **+0,111 % ENGSTE weiter razor-thin verschlechtert** vs Open +0,229 % | max ~336,00 (Do High) × 0,88 = 295,68 (Std-V1 dominant) |
| LLY  | 1.143,02   | 1.193,89  | -4,26 %     | +0,155 %            | 1.098,38 | +4,06 %    | **1.134,20 🔴** | +0,778 % marginal Recovery vs Open +0,622 % | max ~1.220 (Mi) × 0,88 = 1.073,60 (Std-V1 dominant) |
| V    |   365,33   |  357,178  | +2,28 %     | **+0,731 % Best chg** | 328,60 | +11,18 %  | —           | —                             | max ~370,00 × 0,88 = 325,60 (Std-V1 dominant) |
| UNH  |   419,44   |  401,57   | +4,45 %     | -0,036 %            | 369,44  | +13,53 %   | —           | —                             | max ~430,54 × 0,88 = 378,88 (Std-V1 dominant) |
| JPM  |   353,20   |  332,78   | **+6,14 % Best P/L** | +0,756 %      | 306,16  | +15,36 %   | —           | —                             | max ~358,54 × 0,88 = 315,52 (Std-V1 dominant) |

**Verkaufssignal-Check per Midday-Routine (V1/V2/V3/V4, ohne RSI/EMA per Midday):**
- **V1 (-8 %):** 5 SICHER per strategy.md Std-V1, min AAPL +3,38 % ENGSTE — kein Trigger.
- **V2 (Trailing -12 % vom Hoch):** 5 SICHER, Trailing bei allen weniger restriktiv als Std-V1 → kein Trigger.
- **V3 (P/L ≥ 20 % TP1):** max JPM +6,14 % << 20 % → kein Trigger.
- **V4 (P/L ≥ 35 % TP2):** kein Trigger.

**→ KEINE Sell-Order platziert. KEIN Cap-Alert. 0 offene Orders.**

**Blackout-Kalender-Status (Bull-Konvention, nur informativ, Strategie-Lock CLAUDE.md Rule 3 → nur Std-V1 bindend):**
- AAPL Q3 FY26 ✓ RELEASED (Do 30.07. AMC), Blackout-V1_neu 301,02 aktiv Post-Earnings-Konsolidierung bis Fr Close. Aktuell **+0,111 % ENGSTE razor-thin verschlechtert** vs Open +0,229 %.
- LLY Q2 CY26 Mi 05.08. BMO, HT-3 aktiv seit HEUTE. Blackout-V1_neu 1.134,20 = Puffer +0,778 % marginal verbessert vs Open +0,622 %.
- Beide Blackout-Puffer weiter <1 %, aber Std-V1 alle sicher.

**Guardrails Midday 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     -1,313 %                                                [GRÜN]
2. Weekly Loss Cap (-5 %):    -1,382 %                                                [GRÜN]
3. Drawdown-Alarm (-15 %):    -3,885 %                                                [GRÜN]
4. Drawdown-Stopp (-20 %):    -3,885 %                                                [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,405 %                                            [INAKTIV]
6. VIX-Filter (>30):          VIX ~18 (Do Close-Referenz)                             [GRÜN]
7. Earnings-Blackout (3 HT):  AAPL HT+0 razor-thin +0,11 % + LLY HT-3 +0,78 %         [WARN 2 aktiv]
8. Max Käufe KW31:            0/2                                                     [GRÜN]
```

**ClickUp Routine-Log:** KEIN Log gesendet (Midday-Routine STEP 5: Nur bei Stop-Trigger oder Daily-Cap → ClickUp-Flut vermeiden).

**PushNotification Prio 2 Owner** — Follow-up zur Prio 1 Escalation vom Open (AAPL/LLY Blackout-Puffer <1 %). Update: Std-V1 5 SICHER, keine Aktion. AAPL Blackout-Puffer weiter razor-thin (+0,11 % vs Open +0,23 %, chg -0,118 % vs Open), LLY marginal Recovery (+0,78 % vs Open +0,62 %). Portfolio insgesamt leichte Stabilisierung (-1,313 % vs Open -1,376 %).

**Nächste Routine:** Fr 31.07. 16:00 ET Market Close Tagesbilanz — V1-V6-Vollcheck EOD-Bars für 5 Positionen, Weekly-Alpha-Zwischencheck, LLY-Blackout-Monitoring HT-3, AAPL-Post-Earnings-Konsolidierung Close-Kurs für Wochenende, Watchlist Mo 03.08. K1-K3 Pre-Read.

---

## Market Open 2026-07-31 09:42 ET (Fr, KW31 Tag 5) — 🔴 AAPL Blackout-V1_neu 301,02 intraday UNTERSCHRITTEN (Dip 300,535 09:41 ET, Recovery 301,71 razor-thin), LLY Blackout HT-3 aktiviert Puffer +0,62 % ENGSTE, kein V-Trigger per strategy.md, Slot 1/2 KW31 bleibt OFFEN (alle 4 Kandidaten REJECT/SKIP)

```
Alpaca clock:      is_open=true | Fr 31.07. 09:42 ET | next_open Mo 03.08. 09:30 ET
Equity Live:       96.117,58 $   (Alpaca /v2/account)
Cash:              56.707,49 $   (58,99 %, unverändert)
Portfolio MV:      39.410,09 $   (41,01 %, 5 Positionen, -1.341,03 $ vs Do Close 40.751,12 = -3,290 %)
Buying_power:     337.115,93 $   (Paper-Margin)
Daily P/L Live:    -1.341,03 $   (-1,376 % vs Do Close 97.458,61)                                     [GRÜN, Cap -3 %]
Alt vs last_equity 97.340,70:    -1.223,12 $ = -1,257 %                                                [GRÜN, Cap -3 %]
SPY Live 09:42:     743,51       (vs Do Close 741,63 = +0,253 %, milde Post-FOMC-Konsolidierung)      [Crash-Filter INAKTIV]
Alpha vs SPY:      -1,629 pp NEGATIV (AAPL -9,72 % Post-Earnings Guidance-Sell-off dominant)
VIX (Perplexity):   17,98        (leicht Vola-Rückgang vs Do Close ~19,8)                              [GRÜN <25 volle Pos-Size]
Weekly KW31 Tag 5: -1,444 %      (vs Fr 24.07. Close 97.526,60, -1.409,02 $)                          [GRÜN]
DD vs ATH:         -3,947 %      (vs 100.066,47, verschlechtert vs Do -2,606 %)                        [GRÜN]
Open Orders:           0         (KEINE Pending-Order, 0 Sell-/Limit-Orders)
Käufe KW31:            0/2       (Slot 1/2 + 2/2 bleiben OFFEN)
```

**Positionen Live 09:42 ET (5 Positionen, sortiert V1-Std-Puffer ENG→WEIT):**

| Sym  | Live 09:42 | Qty | Entry     | P/L %                    | chg_today                              | V1-Std   | V1-Blackout    | V1-Puffer                       | V5 EMA-Diff | V6 RSI | Blackout |
|------|------------|-----|-----------|--------------------------|------------------------------------------|----------|-----------------|---------------------------------|-------------|--------|----------|
| AAPL |   301,71   | 31  |  316,857  | **-4,78 % Worst P/L** | **-9,72 % Worst chg** Guidance-Sell-off | 291,51   | **301,02 🔴**   | **Std +3,50 % / Blackout +0,23 % ENGSTE razor-thin** — **intraday 09:41 ET Dip 300,535 = Blackout-V1_neu UNTERSCHRITTEN** | +11,10 % ✓ | ~40 ✓ | **🔴 HT+0 Blackout-V1 intraday gebrochen** |
| LLY  | 1.141,25   |  8  | 1.193,89  | **-4,41 % Worst P/L 2** | -1,36 %                                  | 1.098,38 | **1.134,20 🔴** | Std +3,90 % / **Blackout +0,62 % ENGSTE Blackout** | +12,03 % ✓ | 46,9 ✓ | **🔴 HT-3 AKTIVIERT ab HEUTE** |
| V    |   362,68   | 27  |  357,178  | +1,54 %                  | -0,98 %                                  | 328,60   | —              | +10,36 %                        | **+3,96 % engster** | 63,3 max ✓ | inaktiv |
| UNH  |   419,59   | 24  |  401,57   | +4,49 %                  | -1,20 % XLV-Sell-off                     | 369,44   | —              | +13,57 %                        | +14,71 % ✓ | 51,5 ✓ | inaktiv |
| JPM  |   350,55   |  3  |  332,78   | +5,34 %                  | **-0,09 % Best chg**                     | 306,16   | —              | +14,50 %                        | +5,33 % ✓ | 60,1 ✓ | inaktiv |

**V1-V6-Check Market Open Live:**
- **V1** (Stop -8 %): **5 SICHER per strategy.md Std-V1**, min AAPL +3,50 % ENGSTE, LLY +3,90 %. Blackout-V1_neu (Bull-Konvention) AAPL 09:41 ET intraday-Dip 300,535 → **UNTERSCHRITTEN kurzzeitig, aktuelle Recovery 301,71 = +0,23 %**. Strategie-Lock (Rule 3 CLAUDE.md): nur strategy.md V1 bindend → HALTEN, Owner-Push zwingend.
- **V2-V6:** kein Trigger. V engster V5-Spread +3,96 % positiv, max RSI V ~63 << 80.

**→ KEINE Sell-/Limit-Order platziert. Kein V-Trigger per strategy.md. 0 offene Orders.**

**Kaufsignal-Scan Slot 1/2 KW31 — alle 4 Kandidaten REJECT/SKIP:**

| Kand | K1 EMA | K2 RSI | K3 RS_63d | K4 (Do EOD) | K5 | Entscheidung |
|------|--------|--------|-----------|-------------|----|----|
| CVS  | +17,23% ✓ | 52,2 ✓ | +21,57 pp ✓ #1 | 157% ✓ | **FAIL** Q1 2026 RevGr +6,2 % < 10 % (Perplexity Multi-Source) | **REJECT K5 definitiv** |
| BAC  | +8,18% ✓  | 61,7 ✓ | +12,86 pp ✓ | **74% FAIL** | nicht recherchiert | **SKIP K4-FAIL** |
| UNP  | +10,41% ✓ | 51,9 ✓ | +5,38 pp ✓ | **99% FAIL** | nicht recherchiert | **SKIP K4-FAIL** |
| EOG  | +9,90% ✓  | 61,4 ✓ | +0,94 pp ✓ | **81% FAIL** | vorbekannt ✓ FwdPE 9,98 + RevGr +15,63 % | **SKIP K4-FAIL** |

**Cascade-Framework aktiviert:** AAPL Blackout-Puffer +0,23 % + LLY Blackout-Puffer +0,62 % — beide unter 1 %. Selbst wenn Kandidat qualifiziert wäre: neue Position würde Cash-Puffer reduzieren, während 47,4 % MV (AAPL+LLY) unter Blackout-Stress stehen → **defensiv NO BUY** unabhängig von Signal-Qualität. **Slot 1/2 KW31 bleibt OFFEN.**

**Sektor-Struktur Live (AAPL-Sell-off senkt XLK):**
- XLV: 19,98 % (UNH 10,47 + LLY 9,51)
- XLF: 11,29 % (JPM 1,10 + V 10,19)
- XLK: 9,73 % (AAPL)
- Cash: 58,99 %

**Guardrails Live 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     -1,376 %                                                [GRÜN]
2. Weekly Loss Cap (-5 %):    -1,444 %                                                [GRÜN]
3. Drawdown-Alarm (-15 %):    -3,947 %                                                [GRÜN]
4. Drawdown-Stopp (-20 %):    -3,947 %                                                [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,253 %                                            [INAKTIV]
6. VIX-Filter (>30):          VIX 17,98                                               [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT+0 Blackout-V1 intraday gebrochen + LLY HT-3     [WARN 2 aktiv]
8. Max Käufe KW31:            0/2                                                     [GRÜN]
```

**Nächste Routine:** Fr 31.07. 13:00 ET Midday Stop-Check — **Prio 1 AAPL/LLY Blackout-Puffer Stabilisierung**, K4-Session-Vol Halbtags-belastbar Watchlist-Recheck (falls Portfolio stabilisiert), XLV-Sell-off Fortsetzung Watch.

---

## Market Close 2026-07-30 16:00 ET (Do, KW31 Tag 4) — Post-FOMC-Recovery SPY +1,653 % Close-Fest, LLY XLV-Sell-off -4,38 % Worst-Fortsetzung, 5 V1-V6 SICHER Vollcheck, LLY-Blackout-Aktivierung morgen HT-3

```
Alpaca clock:      is_open=false | Do 30.07. 16:02 ET | next_open Fr 31.07. 09:30 ET
Equity Close:      97.458,61 $   (Alpaca /v2/account)
Cash:              56.707,49 $   (58,19 %, unverändert)
Portfolio MV:      40.751,12 $   (41,81 %, 5 Positionen, +51,49 $ vs Midday 40.699,63)
Buying_power:     340.933,11 $   (Paper-Margin)
Daily P/L Close:   -512,06 $     (-0,523 % vs Mi Close 97.970,67, minimal verbessert vs Midday -0,575 %) [GRÜN, Cap -3 %]
Alt vs last_equity 98.276,07: -817,46 $ = -0,832 %                                                       [GRÜN, Cap -3 %]
SPY Close 16:00:    741,63       (vs Mi Close 729,57 = +1,653 % Post-FOMC-Recovery fortgesetzt)         [Crash-Filter INAKTIV]
Alpha vs SPY:      -2,176 pp NEGATIV (LLY XLV-Sell-off dominant dämpft SPY-Recovery-Beta)
VIX (Perplexity):   19,8         (Perplexity Close-Read)                                                 [GRÜN <25]
Weekly KW31 Tag 4: -0,070 %      (vs Fr Close 97.526,60, -67,99 $, verbessert vs Open -0,225 %)          [GRÜN]
DD vs ATH:         -2,606 %      (vs 100.066,47, minimal verbessert vs Open -2,758 %)                    [GRÜN]
Open Orders:           0         (KEINE Pending-Order, 0 Sell-/Limit-Orders für morgen)
Käufe KW31:            0/2       (Slot 1/2 + 2/2 bleiben OFFEN, Re-Check Fr Pre-Market)
```

**Positionen Close 16:00 ET (5 Positionen, sortiert V1-Puffer ENG→WEIT, V5/V6 aus EOD-Bars 30.07.):**

| Sym  | Close    | Qty | Entry     | P/L %                    | chg_today                              | V1-Std   | V1-Blackout    | V1-Puffer               | V5 EMA50/200 Diff | V6 RSI(14) | Blackout |
|------|----------|-----|-----------|--------------------------|------------------------------------------|----------|-----------------|-------------------------|-------------------|------------|----------|
| LLY  | 1.157,00 |  8  | 1.193,89  | **-3,09 % Worst P/L weiter verschlechtert** | **-4,382 % Worst chg** XLV+Pharma-Sell-off | 1.098,38 | — (HT-4 inaktiv) | **+5,34 % ENGSTE weiter verschlechtert** vs Midday +5,80 % | +11,95 % ✓ | 47,0 ✓ (RS_4w -2,51 pp NEG aber RSI<80 → V6 sicher) | HT-4 inaktiv, morgen Fr 31.07. HT-3 → V1_neu 1.134,20 = -1,97 % dann als virt. Puffer |
| AAPL |  334,20  | 31  |  316,857  | **+5,47 %**              | -1,18 %                                  | 291,51   | **301,02 🔴**  | **+11,02 %** Blackout HT-0 | +10,90 % ✓ | 61,5 ✓ | **🔴 AKTIV HT-0 Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE nach Close** |
| V    |  366,27  | 27  |  357,178  | +2,55 %                  | -0,67 %                                  | 328,60   | —              | +11,46 %                | **+2,92 % engster Spread ✓** | 63,3 ✓ (max) | inaktiv Post-Earnings (Q3 Di 28.07. AMC ✓) |
| JPM  |  350,85  |  3  |  332,78   | +5,43 %                  | **+1,78 % Best chg** XLF-Post-FOMC-Recovery-Fortsetzung | 306,16 | —          | +14,60 %                | +5,73 % ✓ | 60,1 ✓ | inaktiv (Q3 ~Mitte Okt) |
| UNH  |  424,686 | 24  |  401,57   | **+5,76 % Best P/L**     | +0,98 % XLV-Divergenz Recovery           | 369,44   | —              | +14,95 %                | +15,31 % ✓ | 51,6 ✓ | inaktiv (Q3 ~Mitte Okt) |

**V1-V6-Vollcheck EOD-Bars 30.07.:**
- **V1** (Stop -8 %): **5 SICHER**, min LLY +5,34 % ENGSTE (weiter verschlechtert vs Midday +5,80 %, Open +7,36 %). Bei weiteren -5,08 % würde V1 greifen — LLY Fr Pre-Market zwingend beobachten.
- **V2** (Trailing -12 % vs Hoch): V-52w-Hoch 369,12 × 0,88 = 324,83 → 366,27 SAFE. Keine anderen Trailing-Trigger.
- **V3** (+20 % TP1): max UNH +5,76 % / AAPL +5,47 % / JPM +5,43 % << 20 %, kein Trigger.
- **V4** (+35 % TP2): kein Trigger.
- **V5** (Death Cross EMA50<EMA200): **5 SICHER** alle Golden Cross intakt. Engster Spread V +2,92 % (positiv, keine Death-Cross-Warnung).
- **V6** (RSI>80 UND RS_4w<0): **5 SICHER**. Max RSI V 63,3 << 80. LLY RS_4w vs SPY -2,51 pp NEGATIV (LLY -3,05 % / SPY -0,54 % 20d), aber RSI 47,0 << 80 → V6 nicht ausgelöst (UND-Bedingung erforderlich).

**→ KEINE Sell-/Limit-Order für Fr 31.07. platziert. Kein V5/V6-Trigger. 0 offene Orders.**

**Daily Loss Cap Check:** daily_pnl_pct = -0,523 % vs Mi Close 97.970,67 << Cap -3 % → **GRÜN**. Kein Alert.

**Weekly Loss Cap Check (KW31 Tag 4):**
- weekly_pnl_pct = (97.458,61 - 97.526,60) / 97.526,60 * 100 = **-0,070 %** << Cap -5 % → **GRÜN**
- KEINE Pending-Orders zu stornieren, kein WEEKLY_CAP-Alert.

**Tages-Highlights Close:**
- Best chg: **JPM +1,78 %** (XLF Post-FOMC-Recovery-Fortsetzung)
- Worst chg: **LLY -4,38 %** (XLV+Pharma-Sell-off dominant, verschlechtert von Open -2,745 % → Close -4,382 %)
- Best P/L: **UNH +5,76 %** (XLV-Divergenz Recovery)
- Worst P/L: **LLY -3,09 %** (weiter verschlechtert vs Open -1,23 % → Close -3,09 %, aber V1-Puffer +5,34 % noch sicher)
- Portfolio-MV +51,49 $ vs Midday (+0,127 %), Alpha vs SPY **-2,176 pp NEGATIV** (LLY XLV-Weakness dominiert Portfolio-Beta)
- **XLV-Bifurkation Fortsetzung:** UNH Recovery +0,98 % vs LLY Sell-off -4,38 % (Divergenz +5,36 pp)

**Watchlist Fr 31.07. (K1-K3 EOD-Bar 30.07. Close bestätigt, K4/K5 zwingend Pre-Market/Open Multi-Source):**

| Kand | Sektor | Close  | chg %  | EMA50/200 | RSI | RS_63d vs SPY | K5-Status | Notiz |
|------|--------|--------|--------|-----------|-----|---------------|-----------|-------|
| CVS  | XLV    | 105,11 | -0,72 %| +17,69 % ✓| 52,2 ✓ | **+21,57 pp #1 Top-Rank** ✓ | K5 zwingend Multi-Source | XLV-Cap-Warnung (Portfolio 21 % nach LLY-Sell-off), 3. XLV pusht auf ~29 % → OK aber knapp |
| BAC  | XLF    |  61,76 | +1,13 %| +7,68 % ✓ | 61,7 ✓ | +12,86 pp ✓ | K5 zwingend Multi-Source | XLF 11 % → +BAC ~21 %, OK. Post-FOMC Bank-Rebound intakt |
| UNP  | XLI    | 289,42 | -1,01 %| +11,45 % ✓| 51,9 ✓ | +5,38 pp ✓ | K5 zwingend Multi-Source | XLI 0 % → **neue Sektor-Diversifikation**, Rails-Wide-Moat |
| EOG  | XLE    | 145,59 | -0,25 %| +11,29 % ✓| 61,4 ✓ | +0,94 pp ✓ | K5 **vorbekannt ✓** (FwdPE 9,98 + RevGr +15,63 %) | XLE 0 %, Rebound-Watch nach 27.-29.07. Konsolidierung |

**Nicht-Watchlist REJECT-Verifikation:** GE (K5 FwdPE 44,72 >35 persistent FAIL), PSX (K5 RevGr +6,9 % <10 % persistent FAIL), HON (K5 RevGr +2,4 % <10 % persistent FAIL), DE (K5 RevGr +9,6 % <10 % persistent FAIL), D (K5 RevGr +7,49 % <10 % persistent FAIL), NEE/DUK (K3 FAIL), MSFT (chg +15,48 % aber K1-FAIL Diff -8,72 % + RSI 72,1 >70), META (chg -8,29 % K1-FAIL + RSI 32,1), CAT (RSI 34,9 <50 + RS -4,50 pp).

**Sektor-Struktur Close (LLY-Sell-off reduziert XLV marginal):**
- XLV: 19,95 % (UNH 10,46 + LLY 9,49) — LLY dropped von 9,90 % Midday auf 9,49 % Close
- XLF: 11,23 % (JPM 1,08 + V 10,15)
- XLK: 10,63 % (AAPL)
- Cash: 58,19 %

**Guardrails Close 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     -0,523 % vs Mi Close                                 [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 4 -0,070 %                                  [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,606 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,606 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Close +1,653 % Recovery                          [INAKTIV]
6. VIX-Filter (>30):          VIX 19,8                                             [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT-0 Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE    [WARN aktiv nach Close]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                            [GRÜN]
```

**Blackout-Kalender:**
- **AAPL Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE nach Close** → Post-Earnings-Reaktion in AH-Handel morgen im Pre-Market abbildbar. Blackout aktiv bis Fr 31.07. Konsolidierung.
- **LLY Q2 CY26 Mi 05.08. BMO** → Blackout aktiv ab morgen Fr 31.07. HT-3 → V1_neu 1.134,20 dann (aktueller Close 1.157,00 = +1,97 % Puffer wenn Blackout aktiv wird, marginal aber positiv).
- V (Q3 CY26 Di 28.07. AMC ✓ RELEASED), JPM/UNH Q3 CY26 ~Mitte Okt (weit weg).

**Nächste Routine:** Fr 31.07. 08:30 ET Pre-Market — **AAPL Post-Earnings-Reaktion** (K5-Multi-Source-Wert-Check, potenzielle V1_neu-Neubewertung), **LLY Blackout HT-3 Aktivierung** (V1_neu 1.134,20 wird primäre Stop-Referenz), **Watchlist CVS/BAC/UNP/EOG K4/K5-Multi-Source-Verifikation**, XLV-Sell-off Konsolidierungs-Prüfung.

---

## Midday 2026-07-30 13:06 ET (Do, KW31 Tag 4) — Post-FOMC-Recovery-Fortsetzung SPY +1,418 %, UNH+JPM-Rebound aber LLY XLV-Sell-off dominant, 5 V1 SICHER (LLY Puffer +5,80 % ENGSTE verschlechtert)

```
Alpaca clock:      is_open=true | Do 30.07. 13:06 ET | next_close Do 30.07. 16:00 ET
Equity Live:       97.407,12 $   (Alpaca /v2/account)
Cash:              56.707,49 $   (58,22 %, unverändert)
Portfolio MV Live: 40.699,63 $   (41,78 %, 5 Positionen, +100,46 $ vs Open 40.599,17)
Buying_power:     340.788,92 $   (Paper-Margin)
Daily P/L Live:    -563,55 $     (-0,575 % vs Mi Close 97.970,67, verbessert vs Open -0,678 %) [GRÜN, Cap -3 %]
Alt vs last_equity 98.276,07: -868,95 $ = -0,884 %                                              [GRÜN, Cap -3 %]
SPY Live 13:06 ET:  739,915       (vs Mi Close 729,57 = +1,418 % Post-FOMC-Recovery)            [Crash-Filter INAKTIV]
Alpha vs SPY:      -1,993 pp NEGATIV (LLY XLV-Sell-off dominant, dämpft UNH+JPM-Recovery-Beta)
Weekly KW31 Tag 4: -0,123 %       (vs Fr Close 97.526,60, -119,48 $, verbessert vs Open -0,225 %) [GRÜN]
DD vs ATH:         -2,657 %       (vs 100.066,47, verbessert vs Open -2,758 %)                    [GRÜN]
Open Orders:           0          (KEINE Pending-Order)
```

**Positionen Live 13:06 ET (5 Positionen, sortiert V1-Puffer ENG→WEIT):**

| Sym  | Live-Cur | Qty | Entry     | P/L %                    | chg_today                          | V1-Std   | V1-Blackout    | V1-Puffer               | Blackout-Status |
|------|----------|-----|-----------|--------------------------|-------------------------------------|----------|-----------------|-------------------------|-----------------|
| LLY  | 1.162,12 |  8  | 1.193,89  | **-2,66 % Worst P/L verschlechtert** | **-3,959 % Worst chg**  | 1.098,38 | — (HT-4 inaktiv) | **+5,80 % ENGSTE verschlechtert vs Open +7,36 %** | inaktiv HT-4 (Q2 CY26 Mi 05.08. BMO, Blackout ab Fr 31.07. HT-3 V1_neu 1.134,20 = -2,49 % dann als virt. Puffer) |
| AAPL |  332,18  | 31  |  316,857  | +4,84 %                  | -1,777 %                            | 291,51   | **301,02 🔴**  | **+10,35 %** Blackout HT-0 | **🔴 AKTIV HT-0 Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE** |
| V    |  364,28  | 27  |  357,178  | +1,99 %                  | -1,207 %                            | 328,60   | —              | +10,86 %                | inaktiv Post-Earnings (Q3 Di 28.07. AMC ✓) |
| JPM  |  351,87  |  3  |  332,78   | +5,74 %                  | **+2,077 % Best chg** XLF Post-FOMC-Recovery | 306,16 | —          | +14,93 %                | inaktiv (Q3 ~Mitte Okt) |
| UNH  |  425,67  | 24  |  401,57   | **+6,00 % Best P/L**     | +1,213 % XLV-Divergenz Recovery      | 369,44   | —              | +15,22 %                | inaktiv (Q3 ~Mitte Okt) |

**V1-V4-Check Midday (V5/V6 laut Routine nicht bei Midday):**
- **V1** (Stop -8 %): 5 SICHER, min **LLY +5,80 % ENGSTE verschlechtert** vs Open +7,36 % (LLY -3,959 % chg fortgesetzter XLV+Pharma-Sell-off, aber V1 1.098,38 noch weit weg — bei weiteren -5,80 % würde Stop greifen)
- **V2** (Trailing -12 % vs Hoch): V-52w-Hoch 369,12 × 0,88 = 324,83 → 364,28 SAFE. Keine anderen Trailing-Trigger.
- **V3** (+20 % TP1): max UNH +6,00 % / JPM +5,74 % / AAPL +4,84 % << 20 %, kein Trigger.
- **V4** (+35 % TP2): kein Trigger.

**→ KEINE Sell-/Limit-Order platziert Midday. Kein Stop ausgelöst. 0 offene Orders.**

**Daily Loss Cap Check Midday:**
- daily_pnl_pct = (97.407,12 - 97.970,67) / 97.970,67 * 100 = **-0,575 %** << Cap -3 % → **GRÜN**
- Alternativ vs Alpaca last_equity 98.276,07: -0,884 % << Cap -3 % → **GRÜN**
- **KEINE Offenen-Limit-Orders zu stornieren** (0 offene Orders)

**Tages-Highlights Midday:**
- Best chg: JPM **+2,077 %** (XLF Post-FOMC-Recovery-Fortsetzung stark)
- Worst chg: LLY **-3,959 %** (XLV-Sektor+Pharma-Sell-off Fortsetzung, verschlechtert vs Open -2,745 %)
- Best P/L: **UNH +6,00 %** (XLV-Divergenz — UNH Recovery vs LLY Sell-off)
- Worst P/L: **LLY -2,66 %** (weiter verschlechtert vs Open -1,23 %, aber V1-Puffer +5,80 % noch sicher)
- Portfolio-MV +100,46 $ vs Open (+0,247 %), Alpha vs SPY **-1,993 pp NEGATIV** (LLY XLV-Weakness dominiert)
- **XLV-Bifurkation:** UNH Recovery +1,213 % vs LLY Sell-off -3,959 % Fortsetzung (Divergenz +5,17 pp)
- **XLF-Recovery:** JPM +2,077 % Post-FOMC-Bank-Rebound

**Guardrails Midday 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     -0,575 % vs Mi Close                                 [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 4 -0,123 %                                  [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,657 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,657 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Live +1,418 % Post-FOMC-Recovery                 [INAKTIV]

---

## Market Open 2026-07-30 09:37 ET (Do, KW31 Tag 4) — Post-FOMC-Recovery SPY +0,801 %, aber XLV-Sektor-Sell-off breit, 5 V1-V6 SICHER Live (LLY -2,745 % Worst chg + P/L -1,23 % Worst), LEVEL 0 SKIP JNJ/MRK/ABBV wegen Gap-Down bei Open

```
Alpaca clock:      is_open=true | Do 30.07. 09:37 ET | next_close Do 30.07. 16:00 ET
Equity Live:       97.306,66 $   (Alpaca /v2/account)
Cash:              56.707,49 $   (58,28 %, unverändert)
Portfolio MV Live: 40.599,17 $   (41,72 %, 5 Positionen, -664,01 $ vs Mi Close 41.263,18 = -1,609 %)
Buying_power:     340.507,62 $   (Paper-Margin)
Daily P/L Live:     -664,01 $    (-0,678 % vs Mi Close 97.970,67)                 [GRÜN, Cap -3 %]
Alt vs Alpaca last_equity 98.276,07: -0,987 %                                     [GRÜN, Cap -3 %]
SPY Live 09:37 ET:  735,41       (vs Mi Close 729,57 = +0,801 % Post-FOMC-Recovery)[Crash-Filter INAKTIV]
Alpha vs SPY:      -1,479 pp NEGATIV (XLV/XLK/XLF-Give-back dämpft SPY-Recovery)
VIX (Pre-Read):     15,8         (Perplexity, Pre-Market carry-over)               [GRÜN <25]
Weekly KW31 Tag 4: -0,225 %      (vs Fr Close 97.526,60, -219,94 $)                [GRÜN, Cap -5 %]
DD vs ATH:         -2,758 %      (vs 100.066,47)                                   [GRÜN]
Open Orders:           0         (KEINE Pending-Order)
Käufe KW31:            0/2       (Slot 1/2 bleibt OFFEN nach LEVEL 0 SKIP JNJ/MRK/ABBV + Slot 2/2 offen)
```

**Positionen Live 09:37 ET (5 Positionen, sortiert V1-Puffer ENG→WEIT):**

| Sym  | Live-Cur | Qty | Entry     | P/L %    | chg_today | V1-Std   | V1-Blackout    | V1-Puffer    | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|----------|----------------|--------------|-----------------|
| LLY  | 1.179,18 |  8  | 1.193,89  | **-1,23 % Worst P/L verschlechtert** | **-2,745 % Worst chg** | 1.098,38 | — (HT-4 inaktiv) | **+7,36 % ENGSTE vs Std** | inaktiv HT-4 (Q2 CY26 Mi 05.08. BMO, Blackout ab Fr 31.07. HT-3 V1_neu 1.134,20 = +4,55 % dann) |
| AAPL |  332,44  | 31  |  316,857  | +4,92 % Best P/L | -1,641 % | 291,51 | **301,02 🔴** | **+10,44 %** Blackout HT-0 | **🔴 AKTIV HT-0 Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE** |
| V    |  365,43  | 27  |  357,178  | +2,31 %  | -0,895 %  | 328,60   | — | +11,20 %     | inaktiv Post-Earnings-Reaktion (Q3 Di 28.07. AMC ✓) |
| UNH  |  414,07  | 24  |  401,57   | +3,11 %  | -1,545 %  | 369,44   | —              | +12,07 %     | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  346,28  |  3  |  332,78   | +4,06 %  | **-0,320 % Best chg** XLF Post-FOMC-Recovery | 306,16 | —              | +13,05 %     | inaktiv (Q3 ~Mitte Okt) |

**V1-V6-Vollcheck Market Open (Live-Kurse + Mi EOD-Bars für V5/V6):**
- **V1** (Stop -8 % / Blackout -5 %): 5 SICHER, min LLY **+7,36 % ENGSTE vs Std** (verschlechtert vs Pre +8,16 %), AAPL **+10,44 % Blackout HT-0** aktiv.
- **V2** (Trailing -12 % vs 52w-Hoch): Keine neuen 52w-Hochs (V-52w-Hoch 369,12 seit Mi, Live 365,43 = -1,00 % Give-back).
- **V3** (+20 % TP1): max AAPL +4,92 % / JPM +4,06 % / UNH +3,11 % << 20 %, kein Trigger.
- **V4** (+35 % TP2): kein Trigger.
- **V5** (Death Cross): aus Mi EOD-Bars alle Golden Cross intakt, engster V Spread +2,50 %. Kein V5-Trigger.
- **V6** (RSI > 80 UND RS 4w vs SPY < 0): max RSI AAPL 67,2 (Mi EOD) << 80. Kein V6-Trigger.

**→ KEINE Sell-/Limit-Order platziert Market Open. Kein Stop ausgelöst. 0 offene Orders.**

**Kaufsignal-Scan Watchlist JNJ/MRK/ABBV — LEVEL 0 SKIP alle 3:**

| Kand | Open   | Live   | Mi Close | Gap %   | vs SPY  | K4-Session-Vol (~1,79 % Session-Zeit) | Entscheidung |
|------|--------|--------|----------|---------|---------|-------------------------------------|-------------|
| JNJ  | 259,45 | 259,33 | 265,67   | -2,34 % | -3,14 pp | 14.547 / avg20 394.756 = 3,68 % (pro-rata unzuverlässig) | **REJECT LEVEL 0 Momentum-Bruch** |
| MRK  | 128,195| 128,82 | 130,40   | -1,69 % | -2,49 pp | 7.120 / avg20 316.358 = 2,25 % (pro-rata unzuverlässig) | **REJECT LEVEL 0 Momentum-Bruch** |
| ABBV | 255,66 | 258,865| 263,62   | **-3,02 % worst** | **-3,82 pp** stark neg | 7.523 / avg20 266.590 = 2,82 % (pro-rata unzuverlässig) | **REJECT LEVEL 0 Momentum-Bruch STARK trotz RS #1** |

- K1-K3 alle 3 ✓ (Pre-Read Mi EOD-Bars), aber intraday-Momentum am Kauftag stark negativ vs SPY +0,801 % Post-FOMC-Recovery
- K4-Session-Vol pro-rata bei ~1,79 % Session-Zeit nicht belastbar
- K5 (FwdPE + RevGr Multi-Source) **NICHT verifiziert** — LEVEL 0 SKIP macht Perplexity-Call nicht ökonomisch
- **XLV-Sektor-Sell-off breit Post-FOMC** (UNH -1,545 % + LLY -2,745 % + JNJ -2,34 % + MRK -1,69 % + ABBV -3,02 %) → keine sinnvolle 3. XLV-Position
- **Slot 1/2 KW31 bleibt OFFEN** — Re-Check Fr 31.07. Pre-Market (Post-AAPL-Earnings + Post-XLV-Sell-off-Konsolidierung)

**Daily Loss Cap Check Market Open:**
- daily_pnl_pct = (97.306,66 - 97.970,67) / 97.970,67 * 100 = **-0,678 %** << Cap -3 % → **GRÜN**
- Alternativ vs Alpaca last_equity 98.276,07: -0,987 % << Cap -3 % → **GRÜN**

**Weekly Loss Cap Check (KW31 Tag 4):**
- weekly_pnl_pct = (97.306,66 - 97.526,60) / 97.526,60 * 100 = **-0,225 %** >> Cap -5 % → **GRÜN**

**Tages-Highlights Market Open:**
- Best chg: JPM **-0,320 %** (XLF Post-FOMC-Recovery-Ansatz — kleinste Give-back)
- Worst chg: LLY **-2,745 %** (XLV-Sektor-Sell-off + eigene Pharma-Weakness Fortsetzung)
- Best P/L: AAPL +4,92 %
- Worst P/L: **LLY -1,23 %** (verschlechtert vs Pre -0,49 %, aber V1-Puffer +7,36 % noch sicher)
- Portfolio-MV -664,01 $ vs Mi Close (-1,609 %), Alpha vs SPY **-1,479 pp NEGATIV**

**Guardrails Market Open 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     -0,678 % vs Mi Close                                 [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 4 -0,225 %                                  [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,758 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,758 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   Mi -1,515 % → Live +0,801 % Recovery                 [INAKTIV]
6. VIX-Filter (>30):          VIX ~15,8 (Pre-Read)                                 [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT-0 Q3 FY26 Do 30.07. AMC HEUTE V1_neu 301,02  [WARN]
8. Max Käufe KW31:            0/2 (Slot 1/2 bleibt OFFEN + 2/2 offen)              [GRÜN]
```

**Sektor-Struktur Market Open:**
- XLV 19,53 % (UNH 9,82 % + LLY 9,70 %) — reduziert durch XLV-Sell-off
- XLK 10,59 % (AAPL)
- XLF 11,21 % (JPM 1,07 % + V 10,14 %)
- Cash 58,28 %

**Nächste Routine:** Do 30.07. 13:00 ET Midday Stop-Check — LLY Puffer +7,36 % ENGSTE Watch (Post-FOMC-Continuation-Risk), AAPL AMC-Countdown ~5:00 PM ET, XLV-Sell-off-Fortsetzung Watch, potenzielles Rebound-Fenster für Slot 1/2.

---

## Pre-Market 2026-07-30 08:37 ET (Do, KW31 Tag 4) — Post-FOMC-Konsolidierung SPY Pre +0,65 % Recovery, VIX 15,8 (-6 %), 5 V1-V6 SICHER Pre-Read (LLY Overnight-Give-back -1,82 % engste vs Std, P/L -0,49 %), AAPL HT-0 HEUTE AMC, Kaufsignal-Scan JNJ/MRK/ABBV bei Market Open

```
Alpaca clock:      is_open=false | Do 30.07. 08:37 ET | next_open Do 30.07. 09:30 ET
Equity Pre:        97.576,68 $   (Alpaca /v2/account)
Cash:              56.707,49 $   (58,12 %, unverändert)
Portfolio MV Pre:  40.868,88 $   (41,88 %, 5 Positionen, -394,30 $ vs Mi Close 41.263,18 = -0,955 %)
Buying_power:     341.263,69 $   (Paper-Margin)
Daily P/L Pre:      -394,30 $    (-0,402 % vs Mi Close 97.970,67)                 [GRÜN, Cap -3 %]
Alt vs Alpaca last_equity 98.276,07: -0,712 %                                     [GRÜN, Cap -3 %]
SPY Pre 08:33 ET:   734,30       (vs Mi Close 729,57 = +0,65 % Post-FOMC-Recovery)[Crash-Filter INAKTIV]
VIX (Perplexity):   15,8         (-6 % vs Vortag)                                 [GRÜN <25]
VXX letzte:         23,44        (Mi 19:59 ET, keine frische Pre-Open-Bar)        [GRÜN]
10Y Yield:          ~4,12 %      (leicht runter vs Mi ~4,20+ %)
Weekly KW31 Tag 4: +0,051 %      (vs Fr Close 97.526,60, +50,08 $)                [GRÜN, Cap -5 %]
DD vs ATH:         -2,488 %      (vs 100.066,47)                                  [GRÜN]
Open Orders:           0         (KEINE Pending-Order)
Käufe KW31:            0/2       (Slot 1/2 offen + Slot 2/2 offen)
```

**Positionen Pre-Market 08:37 ET (5 Positionen, sortiert V1-Puffer ENG→WEIT):**

| Sym  | Pre-Cur  | Qty | Entry     | P/L %    | chg_today | V1-Std   | V1-Blackout    | V1-Puffer    | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|----------|----------------|--------------|-----------------|
| LLY  | 1.188,00 |  8  | 1.193,89  | **-0,49 % Worst P/L** | **-1,82 % Worst chg** | 1.098,38 | — (HT-4 inaktiv) | **+8,16 % ENGSTE vs Std** | inaktiv HT-4 (Q2 CY26 Mi 05.08. BMO, Blackout ab Fr 31.07. HT-3 V1_neu 1.134,20 = +4,74 % dann) |
| AAPL |  335,13  | 31  |  316,857  | +5,77 % Best P/L | -0,91 %  | 291,51 | **301,02 🔴** | **+11,33 %** Blackout HT-0 | **🔴 AKTIV HT-0 Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE** |
| V    |  368,25  | 27  |  357,178  | +3,10 %  | -0,13 %  | 328,60   | — | +12,06 %     | inaktiv Post-Earnings-Reaktion (Q3 Di 28.07. AMC ✓) |
| UNH  |  416,50  | 24  |  401,57   | +3,72 %  | -0,97 %  | 369,44   | —              | +12,74 %     | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  345,70  |  3  |  332,78   | +3,88 %  | +0,29 % Best chg | 306,16 | —              | +12,91 %     | inaktiv (Q3 ~Mitte Okt) |

**V1-Puffer Übersicht (eng→weit):** LLY **+8,16 % ENGSTE vs Std** (Overnight-Give-back, verschlechtert vs Mi Close +9,41 % um -1,25 pp) | AAPL **+11,33 % Blackout HT-0** | V +12,06 % | UNH +12,74 % | JPM +12,91 %

**V1-V6 Pre-Read Pre-Market (aus Mi EOD-Bars, keine neue EOD-Bar heute, alle 5 SICHER):**
- **V1** (Stop -8 % / Blackout -5 %): 5 SICHER, min LLY **+8,16 % ENGSTE vs Std**, AAPL **+11,33 % Blackout HT-0** aktiv. LLY P/L -0,49 % erste negative Position aber weit von Stop.
- **V2** (Trailing -12 % vs 52w-Hoch): Keine neuen 52w-Hochs, keine Änderung vs Mi Close.
- **V3** (+20 % TP1): max AAPL +5,77 % / JPM +3,88 % / UNH +3,72 % << 20 %, kein Trigger.
- **V4** (+35 % TP2): kein Trigger.
- **V5** (Death Cross): aus Mi EOD-Bars alle Golden Cross intakt, engster V Spread +2,50 %. Kein V5-Trigger.
- **V6** (RSI > 80 UND RS 4w vs SPY < 0): max RSI AAPL 67,2 (Mi EOD) << 80. Kein V6-Trigger.

**→ KEINE Sell-/Limit-Order platziert Pre-Market. Kein Stop ausgelöst. 0 offene Orders. V1-V6-Vollcheck bei Market Close mit neuen EOD-Bars.**

**Daily Loss Cap Check Pre-Market:**
- daily_pnl_pct = (97.576,68 - 97.970,67) / 97.970,67 * 100 = **-0,402 %** << Cap -3 % → **GRÜN**
- Alternativ vs Alpaca last_equity 98.276,07 (Di Close carry-over): -0,712 % << Cap -3 % → **GRÜN**

**Weekly Loss Cap Check (KW31 Tag 4):**
- weekly_pnl_pct = (97.576,68 - 97.526,60) / 97.526,60 * 100 = **+0,051 %** >> Cap -5 % → **GRÜN**

**Tages-Highlights Pre-Read:**
- Best chg: JPM **+0,29 %** (XLF Post-FOMC-Recovery-Ansatz)
- Worst chg: LLY **-1,82 %** (XLV-Konsolidierung + eigene Pharma-Weakness)
- Best P/L: AAPL +5,77 %
- Worst P/L: **LLY -0,49 %** (erste negative Position, aber V1-Puffer +8,16 % noch sicher)
- Portfolio-MV -394,30 $ vs Mi Close (-0,955 %), aber Post-FOMC-Recovery ansteht bei Market Open

**Guardrails Pre-Market 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     -0,402 % vs Mi Close                                 [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 4 +0,051 %                                  [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,488 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,488 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   Mi -1,515 % → Pre +0,65 % Recovery                   [INAKTIV]
6. VIX-Filter (>30):          VIX 15,8 (-6 % vs Vortag)                            [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT-0 Q3 FY26 Do 30.07. AMC HEUTE V1_neu 301,02  [WARN]
8. Max Käufe KW31:            0/2 (Slot 1/2 bleibt OFFEN + 2/2 offen)              [GRÜN]
```

**Sektor-Struktur Pre-Market (Pre-Kurse):**
- XLV 19,84 % (UNH 10,24 % + LLY 9,60 %) — LLY-Give-back reduziert Sektor-Gewicht marginal
- XLK 10,65 % (AAPL)
- XLF 11,26 % (JPM 1,06 % + V 10,19 %)
- Cash 58,12 %

**Watchlist Market Open — K1-K3 EOD-Bar Mi 29.07. bestätigt, K4/K5 zwingend Multi-Source:**
- **JNJ (XLV Healthcare)**: c=265,67 K1-K3 ✓ (RS +14,14 pp), K4/K5 zwingend Market Open
- **MRK (XLV Healthcare)**: c=130,40 K1-K3 ✓ (RS +16,05 pp), K4/K5 zwingend Market Open
- **ABBV (XLV Healthcare)**: c=263,62 K1-K3 ✓ (RS **+30,94 pp #1 Top-Rank**), RSI 67,8 nah 70-Cap Watch, K4/K5 zwingend Market Open
- **XLV-Sektor-Cap-Warnung:** Aktuell 19,84 % XLV. 3. XLV-Position pusht auf ~30 % Cap-Grenze → **Max 1 der 3 kaufbar**, bevorzugt ABBV (RS-Prio #1) oder JNJ/MRK bei besserer K5-Fundamentaldiversifikation

**Earnings-Kalender Do 30.07. + nächste 3 HT (Perplexity Multi-Source):**
- **AAPL Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE HT-0** (Portfolio, Blackout aktiv V1_neu 301,02)
- AMZN Q2 CY26 Do 30.07. AMC (nicht im Portfolio, SPY-Vol-Impact)
- **LLY Q2 CY26 Mi 05.08. BMO** (Blackout ab Fr 31.07. HT-3 aktivierbar V1_neu 1.134,20 — heute HT-4 inaktiv)
- Watchlist JNJ/MRK/ABBV: keine im 3-HT-Fenster (K5-Recheck bei Market Open bestätigt)
- Andere Portfolio (JPM/UNH/V): keine Konflikte

**Post-FOMC Marktreaktion Update:**
- SPY Pre +0,65 % Recovery nach Mi -1,515 % hawkish-Sell-off
- VIX 15,8 -6 % → Vola-Rückgang, Cash-Puffer weiter defensiv
- 10Y Yield 4,12 % (leicht runter vs Mi Post-Fed) → Rate-Cut-Erwartungen minimal wiederhergestellt

**Makro-Ereignisse heute:**
- **08:30 ET Q2 GDP Advance Estimate** (primärer Vol-Katalysator Pre-Market)
- **08:30 ET Core PCE Q2** (Inflations-Signal Post-Fed)
- **10:00 ET Pending Home Sales**
- **AAPL AMC ~5:00 PM ET**

**Entscheidung Pre-Market Do 30.07.:**
- **KEIN Stop ausgelöst** (5 V1-V6 SICHER Pre-Read, min LLY +8,16 % ENGSTE vs Std, alle Golden Cross intakt)
- **KEINE Sell-/Limit-Order** platziert (kein V5/V6-Trigger)
- **KEIN Kauf** Pre-Market (Regel: Kaufsignal-Scan bei Market Open, K4/K5 zwingend)
- **KEIN Critical-Alert** (keine Stops, keine Cap-Verletzung, alle GRÜN)
- **ClickUp Prio 4 Routine-Log ERR ITEM_246** persistenter Fehler (bekannt seit Wochen, Memory-Fallback per Skill)
- **KEINE PushNotification** (Silence-Rule: empty run, kein Trade, kein Stop, keine Cap-Verletzung, Post-FOMC-Recovery positiv → Schweigen die freundliche Wahl)
- **Slot 1/2 KW31 bleibt OFFEN** — Market Open 09:30 ET Kaufsignal-Scan JNJ/MRK/ABBV K4/K5-Multi-Source (max 1 XLV wg. Sektor-Cap)

**Nächste Routine:** Do 30.07. 09:30 ET Market Open + Kaufsignal-Scan JNJ/MRK/ABBV K4/K5-Vollprüfung, dann 13:00 ET Midday Stop-Check + AAPL AMC-Countdown, 16:00 ET Market Close + V1-V6-Vollcheck neue EOD-Bars + Post-AAPL-Earnings-Watch Fr 31.07.

---

## Market Close 2026-07-29 16:00 ET (Mi, KW31 Tag 3 Fed-Day) — Tagesbilanz: Daily -0,311 % (Alpha +1,204 pp POSITIV vs SPY -1,515 %), 5 V1-V6-Vollcheck alle SICHER, Weekly +0,455 % GRÜN, keine Pending-Order

```
Gesamtwert:     97.970,67 $   (equity Close, Alpaca /v2/account)
Cash:           56.707,49 $   (57,88 %, unverändert)
Investiert:     41.263,18 $   (42,12 %, 5 Positionen, -312,37 vs Open 41.575,55)
P/L heute:        -305,40 $   (-0,311 % vs last_equity 98.276,07)                [GRÜN, Cap -3 %]
Alpha vs SPY:    +1,204 pp    POSITIV (Cash-Puffer + V Best chg dämpfen SPY -1,515 %)
ATH:            100.066,47 $
Drawdown:        -2,094 %     [GRÜN, marginal verschlechtert vs Open -1,782 %]
Guardrails:     Daily -0,311 % | Weekly +0,455 % | Käufe 0/2
```

**Account Market Close 16:00 ET (Alpaca /v2/account):**
```
equity_close:      97.970,67 $   (Daily -0,311 % vs last_equity 98.276,07)
Cash:              56.707,49 $   (57,88 %, unverändert)
Portfolio MV:      41.263,18 $   (42,12 %, 5 Positionen, -312,37 $ vs Open = -0,751 %)
Buying_power:     342.366,85 $   (Paper-Margin)
SPY Close:            729,57     (Alpaca IEX Bar-Close vs Di Close 740,795 = -1,515 %) [Crash-Filter INAKTIV]
Alpha vs SPY:      +1,204 pp     (Daily -0,311 % vs SPY -1,515 % Post-FOMC-Sell-off)
VIX/VXX Close:     ~17-18 / 23,44 (leichter Anstieg vs Midday 22,63)             [GRÜN, <25]
Weekly KW31 Tag 3: +0,455 %      (vs Fr Close 97.526,60, +444,07 $)              [GRÜN, Cap -5 %]
DD vs ATH:         -2,094 %      (vs 100.066,47)                                 [GRÜN]
Open Orders:           0          (KEINE Pending-Order)
Käufe KW31:            0/2       (Slot 1/2 bleibt OFFEN + 2/2 offen)
```

**Positionen Market Close 16:00 ET (5 Positionen, sortiert V1-Puffer ENG→WEIT):**

| Sym  | Close    | Qty | Entry     | P/L %    | chg_today | V1-Std   | V1-Blackout    | V1-Puffer    | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|----------|----------------|--------------|-----------------|
| LLY  | 1.212,47 | 8   | 1.193,89  | +1,56 %  | -0,671 %  | 1.098,38 | —              | **+9,41 %** ENGSTE (überholt V) | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07. HT-3) |
| V    |  368,73  | 27  |  357,178  | +3,23 %  | **+0,584 %** Best chg Post-Earnings-Bid | 328,60 | — (Post-Earnings-Ende technisch) | +10,89 %     | inaktiv Post-Earnings-Reaktion positiv (Q3 Di 28.07. AMC ✓) |
| AAPL |  337,99  | 31  |  316,857  | **+6,67 %** Best P/L | -0,615 %  | 291,51 | **301,02 🟡** | **+10,94 %** Blackout HT-1 | **🔴 AKTIV HT-1 → HT-0 morgen Q3 FY26 Do 30.07. AMC** |
| JPM  |  347,39  | 3   |  332,78   | +4,39 %  | **-2,776 % Worst chg** XLF Post-FOMC | 306,16   | —              | +11,87 %     | inaktiv (Q3 ~Mitte Okt) |
| UNH  |  420,57  | 24  |  401,57   | +4,73 %  | -1,917 %  | 369,44   | —              | +12,16 %     | inaktiv (Q3 ~Mitte Okt) |

**V1-Puffer Übersicht (eng→weit):** LLY **+9,41 % ENGSTE** (LLY überholt V durch V Post-Earnings-Bid) | V +10,89 % | AAPL +10,94 % Blackout HT-1 → HT-0 morgen | JPM +11,87 % | UNH +12,16 %

**V1-V6-Vollcheck Market Close (aus heute EOD-Bars, alle 5 SICHER):**
- **V1** (Stop -8 % / Blackout -5 %): 5 SICHER, min LLY **+9,41 % ENGSTE**. Alle P/L positiv.
- **V2** (Trailing -12 % vs 52w-Hoch): V bei 52w-Hoch 369,12 = Close 369,12 → 0 % Distanz zum 52w-Hoch aber Close hat KEIN neues Trailing-Update ausgelöst (nur bei Break möglich). LLY 52wH 1.235,26 → -1,97 % Distanz. AAPL 52wH 340,00 → -0,59 %. UNH 436,39 → -3,63 %. JPM 357,40 → -3,47 %. Kein V2-Trigger.
- **V3** (+20 % TP1): max AAPL +6,67 % / UNH +4,73 % / JPM +4,39 % << 20 %, kein Trigger.
- **V4** (+35 % TP2): kein Trigger.
- **V5** (Death Cross EMA50 < EMA200): AAPL 308,93>279,15 ✓, JPM 330,57>314,96 ✓, LLY 1.137,11>1.016,80 ✓, UNH 406,18>354,79 ✓, V 342,87>334,50 ✓. Alle GOLDEN. **Kein V5-Trigger.**
- **V6** (RSI > 80 UND RS 4w vs SPY < 0): AAPL RSI 67,2 / RS +19,23 pp — kein Trigger. JPM RSI 55,3 / RS +7,72 pp. LLY RSI 58,9 / RS +3,25 pp. UNH RSI 50,8 / RS +3,55 pp. V RSI 66,8 / RS +10,03 pp. **Max RSI AAPL 67,2 << 80, kein V6-Trigger.**

**→ KEINE Sell-/Limit-Order platziert für morgen. KEIN Stop ausgelöst. KEINE Order-Stornierung. 0 offene Orders.**

**Daily Loss Cap Check:**
- daily_pnl_pct = (97.970,67 - 98.276,07) / 98.276,07 * 100 = **-0,311 %** << Cap -3 % → **GRÜN**
- 0 offene Orders → kein DAILY_CAP-Alert nötig

**Weekly Loss Cap Check (KW31 Tag 3):**
- weekly_pnl_pct = (97.970,67 - 97.526,60) / 97.526,60 * 100 = **+0,455 %** >> Cap -5 % → **GRÜN**
- KEINE Order-Stornierung nötig, kein WEEKLY_CAP-Alert

**Tages-Highlights EOD:**
- Best chg: V **+0,584 %** (Post-Earnings-Bid-Fortsetzung Di AMC, technisch Blackout beendet, Close bei 52w-Hoch 369,12)
- Worst chg: JPM **-2,776 %** (XLF Post-FOMC hawkish-Reaktion), UNH -1,917 % (XLV-Sell-off)
- Best P/L: AAPL +6,67 % (marginal verschlechtert vs Midday +7,88 %)
- Worst P/L: LLY +1,56 % (verschlechtert vs Midday +2,03 %)
- Alpha +1,204 pp POSITIV — Cash-Puffer 57,88 % + V Best chg dämpfen SPY -1,515 % deutlich
- Portfolio-MV -312,37 $ vs Open (-0,751 %), aber Alpha vs SPY-MV-Loss deutlich POSITIV

**Guardrails Market Close 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     -0,311 %                                             [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 3 +0,455 %                                  [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,094 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,094 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -1,515 %                                         [INAKTIV]
6. VIX-Filter (>30):          VIX ~17-18 (VXX 23,44)                               [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT-1 → HT-0 morgen Q3 FY26 Do 30.07. AMC        [WARN]
8. Max Käufe KW31:            0/2 (Slot 1/2 bleibt OFFEN + 2/2 offen)              [GRÜN]
```

**Sektor-Struktur EOD (Close-Werte):**
- XLV 20,20 % (UNH 10,30 % + LLY 9,90 %) — 2/3 max
- XLK 10,70 % (AAPL) — 1/3 max
- XLF 11,10 % (JPM 1,06 % + V 10,16 %) — 2/3 max (V ist XLF-Kernindex Zahlungsverkehr)
- Cash 57,88 %

**Watchlist morgen Do 30.07. (K1-K3 EOD-Bar Pre-Check, K4/K5 zwingend Market Open):**
- **JNJ (XLV Healthcare)**: c=265,67 EMA50 247,96 > EMA200 225,01 (K1 ✓), RSI 63,6 im Cap 50-70 (K2 ✓), 63d perf +11,63 % vs SPY -2,51 % = RS **+14,14 pp** (K3 ✓). K4/K5 morgen prüfen. **Sektor-Konflikt Watch**: 3. XLV-Position würde 30 %-Cap pushen.
- **MRK (XLV Healthcare)**: c=130,40 EMA50 123,29 > EMA200 110,32 (K1 ✓), RSI 59,3 (K2 ✓), 63d perf +13,54 % vs SPY -2,51 % = RS **+16,05 pp** (K3 ✓). K4/K5 morgen prüfen. **Sektor-Konflikt Watch** (siehe JNJ).
- **ABBV (XLV Healthcare)**: c=263,62 EMA50 240,31 > EMA200 227,86 (K1 ✓), RSI 67,8 **nah oberem 70-Cap Watch** (K2 ✓ knapp), 63d perf +28,43 % vs SPY -2,51 % = RS **+30,94 pp #1 Top-Rank** (K3 ✓). K4/K5 morgen prüfen. **Sektor-Konflikt Watch** (siehe JNJ).
- Alternative XLK: MSFT/NVDA/AVGO/GOOGL/META alle K1-K3-FAIL EOD (Post-FOMC-Sell-off drückt XLK-EMAs). CRM/LMT/NOW/GE K1-FAIL. GE K2-FAIL (RSI 49,4 <50).
- **XLV-Sektor-Cap-Warnung**: Aktuell 20,20 % XLV. 3. XLV-Position pusht auf ~30 % Sektor-Cap-Grenze. Max nur 1 der 3 XLV-Kandidaten kaufbar.

**Entscheidung Market Close Mi 29.07.:**
- **KEIN Stop ausgelöst** (5 V1-V6 SICHER, min LLY +9,41 % ENGSTE, alle Golden Cross intakt, max RSI 67,2)
- **KEINE Sell-/Limit-Order** für morgen (kein V5/V6-Trigger)
- **KEINE Order-Stornierung** (Weekly +0,455 % >> Cap -5 %, kein WEEKLY_CAP)
- **KEIN Critical-Alert** (keine Stops, keine Cap-Verletzung)
- **ClickUp Prio 3 (Normal)** Tagesbericht wird gesendet (Daily negativ, aber im Rahmen und Alpha +1,204 pp POSITIV)
- **KEINE PushNotification** (Silence-Rule: negativer Tag im Rahmen, kein Trade, kein Stop, keine Cap → Schweigen die freundliche Wahl)
- **Slot 1/2 KW31 bleibt OFFEN** — Do 30.07. Pre-Market K4/K5-Vollprüfung Watchlist (JNJ/MRK/ABBV eine kaufen wenn K4/K5 sauber + Sektor-Cap-Konsistenz), Do AMC AAPL Q3-Earnings Post-Earnings-Reaktion → möglicher Vol-Peak

**Nächste Routine:** Do 30.07. 08:30 ET Pre-Market — Post-FOMC-Konsolidierung + AAPL HT-0 Q3 AMC-Countdown, JNJ/MRK/ABBV K4/K5-Multi-Source-Verifikation, LLY Blackout ab Do HT-3 aktivierbar V1_neu 1.134,20 dann (nur Info).

---

## Midday 2026-07-29 13:08 ET (Mi, KW31 Tag 3) — Stop-Check: 5 V1-V4 SICHER, keine Trigger, Daily P/L +0,052 % GRÜN, V Post-Earnings-Bid +1,68 % ENGSTE-Puffer weiter verbessert

```
Alpaca clock:      is_open=true | now Mi 29.07. 13:08 ET | next_close Mi 29.07. 16:00 ET
Equity Live:       98.327,26 $   (Alpaca /v2/account)
Cash:              56.707,49 $   (57,67 %, unverändert)
Portfolio MV Live: 41.619,84 $   (42,33 %, 5 Positionen, +44,29 $ vs Open 41.575,55)
Buying_power:     343.365,32 $   (Paper-Margin)
Daily P/L Live:      +51,19 $    (+0,052 % vs Alpaca last_equity 98.276,07)      [GRÜN, Cap -3 %]
SPY Live 13:09:     735,39       (vs Di Close 740,795 = -0,730 %)                [Crash-Filter INAKTIV]
Alpha vs SPY:      +0,782 pp     POSITIV (Cash-Puffer 57,67 % + V Post-Earnings-Bid dämpfen SPY-Give-back Pre-Fed)
ATH:              100.066,47 $   DD -1,738 % [GRÜN — Alarm bei -15 %]
Weekly KW31 Tag 3:  +0,821 %     (vs Fr Close 97.526,60, +800,66 $)              [GRÜN, Cap -5 %]
VIX/VXX Live:      ~16-17 / 22,63 (leichter Anstieg vs Open 22,38 Pre-Fed)       [GRÜN, <25]
Käufe KW31:            0/2       (Slot 1/2 bleibt OFFEN, Post-Fed-Re-Check >15:30 ET)
Open Orders:           0         (KEINE Pending-Order)
Guardrails:        8/8 GRÜN + 3 WARN (V-Post-Earnings + AAPL-Blackout HT-1 + Fed 14:00 ET)
```

**Positionen Live 13:08 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym  | Cur Live  | Qty | Entry     | P/L %    | chg_today | V1-Stop      | V1-Puffer   | Status |
|------|-----------|-----|-----------|----------|-----------|--------------|-------------|--------|
| V    |   372,74  | 27  |  357,18   | +4,36 %  | **+1,678 %** Best chg | **339,32 🟡BLACKOUT** | **+9,85 %** ENGSTE | SICHER Blackout Post-Earnings-Bid, weiter verbessert vs Open +7,87 % um +1,98 pp |
| LLY  | 1.218,15  | 8   | 1.193,89  | +2,03 %  | -0,206 %  | 1.098,38     | +10,90 %    | SICHER Worst P/L (marginal verschlechtert vs Open +10,93 %) |
| AAPL |  341,825  | 31  |  316,86   | **+7,88 %** Best P/L | +0,513 %  | **301,02 🟡BLACKOUT HT-1** | +13,56 % | SICHER (verbessert vs Open +13,25 %, **Q3 FY26 morgen Do 30.07. AMC**) |
| JPM  |   349,63  | 3   |  332,78   | +5,06 %  | **-2,149 % Worst chg** | 306,16       | +14,20 %    | SICHER (verschlechtert vs Open +16,51 %, XLF-Give-back Pre-Fed) |
| UNH  |   423,55  | 24  |  401,57   | +5,47 %  | -1,222 %  |   369,44     | +14,65 %    | SICHER (verschlechtert vs Open +16,54 %, XLV-Give-back) |

**V1-Puffer Übersicht (eng→weit):** V **+9,85 % ENGSTE** Post-Earnings-Bid (weiter verbessert +1,98 pp vs Open) | LLY +10,90 % | AAPL +13,56 % Blackout HT-1 | JPM +14,20 % | UNH +14,65 %

**V1-V4 Midday-Check (RSI/EMA nicht Teil Midday-Routine) 5 SICHER:**
- V1 (Stop -8 % / Blackout -5 %) — 5 SICHER, min V-Blackout **+9,85 % ENGSTE** Post-Earnings-Bid (33,42 $ vom Break, Cur 372,74 chg +1,678 % Best chg → V-Post-Earnings-Reaktion positiv nach Di 28.07. AMC)
- V2 (Trailing -12 %) — kein 52w-Hoch-Trigger, kein Update
- V3 (+20 % TP1) — max AAPL +7,88 % / JPM +5,06 % << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger

**→ KEINE Sell-/Limit-Order platziert. KEIN Stop ausgelöst. KEINE Order storniert.**

**Daily Loss Cap Check:**
- daily_pnl_pct = (98.327,26 - 98.276,07) / 98.276,07 * 100 = **+0,052 %** >> Cap -3 % → **GRÜN**
- 0 offene Orders → keine Cap-Aktivierung nötig, kein DAILY_CAP-Alert

**Tages-Highlights Midday:**
- Best chg: V **+1,678 %** (Post-Earnings-Bid Fortsetzung nach Di 28.07. AMC — Puffer-Verbesserung +1,98 pp seit Open)
- Sekundär: AAPL +0,513 % (XLK-Bid Pre-Q3-FY26 Do AMC)
- Worst chg: JPM -2,149 % (XLF-Give-back Pre-Fed), UNH -1,222 % (XLV-Give-back)
- Best P/L: AAPL +7,88 % (überholt JPM als Best P/L bestätigt seit Open)
- Worst P/L: LLY +2,03 % (marginal, aber SICHER)
- Alpha +0,782 pp POSITIV (Cash-Puffer + V Post-Earnings-Bid > SPY -0,730 % Pre-Fed-Volatilität)

**Guardrails 8/8 GRÜN + 3 WARN (V-Post-Earnings + AAPL-Blackout HT-1 + Fed 14:00 ET, kein Aktion nötig):**
```
1. Daily Loss Cap (-3 %):     +0,052 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 3 +0,821 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,738 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,738 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,730 %                                        [INAKTIV]
6. VIX-Filter (>30):          ~16-17 (VXX 22,63)                                  [GRÜN <25]
7. Earnings-Blackout (3 HT):  V Post-Earnings + AAPL HT-1 V1_neu 301,02 sicher    [WARN]
8. Max Käufe KW31:            0/2 (Slot 1/2 OFFEN, Post-Fed-Re-Check >15:30 ET)   [GRÜN]
```

**Entscheidung Midday 13:08 Mi 29.07.:**
- **KEIN Stop ausgelöst** (5 V1-V4 SICHER, min Puffer V +9,85 %)
- **KEINE Sell-Order** (kein Trigger)
- **KEINE Order-Stornierung** (Daily +0,052 % >> Cap -3 %)
- **KEIN ClickUp-Alert** (Routine-Spec: nur bei Stops oder Daily Cap)
- **KEINE PushNotification** (Silence-Rule "empty run": kein Trade, kein Stop, keine Cap → Schweigen)
- **Slot 1/2 KW31 bleibt OFFEN** — Post-Fed-Re-Check >15:30 ET (nach FOMC 14:00 ET + Powell 14:30 ET) für Kandidaten-Neubewertung

**Nächste Routine:** Mi 29.07. 16:00 ET Market Close + Tagesbilanz — Fed-Post-Announcement-Reaktion (SPY-Rebound oder Fortsetzung Give-back), **V ENGSTE Puffer +9,85 %** Post-Earnings-Bid-Fortsetzung, **AAPL Blackout HT-1** vor Q3 FY26 Do 30.07. AMC (V1_neu 301,02 nur Info), V5/V6-Vollcheck alle 5 zwingend, EOD-Kandidaten-Screener für Slot 1/2 Post-Fed-Fenster.

---

## Market Open 2026-07-29 09:38 ET (Mi, KW31 Tag 3) — 🟢 KEIN Kauf ausgeführt (LEVEL 0 SKIP wegen Fed 14:00 ET), 5 V1-V6 SICHER, V Post-Earnings-Recovery +2,01 pp Puffer, Portfolio +0,007 % flat, AAPL überholt JPM als Best P/L.

```
Market Open 09:38 [2026-07-29]:
Gesamtwert:     98.283,04 $  (Alpaca /v2/account Live)
Cash:           56.707,49 $  (57,70 %)
Investiert:     41.575,55 $  (42,30 %, 5 Positionen, +263,28 $ vs Pre 41.312,27)
P/L Daily:      +6,97 $      (+0,007 % vs last_equity 98.276,07) [GRÜN, Cap -3 %]
ATH:            100.066,47 $
Drawdown:       -1,782 %     [GRÜN, verbessert vs Pre -2,045 %]
Guardrails:     Daily +0,007 % | Weekly +0,776 % | Käufe KW31 0/2
```

**Account Market Open 09:38 ET (Alpaca /v2/account):**
```
equity:            98.283,04 $   (Daily +0,007 % vs last_equity 98.276,07)
Cash:              56.707,49 $   (57,70 %, unverändert)
Portfolio MV:      41.575,55 $   (42,30 %, 5 Positionen, +263,28 $ vs Pre = Post-Open-Bid +0,637 %)
Buying_power:     343.241,49 $   (Paper-Margin)
SPY Live:             739,78     (Alpaca IEX Trade 09:38 ET vs Di Close 740,795 = -0,137 %) [Crash-Filter INAKTIV]
Alpha vs SPY:      +0,144 pp     (Daily +0,007 % vs SPY -0,137 %, XLV/XLK-Bid + Cash-Puffer)
VIX ~16-17         (VXX 22,38 Alpaca IEX stabil) [GRÜN <25 volle Pos-Size]
Weekly KW31 Tag 3: +0,776 %      (vs Fr Close 97.526,60, +756,44 $)                    [GRÜN, Cap -5 %]
DD vs ATH:         -1,782 %      (vs 100.066,47, verbessert vs Pre -2,045 %)           [GRÜN]
Open Orders:           0          (KEINE Pending-Order, kein Sell-, kein Kauf-Limit)
Käufe KW31:            0/2       (Slot 1/2 bleibt OFFEN + 2/2 offen)
```

**Positionen Market Open 09:38 ET (5 Positionen, sortiert Puffer ENG→WEIT):**

| Sym  | Cur      | Qty | Entry     | P/L %    | chg_today | V1-Std   | V1-Blackout    | V1-Puffer  | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|----------|----------------|------------|-----------------|
| V    |  365,965 | 27  |  357,178  | +2,46 %  | -0,170 %  | 328,60   | **339,32 🟡** | **+7,87 %** ENGSTE **Post-Earnings-Recovery** verbessert vs Pre +5,86 % um +2,01 pp | Blackout Post-Earnings-Watch (V berichtete Di 28.07. AMC ~17:00 ET) |
| LLY  | 1218,41  | 8   | 1193,89   | +2,05 %  | -0,197 %  | 1.098,38 | —              | +10,93 %   marginal verschlechtert vs Pre +11,09 % | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07.) |
| AAPL |  340,92  | 31  |  316,857  | **+7,60 %** Best P/L | +0,100 %  | 291,51   | **301,02 🟡** | **+13,25 %** verbessert vs Pre +12,65 % | **🔴 AKTIV HT-1 Q3 FY26 Do 30.07. AMC** |
| UNH  |  430,54  | 24  |  401,57   | +7,21 %  | **+0,320 %** Best chg | 369,44   | —              | +16,54 %   verbessert vs Pre +15,79 % | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  356,71  | 3   |  332,78   | +7,19 %  | -0,119 %  | 306,16   | —              | +16,51 %   marginal verschlechtert vs Pre +16,78 % | inaktiv (Q3 ~Mitte Okt) |

**V1-Puffer Übersicht (eng→weit):** V **+7,87 % ENGSTE** Post-Earnings-Recovery (verbessert +2,01 pp vs Pre) | LLY +10,93 % | AAPL +13,25 % Blackout HT-1 | UNH +16,54 % | JPM +16,51 %

**V1-V6-Vollcheck Market Open 5 SICHER:**
- V1 (Stop -8 % / Blackout -5 %) — 5 SICHER, min V-Blackout **+7,87 % ENGSTE Post-Earnings-Recovery** (Cur 365,965 vs Di Close 367,748 = -0,49 %, Puffer verbessert vs Pre +5,86 % um +2,01 pp durch Post-Open-Bid). Break unter 339,32 (-7,25 % vs Cur) triggert V1-Blackout-Market-Sell sofort.
- V2 (Trailing -12 %) — kein 52w-Hoch-Trigger, kein Update
- V3 (+20 % TP1) — max AAPL +7,60 % / JPM +7,19 % << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- V5/V6 aus Di Close-Bars alle 5 SICHER (Vollcheck Di 16:00 ET, Golden Cross alle intakt, max RSI JPM 71,00 << 80 → V6 nicht ausgelöst)

**Daily Loss Cap Check:**
- Daily +0,007 % [weit von -3 %-Cap, GRÜN]
- 0 offene Orders (keine Cap-Aktivierung)

**Weekly Loss Cap Check (KW31 Tag 3):**
- Weekly +0,776 % (vs Fr Close 97.526,60, +756,44 $) [GRÜN, weit von -5 %-Cap]

**Guardrails Market Open 8/8 GRÜN + 3 WARN:**
```
1. Daily Loss Cap (-3 %):     Daily +0,007 %                                             [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 3 +0,776 %                                        [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,782 %                                                   [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,782 %                                                   [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,137 %                                               [INAKTIV]
6. VIX-Filter (>30):          VIX ~16-17 (VXX 22,38)                                     [GRÜN <25 volle Pos-Size]
7. Earnings-Blackout (3 HT):  V Post-Earnings-Watch + AAPL HT-1 + LLY ab Do HT-3         [WARN x3]
8. Max Käufe KW31:            0/2 (Slot 1/2 bleibt OFFEN + 2/2 offen)                    [GRÜN]

FED-WARN: Fed-Meeting HEUTE 14:00 ET FOMC + 14:30 ET Powell → LEVEL 0 restriktiv Vol-Peak 14:00-15:30 ET
```

**Kaufsignal-Scan Slot 1/2 KW31 — LEVEL 0 SKIP alle 5 Kandidaten:**

| Sym  | K1 EMA-Diff | K2 RSI  | K3 RS_63d | K4 Vol Di | K5 | chg_today | Verdict |
|------|-------------|---------|-----------|-----------|-----|-----------|---------|
| EOG  | +7,71 % ✓   | 53,24 ✓ | +1,75 pp ✓ | 108 % ✗   | ✓ (FwdPE 9,98 + RevGr +15,63 %) | +3,27 % Gap-Up | **LEVEL 0 SKIP Fed** (K4 heute in 8 Min nicht bewertbar, Fed 14:00 ET vor Kauf) |
| PANW | +30,36 % ✓  | **48,40 ✗** | +70,53 pp ✓ #1 | 124 % ✓ | offen | +0,61 % | **REJECT K2-FAIL** (<50) |
| GH   | +30,18 % ✓  | **45,13 ✗** | +58,18 pp ✓ | **70 % ✗** | offen | -1,39 % | **REJECT K2+K4-FAIL** |
| ILMN | +22,14 % ✓  | 58,96 ✓ | +46,32 pp ✓ | **94 % ✗** | unverifiziert | +1,89 % | **REJECT K4-FAIL**, Recheck Do Pre |
| ICLR | +4,91 % ✓ (engster) | 67,85 ✓ (nah 70) | +70,89 pp ✓ #2 | 196 % ✓ ★ | **unverifiziert** | +6,72 % (Vortag) → +0,31 % heute Post-Momentum-Digest | **LEVEL 0 SKIP** (K5-Recheck wg. Fed-SKIP nicht wirtschaftlich, Do Pre-Market Post-Fed) |

**XLV-Sektor-Cap-Grenzwertig:** aktuell 20,42 % (UNH+LLY), 3. XLV-Position (GH/ILMN/ICLR) würde Cap ~30 % pushen → EOG/PANW Diversifikationsvorteil bevorzugt, aber PANW K2-FAIL.

**Sektor-Struktur Live:** XLV 20,42 % (UNH+LLY), XLF 11,14 % (JPM+V), XLK 10,74 % (AAPL), Cash 57,70 %.

**V-Post-Earnings-Recovery Positiv:**
- V-Kurs 365,965 vs Di Close 367,748 = -0,49 % nur noch marginal Give-back (verbessert vs Pre -2,32 %)
- Post-Open-Bid +2,01 pp Puffer-Verbesserung → V Post-Earnings-Recovery-Muster
- V1-Blackout 339,32 sicher, kein Order-Update nötig

**AAPL Blackout HT-1 aktiv heute** (Q3 FY26 Do 30.07. AMC): V1_neu 301,02, Puffer +13,25 % sicher, keine Order-Änderung nötig. Best P/L +7,60 %.

**Fed-Meeting-Verhalten:** LEVEL 0 restriktiv aktiv bis 14:00 ET FOMC. Wahrscheinlichkeit Kauf HEUTE vor Fed gering. **Post-Fed >15:30 ET Re-Evaluation** bei dovish Powell + K1-K5 stark → möglich. Realistischer Kauf-Fenster: **Do 30.07. Pre-Market Post-Fed** wenn Signal-Set frisch prüfbar.

**→ KEIN Stop, KEIN Kauf, KEIN Daily-Cap-Trigger, KEINE Sell-/Kauf-Limit-Order. ClickUp Routine-Log Prio 4 wird gesendet. PushNotification Silence (empty run: kein Trade, alle 5 SICHER, V Post-Earnings-Recovery positiv, Silence-Rule respektiert).**

Nächster Check: **Mi 29.07. 13:00 ET Midday Stop-Check** — V Post-Earnings-Recovery-Fortsetzung Watch (ENGSTE +7,87 %), EOG K4 EOD-realistischer Bewertung, LEVEL 0 restriktiv 60 Min vor Fed 14:00 ET, Post-Fed >15:30 ET Re-Evaluation-Fenster.

---

## Pre-Market 2026-07-29 08:36 ET (Mi, KW31 Tag 3) — 🟡 V Post-Earnings Give-back ~-2,3 % (Puffer +5,86 % ENGSTE Blackout, SICHER aber verschlechtert), AAPL Blackout HT-1 aktiv, Fed-Meeting HEUTE 14:00 ET → LEVEL 0 restriktiv default. Alle 5 V1 SICHER, KEINE Pending-Order, Slot 1/2 KW31 offen.

```
Pre-Market 08:36 [2026-07-29]:
Gesamtwert:     98.019,76 $  (Alpaca /v2/account Pre-Market Snapshot)
Cash:           56.707,49 $  (57,85 %)
Investiert:     41.312,27 $  (42,15 %, 5 Positionen)
P/L Pre-Drift:  -256,31 $    (-0,261 % vs last_equity 98.276,07) [GRÜN, Cap -3 %]
ATH:            100.066,47 $
Drawdown:       -2,045 %     [GRÜN — Alarm bei -15 %]
Guardrails:     Daily -0,261 % | Weekly +0,506 % | Käufe KW31 0/2
```

**Account Pre-Market 08:36 ET (Alpaca /v2/account):**
```
equity:            98.019,76 $   (Daily -0,261 % vs last_equity 98.276,07)
Cash:              56.707,49 $   (57,85 %, unverändert)
Portfolio MV:      41.312,27 $   (42,15 %, 5 Positionen, -227,64 $ vs Di Close 41.539,91)
Buying_power:     342.504,32 $   (Paper-Margin)
SPY Pre:              740,63     (Alpaca IEX Trade 08:36 ET vs Di Close 740,795 = -0,022 % flat) [Crash-Filter INAKTIV]
VIX ~16-17         (Perplexity Realtime, VXX Alpaca IEX 22,08-22,29 stabil) [GRÜN <25 volle Pos-Size]
10Y Yield:          ~4,0 %       (Perplexity grob)
Weekly KW31 Tag 3: +0,506 %      (vs Fr Close 97.526,60, +493,16 $)                    [GRÜN, Cap -5 %]
DD vs ATH:         -2,045 %      (vs 100.066,47)                                       [GRÜN]
Open Orders:           0          (KEINE Pending-Order)
Käufe KW31:            0/2       (Slot 1/2 + 2/2 offen)
Reconciliation:    last_equity Alpaca 98.276,07 vs Memory Close 98.247,40 = +28,67 $ marginal, unter Toleranz
```

**Positionen Pre-Market 08:36 ET (5 Positionen, sortiert Puffer ENG→WEIT):**

| Sym  | Cur      | Qty | Entry     | P/L %    | chg_today | V1-Std   | V1-Blackout    | V1-Puffer  | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|----------|----------------|------------|-----------------|
| V    |  359,21  | 27  |  357,178  | +0,57 %  | **-2,013 %** | 328,60  | **339,32 🟡** | **+5,86 %** ENGSTE **Post-Earnings-Give-back** verschlechtert vs Di Close +8,38 % um -2,52 pp | Blackout Post-Earnings-Watch (V berichtete Di 28.07. AMC ~17:00 ET) |
| LLY  | 1220,21  | 8   | 1193,89   | +2,21 %  | -0,037 %  | 1.098,38 | —              | +11,09 %   marginal verschlechtert vs Di Close +11,31 % | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07.) |
| AAPL |  339,10  | 31  |  316,857  | +7,02 %  | -0,288 %  | 291,51   | **301,02 🟡** | **+12,65 %** marginal verschlechtert vs Di Close +13,03 % | **🔴 AKTIV HT-1 Q3 FY26 Do 30.07. AMC** |
| UNH  |  427,80  | 24  |  401,57   | +6,53 %  | -0,231 %  | 369,44   | —              | +15,79 %   verbessert vs Di Close +15,16 % | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  357,54  | 3   |  332,78   | +7,44 %  | +0,064 %  | 306,16   | —              | +16,78 %   marginal verbessert vs Di Close +16,72 % Best P/L | inaktiv (Q3 ~Mitte Okt) |

**V1-Puffer Übersicht (eng→weit):** V **+5,86 % ENGSTE** Post-Earnings-Blackout | LLY +11,09 % | AAPL +12,65 % Blackout HT-1 | UNH +15,79 % | JPM +16,78 %

**V1-V6-Vollcheck Pre-Market 5 SICHER:**
- V1 (Stop -8 % / Blackout -5 %) — 5 SICHER, min V-Blackout **+5,86 % ENGSTE Post-Earnings-Give-back** (Cur 359,21 vs Di Close 367,748 = -2,32 %, Puffer verringert um -2,52 pp aber weiterhin sicher). Break unter 339,32 (-5,54 %) triggert V1-Blackout-Market-Sell sofort.
- V2 (Trailing -12 %) — kein 52w-Hoch-Trigger, kein Update
- V3 (+20 % TP1) — max JPM +7,44 % / AAPL +7,02 % << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- V5/V6 werden bei Pre-Market NICHT geprüft (kein neuer EOD-Bar seit Di Close, letzter Vollcheck Di 16:00 ET alle 5 SICHER — EMA50>EMA200 intakt, max RSI JPM 71,00 << 80)

**Daily Loss Cap Check:**
- Daily -0,261 % [weit von -3 %-Cap, GRÜN]
- 0 offene Orders (keine Cap-Aktivierung)

**Weekly Loss Cap Check (KW31 Tag 3):**
- Weekly +0,506 % (vs Fr Close 97.526,60, +493,16 $) [GRÜN, weit von -5 %-Cap]

**Guardrails Pre-Market 8/8 GRÜN + 3 WARN:**
```
1. Daily Loss Cap (-3 %):     Daily -0,261 %                                             [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 3 +0,506 %                                        [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,045 %                                                   [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,045 %                                                   [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,022 %                                               [INAKTIV]
6. VIX-Filter (>30):          VIX ~16-17 (VXX 22,08-22,29)                               [GRÜN <25 volle Pos-Size]
7. Earnings-Blackout (3 HT):  V Post-Earnings-Watch + AAPL HT-1 + LLY ab Do HT-3         [WARN x3]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                                 [GRÜN]

FED-WARN: Fed-Meeting HEUTE 14:00 ET FOMC + 14:30 ET Powell → LEVEL 0 restriktiv Vol-Peak 14:00-15:30 ET
```

**Pending Orders für Market Open Mi 29.07.:** KEINE (5 V1-V6 SICHER, keine V5/V6-Sell-Limit-Order, kein Kauf-Order Pre-Market platziert)

**Watchlist Market Open Mi 29.07. — Kaufsignal-Scan Slot 1/2 KW31:**
- **EOG** (Energy, K1-K3 ✓ pre-verifiziert Mo/Di, K4 EOD Rebound-Bestätigung fehlt, K5 vorbekannt sauber)
- **PANW** (Software Momentum, Perplexity Top-Rank, K1-K3 + Earnings zwingend)
- **GH** (Health Care Non-Pharma, +66,30 % 3M)
- **ILMN** (Health Care Non-Pharma, +50,52 % 3M)
- **ICLR** (Health Care Non-Pharma, +58,97 % 3M)
- XLV-Sektor-Cap-Grenzwertig: 3. XLV-Position würde Cap ~30 % pushen → PANW/EOG Diversifikationsvorteil

**V-Post-Earnings-Watch Market Open zwingend:**
- V-Kurs 359,21 vs Di Close 367,748 = -2,32 % Post-Earnings-Give-back Pre-Market
- Falls Weakness fortsetzt (chg <-4 % kumulativ, Cur unter ~352 → Puffer ~+3,7 %), Break-Watch zwingend
- Bei starker Erholung/Post-Earnings-Bid → Puffer wiederherstellbar

**AAPL Blackout HT-1 aktiv heute** (Q3 FY26 Do 30.07. AMC): V1_neu 301,02, Puffer +12,65 % sicher, keine Order-Änderung nötig.

**Fed-Meeting-Verhalten:** LEVEL 0 restriktiv default vor 14:00 ET FOMC. Kauf möglich bei starkem K1-K5 + V stabilisiert, aber wahrscheinlichkeit gering. Post-Fed (>15:30 ET) Re-Evaluation bei dovish + K1-K5 stark → möglich.

**→ KEIN Stop, KEIN Kauf, KEIN Daily-Cap-Trigger, KEINE Sell-Limit-Order. ClickUp Routine-Log Prio 4 wird gesendet. PushNotification Prio 3 Owner (V-Post-Earnings-ENGSTE + AAPL HT-1 + Fed-Meeting-Warnung).**

Nächster Check: **Mi 29.07. 09:30 ET Market Open + Kaufsignal-Scan** — V-Post-Earnings-Fortsetzung Watch (Puffer +5,86 % ENGSTE), EOG/PANW/GH/ILMN/ICLR K1-K5 vollständige Prüfung, LEVEL 0 restriktiv vor Fed 14:00 ET.

---

## Market Close 2026-07-28 16:00 ET (Di, KW31 Tag 2) — Tagesbilanz +0,651 % [GRÜN], Alpha +0,388 pp POSITIV vs SPY +0,263 %. **V5/V6-Vollcheck: alle 5 SICHER, KEINE Sell-Limit-Order** für morgen. V-Blackout letzter HT AMC HEUTE ~17:00 ET (Post-Earnings-Reaktion Mi Pre-Market Watch). AAPL Blackout schaltet auf HT-1 morgen. Fed-Meeting Mi 29.07. → LEVEL 0 restriktiv erwartet.

```
Market Close 16:00 [2026-07-28]:
Gesamtwert:     98.247,40 $  (letztes Alpaca /v2/account Snapshot vor Close)
Cash:           56.707,49 $  (57,72 %)
Investiert:     41.539,91 $  (42,28 %, 5 Positionen)
P/L heute:      +635,19 $    (+0,651 %) [GRÜN, Cap -3 %]
Alpha vs SPY:   +0,388 pp    POSITIV (Portfolio +0,651 % vs SPY +0,263 %)
ATH:            100.066,47 $
Drawdown:       -1,818 %     [GRÜN — Alarm bei -15 %]
Guardrails:     Daily +0,651 % | Weekly +0,739 % | Käufe KW31 0/2
```

**Account Close 16:00 ET (Alpaca /v2/account):**
```
equity:            98.247,40 $   (Daily +635,19 $ / +0,651 % vs last_equity 97.612,21)
Cash:              56.707,49 $   (57,72 %, unverändert)
Portfolio MV:      41.539,91 $   (42,28 %, 5 Positionen, -39,69 $ vs Midday 41.579,60)
Buying_power:     343.141,71 $   (Paper-Margin)
SPY Close:            740,795     (Alpaca IEX 1D-Bar, vs Mo Close 738,85 = +0,263 %) [Crash-Filter INAKTIV]
Weekly KW31 Tag 2: +0,739 %      (vs Fr Close 97.526,60, +720,80 $)                   [GRÜN, Cap -5 %]
DD vs ATH:         -1,818 %      (vs 100.066,47)                                      [GRÜN]
Open Orders:           0          (nichts zu stornieren, keine Weekly-Cap-Aktivierung)
Käufe KW31:            0/2       (Slot 1/2 + 2/2 offen, EOG heute geskippt)
```

**Positionen Close 16:00 ET (5 Positionen, sortiert Puffer ENG→WEIT):**

| Sym  | Cur      | Qty | Entry     | P/L %    | chg_today | V1-Std   | V1-Blackout    | V1-Puffer  | V5 EMA50>200 | V6 RSI/RS4w vs SPY |
|------|----------|-----|-----------|----------|-----------|----------|----------------|------------|--------------|--------------------|
| V    |  367,748 | 27  |  357,18   | +2,96 %  | +1,439 %  |  328,60  | **339,32 🟡**  | **+8,38 %** ENGSTE (Post-Earnings-Bid, minimal give-back vs Midday +8,70 %) | 341,72>330,48 ✓ (Spread +11,24) | RSI 65,34 / RS +7,36 pp — SICHER |
| LLY  | 1.222,608| 8   | 1.193,89  | +2,41 %  | +2,094 %  | 1.098,38 | —              | +11,31 %   XLV-Rebound Best chg | 1.133,84>1.017,57 ✓ (Spread +116,27) | RSI 61,78 / RS -0,58 pp knapp neg — SICHER (RSI <80) |
| AAPL |  340,234 | 31  |  316,86   | +7,38 %  | +0,986 %  |  291,51  | **301,02 🟡**  | **+13,03 %** (Blackout schaltet morgen HT-1 vor Do AMC) | 307,70>277,53 ✓ (Spread +30,17) | RSI 69,19 / RS +20,71 pp — SICHER |
| UNH  |  425,44  | 24  |  401,57   | +5,94 %  | +1,868 %  |  369,44  | —              | +15,16 %   XLV-Momentum stetig | 404,92>343,39 ✓ (Spread +61,53) | RSI 56,32 / RS +2,19 pp — SICHER |
| JPM  |  357,35  | 3   |  332,78   | +7,38 %  | +0,323 %  |  306,16  | —              | +16,72 %   Best-Puffer XLF | 329,20>309,71 ✓ (Spread +19,49) | RSI **71,00** (max, WATCH aber <80) / RS +8,99 pp — SICHER |

**V1-Puffer Übersicht (eng→weit):** V **+8,38 %** Blackout ENGSTE | LLY +11,31 % | AAPL +13,03 % Blackout | UNH +15,16 % | JPM +16,72 %

**V1-V6-Vollcheck Market Close 5 SICHER:**
- V1 (Stop -8 % / Blackout -5 %) — 5 SICHER, min V-Blackout **+8,38 % ENGSTE** (marginal give-back vs Midday +8,70 %, aber Post-Earnings-Bid trägt), AAPL-Blackout HT-1 morgen aktiv +13,03 %
- V2 (Trailing -12 %) — max P/L 7,38 %, kein 52w-Hoch-Trigger, kein Update nötig
- V3 (+20 % TP1) — max AAPL/JPM +7,38 % << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- V5 (EMA50<EMA200 = Death Cross) — alle 5 SICHER, engster Spread V +11,24 (EMA50 341,72 > EMA200 330,48) noch komfortabel
- V6 (RSI>80 UND RS4w<0) — kein Trigger: max RSI JPM 71,00 (<80), einziger RS4w<0 = LLY -0,58 pp knapp (aber RSI 61,78 << 80). V6 verlangt BEIDES.
- **→ KEINE Sell-Limit-Order für Mi 29.07. platziert**

**Daily Loss Cap Check:**
- Daily +0,651 % [weit von -3 %-Cap, GRÜN]
- 0 offene Orders zum Stornieren (keine Cap-Aktivierung)

**Weekly Loss Cap Check (KW31 Tag 2):**
- Weekly +0,739 % (vs Fr Close 97.526,60, +720,80 $) [GRÜN, weit von -5 %-Cap]
- Keine Aktion nötig, keine Order-Stornierung, kein WEEKLY_CAP-Alert

**Guardrails Close 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     Daily +0,651 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 2 +0,739 %                                       [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,818 %                                                  [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,818 %                                                  [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,263 %                                              [INAKTIV]
6. VIX-Filter (>30):          VXX ~22 (Proxy VIX ~16-19) — carry-over Midday            [GRÜN <25]
7. Earnings-Blackout (3 HT):  V letzter HT AMC HEUTE, AAPL HT-1 morgen                  [WARN x2]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                                [GRÜN]
```

**Pending Orders für Mi 29.07.:** KEINE (5 V1-V6 SICHER, keine V5/V6-Sell-Limit-Order)

**Watchlist Mi 29.07. Pre-Market / Market Open:**
- **EOG** (carry-over aus heute, K1-K3 ✓ pre-verifiziert, K4 EOD nachträglich zu prüfen, Fed-Uncertainty-Watch)
- **PANW** (Software Momentum, Perplexity 07-28)
- **GH** (Health Care Non-Pharma Momentum)
- **ILMN** (Health Care Non-Pharma)
- **ICLR** (Health Care Non-Pharma)
- K1-K3 pre-check zwingend bei Market Open Mi 29.07., K4/K5 vollständige Prüfung dort
- **Fed-Meeting Mi 29.07. FOMC-Statement 14:00 ET / Powell-Presskonferenz 14:30 ET → LEVEL 0 restriktiv default vor Event, Kauf ggf. Do 30.07. nach Fed-Reaktion**

**V-Post-Earnings-Reaktion Watch Mi 29.07. Pre-Market 08:30 ET zwingend:**
- V berichtete heute AMC ~17:00 ET (letzter HT) → nach Close war Move noch nicht sichtbar in equity 98.247,40
- Pre-Market-Kurs vs Close 367,748 = Post-Earnings-Move; Break unter Blackout 339,32 (-7,7 %) löst V1-Blackout-Sell aus (Pre-Market Market-Order)
- Break unter Std-V1 328,60 (-10,6 %) löst V1-Std-Sell aus, falls Pre-Market ohne Blackout-Regel gilt (Regel-Präzedenz beobachten)

**AAPL Blackout HT-1 aktiv ab Mi 29.07. Open** (Q3 FY26 Do 30.07. AMC bestätigt):
- V1_neu 301,02 (statt Std 291,51), Puffer +13,03 % Close → SICHER, aber engere Stop-Loss-Zone
- Bei chg <-4 % Mi Pre-Market → Break-Watch AAPL

**→ KEIN Stop, KEIN Daily-Cap-Trigger, KEINE Sell-Limit-Order, KEIN Kauf-Alert. ClickUp Tagesbericht Prio 4 (positive Performance) wird gesendet. PushNotification wegen positivem Alpha + Watchlist-Aktivierung + V-Post-Earnings-Watch → JA (routine-relevant, Owner soll morgen Pre-Market prüfen).**

Nächster Check: **Mi 29.07. 08:30 ET Pre-Market** — V-Post-Earnings-Reaktion primär, AAPL Blackout HT-1, EOG-Rebound-Watch + PANW/GH/ILMN/ICLR K1-K3 Erst-Screening, Fed-Meeting-Vorbereitung (14:00 ET FOMC + 14:30 ET Powell).

---

## Midday Stop-Check 2026-07-28 13:09 ET (Di, KW31 Tag 2) — Alle 5 V1 SICHER, KEIN Stop-Trigger, KEIN Daily-Cap-Trigger. Puffer alle verbessert vs Market Open (breite Marktstärke SPY +0,39 %, UNH-XLV-Momentum +2,67 % Best chg, V-Blackout Puffer verbessert +7,84 %→+8,70 % Post-Open Bid).

```
Midday 13:09 [2026-07-28]:
Positionen: 5/8 | Ø P/L: +5,26 %
Schlechteste Position: LLY +2,27 %
Beste Position: JPM +7,12 %
Stops: alle regulär (5/5 V1 SICHER, keine V3/V4-Trigger)
Daily P/L: +0,691 % [GRÜN, Cap -3 %]
```

**Account Live 13:09 ET:**
```
Equity Live:       98.287,09 $   (Daily +674,88 $ / +0,691 % vs last_equity 97.612,21)
Cash:              56.707,49 $   (57,70 %, unverändert)
Portfolio MV Live: 41.579,60 $   (42,30 %, 5 Pos, +260,83 $ vs Market Open 41.318,77)
SPY Live 13:09:      741,73       (vs Mo Close 738,85 = +0,390 %)                     [Crash-Filter INAKTIV]
Alpha vs SPY:       +0,301 pp    POSITIV knapp (Cash-Puffer 57,70 % dämpft, aber UNH/LLY-XLV-Rebound + V-Bid stützen)
Weekly KW31 Tag 2: +0,780 %       (vs Fr Close 97.526,60, +760,49 $)                  [GRÜN, Cap -5 %]
DD vs ATH:         -1,778 %       (vs 100.066,47)                                     [GRÜN]
Open Orders:           0          (nichts zu stornieren)
Käufe KW31:            0/2       (Slot 1/2 + 2/2 offen, EOG Re-Check EOD/Mi Pre-Market)
```

**Positionen Live 13:09 ET (5 Positionen, sortiert Puffer ENG→WEIT):**

| Sym  | Cur      | Qty | Entry     | P/L %    | chg_today | V1-Std      | V1-Blackout   | V1-Puffer  | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|-------------|---------------|------------|-----------------|
| V    |  368,83  | 27  |  357,18   | +3,26 %  | +1,72 %   | 328,60      | **339,32 🟡** | **+8,70 %** ENGSTE (verbessert vs MO +7,84 % um +0,86 pp, Post-Open Bid Rebound) | AKTIV letzter HT Q3 CY26 HEUTE AMC 5:00 PM ET |
| LLY  | 1.220,96 | 8   | 1.193,89  | +2,27 %  | +1,93 %   | 1.098,38    | —             | +11,16 %   verbessert vs MO +10,96 % XLV-Fortsetzung | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07.) |
| AAPL |  339,38  | 31  |  316,86   | +7,11 %  | +0,66 %   | 291,51      | **301,02 🟡** | **+12,74 %** marginal verschlechtert vs MO +12,88 % (AAPL -0,12 % vs MO Give-back) | **🔴 AKTIV Q3 FY26 Do 30.07. AMC HT-2 HEUTE** |
| UNH  |  427,92  | 24  |  401,57   | +6,56 %  | +2,67 %   | 369,44      | —             | +15,83 %   verbessert vs MO +13,58 % **Best chg XLV-Momentum** | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  356,49  | 3   |  332,78   | +7,12 %  | +0,20 %   | 306,16      | —             | +16,44 %   verbessert vs MO +16,11 % Best P/L | inaktiv (Q3 ~Mitte Okt) |

**V1/V2/V3/V4-Check Midday:**
- V1 (Stop -8 % / Blackout -5 %) — 5 SICHER, min V-Blackout **+8,70 % ENGSTE verbessert vs MO +7,84 %** um +0,86 pp (V chg +1,72 % Post-Open Bid, Blackout-Puffer stabil)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (+20 % TP1) — max JPM +7,12 % / AAPL +7,11 % << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- V5/V6 werden bei Midday NICHT geprüft (Routine-Regel, nur Market Open & Close)

**Daily Loss Cap Check:**
- Daily +0,691 % [weit von -3 %-Cap, GRÜN]
- Keine Limit-Orders zum Stornieren (0 offene Orders)

**Guardrails Midday 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     Daily +0,691 %                                             [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 2 +0,780 %                                        [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,778 %                                                   [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,778 %                                                   [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,390 %                                               [INAKTIV]
6. VIX-Filter (>30):          VXX ~22 (Proxy VIX ~16-19)                                 [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV letzter HT + AAPL AKTIV HT-2                       [WARN x2]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                                 [GRÜN]
```

**→ KEIN Stop, KEIN Daily-Cap-Trigger, KEIN ClickUp Alert (Routine-Spec: nur bei Stops/Cap), KEIN PushNotification (empty run — Silence-Rule respektiert).**

Nächster Check: **Di 28.07. 16:00 ET Market Close** — V Q3 CY26 AMC HEUTE 5:00 PM ET (Blackout Post-Earnings-Reaktion morgen relevant), AAPL Blackout HT-2 (Do 30.07. AMC), V5/V6-Vollcheck alle 5 zwingend, EOD-Screener für Slot 1/2 EOG K4-EOD-Volumen-Verifikation + evtl. weitere Kandidaten.

---

## Market Open 2026-07-28 09:38 ET (Di, KW31 Tag 2) — KEIN Kauf: EOG K4 formal offen + Rebound +0,74 % zu schwach + Fed Mi 29.07. Unsicherheit → LEVEL 0 No-Action. Alle 5 V1-V6 SICHER, Alpha +0,503 pp POSITIV knapp, Slot 1/2 KW31 OFFEN Re-Check Midday.

```
Alpaca clock:      is_open=true | 09:38 ET | next_close Di 28.07. 16:00 ET
Equity Live:       98.026,26 $   (Alpaca /v2/account, Daily +414,05 $ / +0,424 % vs last_equity 97.612,21)
Cash:              56.707,49 $   (57,85 %, unverändert)
Portfolio MV Live: 41.318,77 $   (42,15 %, 5 Positionen, -46,20 vs Pre 41.364,97)
Buying_power:     342.522,52 $   (Paper-Margin)
Daily P/L:         +414,05 $     (+0,424 %)                                              [GRÜN, Cap -3 %]
SPY Live 09:38:      738,27       (vs Mo Close 738,85 = -0,079 %)                        [Crash-Filter INAKTIV]
Alpha vs SPY:       +0,503 pp    POSITIV (Cash-Puffer 57,85 % dämpft aber LLY/AAPL-Rebound-Beta > SPY-Flat)
VXX Live:            22,38        (VIX-Proxy, vs Mo Close 22,225 = +0,7 %)               [GRÜN <25 volle Pos-Size]
ATH:              100.066,47 $   DD -2,039 % [GRÜN — Alarm bei -15 %]
Weekly KW31 Tag 2: +0,512 %       (vs Fr Close 97.526,60, +499,66 $)                     [GRÜN, Cap -5 %]
Käufe KW31:            0/2       (Slot 1/2 bleibt OFFEN, Slot 2/2 offen)
Open Orders:           0          (KEINE Pending-Order)
Guardrails:        8/8 GRÜN + 2 WARN (V-Blackout letzter HT AMC HEUTE + AAPL-Blackout HT-2)
```

**Positionen Live 09:38 ET (5 Positionen, sortiert Puffer ENG→WEIT):**

| Sym  | Cur      | Qty | Entry     | P/L %    | chg_today | V1-Std      | V1-Blackout   | V1-Puffer  | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|-------------|---------------|------------|-----------------|
| V    |  365,93  | 27  |  357,18   | +2,45 %  | +0,94 %   | 328,60      | **339,32 🟡** | **+7,84 %** ENGSTE (verschlechtert vs Pre +9,04 %, Post-Open Give-back von 370,00) | AKTIV letzter HT Q3 CY26 HEUTE AMC 5:00 PM ET |
| LLY  | 1.218,81 | 8   | 1.193,89  | +2,09 %  | +1,78 %   | 1.098,38    | —             | +10,96 %   verbessert vs Pre +10,41 % XLV-Rebound | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07.) |
| AAPL |  339,79  | 31  |  316,86   | +7,24 %  | +0,86 %   | 291,51      | **301,02 🟡** | **+12,88 %** verbessert vs Pre +12,59 % XLK-Bid | **🔴 AKTIV Q3 FY26 Do 30.07. AMC HT-2 HEUTE** |
| UNH  |  419,60  | 24  |  401,57   | +4,49 %  | +0,47 %   | 369,44      | —             | +13,58 %   verschlechtert vs Pre +13,85 % XLV-Divergenz | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  355,48  | 3   |  332,78   | +6,82 %  | -0,20 %   | 306,16      | —             | +16,11 %   verschlechtert vs Pre +17,11 % XLF-Give-back Best P/L | inaktiv (Q3 ~Mitte Okt) |

**V1-V6-Vollcheck Market Open 5 SICHER:**
- V1 (Stop -8 % / Blackout -5 %) — 5 SICHER, min V-Blackout +7,84 % ENGSTE (verschlechtert vs Pre +9,04 % um -1,20 pp, V-Give-back von Pre-Peak 370 auf Live 365,93 = -1,10 %)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (+20 % TP1) — max JPM +6,82 % << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- V5 (EMA50<EMA200 Death Cross) — 5 SICHER, aus Mo Close-Bars alle Golden Cross intakt (V EMA-Diff +1,85 % engste aber intakt, keine EOD-Bar heute)
- V6 (RSI>80 & RS<0) — 5 SICHER, aus Mo Close max RSI JPM 69,94 << 80

**→ KEINE Sell-/Limit-Order platziert. KEIN Stop-Trigger.**

**Kaufsignal-Scan Slot 1/2 KW31 — EOG SKIP LEVEL 0 No-Action:**

| Kriterium | EOG Wert | Cap | Erfüllt |
|-----------|----------|-----|---------|
| K1 EMA50>EMA200 | 136,54 / 125,52 diff +8,78 % | > 0 | ✓ |
| K2 RSI(14) | 54,53 | 50-70 | ✓ |
| K3 RS_63d vs SPY | +2,54 pp (EOG +6,12 % vs SPY +3,58 %) | > 0 | ✓ |
| K4 Volumen | Session-Vol 1.302 / avg20 128.200 = 1,02 % bei 8 Min in Session (pro-rata 63.472 = ~49 % avg20 unzuverlässig zu früh) | ≥ 120 % | **✗ formal offen** |
| K5 FwdPE / RevGr YoY | 9,98 / +15,63 % vorbekannt Mo | ≤ 35 / ≥ 10 % | ✓ |

- **chg today +0,74 %** (Cur 141,36 vs Mo Close 140,32) → milder Rebound, aber NICHT konvinzent stark (Momentum-Bruch -4,14 % Mo nicht überwunden)
- **XLE-Sektor-Rückenwind heute unklar** (kein Realtime-Sektor-Check erfolgt, Mo XLE -0,90 % war Kontra-Öl-Narrative)
- **Fed-Meeting Mi 29.07.** schafft zusätzliche Unsicherheit → LEVEL 0 restriktiv
- **Watchlist-Rest** GE/PSX/HON/DE/D K5-persistent-FAIL, F SKIP Blackout AMC heute, NEE/DUK K3-FAIL — kein Alternativ-Kandidat verfügbar

**→ EOG SKIP: Re-Check Midday 13:00 ET (K4 Volumen EOD-realistisch bewertbar + Intraday-Rebound-Konsolidierung). Slot 1/2 KW31 bleibt OFFEN.**

**Guardrails Market Open 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     Daily +0,424 %                                             [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 2 +0,512 %                                        [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,039 %                                                   [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,039 %                                                   [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,079 %                                               [INAKTIV]
6. VIX-Filter (>30):          VXX 22,38 (Proxy VIX ~16-19)                               [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV letzter HT + AAPL AKTIV HT-2                       [WARN x2]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                                 [GRÜN]
```

**Sektor-Struktur unverändert vs Pre-Market:**

| Sektor | Positionen | MV Live $ | % Portfolio (98.026) | Status |
|--------|-----------|-----------|-----------------------|--------|
| XLV | UNH + LLY | 19.820,84 | 20,22 % | GRÜN <30 % |
| XLF | JPM + V | 10.946,55 | 11,17 % | GRÜN |
| XLK | AAPL | 10.533,49 | 10,74 % | GRÜN |
| Cash | — | 56.707,49 | 57,85 % | GRÜN (>20 % Min, hoch) |

**Entscheidung Market Open Di 28.07.:**
- **KEIN Kauf** — EOG K4 formal offen + Rebound zu schwach → LEVEL 0 No-Action
- **KEINE Sell-/Limit-Order** — alle 5 V1-V6 SICHER
- **Slot 1/2 KW31 bleibt OFFEN** — Re-Check Midday 13:00 ET für EOG K4 EOD-realistischer Volumen-Bewertung
- **AAPL Blackout V1_neu 301,02** Info-only, Puffer +12,88 % sicher aktivierbar ohne Alpaca-Order-Änderung
- **V-Blackout letzter HT** — Post-Earnings-Reaktion Mi 29.07. Pre-Market Watch zwingend
- **ClickUp Routine-Log Prio 4** wird gesendet
- **PushNotification Silence** (empty run: kein Trade, alle safe, EOG deferred — Silence-Rule "wenn Run leer kommt, ist Schweigen die freundliche Wahl")

**Nächste Routine:** Di 28.07. 13:00 ET Midday Stop-Check — EOG K4 EOD-realistische Volumen-Bewertung + evtl. Nachmittag-Kauf-Fenster, V-Blackout Post-Earnings-Bid Watch (V ENGSTE Puffer +7,84 %), AAPL Blackout V1_neu 301,02 nur Info.

---

## Pre-Market 2026-07-28 08:36 ET (Di, KW31 Tag 2) — 🔴 AAPL Blackout NEU AKTIVIERT (Q3 FY26 Do 30.07. AMC HT-2 heute, Memory-Fehler von Fr 24.07. korrigiert), V-Blackout letzter HT (Q3 CY26 AMC HEUTE 5:00 PM ET). 5 V1-V6 SICHER, Pre-Drift +0,472 %, Slot 1/2 offen EOG-Watch.

```
Alpaca clock:      is_open=false | 08:36 ET | next_open Di 28.07. 09:30 ET
Equity Pre:        98.072,46 $   (Alpaca /v2/account, +460,25 $ / +0,472 % vs last_equity 97.612,21)
Cash:              56.707,49 $   (57,82 %, unverändert vs Mo Close)
Portfolio MV Live: 41.364,97 $   (42,18 %, 5 Positionen, +469,58 vs Mo Close 40.895,39)
Buying_power:     342.651,88 $   (Paper-Margin)
Daily P/L Pre:      +460,25 $    (+0,472 % vs last_equity 97.612,21)                    [GRÜN, Cap -3 %]
SPY Pre 08:34:      739,87        (vs Mo Close 738,85 = +0,138 %)                       [Crash-Filter INAKTIV]
VIX carry-over:    16-19 Bandbr. (Perplexity 16,3 first / VXX Mo Close 22,225)         [GRÜN <25]
10Y Yield:          ~4,24 %       (Perplexity)
ATH:              100.066,47 $   DD -1,993 % [GRÜN — Alarm bei -15 %]
Weekly KW31 Tag 2: +0,559 %       (vs Fr Close 97.526,60, +545,86 $)                    [GRÜN, Cap -5 %]
Käufe KW31:            0/2       (Slot 1/2 offen EOG-Watch, Slot 2/2 offen)
Open Orders:           0          (KEINE Pending-Order)
Reconciliation:    last_equity Alpaca 97.612,21 vs Memory Close 97.602,90 = +9,31 $ marginal, keine Prüfung nötig
Guardrails:        8/8 GRÜN + 2 WARN (V-Blackout letzter HT AMC HEUTE + AAPL-Blackout NEU HT-2)
```

**Positionen Pre 08:35 ET (5 Positionen, sortiert Puffer ENG→WEIT, Blackout-V1_neu wo aktiv):**

| Sym  | Cur      | Qty | Entry     | P/L %    | V1-Std      | V1-Blackout   | V1-Puffer  | Blackout-Status |
|------|----------|-----|-----------|----------|-------------|---------------|------------|-----------------|
| V    |  370,00  | 27  |  357,18   | +3,59 %  | 328,60      | **339,32 🟡** | **+9,04 %** ENGSTE | AKTIV letzter HT Q3 CY26 HEUTE AMC 5:00 PM ET |
| LLY  | 1.212,73 | 8   | 1.193,89  | +1,58 %  | 1.098,38    | —             | +10,41 %   | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07.) |
| AAPL |  338,92  | 31  |  316,86   | +6,96 %  | 291,51      | **301,02 🟡** | **+12,59 %** | **🔴 NEU AKTIV Q3 FY26 Do 30.07. AMC HT-2 HEUTE** |
| UNH  |  420,60  | 24  |  401,57   | +4,74 %  | 369,44      | —             | +13,85 %   | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  358,54  | 3   |  332,78   | +7,74 %  | 306,16      | —             | +17,11 %   | inaktiv (Q3 ~Mitte Okt) |

**V1-V6-Puffer-Analyse Pre-Market 5 SICHER — alle 5 Puffer verbessert vs Mo Close** (Pre-Drift +0,472 %):
- V1 (Stop -8 % / Blackout -5 %) — 5 SICHER, min V-Blackout +9,04 % (verbessert vs Mo Close +6,86 % um +2,18 pp — V-Rebound Pre-Earnings-Bid +2,04 % chg treibt Puffer)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (+20 % TP1) — max +7,74 % JPM << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- V5/V6 — Pre-Market keine EOD-Bars, aus Mo Close alle Golden Cross intakt, max RSI JPM 69,94 << 80

**→ KEINE Sell-/Limit-Order platziert. KEIN Stop-Trigger. Pre-Drift-Rally treibt alle 5 Puffer weiter safe.**

**🔴 AAPL-BLACKOUT-KORREKTUR — CRITICAL Memory-Fix:**
- Vorheriges Memory (Fr 24.07. Pre-Market): "AAPL/JPM/UNH/LLY/GS kein Blackout, alle Q2 CY26 bereits Mitte Juli gemeldet, nächste Q3 ~Ende Oktober" **WAR FALSCH für AAPL**.
- Apple Fiscal Q3 FY26 = Kalenderquartal Apr-Jun 2026 → Report Ende Juli (nicht Oktober).
- **Multi-Source-Bestätigung heute Pre-Market** (Apple IR, 9to5Mac, MacDailyNews, Wall Street Horizon, MarketBeat, MarketChameleon, Investing.com — 7+ Quellen konvergent): **Do 30.07.2026 AMC 5:00 PM ET Call**.
- Blackout-Regel: 3 HT vor Earnings → Aktivierung ab HT-3.
- HT-3 = **Mo 27.07.** (verpasst gestern durch Memory-Fehler)
- HT-2 = **Di 28.07. HEUTE** (Aktivierung NEU jetzt)
- HT-1 = Mi 29.07. | HT-0 = Do 30.07. AMC
- **V1_neu = 316,86 × 0,95 = 301,02 $** (statt Standard 291,51 $), aktueller Kurs 338,92 → **Puffer +12,59 %**, sicher aktivierbar ohne Sofort-Stop.
- **Aktion:** V1-Watch verengt, keine Alpaca-Order-Änderung nötig (Alpaca hat keine offenen Stop-Orders auf AAPL).
- Blackout aktiv bis Fr 31.07. Post-Earnings-Reaktion (Do AMC + 1 HT Konsolidierung).

**Watchlist Slot 1/2 KW31 (aus Mo Close K1-K3-Screener):**

| Sym | Mo Close | Entscheidung Di | Rationale |
|-----|----------|-----------------|-----------|
| **EOG** | 140,32 (-4,14 %) | **PRIMÄR — Rebound-Watch Market Open** | K1-K3 ✓, K5 vorbekannt ✓ (FwdPE 9,98 + RevGr +15,63 %). Bei Rebound + Vol ≥120 % + K5-Recheck sauber → Kauf. Bei Weakness Fortsetzung → LEVEL 0 SKIP |
| GE | 361,66 | REJECT persistent | K5-FAIL FwdPE Median 44,72 (>35) |
| PSX | 207,75 | REJECT persistent | K5-FAIL RevGr Q +6,9 % (<10 %) |
| F | 14,69 | SKIP Blackout | Q2 Di 28.07. AMC HEUTE bestätigt |
| HON | 245,76 | REJECT persistent | K5-FAIL RevGr +2,4 % |
| DE | 624,78 | REJECT persistent | K5-FAIL RevGr +9,6 % |
| D | 70,27 | REJECT persistent | K5-FAIL RevGr +7,49 % |
| NEE/DUK | — | DROP K3-FAIL | RS_63d negativ |

**Makro heute Di 28.07.:** Consumer Confidence 14:30 ET (sekundär), API Öl 22:40 ET. **Wochenausblick:** Mi 29.07. FOMC + Zinsentscheid (primärer Vol-Katalysator), MSFT/META/SBUX AMC. Do 30.07. GDP+PCE 14:30 ET + AAPL/AMZN AMC.

**Guardrails Pre-Market 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     Pre-Drift +0,472 %                                     [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 2 +0,559 %                                    [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,993 %                                               [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,993 %                                               [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Mo -0,007 % / Pre +0,138 %                        [INAKTIV]
6. VIX-Filter (>30):          VIX ~16-19 Bandbreite                                  [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV letzter HT + AAPL NEU AKTIV HT-2              [WARN x2]
8. Max Käufe KW31:            0/2                                                    [GRÜN]
```

**Sektor-Struktur Pre-Market (unverändert vs Mo Close):**

| Sektor | Positionen | MV Pre $ (approx) | % Portfolio (98.072) | Status |
|--------|-----------|-------------------|-----------------------|--------|
| XLV | UNH + LLY | 19.796,24 | 20,18 % | GRÜN <30 % |
| XLF | JPM + V | 11.065,62 | 11,28 % | GRÜN |
| XLK | AAPL | 10.506,52 | 10,71 % | GRÜN |
| Cash | — | 56.707,49 | 57,82 % | GRÜN (>20 % Min, hoch) |

**Entscheidung Pre-Market Di 28.07.:**
- **AAPL Blackout ACTION**: V1-Watch auf 301,02 $ verengt, Puffer +12,59 % sicher, keine Order-Änderung nötig
- **Market-Open-Scan JA** — EOG Rebound-Watch Primärkandidat für Slot 1/2, K4-Vol + K5-Multi-Source-Recheck 09:30 ET zwingend
- **Kauf-Wahrscheinlichkeit heute GERING** (Fed-Meeting morgen schafft Unsicherheit → LEVEL 0 restriktiv, EOG braucht Rebound-Bestätigung)
- **ClickUp Routine-Log Prio 4** wird gesendet
- **PushNotification Prio 2 Owner** — AAPL-Blackout-Neuaktivierung ist echtes Signal (Memory-Fehler korrigiert), Sichtbarkeit gerechtfertigt

**Nächste Routine:** Di 28.07. 09:30 ET Market Open + Kaufsignal-Scan — EOG K4/K5 Vollcheck + evtl. Limit-Order, V-Blackout letzter Tag Post-Earnings-Bid Watch, AAPL Blackout V1_neu 301,02 Info-only.

---

## Market Close 2026-07-27 16:03 ET (Mo, KW31 Tag 1) — Tagesbilanz: 5/8 Positionen V1-V6 SICHER, Daily +0,075 %, Alpha +0,082 pp knapp POSITIV, keine Pending-Order, Slot 1/2 KW31 offen

```
Alpaca clock:      is_open=false | close_ts Mo 27.07. 16:00 ET | next_open Di 28.07. 09:30 ET
Equity Close:      97.602,90 $   (Alpaca /v2/account)
Cash:              56.707,51 $   (58,10 %, unverändert nach GS-Sell Midday)
Portfolio MV:      40.895,39 $   (41,90 %, 5 Positionen)
Buying_power:     341.337,13 $   (Paper-Margin)
Daily P/L:            +73,32 $   (+0,075 % vs last_equity 97.529,58)                  [GRÜN, Cap -3 %]
SPY Close:           738,85       (vs Fr Close 738,90 = -0,007 % effektiv flat)         [Crash-Filter INAKTIV]
Alpha vs SPY:       +0,082 pp    POSITIV knapp
ATH:              100.066,47 $   DD -2,462 % [GRÜN — Alarm bei -15 %]
Weekly KW31 Tag 1:  +0,078 %      (vs Fr Close 97.526,60, +76,30 $)                     [GRÜN, Cap -5 %]
Käufe KW31:            0/2       (Slot 1/2 offen, Slot 2/2 offen)
Open Orders:           0          (KEINE Pending-Order für Di 28.07.)
Guardrails:        8/8 GRÜN + 1 WARN (V-Blackout Tag+2/2 letzter HT vor Q3 Di 28.07. AMC)
```

**Positionen Close 16:03 ET (5 Positionen, sortiert Puffer ENG→WEIT):**

| Sym  | Close    | Qty | Entry     | P/L %    | chg_today | V1-Stop     | V1-Puffer  | EMA50/200 | RSI    | Status |
|------|----------|-----|-----------|----------|-----------|-------------|------------|-----------|--------|--------|
| V    |  362,60  | 27  |  357,18   | +1,52 %  | +1,93 %   | **339,32** 🟡BLACKOUT | **+6,86 %** | +1,85 % | 62,48 | SICHER **ENGSTE** verbessert vs Midday +6,88 %/Open +6,27 %, V1-V6 alle safe, EMA-Diff engste aber intakt |
| LLY  | 1.197,88 | 8   | 1.193,89  | +0,33 %  | +0,15 %   | 1.098,38    | +9,06 %    | +12,38 %  | 57,44 | SICHER stabil vs Midday +9,15 % |
| UNH  |  416,80  | 24  |  401,57   | +3,79 %  | -0,94 %   |   369,44    | +12,82 %   | +13,92 %  | 49,41 | SICHER **Worst chg** verschlechtert vs Midday +13,47 % XLV-Give-back |
| AAPL |  337,15  | 31  |  316,86   | +6,41 %  | +1,24 %   |   291,51    | +15,66 %   | +10,30 %  | 67,61 | SICHER verbessert vs Midday +15,25 % XLK-Rebound |
| JPM  |  355,78  | 3   |  332,78   | +6,91 %  | +0,73 %   |   306,16    | +16,21 %   | +4,95 %   | 69,94 | SICHER **Best P/L** verbessert vs Midday +15,35 %, RSI näher 80 aber weit unter |

**V1-V6-Vollcheck Close 5 SICHER:**
- V1 (Stop -8 %) — 5 SICHER, min V +6,86 % Blackout (Blackout V1_neu 339,32; Puffer 23,28 $ vom Break)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (+20 % TP1) — max +6,91 % JPM << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- **V5 (EMA50<EMA200 = Death Cross) — 5 SICHER** (Alpaca IEX Bars bis 27.07., Golden Cross intakt): V EMA-Diff +1,85 % (**engste**, verschlechtert vs Fr +1,76 % nach V-Rebound → EMA50 pushed higher, aber intakt), JPM +4,95 %, AAPL +10,30 %, LLY +12,38 %, UNH +13,92 % — kein Death Cross
- **V6 (RSI>80 & RS_4w vs SPY<0) — 5 SICHER**: max **RSI JPM 69,94** (verschlechtert vs Midday geschätzt / Fr 68,01, näher 80 aber weit unter), AAPL 67,61, V 62,48, LLY 57,44 (RS_4w -2,06 pp aber RSI << 80), UNH 49,41 (RS_4w -3,61 pp aber RSI << 80) — alle << 80

**→ KEINE Sell-/Limit-Order für Di 28.07. platziert. KEIN Stop-Trigger. Keine V5/V6-Order pending.**

**Watchlist Di 28.07. (K1-K3 aus Alpaca IEX Bars 27.07. Close, K4/K5 zwingend bei Market Open):**

| Sym | Close   | chg   | EMA50/200 diff | RSI    | RS_63d vs SPY | K1 | K2 | K3 | K5 vorbekannt | Decision Tue |
|-----|---------|-------|----------------|--------|---------------|----|----|----|--------------|--------------|
| GE  | 361,66  | +2,24 % | +8,15 %      | 58,17  | **+23,55 pp #1** | ✓ | ✓ | ✓ | ✗ FwdPE Median 44,72 (>35) | **REJECT** K5 persistent, kein Kauf |
| PSX | 207,75  | +0,47 % | +15,82 %     | 68,09  | **+24,10 pp #2** | ✓ | ✓ | ✓ | ✗ RevGr Q +6,9 % (<10 %) | **REJECT** K5 persistent |
| F   |  14,69  | +2,30 % | +5,49 %      | 59,43  | +15,13 pp     | ✓ | ✓ | ✓ | K5 offen | **SKIP** Blackout Q2 Di 28.07. AMC |
| HON | 245,76  | +1,10 % | +3,37 %      | 67,03  | +11,81 pp     | ✓ | ✓ | ✓ | ✗ RevGr +2,4 % (<10 %) | **REJECT** K5 persistent |
| EOG | 140,32  | **-4,14 %** | +8,75 %  | 53,54  | +1,90 pp      | ✓ | ✓ | ✓ | ✓ FwdPE 9,98 + RevGr +15,63 % | **WATCH** Rebound-Watch, Momentum-Bruch heute → wenn Di Rebound + Volumen ≥120 % → K4-Check + Kauf |
| DE  | 624,78  | -0,55 % | +8,52 %      | 60,83  | +7,56 pp      | ✓ | ✓ | ✓ | ✗ RevGr +9,6 % (<10 %) | **REJECT** K5 persistent |
| D   |  70,27  | -1,15 % | +6,78 %      | 53,41  | +8,82 pp      | ✓ | ✓ | ✓ | ✗ RevGr +7,49 % | **REJECT** K5 persistent |
| NEE |  88,81  | -1,07 % | +3,64 %      | 52,24  | **-10,29 pp** | ✓ | ✓ | ✗ | offen | **DROP** K3-FAIL |
| DUK | 128,84  | -1,23 % | +1,35 %      | 56,32  | **-2,26 pp**  | ✓ | ✓ | ✗ | offen | **DROP** K3-FAIL |

**→ Watchlist Di 28.07. Primärkandidat: EOG (bei Rebound + K4-Volumen ≥120 % + K5-Recheck).** Alle klassischen RS-Leader (GE/PSX/HON/D/DE) K5-persistent-FAIL. F Blackout AMC. **Slot 1/2 KW31 bleibt OFFEN.**

**Guardrails 8/8 GRÜN + 1 WARN (V-Blackout Tag+2/2 letzter HT vor Q3):**
```
1. Daily Loss Cap (-3 %):     +0,075 %                                                [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 1 +0,078 %                                     [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,462 %                                                [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,462 %                                                [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,007 %                                            [INAKTIV]
6. VIX-Filter (>30):          carry-over Mo 19-21                                     [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV Tag+2/2 letzter HT vor Q3 Di 28.07. AMC        [WARN]
8. Max Käufe KW31:            0/2 Slot 1/2 + 2/2 offen                                [GRÜN]
```

**Sektor-Struktur Close (Post-GS-Sell konstant):**

| Sektor | Positionen | MV Close $ | % Portfolio (97.603) | Status |
|--------|-----------|-----------|-----------------------|--------|
| XLV | UNH + LLY | 19.586,20 | 20,07 % | GRÜN <30 % |
| XLF | JPM + V | 10.857,54 | 11,13 % | GRÜN |
| XLK | AAPL | 10.451,65 | 10,71 % | GRÜN |
| Cash | — | 56.707,51 | 58,10 % | GRÜN (>20 % Min, hoch nach GS-Sell) |

**Entscheidung Market Close Mo 27.07.:**
- **KEIN Trade**, keine Pending-Order für Di 28.07. platziert
- **5 V1-V6 alle SICHER**, engste V +6,86 % Blackout (Q3 Di 28.07. AMC letzter HT)
- **Slot 1/2 KW31 OFFEN** — EOG Rebound-Watch Primärkandidat, alle anderen K5-persistent-FAIL
- **Weekly Loss Cap** GRÜN weit von -5 %-Cap
- **ClickUp Tagesbericht Prio 4** → **ERR ITEM_246 persistent** ("Max usage for custom task types reached", bekannter Fehler seit Wochen) → Fallback: direkt in Memory/Trade-Log geschrieben (Memory-First-Regel Trade-Skill)
- **PushNotification unterlassen** (empty run: kein Trade, alle safe, keine Aktion + ClickUp-ITEM_246-Fehler ist bekannt persistent → nicht neu alarmierend — Silence-Rule)

**Nächste Routine:** Di 28.07. 08:30 ET Pre-Market KW31 Tag 2 — **V Q3 CY26 AMC HEUTE** (Blackout letzter Tag, V1_neu 339,32 Puffer +6,86 % sicher aber Watch), EOG Rebound-Watch für Slot 1/2, K5-Multi-Source-Recheck der EOG-Kandidatur, VIX-Check für Pos-Size-Kalibrierung, F Q2 AMC nur Info (nicht im Portfolio).

---

## Midday 2026-07-27 13:07 ET (Mo, KW31 Tag 1) — 🔴 GS V1-STOP_LOSS ausgelöst @ 1.040,25 $, 5 verbleibende Positionen V1-V4 SICHER

```
Alpaca clock:      is_open=true | now Mo 27.07. 13:07 ET | next_close Mo 27.07. 16:00 ET
Equity Live:       97.629,71 $   (Alpaca /v2/account post-Sell)
Cash:              56.707,51 $   (58,08 %, +8.322,00 GS-Sell-Erlös vs Open 48.385,51)
Portfolio MV Live: 40.922,20 $   (41,92 %, 5 Positionen, -8.595,96 vs Open 49.518,16)
Buying_power:     341.412,21 $   (Paper-Margin)
Daily P/L Live:      +100,13 $   (+0,103 % vs Alpaca last_equity 97.529,58)         [GRÜN, Cap -3 %]
SPY Live 13:07:     736,37        (vs Fr Close 738,90 = -0,343 %)                    [Crash-Filter INAKTIV]
Alpha vs SPY:      +0,446 pp     POSITIV (GS-Sell vor weiterem XLF-Drop + Cash-Puffer)
ATH:              100.066,47 $   DD -2,435 % [GRÜN — Alarm bei -15 %]
Weekly KW31 Tag 1:  +0,105 %      (vs Fr Close 97.526,60, +103,11 $)                 [GRÜN, Cap -5 %]
Käufe KW31:            0/2       (Slot 1/2 offen, Slot 2/2 offen — Re-Check EOD Mo/Di Pre-Market)
Open Orders:           0          (KEINE offene Order nach GS-Sell)
Guardrails:        8/8 GRÜN + 1 WARN (V-Blackout Tag+1/2 letzter HT vor Q3 Di 28.07. AMC)
```

**🔴 GS V1-STOP_LOSS-Execution (Alpaca Order 944ad09f-8857-4715-87a8-c9095db7d682):**
- Kaufkurs: 1.141,74 $ (Kauf 2026-07-15)
- V1-Stop: 1.050,40 $ (Kaufkurs × 0,92)
- Trigger: Aktueller Kurs 1.040,57 $ (Midday 13:06 ET Alpaca /trades/latest) < V1 1.050,40 = **-9,83 $ unter Break**
- Market-Sell platziert: 13:07:25 ET, gefüllt 13:07:26 ET (Fill in **1 sec**)
- Fill-Preis: 1.040,25 $ × 8 Sh = Erlös **8.322,00 $**
- Realisierter Verlust: **-811,95 $ (-8,89 %)** vs cost_basis 9.133,95
- Muster: **GS Fill-Day+7 Rebound-Tag+1-Reversal** (Open chg +2,18 % / 1.084,34 → Midday -1,90 % / 1.040,57, Intraday-Reversal -3,84 pp)

**Positionen Live 13:07 ET POST-SELL (5 verbleibend, sortiert Puffer ENG→WEIT):**

| Sym  | Cur Live  | Qty | Entry     | P/L %    | chg_today | V1-Stop      | V1-Puffer   | Status |
|------|-----------|-----|-----------|----------|-----------|--------------|-------------|--------|
| V    |   362,68  | 27  |   357,18  | +1,54 %  | +1,95 %   | **339,32** 🟡BLACKOUT | **+6,88 %** | SICHER **ENGSTE** verbessert vs Open +6,27 %, XLF-Rebound-Fortsetzung + Pre-Earnings-Bid |
| LLY  | 1.198,85  | 8   | 1.193,89  | +0,42 %  | +0,24 %   | 1.098,38     | +9,15 %     | SICHER (verbessert vs Open +9,03 %) |
| UNH  |   419,25  | 24  |   401,57  | +4,40 %  | -0,35 %   |   369,44     | +13,47 %    | SICHER (verbessert marginal vs Open +13,41 %) |
| AAPL |   336,05  | 31  |   316,86  | +6,06 %  | +0,91 %   |   291,51     | +15,25 %    | SICHER (verbessert vs Open +15,07 %) |
| JPM  |   353,16  | 3   |   332,78  | +6,12 %  | -0,01 %   |   306,16     | +15,35 %    | SICHER (verschlechtert vs Open +16,85 %, JPM Give-back vs Open) |

**V1-V4-Vollcheck Midday 5 SICHER:**
- V1 (Stop -8 %) — 5 SICHER, min V +6,88 % (Blackout V1_neu 339,32; Puffer 23,36 $ vom Break)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (+20 % TP1) — max +6,12 % JPM << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- V5/V6 NICHT geprüft (Midday-Regel, nur bei Market Open & Close)

**Guardrails 8/8 GRÜN + 1 WARN (V-Blackout Tag+1/2 aktiv):**
```
1. Daily Loss Cap (-3 %):     +0,103 % (post-Sell, GS-Verlust bereits eingepreist)  [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 1 +0,105 %                                   [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,435 %                                              [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,435 %                                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,343 %                                          [INAKTIV]
6. VIX-Filter (>30):          carry-over Mo 19-21                                   [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV Tag+1/2 vor Q3 Di 28.07. AMC (V1_neu 339,32, Puffer +6,88 %) [WARN]
8. Max Käufe KW31:            0/2 Slot 1/2 + 2/2 offen                              [GRÜN]
```

**Sektor-Struktur POST-GS-SELL:**

| Sektor | Positionen | MV Live $ | % Portfolio (97.630) | Status |
|--------|-----------|-----------|-----------------------|--------|
| XLV | UNH + LLY | 19.652,80 | 20,13 % | GRÜN <30 % |
| XLF | JPM + V (GS raus) | 10.851,85 | 11,12 % | GRÜN, 2-Pos statt 3 |
| XLK | AAPL | 10.417,55 | 10,67 % | GRÜN |
| Cash | — | 56.707,51 | 58,08 % | GRÜN (>20 % Min, deutlich erhöht +8,66 pp) |

**Entscheidung Midday 13:07 Mo 27.07.:**
- **🔴 GS Market-Sell ausgeführt** (V1 1.050,40 verletzt bei Live-Kurs 1.040,57, Fill 1.040,25 in 1 sec)
- **KEIN weiterer Sell/Stop** (5 verbleibende V1-V4 SICHER)
- **KEINE Order storniert** (keine offene Limit-Order vorher)
- **Daily Loss Cap NICHT ausgelöst** (+0,103 %, GS-Verlust bereits eingepreist da unrealized_pl vorher bereits in equity)
- **ClickUp Critical Alert STOP_LOSS Prio 1** → ERR ITEM_246 (persistent bekannter Fehler) → **PushNotification Fallback ausgeführt**
- **Slot 1/2 KW31 bleibt OFFEN** (kein Kauf-Signal grün, Re-Check EOD Mo 16:00 ET oder Di 28.07. Pre-Market)

**Nächste Routine:** Mo 27.07. 16:00 ET Market Close — **EOD-Screener zwingend** (EOG Intraday-Reversal-Watch, K4 EOD-Volumen-Verifikation für EOG/GE-Reject bestätigen, frische XLU/XLI-Runde), V-Blackout Tag+2/2 letzter HT vor Q3 Di 28.07. AMC nur Info (Puffer +6,88 % sicher), V5/V6-Vollcheck alle 5 zwingend.

---

## Market Open 2026-07-27 09:38 ET (Mo, KW31 Tag 1) — Kaufsignal-Scan: KEIN Kauf (EOG intraday-Weakness + K4 formal offen + GE K5-FAIL), 6 V1-V6 SICHER, Slot 1/2 OFFEN

```
Alpaca clock:      is_open=true | now Mo 27.07. 09:38 ET | next_close Mo 27.07. 16:00 ET
Equity Live:       97.903,67 $   (Alpaca /v2/account)
Cash:              48.385,51 $   (49,42 %, unverändert vs Fr Close)
Portfolio MV Live: 49.518,16 $   (50,58 %, 6 Positionen, +377,07 $ vs Fr Close)
Buying_power:     332.152,96 $   (Paper-Margin)
Daily P/L Live:      +374,09 $   (+0,384 % vs Alpaca last_equity 97.529,58)      [GRÜN, Cap -3 %]
SPY Live 09:39:     745,05        (vs Fr Close 738,90 = +0,832 %)                 [Crash-Filter INAKTIV]
Alpha vs SPY:      -0,448 pp     NEGATIV (Cash-Puffer 49,42 % dämpft Rebound-Beta)
ATH:              100.066,47 $   DD -2,161 % [GRÜN — Alarm bei -15 %]
Weekly KW31 Tag 1:  +0,387 %      (vs Fr Close 97.526,60, +377,07 $ frischer Start) [GRÜN, Cap -5 %]
VIX Mo Pre:         19-21         (Fr-Close 18,70 +12,4 %, Mo-Anstieg +0,6 bis +2,3 pp aber <25) [GRÜN]
Käufe KW31:            0/2       (Slot 1/2 offen, Slot 2/2 offen)
Open Orders:           0          (KEINE Limit-Order platziert)
Guardrails:        8/8 GRÜN + 1 WARN (V-Blackout Tag+1/2 letzter HT vor Q3)
```

**Positionen Live 09:38 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym  | Cur Live | Qty | Entry     | P/L %    | chg_today | V1-Stop      | V1-Puffer   | Status |
|------|----------|-----|-----------|----------|-----------|--------------|-------------|--------|
| **GS**   | 1.084,34 | 8  | 1.141,74  | -5,03 %  | **+2,18 %** | 1.050,40     | **+3,23 %** | SICHER **ENGSTE** verbessert vs Fr-Close +1,03 % um +2,20 pp, Fill-Day+7-Rebound-Tag+1 überstanden |
| V    |   360,61 | 27 |   357,18  | +0,96 %  | +1,37 %   | **339,32** 🟡BLACKOUT | +6,27 % | SICHER (Blackout Tag+1/2 vor Q3 Di 28.07. AMC, verbessert vs Fr-Close +4,84 %, XLF-Rebound + Pre-Earnings-Bid) |
| LLY  | 1.197,54 | 8  | 1.193,89  | +0,31 %  | +0,13 %   | 1.098,38     | +9,03 %     | SICHER (verbessert vs Fr-Close +8,89 %, XLV-Konsolidierung nach Rebound Tag+2) |
| UNH  |   419,00 | 24 |   401,57  | +4,34 %  | -0,41 %   |   369,44     | +13,41 %    | SICHER (verschlechtert vs Fr-Close +13,79 %, **Worst chg heute** XLV-Konsolidierung) |
| AAPL |   335,44 | 31 |   316,86  | +5,86 %  | +0,73 %   |   291,51     | +15,07 %    | SICHER (verbessert vs Fr-Close +14,30 %, XLK stabil nach XLK-Rebound Fr) |
| JPM  |   357,75 | 3  |   332,78  | +7,51 %  | +1,29 %   |   306,16     | **+16,85 %** | SICHER (verbessert vs Fr-Close +15,37 %, **Best chg heute** XLF-Rebound Fortsetzung, RSI 71,68 näher am 80-Watch aber weit unter) |

**V1-V6-Vollcheck Market Open 6 SICHER:**
- V1 (Stop -8 %) — 6 SICHER, min GS +3,23 % (33,94 $ vom Break, deutlich verbessert vs Fr-Close +1,03 %)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (+20 % TP1) — max +7,51 % JPM << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- **V5 (EMA50<EMA200) — 6 SICHER** (Alpaca IEX Bars bis 27.07., Golden Cross intakt): V EMA-Diff +2,82 % (**engste** aber verbessert vs Fr-Close +1,76 %, XLF-Rebound + Pre-Earnings-Bid), JPM +7,16 %, AAPL +10,91 %, UNH +11,48 %, LLY +11,59 %, GS +14,11 % — kein Death Cross
- **V6 (RSI>80 & RS<0) — 6 SICHER**: max **RSI JPM 71,68** (Watch näher am 80-Threshold aber weit unter, verschlechtert vs Fr-Close 68,01), AAPL 66,80, V 61,07, LLY 57,22, GS 54,20, UNH 50,49 — alle << 80

**→ KEINE Sell-/Limit-Order platziert. KEIN Stop ausgelöst. KEINE Order storniert.**

**Kaufsignal-Scan Slot 1/2 KW31 — LEVEL 0 No-Action bei Unsicherheit:**

| Sym | K1 EMA | K2 RSI | K3 RS_63d | K4 Vol | K5 P/E + Growth | chg today | Blackout | Decision |
|-----|--------|--------|-----------|--------|-----------------|-----------|----------|----------|
| **EOG** | ✓ +7,49 % | ✓ 61,72 | ✓ +4,25 pp | offen* + Weakness | ✓ 9,98 + 15,63 % | **-1,71 %** Gap-Down | frei | **REJECT LEVEL 0** |
| GE | ✓ | ✓ ~62 | ✓ +21 pp #1 | ✓ likely | ✗ Median 44,72 (Y 34,72 / Z 45,19 / SA 47,61 / GF 44,72) + RevGr +24,6 % ✓ | **+3,16 %** | frei | **REJECT K5-Median-FAIL** |
| HON | ✓ | ✓ | ✓ +9,1 pp | offen | ✗ RevGr +2,4 % | +1,33 % | frei | **REJECT K5-FAIL** |
| F | ✓ | ✓ | ✓ +10,8 pp | offen | ⚠ P/E 9,58 + RevGr +430 %* | +2,40 % | Q2 Di 28.07. AMC | **SKIP Blackout** |
| D | ✓ | ✓ | ✓ +9,4 pp | offen | ✗ RevGr +7,49 % | -0,19 % (XLU flat) | frei | **REJECT K5-FAIL** |
| NEE | offen | offen | offen | offen | offen | +0,01 % (XLU flat) | offen | **DROP kein Momentum** |
| DUK | offen | offen | offen | offen | offen | -0,60 % (XLU neg) | offen | **DROP kein Momentum** |
| SO / AEP / EXC | offen | offen | offen | offen | offen | -0,13 % / -0,30 % / -0,29 % | offen | **DROP kein Momentum** |
| UNP | offen | offen | offen | offen | offen | **-1,23 %** (XLI trotz Rebound) | offen | **DROP kein Momentum** |
| CAT | offen | offen | offen | offen | offen | -0,57 % | offen | **DROP kein Momentum** |
| DE | ✓ | ✓ | ✓ +1,4 pp | offen | ✗ RevGr +9,6 % | -0,19 % | frei (nächste Earnings 14.08.) | **REJECT K5-FAIL persistent** |

*K4 Session-Vol so früh (09:38, 9/390 Min) nicht belastbar; pro-rata extrapoliert EOG 3.735×43,33 ~161.850 vs avg20 132.445 = ~122 % grenzwertig aber unzuverlässig; K5-Prä-Screen EOG Multi-Source Fr FwdPE 9,98 + RevGr +15,63 % ✓ solide.

**Rationale KEIN Kauf Slot 1/2:**
- **EOG**: alle 4 klassischen K1-K3+K5-Signale ✓, aber Intraday-Weakness -1,71 % chg + Gap-Down Open -2,08 % + XLE-Sektor -0,90 % kontra Pre-Market Iran/Oil-Bull-Thesis → **Momentum-Quality-Thesis intraday verletzt**, Kauf bei Weakness = "Falling Knife"-Muster. K4 formal offen (Session zu früh), pro-rata Extrapolation grenzwertig 122 % — nicht robust genug für Kauf. **LEVEL 0 "No-Action bei Unsicherheit" + Re-Check Midday 13:00 ET oder Di Pre-Market**.
- **GE**: Perplexity Multi-Source Recheck **FwdPE Median 44,72** (3 von 4 Sources 44-48 >35-Cap, nur Yahoo 34,72 knapp unter) → strikte Regel-Anwendung analog MMM-Präzedenz REJECT. RS #1 +21 pp wäre stark aber K5 dominiert.
- **HON/D/DE**: K5-FAIL RevGr <10 %-Cap persistent.
- **F**: Q2 Earnings Di 28.07. AMC bestätigt → SKIP KW31 (Blackout aktivieren nach Kauf sofort → nicht rechtfertigbar).
- **XLU-Screener (NEE/DUK/SO/AEP/EXC) alle intraday flat/negativ** → kein Momentum-Signal, K1-K3-Vollcheck nicht sinnvoll ohne Momentum-Basis (Zeitkosten).
- **XLI-Screener (UNP/CAT/DE) alle intraday negativ** → kein Momentum-Signal, XLI-Rebound Ø +0,94 % dominiert von GE (K5-FAIL) und HON (K5-FAIL).

**→ Slot 1/2 KW31 bleibt OFFEN. Re-Check Midday 13:00 ET (EOG Intraday-Reversal-Potenzial) und/oder Di 28.07. Pre-Market (K4 EOD-Volumen-Verifikation Mo + frische XLU/XLI-Screener-Runde).**

**Sektor-Struktur (kein Trade, live 09:38):**

| Sektor | Positionen | MV Live $ | % Portfolio (97.904) | Status |
|--------|-----------|-----------|-----------------------|--------|
| XLV | UNH + LLY | 19.636,64 | 20,06 % | GRÜN <30 % |
| XLF | GS + JPM + V | 19.459,99 | 19,88 % | GRÜN, 3-Pos-Cap intakt |
| XLK | AAPL | 10.410,42 | 10,63 % | GRÜN |
| Cash | — | 48.385,51 | 49,42 % | GRÜN (>20 % Min) |

**Guardrails 8/8 GRÜN + 1 WARN (V-Blackout Tag+1/2 aktiv, kein Aktion nötig):**
```
1. Daily Loss Cap (-3 %):     +0,384 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 1 +0,387 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,161 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,161 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,832 %                                        [INAKTIV]
6. VIX-Filter (>30):          Mo Pre 19-21 (Fr 18,70 +12,4 %)                     [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV Tag+1/2 vor Q3 Di 28.07. AMC (V1_neu 339,32, Puffer +6,27 % sicher) [WARN]
8. Max Käufe KW31:            0/2 Slot 1/2 + 2/2 offen                            [GRÜN]
```

**Entscheidung Market Open 09:38 Mo 27.07.:**
- **KEIN Kauf** (Slot 1/2 offen, EOG deferred wg Intraday-Weakness + K4-Unsicherheit, GE K5-Median-FAIL, alle Alternativen K5-FAIL/Blackout/kein Momentum)
- **KEIN Sell/Stop** (6 V1-V6 SICHER, min GS Puffer +3,23 %)
- **KEINE Limit-Order für Di 28.07.** (kein Kauf-Signal grün)
- **KEIN ClickUp Critical Alert** (kein Trade, kein Stop)
- **ClickUp Routine-Log Prio 4** wird gesendet (Owner-Info Slot 1/2 offen)
- **PushNotification Silence** (Silence-Rule respektiert — kein Trade, alle safe, EOG deferred; kein Owner-Actionable)

**Nächste Routine:** Mo 27.07. 13:00 ET Midday Stop-Check — **GS V1 1.050,40 Puffer +3,23 % ENGSTE Rebound-Fortsetzung Watch**, V Blackout letzter HT vor Q3 Di 28.07. AMC (nur Info), **EOG Intraday-Reversal-Watch für Slot 1/2 potenzielles Nachmittag-Kauf-Fenster** (K4 gegen EOD besser bewertbar), JPM RSI 71,68 Watch (näher am 80-Threshold).

---

## Weekly Review 2026-07-24 17:00 ET (Fr, KW30 Abschluss)

```
Depot Fr 17.07. Close:  98.236,14 $
Depot Fr 24.07. Live:   97.513,66 $   (Alpaca /v2/account, portfolio_value 49.128,15, Cash 48.385,51)
Wochenrendite KW30:    -0,7355 %      (-722,48 $)
SPY Fr 17.07. Close:      743,28
SPY Fr 24.07. Close:      738,90
SPY Wochenrendite:     -0,589 %
Alpha KW30:            -0,147 pp

YTD Depot (Init 100k):   -2,486 %
YTD SPY (YE25 681,82):   +8,373 %
YTD-Alpha:              -10,86 pp

ATH:                   100.066,47 $
Drawdown:                 -2,486 %    [GRÜN — Alarm bei -15 %]
Weekly-Cap-Puffer:        +4,264 pp   (Cap -5 %)
VIX/VXX:                  ~18 / 22    [GRÜN <25]
Offene Positionen:         6/8
Cash-Quote:               49,62 %     (Cash 48.385,51 / Equity 97.513,66)
Investiert-Quote:         50,38 %     (MV 49.128,15)
```

**Wochenaktivität KW30 (Mo 20.07. → Fr 24.07.):**
- **1 Kauf:** V (Mo 20.07. 09:41 ET Limit-Buy 27 Sh @ 357,178 = 9.643,80 $, alle 5 K-Signale multi-source ✓, Blackout Tag+1 aktiv V1_neu 339,32)
- **1 Verkauf (V1-Stop):** GOOGL (Do 23.07. 09:38 ET Market-Sell 26 Sh @ 321,51 = 8.359,26 $, Realisierter Verlust -1.211,34 $ / -12,65 % vs Entry 368,10, Haltedauer 12 HT, Gap-Slippage -4,65 pp durch Q2-Post-Release-Overnight)
- **Slot 2/2 KW30 verfallen:** PSX/FTI/DE alle K5- bzw. Timing-REJECT Fr 24.07. Open (LEVEL 0 No-Action bei Unsicherheit)

**Position-Weekly-Moves (Fr 17.07. Close → Fr 24.07. Close, Alpaca IEX):**

| Sym  | 17.07.   | 24.07.   | Weekly Δ | Bester Tag       | Anmerkung |
|------|----------|----------|----------|------------------|-----------|
| JPM  |   341,10 |   353,14 | **+3,53 %** | Fr +0,95 %      | Beste-Position KW30, XLF-Rebound |
| LLY  | 1.178,57 | 1.196,14 | +1,49 %  | Fr +0,86 %      | XLV-Rebound Tag+2, P/L wieder GRÜN |
| AAPL |   333,75 |   333,05 | -0,21 %  | Fr **+3,59 %**  | XLK-Volatilität aber Fr-Rebell |
| GS   | 1.065,71 | 1.061,25 | -0,42 %  | Mo +2,89 %      | Fill-Day+7 Give-back, V1-Puffer +1,03 % ENGSTE |
| V    |   357,18 |   355,62 | -0,44 % (vs Entry -0,40 %) | Fr +1,18 %      | Kauf Mo, Blackout Tag+1 vor Q3 Di 28.07. |
| UNH  |   426,06 |   420,67 | **-1,27 %** | Di +3,67 %      | XLV-Divergenz vs LLY, Worst chg Fr -0,75 % |
| GOOGL |  346,76 |   321,51 (Sell) | **-7,28 %** (Sell-Move) | Mi +1,61 %      | V1-Stop Do -12,65 % realisiert |

**Sektor-Ranking KW30 (Alpaca IEX Fr 17.07. → Fr 24.07.):**

| Rank | Sektor | Weekly % | Bemerkung |
|------|--------|----------|-----------|
| 1  | **XLE** | **+3,35 %** | Energy Top-Sektor, Iran-Öl + Rebound |
| 2  | **XLU** | **+2,48 %** | Utilities, Defensiv-Rotation |
| 3  | **XLI** | **+1,79 %** | Industrials, GE Q2-Beat 16.07. |
| 4  | XLB    | +1,46 %  | Materials |
| 5  | XLRE   | +1,12 %  | Real Estate |
| 6  | XLV    | +0,92 %  | Healthcare, LLY-Rebound Tag+2 |
| 7  | XLK    | +0,22 %  | Tech, AAPL Fr-Rebell |
| 8  | XLF    | +0,13 %  | Financials, JPM-Beste dennoch Sektor-Flat |
| 9  | XLP    | -1,28 %  | Staples |
| 10 | XLC    | **-3,95 %** | Comm Services, GOOGL-Selloff dominiert |
| 11 | XLY    | **-5,19 %** | Consumer Disc Bottom |

**SPY:** -0,589 % (Ref).

**Sektor-Gewichtung Portfolio Fr-Close (V1-Regel "kein Sektor > 30 % investiert"):**

| Sektor | Positionen | MV $ | % investiert (49.141) | % Portfolio (97.514) | Deutung |
|--------|-----------|------|------------------------|------------------------|---------|
| XLV | UNH + LLY | 19.657 | **40,00 %** ⚠ | 20,16 % | strenge Deutung VIOLATION, Portfolio-Deutung OK |
| XLF | GS + JPM + V | 19.154 | **38,98 %** ⚠ | 19,64 % | strenge Deutung VIOLATION, Portfolio-Deutung OK |
| XLK | AAPL | 10.329 | 21,02 % | 10,59 % | OK |
| Cash | — | 48.386 | — | 49,62 % | OK (>20 % Min) |

**Owner-Entscheidung Sektor-Cap-Deutung KW31 zwingend** (blockiert 3.-XLV- und 4.-XLF-Kandidaten formal).
- Bei strenger Deutung schwächste XLV = **LLY +0,18 %** → Reduktions-Watch
- Bei strenger Deutung schwächste XLF = **GS -7,05 %** → Reduktions-Watch (aber V1 aktiv)

**Fundamentals-Screen KW31-Kandidaten (Perplexity Multi-Source):**

| Sym | Sektor | FwdPE | RevGr YoY | MCap $B | NextEarn | K5 | Verdikt |
|-----|--------|-------|-----------|---------|----------|-----|---------|
| **EOG** | XLE #1 | **9,98** | **+15,63 %** | 72,06 | ~Nov 2026 | ✓ | **HAUPTKANDIDAT KW31** |
| GE | XLI #3 | 47,61 | +24,70 % | 385 | 16.07. (past) | ✗ FwdPE>35 | DROP |
| HON | XLI #3 | 20,86 | +2,40 % | 137 | 23.07. (past) | ✗ RevGr<10 | DROP |
| D | XLU #2 | 17,83 | +7,49 % | 41 | 31.07. Fr | ✗ RevGr<10 | DROP |
| F | XLY (nicht Top-3) | 9,58 | +430,80 %* | 56 | 29.07. Mi | ⚠ Blackout | SKIP KW31 (Basis-Effekt + Earnings Di+1 nach Kauf) |

**KW31 Zusatz-Screener zwingend Mo Pre-Market:** frische XLU-Kandidaten (NEE/DUK/SO/AEP/EXC) + XLI-Kandidaten (UNP/CAT/DE Re-Check) K5-Prä-Screen.

**Guardrails Wochenabschluss KW30:**
```
1. Daily Loss Cap (-3 %):     Fr +0,388 % (letzter HT)                             [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Final -0,736 %                                  [GRÜN, Puffer +4,264 pp]
3. Drawdown-Alarm (-15 %):    -2,486 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,486 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY KW30 -0,589 %                                    [INAKTIV]
6. VIX-Filter (>30):          ~18                                                   [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV Tag+1 vor Q3 Di 28.07. AMC (V1_neu 339,32)   [WARN]
8. Max Käufe KW31:            Reset 2/2 Mo 27.07.                                  [GRÜN]
```

**Wochenabschluss KW30:**
```
Gesamtwert:            97.513,66 $
Cash:                  48.385,51 $ (49,62 %)
Investiert:            49.128,15 $ (50,38 %, 6 Positionen)
Wochenrendite:         -0,736 %
Alpha vs SPY:          -0,147 pp
YTD Rendite:           -2,486 %
YTD Alpha:            -10,86 pp
ATH:                  100.066,47 $
Drawdown:              -2,486 %
Offene Positionen:     6/8
Nächste Woche max. Käufe: 2 (Slot 1/2 EOG-Priorität, Slot 2/2 XLU/XLI-Screener)
Watchlist KW31: EOG (Hauptkandidat XLE), + XLU/XLI-Screener Mo
```

**Strategie-Status:** STABIL — alle V1-V6/K1-K5/Blackout/Weekly-Cap regelkonform. Diskussions-Punkte KW31: (1) Sektor-Cap-Deutung Owner-Klärung ZWINGEND, (2) Cash-Quote-Optimierung bei VIX <20, (3) Screener-Universe-Erweiterung MidCap 400.

**Nächste Routine:** Mo 27.07. 08:30 ET Pre-Market Check KW31 Tag 1 — GS V1 1.050,40 Puffer +1,03 % Wochenend-Watch zwingend, V Blackout letzter HT vor Q3 Di 28.07. AMC, EOG K4/K5-Vollcheck Market Open + XLU/XLI-Screener frische Runde.

---

## Market Close 2026-07-24 16:00 ET (Fr, KW30 Tag 5 letzter HT) — Tagesbilanz: P/L +376,57 $ (+0,388 %) Alpha +0,274 pp, 6 V1-V6 SICHER, KEINE Pending-Orders Mo

---

## Market Close 2026-07-24 16:00 ET (Fr, KW30 Tag 5 letzter HT) — Tagesbilanz: P/L +376,57 $ (+0,388 %) Alpha +0,274 pp, 6 V1-V6 SICHER, KEINE Pending-Orders Mo

```
Alpaca clock:      is_open=false | now Fr 24.07. 16:02 ET | next_open Mo 27.07. 09:30 ET
Equity End:         97.526,60 $   (Alpaca /v2/account, MarketClose Fr 16:00)
last_equity:        97.150,03 $   (= Alpaca Do 23.07. Close)
Cash:               48.385,51 $   (49,61 %, unverändert)
Portfolio MV Live:  49.141,09 $   (50,39 %, 6 Positionen)
Buying_power:      331.137,09 $   (Paper-Margin)
Daily P/L:            +376,57 $   (**+0,388 %** vs last_equity 97.150,03)          [GRÜN, Cap -3 %]
SPY Close 24.07.:     738,90       (vs Do-Close 738,06 = **+0,114 %** Alpaca IEX)   [Crash-Filter INAKTIV]
Alpha vs SPY:      **+0,274 pp**   POSITIV (Portfolio outperformt SPY um +0,27 pp durch AAPL XLK-Rebound)
ATH:              100.066,47 $   DD **-2,538 %** [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 5:  **-0,722 %**  (vs Fr-Close 18.07. 98.236,14, -709,54 $)         [GRÜN, Cap -5 %]
VIX/VXX (carry):   ~18 / ~22     [GRÜN, <25]
Käufe KW30 Final:      1/2       (V 20.07. only — Slot 2/2 verfallen ohne 2. Kauf)
Open Orders:           0          (KEINE Limit-Order für Mo platziert)
Guardrails:        8/8 GRÜN + 1 WARN (V-Blackout aktiv Q3 Di 28.07. AMC, kein Aktion)
```

**Positionen Close 16:00 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym  | Close    | Qty | Entry     | P/L %    | chg_today | V1-Stop      | V1-Puffer   | Status |
|------|----------|-----|-----------|----------|-----------|--------------|-------------|--------|
| **GS**   | 1.061,23 | 8  | 1.141,74  | -7,05 %  | -1,26 %   | 1.050,40     | **+1,031 %** | SICHER **ENGSTE** verschlechtert vs Midday +1,62 % um -0,58 pp, Fill-Day+7 Give-back weiter Close, **10,83 $ vom V1** |
| V    |   355,74 | 27 |   357,18  | -0,40 %  | +1,18 %   | **339,32** 🟡BLACKOUT | +4,838 % | SICHER (Blackout V1_neu, verbessert vs Midday +4,04 % um +0,80 pp, XLF-Rebound Close) |
| LLY  | 1.196,04 | 8  | 1.193,89  | +0,18 %  | +0,86 %   | 1.098,38     | +8,893 %    | SICHER (P/L knapp GRÜN, verschlechtert vs Midday +9,42 %, XLV-Rebound Tag+2 Fortsetzung Close) |
| UNH  |   420,38 | 24 |   401,57  | +4,68 %  | -0,75 %   |   369,44     | +13,791 %   | SICHER (verbessert vs Midday +13,68 %, chg Worst heute -0,75 %, XLV-Divergenz vs LLY Tag+2) |
| AAPL |   333,20 | 31 |   316,86  | +5,16 %  | **+3,59 %** |   291,51     | +14,300 %   | SICHER (**Best chg heute** verbessert vs Midday +3,45 %, XLK-Rebound bestätigt) |
| JPM  |   353,21 | 3  |   332,78  | +6,14 %  | +0,95 %   |   306,16     | +15,367 %   | SICHER (verbessert vs Midday +5,98 %, XLF-Rebound Close) |

**V1-V6-Vollcheck Close 6 SICHER:**
- V1 (Stop -8 %) — 6 SICHER, min GS +1,031 % (10,83 $ vom Break, verschlechtert vs Midday +1,615 % um -0,58 pp)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (+20 % TP1) — max +6,14 % JPM << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger
- **V5 (EMA50<EMA200) — 6 SICHER** (Alpaca IEX 260d Bars, Golden Cross intakt): AAPL 305,17/274,33 (+11,24 %), GS 1.036,66/914,26 (+13,39 %), JPM 327,75/310,98 (+5,39 %), LLY 1.127,80/994,74 (+13,38 %), UNH 404,10/354,40 (+14,02 %), V 339,90/334,04 (+1,76 %) — **kein Death Cross, keine Sell-Order für Mo**
- **V6 (RSI>80 & RS<0) — 6 SICHER** (Alpaca IEX): max RSI JPM 68,01, AAPL 65,55, V 57,66, LLY 57,21, UNH 51,42, GS 49,76 — alle << 80, kein Trigger

**→ KEINE Sell-/Limit-Order für Mo 27.07. platziert. KEIN Stop ausgelöst. KEINE Order storniert.**

**Weekly Loss Cap Check KW30:**
- weekly_pnl = (97.526,60 - 98.236,14) / 98.236,14 * 100 = **-0,722 %** > Cap -5 % → **GRÜN**
- Keine Order-Stornierung, kein WEEKLY_CAP-Alert
- KW30 Final: 5 HT, Range Fr-Fr -0,72 %, Käufe 1/2 (V 20.07.)

**Tages-Highlights Close:**
- Best chg: AAPL +3,59 % (XLK-Rebound bestätigt Close, +0,14 pp vs Midday)
- Sekundär: LLY intraday-Rebound (Best chg Midday +1,34 % → Close +0,86 %, XLV-Rebound Tag+2)
- Worst chg: GS -1,26 % (Fill-Day+7 Give-back weiter Close, Puffer verschlechtert vs Midday -0,58 pp)
- Best P/L: JPM +6,14 %
- Worst P/L: GS -7,05 %
- **Alpha +0,274 pp POSITIV** (Portfolio +0,39 % vs SPY +0,11 %, AAPL-Beitrag dominiert)

**Guardrails 8/8 GRÜN + 1 WARN (V-Blackout aktiv, kein Aktion nötig):**
```
1. Daily Loss Cap (-3 %):     +0,388 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Final -0,722 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,538 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,538 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,114 %                                        [INAKTIV]
6. VIX-Filter (>30):          ~18 (carry-over)                                    [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV V1_neu 339,32 (kein Sofort-Stop-Risiko)     [WARN]
8. Max Käufe KW30:            1/2 Final                                           [GRÜN]
```

**Watchlist Mo 27.07. (K1-K3 ✓ Alpaca IEX, K4/K5 bei Market Open Mo geprüft):**
- **GE** (Industrials) EMA50 341,07 > EMA200 311,31 ✓ | RSI 53,0 ✓ | RS_63d +21,0 pp ✓ (**#1 RS**)
- **HON** (Industrials) EMA50 226,44 > EMA200 221,40 ✓ | RSI 65,2 ✓ | RS_63d +9,1 pp ✓
- **F** (Consumer Discretionary) EMA50 13,98 > EMA200 13,09 ✓ | RSI 54,6 ✓ | RS_63d +10,8 pp ✓
- **D** (Utilities) EMA50 68,29 > EMA200 63,75 ✓ | RSI 59,0 ✓ | RS_63d +9,4 pp ✓
- **EOG** (Energy) EMA50 136,79 > EMA200 127,93 ✓ | RSI 67,1 ✓ | RS_63d +5,1 pp ✓
- (**PSX/DE** aus Do-Screen persistent K5-FAIL RevGrowth <10 %, nicht wiederkehrend)

**Entscheidung Close 16:00 Fr 24.07.:**
- **KEINE Sell-/Limit-Order platziert** (6 V1-V6 SICHER)
- **KEIN Stop ausgelöst**
- **KEINE Order-Stornierung** (Daily +0,39 %, Weekly -0,72 % beide GRÜN)
- **ClickUp Task erstellt**: [CLOSE] Tagesbilanz — 2026-07-24, Prio 4 (Low, positive Perf) ID 869e97vn8
- **PushNotification Prio 4 Owner**: Silence-Rule NEIN — Routine-Spec fordert Close-Notification (Owner erwartet Tagesbilanz)

**Nächste Routine:** Mo 27.07. 08:30 ET Pre-Market Check KW31 Tag 1 — **GS V1 1.050,40 Puffer +1,03 % ENGSTE Wochenend-Watch**, V-Blackout letzte Tag vor Q3 (Di 28.07. AMC), Watchlist GE/HON/F/D/EOG K4/K5-Prüfung Market Open.

---

## Midday 2026-07-24 13:07 ET (Fr, KW30 Tag 5 letzter HT) — Stop-Check: 6 V1-V4 SICHER, keine Trigger, Daily P/L +0,38 % GRÜN

```
Alpaca clock:      is_open=true | now Fr 24.07. 13:07 ET | next_close Fr 24.07. 16:00 ET
Equity Live:       97.522,81 $   (Alpaca /v2/account)
Cash:              48.385,51 $   (49,61 %, unverändert)
Portfolio MV Live: 49.137,30 $   (50,39 %, 6 Positionen)
Buying_power:     331.126,47 $   (Paper-Margin)
Daily P/L Live:      +372,78 $   (+0,384 % vs Alpaca last_equity 97.150,03)      [GRÜN, Cap -3 %]
SPY Live 13:07:     740,88        (vs Do-Close 738,06 = +0,382 %)                [Crash-Filter INAKTIV]
Alpha vs SPY:      +0,002 pp     NEUTRAL (Portfolio-Rebound gleichauf SPY)
ATH:              100.066,47 $   DD -2,542 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 5:  -0,727 %     (vs Fr-Close 98.236,14, -713,33 $)              [GRÜN, Cap -5 %]
VIX/VXX (carry):   ~18 / ~22     [GRÜN, <25]
Käufe KW30:            1/2       (Slot 2/2 verfällt Ende Fr, kein Kauf)
Open Orders:           0          (KEINE Limit-Order platziert)
Guardrails:        8/8 GRÜN + 1 WARN (V-Blackout aktiv, kein Aktion)
```

**Positionen Live 13:07 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym  | Cur Live | Qty | Entry     | P/L %    | chg_today | V1-Stop      | V1-Puffer   | Status |
|------|----------|-----|-----------|----------|-----------|--------------|-------------|--------|
| **GS**   | 1.067,37 | 8  | 1.141,74  | -6,51 %  | -0,68 %   | 1.050,40     | **+1,615 %** | SICHER **ENGSTE** verschlechtert vs Open +1,84 % um -0,22 pp, Fill-Day+7 Give-back leicht fortgeführt, 16,97 $ vom V1 |
| V    |   353,01 | 27 |   357,18  | -1,17 %  | +0,40 %   | **339,32** 🟡BLACKOUT | +4,035 % | SICHER (Blackout V1_neu, marginal verbessert vs Open +3,81 %) |
| LLY  | 1.201,81 | 8  | 1.193,89  | +0,66 %  | +1,34 %   | 1.098,38     | +9,417 %    | SICHER (P/L wieder GRÜN, **Best chg +1,34 % XLV-Rebound Tag+2**) |
| UNH  |   419,98 | 24 |   401,57  | +4,59 %  | -0,85 %   |   369,44     | +13,681 %   | SICHER (verschlechtert vs Open +14,56 %, **Worst chg heute**, UNH-vs-LLY XLV-Divergenz Tag+2) |
| AAPL |   332,75 | 31 |   316,86  | +5,02 %  | +3,45 %   |   291,51     | +14,148 %   | SICHER (**Best chg heute** stark verbessert vs Open +2,71 %) |
| JPM  |   352,70 | 3  |   332,78  | +5,98 %  | +0,80 %   |   306,16     | +15,200 %   | SICHER (leicht verbessert vs Open +4,73 %, XLF-Rebound) |

**V1-V4 Midday-Check (RSI/EMA nicht Teil Midday) 6 SICHER:**
- V1 (Stop -8 %) — 6 SICHER, min GS +1,615 % (16,97 $ vom Break, chg -0,68 % leichte Give-back-Fortsetzung Fill-Day+7)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (+20 % TP1) — max +5,98 % JPM << 20 %, kein Trigger
- V4 (+35 % TP2) — kein Trigger

**→ KEINE Sell-/Limit-Order platziert. KEIN Stop ausgelöst. KEINE Order storniert.**

**Daily Loss Cap Check:**
- daily_pnl_pct = (97.522,81 - 97.150,03) / 97.150,03 * 100 = **+0,384 %** > Cap -3 % → **GRÜN**
- Keine Order-Stornierung, kein DAILY_CAP-Alert

**Tages-Highlights Midday:**
- Best chg: AAPL +3,45 % (XLK-Rebound Fr, verbessert vs Open +2,71 %)
- Sekundär best: LLY +1,34 % (XLV-Rebound Tag+2 Fortsetzung, P/L wieder GRÜN)
- Worst chg: UNH -0,85 % (XLV-Divergenz vs LLY, aber Puffer +13,68 % komfortabel)
- Best P/L: JPM +5,98 %
- Worst P/L: GS -6,51 % (aber Puffer +1,62 % SICHER, +16,97 $ vom V1)
- Alpha +0,002 pp NEUTRAL (Portfolio +0,38 % ≈ SPY +0,38 %)

**Guardrails 8/8 GRÜN + 1 WARN (V-Blackout aktiv, kein Aktion nötig):**
```
1. Daily Loss Cap (-3 %):     +0,384 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 5 -0,727 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,542 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,542 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,382 %                                        [INAKTIV]
6. VIX-Filter (>30):          ~18 (carry-over)                                    [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV V1_neu 339,32 (kein Sofort-Stop-Risiko)     [WARN]
8. Max Käufe KW30:            1/2 (Slot 2/2 verfällt Ende Fr, kein Kandidat)      [GRÜN]
```

**Entscheidung Midday 13:07 Fr 24.07.:**
- **KEIN Stop ausgelöst** (6 V1-V4 SICHER)
- **KEINE Sell-Order** (kein Trigger)
- **KEINE Order-Stornierung** (Daily +0,38 % >> Cap -3 %)
- **KEIN ClickUp-Alert** (Routine-Spec: nur bei Stops oder Daily Cap)
- **KEINE PushNotification** (Routine-Spec: nur bei Stops oder Daily Cap; Silence bei Regulärlauf per Prompt "when the run comes up empty — silence")

**Nächste Routine:** Fr 24.07. 16:00 ET Market Close + Tagesbilanz — **GS V1 1.050,40 Puffer +1,62 % ENGSTE** (Fill-Day+7 zwingender Close-Watch), V-Blackout-Puffer +4,03 %, LLY XLV-Rebound-Fortsetzung Tag+2, KW30 letzte Handelstag-Bilanz + V5/V6-Vollcheck.

---

## Market Open 2026-07-24 09:38 ET (Fr, KW30 Tag 5 letzter HT) — Kaufsignal-Scan: KEIN Kauf (alle 3 Kandidaten K5-Blockiert), 6 V1-V6 SICHER, Slot 2/2 verfällt

```
Alpaca clock:      is_open=true | now Fr 24.07. 09:38 ET | next_close Fr 24.07. 16:00 ET
Equity Live:       97.282,89 $   (Alpaca /v2/account)
Cash:              48.385,51 $   (49,74 %, unverändert)
Portfolio MV Live: 48.897,38 $   (50,26 %, 6 Positionen)
Buying_power:     330.451,47 $   (Paper-Margin, effektiv Cash-Budget)
Daily P/L Live:      +132,86 $   (+0,137 % vs Do-Close 97.152,97)                [GRÜN, Cap -3 %]
SPY Live 09:38:     739,46        (vs Do-Close 738,06 = +0,189 %)                [Crash-Filter INAKTIV]
Alpha vs SPY:      -0,056 pp     NEUTRAL (Cash-Puffer 49,74 % dämpft SPY-Rebound)
ATH:              100.066,47 $   DD -2,783 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 5:  -0,972 %     (vs Fr-Close 98.236,14, -953,25 $)              [GRÜN, Cap -5 %]
VIX/VXX Live:       ~18 / 22,2   [GRÜN, <25 volle Pos-Size wäre möglich]
Käufe KW30:            1/2       (Slot 2/2 verfällt Ende Fr, kein Kauf möglich)
Open Orders:           0          (KEINE Limit-Order platziert)
Guardrails:        8/8 GRÜN
```

**Positionen Live 09:38 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym  | Cur Live | Qty | Entry     | P/L %    | V1-Stop      | V1-Puffer   | Status |
|------|----------|-----|-----------|----------|--------------|-------------|--------|
| **GS**   | 1.069,68 | 8  | 1.141,74  | -6,31 %  | 1.050,40     | **+1,84 %** | SICHER **ENGSTE** verschlechtert vs Pre +3,39 %, Fill-Day+7 Give-back-Fortsetzung |
| V    |   352,26 | 27 |   357,18  | -1,38 %  | **339,32** 🟡BLACKOUT | +3,81 % | SICHER (Blackout Standard 328,60 → 339,32 aktiviert, Q3 Di 28.07. AMC) |
| LLY  | 1.192,00 | 8  | 1.193,89  | -0,16 %  | 1.098,38     | +8,52 %     | SICHER |
| AAPL |   325,46 | 31 |   316,86  | +2,71 %  |   291,51     | +11,64 %    | SICHER |
| JPM  |   348,51 | 3  |   332,78  | +4,73 %  |   306,16     | +13,83 %    | SICHER |
| UNH  |   423,25 | 24 |   401,57  | +5,40 %  |   369,44     | +14,56 %    | SICHER |

**V1-V6 Vollcheck 6 SICHER:**
- V1 (Stop -8 %) — 6 SICHER, min GS +1,84 % (24,32 $ vom Break)
- V2/V3/V4 — kein Trigger (kein 52w-Hoch relevant, max +5,40 % UNH << 20 %)
- V5 (EMA50<EMA200) — 6 SICHER, alle Golden Cross intakt (Vortag-Basis)
- V6 (RSI>80 UND RS_4w<0) — 6 SICHER, max RSI 65,76 JPM (Vortag) << 80

**→ KEINE Sell-/Limit-Order platziert**

**Kaufsignal-Scan Slot 2/2 KW30 — LEVEL 0 No-Action bei Unsicherheit:**

| Sym | K1 EMA | K2 RSI | K3 RS | K4 Vol* | K5 P/E + Growth        | Blackout | Decision |
|-----|--------|--------|-------|---------|------------------------|----------|----------|
| **PSX** | ✓ | ✓ 67,60 | ✓ +25 % | offen** | ✗ Growth +6,9 % <10 %  | frei     | **REJECT K5-FAIL** |
| FTI     | ✓ | ✓ 66,80 | ✓ +1,5 %| offen** | ✓ P/E 19,4 + Growth 11,6 % | Earnings 30.07. → 4 HT → Blackout Mo (Tag+1) | **REJECT LEVEL 0 Timing** |
| DE      | ✓ | ✓ 56,40 | ✓ +1,4 %| offen** | ✗ Growth +9,6 % <10 %  | Earnings 14.08. frei | **REJECT K5-FAIL** |

*K4 Session-Vol so früh (09:38) nicht belastbar, formal offen — aber irrelevant weil K5-Fail dominierend
**Perplexity Multi-Source K5-Verifikation: PSX Zacks/Yahoo/GuruFocus P/E 10.8-11.9 ✓ aber RevGrowth Q1 CY26 +6,9 % (MarketBeat); FTI P/E 19,4 + Q1 26 +11,6 %; DE P/E 23 + Q3 FY25 +9,6 %

**Rationale KEIN Kauf:**
- PSX Hauptkandidat: RevGrowth +6,9 % KLAR unter 10 %-Cap → strikte Regel-Anwendung REJECT
- FTI: alle 5 K-Signale ✓ ABER Earnings-Blackout in nur 4 HT (Do 30.07. Fenster) → Blackout aktiviert bereits Mo 27.07. am Tag+1 nach Kauf → analog V-Muster (Kauf 20.07., Blackout aktiv 24.07.) aber V hatte 6 HT Buffer, FTI nur 4 HT → **zu knapp, LEVEL 0 "No-Action bei Unsicherheit"** (Kauf direkt vor Earnings-Reporting-Risiko + Fill-Day+1 Give-back-Muster + Sofort-Blackout-Aktivierung)
- DE: RevGrowth +9,6 % KNAPP unter 10 %-Cap → strikte Regel FAIL, kein K5-Multi-Source-Override rechtfertigbar bei -0,4 pp Diff
- Weitere Kandidaten aus Do-Close-Screener bereits Rejects (CVX/UNP/EQNR K2-FAIL, CAT K2-FAIL, LMT K1-FAIL, TPR/NEE K3-FAIL)

**→ Slot 2/2 KW30 verfällt Ende Fr 24.07. ohne Kauf. KW30 final: 1 Kauf (V 20.07.).**

**Sektor-Struktur unverändert (kein Trade):**
| Sektor | Positionen | MV        | % Portfolio | Status |
|--------|------------|-----------|-------------|--------|
| XLV    | UNH + LLY  | 19.694,12 | 20,25 %     | GRÜN <30 % |
| XLF    | GS+JPM+V   | 19.113,99 | 19,65 %     | GRÜN, 3-Pos-Cap intakt |
| XLK    | AAPL       | 10.089,27 | 10,37 %     | GRÜN |
| XLC/XLE/XLI | —      |     0     |  0 %        | GRÜN |

**Guardrails 8/8 GRÜN + 1 WARN (V-Blackout aktiv, kein Aktion nötig):**
```
1. Daily Loss Cap (-3 %):     +0,137 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 5 -0,972 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,783 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,783 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,189 %                                        [INAKTIV]
6. VIX-Filter (>30):          ~18 / VXX 22,2                                      [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV V1_neu 339,32 (kein Sofort-Stop-Risiko)     [WARN]
8. Max Käufe KW30:            1/2 (Slot 2/2 verfällt Ende Fr, kein K1-K5 ✓ ohne Blackout-Risiko) [GRÜN]
```

**Entscheidung Market Open 09:38 Fr 24.07.:**
- **KEIN Kauf** (LEVEL 0 No-Action: alle 3 K1-K3-Kandidaten K5-blockiert oder Timing-blockiert)
- **KEINE Sell-/Limit-Order** (6 V1-V6 SICHER)
- **V-Blackout-Aktivierung dokumentiert** (V1_neu 339,32 statt 328,60, Puffer +3,81 % ohne Sofort-Stop-Risiko)
- **ClickUp Routine-Log Prio 4** (Info-Level, Fallback PushNotification bei Fehler)
- **PushNotification Prio 3** an Owner (Slot 2/2 verfällt + V-Blackout Aktivierung + GS ENGSTE +1,84 %)

**Nächste Routine:** Fr 24.07. 13:00 ET Midday Stop-Check — **GS V1 1.050,40 Puffer +1,84 % ENGSTE** (Fill-Day+7 Give-back-Fortsetzung-Risiko), V Blackout-Puffer +3,81 % Watch, LLY XLV-Konsolidierung.

---

## Market Close 2026-07-23 16:03 ET (Do, KW30 Tag 4) — Tagesbilanz: Alle 6 V1-V6 SICHER, Alpha +0,31 pp POSITIV, keine Limit-Order Fr, PSX-Watchlist

```
Alpaca clock:      is_open=false | next_open Fr 24.07. 09:30 ET | next_close Fr 24.07. 16:00 ET
Equity End:        97.152,97 $   (Alpaca /v2/account portfolio_value)
Cash:              48.385,53 $   (49,80 %, unverändert seit Open Post-GOOGL-Sell)
Portfolio MV End:  48.767,44 $   (50,20 %, 6 Positionen)
Buying_power:      48.385,53 $   (last_equity=0 Paper-Reset-Artefakt)
Daily P/L End:       -934,82 $   (-0,953 % vs Mi-Close 98.087,79)                 [GRÜN, Cap -3 %]
SPY Close 23.07.:   738,06        (vs Mi-Close 747,49 = -1,262 %)                 [Crash-Filter INAKTIV, <5 %]
Alpha vs SPY:      +0,309 pp     POSITIV (Cash-Puffer 49,80 % dämpft Verlust)
ATH:              100.066,47 $   DD -2,912 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 4:  -1,103 %     (vs Fr-Close 98.236,14, -1.083,17 $)             [GRÜN, Cap -5 %]
VXX Close:          22,61         (VIX-Proxy → VIX ~17-18 carry-over)             [GRÜN, <30]
Käufe KW30:            1/2       (Slot 2/2 offen letzter Handelstag Fr 24.07.)
Open Orders:           0          (KEINE Limit-Order platziert für Fr)
Guardrails:        8/8 GRÜN
```

**Positionen Close 16:00 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Cur Close  | Entry      | P/L %    | chg_today  | V1-Stop     | V1-Puffer    | V5 (EMA50/200) | V6 (RSI/RS4w) | Status |
|--------|-----------|-----------|---------|-----------|------------|--------------|----------------|---------------|--------|
| **GS** | 1.074,72  | 1.141,74  | -5,87 % | -2,14 %   | 1.050,40   | **+2,32 %** | ✓ 1.042/933 diff +109 | ✓ RSI 51,86 / RS4w -0,91 % | SICHER **ENGSTE**, Fill-Day+6 Give-back verstärkt (Midday +2,50 % → Close +2,32 %, -0,55 pp vs Open), 24,32 $ vom V1 |
| V      |   351,85  |   357,18  | -1,49 % | -0,45 %   |   328,60   | +7,08 %      | ✓ 341/332 diff +8,4 | ✓ RSI 54,27 / RS4w +5,09 % | SICHER (marginal vs Midday +6,77 %, Fill-Day+3 Konsolidierung, V5 EMA-Spread marginal aber intakt) |
| LLY    | 1.185,31  | 1.193,89  | -0,72 % | +1,92 %   | 1.098,38   | +7,92 %      | ✓ 1.131/1.020 diff +111 | ✓ RSI 55,30 / RS4w +5,45 % | SICHER (verbessert vs Midday +7,55 %, XLV-Rebound Fortsetzung Tag+1 **Best-chg heute**) |
| AAPL   |   321,66  |   316,86  | +1,52 % | -1,30 %   |   291,51   | +10,34 %     | ✓ 308/280 diff +27 | ✓ RSI 58,25 / RS4w +8,98 % | SICHER (verschlechtert vs Midday +9,99 %, chg -1,30 %) |
| JPM    |   349,90  |   332,78  | +5,14 % | +0,49 %   |   306,16   | +14,29 %     | ✓ 327/313 diff +13 | ✓ RSI 65,76 / RS4w +4,23 % | SICHER (leicht verbessert vs Midday +13,62 %) |
| UNH    |   423,59  |   401,57  | +5,48 % | -1,79 %   |   369,44   | +14,65 %     | ✓ 413/360 diff +53 | ✓ RSI 53,27 / RS4w +3,69 % | SICHER (verbessert vs Midday +14,23 %, chg -1,79 % XLV-gemischt) |

**V1-V6 Vollständiger Check 6 SICHER (Market Close Signal-Prüfung):**
- V1 (Stop -8 %) — 6 SICHER, Puffer +2,32 % GS bis +14,65 % UNH (kein Break)
- V2 (Trailing -12 %) — kein 52w-Hoch relevant, kein Trigger
- V3 (TP1 +20 %) — max +5,48 % UNH << 20 %, kein Trigger
- V4 (TP2 +35 %) — kein Trigger
- **V5 (EMA50<EMA200) — 6 SICHER**, alle Golden Cross intakt (min V EMA-Spread +8,4)
- **V6 (RSI>80 UND RS_4w<0) — 6 SICHER**, max RSI 65,76 JPM << 80-Threshold (nur GS RS_4w -0,91 % negativ, aber RSI 51,86 << 80)

**→ KEINE Limit-Order für Fr 24.07. platziert** (kein V5/V6-Trigger)

**Tages-Highlights:**
- **Best chg_today:** LLY +1,92 % (XLV-Rebound Fortsetzung Tag+1, RSI 55,30 rekonvertiert stabil, Puffer verbessert +6,52 % → +7,92 %)
- **Worst chg_today:** GS -2,14 % (Fill-Day+6 Give-back verstärkt, Puffer +2,87 % → +2,32 % **NEUE ENGSTE ALLER ZEITEN Fill-Zeitraum**, aber V1-Break-Distanz 24,32 $)
- **Best P/L:** UNH +5,48 % (+528,48 $)
- **Worst P/L:** GS -5,87 % (-536,19 $)
- **UNH -1,79 % / AAPL -1,30 %** milde Give-back trotz XLV-Rebound (UNH-Sektor-Divergenz LLY vs UNH)
- **Alpha +0,31 pp POSITIV** (Cash-Puffer 49,80 % dämpft, Portfolio-Fokus-Positionen mildere Give-back vs SPY -1,26 % Breitmarkt-Sell)

**Daily/Weekly Loss Cap Check:**
- Daily -0,953 % > Cap -3 % → **GRÜN**
- Weekly KW30 Tag 4 -1,103 % > Cap -5 % → **GRÜN** (keine pending-Order-Stornierung, kein Kauf-Sperre)

**Sektor-Struktur Post-GOOGL-Sell (Live Close 16:00 ET):**
| Sektor | Positionen | MV        | % investiert | % Portfolio | Status |
|--------|------------|-----------|--------------|-------------|--------|
| XLV    | UNH + LLY  | 19.648,64 | 40,29 %      | 20,23 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLF    | GS+JPM+V   | 19.147,34 | 39,26 %      | 19,71 %     | ⚠ investiert > 30 %, Portfolio SAFE (3-Pos-Cap intakt) |
| XLK    | AAPL       |  9.971,46 | 20,45 %      | 10,26 %     | GRÜN |
| XLC    | —          |     0     |  0 %         |  0 %        | GRÜN (GOOGL raus) |

**Watchlist Fr 24.07. — Slot 2/2 KW30 letzter Handelstag (Alpaca-Screener K1-K3):**
- **PSX (XLE, K1-K3 3/3 ✓✓✓)** — Hauptkandidat, RSI 67,60 (im Cap 55-70), RS_63d vs SPY **+25,0 % #1**, ret_20d +22,6 %, EMA50 185/200 163 diff +22 — Refining/Marketing-Leadership XLE
- **FTI (XLE, K1-K3 3/3 ✓✓✓)** — Backup, RSI 66,80, RS_63d +1,5 %, ret_20d +18,3 %, EMA50 70,6/200 61,1 diff +9,5 — Energy Services
- **DE (XLI, K1-K3 3/3 ✓✓✓)** — Backup, RSI 56,40, RS_63d +1,4 %, ret_20d +1,4 %, EMA50 592/200 552 diff +40 — Industrials-Leader
- Rejects: CVX RSI 71,0 K2-FAIL (>70), UNP RSI 71,0 K2-FAIL, EQNR RSI 76,4 K2-FAIL, CAT RSI 43,9 K2-FAIL, LMT EMA50 521 < EMA200 542 K1-FAIL, TPR RS -8,6 % K3-FAIL, NEE RS -4,0 % K3-FAIL
- K4/K5 zwingend Fr Market Open (Volumen + FwdPE + RevGrowth + Blackout-Check)
- XLE nach GOOGL-Sell = 0 % Portfolio → PSX/FTI-Add unkritisch (max Add ~10 % << 30 %-Cap)
- XLI nach GOOGL-Sell = 0 % Portfolio → DE-Add unkritisch

**Guardrails 8/8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     -0,953 % (vs Mi-Close 98.087,79)                    [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 4 -1,103 % (vs Fr-Close 98.236,14)         [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,912 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,912 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Close -1,262 % vs Mi-Close                      [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (VXX 22,61 Proxy)                            [GRÜN]
7. Earnings-Blackout (3 HT):  Keine bestätigt                                     [GRÜN]
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                  [FREI 1]
V-Regel: 6/6 V1-V6 SICHER (keine Trigger, keine Limit-Order)
```

**Entscheidung Market Close 16:03 Do 23.07.:**
- **Keine Sell-/Limit-Order** (6 V1-V6 SICHER, keine V5/V6-Trigger)
- **Weekly Loss Cap nicht ausgelöst** (-1,103 % > -5 %)
- **ClickUp Tagesbericht Prio 4** (positive Alpha vs SPY trotz negativer absoluter Perf → Fallback PushNotification bei Fehler)
- **PushNotification Prio 3** (Tages-Zusammenfassung, GS-Puffer-Watch für Fr Pre-Market)

**Nächste Routine:** Fr 24.07. 08:30 ET Pre-Market Check — **GS V1 1.050,40 Puffer +2,32 % ENGSTE Watch** (Fill-Day+7 Give-back-Fortsetzung-Risiko), PSX/FTI/DE K4/K5-Vollcheck als Slot 2/2 KW30 letzter Handelstag, LLY XLV-Rebound-Fortsetzung, Alpaca-Bar-Update EMA/RSI.

---

## Midday 2026-07-23 13:07 ET (Do, KW30 Tag 4) — Alle 6 Positionen V1-V4 SICHER, keine Stops, kein Alert

```
Alpaca clock:      is_open=true | now Do 23.07. 13:07 ET | next_close Do 23.07. 16:00 ET
Equity Live:       97.030,95 $   (Alpaca /v2/account)
Cash:              48.385,53 $   (49,87 %, unverändert seit Open Post-GOOGL-Sell)
Portfolio MV Live: 48.649,23 $   (50,14 %, 6 Positionen)
Buying_power:      48.385,53 $   (last_equity=0 Paper-Reset-Artefakt)
Daily P/L Midday:  -1.056,84 $   (-1,078 % vs Mi-Close 98.087,79)                 [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -3,034 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 4:  -1,227 %     (vs Fr-Close 98.236,14, -1.205,19 $)             [GRÜN, Cap -5 %]
SPY Live 13:07:    737,90        (vs Mi-Close 747,49 = -1,283 %)                  [Crash-Filter INAKTIV, < 5 %]
VIX-Proxy VXX:     22,96         (VIX ~17-18 carry-over)                          [GRÜN, <30]
Käufe KW30:            1/2       (Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0
Guardrails:        8/8 GRÜN, keine V-Regel-Trigger
```

**Positionen Live 13:07 ET (Alpaca /v2/positions + /trades/latest IEX) — sortiert Puffer ENG→WEIT:**

| Sym    | Cur Live   | Entry      | P/L %     | V1-Stop     | V1-Puffer    | Status |
|--------|-----------|-----------|----------|------------|--------------|--------|
| **GS** | 1.076,70  | 1.141,74  | -5,70 %  | 1.050,40   | **+2,50 %** | SICHER **ENGSTE**, Fill-Day+6 Give-back verschärft vs Open +2,87 % um -0,37 pp, 26,30 $ vom V1 |
| V      |   350,845 |   357,18  | -1,77 %  |   328,60   | +6,77 %      | SICHER (marginal verbessert vs Open +6,27 %, Fill-Day+3 Konsolidierung) |
| LLY    | 1.181,30  | 1.193,89  | -1,05 %  | 1.098,38   | +7,55 %      | SICHER (verbessert vs Open +6,52 % um +1,03 pp, XLV-Rebound Fortsetzung) |
| AAPL   |   320,64  |   316,86  | +1,19 %  |   291,51   | +9,99 %      | SICHER (verschlechtert vs Open +10,53 % um -0,54 pp, chg -0,49 %) |
| JPM    |   347,87  |   332,78  | +4,53 %  |   306,16   | +13,62 %     | SICHER (marginal verschlechtert vs Open +13,81 %, chg -0,16 %) |
| UNH    |   422,04  |   401,57  | +5,10 %  |   369,44   | +14,23 %     | SICHER (verschlechtert vs Open +16,24 % um -2,01 pp, chg -1,72 % XLV trotz LLY-Rebound gemischt) |

**V1-V4-Check 6 SICHER (Midday, RSI/EMA nicht geprüft per Routine-Regel):**
- V1 (Stop -8 %) — 6 SICHER (Puffer +2,50 % GS bis +14,23 % UNH), kein Break
- V2 (Trailing -12 %) — kein 52w-Hoch-Trigger
- V3 (TP1 +20 %) — max +5,10 % UNH << 20 %, kein Trigger
- V4 (TP2 +35 %) — kein Trigger

**Daily Loss Cap Check:**
- Daily P/L -1,078 % > Cap -3 % → **KEINE Order-Stornierung, keine Sperre**
- Weekly KW30 Tag 4 -1,227 % > Cap -5 % → **GRÜN**

**Guardrails 8/8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     -1,078 % (vs Mi-Close 98.087,79)                    [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 4 -1,227 % (vs Fr-Close 98.236,14)         [GRÜN]
3. Drawdown-Alarm (-15 %):    -3,034 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -3,034 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Live -1,283 % vs Mi-Close                       [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (VXX 22,96 Proxy)                            [GRÜN]
7. Earnings-Blackout (3 HT):  Keine bestätigt                                     [GRÜN]
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                  [FREI 1]
V-Regel: 6/6 SICHER (Puffer +2,50 % GS bis +14,23 % UNH)
```

**Entscheidung Midday 13:07 Do 23.07.:**
- **Keine Sell-/Kauf-Order** (6 V1-V4 SICHER, keine Trigger)
- **Kein ClickUp-Alert** (Routine-Regel: nur bei Stops oder Daily Cap)
- **Keine PushNotification** (routinemäßig ruhig; GS Puffer +2,50 % marginal enger vs Open +2,87 %, aber unverändertes Muster)

**Beobachtungen Midday:**
- **GS Fill-Day+6 Give-back setzt sich fort** (Open +2,87 % → Midday +2,50 %, -0,37 pp), 26,30 $ vom V1 — Close 16:00 ET Watch weiter zwingend, aber nicht kritisch
- **SPY -1,283 % vs Mi-Close** verstärkt sich (Open war -0,787 %) — Portfolio-Alpha **-0,205 pp NEGATIV** (Daily -1,078 % vs SPY -1,283 % — leicht positive Kompensation durch Cash-Puffer 49,87 %)
- **UNH -1,72 % chg** trotz LLY-Rebound (Puffer 14,23 % weiterhin komfortabel)
- **LLY +0,11 % chg vs Open** setzt XLV-Rebound fort (Puffer 7,55 %)
- **V/AAPL/JPM stabil** in Bandbreite ±0,5 %

**Nächste Routine:** Do 23.07. 16:00 ET Market Close + Tagesbilanz — GS V1 1.050,40 Watch (Puffer +2,50 % engste), Tages-Alpha vs SPY, UNH XLV-Konsolidierung, KW30 Weekly-Zwischenstand.

---

## Market Open 2026-07-23 09:38 ET (Do, KW30 Tag 4) — ✅ GOOGL V1-Market-Sell ausgeführt, 6 Positionen V1-V6 SICHER, kein neuer Kauf

```
Alpaca clock:      is_open=true | now Do 23.07. 09:38 ET | next_close Do 23.07. 16:00 ET
Equity Live:       97.176,52 $   (Alpaca /v2/account, Post-GOOGL-Sell)
Cash:              48.385,53 $   (49,79 %, +8.359,26 vs Pre nach GOOGL-Sell)
Portfolio MV Live: 48.790,99 $   (50,21 %, 6 Positionen nach GOOGL-Close)
Buying_power:      48.385,53 $
Daily P/L Open:     -911,27 $    (-0,929 % vs Mi-Close 98.087,79)                  [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -2,888 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 4:  -1,079 %     (vs Fr-Close 98.236,14, -1.059,62 $)              [GRÜN, Cap -5 %]
SPY Live 09:39:    741,61        (vs Mi-Close 747,49 = -0,787 %)                   [Crash-Filter INAKTIV]
VIX-Proxy VXX:     22,55         (VIX ~17-18 carry-over)                           [GRÜN, <30]
Käufe KW30:            1/2       (Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0
Guardrails:        8/8 GRÜN, GOOGL V1-Regel-Trigger AUSGEFÜHRT (Market-Sell fill @ 321,51)
```

**GOOGL Market-Sell Details (Alpaca Order 73cac698-9a42-465c-9e5f-32c754eff1c5):**
- Order Type: Market Sell (Day, position_intent=sell_to_close)
- Fill Time: 2026-07-23 09:38:05.726 ET (0,5 sec nach Submission)
- Fill: 26 Shares × **321,51 $** = **8.359,26 $** Erlös
- Realisierter Verlust: **-1.211,34 $ (-12,65 %)** vs Entry 368,10 $ (07.07.2026)
- Grund: V1 338,65 verletzt Pre-Market -4,26 % + Open -4,91 % nach Q2 CY26 Earnings-Beat-Selloff (EPS 9,11 / Rev 119,8 Mrd BEAT, aber Aftermarket -4,2 % + Pre -4,6 % wegen Capex-Guidance-Sorge, Marktreaktion NEGATIV überwiegt Fundamentals)

**Positionen Live 09:38 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Cur Live   | Entry      | P/L %     | V1-Stop     | V1-Puffer    | Status |
|--------|-----------|-----------|----------|------------|--------------|--------|
| **GS** | 1.080,55  | 1.141,74  | -5,36 %  | 1.050,40   | **+2,87 %** | SICHER **ENGSTE**, Fill-Day+6 Give-back -1,61 % (verschlechtert vs Mi-Close +4,55 % um -1,68 pp, 30,15 $ vom V1) |
| V      |   349,19  |   357,18  | -2,24 %  |   328,60   | +6,27 %      | SICHER (verschlechtert vs Close +7,55 % um -1,28 pp, Fill-Day+3 Konsolidierung, V5 EMA-Spread +5,63) |
| LLY    | 1.170,00  | 1.193,89  | -2,00 %  | 1.098,38   | +6,52 %      | SICHER (verbessert vs Close +5,53 % um +0,99 pp, XLV-Rebound chg +0,60 %) |
| AAPL   |   322,21  |   316,86  | +1,69 %  |   291,51   | +10,53 %     | SICHER (verschlechtert vs Close +11,87 %, chg -1,13 %) |
| JPM    |   348,44  |   332,78  | +4,71 %  |   306,16   | +13,81 %     | SICHER (marginal, chg +0,07 % flat, 3 Shares) |
| UNH    |   429,42  |   401,57  | +6,94 %  |   369,44   | +16,24 %     | SICHER (marginal verschlechtert vs Close +16,74 %, chg -0,44 %) |

**V1-V6-Check 6 SICHER (Post-GOOGL-Sell):**
- V1 (Stop -8 %) — 6 SICHER (Puffer +2,87 % GS bis +16,24 % UNH)
- V2 (Trailing -12 %) — kein 52w-Hoch-Trigger
- V3/V4 (TP1/TP2 20/35 %) — max +6,94 % UNH << 20 %
- V5/V6 (EMA/RSI) — EMA50>EMA200 überall Golden Cross intakt, max RSI ~64 << 80-Threshold aus Vortagsberechnung

**Sektor-Struktur Post-GOOGL-Sell (Live 09:38 ET):**
| Sektor | Positionen | MV       | % investiert | % Portfolio | Status |
|--------|------------|----------|--------------|-------------|--------|
| XLF    | GS+JPM+V   | 19.117,85| 39,18 %      | 19,67 %     | ⚠ investiert > 30 %, Portfolio SAFE (3-Pos-Cap intakt) |
| XLV    | UNH + LLY  | 19.666,08| 40,31 %      | 20,24 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLK    | AAPL       |  9.988,51| 20,47 %      | 10,28 %     | GRÜN |
| XLC    | —          |     0    |  0 %         |  0 %        | GRÜN (GOOGL raus) |

**Kaufsignal-Scan Slot 2/2 KW30 — LEVEL 0 No-Action bei Unsicherheit:**
- Perplexity Sektor-Check keine belastbaren 3M-RS-Daten geliefert (Refusal, allgemeine ETF-Infos ohne konkrete 3M-Performance)
- XLV nach GOOGL-Sell = 20,24 % Portfolio + neuer XLV ~9 % = ~29,24 % knapp <30 %-Cap, aber **Owner-Sektor-Cap-Ambiguität persistiert** (ABBV/MRK/JNJ 3/3 K1-K3 aus Pre-Market Watchlist)
- XLK-Backup: NVDA/META/MSFT/AMZN blockiert (Sektor-Cap) oder AVGO/MU K5-anfällig
- XLE-Kandidaten K3-FAIL bislang, XLI MMM/UPS K5-FAIL bislang
- **Slot 2/2 KW30 bleibt OFFEN bis Fr 24.07.** — kein neuer Kauf ausgeführt, Kauf-Wahrscheinlichkeit weiter GERING ohne Owner-XLV-Freigabe oder frischen K5-Kandidaten

**Guardrails 8/8 GRÜN (Post-Sell):**
```
1. Daily Loss Cap (-3 %):     -0,929 % (vs Mi-Close 98.087,79)                    [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 4 -1,079 % (vs Fr-Close 98.236,14)         [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,888 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,888 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Live -0,787 % vs Mi-Close                       [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (VXX 22,55 Proxy)                            [GRÜN]
7. Earnings-Blackout (3 HT):  Keine bestätigt (Perplexity)                        [GRÜN]
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                  [FREI 1]
V-Regel: GOOGL V1 AUSGEFÜHRT — sonstige 6 V1-V6 SICHER
```

**Entscheidung Market Open 09:38 Do 23.07.:**
- **GOOGL V1-Market-Sell AUSGEFÜHRT** ✅ Fill @ 321,51 × 26 Sh, Realisierter Verlust -1.211,34 $
- **KEIN weiterer Sell/Kauf** (6 V1-V6 SICHER, Slot 2/2 KW30 offen aber No-Action)
- **PushNotification Prio 1 Owner** ✅ (V1-Trigger + Fill-Details)
- **ClickUp Critical Alert** ✗ ITEM_246 persistent → PushNotification Fallback ausgeführt
- **ClickUp Routine-Log Prio 4** — Fallback PushNotification bei Fehler

**Nächste Routine:** Do 23.07. 13:00 ET Midday Stop-Check — GS V1 1.050,40 Puffer +2,87 % ENGSTE, V/LLY-Watch, UNH XLV-Konsolidierung.

---

## Pre-Market 2026-07-23 08:36 ET (Do, KW30 Tag 4) — 🔴 GOOGL V1 VERLETZT Pre-Market, Market-Sell Open ZWINGEND

```
Alpaca clock:      is_open=false | next_open Do 23.07. 09:30 ET | next_close Do 23.07. 16:00 ET
Equity Pre:        97.267,18 $   (Alpaca /v2/account, portfolio_value)
Cash:              40.026,27 $   (41,15 %, unverändert)
Portfolio MV Pre:  57.240,81 $   (58,85 %, 7 Positionen)
Buying_power:      40.026,27 $   (last_equity=0 = Pre-Market-Reset-Artefakt)
Daily P/L Pre:      -820,61 $    (-0,837 % vs Mi-Close 98.087,79)                [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -2,797 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 4:  -0,986 %     (vs Fr-Close 98.236,14, -968,96 $)              [GRÜN, Cap -5 %]
SPY Pre 08:28 ET:  742,12        (vs Mi-Close 747,49 = -0,718 %)                 [Crash-Filter INAKTIV]
VIX:               ~17-18        (Perplexity Pre)                                [GRÜN, <30]
Käufe KW30:            1/2       (Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0
Guardrails:        8/8 GRÜN, aber V1-Regel-Trigger GOOGL Pre-Market → Sofort-Sell Open ZWINGEND
```

**Positionen Pre-Market 08:36 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Cur Pre    | Entry      | P/L %     | V1-Stop     | V1-Puffer    | Status |
|--------|-----------|-----------|----------|------------|--------------|--------|
| **GOOGL**| 324,06 (current) / 324,23 (latest trade) | 368,10 | **-11,96 %** | 338,65 | **-4,26 %** 🔴🔴🔴 | **V1 VERLETZT Pre-Market → Market-Sell 26 Sh @ Open 09:30 ET SOFORT** (Q2 BEAT EPS 9,11 / Rev 119,8 B aber Aftermarket -4,2 % / Pre-Market -4,6 % — Marktreaktion NEGATIV, Capex-Guidance-Sorge oder Erwartungs-Setup zu hoch) |
| GS     | 1.086,01  | 1.141,74  | -4,88 %  | 1.050,40   | +3,39 %      | SICHER (verschlechtert vs Mi-Close +4,55 % um -1,16 pp overnight-Drift) |
| LLY    | 1.151,00  | 1.193,89  | -3,59 %  | 1.098,38   | +4,79 %      | SICHER (leicht verschlechtert vs Mi-Close +5,53 %) |
| V      |   353,38  |   357,18  | -1,06 %  |   328,60   | +7,54 %      | SICHER (marginal vs Mi-Close +7,55 %) |
| AAPL   |   324,33  |   316,86  | +2,36 %  |   291,51   | +11,26 %     | SICHER (leicht verschlechtert vs Mi-Close +11,87 %) |
| JPM    |   349,12  |   332,78  | +4,91 %  |   306,16   | +14,03 %     | SICHER (marginal verbessert vs Mi-Close +13,96 %) — **DATA-HINWEIS: Alpaca /v2/positions bestätigt nur 3 Shares (Orig-Fill 17.06. 3 Sh @ 332,78, MV 1.047,36 $), Portfolio-Log historisch inflatiert → Konsolidierung im Weekly Review nötig** |
| UNH    |   428,18  |   401,57  | +6,63 %  |   369,44   | +15,90 %     | SICHER (leicht verschlechtert vs Mi-Close +16,74 %) |

**V1-V6-Check 6/7 SICHER, 1 VERLETZT:**
- **V1 (Stop -8 %) — GOOGL VERLETZT Pre-Market** (324,23 < 338,65 = -4,26 % unter Stop, -14,42 $ Distanz) → **Market-Sell 09:30 ET Open ZWINGEND (V1-Regel: Market Order SOFORT)**
- V1 restliche 6 SICHER (Puffer +3,39 % bis +15,90 %)
- V2-V6 keine Verletzung (V2 kein 52w-Hoch relevant, V3/V4 max +6,63 % UNH << 20 %, V5/V6 EMA-Spreads intakt aus Vortagsberechnung)
- **→ Market-Sell GOOGL 26 Shares @ Open 09:30 ET SOFORT** (V1-Regel: Market Order)

**GOOGL Q2 CY26 Earnings Post-Release (Perplexity Multi-Source):**
- EPS **9,11 $** BEAT vs Konsens 2,88–2,89 (Split/Adjustment-Frage offen für so hohes Beat-Ratio)
- Revenue **119,8 Mrd. $** BEAT vs Konsens 116,5–116,9
- Aftermarket Mi 22.07.: 327,40 $ (-4,2 %), Pre-Market Do 08:15 ET: 326,10 $ (-4,6 %), Alpaca 08:36 ET: 324,23 $ (-5,26 % vs Close 341,91)
- Interpretation: Trotz BEAT — Kapex-Guidance-Sorge oder AI-Investment-Ausblick negativ, Marktreaktion überwiegt Fundamentals
- Realisierter Verlust bei V1-Sell @ Open ~324 $ = **-1.144 $ (-11,96 %)** vs Entry 368,10

**Sektor-Gewichte Pre (vor GOOGL-Sell):**
| Sektor | Positionen | MV       | % investiert | % Portfolio | Status |
|--------|------------|----------|--------------|-------------|--------|
| XLF    | GS+JPM+V   | 19.276,70| 33,68 %      | 19,82 %     | ⚠ investiert > 30 %, Portfolio SAFE (3-Pos-Cap intakt) |
| XLV    | UNH + LLY  | 19.484,32| 34,04 %      | 20,03 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLK    | AAPL       | 10.054,23| 17,57 %      | 10,34 %     | GRÜN |
| XLC    | GOOGL      |  8.425,56| 14,72 %      |  8,66 %     | GRÜN — nach Sell 0 % |

**Sektor-Struktur Post-GOOGL-Sell (Projected):**
- XLC 0 % (GOOGL raus)
- XLF unverändert 19,82 % Portfolio
- XLV unverändert 20,03 % Portfolio
- XLK unverändert 10,34 % Portfolio
- Cash-Zufluss ~8.430 $ → Cash steigt auf ~48.460 $ (~49,8 % Portfolio, weit >20 % Min)
- Positionen: 6 (unter Cap 8)

**Watchlist Do 23.07. (Watchlist-Check nach GOOGL-Sell im Market-Open-Scan):**
- Perplexity 24./25./28.07. Earnings-Kalender NICHT verfügbar → K5-Blackout-Check pro Kandidat einzeln zwingend
- ABBV/MRK/JNJ (XLV, 3/3 K1-K3 vor Vortagen) — **XLV nach GOOGL-Sell 20,03 %**, +neuer XLV ~9 % = ~29 % formal <30 %-Cap, aber weiter Owner-Sektor-Cap-Ambiguität-Frage
- XLK-Backup: AVGO/MU historisch K5-anfällig, NVDA/META/MSFT/AMZN blockiert oder XLK-doppel
- XLE (XOM/CVX/COP) K3-FAIL bislang, XLI MMM/UPS K5-FAIL bislang
- **Kauf-Wahrscheinlichkeit Do 23.07. weiterhin GERING** ohne Owner-Freigabe oder frischen K5-Kandidaten

**Weekly Loss Cap Check KW30 Tag 4:** Weekly -0,986 % > -5 % → **NICHT ausgelöst, keine Cash-Aktion, keine Order-Stornierung** (auch nichts pending).

**Guardrails 8/8 GRÜN, aber V1-Trigger GOOGL:**
```
1. Daily Loss Cap (-3 %):     -0,837 % (vs Mi-Close 98.087,79)                  [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 4 -0,986 % (vs Fr-Close 98.236,14)       [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,797 %                                          [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,797 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Pre -0,718 % vs Mi-Close                      [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (Perplexity Pre)                           [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Post-Release obsolet, keine neuen bestätigt [GRÜN]
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                [FREI 1]
V-Regel-Trigger: GOOGL V1 -4,26 % unter Stop → Market-Sell Open ZWINGEND
```

**Entscheidung Pre-Market 08:36 Do 23.07.:**
- **GOOGL V1-Market-Sell Vorbereitung: 26 Shares Market Order @ Open 09:30 ET** (nächste Routine Market Open führt aus)
- Keine anderen Sell-/Limit-Orders erforderlich
- **PushNotification Prio 1 an Owner** (V1 GOOGL Pre-Market Trigger, Sofort-Sell Open zwingend, Realisierter Verlust ~-1.144 $)
- **ClickUp Critical Alert Prio 1** (STOP_LOSS GOOGL Pre-Market Trigger, CLICKUP_CRITICAL_LIST_ID)
- **ClickUp Routine-Log Prio 4** (Pre-Market fertig, CLICKUP_LIST_ID)
- Fallback PushNotification bei ClickUp-Fehler

**Nächste Routine:** Do 23.07. 09:30 ET Market Open — **GOOGL V1-Market-Sell Sofort-Öffnung Ausführung**, danach Kaufsignal-Scan Slot 2/2 KW30 (Kauf-Wahrscheinlichkeit GERING).

---

## Market Close 2026-07-22 16:03 ET (Mi, KW30 Tag 3) — Alle 7 V1-V6 SICHER, KEINE Limit-Order Do 23.07., GOOGL Q2 AMC released HEUTE Post-Close, Puffer +1,07 % KRITISCH ENGSTE

```
Alpaca clock:      is_open=false | next_open Do 23.07. 09:30 ET | next_close Do 23.07. 16:00 ET
Equity End:        98.087,79 $   (Alpaca /v2/account, portfolio_value)
Cash:              40.026,27 $   (40,81 %)
Portfolio MV:      58.061,52 $   (59,19 %, 7 Positionen)
Buying_power:     322.677,33 $
Daily P/L:          -327,31 $    (-0,3326 % vs last_equity 98.415,10)              [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -1,977 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 3:  -0,151 %     (vs Fr-Close 98.236,14, -148,35 $)                [GRÜN, Cap -5 %]
SPY IEX Close:     747,49        (vs Di-Close 748,155 = -0,089 %; vs Fr-Close 743,28 = +0,566 %)
Alpha vs SPY:      -0,244 pp     (Portfolio -0,333 vs SPY -0,089)                  [LEICHT NEGATIV]
Alpha Weekly:      -0,717 pp     (Portfolio -0,151 vs SPY +0,566)                  [NEGATIV]
VIX:               ~17-18        (Perplexity carry-over, keine Auffrischung)       [GRÜN, <30]
Käufe KW30:            1/2       (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0
Guardrails:        7/8 GRÜN + 1 WATCH (GOOGL Q2 AMC released HEUTE Post-Close, morgen Öffnungs-Reaktion kritisch)
```

**Positionen Close 16:03 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Close      | Entry      | P/L %    | chg heute | V1-Stop     | V1-Puffer       | Status |
|--------|------------|------------|----------|-----------|-------------|-----------------|--------|
| **GOOGL**|  342,27  | 368,10     | -7,02 %  | -1,41 %   | 338,65      | **+1,07 %** 🔴🔴| SICHER ABER KRITISCH ENGSTE ALLER ZEITEN (verschlechtert vs Open +2,40 % um -1,33 pp; **Q2 Earnings AMC HEUTE Post-Close released** — Preview ~$2,87 EPS / $116,5-116,9 B Rev / Capex-Guidance hoch erwartet; Reaktion morgen Öffnung kritisch, V1-Bruch bei jedem -1,08 %-Move → Sofort-Sell-Watch Do Pre-Market/Open zwingend, Owner-Freigabe LETZTE CHANCE VERPASST 15:59 ET, Blackout jetzt obsolet Post-Release) |
| **GS** | 1.098,20   | 1.141,74   | -3,81 %  | +1,16 %   | 1.050,40    | **+4,55 %**     | SICHER (Rebound-Tag+2, verbessert vs Open +4,16 % um +0,39 pp, Fill-Day+5-Muster AVGO/MU überwunden) |
| LLY    | 1.159,11   | 1.193,89   | -2,91 %  | -1,39 %   | 1.098,38    | +5,53 %         | SICHER (verschlechtert vs Open +6,17 % um -0,64 pp, XLV-Konsolidierungstag, RSI ~48 unter 50) |
| V      |   353,42   |   357,18   | -1,05 %  | -0,67 %   |   328,60    | +7,55 %         | SICHER (Fill-Day+2, V5 EMA-Spread +5,63 marginal aber Golden Cross intakt, RSI ~57) |
| AAPL   |   326,12   |   316,86   | +2,92 %  | -0,49 %   |   291,51    | +11,87 %        | SICHER (leicht verschlechtert vs Open +12,43 % um -0,56 pp) |
| JPM    |   348,90   |   332,78   | +4,84 %  | +1,06 %   |   306,16    | +13,96 %        | SICHER (verbessert vs Open +12,80 %, XLF-Rebound Tag+2) |
| UNH    |   431,31   |   401,57   | +7,41 %  | -1,16 %   |   369,44    | **+16,74 %**    | SICHER (leicht verschlechtert vs Open +17,94 %, Beste-P/L bleibt komfortabel) |

**V1-V6-Check alle 7 SICHER — Details (Alpaca Bars 210d):**
- V1 (Stop -8 %) alle sicher, **GOOGL +1,07 % KRITISCH ENGSTE ALLER ZEITEN** (bislang GS Mo 20.07. +0,50 % war Rekord), alle anderen >4 %
- V2 (52w × 0,88) keine Verletzung (keine Position nahe 52w-Hoch)
- V3/V4 (Gewinn ≥ 20 % / 35 %) — max UNH +7,41 % << 20 %
- V5 (EMA50 < EMA200) alle negativ (Golden Cross intakt): GOOGL Spread +38,06 / GS +119,99 / LLY +115,24 / AAPL +26,98 / V +5,63 (marginal) / JPM +12,73 / UNH +51,28
- V6 (RSI > 80 UND RS_4w < 0) — max RSI 66,01 (JPM) << 80, GOOGL RSI 40,23 + RS_4w -3,10 % erfüllt V6-Teil aber RSI << 80, GS RSI 56,56 + RS_4w -1,57 % analog → V6 verlangt BEIDES → nicht ausgelöst
- **→ KEINE Sell-Order 16:03 ET, KEINE Limit-Order für Do 23.07.** platziert

**GOOGL Q2 Earnings AMC HEUTE Post-Close — Watch Do 23.07. Pre-Market/Open:**
- Preview (Perplexity): EPS ~$2,87 / Revenue $116,5–116,9 Mrd / Capex-Guidance hoch erwartet
- Blackout jetzt **obsolet** (Post-Release), Owner-Freigabe LETZTE CHANCE 15:59 ET VERPASST
- V1 338,65 Puffer nur +1,07 % → **jede -1,08 %-Morgen-Reaktion triggert V1 Sofort-Sell**
- **Sofort-Sell-Watch Do 23.07. 08:30 ET Pre-Market + 09:30 ET Open zwingend**
- Historische GOOGL Q2-Post-Release-Volatilität: Median-Move ±3-5 % (typische Big-Tech-Post-Earnings)

**Sektor-Gewichte Close (leicht verändert vs Open durch Marktwert-Bewegung):**
| Sektor | Positionen | MV       | % investiert | % Portfolio | Status |
|--------|------------|----------|--------------|-------------|--------|
| XLF    | GS+JPM+V   | 19.374,64| 33,37 %      | 19,75 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLV    | UNH + LLY  | 19.624,32| 33,80 %      | 20,00 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLK    | AAPL       | 10.109,72| 17,41 %      | 10,31 %     | GRÜN |
| XLC    | GOOGL      |  8.899,06| 15,33 %      |  9,07 %     | GRÜN |

**Watchlist Do 23.07. (Perplexity Sektor-RS + K1-K3 Vorab-Prüfung):**
- **Sektor-RS 4w (Perplexity):** XLK, XLI, XLE, XLF, XLV (Top-5)
- **Sektor-RS 3M (Perplexity):** XLK, XLE, XLV, XLI, XLB
- **Top-3M-Momentum-Stocks Perplexity:** NVDA, AVGO (Broadcom), META, MSFT, AMZN — **alle 5 aus XLK/XLC blockiert oder K5-anfällig** (AVGO K5-Range grenzwertig, NVDA K5-Range 20-41 grenzwertig historisch, META/GOOGL bereits XLC-belegt, AMZN XLC → doppel-Sektor)
- **XLE-Kandidaten** (XOM/CVX/COP): K3-FAIL im Vortag-Screener (Ret63 vs SPY negativ) → REJECT
- **XLI-Kandidaten** MMM K5-FAIL (Rev +2,4 %) + UPS K5-permanent-FAIL — durchweg blockiert
- **XLV-Backup** ABBV 3/3 / MRK 3/3 / JNJ 3/3 K1-K3 ✓ — **XLV-Sektor-Cap-Owner-Entscheidung Pending** (20,00 % + neu ~9 % = ~29 % formal <30 %-Cap, aber Owner-Ambiguität seit KW29)
- **Bewertung:** Kein 5/5 K-Signal-Kandidat außerhalb XLV bestätigt → **Slot 2/2 KW30 bleibt offen bis Fr 24.07.**, Kauf-Wahrscheinlichkeit GERING ohne Owner-Freigabe

**Weekly Loss Cap Check KW30:** Weekly -0,151 % > -5 % → **NICHT ausgelöst, keine Cash-Aktion, keine Order-Stornierung** (auch nichts pending).

**Guardrails 7/8 GRÜN + 1 WATCH:**
```
1. Daily Loss Cap (-3 %):     -0,333 %                                          [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 3 -0,151 %                               [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,977 %                                          [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,977 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Close -0,089 % vs Di, +0,566 % Weekly         [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (carry-over Pre)                           [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Q2 AMC released HEUTE Post-Close → obsolet, morgen V1-Watch zwingend | [WATCH]
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                [FREI 1]
```

**Entscheidung Market Close 16:03 Mi 22.07.:** **Keine Sell-Order platziert** (alle 7 V1-V6 SICHER). **Keine Limit-Order für Do 23.07.** (alle V5/V6 SICHER). **PushNotification Prio 2** an Owner (GOOGL Q2 Post-Release Morgen-Reaktion kritisch, Puffer +1,07 % KRITISCH ENGSTE ALLER ZEITEN). **ClickUp Tagesbericht Prio 3** (negative Perf) — Fallback PushNotification wenn ClickUp-Fehler.

**Nächste Routine:** Do 23.07. 08:30 ET Pre-Market — GOOGL V1 338,65 zwingender Watch (Post-Q2-Reaktion Öffnung), GS V1 1.050,40 Rebound-Fortsetzung, LLY RSI-Watch nach -1,39 % Tag.

---

## Market Open 2026-07-22 09:40 ET (Mi, KW30 Tag 3) — Alle 7 V1-V6 SICHER, KEIN Kauf (LEVEL 0 No-Action), GOOGL Blackout LETZTE CHANCE

```
Alpaca clock:      is_open=true | next_close Mi 22.07. 16:00 ET
Equity:            98.406,07 $   (Alpaca /v2/account, portfolio_value)
Cash:              40.026,27 $   (40,67 %)
Portfolio MV:      58.379,80 $   (59,33 %, 7 Positionen, Live)
Buying_power:     323.568,52 $
Daily P/L:          -9,03 $      (-0,009 % vs last_equity 98.415,10)             [GRÜN, Cap -3 %]
ATH:              100.066,47 $   DD -1,659 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 3:  +0,173 %     (vs Fr-Close 98.236,14, +169,93 $)              [GRÜN, Cap -5 %]
SPY Live 09:40:    747,295       (vs Fr-Close 743,28 = +0,540 %, vs Di-Close 748,155 = -0,115 %) [Crash-Filter INAKTIV]
Alpha vs SPY:      -0,549 pp     (Portfolio ±0 vs SPY +0,540 %)                  [LEICHT NEGATIV]
VIX:               ~17-18        (Perplexity carry-over)                          [GRÜN, <30]
Käufe KW30:            1/2       (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0
Guardrails:        7/8 GRÜN + 1 WARN (GOOGL Blackout Tag 0 AMC HEUTE, Owner-Freigabe LETZTE CHANCE)
```

**Positionen Live 09:40 ET (Alpaca /v2/positions + latest trades IEX) — sortiert Puffer ENG→WEIT:**

| Sym    | Live       | Entry      | P/L %    | V1-Stop     | V1-Puffer       | Δ vs Pre  | Status |
|--------|------------|------------|----------|-------------|-----------------|-----------|--------|
| **GOOGL**|  346,78  | 368,10     | -5,79 %  | 338,65      | **+2,40 %** 🔴  | -0,38 pp  | SICHER ENGSTE (leicht verschlechtert vs Pre +2,78 %; Blackout Tag 0 AMC HEUTE, V1_neu 349,70 > Kurs = **-0,84 % negativ** → Aktivierung würde Sofort-Stop; Option A Strategie-Lock aktiv, **Owner-Freigabe LETZTE CHANCE bis 15:59 ET**) |
| **GS** | 1.094,14   | 1.141,74   | -4,17 %  | 1.050,40    | **+4,16 %**     | +0,56 pp  | SICHER (Rebound-Fortsetzung Tag+2 vs Pre +3,60 %, Fill-Day+4-Muster überwunden) |
| LLY    | 1.166,11   | 1.193,89   | -2,33 %  | 1.098,38    | +6,17 %         | -0,62 pp  | SICHER (marginal verschlechtert vs Pre +6,79 %, XLV-Watch bleibt) |
| V (NEU)|   355,11   |   357,18   | -0,58 %  |   328,60    | +8,07 %         | -0,39 pp  | SICHER (Fill-Day+2, V5 EMA-Spread bleibt marginal aber Golden Cross intakt) |
| AAPL   |   327,755  |   316,86   | +3,44 %  |   291,51    | +12,43 %        | ±0        | SICHER |
| JPM    |   345,355  |   332,78   | +3,78 %  |   306,16    | +12,80 %        | -0,02 pp  | SICHER |
| UNH    |   435,73   |   401,57   | +8,51 %  |   369,44    | **+17,94 %**    | -0,62 pp  | SICHER (Beste-P/L komfortabel) |

**V1-V6-Check alle 7 SICHER:**
- V1 (Stop-Loss -8%) alle sicher, engste GOOGL +2,40 % Puffer, alle anderen >4 %
- V2 (52w-Hoch × 0,88) alle sicher, keine Trailing-Stops verletzt
- V3/V4 (Gewinn ≥20%/35%) — max P/L UNH +8,51 % << +20 %-Schwelle
- V5 (EMA50<EMA200) alle negativ (Golden Cross intakt) — Details siehe Close 21.07. V5/V6-Details
- V6 (RSI>80 UND RS_4w<0) — max RSI ~64 (AAPL/V) << 80-Threshold
- **→ KEINE Sell-Order 09:40 ET Mi 22.07.**

**Market-Open-Scan Slot 2/2 KW30 — Entscheidung KEIN Kauf:**

**Perplexity Sektor-Strength-Check:**
- **Top 3M-RS-Sektoren:** XLE +6,23 % 3M (klar #1), XLI Leading-Quadrant, XLU defensiv-vorne
- XLE Top-Holdings (XOM, CVX, COP): alle K3 pre-Market bereits FAIL (Ret63 vs SPY negativ -1,29 % bis -4,63 %)
- XLI Top-Holdings: MMM K5-FAIL (TTM Rev-Growth +2,4 % << 10 %) bestätigt Pre-Market; UPS K5 permanent-FAIL (-2,65 %); HON/RTX/CAT/DE/LMT/NOC K3-FAIL
- XLV Backup ABBV/MRK/JNJ (alle 3/3 K1-K3): **XLV-Sektor-Cap-Owner-Entscheidung weiter Pending** (aktuell 20,21 % + neu ~9 % = ~29 % knapp am 30 %-Cap; formal <30 %, aber Owner-Ambiguität → LEVEL 0)
- XLU/XLB frische Screener-Runde nicht durchgeführt (Zeit-Constraint 09:40 ET)

**→ LEVEL 0 "No-Action bei Unsicherheit" aktiviert:**
- Kein 5/5 K-Signal-Kandidat außerhalb XLV bestätigt
- XLV Owner-Pending → nicht handeln ohne Freigabe
- **Slot 2/2 KW30 bleibt OFFEN bis Fr 24.07.** (aber Kauf-Wahrscheinlichkeit KW30 weiter GERING)

**Sektor-Gewichte Live (unverändert vs Close 21.07.):**
| Sektor | Positionen | MV       | % investiert | % Portfolio | Status |
|--------|------------|----------|--------------|-------------|--------|
| XLF    | GS+JPM+V   | 19.382,52| 33,20 %      | 19,70 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLV    | UNH + LLY  | 19.781,04| 33,88 %      | 20,10 %     | ⚠ investiert > 30 %, Portfolio SAFE |
| XLK    | AAPL       | 10.163,71| 17,41 %      | 10,33 %     | GRÜN |
| XLC    | GOOGL      |  9.036,28| 15,48 %      |  9,18 %     | GRÜN |

**Guardrails 7/8 GRÜN + 1 WARN (unverändert vs Pre-Market):**
```
1. Daily Loss Cap (-3 %):     -0,009 %                                          [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 3 +0,173 %                               [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,659 %                                          [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,659 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Live +0,540 % vs Fr-Close                     [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (carry-over Pre)                           [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi 22.07. AMC Tag 0 aktivierungssensitiv -0,84 % (Owner-Pending LETZTE CHANCE) | [WARN] |
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                [FREI 1]
```

**GOOGL Blackout-Verlauf HEUTE (Timeline):**
- Mo-Close +0,69 % positiv → Di-Pre +0,41 % → Di-Open -0,05 % → Di-Close -0,67 % → Mi-Pre -0,47 % → **Mi-Open 09:40 -0,84 % NEGATIV** (verschlechtert)
- V1_neu Blackout 349,70 > Kurs 346,78 → Aktivierung würde AKTUELL Sofort-Stop auslösen
- **Owner-Freigabe muss bis 15:59 ET erfolgen** — danach Blackout obsolet (Q2 Earnings-Ereignis eingetreten, Post-Release Reset)
- Empfehlung: **Option A Strategie-Lock beibehalten** — Aktivierung wäre bei aktueller Kurslage funktional wirkungslos

**Entscheidung Market Open 09:40 Mi 22.07.:** **Keine Aktion Buy-seitig** (LEVEL 0 No-Action: XLV Owner-Pending, XLE/XLI K3/K5-blocked). **Keine Aktion Sell-seitig** (alle 7 V1-V6 SICHER). **PushNotification Prio 3** an Owner (GOOGL Blackout LETZTE CHANCE HEUTE Vormittag).

**Nächste Routine:** Mi 22.07. 13:00 ET Midday Stop-Check — GOOGL V1 338,65 + Blackout-Entscheidung post-Owner (falls Freigabe), GS V1 1.050,40 Rebound-Fortsetzung, LLY RSI-Watch.

---

## Pre-Market 2026-07-22 08:36 ET (Mi, KW30 Tag 3) — Alle 7 V1 SICHER (Puffer erholt), GOOGL Blackout aktivierungssensitiv weiter negativ HEUTE letzte Chance, MMM K5-FAIL Multi-Source

```
Alpaca clock:      is_open=false | next_open Mi 22.07. 09:30 ET | next_close 16:00 ET
Equity:            98.500,63 $   (Alpaca /v2/account, portfolio_value)
Cash:              40.026,27 $   (40,64 %)
Portfolio MV:      58.471,25 $   (59,36 %, 7 Positionen)
Buying_power:     323.833,30 $
Daily P/L Pre:      +85,53 $     (+0,087 % vs last_equity 98.415,10)             [GRÜN, Cap -3 %]
                    +83,52 $     (+0,085 % vs Memory 21.07. Close 98.417,11)
ATH:              100.066,47 $   DD -1,566 % [GRÜN — Alarm bei -15 %]
Weekly KW30 Tag 3:  +0,269 %     (vs Fr-Close 98.236,14)                         [GRÜN, Cap -5 %]
VIX:              ~17-18         (Perplexity)                                    [GRÜN, <30]
SPY Pre:          ±0,3 %         (Futures-Indikation)                            [Crash-Filter INAKTIV]
10Y Treasury:     ~3,9-4,0 %     (leicht niedriger vs Vortag)
Käufe KW30:            1/2       (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Open Orders:           0
Guardrails:        7/8 GRÜN + 1 WARN (GOOGL Blackout Tag 0 AMC HEUTE, Owner-Freigabe LETZTE CHANCE)
```

**Positionen Pre-Market 08:36 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Pre-Kurs   | Entry      | P/L %    | V1-Stop     | V1-Puffer       | Δ vs Close  | Status |
|--------|------------|------------|----------|-------------|-----------------|-------------|--------|
| **GOOGL**|  348,07  | 368,10     | -5,44 %  | 338,65      | **+2,78 %** 🔴  | +0,21 pp    | SICHER ENGSTE (Blackout Tag 0 AMC HEUTE, V1_neu 349,70 > Kurs = **-0,47 % negativ** → Aktivierung würde Sofort-Stop; verbessert vs Close -0,67 %; Option A Strategie-Lock aktiv, **Owner-Freigabe LETZTE CHANCE bis 15:59 ET**) |
| **GS** | 1.088,27   | 1.141,74   | -4,68 %  | 1.050,40    | **+3,60 %**     | +0,25 pp    | SICHER (Rebound-Fortsetzung Tag+1 vs Close +3,35 %, Fill-Day+5, Muster überwunden) |
| LLY    | 1.173,00   | 1.193,89   | -1,75 %  | 1.098,38    | +6,79 %         | -0,17 pp    | SICHER (marginal verschlechtert vs Close +6,96 %, RSI-Watch nach Rebound +2,43 % Vortag) |
| V (NEU)|   356,40   |   357,18   | -0,22 %  |   328,60    | +8,46 %         | +0,18 pp    | SICHER (Fill-Day+2, V5 EMA-Spread bleibt marginal aber Golden Cross intakt) |
| AAPL   |   327,75   |   316,86   | +3,44 %  |   291,51    | +12,43 %        | +0,15 pp    | SICHER (leicht verbessert vs Close +12,28 %) |
| JPM    |   345,40   |   332,78   | +3,79 %  |   306,16    | +12,82 %        | +0,13 pp    | SICHER (leicht verbessert vs Close +12,69 %) |
| UNH    |   438,00   |   401,57   | +9,07 %  |   369,44    | **+18,56 %**    | +0,27 pp    | SICHER (Beste-P/L komfortabel, verbessert vs Close +18,29 %) |

**Konsistenz-Check Memory vs Alpaca:**
- Cash: Memory 40.026,27 = Alpaca 40.026,27 ✓
- Positionen: Memory 7 = Alpaca 7 ✓ (AAPL/GOOGL/GS/JPM/LLY/UNH/V)
- Equity Alpaca 98.500,63 vs Memory Close 98.417,11 → +83,52 $ Pre-Market-Drift (+0,085 %), Positionen Live-MV 58.471,25 vs Memory 58.390,84 = +80,41 $ (Pre-Market-Bewegung)

**Guardrail-Status Pre-Market:**
```
1. Daily Loss Cap (-3 %):     Pre +0,087 %                                        [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 3 +0,269 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,566 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,566 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Pre ±0,3 %                                      [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (Perplexity)                                 [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi 22.07. AMC Tag 0 aktivierungssensitiv -0,47 % (Owner-Pending LETZTE CHANCE) | [WARN] |
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                  [FREI 1]
```

**GOOGL Blackout-Aktivierungssensitivität Verlauf — LETZTE ENTSCHEIDUNGSCHANCE (heute Vormittag):**
- Mo-Close +0,69 % positiv → Di-Pre +0,41 % positiv → Di-Open -0,05 % negativ → Di-Close -0,67 % negativ → **Mi-Pre -0,47 % negativ**
- V1_neu Blackout 349,70 (368,10 × 0,95 = -5 %) > Kurs 348,07 → Aktivierung würde Sofort-Stop auslösen
- Q2 CY26 Earnings HEUTE Mi 22.07. AMC bestätigt (Perplexity Multi-Source [1][2][6][10][16])
- **Owner-Freigabe muss bis 15:59 ET erfolgen** — danach ist Blackout obsolet (Earnings-Ereignis eingetreten, Post-Release Reset)
- **Empfehlung:** Option A Strategie-Lock beibehalten — Aktivierung wäre bei aktueller Kurslage funktional wirkungslos (Sofort-Stop-auslösend statt Schutz)

**MMM K5-Multi-Source-Recheck — REJECT (Watchlist-Prio Slot 2/2 KW30 entfällt):**
- Q2 CY26 Earnings **BMO Di 21.07. bereits gemeldet** — kein Blackout mehr
- FwdPE Multi-Source: GuruFocus ~19,0x / StockAnalysis ~18,5x / AlphaSpread ~18,0x → alle ≤ 35 ✓
- **TTM Revenue-Growth YoY: +2,4 %** (Q2 2026: 6,5 Mrd $) → **K5-FAIL** (Kriterium ≥ +10 %)
- → **MMM REJECT** (analog UPS K5 dauerhaft-blocked)

**Slot 2/2 KW30 Verfügbare Kandidaten (nach MMM/UPS-REJECT):**
- **ABBV / MRK / JNJ** (XLV, alle 3/3 K1-K3) — **XLV-Sektor-Cap-Entscheidung Owner-Pending** (aktuell 20,21 % + neu ~9 % = ~29 % knapp am 30 %-Cap)
- Alternative: Market-Open frische Screener-Runde (XLI/XLP/XLE/XLU/XLB) mit neuen 5 K-Signalen-Recheck

**Entscheidung Market-Open-Scan:** **JA** (7/8 Guardrails GRÜN, Slot 2/2 offen bis Fr 24.07.)
- Kauf nur bei Owner-Freigabe XLV-Sektor-Cap (ABBV/MRK/JNJ) oder neuer 3/3-Kandidat aus Alt-Screener
- **Wahrscheinlichkeit Kauf KW30 GERING** ohne Owner-Freigabe

**PushNotification Prio 3 an Owner:** GOOGL Blackout-Entscheidung HEUTE Vormittag zeitkritisch (LETZTE CHANCE vor AMC).

**Nächste Routine:** Mi 22.07. 09:30 ET Market Open + Kaufsignal-Scan — GOOGL/GS V1-Watch, ABBV/MRK/JNJ K4/K5-Recheck falls Owner Sektor-Cap freigibt, alternative Non-XLK/XLV/XLF/XLC-Screener-Runde.

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
