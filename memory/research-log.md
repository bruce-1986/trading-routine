# Research Log

**Bot:** Bull | **Aktualisiert:** täglich

---

## Market Close 16:04 ET — 2026-06-30 (Di, KW27) — Tagesbilanz + Watchlist Mi 01.07.

**Tages-Performance (Alpaca + IEX-Bars Close 16:00 ET):**
```
Bull-Depot:   99.722,36 $   (vs last_equity 99.831,59)  Daily P/L -109,23 $  -0,1094 %  [GRÜN]
SPY:             746,65 $   (vs Mo-Close 740,86)         Daily +0,782 % (IEX 1Day-Bar)
Alpha:           -0,891 %   (Cash-Heavy 89 % → Beta-Verzicht an Risk-on-Tag)
ATH:          100.066,47 $  Drawdown -0,344 %  [GRÜN]
Weekly P/L:      -0,302 %   (KW27 Mo-Basis = Fr-Close 100.024,25)  [GRÜN >-5 %]
VIXY:             21,305 $  (-2,16 % vs gestern 21,775) → Spot ~17 [GRÜN]
Crash-Filter:    INAKTIV (SPY +0,78 %)
```

**SPY-Quelle:** Alpaca IEX 1Day-Bar 30.06. (Close 746,65 vs Mo-Close 740,86 = +0,782 %). Perplexity-SPY-Abfrage nicht erforderlich (Datum-in-Zukunft-Bug carry-over) — Alpaca-Bar autoritativ.

**Markt-News (Perplexity 30.06.):**
- S&P 500 + Nasdaq schliessen moderat höher nach cooler-than-expected Inflations-Daten → Fed-Rate-Cut-Erwartung steigt
- Megacap Tech + Large-Cap Pharma outperformed (LLY -2,4 % heute aber bleibt strukturell Pharma-Lead)
- Financials lagged auf lower-rate expectations + flatter Yield Curve (bestätigt JPM -0,66 %)

**Verkaufssignal-Check JPM + UNH (V1–V6 Close 16:00 ET, Alpaca IEX + Live-berechnete Indikatoren):**
```
Symbol | Close   | V1 Stop | V2 Trail | V5 EMA50/EMA200       | V6 RSI / RS_4w
JPM    | 327,24  | 306,16 ✓ +6,89 %  | 302,11 ✓ +8,28 %  | 314,15 > 308,78 ✓  | 57,6 / +11,86 % ✓
UNH    | 415,51  | 369,44 ✓ +12,47 % | 376,47 ✓ +10,38 % | 383,13 > 339,23 ✓  | 60,6 / +10,94 % ✓
```
→ **Keine pending Verkaufsorder für Mi.** Trail-Stop UNH bleibt 376,47 (Hoch 427,81 vom 26.06. carry-over, kein neues Hoch heute — Tageshoch 422,51).

**Watchlist-Scan Mi 01.07. (Alpaca IEX 200d-Window Close 30.06.):**
```
Symbol | Close   | K1 EMA50/EMA200        | K2 RSI14 | K3 RS_63d | K4 Vol% | K5            | Status
LLY    | 1199,36 | ✓ 1073,1 > 978,5      | ✓ 66,5  | ✓ +17,1 % | ✗ 99 %  | ✓ FwdPE 32–33 / Rev +26 % | 4/5 LEAD K4-Trigger
INTC   |  139,55 | ✓ 109,4 > 61,0        | ✓ 63,0  | ✓ +220,7%| ✗ 49 %  | unklar (Perplexity-Quelle leer) | 3/4 + K5-Recheck
CRWD   |  763,12 | ✓ 621,7 > 504,4       | ✗ 70,3  | ✓ +82,7 % | ✗ 85 %  | ✗ FwdPE ~69x                 | 2/5 BLOCKS
AMD    |  580,52 | ✓ 451,3 > 280,7       | ✓ 64,8  | ✓ +178,0%| ✓ 121 % | ✗ FwdPE 35–95x (Multi-Source) | 4/5 K5-BLOCKS (strukturell)
CAT    | 1063,33 | ✓ 906,6 > 694,5       | ✓ 65,3  | ✓ +41,2 % | ✗ 83 %  | ✗ RevGrowth Q1 -1 % YoY      | 3/5 BLOCKS
ELV    |  386,98 | ✓ 380,9 > 344,6       | ✗ 46,9  | ✓ +17,8 % | ✗ 69 %  | ✗ RevGrowth +7 % (Perplexity neu) | 2/5 BLOCKS
NVDA   |  199,93 | ✓ 204,8 > 190,5 knapp | ✗ 45,1  | ✗ +2,9 %  | ✗ 118 % | n/a                              | 2/4 K2+K3 BLOCKS
```

**Perplexity K5 Multi-Source-Verifikation 30.06.:**
- **LLY**: FwdPE 32,4–33,0 ✓ | Q1 2026 Rev YoY +26 % ✓ | Earnings 2026-07-31 ✓ — K5 voll bestätigt
- **CRWD**: FwdPE ~69x ✗ (carry-over Multi-Source: Yahoo 151, MarketBeat 798) — strukturell K5-blockiert bis EPS-Wendepunkt; Rev YoY +32 % ✓
- **CAT**: FwdPE ~15x ✓ aber RevGrowth Q1 2026 -1 % YoY ✗ — K5 RevGrowth-Hürde NEU bestätigt durch Perplexity
- **ELV**: FwdPE ~16x ✓ aber RevGrowth +7 % YoY ✗ (<10 %-Hürde) — Watch nach Q2-Earnings 17.07.
- **AMD**: FwdPE Konsens 35–95x (GuruFocus 37 / Finbox 70 / MarketBeat 94 / StockAnalysis 60–62) — strukturell K5-blockiert obwohl RevGrowth +37,8 % ✓ stark

**Watchlist morgen: LLY (Lead 4/5, K4 Vol-Trigger morgen entscheidend), INTC (3/4 K4 fehlt + K5 Pre-Market-Recheck zwingend), CAT (K5 strukturell), ELV (K2 + K5 Earnings-Trigger 17.07.).**

**Sektor-Check kompakt:** Health Care (XLV: LLY + UNH stark — bei LLY-Kauf morgen ~20 % Gesamt-Allocation, innerhalb 30 %-Limit). Financials (XLF: JPM Yield-Curve-Drag). Tech (XLK: 0 % Exposure — AMD/CRWD K5 strukturell blockiert, INTC einzige Hoffnung). Industrials (XLI: CAT K5 blockt).

**Entscheidung Market Close:**
- KEINE Verkaufsorders (alle V1–V6 SICHER für JPM + UNH).
- KEINE Pending Buys (Routine kauft erst bei Market Open mit K4-Live-Volumen).
- Bot bleibt Long JPM + UNH, 89 % Cash für LLY-Kauf-Setup morgen reserviert.
- **Nächste Routine:** Mi 2026-07-01 08:30 ET Pre-Market Check.

**Lessons:**
1. K5-FwdPE-Filter (≤35) blockt aktuell die gesamte Mega-Cap-Tech-Range außer NVDA (NVDA blockt an K2 RSI 45). Strategie-Disziplin: kein Override.
2. RSI-Cooldown bei LLY funktioniert (Mo 74,5 → Di 66,5) → K2 wieder ✓. Cooldown-Watch-Routine läuft sauber.
3. Bot Alpha heute -0,89 % strukturell durch Cash-Heavy bei risk-on. Akzeptabel solang Trades K5 ✓.
4. ClickUp Tier-Limit-Issue carry-over (ITEM_246 seit 26.06.) → Push-Notification + Memory primärer Notification-Kanal.

---

## Market Open 09:32 ET — 2026-06-30 (Di, KW27) — KEIN TRADE (CRWD K5 FAIL)

**Live-Snapshot Market Open (Alpaca 09:32 ET):**
```
Equity:             99.817,37 $   (vs last_equity 99.831,59 → -0,014 % GRÜN)
Cash:               88.767,74 $   (88,93 %)
Long MV:            11.049,63 $   (JPM 988,25 + UNH 10.056,04)
SPY:                  741,39 $    (+0,07 % vs Mo-Close 740,86 → flat Open)
VIXY:                  21,80 $    (+0,11 % vs Close 21,775 → Spot ~17,7)
DayTrade Count:     0 / PDT False | Buying Power: 386.009,92 $
Open Orders:        0
```

**Positionen Live V1–V6 (Alpaca trades latest, 09:32 ET):**
- JPM  329,29 $ — V1 306,16 SICHER +7,55 % | V2 ~302,11 SICHER +9,00 % | V5 EMA50 313,62>EMA200 307,76 ✓ | V6 RSI ~60 / RS_4w +12 % → KEIN Trigger
- UNH  419,255 $ — V1 369,44 SICHER +13,48 % | V2 ~376,47 SICHER +11,36 % | V5 EMA50 381,82>EMA200 340,19 ✓ | V6 RSI ~64 / RS_4w +12 % → KEIN Trigger

→ Keine Verkaufsorder pending. Beide Positionen V1–V6 vollständig SICHER.

**Kandidaten-Scan K1–K5 (Alpaca IEX-Bars vollständig 251 Daily Bars):**
- **CRWD** Close 29.06. 742,61 | Live 744,77 (+0,29 %)
  - **K1 ✓** EMA50 621,31 > EMA200 522,82 (Spread +98,49)
  - **K2 ✓** RSI(14) 68,88 (knapp unter 70 — Overheat-Watch)
  - **K3 ✓** RS_63d +84,03 % (CRWD +100,88 % vs SPY +16,85 %, gemessen 27.03.→29.06.)
  - **K4 N/A** (Open-Live-Vol bei 3 min IEX 1.408 — nicht aussagekräftig; Vortag 158 % Avg20 als Indikator)
  - **K5 ✗ FAIL** — Multi-Source-Verifikation Perplexity:
    - Yahoo Finance: FwdPE 151,52 (Trailing 401,83 oder "--")
    - MarketBeat: FwdPE 798,83 / TTM N/A (Earnings negativ -$0,19)
    - GuruFocus: At Loss (TTM-EPS -$0,69)
    - Wisesheets: TTM 181,37
    - Macrotrends: TTM 1.947,47
    - Companies Market Cap: TTM -947,42
    - **Konsens: FwdPE >>35 (selbst niedrigste Source 151) → K5 hart blockiert**
    - Rev YoY: +26 % (MarketBeat Q1 FY2027) → ✓ über 10 %-Hürde
  - **Verdict:** 4/5 — K5 BLOCKS. Pre-Market-Schätzung 28,5 erwies sich als Stat-Typ-Verwechslung (vermutlich P/S statt P/E) oder veraltete Datenquelle. CRWD aktuell **NICHT** strategiekonform investierbar bis EPS dauerhaft positiv.
- **LLY** carry-over Close 1.229,06 | K2 ✗ RSI 74,5 Overheat → Cooldown abwarten
- **CAT** carry-over Close 1.033,53 | K4 ✗ Vol 95 % + K5 ✗ FwdPE >35
- **ELV** carry-over Close 387,92 | K2 ✗ RSI 47,5 + K5 ✗ RevGrowth +1,5 %

→ **KEIN Kandidat erfüllt alle 5 Kaufsignale. KEIN Trade.**

**Guardrails (alle 8 GRÜN):**
- Daily P/L -0,014 % | Weekly KW27 -0,207 % | DD -0,249 % | VIX-Spot ~17,7 | Käufe 0/2 | Crash-Filter NEIN | Earnings-Blackout NEIN | Cash-Quote 88,93 % > 20 %

**ClickUp:** ROUTINE Normal-Alert (Prio 3) → ITEM_246 "Max usage for custom task types reached" (Tier-Limit-Issue seit 26.06.). Fallback: Push-Notification + Memory-Log.

**Lessons:**
1. K5 Pre-Market-Schätzung **immer** am Open Multi-Source verifizieren. Single-Quelle reicht nicht — Stat-Typ-Verwechslung (P/E vs P/S, TTM vs Forward) ist häufig.
2. CRWD strukturell von K5-Hard-Filter ausgeschlossen, solange Earnings negativ — vermerken für Watchlist-Pflege (nicht bei jedem Scan re-prüfen).
3. Tier-Limit ClickUp seit 26.06. open → Memory + Push als primärer Notification-Kanal.

**Entscheidung:** KEIN Trade. 2 Slots KW27 bleiben frei. Watchlist neu sortieren für Mi:
- LLY: RSI-Cooldown (auf <70 warten — heute Vorgang prüfen)
- CAT: K5-FwdPE warten (Q2-Earnings ~Mitte Juli könnte EPS-Bild verbessern)
- ELV: Q2-Earnings ~16.07. als Trigger für RevGrowth-Revision
- CRWD: Watchlist-Cooldown (mind. 1 Quartal positive EPS Voraussetzung)
- Neue Kandidaten-Suche: Top-3-Sektor-ETFs erneut via Perplexity beim Mi Pre-Market

**Nächste Routine:** 13:00 ET Midday Stop-Check.

---

## Pre-Market 08:30 ET — 2026-06-30 (Di, KW27) — Guardrails GRÜN, Buy-Scan JA, Lead CRWD

**Makro-Lage (Pre-Market 08:33 ET, Alpaca IEX + Perplexity):**
```
VIX (Spot):         17,65          [GRÜN — entspannt, <25 → 10 % Sizing erlaubt; Perplexity-Quelle Mo 29.06. via Yahoo]
SPY Last Trade:     741,61 $       (08:13 ET, vs Mo-Close 740,86 → +0,10 % flach Premarket)
SPY Quote 08:33 ET: bid 740,54 / ask 740,67 → Mid 740,605 $ (-0,03 %)
SPY Hourly Bar:     741,81 → 741,61 (08:00 ET, n=2 Trades, v=200)
VIXY Close 29.06.:  21,775 $       (-3,65 % vs Fr-Close 22,60 → Vola weiter abgebaut)
VIXY After-Hours:   bid 21,63 (20:00 UTC) → Spot ~17,5–18,0 konsistent zu Perplexity 17,65
10Y Treasury Yield: n/v (Perplexity-Quelle weiterhin leer — nicht handlungsblockierend)
Crash-Filter:       NEIN (SPY Mo +1,58 % → weit von -5 %)
Markt-Status:       CLOSED (next_open 09:30 ET)
```

**Alpaca Account-Status (Konsistenz-Check):**
```
Equity:             99.847,91 $    (Pre-Market Mark, vs Mo-Close 99.841,92 → +5,99 $ +0,006 % Settlement-Tick)
Cash:               88.767,74 $    (identisch zu Memory)
Last_Equity:        99.831,59 $    (Mo-EOD-Mark)
Long Market Value:  11.080,17 $    (JPM 988,41 + UNH 10.091,76)
Status:             ACTIVE (trading_blocked=false, account_blocked=false)
DayTrade Count:     0 / PDT False
Buying Power:       386.095,44 $   (Margin 4× Cash)
Open Orders:        0
Positions Live:     JPM 329,47 $ (P/L -1,00 %, change_today +0,02 %)
                    UNH 420,49 $ (P/L +4,71 %, change_today +0,16 %)
```

**Guardrails-Check (alle 8 Hierarchien):**
```
1. Daily Loss Cap (-3 %/Tag):    +0,016 % (99.847,91 / 99.831,59) [GRÜN]
2. Weekly Loss Cap (-5 %/Woche): -0,176 % (vs KW27 Mo-Basis 100.024,25 = Fr-Close) [GRÜN]
3. Drawdown vom ATH:             -0,219 % (vs ATH 100.066,47) [GRÜN — Alarm -15 % bei 85.057]
4. Drawdown-Stopp -20 %:         INAKTIV
5. Crash-Filter (SPY -5 %):      INAKTIV (Mo +1,58 %)
6. VIX-Filter (>30):             INAKTIV (17,65 → klar GRÜN, sogar <25 → 10 % Sizing)
7. Earnings-Blackout (3 HT):     KEINER — JPM 14.07. (14 Tage) | UNH 16.07. (16 Tage)
8. Max neue Käufe KW27:          0/2 genutzt → 2 frei
```
→ **STATUS: GRÜN auf allen 8 Levels.**

**Positionen Signal-Recheck (Pre-Market, V1–V6 carry-over Close 29.06. + Live-Adjustment):**
```
JPM    329,47 $ — V1 306,16 SICHER (+7,61 %) | V2 ~302,11 SICHER (+9,06 %) | V5 EMA50 313,62>EMA200 307,76 ✓ | V6 RSI ~60 / RS_4w +12 % → KEIN Trigger
UNH    420,49 $ — V1 369,44 SICHER (+13,82 %) | V2 ~376,47 SICHER (+11,68 %) | V5 EMA50 381,82>EMA200 340,19 ✓ | V6 RSI ~64 / RS_4w +12,4 % → KEIN Trigger
```
→ Keine Verkaufsorder pending. EMA50>EMA200 für beide intakt. RSI weit unter 80, RS positiv.

**Earnings-Korrektur (Perplexity verifiziert heute):**
- **JPM Q2 2026: 2026-07-14 (KORRIGIERT — bisher 07-15 angenommen)** — 14 Tage entfernt → KEIN Blackout
- UNH Q2 2026: 2026-07-16 (carry-over, Perplexity nicht final bestätigt, plausibel) — 16 Tage → KEIN Blackout
- Keine Stop-Tightening erforderlich (alle >3 HT entfernt).

**Top-News / Makro heute (Perplexity):**
- Perplexity lieferte keinen verifizierten US-Wirtschaftskalender für 30.06.2026 (Datum-in-Zukunft-Restriktion bleibt)
- Keine Top-3-Headlines belastbar abrufbar
- VIX-Spot 17,65 → Mo-Schlussstand (Yahoo via Perplexity), keine Spot-Print für Di 30.06. premarket
- VIXY-Tag −3,65 % bestätigt Vola-Entspannung — Risk-on-Stimmung hält an
- Bekannter Watchlist-Lead: **CRWD +6,08 % Mo** mit 4/4 tech-Kriterien voll erfüllt (Close 742,61)

**Watchlist-Status (Carry-over Close 29.06., Alpaca IEX):**
```
Symbol | Close   | K1     | K2 RSI | K3 RS_63d | K4 Vol% | K5 (Perplexity carry-over) | Score
CRWD   |  742,61 | ✓      | ✓ 67,6 | ✓ +84,0 % | ✓ 158 % | vorläufig ✓ FwdPE 28,5 / Rev YoY +12,3 % | 5/5 LEAD
LLY    | 1229,06 | ✓      | ✗ 74,5 | ✓ +23,1 % | ✓ 151 % | ✓ (32,39/+55,5 %) | 4/5 K2 BLOCKS (Overheat)
CAT    | 1033,53 | ✓      | ✓ 62,4 | ✓ +31,8 % | ✗ 95 %  | ✗ FwdPE >35 carry-over | 3/5 K4+K5 BLOCKS
ELV    |  387,92 | ✓      | ✗ 47,5 | ✓ +18,7 % | ✗ 72 %  | ✗ RevGrowth +1,5 % | 2/5 K2+K5 BLOCKS
```

**Entscheidung 09:30 ET Market Open:**
- **Buy-Scan JA** — Guardrails GRÜN, Pre-Market flach (+0,10 %), VIX entspannt (17,65), Vola-Entspannung (VIXY -3,65 %)
- **Lead-Kandidat: CRWD** (Close 742,61 — 4/4 technische Kriterien ✓, K5 vorläufig ✓)
  - **K5-Final-Check via Perplexity am Open zwingend:** FwdPE-Konsistenz (Yahoo/Marketwatch/Onvista), Q1 FY27 Rev YoY +12,3 % verifizieren
  - **K4 Live-Volumen am Open prüfen** — gestriger Trigger 158 % muss bei Open-Stunde bestätigt werden (CRWD gap-up möglich)
  - **K2 RSI nach +6 % Vortag:** falls Live-RSI bei Open >70 → K2 kippt
  - Limit-Order: max +0,5 % über Vortagesschluss = max 746,32 $ Limit
  - Sizing: ~10 % Portfolio = ~9.985 $ → 13 Shares bei ~745 $
- Sektor: CRWD = XLK Tech (Bot aktuell 0 % XLK) — würde Sektor-Lücke nach AVGO-V1 schließen
- Earnings: CRWD nächste Q1 FY27 release vermutlich Aug/Sep → kein Blackout
- Fallback: falls CRWD K5 final FAIL → kein Pflicht-Kauf, Slot bleibt frei (LLY RSI-Cooldown abwarten)
- Max 2 Käufe KW27 — nach CRWD (falls Trigger) noch 1 Slot frei

**Datenqualitäts-Hinweis:**
Perplexity Datum-in-Zukunft-Bug bleibt (keine 30.06.2026-Macro-Termine, keine spezifischen US-Headlines). Alpaca IEX SPY-Quotes/Bars + VIXY-Bars als Source of Truth für Premarket. VIX-Spot via Perplexity-Yahoo-Zitation (Mo-Schluss 17,65), plausibel zu VIXY-Drop.

---

## Market Close 16:00 ET — 2026-06-29 (Mo, KW27) — Tagesbilanz + Watchlist Di 30.06.

**Tages-Performance (Alpaca + IEX-Bars Close 16:00 ET):**
```
Bull-Depot:   99.841,92 $   (vs last_equity 100.024,25)  Daily P/L -182,33 $  -0,182 %  [GRÜN]
SPY:             740,86 $   (vs Fr-Close 729,35)         Daily +1,578 % (IEX)
Alpha:           -1,760 %   (Cash-Heavy 89 % → Beta-Verzicht an Risk-on-Tag)
ATH:          100.066,47 $  Drawdown -0,225 %  [GRÜN]
Weekly P/L:      -0,182 %   (KW27 Mo-Basis = Fr-Close 100.024,25)  [GRÜN >-5 %]
VIX-Tag:         carry-over Pre-Market 18,41  [GRÜN]
Crash-Filter:    INAKTIV (SPY +1,58 %)
```

**Hinweis Perplexity:** SPY-Abfrage lieferte halluzinierten Options-Kontrakt (745er Put statt SPY-Underlying). SPY-Close-Wert via Alpaca IEX-Bars (740,86) als autoritativ verwendet.

**Verkaufssignal-Check JPM + UNH (V1–V6 Close 16:00 ET, Alpaca IEX + Indikatoren):**
```
Symbol | Close   | V1 Stop | V2 Trail | V5 EMA50/EMA200       | V6 RSI / RS_4w
JPM    | 331,39  | 306,16 ✓ +8,23 %  | 302,11 ✓ +9,69 %  | 313,62 > 307,76 ✓  | 60,10 / +12,11 % ✓
UNH    | 420,00  | 369,44 ✓ +13,67 % | 376,47 ✓ +11,55 % | 381,82 > 340,19 ✓  | 64,15 / +12,43 % ✓
```
→ **Keine pending Verkaufsorder für Di.** Trail-Stop UNH bleibt 376,47 (Hoch 427,81 carry-over, kein neues Hoch heute).

**Watchlist-Scan Di 30.06. (Alpaca IEX 200d-Window Close 29.06.):**
```
Symbol | Close   | K1 EMA50>EMA200        | K2 RSI14 | K3 RS_63d | K4 Vol% | Status
CRWD   |  742,61 | ✓ 616,0 > 516,3       | ✓ 67,6  | ✓ +84,0 % | ✓ 158 % | 4/4 LEAD — K5 vorläufig ✓
LLY    | 1229,06 | ✓ 1068,0 > 969,2      | ✗ 74,5  | ✓ +23,1 % | ✓ 151 % | 3/4 K2 BLOCKS (heißer)
CAT    | 1033,53 | ✓ 900,2 > 694,3       | ✓ 62,4  | ✓ +31,8 % | ✗ 95 %  | 3/4 K4 + K5 carry-over
ELV    |  387,92 | ✓ 380,6 > 346,7       | ✗ 47,5  | ✓ +18,7 % | ✗ 72 %  | 2/4 K2 + K5 BLOCKS
NVDA   |  194,92 | ✓ 205,0 > 191,8 knapp | ✗ 40,2  | ✗ -0,4 %  | ✗ 74 %  | 1/4 K2 + K3 BLOCKS
AVGO   |  372,30 | ✓ 395,3 > 361,4 (Krs<EMA50) | ✗ 42,5 | ✓ +6,9 % | ✗ 55 % | 1/4 K2 + K4 BLOCKS (Watch nach V1-Stop 26.06.)
```

**Perplexity K5 Pre-Check (lead-Kandidaten):**
- **CRWD**: FwdPE 28,5 ✓ (≤35) | Umsatzwachstum YoY +12,3 % ✓ (Q1 FY27, Onvista) — K5 vorläufig ✓ → finale Verifizierung bei Market Open (Quelle-Konsistenz Yahoo/Marketwatch nötig)
- **LLY**: K5 carry-over ✓ vom Open (FwdPE 32,39, Rev +55,5 % YoY) — bleibt fundamental top, blockiert nur an K2 Overheat
- **CAT**: K5 carry-over FwdPE >35 — strukturell blockt
- **ELV**: K5 carry-over RevGrowth Q1 nur +1,5 % — Watch nach Q2-Earnings

**Watchlist morgen: CRWD (Lead, 4/4 tech, K5 ✓ vorläufig), LLY (RSI-Cooldown <70 abwarten), CAT (K4-Vol-Trigger + K5 strukturell), ELV (Earnings-Trigger ~16.07.).**

**Sektor-Check kompakt:** Tech-Sektor (XLK) führt heute mit CRWD +6 %, LLY +1,9 %, NVDA +1,5 %; Financials XLF stabil (JPM +0,7 %); Health Care XLV mixed (UNH -1,8 % Cooldown, LLY +1,9 %). Bot ist 0 % XLK exponiert — Möglichkeit für 1 Slot via CRWD morgen.

**Entscheidung Market Close:**
- KEINE Verkaufsorders (alle V1–V6 SICHER).
- KEINE Pending Buys (Routine kauft erst bei Market Open mit K4-Live-Volumen).
- Bot bleibt Long JPM + UNH, 88,91 % Cash für CRWD-Kauf-Setup morgen reserviert.
- **Nächste Routine:** Di 2026-06-30 08:30 ET Pre-Market Check.

---

## Market Open 09:33 ET — 2026-06-29 (Mo, KW27) — KEIN TRADE (LLY K2 blockt, ELV K5 blockt)

**Live-Daten (Alpaca IEX 09:32–09:33 ET):**
```
SPY:      737,80 $     (+1,16 % vs Fr-Close 729,35 — risk-on Open)
LLY:    1.216,74 $     (+0,84 % vs Fr-Close 1.206,57 — Folge-Gap nach Fr +7 %)
JPM:      329,31 $     (-1,04 % vs Entry, change_today +0,11 %)
UNH:      422,43 $     (+5,20 % vs Entry, change_today -1,27 % — Cooldown nach Fr +3 %)
Equity:  99.890,15 $   (Daily P/L -0,134 % vs last_equity 100.024,25)
```

**Kandidaten-Scan (Alpaca IEX Bars bis Close 26.06., 200 Tages-Window):**
```
Symbol | Close   | K1 EMA50/EMA200          | K2 RSI14 | K3 RS_63d | K4 Vol%    | K5 (Perplexity)        | Total
LLY    | 1206,57 | ✓ 1061,41 > 973,76       | ✗ 72,16  | ✓ +21,40% | ✓ 222 %    | ✓ FwdPE 32,39 / +55,5% | 4/5 K2 BLOCKS
ELV    |  395,20 | ✓ 380,31 > 343,77        | ✓ 51,93  | ✓ +21,28% | ✓ 138 %    | ✗ FwdPE 14,8 / +1,5%   | 4/5 K5-RevGrowth BLOCKS
CAT    |  998,18 | ✓ 894,79 > 687,30        | ✓ 58,67  | ✓ +15,88% | ✓ 220 %    | ✗ FwdPE 38,87–42,19    | 4/5 K5 BLOCKS
CI     |  282,39 | ✓ 283,57 > 281,51 knapp  | ✗ 47,27  | ✗ -9,25%  | ✓ 138 %    | n/a                    | 2/5
COR    |  286,08 | ✗ 285,88 < 322,37        | ✓ 58,58  | ✗ -23,10% | ✓ 125 %    | n/a                    | 2/5
CRWD   |  700,04 | ✓ 610,79 > 499,35        | ✓ 60,50  | ✓ +52,13% | ✗ 78 %     | wahrscheinlich FAIL    | 3/5
```

**Perplexity K5 Detail:**
- LLY: FwdPE 32,39 (TTM consensus bei $1206–1220) ✓ | Q1 2026 Rev YoY +55,5 % ✓ (GLP-1-Driven) | Earnings 06.08.2026 (38 Tage) ✓ keine Blackout
- ELV: FwdPE 14,8x ✓ | Q1 2026 Rev YoY nur +1,5 % (off. Filing) ✗ | Health-Insurer-Sektor strukturell langsam-wachsend → K5 RevGrowth-Hürde nicht passierbar mit aktuellem Quartal

**Schlussfolgerung:**
- LLY-Setup fundamental top (K1/K3/K4/K5 alle ✓), aber **RSI 72,16 = K2-Overheat** nach +7 %/+0,84 % Gap-up-Tagen. Diszipliniertes Warten = Strategie-Vorgabe.
- ELV blockt strukturell an K5-Revenue-Growth. Fundamentaldaten verbessern sich evtl. nach Q2-Earnings (~Mitte Juli) — Watch.
- CAT bleibt durch FwdPE >35 carry-over geblockt.

**Entscheidung Market Open:**
- **KEIN Kauf KW27 Mo.** 0/2 Slots genutzt, 2 frei.
- **Verkaufsorders:** Keine. Positionen JPM/UNH V1–V6 ALLE SICHER.
- **Nächste Routine:** 13:00 ET Midday Stop-Check.
- **Watchlist Di–Fr KW27:** LLY (RSI-Cooldown <70 abwarten — derzeit overheated), ELV (K5-Rev-Recheck nach Q2-Earnings ~16.07.), CRWD (Vol-Trigger), CAT (K5 strukturell blockt).

---

## Pre-Market 08:30 ET — 2026-06-29 (Mo, KW27) — Wochenstart, Guardrails GRÜN, Buy-Scan JA

**Makro-Lage (Pre-Market 08:33 ET, Alpaca IEX + Perplexity):**
```
VIX (Spot):         18,41           [GRÜN — deutlich unter 30, sogar unter 25-Schnitt]
SPY Premarket:      737,09          (vs Fr-Close 729,35 → +1,06 % Risk-on Open)
SPY Hourly Range:   734,52 – 738,10 (Pre-Market 04:00 ET → 08:00 ET)
VIXY (Fr-Close):    22,60           (kein Pre-Market-Update vor 09:30 ET, VIX-Spot Perplexity primär)
10Y Treasury Yield: n/v             (Perplexity-Quelle leer; nicht handlungsblockierend)
Crash-Filter:       NEIN            (SPY Fr -0,54 % > -5 %)
Markt-Status:       CLOSED          (next_open 09:30 ET)
```

**Alpaca Account-Status (Konsistenz-Check):**
```
Equity:             100.015,18 $    (Pre-Market-Mark, vs Fr-Close 100.025,35 → -10,17 $ -0,010 % drift)
Cash:               88.767,74 $     (vs memory 88.767,76 → identisch, $0,02 Rounding)
Last_Equity:        100.024,25 $    (Fr-Close — konsistent)
Status:             ACTIVE          (trading_blocked=false, account_blocked=false)
Positions Live:     JPM 329,50 $ (PnL -0,99 %, change_today +0,14 %)
                    UNH 427,46 $ (PnL +6,45 %, change_today -0,10 %)
Open Orders:        0
```

**Guardrails-Check (alle 8 Hierarchien):**
```
1. Daily Loss Cap (-3 %/Tag):    n/a (Wochenstart, kein last-EOD Vergleich relevant für Open)
2. Weekly Loss Cap (-5 %/Woche): RESET KW27 (Mo-Basis = 100.025,35 $ Fr-Close)
3. Drawdown vom ATH:             -0,051 % vs ATH 100.066,47 [GRÜN — Schwelle -15 % bei 85.057 $]
4. Drawdown-Stopp -20 %:         INAKTIV
5. Crash-Filter (SPY -5 %):      INAKTIV (Fr -0,54 %)
6. VIX-Filter (>30):             INAKTIV (18,41 → klar GRÜN)
7. Earnings-Blackout:            KEINER (JPM 07-15: 16d / UNH 07-16: 17d entfernt — >3d)
8. Max neue Käufe KW27:          0/2 genutzt
```
→ **STATUS: GRÜN auf allen 8 Levels.**

**Positionen Signal-Recheck (Pre-Market, V1–V6):**
```
JPM    329,50 $ — V1 306,16 SICHER (+7,62 %) | V5 EMA50>EMA200 ✓ carry-over | KEIN Trigger
UNH    427,46 $ — V1 369,44 SICHER (+15,71 %) | V2 ~376,4 SICHER (+13,55 %) | V6 RSI ~74 / RS_4w >+10 % → KEIN Trigger
```
→ Keine Verkaufsorder pending. EMA50>EMA200 für beide intakt.

**Earnings-Kalender nächste 3 Handelstage (für offene Positionen):**
- JPM Earnings: 2026-07-15 (16 Tage entfernt) → KEIN Blackout, V1 -8 % bleibt
- UNH Earnings: 2026-07-16 (17 Tage entfernt) → KEIN Blackout, V1 -8 % bleibt
- Keine Stop-Loss-Anpassung erforderlich.

**Top-News / Makro heute (Perplexity):**
- Perplexity-Quelle lieferte keine belastbaren neuen Top-3-News seit Fr-Close — niedrige News-Dichte
- VIX-Kommentar: Range 18,25–18,60 — ruhige Risiko-Stimmung
- Keine Termin-Daten in Quellen (Fed/CPI/PCE/Jobs nicht abrufbar via Perplexity heute)
- **Bekannte Watchlist-Bewegung Fr 26.06.: LLY +7,00 % Vol +217 %** — Lead für 09:30 ET Buy-Scan (K2/K5 Recheck zwingend)

**Entscheidung 09:30 ET Market Open:**
- Buy-Scan JA — Guardrails alle GRÜN, Pre-Market risk-on (+1,06 %), VIX entspannt
- Lead-Kandidat: **LLY** (Fr-Vol-Explosion 217 %, Watchlist-Lead) — K2 RSI nach Gap-up und K5 FwdPE-Recheck am Open zwingend
- Sektor-Check: LLY = XLV (zusammen mit UNH max 2 Positionen XLV → erlaubt unter 30 %-Limit)
- Falls LLY K5/K2 kippt: keine Pflicht zum Kauf, Slot ungenutzt lassen
- Max 2 Käufe KW27 — nach LLY (falls Trigger) noch 1 Slot frei für ggf. CAT/ELV/CI später

**Datenqualitäts-Hinweis:**
Perplexity Datum-in-Zukunft-Bug bleibt (keine 2026-Termine/News). Alpaca IEX SPY-Hourly-Bars als Source of Truth für Premarket. VIX-Spot 18,41 via Perplexity glaubwürdig (Range plausibel, Yahoo-Zitation).

---

## Market Close 16:00 ET — 2026-06-26 (Fr, KW26) — Tagesbilanz + Wochenabschluss + Watchlist Mo

**Makro-Lage (Tagesschluss, Alpaca IEX-Bar Source of Truth):**
```
SPY Close:        729,35 $ (-0,5427 % vs 733,33 Do-Close — risk-off Tag)
SPY Tagesspanne:  716,58 – 736,50 (Open 728,88 → intraday-Low -2,4 %, Close-Erholung)
VIXY Close:       22,60 $ (+0,49 % vs 22,49) → Spot ~21,6 [GRÜN <25]
Crash-Filter:     NEIN (SPY -0,54 % > -5 %)
Markt-Status:     CLOSED
```

**Tages-Performance Bull:**
```
Equity Start (last_equity): 99.925,53 $  →  Equity Close: 100.025,35 $
Daily P/L:                  +99,82 $  (+0,0999 %)
Alpha vs SPY:               +0,6426 %  [POSITIV stark — UNH +3,00 % treibt; JPM -1,97 % belastet; AVGO Realisierung -596,19 $ bereits in last_equity-Mark eingepreist]
Treiber:                    UNH +3,00 % auf neues Posit-Hoch 427,81 (+299,28 $ intraday unreal);
                            JPM -1,97 % Tagestief 327,50 (-19,77 $ intraday unreal).
ATH:                        100.066,47 $ (unverändert) | DD -0,041 % [GRÜN]
Weekly P/L:                 +0,0627 % vs Mo-Basis 99.962,66 [GRÜN — Limit -5 %]
Realisiert KW26:            -596,19 $ (AVGO V1 26.06.)
```

**Positionen Signal-Check Close (V1–V6) — alle SICHER, keine Verkaufsorder pending:**
```
Symbol | Close   | Entry   | P/L %   | V1 Stop | Puffer  | change | V5 EMA50/EMA200       | V6 RSI / RS_4w  | Status
JPM    | 328,53  | 332,78  | -1,28 % | 306,16  | +7,31 % | -1,97% | ~312,1 > ~301,8 ✓     | ~55 / +8,6 %    | SICHER (V1 weit weg)
UNH    | 428,00  | 401,57  | +6,58 % | 369,44  | +15,85% | +3,00% | ~377,6 > ~334,1 ✓     | ~75 / +12 %     | STARK (Posit-Hoch 427,81)
```
→ KEINE Verkaufsorder für Mo. EMA50>EMA200 für beide intakt. V6-RSI für UNH ~75 (knapp unter 80) ABER RS_4w stark positiv (+12 %) → V6 erfordert RSI>80 UND RS<0 → bleibt nicht ausgelöst.

**Watchlist Mo 29.06. (K1–K4 via Alpaca IEX-Bars Close 26.06., K5 carry-over Perplexity):**
```
Symbol | Close 26.06 | Chg Tag   | EMA50/EMA200       | RSI    | RS_63d vs SPY        | Vol/Avg20             | K1 K2 K3 K4 | K5            | Score
LLY    | 1.206,57    | +7,00 %!  | ~1060 / ~975       | ~68    | ~+25–30 %            | 305,6k / ~141k = 217%  | ✓ ✓ ✓ ✓     | ✓ (34,91 carry-over) | 5/5 möglich → LEAD
CAT    |   998,18    | -5,53 %   | ~890 / ~690        | ~58    | ~+30 %               | 294,8k / ~127k = 232%  | ✓ ✓ ✓ ✓     | FAIL (38,87–42,19) | 4/5 (K5 blockt)
CRWD   |   700,04    | +3,16 %   | ~610 / ~514        | ~58    | ~+55 %               |  89,9k / ~117k = 77%   | ✓ ✓ ✓ ✗     | FAIL ?         | 3/5
ANET   |   157,71    | -4,74 %   | ~156 / ~144        | ~46    | ~+3 %                | 560,5k / ~364k = 154%  | ✓ ✓ ✗-grenz ✗-vol(neg) | FAIL (44,13) | 2–3/5
```
→ **LEAD = LLY**: K4 Vol-Explosion 217 % (Gap-up +7,00 % auf 1.206,57!), K5 grenzwertig OK 34,91 (carry-over), K3 RS stark. **K2 (RSI nach Gap-up) und K5 (FwdPE-Recheck nach Kurssprung — könnte über 35 rutschen!) am Mo-Open zwingend verifizieren.**
→ **CAT**: Selloff nach Do-Vol-Explosion, K5 weiter blockierend. Watch.
→ **CRWD**: Vol bleibt schwach (77 %).
→ **ANET**: Selloff, K3 wahrscheinlich kippt, K5 FAIL.

**Watchlist Mo: LLY (Lead — K4 Vol-Explosion +217 %, K2/K5 Recheck am Open zwingend), CAT (K5 Block), CRWD (K4 schwach), ANET (Selloff, K5 FAIL)**

**Key-Beobachtungen Tag/Woche:**
```
1. UNH +3,00 % auf neues Posit-Hoch 427,81 — Health-Care weiter führend für unsere Allokation.
2. LLY massive Bewegung +7,00 % bei Vol +217 % — potenziell Earnings-Pre-Run/News-Trigger (07.08. Earnings, 42 Tage entfernt, kein Blackout).
3. SPY -2,01 % auf Wochenbasis (744,27 Mo → 729,35 Fr) — wir +0,063 % → Wochen-Alpha +2,07 %.
4. AVGO V1-Stop war sauberer Regel-Vollzug, -596,19 $ realisiert. Cash-Quote 88,75 % schützt vor weiterer Belastung.
5. Sektor-Lücke XLK (0 %) — Mo nicht zwingend füllen, LLY würde 2. XLV (zulässig ≤3 pro Sektor).
```

**Entscheidung Mo:**
- Pre-Market-Routine 29.06. 08:30 ET wie geplant.
- Buy-Scan 09:30 ET JA falls Guardrails GRÜN: **LLY K5-Recheck via Perplexity zwingend** (FwdPE nach +7 % Kurssprung vermutlich gestiegen; bei FwdPE >35 → K5 FAIL und Lead-Kandidat fällt).
- Sektor-Diversifikation beachten — falls LLY K5 kippt: kein Pflicht-Kauf, Slot ungenutzt lassen.

**Datenqualitäts-Hinweis:**
Perplexity SPY-Realtime nicht abgefragt (Datum-in-Zukunft-Bug bleibt). Alpaca IEX-Bar Source of Truth (-0,5427 % bestätigt). VIX-Spot via VIXY-Proxy 22,60 → Spot ~21,6.

**Lessons-Tag KW26 (Weekly Review heute Fr 17:00 ET):**
- KW26 1 Kauf (AVGO Mo), 1 Verkauf (AVGO V1 Fr) — voller Trade-Zyklus in 5 Tagen
- Wochen-Alpha +2,07 % stark trotz realisiertem Verlust (Cash-Schutz wirkt)
- LLY heute Vol-Explosion = bestätigt: Lead-Watchlist-Disziplin liefert auch bei Verzögerung Kandidaten

---

## Market Open 09:34 ET — 2026-06-26 (Fr, KW26) — V1 AVGO STOP-LOSS ausgelöst, KEIN Trade-Buy

**Markt (Live Open 09:33 ET):**
```
SPY Live:         727,42 $ (-0,80 % vs Close 733,33) → Risk-off, aber Crash-Filter NEIN
VIXY Live:         23,36 $ (+3,87 % vs 22,49 Close) → Spot ~22,3 [GRÜN <25 → 10 % Sizing]
VIX-Quelle:        Alpaca Bar (Perplexity nicht zwingend)
Markt-Status:      OPEN
```

**V1 STOP-LOSS — AVGO TRIGGERED & FILLED:**
```
Trigger:           Last Trade $370,13 < V1 Stop $371,14 (Pre-Market-Puffer war +0,16 %)
Order:             SELL 17 Sh @ Market → FILLED @ $368,34 avg um 09:33:28 ET
Entry:             $403,41 (Kauf 22.06.)
Realisierter Verlust: -596,19 $ (-8,69 % vs Entry)
Order-ID:          c5b9adf0-229d-4330-9f75-9672674b946f
ClickUp:           Tier-Limit ITEM_246 — Push-Notification stattdessen
```

**Account nach Sell (Alpaca 09:34 ET):**
- equity 99.817,78 $ | cash 88.767,76 $ (88,92 %) | long_market_value 11.050,02 $ (11,07 %)
- Daily P/L: -0,108 % [GRÜN — Limit -3 %] (99.817,78 / 99.925,53)
- Weekly P/L: -0,145 % vs Mo-Basis 99.962,66 [GRÜN — Limit -5 %]
- DD vom ATH 100.066,47: -0,249 % [GRÜN]
- Käufe KW26: 1/2 (AVGO 22.06., heute gestoppt) | Pending Orders: 0
- Realisiert YTD: -596,19 $ (erster geschlossener Trade des Bots)

**Positionen Live nach Sell:**
```
Symbol | Last     | Entry   | P/L %   | V1 Stop | Puffer  | change_today | Status
JPM    | 334,95   | 332,78  | +0,65 % | 306,16  | +9,48 % | -0,05 %      | SICHER
UNH    | 417,95   | 401,57  | +4,08 % | 369,44  | +13,12% | +0,58 %      | SICHER (Posit-Hoch)
```

**Kandidaten-Scan K1–K5 (Watchlist KW26, Live 09:33 ET):**
```
Symbol | Live      | Chg vs Close | K1 K2 K3 K4 (Live)   | K5            | Score / Block
CAT    | 1.018,71  | -3,59 %      | carry-over K1✓K2✓K3✓ K4 Live n/a (Pullback) | FAIL FwdPE >35 | 4/5 (K5 hard-blockt)
LLY    | 1.145,81  | +1,61 %      | K1✓K2✓K3✓ K4 schwach (gestern 83 %)           | ✓ (34,91 grenz) | 4/5 (K4 schwach + Live-Vol nicht bestätigt)
ANET   |   157,09  | -5,11 %      | K1✓K2✓K3✓ K4 Live n/a (Selloff)                | FAIL (44,13)   | 3/5
CRWD   |   678,29  | -0,05 %      | K1✓K2✓K3✓ K4 schwach (gestern 51 %)            | FAIL (Cloud)   | 3/5
```
→ **KEIN Kandidat erfüllt alle 5 Signale.** Plus 3 belastende Faktoren:
1. Markt risk-off (SPY -0,80 %, VIX +3,87 %)
2. Frischer V1-Stop-Out AVGO — Strategie-Regel "No-Action bei Unsicherheit"
3. CAT/ANET fallen direkt am Open trotz gestriger Stärke = Sentiment-Wechsel

→ **KEIN Kauf heute.** 1 Slot KW26 bleibt ungenutzt (letzter Handelstag).

**Sektor-Snapshot nach Sell:**
- XLF (JPM):   1.004,85 $ → 1,01 % Gesamt / 9,09 % invest.   | 1 Pos
- XLV (UNH):  10.030,80 $ → 10,05 % Gesamt / 90,78 % invest. | 1 Pos
- XLK (AVGO): 0 $ → KEINE TECH-EXPOSURE mehr (war 6,28 %)
→ Sektor-Konzentration jetzt extrem in XLV — bei nächstem Kauf Mo XLK/XLI/Industrials priorisieren.

**Lessons-Tag für Weekly Review (Fr 17:00 ET):**
- V1 Stop-Loss hat sauber gegriffen (Pre-Market Warnung +0,16 % Puffer → Open-Trigger exakt eingetreten)
- Erster realisierter Verlust seit Bot-Init 31.05. → -596,19 $ realisiert
- AVGO-Kauf 22.06. war K1–K5 ✓, aber Partial-Fill nur 17/24 + ungünstiges Timing (Tech-Schwäche Mo-Di)
- Lehre: Bei sehr schmalem V1-Puffer (<1 %) am Pre-Market könnte ein präventiver Stop-Tightening/Pre-Open-Manuell-Sell-Markt überlegt werden (aktuell nicht in Strategie)

**Nächste Routine:** Midday 13:00 ET — Stop-Check JPM/UNH + Daily-Cap-Re-Check (-3 %)

---

## Pre-Market 08:30 ET — 2026-06-26 (Fr, KW26) — AVGO V1-ALERT

**Marktdaten:**
- VIX Spot **20,29** (Perplexity, +7,41 % vs Vortag 18,87) — Vola steigt, aber <25 → 10 % Sizing erlaubt, kein VIX-Filter
- SPY Pre-Market Mid **730,32 $** (Alpaca IEX-Quote 08:33 ET, bid 730,23 / ask 730,40) → **-0,41 %** vs Close 25.06. 733,33 [GRÜN, weit über -2 %]
- VIXY After-Hours-Tick: 21,68 $ (Close 25.06.) → bestätigt Vola-Anstieg
- 10Y Treasury Yield: via Perplexity nicht verfügbar (Datums-Restriktion)
- Crash-Filter: NEIN (SPY gestern +0,001 % flat)

**Alpaca-Account (Pre-Market 08:32 ET):**
- equity **99.819,55 $** | cash 82.505,98 $ | last_equity 99.925,53 $ | portfolio_value 99.819,55 $
- Daily P/L: **-0,106 %** [GRÜN — Limit -3 %]
- Weekly P/L: **-0,143 %** vs Mo-Basis 99.962,66 [GRÜN — Limit -5 %]
- DD vom ATH 100.066,47: **-0,247 %** [GRÜN — Alarm -15 %]
- Reconciliation portfolio.md Close 25.06. 99.972,12 $ vs Alpaca last_equity 99.925,53 $ → Diff -46,59 $ Settlement-Tick (After-Hours Mark-to-Market), OK
- Käufe KW26: 1/2 (1 Slot frei — letzter Handelstag KW26) | Pending Orders: 0

**Positionen Live (Alpaca 08:32 ET):**
```
Symbol | Last     | Entry   | P/L %   | V1 Stop | Puffer  | change_today | Status
JPM    | 336,00   | 332,78  | +0,97 % | 306,16  | +9,75 % |  +0,26 %     | SICHER
UNH    | 416,10   | 401,57  | +3,62 % | 369,44  | +12,63% |  +0,14 %     | SICHER
AVGO   | 371,72   | 403,41  | -7,86 % | 371,14  | +0,16 % |  -1,90 %     | KRITISCH HÖCHSTSTUFE
```
→ **AVGO V1-Schwelle praktisch erreicht** (Last 371,72 $ vs Stop 371,14 $, Puffer nur +0,16 %).
→ Bei Open ≤ 371,14 $ wird V1 Market-Order automatisch ausgelöst (17 Shares Verkauf, Verlust -538,80 $ unreal aktuell).
→ Pre-Market-Quote bid 359,55 / ask 398,45 nicht verlässlich (Spread zu breit) — Last-Trade 371,72 vom After-Hours-Close.

**Earnings-Blackout-Check (nächste 3 HT, Perplexity 26.06.):**
- JPM: 14.07.2026 (CONFIRMED) → 18 Tage entfernt → KEIN Blackout
- UNH: Mitte Juli 2026 (carry-over) → ~20 Tage entfernt → KEIN Blackout
- AVGO: August 2026 (carry-over) → >35 Tage entfernt → KEIN Blackout
- → KEIN Stop-Tightening nötig (Standard V1 -8 % bleibt).

**Guardrails-Status (alle GRÜN):**
- Daily Loss Cap -3 %: NEIN (-0,11 %)
- Weekly Loss Cap -5 %: NEIN (-0,14 %)
- Drawdown-Alarm -15 %: NEIN (-0,25 %)
- Drawdown-Stopp -20 %: NEIN
- Crash-Filter SPY -5 %: NEIN (gestern +0,001 %)
- VIX-Filter >30: NEIN (20,29 — sogar <25 → 10 % Sizing)
- Käufe-Limit 2/Wo: 1/2 (1 Slot frei, letzter Tag KW26)

**Makro-Events 26.06. (Perplexity sonar-pro):**
- U-Michigan Consumer Sentiment Final 10:00 ET (zentrales Stimmungs-Update)
- KEIN FOMC/PCE/GDP-Release bestätigt
- VIX +7,41 % steigend trotz freundlicher Vortagsstimmung — leichte Risk-off-Tendenz Pre-Market (SPY -0,41 %)
- Keine spezifischen Top-3-News belastbar in Quellen identifizierbar

**Entscheidung Pre-Market:**
- Market-Open-Scan 09:30 ET: **JA** — alle Guardrails GRÜN, ABER erhöhte Vorsicht (SPY Pre-Market -0,41 %, VIX-Anstieg +7,4 %, AVGO V1-Schwelle).
- **Priorität HÖCHSTE Stufe**: AVGO-V1-Stop-Watch. Stop ist hart (kein manueller Eingriff). Bei Open ≤ 371,14 $ → V1 Market-Order automatisch.
- Watchlist KW26 (1 Slot frei, letzter Tag): CAT (Lead — gestern Vol-Explosion 237 % bei +6,28 %, K5 FwdPE-Recheck am Open zwingend), ANET (K4 nahe Trigger 111 %, K5 FAIL FwdPE 44,13), LLY (K4 schwach 83 %), CRWD (K4 sehr schwach 51 %).
- Kauf nur bei vollem K1–K5 und sehr starkem Setup (Risk-off + AVGO-Druck = Vorsichtsmodus).

---

## Market Close 16:00 ET — 2026-06-25 (Do, KW26) — KEIN TRADE

**Makro-Lage (Tagesschluss, Alpaca IEX-Bar Source of Truth):**
```
SPY Close:        733,33 $ (+0,001 % vs 733,32 Mi-Close — quasi flach)
SPY Tagesspanne:  729,63 – 739,31 (Open 738,90 → Pullback)
VIX-Proxy VIXY:   22,49 $ (-1,53 % vs 22,84) → Spot ~21,5 [GRÜN <25]
Crash-Filter:     NEIN (SPY flach < |-5 %|)
Markt-Status:     CLOSED
```

**Tages-Performance Bull:**
```
Equity Start (last_equity): 99.740,72 $  →  Equity Close: 99.972,12 $
Daily P/L:                  +231,40 $  (+0,232 %)
Alpha vs SPY:               +0,231 %  [POSITIV]
Treiber:                    UNH +2,51 % auf neues Posit-Hoch 417,54 (+345,84 $ unreal P/L);
                            JPM +0,51 %; AVGO -0,28 % (leichter Drift Richtung V1-Watch).
ATH:                        100.066,47 $ (unverändert) | DD -0,094 % [GRÜN]
Weekly P/L:                 +0,0095 % vs Mo-Basis 99.962,66 [GRÜN — Limit -5 %]
```

**Positionen Signal-Check Close (V1–V6) — alle SICHER, keine Verkaufsorder pending:**
```
Symbol | Close   | Entry   | P/L %   | V1 Stop | Puffer  | change | V5 EMA50/EMA200       | V6 RSI / RS_4w  | Status
JPM    | 335,15  | 332,78  | +0,71 % | 306,16  | +9,47 % | +0,51% | ~311,5 > ~301,5 ✓     | ~67 / +10 %     | SICHER (Hoch heute 343,31)
UNH    | 415,98  | 401,57  | +3,59 % | 369,44  | +12,60% | +2,51% | ~375,5 > ~333,2 ✓     | ~70 / +>8 %     | STARK (neues Posit-Hoch 417,54)
AVGO   | 381,01  | 403,41  | -5,55 % | 371,14  | +2,66 % | -0,28% | ~397,4 > ~356,2 ✓     | ~46 / ~-6 %     | KRITISCH (Watch)
```

**Watchlist morgen (Fr 26.06., K1–K4 via Alpaca IEX-Bars Close 25.06., K5 carry-over):**
```
Symbol | Close 25.06 | Chg Tag   | EMA50/EMA200 | RSI    | RS_63d vs SPY | Vol/Avg20            | K1 K2 K3 K4 | K5         | Score
CAT    | 1.056,65    | +6,28 %!  | 883,8>684,1  | ~65    | ~+34 % vs +12 | 296,3k / ~125k = 237%| ✓ ✓ ✓ ✓     | FAIL (38,87–42,19) | 4/5 (K5 blockt)
LLY    | 1.127,63    | +0,92 %   | 1052,6>962,6 | ~58    | ~+12 %        | 117,3k / ~141k = 83% | ✓ ✓ ✓ ✗     | ✓ (34,91)  | 3/5 (K4 schwach)
ANET   |   165,56    | +2,29 %   | 156,6>144,0  | ~52    | ~+8 %         | 404,1k / ~364k = 111%| ✓ ✓ ✓ grenz| FAIL (44,13)| 3/5
CRWD   |   678,62    | +0,88 %   | 604,2>510,4  | ~55    | ~+50 %        | 59,2k / ~117k = 51%  | ✓ ✓ ✓ ✗     | FAIL ?     | 3/5
```
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Slot KW26 (1/2) bleibt frei für Fr.
→ **Lead: CAT** — heute Volumen-Explosion 237 % Avg20 und +6,28 % Tagesgewinn (mögliche News/Sektor-Rotation Industrials/XLI). K5 (FwdPE) bleibt blockierender Faktor — am Open via Perplexity zwingend rechecken, ob Konsensus-Revisions FwdPE < 35 drücken.
→ ANET nähert sich K4-Trigger (111 %) — bei weiterem Volumen-Push morgen erneut prüfen.

**Watchlist morgen: CAT (Lead, K5 Recheck), ANET (K4 nahe Trigger), LLY (K4 schwach), CRWD (K4 sehr schwach)**

**Key-News (knapp):**
```
1. Industrials/Materials zeigen Stärke (CAT +6,28 % bei Vol-Explosion) — mögliche Rotation aus Mega-Cap-Tech
2. SPY tagesspannig (Open 738,90 → Close 733,33, intraday -1,29 % vom Hoch) — Pullback-Day mit knappem Plus
3. VIXY -1,53 % → Spot ~21,5 entspannt; KEINE Filter aktiv
```

**Entscheidung morgen:**
Pre-Market-Routine 08:30 ET wie geplant. Buy-Scan 09:30 ET JA, falls Guardrails GRÜN — CAT-Recheck K5 prioritär, sonst Slot KW26 bleibt frei (letzter Handelstag KW26 → Wochen-Slot verfällt).

**Datenqualitäts-Hinweis:**
Perplexity SPY-Realtime liefert Pre-Market-Werte (+0,77 %) statt Tagesschluss — Datum-in-Zukunft-Bug bleibt bestehen. Alpaca IEX-Bar = Source of Truth. Sektor-/Volume-Daten ebenfalls aus Alpaca, da Perplexity keine SPDR-ETF-Sektorperformance liefert.

---

## Market Open 09:33 ET — 2026-06-25 (Do, KW26) — KEIN KAUF

**Guardrail-Check (alle GRÜN):**
- Daily P/L +0,184 % (equity 99.924,28 / last 99.740,72) [GRÜN — Limit -3 %]
- Weekly P/L -0,038 % (vs Mo-Basis 99.962,66) [GRÜN — Limit -5 %]
- Drawdown vom ATH 100.066,47: -0,142 % [GRÜN — Alarm -15 %]
- VIX-Proxy VIXY 22,10 (-3,24 % vs 22,84) → Spot ~20,9 < 30 [GRÜN; <25 → 10 % Sizing erlaubt]
- Crash-Filter NEIN (SPY 737,54 = +0,576 % vs Close 24.06. 733,32)
- Cash 82,57 % > 20 % Mindestreserve
- Käufe KW26: 1/2 → 1 Slot frei

**Positionen Live (Alpaca 09:32 ET), V1–V6 Signal-Check:**
```
Symbol | Last     | Entry   | P/L %   | V1 Stop | Puffer  | change_today | V5 EMA50/EMA200       | V6 RSI / RS_4w   | Status
JPM    | 335,96   | 332,78  | +0,96 % | 306,16  | +9,73 % |  +0,75 %     | ~311,3 > ~301,4 ✓     | ~66 / +9,9 %     | SICHER
UNH    | 411,37   | 401,57  | +2,44 % | 369,44  | +11,35% |  +1,37 %     | ~375,1 > ~332,8 ✓     | ~61 / +6,5 %     | SICHER
AVGO   | 384,57   | 403,41  | -4,67 % | 371,14  | +3,62 % |  +0,66 %     | ~397,7 > ~355,8 ✓     | ~45 / ~-6 %      | ENTSPANNT
```
→ Alle V1–V6 NICHT ausgelöst. AVGO V1-Puffer +3,62 % (vs Close 24.06. +3,33 %) — leichte Entspannung dank intraday-Erholung.
→ Kein Eingriff (regelbasiert: Stop läuft automatisch bei ≤ 371,14 $).

**Kandidaten-Scan (Watchlist KW26, K1–K4 via Alpaca-IEX-Bars bis Close 24.06., K5 carry-over verifiziert 24.06.):**
```
Symbol | Close 24.06 | EMA50/EMA200      | RSI(14) | RS_63d vs SPY  | Vol/Avg20          | K1 K2 K3 K4 | K5
CAT    |    994,18   |  883,81 /  684,07 |  62,61  | +38,74 / +12,27| 136,8k/123,4k=110,9%| ✓ ✓ ✓ ✗    | ✗ FAIL (FwdPE 38,87/42,19 > 35)
LLY    |  1.117,35   | 1052,56 /  962,58 |  57,99  | +23,73 / +12,27| 111,7k/137,4k= 81,3%| ✓ ✓ ✓ ✗    | ✓ grenzwertig (FwdPE 34,91)
CRWD   |    672,72   |  604,23 /  510,43 |  54,74  | +71,25 / +12,27|  37,7k/116,9k= 32,3%| ✓ ✓ ✓ ✗    | vermutlich FAIL (Cloud-SaaS >35)
ANET   |    161,87   |  156,64 /  144,03 |  50,95  | +23,76 / +12,27| 250,8k/364,4k= 68,8%| ✓ ✓ ✓ ✗    | ✗ FAIL (FwdPE 44,13)
```
SPY 63d Return: +12,27 % (Baseline für RS).

**Auswahl:**
- CAT: K1–K3 stark (RS +26,48 %), aber K4 110,9 % < 120 % Schwelle und K5 FAIL → 3/5.
- LLY: K1–K3 ✓, K5 ✓ grenzwertig, aber K4 81,3 % FAIL → 4/5.
- CRWD: K1–K3 ✓ (RS +58,98 % stark), aber K4 32,3 % stark FAIL → max 3/5.
- ANET: K1–K3 ✓, aber K4 68,8 % FAIL und K5 44,13 > 35 FAIL → 3/5.
- → **KEIN Kandidat erfüllt alle 5 Kaufsignale** → Kauf-Slot bleibt ungenutzt für 25.06.

**Markt-Kontext (Risk-on, Vola entspannt):**
- SPY 737,54 = +0,576 % intraday (Pre-Market +0,78 % teils bestätigt — leichte Abschwächung nach Open)
- VIXY 22,10 (-3,24 % vs Close 22,84) → VIX Spot ~20,9 (klar entspannt)
- Intraday-Pops auf Watchlist (CAT +3,59 %, ANET +3,20 %, CRWD +2,02 %, LLY +0,26 %) — Vol-Bilanz wird erst über volle Session aussagekräftig.
- AVGO Erholung +0,66 % intraday — V1-Stop-Druck weiter nachgelassen.

**Entscheidung Market-Open:**
- KEIN Buy (kein Kandidat mit allen K1–K5 ✓).
- KEIN Sell (V1–V6 für alle 3 Positionen NICHT ausgelöst).
- Priorität bis 13:00 Midday-Check: AVGO weiter im Erholungs-Watch (V1 371,14 $ Puffer +3,62 % komfortabel).
- 1 Slot KW26 bleibt für Fr (letzter Handelstag der Woche).

**Datenquellen:**
- Alpaca /v2/account, /v2/positions, /v2/orders, /v2/clock (09:32 ET) — `is_open=true`
- Alpaca Market Data IEX-Feed: SPY/VIXY/CAT/LLY/CRWD/ANET latest trades + 225 daily bars (start 2025-08-01) für K1–K4.
- K5-Fundamentals carry-over aus Close 24.06. (Perplexity-Verifizierung von gestern bleibt aktuell — keine Earnings/Guidance heute).

---

## Pre-Market 08:30 ET — 2026-06-25 (Do, KW26)

**Marktdaten:**
- VIX Spot **17,93** (Perplexity finanzen.net, -3,76 % vs 18,63) — deutlich entspannter vs Vortag 19,49 → GRÜN <25 → 10 % Sizing erlaubt
- SPY Pre-Market Mid **739,04 $** (Alpaca Quote 08:33 ET, bid 738,95 / ask 739,13) → **+0,78 %** vs Close 24.06. 733,32 [GRÜN, weit über -2 %]
- VIXY After-Hours Quote: bid 22,11 / ask 23,61 (Mid 22,86, t=24.06. 20:00 UTC) — bestätigt entspanntes Vola-Bild
- 10Y Treasury Yield: via Perplexity nicht verfügbar (Datums-Restriktion)
- Crash-Filter: NEIN (SPY 24.06. -0,041 % → weit von -5 %)

**Alpaca-Account (Pre-Market 08:32 ET):**
- equity **99.840,20 $** | cash 82.505,98 $ | last_equity 99.740,72 $ | portfolio_value 99.840,20 $
- Daily P/L: **+0,0997 %** [GRÜN — Limit -3 %]
- Weekly P/L: **-0,123 %** vs Mo-Basis 99.962,66 [GRÜN — Limit -5 %]
- DD vom ATH 100.066,47: **-0,226 %** [GRÜN — Alarm -15 %]
- Reconciliation portfolio.md Close 24.06. 99.772,92 $ vs Alpaca last_equity 99.740,72 $ → Diff -32,20 $ Settlement-Tick (After-Hours Mark-to-Market), OK
- Käufe KW26: 1/2 (1 Slot frei für Do/Fr) | Pending Orders: 0

**Positionen Live (Alpaca 08:32 ET):**
```
Symbol | Last     | Entry   | P/L %   | V1 Stop | Puffer  | change_today | Status
JPM    | 334,02   | 332,78  | +0,37 % | 306,16  | +9,10 % |  +0,17 %     | SICHER
UNH    | 405,05   | 401,57  | +0,87 % | 369,44  | +9,64 % |  -0,18 %     | SICHER
AVGO   | 388,88   | 403,41  | -3,60 % | 371,14  | +4,78 % |  +1,78 %     | ENTSPANNT (Erholung +1,78 %)
```
→ AVGO-Puffer hat sich von Close +3,33 % auf +4,78 % verbessert (Erholung +1,78 % Pre-Market). Kein Stop-Druck.

**Earnings-Blackout-Check (nächste 3 HT, Perplexity verifiziert):**
- JPM: 14.07.2026 (CONFIRMED Wall Street Horizon) → 19 Tage entfernt → KEIN Blackout
- UNH: 16.07.2026 (carry-over verifiziert 24.06.) → 21 Tage entfernt → KEIN Blackout
- AVGO: 29.08.2026 (carry-over verifiziert 24.06.) → 65 Tage entfernt → KEIN Blackout
- → KEIN Stop-Tightening nötig (Standard V1 -8 % bleibt).

**Guardrails-Status (alle GRÜN):**
- Daily Loss Cap -3 %: NEIN (+0,10 %)
- Weekly Loss Cap -5 %: NEIN (-0,12 %)
- Drawdown-Alarm -15 %: NEIN (-0,23 %)
- Drawdown-Stopp -20 %: NEIN
- Crash-Filter SPY -5 %: NEIN (gestern -0,04 %)
- VIX-Filter >30: NEIN (17,93 — sogar <25 → 10 % Sizing)
- Käufe-Limit 2/Wo: 1/2 (1 Slot frei)

**Makro-Events 25.06. (Perplexity):**
- Keine bestätigten US-FOMC/CPI/PCE-Releases in Perplexity-Treffern (sonar-pro lieferte nur DE-Bundesbank-Konjunkturprognose 11:00 als gesicherten Termin)
- VIX bei -3,76 % Vortagestief → Risk-on-Tendenz nach Di-Sell-Off und Mi-Konsolidierung
- Keine Top-3-Earnings/News spezifisch belastbar — Marktkontext bleibt neutral mit Vola-Entspannung

**Entscheidung Pre-Market:**
- Market-Open-Scan 09:30 ET: **JA** — alle Guardrails GRÜN, SPY Pre-Market positiv (+0,78 %), VIX 17,93 deutlich unter 25.
- Priorität: AVGO Erholungs-Watch (V1-Puffer jetzt komfortabel +4,78 %; Stop bleibt automatisch bei ≤ 371,14 $).
- Watchlist KW26 (1 Slot frei für Do/Fr): CAT (Lead-Kandidat K1–K4 ✓, K5 FwdPE >35 Block — Perplexity-Recheck am Open), LLY (K4 Vol-Trigger >120 % abwarten), CRWD (K4 sehr schwach 26 %, vermutlich kein Setup), ANET (K5 FAIL bleibt).
- Kauf nur bei vollem K1–K5.

---

## Market Close 16:00 ET — 2026-06-24 (Mi, KW26) — Tagesbilanz + Watchlist 25.06.

**Tagesperformance:**
- Alpaca equity Close: 99.772,92 $ (vs last_equity 99.792,95 → -20,03 $ / -0,0201 %) [GRÜN — Limit -3 %]
- SPY 24.06. Close 733,32 (Alpaca IEX-Bar) vs 23.06. Close 733,62 → -0,041 %
- Alpha heute: +0,021 % (leicht positiv durch hohe Cash-Quote 82,69 %)
- Weekly P/L: -0,190 % vs Mo-Basis 99.962,66 → GRÜN, kein WEEKLY_CAP
- ATH 100.066,47 $ unverändert | DD -0,293 % [GRÜN]
- VIXY 22,84 (-0,7 % vs 23,00) → Spot ~21,6 → GRÜN (<25 → 10 % Sizing erlaubt)
- Crash-Filter NEIN | VIX-Filter NEIN | Käufe KW26: 1/2 (1 Slot frei)

**Hinweis Datenquellen-Diskrepanz:**
- Perplexity SPY 24.06.: +0,29 % (cnbc.com Snapshot 735,17 vs 733,58) — Datum-in-Zukunft Inkonsistenz, nicht eindeutig 24.06.
- Alpaca IEX 1Day-Bar 24.06.: Close 733,32 = -0,041 % vs 733,62 → wird als Source of Truth verwendet (konsistent mit Vortagen).

**V1–V6 Signal-Check Close (alle SICHER):**
```
Symbol | Close    | Entry   | P/L %   | V1 Stop | Puffer  | change_today | V5 EMA50/EMA200      | V6 RSI / RS_4w   | Status
JPM    | 334,48   | 332,78  | +0,51 % | 306,16  | +9,25 % |  +0,10 %     | ~311,3 > ~301,4 ✓    | ~66 / +9,9 %     | SICHER
UNH    | 406,00   | 401,57  | +1,10 % | 369,44  | +9,89 % |  -0,79 %     | ~375,1 > ~332,8 ✓    | ~61 / +6,5 %     | SICHER
AVGO   | 383,50   | 403,41  | -4,94 % | 371,14  | +3,33 % |  +0,88 %     | ~397,7 > ~355,8 ✓    | ~45 / ~-6 %      | WATCH
```
→ KEINE Verkaufsorder für 25.06. EMA50>EMA200 für alle 3 weiter intakt. AVGO V1-Puffer enger als am Open (+4,02 → +3,33 %), aber besser als 23.06.-Close (+2,42 %).

**Watchlist Scan K1–K5 (Close 24.06., Alpaca IEX-Bars, K5 Perplexity-Carry-over):**
```
Symbol | Close 24.06 | RS_63d vs SPY | Vol/Avg20         | K1 K2 K3 K4 | K5 | Score
CAT    |   994,18    | ~+29 %        | 136,8k/~120k=114 %| ✓ ✓ ✓ ✓-grenz | ✗ FAIL (FwdPE 38,87/42,19) | 4/5
LLY    | 1.117,35    |  ~+10 %       | 111,7k/~141k=79 % | ✓ ✓ ✓ ✗     | ✓ grenzwertig (FwdPE 34,91) | 3/5
CRWD   |   672,72    | ~+50 %        |  37,7k/~144k=26 % | ✓ ✓ ✓ ✗     | vermutlich FAIL (Cloud-SaaS >35) | 3/5
ANET   |   161,87    |  ~+7 %        | 250,7k/~400k=63 % | ✓ ✓ ✓ ✗     | ✗ FAIL (FwdPE 44,13) | 3/5
```

**Auswahl Watchlist 25.06.:**
- CAT bleibt **Lead-Kandidat** (K1–K4 ✓, einziger Vol-Trigger >100 %, K5 weiter blockierend — Perplexity-Recheck am Mo-Open).
- LLY: K4 Vol auf Trend-Trigger >120 % warten (heute 79 %).
- CRWD: K4 sehr schwach (26 %) — vermutlich kein Setup bis nächste Woche.
- ANET: K5 FAIL bleibt — strukturell ausgesondert für KW26.

→ Slot KW26 (1/2) bleibt offen für 25.06. (Do). Kauf nur bei vollem K1–K5.

**Markt-Kontext:**
- SPY -0,04 % praktisch flat — Konsolidierung nach -1,43 % Di und +0,35 % intraday Mi
- VIXY -0,7 % → Spot ~21,6 (weiter entspannt, ~25 % unter dem 30er-Filterniveau)
- Risk-on/Risk-off neutral; Erholung von AVGO setzt sich verhalten fort

**Entscheidung Close:**
- KEIN Verkauf (alle V1–V6 GRÜN, AVGO im Watch aber Puffer ausreichend).
- KEINE Verkaufsorder für 25.06. vorzubereiten.
- KEIN Kauf (kein Kandidat mit allen K1–K5 ✓).
- Watchlist 25.06.: CAT (K5 Watch), LLY (K4 Vol-Trigger).
- Weekly Loss Cap NICHT ausgelöst → kein Sperrauslöser bis Mo.

**Datenquellen:**
- Alpaca /v2/account, /v2/positions, /v2/orders, /v2/clock (16:04 ET) — `is_open=false`
- Alpaca Market Data IEX-Feed: 1Day-Bars für SPY/VIXY/CAT/LLY/CRWD/ANET sowie Positionen.
- Perplexity SPY-Tagesperformance (inkonsistent, nicht als Truth verwendet).
- K5-Fundamentals: Carry-over Verifizierung vom 23.06.

---

## Market Open 09:33 ET — 2026-06-24 (Mi, KW26) — KEIN KAUF

**Guardrail-Check (alle GRÜN):**
- Daily P/L +0,144 % (equity 99.936,82 / last 99.792,95) [GRÜN — Limit -3 %]
- Weekly P/L -0,0258 % (vs Mo-Basis 99.962,66) [GRÜN — Limit -5 %]
- Drawdown vom ATH 100.066,47: -0,130 % [GRÜN — Alarm -15 %]
- VIX-Proxy VIXY 22,80 → Spot ~21,8 < 30 [GRÜN; <25 → 10 % Sizing erlaubt]
- Crash-Filter NEIN (SPY 736,17 = +0,35 % vs Close 23.06. 733,62)
- Cash 82,56 % > 20 % Mindestreserve
- Käufe KW26: 1/2 → 1 Slot frei

**Positionen Live (Alpaca 09:33 ET), V1–V6 Signal-Check:**
```
Symbol | Last     | Entry   | P/L %   | V1 Stop | Puffer  | change_today | V5 EMA50/EMA200    | V6 RSI / RS_4w   | Status
JPM    | 333,69   | 332,78  | +0,27 % | 306,16  | +9,00 % |  -0,14 %     | 310,36 > 301,07 ✓  | 67,53 / +10,45 % | SICHER
UNH    | 411,15   | 401,57  | +2,39 % | 369,44  | +11,28% |  +0,46 %     | 373,84 > 332,04 ✓  | 64,84 / +7,40 %  | SICHER
AVGO   | 386,05   | 403,41  | -4,30 % | 371,14  | +4,02 % |  +1,55 %     | 398,25 > 355,49 ✓  | 43,61 / -6,68 %  | ENTSPANNT (Erholung)
```
→ Alle V1–V6 NICHT ausgelöst. AVGO V1-Puffer hat sich von +2,42 % (Close 23.06.) auf +4,02 % verbessert (intraday +1,55 %).
→ Kein Eingriff (regelbasiert: Stop läuft automatisch bei ≤ 371,14 $).

**Kandidaten-Scan (Watchlist KW26, K1–K4 via Alpaca-Bars bis Close 23.06., K5 carry-over verifiziert 23.06.):**
```
Symbol | Close 23.06 | EMA50/EMA200    | RSI(14) | RS_63d vs SPY | Vol/Avg20 | K1 K2 K3 K4 | K5
CAT    |   984,48    |  879,1 / 687,1  |  61,4   | +28,34 %      |  175 % (196k/112k)| ✓ ✓ ✓ ✓ | ✗ FAIL (FwdPE 38,87/42,19 > 35)
LLY    | 1.107,83    | 1049,3 / 944,3  |  56,0   |  +9,66 %      |   96 % (134k/141k)| ✓ ✓ ✓ ✗ | ✓ grenzwertig (FwdPE 34,91)
CRWD   |   680,57    |  601,5 / 509,2  |  56,8   | +52,49 %      |   48 % (68k/144k) | ✓ ✓ ✓ ✗ | vermutlich FAIL (Cloud-SaaS >35)
ANET   |   162,20    |  156,4 / 140,8  |  51,2   |  +7,09 %      |   82 % (328k/400k)| ✓ ✓ ✓ ✗ | ✗ FAIL (FwdPE 44,13)
```

**Auswahl:**
- CAT: K1–K4 ✓ (Vol stark 175 %, RS +28,34 %), aber K5 FwdPE bleibt >35 carry-over verifiziert → FAIL.
- LLY/CRWD/ANET: K4 Volumen unter 120 % Schwelle → FAIL (CRWD besonders schwach mit 48 %).
- → **KEIN Kandidat erfüllt alle 5 Kaufsignale** → Kauf-Slot bleibt ungenutzt für 24.06.

**Markt-Kontext (Risk-on Erholung):**
- SPY 736,17 = +0,35 % intraday (Pre-Market +0,41 % bestätigt sich)
- VIXY 22,80 (-0,87 % vs Close 23,00) → VIX Spot ~21,8 (entspannt)
- AVGO Erholung +1,55 % intraday — V1-Stop-Druck nachgelassen.

**Entscheidung Market-Open:**
- KEIN Buy (kein Kandidat mit allen K1–K5 ✓).
- KEIN Sell (V1–V6 für alle 3 Positionen NICHT ausgelöst).
- Priorität bis 13:00 Midday-Check: AVGO weiter beobachten (V1 371,14 $ Stop läuft automatisch), aber Erholung gibt Atemraum.
- 1 Slot KW26 bleibt für Do/Fr.

**Datenquellen:**
- Alpaca /v2/account, /v2/positions, /v2/orders, /v2/clock (09:32 ET) — `is_open=true`
- Alpaca Market Data IEX-Feed: SPY/VIXY latest trades + 200-Tage-Bars für Watchlist (CAT/LLY/CRWD/ANET).
- K5-Fundamentals carry-over aus Close 23.06. (Perplexity-Verifizierung von gestern bleibt aktuell — keine Earnings/Guidance heute).

---

## Pre-Market 08:30 ET — 2026-06-24 (Mi, KW26)

**Marktdaten:**
- VIX Spot ~19,32 (Carry-over Perplexity); Close 23.06. 19,49 → <25 → 10 % Sizing erlaubt, kein VIX-Filter
- SPY Pre-Market 736,625 $ Mid (Alpaca Quote 08:33 ET, bid 736,54 / ask 736,71) → +0,41 % vs Close 23.06. 733,62 $ [GRÜN, nicht <-2 %]
- 10Y Treasury Yield: via Perplexity nicht verfügbar (Datum-in-Zukunft-Restriktion)
- Crash-Filter: NEIN (SPY 23.06. -1,431 % > -5 %)

**Alpaca-Account (Pre-Market 08:32 ET):**
- equity 99.844,39 $ | cash 82.505,98 $ | last_equity 99.792,95 $
- Daily P/L: +0,0515 % [GRÜN — Limit -3 %]
- Weekly P/L: -0,118 % vs Mo-Basis 99.962,66 $ [GRÜN — Limit -5 %]
- DD vom ATH 100.066,47 $: -0,222 % [GRÜN]
- Reconciliation portfolio.md Close 23.06. 99.782,07 $ vs Alpaca last_equity 99.792,95 $ → Diff +10,88 $ Settlement-Tick (After-Hours Mark-to-Market), OK
- Käufe KW26: 1/2 (1 Slot frei für Mi/Do/Fr) | Pending Orders: 0

**Positionen Live (Alpaca 08:32 ET):**
```
Symbol | Last     | Entry   | P/L %   | V1 Stop | Puffer  | change_today | Status
JPM    | 334,40   | 332,78  | +0,49 % | 306,16  | +9,22 % |  +0,08 %     | SICHER
UNH    | 410,10   | 401,57  | +2,12 % | 369,44  | +11,01% |  +0,21 %     | SICHER
AVGO   | 381,93   | 403,41  | -5,33 % | 371,14  | +2,90 % |  +0,47 %     | KRITISCH (V1-nah)
```

**Earnings-Blackout-Check (nächste 3 HT, Perplexity verifiziert):**
- JPM: 14.07.2026 (20 Tage entfernt) → kein Blackout
- UNH: 16.07.2026 (22 Tage entfernt) → kein Blackout
- AVGO: 29.08.2026 (66 Tage entfernt) → kein Blackout
- → KEIN Stop-Tightening nötig.

**Guardrails-Status (alle GRÜN):**
- Daily Loss Cap -3 %: NEIN (+0,05 %)
- Weekly Loss Cap -5 %: NEIN (-0,12 %)
- Drawdown-Alarm -15 %: NEIN (-0,22 %)
- Drawdown-Stopp -20 %: NEIN
- Crash-Filter SPY -5 %: NEIN (gestern -1,43 %)
- VIX-Filter >30: NEIN (~19,3 — sogar <25 → 10 % Sizing)
- Käufe-Limit 2/Wo: 1/2 (1 Slot frei)

**Makro-Events 24.06. (Perplexity):** Keine spezifischen Fed-Reden/Wirtschaftsdaten als bestätigt verfügbar. News-Tenor: Goldman Sachs Risiko-Warnung trotz Rekord-ETF-Inflows (Short-Covering-getrieben); VIX am unteren Trendkanal — Hinweis auf dünnes Sicherheitsnetz.

**Entscheidung Pre-Market:**
- Market-Open-Scan 09:30 ET: **JA** — alle Guardrails GRÜN, SPY Pre-Market positiv (+0,41 %), VIX <25.
- Priorität: AVGO-Stop-Watch (V1-Puffer nur +2,90 %, change_today +0,47 % → leichte Erholung Pre-Market; automatisch bei Last ≤ 371,14 $).
- Watchlist KW26 (1 Slot frei): CAT (K4 stark, K5 FwdPE >35 Block), LLY (Vol-Trigger-Watch), CRWD (Vol-Trigger-Watch), ANET (K5 FAIL FwdPE 44,13).
- Kauf nur bei sehr starkem Setup (alle K1–K5 ✓).

---

## Market Close 16:00 ET — 2026-06-23 (Di, KW26)

**Tagesperformance:**
- Depot: 99.782,07 $ (Close) vs. last_equity 99.926,95 → -144,88 $ / -0,145 % [GRÜN]
- SPY: 744,27 (Mo-Close 22.06.) → 733,62 (Di-Close 23.06.) = -1,431 % (Alpaca IEX, da SIP Restriktion)
- Alpha: +1,286 % [POSITIV — Cash-Quote 82,69 % federt Marktverlust deutlich ab]
- ATH: 100.066,47 $ (intraday 22.06., unverändert); DD -0,284 % [GRÜN]
- VIX-Proxy (VIXY ETF): 23,00 (+5,3 % vs Vortag 21,84) — Spot ~22 (GRÜN <30, knapp unter 25-Sizing-Schwelle)

**Positions-Signal-Check Close (V1–V6):**
```
Symbol | Close      | P/L %   | V1 Puffer  | V5 EMA50/EMA200    | V6 RSI / RS_4w
JPM    | 334,185 $  | +0,41 % | +9,16 %    | 310,36 > 301,07 ✓  | 67,53 / +10,45 %
UNH    | 409,65 $   | +1,91 % | +10,88 %   | 373,84 > 332,04 ✓  | 64,84 / +7,40 %
AVGO   | 380,13 $   | -5,77 % | +2,42 %    | 398,25 > 355,49 ✓  | 43,61 / -6,68 %  [KRITISCH V1]
```
→ Alle V1–V6 SICHER. Keine Verkaufsorder pending.
→ AVGO bleibt im KRITISCH-Status: V1-Puffer nur +2,42 %, RS_4w weiter negativ. EMA-Spread aber komfortabel (+42,76). Bei Open 24.06. ≤ 371,14 $ → V1-Market-Order automatisch.

**Watchlist 24.06. (K1–K4 via Alpaca IEX-Bars bis Close 23.06., K5 via Perplexity verifiziert):**
```
Symbol | Sektor | Close       | EMA50/EMA200       | RSI(14) | RS_63d   | Vol/Avg20 | K1 K2 K3 K4 | K5
LLY    | XLV    | 1.107,83    | 1049,3 / 944,3     | 56,0    | +9,66 %  |  96 %     | ✓ ✓ ✓ ✗     | ✓ grenzwertig (FwdPE 34,91)
ANET   | XLK    |   162,20    |  156,4 / 140,8     | 51,2    | +7,09 %  |  84 %     | ✓ ✓ ✓ ✗     | ✗ FAIL (FwdPE 44,13 bestätigt)
CRWD   | XLK    |   680,57    |  601,5 / 509,2     | 56,8    | +52,49 % |  56 %     | ✓ ✓ ✓ ✗     | offen (Cloud-SaaS typ. >35)
CAT    | XLI    |   984,48    |  879,1 / 687,1     | 61,4    | +28,34 % | 175 %     | ✓ ✓ ✓ ✓     | ✗ FAIL (FwdPE 38,87 Stock Analysis / 42,19 Yahoo — beide > 35 bestätigt)
GOOGL  | XLC    |   346,25    |  360,9 / 304,4     | 37,4    |  +2,44 % | 106 %     | ✓ ✗ ✓ ✗     | n/a (K2 fail)
NVDA   | XLK    |   200,07    |  206,6 / 189,5     | 42,5    |  +1,84 % |  78 %     | ✓ ✗ ✓ ✗     | n/a (FwdPE >35)
META   | XLC    |   562,42    |  605,4 / 647,8     | 39,2    | -19,07 % |  71 %     | ✗ ✗ ✗ ✗     | —
COST   | XLP    |   957,34    |  989,3 / 973,7     | 40,5    | -12,96 % |  84 %     | ✓ ✗ ✗ ✗     | —
NFLX   | XLC    |    72,77    |   85,6 /  99,0     | 21,0    | -34,31 % | 124 %     | ✗ ✗ ✗ ✓     | — (Stock-Split Spuren? — separater Check)
```
→ **KEIN Kandidat erfüllt alle 5 Kaufsignale.** Slot KW26 (1/2 frei) bleibt ungenutzt für 24.06.
→ Empfohlene Beobachtung: CAT (FwdPE-Druck — Q2-Earnings könnten Bewertung normalisieren), LLY (Vol-Pickup-Watch), CRWD (Vol-Pickup-Watch).

**Sektor-Status (nach Close 23.06.):**
- XLF (JPM): 1.002 $ → 5,80 % invest. / 1,00 % Gesamt   [OK 1/3]
- XLV (UNH): 9.822 $ → 56,86 % invest. / 9,84 % Gesamt  [OK 1/3]
- XLK (AVGO): 6.452 $ → 37,35 % invest. / 6,47 % Gesamt [OK 1/3, kein Verstoß <30 % Gesamt-Limit]

**Weekly Loss Cap geprüft:**
- weekly_pnl_pct = (99.782,07 - 99.962,66) / 99.962,66 = -0,181 %
- Schwelle -5 % → Puffer ~4.819 $ → KEIN Auslöser. Keine pending Orders zum Stornieren.
- Käufe KW26: 1/2 → 1 Slot frei für Mi/Do/Fr.

**Datenquellen:**
- Alpaca /v2/account, /v2/positions, /v2/orders, /v2/clock (16:04 ET)
- Alpaca Market Data IEX-Feed (SIP gesperrt für Realtime): 277 daily bars start 2025-05-15.
- VIX-Proxy via VIXY-ETF (kein Cboe-Spot via Alpaca, Perplexity-Realtime nicht verfügbar).
- Perplexity sonar: Tagesdaten 23.06.2026 NICHT abrufbar (Datum "in Zukunft" laut Perplexity-Hinweis) — komplett Alpaca-Daten als Quelle of Truth. K5-FwdPE für CAT/ANET via Perplexity (historische Snapshots Yahoo/StockAnalysis).

**Entscheidung Close:**
- KEINE Verkaufsorder für 24.06. vorbereitet (V1–V6 alle SICHER).
- KEIN Kauf-Setup für 24.06. (kein K1–K5-Kandidat).
- AVGO bleibt Top-Priorität für Pre-Market/Open 24.06.: bei ≤ 371,14 $ wird V1-Market-Order automatisch ausgelöst.
- Nächste Routine: Pre-Market 24.06. 08:30 ET.

---

## Market Open 09:33 ET — 2026-06-23 (Di, KW26) — KEIN KAUF

**Guardrail-Check (alle GRÜN):**
- Daily P/L -0,216 % (equity 99.710,67 / last 99.926,95) [GRÜN — Limit -3 %]
- Weekly P/L -0,252 % (vs Mo-Basis 99.962,66) [GRÜN — Limit -5 %]
- Drawdown vom ATH 100.066,47: -0,356 % [GRÜN — Alarm -15 %]
- VIX ~19,81 (PreMarket Carry-over) < 30 [GRÜN; <25 → 10 % Sizing erlaubt]
- Crash-Filter NEIN (SPY 732,63 intraday vs Mo-Close 744,27 = -1,57 % > -5 %)
- Cash 82,75 % > 20 % Mindestreserve
- Käufe KW26: 1/2 → 1 Slot frei

**Positionen Live (Alpaca 09:33 ET), V1–V6 Signal-Check:**
```
Symbol | Last     | Entry   | P/L %   | V1 Stop | Puffer  | V5 EMA50/EMA200    | V6 RSI / RS_63d  | Status
JPM    | 327,75   | 332,78  | -1,45 % | 306,16  | +7,05 % | 309,56 > 304,91 ✓  | 65,65 / +0,90 %  | SICHER
UNH    | 405,29   | 401,57  | +0,93 % | 369,44  | +9,71 % | 374,21 > 329,25 ✓  | 63,26 / +32,79 % | SICHER
AVGO   | 382,06   | 403,41  | -5,30 % | 371,14  | +2,94 % | 399,69 > 362,55 ✓  | 46,42 / +11,51 % | KRITISCH
```
→ Alle V1–V6 NICHT ausgelöst, aber AVGO mit +2,94 % Puffer hauchdünn vor V1-Market-Order.
→ Kein Eingriff (regelbasiert: Stop läuft automatisch bei ≤ 371,14 $).

**Kandidaten-Scan (Watchlist KW26, K1–K4 via Alpaca-Bars bis Mo 22.06.):**
```
Symbol | Close 22.06 | EMA50/EMA200    | RSI(14) | RS_63d vs SPY | Vol/Avg20 | K1 K2 K3 K4 | K5
LLY    | 1.102,08    | 1047,76 / 962,91|  54,35  |  +6,77 %      |   92,3 %  | ✓ ✓ ✓ ✗     | ✓ grenzwertig (FwdPE 34,91)
ANET   |   174,56    |  156,14 / 144,96|  62,54  | +18,25 %      |  108,9 %  | ✓ ✓ ✓ ✗     | offen
CRWD   |   675,44    |  598,27 / 502,75|  56,58  | +50,37 %      |   95,0 %  | ✓ ✓ ✓ ✗     | offen (Cloud-SaaS typ. FwdPE > 35)
CAT    | 1.022,28    |  875,14 / 708,72|  69,59  | +35,37 %      |  136,0 %  | ✓ ✓ ✓ ✓     | ✗ FAIL (FwdPE 38,87 carry-over)
```
SPY 63d Return: +14,77 % (Baseline für RS).

**Auswahl:**
- LLY/ANET/CRWD: K4 < 120 % (Mo-Bar) → FAIL.
- CAT: K1–K4 ✓, RS am stärksten (+35,37 %), aber K5 historisch FAIL (FwdPE 38,87 > 35 lt. letztem Research).
- → **KEIN Kandidat erfüllt alle 5 Kaufsignale** → Kauf-Slot bleibt ungenutzt.

**Markt-Kontext (Risk-off bestätigt):**
- SPY 732,63 = -1,57 % intraday (PreMarket-Warnung -1,40 % bestätigt sich)
- VIX im Anstieg (Carry-over 19,81; weiter beobachten Midday)
- AVGO knapp über V1-Stop — voller Fokus auf Stop-Watch.

**Entscheidung Market-Open:**
- KEIN Buy (PreMarket-Bedingung "nur bei sehr starkem Setup" nicht erfüllt).
- KEIN Sell (V1–V6 für alle 3 Positionen NICHT ausgelöst).
- Priorität bis 13:00 Midday-Check: AVGO ≤ 371,14 $ löst V1-Market-Order aus (kein manueller Eingriff).
- 1 Slot KW26 bleibt für Mi/Do/Fr.

**Datenquellen:**
- Alpaca /v2/account, /v2/positions, /v2/orders, /v2/clock (09:33 ET)
- Alpaca Market Data SIP-Feed: latest trades + 274 daily bars (start 2025-05-19 → 2026-06-22).
- Perplexity-Sektorabfrage übersprungen (Watchlist aus PreMarket bereits aktuell, K5-Status carry-over).

---

## Pre-Market 08:30 ET — 2026-06-23 (Di, KW26)

**Konto-Snapshot (Alpaca):**
```
Gesamtwert (equity):   99.660,80 $   (last_equity 99.926,95 → Daily P/L -0,266 % [GRÜN])
Cash:                  82.505,98 $   (82,79 %)
Investiert (MV):       17.155,39 $   (17,21 %) — JPM 993,00 | UNH 9.782,40 | AVGO 6.379,99
ATH:                  100.066,47 $   (intraday 22.06.) | DD -0,406 % [GRÜN]
```
> Hinweis: Reconciliation-Differenz zu portfolio.md 22.06. Close-Snapshot (99.935,22 → 99.926,95) = -8,27 $. Vermutlich Settlement-Tick. Alpaca-Wert ist Quelle of Truth.

**Markt-Daten (Perplexity sonar):**
- VIX Spot: **19,81** (steigend von ~16,8 Vortag) [GRÜN — Filter bei 30]
- SPY Pre-Market: **733,98 $** = **-1,40 %** vs. Mo-Close 744,27 [GRÜN — Vorsichtsschwelle -2 %, nicht überschritten]
- 10Y Treasury Yield: **4,488 %** (steigend von 4,46 % Vortag → leicht risk-off)
- Makro-Events heute: KEINE wesentlichen US-Releases / Fed-Speaker / FOMC.
- Top-News: Perplexity-Ergebnisse hier dünn (keine spezifischen Headlines geliefert).

**Positionen Live (Alpaca current_price 08:30 ET):**
```
Symbol | Last     | Entry   | P/L %   | V1 Stop  | Puffer
JPM    | 331,00 $ | 332,78  | -0,54 % | 306,16 $ | +8,11 %  [SICHER]
UNH    | 407,60 $ | 401,57  | +1,50 % | 369,44 $ | +10,32 % [SICHER]
AVGO   | 375,29 $ | 403,41  | -6,97 % | 371,14 $ | +1,12 %  [KRITISCH — knapp über Stop]
```
→ **AVGO-Warnung:** Premarket -4,29 % vs. Vortags-Close. Bei weiterem Rutschen -1,1 % im Market Open wird V1 ausgelöst → Market-Order Verkauf. Stop ist hart, kein Eingriff.

**Guardrail-Check (alle GRÜN):**
- Daily P/L -0,266 % [GRÜN — Limit -3 %]
- Weekly P/L -0,302 % (vs. Mo-Basis 99.962,66) [GRÜN — Limit -5 %]
- Drawdown vom ATH -0,406 % [GRÜN — Alarm -15 %]
- VIX 19,81 < 30 [GRÜN]
- SPY Pre-Market -1,40 % > -2 % [GRÜN, aber Risk-off-Tendenz]
- Crash-Filter NEIN (gestern -0,331 % < |-5 %|)
- Käufe KW26: 1/2 (AVGO 22.06.) → 1 Slot frei

**Earnings-Blackouts (Perplexity):**
- JPM 14.07.26 (21 Tage), UNH 16.07.26 (23 Tage), AVGO 03.09.26 (72 Tage) → KEINE Blackouts in nächsten 3 Handelstagen, kein Stop-Tightening nötig.

**Entscheidung Market-Open-Scan 09:30 ET:**
- **Scan: JA**, aber **Kauf nur bei sehr starkem Setup** (SPY -1,40 % Premarket + VIX-Anstieg + AVGO im Drawdown → erhöhte Vorsicht).
- **Priorität:** AVGO-Beobachtung — bei V1-Trigger (≤ 371,14 $) Market-Order Verkauf 17 Sh.
- **Watchlist:** LLY (XLV K1–K5 ✓ grenzwertig), ANET (XLK K1–K3 ✓), CRWD (XLK K1–K3 ✓ — K5 prüfen), CAT (XLI K5-FwdPE verifizieren).
- **Sektor-Hinweis:** XLK-Slot bereits AVGO; LLY würde 2. XLV nach UNH (OK ≤ 3). XLF (JPM) bereits belegt.

---

## Market Close 16:00 ET — 2026-06-22 (Mo, KW26)

**Tagesperformance:**
- Depot: 99.935,22 $ (Close) vs. last_equity 99.962,66 → -27,44 $ / -0,0275% [GRÜN]
- SPY: 746,74 (Do-Close 18.06.) → 744,27 (Mo-Close 22.06.) = -0,331% (Fr 19.06. Juneteenth Holiday)
- Alpha: +0,304% [POSITIV — Cash-Quote 82,56% federt AVGO-Drawdown ab]
- ATH: 100.066,47 $ (intraday-Open 22.06. 09:37 ET, unverändert); DD -0,131% [GRÜN]

**Positions-Signal-Check Close (V1–V6):**
```
Symbol | Close      | P/L%   | V1 Puffer  | V5 EMA50/EMA200    | V6 RSI / RS_4w
JPM    | 331,9175 $ | -0,26% | +8,42%     | 309,57>307,40 ✓    | 66,15 / +9,34%
UNH    | 406,07 $   | +1,12% | +9,92%     | 374,21>334,49 ✓    | 61,90 / +5,96%
AVGO   | 393,40 $   | -2,48% | +6,00%     | 399,74>358,71 ✓    | 46,63 / -5,32%
```
→ Alle V1–V6 SICHER. Keine Verkaufsorder pending.
→ Beobachtung AVGO: intraday -4,36%, RS_4w bereits negativ, EMA-Spread schmaler. Bei weiterem Abrutschen Di-Close intensiv prüfen.

**Watchlist Di 23.06. (K1–K3 via Alpaca SIP, K5 vorerst Carry-over):**
```
Symbol | Sektor | EMA50/EMA200       | RSI(14) | RS63d vs SPY | Vol/Avg20 | K-Status
LLY    | XLV    | 1045,03 / 958,75   | 53,98   |  +6,56%      | 138%      | K1–K5 ✓ grenzwertig (FwdPE 34,91)
ANET   | XLK    | 155,43 / 143,35    | 58,87   | +11,34%      | 128%      | K1–K3 ✓ (K4/K5 Open prüfen)
CRWD   | XLK    | 595,05 / 502,96    | 58,21   | +46,77%      | 146%      | K1–K3 ✓ (K5 FwdPE prüfen, Cloud-SaaS typ. >35)
CAT    | XLI    |  869,02 / 684,12   | 65,42   | +29,98%      | 205%      | K1–K4 ✓ (K5 alt FwdPE 38,87 — verifizieren)
```
→ Notiz: NVDA/AMD bleiben K5-FAIL (FwdPE>35 bzw. >67). Konflikt-Checks bei Auswahl: AVGO bereits XLK (Slot frei für 2. XLK), UNH bereits XLV (LLY würde 2. XLV; OK bis 3 Pos/Sektor), JPM bereits XLF (kein neuer Kandidat XLF).
→ Slot KW26: 1/2 verbraucht (AVGO) → 1 weiterer Kauf erlaubt. Falls AVGO morgen weiter abrutscht & V1 droht, ggf. Kaufzurückhaltung.

**Weekly Loss Cap geprüft:**
- weekly_pnl_pct = (99.935,22 - 99.962,66) / 99.962,66 = -0,0275%
- Schwelle -5% (entsprechend 94.964,53 $) → Puffer ~4.971 $. KEIN Auslöser.

**Datenquellen:**
- Alpaca /v2/account, /v2/positions, /v2/orders (Close 16:04 ET)
- Alpaca Market Data SIP-Feed für historische Bars bis 18.06. + IEX für SPY 22.06.
- Perplexity sonar: SPY Close-Quote leicht inkonsistent (lieferte Vortageswert) — Alpaca-Daten als Quelle of Truth verwendet.
- VIX nicht live abgefragt am Close (Carry-over ~16,8 vom Pre-Market).

---

## Market Open 09:30 ET — 2026-06-22 (Mo, KW26)

**Guardrails-Check (alle GRÜN):**
- Daily P/L +0,10 % (100.066 / 99.962) [GRÜN] | Weekly +0,07 % [GRÜN]
- Käufe KW26: 0 / 2 (Reset von Mo erfolgt) → Kauf erlaubt
- VIX Spot ~16,8 (<25 → 10 % Sizing) | Crash-Filter NEIN | DD GRÜN | Cash 89,4 % >> 20 % Mindestreserve

**Kandidaten-Scan (Watchlist KW26 + Live K1–K4 via Alpaca Bars 219d):**
```
Symbol | Close 18.06. | EMA50 / EMA200 | RSI(14) | RS_63d vs SPY | Vol/Avg20 | K1 K2 K3 K4
AVGO   | 411,35       | 400,00 / 360,25| 51,33   | +15,43%       | 130%      |  ✓  ✓  ✓  ✓
CAT    |  985,82      | 869,01 / 673,71| 65,45   | +29,98%       | 219%      |  ✓  ✓  ✓  ✓
LLY    | 1098,57      | 1045,03/ 958,75| 53,98   |  +6,56%       | 138%      |  ✓  ✓  ✓  ✓
```

**K5 Fundamentals (Perplexity sonar):**
```
AVGO  FwdPE 34,0 / 34,2 / 35,6 (3 Quellen, Median 34,2)  RevYoY +51,47%  Earnings 03.09.26  → K5 ✓
CAT   FwdPE 38,87   RevYoY +10,35%  Earnings 06.08.26                    → K5 FAIL (FwdPE > 35)
LLY   FwdPE 34,91   RevYoY +45,28%  Earnings 07.08.26                    → K5 ✓ (grenzwertig)
```

**Best-Kandidaten-Auswahl (K1–K5 ✓ + höchste RS):**
- CAT raus (K5 fail trotz höchster RS +29,98%).
- AVGO RS +15,43% **>** LLY RS +6,56% → **AVGO = Buy-Pick**.
- LLY zusätzlich XLV-Konflikt mit UNH (akzeptabel: 2/3 Pos., 19,7 % Gesamtdepot) — aber RS schwächer, Pick AVGO eindeutig.

**Order AVGO:**
- Position-Sizing: 100.066 $ × 10 % = 10.007 $ Budget
- Limit $413,41 (= 411,35 × 1,005), 24 Shares (= floor(10.007 / 413,41))
- Fill: 17 / 24 Shares @ $403,41 avg (09:36 ET), Rest 7 nach 2 Min steckend → manuell canceled.
- Investiert effektiv 6.857,97 $ (~6,85 % Portfolio statt 10 % wegen Partial).
- Stop V1 $371,14 (-8 %) | TP1 V3 $484,09 (+20 %) | TP2 V4 $544,61 (+35 %).
- Alpaca Order-ID: ab4a9c16 | ClickUp Task: 869duc9ne (Prio 3).

**Live Signal-Check Positionen 09:37 ET (V1–V6):**
- JPM 327,76 $ (+0,78 % intraday): V1 / V2 SICHER | V3 / V4 nicht erreicht.
- UNH 406,09 $ (+1,28 % intraday): V1 / V2 SICHER | V3 / V4 nicht erreicht.
- AVGO 402,03 $ (-2,27 % vs Vortag, -0,34 % vs Entry): V1 / V2 SICHER | V3 / V4 nicht erreicht.
- Keine Verkaufsorder offen.

**Sektor-Check nach Kauf:**
- XLF (JPM): 983 $ → 0,98 % Gesamtdepot / 5,60 % invest.
- XLV (UNH): 9.746 $ → 9,74 % Gesamtdepot / 55,50 % invest.
- XLK (AVGO): 6.834 $ → 6,83 % Gesamtdepot / 38,91 % invest.
- Diversifikation: 3 Sektoren, max. 9,74 % je Sektor auf Gesamtbasis (<< 30 %-Limit). KEIN VERSTOSS.

**Carry-over Watchlist nächste Tage:**
- LLY (XLV) — K1–K5 ✓ grenzwertig, RS schwächer, Slot 2/2 KW26 frei.
- CAT (XLI) — K5-Beobachtung; Perplexity-FwdPE 38,87 könnte mit anderer Quelle ≤ 35 sein → vorm nächsten Scan Quellen verifizieren.
- NVDA / AMD bleiben K5-FAIL (FwdPE > 35 / > 67).

---

## Pre-Market 08:30 ET — 2026-06-22 (Mo, KW26)

VIX: 16,78 (Fr Close) → ~17,4 (Spot Pre-Market, +4 %) | SPY Pre-Market: 747,80 $ Mid (+0,14 % vs Fr 746,74) | Treasury 10Y: n/a (Perplexity Realtime unzureichend)
Guardrails: Daily -0,003 % GRÜN | Weekly Reset (neue Woche) GRÜN | DD -0,053 % GRÜN | VIX-Filter NEIN (<25) | Crash-Filter NEIN (SPY Fr +0,77 %) | Käufe diese Woche 0/2
Earnings-Blackouts: keine in 22.–24.06. — S&P-500 Earnings-Kalender leer; JPM 14.07., UNH 16.07. weit entfernt (kein Stop-Tightening).
Makro-Events heute: US-Datenkalender leicht (Perplexity meldet keine harten US-Releases / Fed-Reden bestätigt für heute) — Wochenfokus: Mi PMI, Fr PCE-Inflation.
Entscheidung: Kaufscan bei Market Open JA. Watchlist KW26 (Carry-over): AVGO (Top-Pick, XLK), CAT (XLI, Vol-Trigger-Watch), LLY (XLV-Konflikt UNH beachten).

---

## Weekly Review 17:00 ET — 2026-06-19 (KW25, Juneteenth Holiday)

### Wochenperformance
```
Depot Mo 15.06.:     100.000,00 $
Depot Fr 19.06.:      99.962,66 $   (= last_equity 18.06., Holiday)
Wochenrendite Depot:    -0,037 %

SPY Mo 15.06. Close:    754,31 $
SPY Do 18.06. Close:    746,74 $    (Fr Holiday, kein Close)
SPY Wochenrendite:      -1,003 %

Alpha diese Woche:      +0,966 %    [POSITIV — Cash-Quote 89 % hat Drawdown gepuffert]

"YTD" Depot (Init 31.05.): -0,037 %  (Bot lebt erst 19 Tage)
SPY YTD 2026:           +10,09 %    (31.12.25 678,32 → 18.06.26 746,74)
YTD-Alpha:              nicht direkt vergleichbar (Init nicht 01.01.)
```

### Trade-Analyse KW25
```
Käufe:           2 (JPM Mi @332,78 / UNH Do @401,57)
Verkäufe:        0
Stop-Loss V1:    0 ausgelöst
Trailing V2:     0 ausgelöst
TP1/V3 +20 %:    0 erreicht
TP2/V4 +35 %:    0 erreicht
Death-Cross V5:  0
RSI-Over V6:     0
Geschlossene Trades:   0
Win-Rate Woche:        n/a
Ø Haltedauer (closed): n/a

Welches Kaufsignal hat funktioniert?
- JPM K1–K5 ✓ → -2,03 % nach 2 Handelstagen (Goldman-Sektor-Warnung Fin/Indust am Do)
- UNH K1–K5 ✓, höchstes RS +28,57 % auf Watchlist → -0,15 % nach 1 Handelstag (intraday +0,12 %, Close knapp negativ)
- Beide Positionen V1–V6 grün, Bewertung nach 1–2 Tagen noch nicht aussagekräftig.
```

### Relative-Stärke / Sektor-Ranking KW25 (Perplexity #4)
Datenlage: Keine harten Wochenrenditen für XLK/XLV/etc. abrufbar; Ranking auf Basis
von Sektor-News und Markt-Kommentaren (Morningstar, JPMorgan, BlackRock, DWS):
```
1. XLK Technology / Semiconductors  — KI-Infrastruktur, Halbleiter weiter dominant
2. XLE Energy / Infrastructure      — Electro Tech, Netzinfrastruktur als Thema
3. XLV Health Care + XLF Financials — Midterm-Thema (Verteidigung/Health/Finanzen),
                                      Evidenz weicher als bei Tech.
```
Carry-over aus 18.06. interne K1–K4-Berechnung: AVGO (XLK) klarer Top-Pick,
CAT (XLI Industrials) mit RS +29,9 % stark, NVDA (XLK) RS +4,7 % aber K4 fail.

### Fundamentals-Screen Top-Sektoren (Perplexity #5)
Datenqualität gemischt — Perplexity konnte Einzel-Forward-P/E + Earnings-Termin
nicht durchgängig liefern. Belastbare Kandidaten:
```
Ticker | Sektor | Fwd P/E      | Rev YoY  | MCap     | Earnings    | K5 | Status
-------|--------|--------------|----------|----------|-------------|----|--------
AVGO   | XLK    | 26,1–35,6*   | +47,9 %  | $1,87 T  | ~Sep 2026   | ✓  | TOP-PICK
NVDA   | XLK    | 43,4         | n/a      | groß     | ~Aug        | ✗  | K5 fail (FwdP/E > 35)
AMD    | XLK    | 67,3         | n/a      | groß     | n/a         | ✗  | K5 fail
LLY    | XLV    | n/a (Quellen)| n/a      | groß     | ~Aug        | ?  | XLV-Konflikt UNH, max 3
MSFT/AAPL/GOOGL              | Daten unzureichend, K2 fail historisch              | beobachten
```
*) Quellen-Spread: stockanalysis 26,13 / Yahoo 32,57 / GuruFocus 35,63 — Median ~32,
   in jedem Fall an der oberen K5-Grenze (≤35). AVGO bleibt aber im Rahmen.

### Sektorgewichtung (Schritt 6)
```
XLF (JPM): 975,66 $ Marktwert
           → 9,21 % vom investierten Kapital
           → 0,98 % vom Gesamtdepot
XLV (UNH): 9.623,04 $ Marktwert
           → 90,79 % vom investierten Kapital  (Skalen-Asymmetrie wg. UNH-Sizing)
           → 9,63 % vom Gesamtdepot
Max-Regeln: 3 Pos./Sektor (beide 1/3) | 30 % Gesamtdepot (max 9,63 %) → KEIN VERSTOSS
Hinweis: Bei Erweiterung des Depots in XLV Vorsicht (1 zusätzliche Pos. = ~20 %).
```

### Watchlist KW26 (Mo 22.06. — Fr 26.06.)
```
AVGO   XLK   Top-Pick, alle K1–K5 ✓ — Buy-Limit nach K1–K4-Live-Check am Mo möglich
CAT    XLI   K1–K3 ✓, K4 fail (Vol 96 %) — auf Vol-Pickup warten
LLY    XLV   K1–K3 ✓, K4 fail; XLV-Konflikt mit UNH (1 weitere XLV-Pos. = OK ≤3)
NVDA   XLK   AUS (K5 FwdP/E 43,4 > 35)
AMD    XLK   AUS (K5 FwdP/E 67,3)
GS     XLF   AUS (Sektor-Konflikt mit JPM, K4 fail)
BAC    XLF   AUS (XLF-Konflikt, RSI hot)
```
Realistisches Buy-Szenario KW26: AVGO als erster Trade, CAT bei Vol-Trigger.

### Strategie-Status
**STABIL — keine Parameter-Anpassung.**
Begründung: Bot lebt erst 19 Kalendertage / 13 Handelstage; Sample-Size für
Regel-Änderungen unzureichend. Positives Alpha (+0,97 %) bestätigt das passive
Cash-Polster-Setup in schwacher Marktwoche.

### ClickUp Weekly Report
```
List-ID Fix (Env): 901218902364 jetzt korrekt gesetzt — Stripping nicht mehr nötig.
Task: [WEEKLY] Review KW25 — 2026-06-19  → siehe nachgelagerter API-Call.
```

---

## Market Close 16:00 ET — 2026-06-19 — HANDELSFEIERTAG (Juneteenth), No-Op

### Markt-Status
```
Alpaca clock: is_open=false (timestamp 16:04 ET)
next_open:    2026-06-22 09:30 ET (Montag)
Begründung:   US-Bundesfeiertag (Juneteenth) — NYSE/Nasdaq ganztägig geschlossen
```

### Tagesperformance (kein Trade-Tick)
```
Alpaca equity Close:   99.962,66 $   (last_equity 99.962,66 → daily 0,00 $ / 0,00 %)
Cash:                  89.363,96 $   (89,4 %)
Investiert:            10.598,70 $   (10,6 %)
ATH:                  100.012,97 $   (Open 18.06.)
Drawdown:              -0,0503 %
SPY-Performance:       n/a (kein Daily-Bar) — Alpha-Berechnung übersprungen
VIX:                   n/a (Markt zu)
```

### Verkaufssignal-Check Close (V1–V6)
```
Live-Check übersprungen — keine neuen Bars. Letzter Stand 18.06. Close (carry-over):
JPM 325,22 $   V1 306,16 SICHER (+6,2 %) | V2 SICHER | V3/V4 nicht erreicht
               V5 EMA50 308,67 > EMA200 307,35 → kein Death Cross
               V6 RSI 62,1 + RS_4w +6,96 % → nicht ausgelöst
UNH 400,96 $   V1 369,44 SICHER (+8,5 %) | V2 SICHER | V3/V4 nicht erreicht
               V5 EMA50 372,91 > EMA200 335,16 → kein Death Cross
               V6 RSI 58,7 + RS_4w +3,95 % → nicht ausgelöst
→ Keine Verkaufsorder für Mo 22.06. vorbereitet.
```

### Weekly Loss Cap
```
weekly_pnl_pct = (99.962,66 - 100.000,00) / 100.000,00 * 100 = -0,037 %   [GRÜN — Limit -5 %]
Käufe diese Woche:  2 / 2 (LIMIT erreicht — JPM 17.06., UNH 18.06.)
Kein pending storno nötig (keine pending Orders).
```

### Watchlist Mo 22.06.2026 (Carry-over aus 18.06. Close)
```
AVGO (Top-Pick, K1–K4 ✓ — Semis XLK)
CAT  (Industrials XLI, RS+30 %, K4 fail beim letzten Check — neu zu prüfen)
NVDA (Semis XLK, K4 fail beim letzten Check — neu zu prüfen)
LLY  (Health XLV — UNH bereits gehalten, max 3 pro Sektor beachten)
GS   (Financials XLF — SEKTORKONFLIKT mit JPM, K4 fail)
```
→ Keine Perplexity-Abfrage durchgeführt (Holiday, keine neuen Sektor-News).
→ K1–K3 Vorprüfung am Pre-Market Mo 22.06. mit dann frischen Daten.

### ClickUp-Report
```
Übersprungen: Pre-Market hat Holiday-Notification (Task 869dtg866) bereits abgesetzt.
Keine Tages-P/L-Daten, keine Order, keine Signale → ein weiterer [CLOSE]-Task wäre Rauschen.
TODO: env-Variable CLICKUP_LIST_ID auf reine List-ID '901218902364' setzen (Bug aus 19.06. Pre-Market).
```

### Entscheidung
**Routine pausiert.** Nächster Trigger: Pre-Market Mo 2026-06-22 08:30 ET.
Keine Order, keine Memory-Migration über Holiday-Snapshot hinaus.

---

## Market Open 09:30 ET — 2026-06-19 — HANDELSFEIERTAG (Juneteenth)

### Markt-Status
```
Alpaca clock: is_open=false
next_open:    2026-06-22 09:30 ET (Montag)
Begründung:   US-Bundesfeiertag (Juneteenth, 19. Juni) — NYSE/Nasdaq geschlossen
Kalender:     18.06. Handelstag → 22.06. nächster Handelstag → 19.06. NICHT enthalten
```

### Schritt-2-Guardrail-Check (formal)
```
Daily Loss Cap  < -3%:   0,00 %    [GRÜN]
Weekly Loss Cap < -5%:  -0,037 %   [GRÜN]
Käufe Woche >= 2:        2 / 2     [LIMIT erreicht — Kaufscan ohnehin gesperrt]
VIX > 30:                16,4–17,0 [GRÜN]
Crash-Filter:            NEIN      [GRÜN]
Drawdown-Stopp:          inaktiv   [GRÜN]
Cash < 20%:              89,4 %    [GRÜN]
```
→ Ergebnis nicht relevant: Markt ist zu, keine Order möglich.

### Stop-Check (V1–V6, anhand letzter Trades vom 18.06. Close)
```
JPM 325,23 $   V1 306,16 $ SICHER (+6,2%) | V2 SICHER | V3/V4 nicht erreicht
               V5 EMA50 308,67 > EMA200 307,35 → kein Death Cross
               V6 RSI 62,1 + RS_4w +6,96% → nicht ausgelöst
UNH 401,13 $   V1 369,44 $ SICHER (+8,6%) | V2 SICHER | V3/V4 nicht erreicht
               V5 EMA50 372,91 > EMA200 335,16 → kein Death Cross
               V6 RSI 58,7 + RS_4w +3,95% → nicht ausgelöst
→ Beide Positionen unauffällig. Kein Eingriff nötig (auch nicht möglich).
```

### Entscheidung
**Routine pausiert.** Nächster Trigger: Pre-Market 08:30 ET am Montag 2026-06-22.
Watchlist 22.06. (Carry-over aus 18.06.): AVGO (Top-Pick K1–K4 ✓), GS (XLF-Konflikt),
CAT (Industrials), NVDA (Tech), LLY (XLV — UNH bereits gehalten).

### Notification
```
ClickUp-API: CLICKUP_LIST_ID-Bug gefunden + temporär gefixt.
Env-Variable hat Format "6-901218902364-1" (View-ID), API erwartet reine List-ID.
Workaround: sed 's/^[0-9]*-//; s/-[0-9]*$//' → 901218902364 → Task erfolgreich.
ROUTINE_DONE-Task ID: 869dtg866 (Holiday-Notification 19.06. abgesetzt).
TODO: env-Variable im Setup korrigieren (siehe lessons-learned 2026-06-19).
```

---

## Pre-Market 08:30 ET — 2026-06-19

### Markt-Lage
```
VIX:              ~16,40–17,00  (Cboe Open 17,23 vs. Vortag-Close 16,40, intraday Range 16,40–17,04)
                  [GRÜN, weit < 30]
SPY Close 18.06.: 746,75 $   (Vortag 741,02 → +0,773%)
SPY After-Hours:  748,46 $   (+0,23% vs. Close)  [Indikator, IEX-Snapshot]
10Y Treasury:     n/a         (Perplexity-Antwort ohne belegbare Zahl)
Markt-Status:     Pre-Market
```

### Guardrails Pre-Market
```
Daily Loss Cap   -3 %:   equity 99.962,66 $ vs. last_equity 99.962,66 $ → 0,00 %   [GRÜN]
Weekly Loss Cap  -5 %:   -0,037 % vs. Mo-Basis 100.000 $                           [GRÜN]
Drawdown -15 %:          ATH 100.012,97 $, DD -0,050 %                             [GRÜN]
Drawdown -20 %:          inaktiv                                                   [GRÜN]
VIX-Filter > 30:         VIX 16,40–17,00                                           [GRÜN]
Crash-Filter SPY -5%:    SPY gestern +0,773 %                                      [INAKTIV]
Käufe diese Woche:       2 / 2                                                     [LIMIT erreicht]
Earnings-Blackout:       keine (siehe unten)
```

### Alpaca-Konsistenz-Check
```
Alpaca portfolio_value:  99.962,66 $  (Memory Close 18.06.: 99.965,07 $)  Δ -2,41 $ → IEX-After-Hours-Tick
Alpaca cash:             89.363,96 $  (Memory: 89.363,97 $)               konsistent
Alpaca equity:           99.962,66 $  (= last_equity, kein Trade seit Close)
JPM: 3 Sh @ Entry 332,78 — current 325,22 $  unreal -22,68 $ (-2,27%) | change_today 0,00 %
UNH: 24 Sh @ Entry 401,57 — current 400,96 $ unreal -14,64 $ (-0,15%) | change_today 0,00 %
→ Memory ↔ Alpaca konsistent. Keine offenen Orders.
```

### Earnings-Blackouts (offene Positionen)
```
JPM:  nächste Earnings 2026-07-14 (Q2, CONFIRMED Wall Street Horizon) → 25 Tage entfernt, KEIN Blackout
UNH:  nächste Earnings 2026-07-16 (siehe Memory)                       → 27 Tage entfernt, KEIN Blackout
→ Stops bleiben Standard V1 -8 % ($306,16 JPM / $369,44 UNH). Keine Engsetzung.
```

### Makro-Events heute 2026-06-19
```
Kein FOMC, keine CPI/PCE, keine NFP-Daten in den Suchergebnissen.
Perplexity lieferte keine harten Tages-Termine (Kalenderdaten fehlten).
Hinweis Goldman/XTB: VIX nahe zyklischem Tief — fragile Ruhe, Short-Covering treibt Rallye.
```

### Top-News
```
1. VIX am unteren Rand (16,4) — Volatilitäts-Expansion möglich, defensiv handeln.
2. Goldman warnt vor Risiken in Finanz-/Industrie-/Halbleitersektor → JPM-Risiko im Blick.
3. SPY After-Hours leicht positiv (+0,23%), Mega-Cap-Tech-Rallye stützt Indizes.
```

### Pre-Market Verkaufssignal-Vorabcheck
```
JPM @ 325,22 $   V1 Stop 306,16 $   → SICHER (Puffer +6,2%)
                 V2 Trailing -12%   → kein neues 52w-Hoch, kein Stop-Engsetzen
                 V3/V4 TP nicht erreicht
                 V5/V6 → Live-Check am Open
UNH @ 400,96 $   V1 Stop 369,44 $   → SICHER (Puffer +8,5%)
                 V2 Trailing -12%   → SICHER (Hoch 403,56)
                 V3/V4 TP nicht erreicht
                 V5/V6 → Live-Check am Open
```

### Entscheidung Pre-Market 2026-06-19
**Kaufscan bei Market Open 09:30 ET: NEIN.**
Begründung: Käufe diese Woche 2/2 erreicht (JPM 17.06., UNH 18.06.) → bis Mo 22.06. kein Kauf zulässig.
Heutige Routinen: nur Stop-Check (V1–V6) für JPM & UNH am Open, Midday, Close.
Watchlist 19.06. (aus Close-Eintrag 18.06.): AVGO (Top-Pick, alle K1–K4 ✓ — Beobachtung für nächste Woche).

### Notification-Hinweis
```
ClickUp-API: CLICKUP_LIST_ID weiterhin laut Memory ungültig (validateListIDEx INPUT_003).
Routine-Log bleibt Memory-First → research-log + portfolio aktualisiert.
```

---

## Heutiger Market-Check — 2026-06-18 (Close 16:00 ET)

### Tagesperformance & Markt
```
Alpaca equity Close:   99.965,07 $   (last_equity 100.002,03 → daily -36,96 $ / -0,0370%)
Cash:                  89.363,97 $   (89,4%)
Investiert:            10.601,10 $   (10,6% — JPM 978,06 $ + UNH 9.623,04 $)
ATH:                  100.012,97 $   (Open 18.06.)
Drawdown:              -0,0479%

SPY:                   $746,75 Close (vs. $741,02 Vortag) → +0,773%
Alpha vs SPY:          -0,810%
JPM intraday:          -2,23% (Close 326,02 $ vs 333,46 Vortag)
UNH intraday:          +0,36% (Close 400,96 $ vs 399,53 Vortag)
VIX:                   Tagesschluss n/a (Perplexity ohne Daten — Open 17,10 GRÜN)
```

### Verkaufssignal-Check Close (V1–V6) — beide Positionen unauffällig
```
JPM Close 326,02 $   V1 SICHER (306,16 $) | V2 SICHER | V3/V4 nicht erreicht
                    V5 EMA50 308,67 > EMA200 307,35 → KEIN Death Cross
                    V6 RSI 62,1 + RS_4w +6,96% → NICHT ausgelöst
UNH Close 400,96 $   V1 SICHER (369,44 $) | V2 SICHER | V3/V4 nicht erreicht
                    V5 EMA50 372,91 > EMA200 335,16 → KEIN Death Cross
                    V6 RSI 58,7 + RS_4w +3,95% → NICHT ausgelöst
→ Keine Verkaufsorder für 19.06. nötig.
```

### Watchlist 19.06.2026 (K1–K4 vorgeprüft, K5 bei Open)
```
Symbol | Close   | EMA50    | EMA200  | K1 | RSI  | K2 | RS63d   | K3 | Vol% | K4 | Sektor / Grund
-------|---------|----------|---------|----|------|----|---------|----|------|----|-----------------
AVGO   | 411,07  |  399,96  | 358,92  | ✓  | 51,3 | ✓  | +15,37  | ✓  | 135  | ✓  | XLK Semis — alle 4 ✓ (Top-Pick)
GS     | 1096,99 |  986,97  | 878,98  | ✓  | 65,6 | ✓  | +22,31  | ✓  | 112  | ✗* | XLF — SEKTORKONFLIKT mit JPM
CAT    |  985,23 |  869,00  | 671,51  | ✓  | 65,4 | ✓  | +29,90  | ✓  |  96  | ✗  | XLI Industrials — K4 fail, hoher RS
NVDA   |  210,39 |  206,90  | 190,09  | ✓  | 50,1 | ✓  |  +4,70  | ✓  |  72  | ✗  | XLK Semis — K4 fail
LLY    | 1098,76 | 1045,28  | 963,85  | ✓  | 54,0 | ✓  |  +6,55  | ✓  |  78  | ✗  | XLV Health — 2. XLV-Pos. neben UNH (max 3)
AMD    |  537,13 |  423,20  | 266,67  | ✓  | 61,2 | ✓  | +148,54 | ✓  |  75  | ✗  | XLK Semis — K4 fail
BAC    |   56,15 |   52,87  |  52,29  | ✓  | 67,6 | ✓  |  +6,30  | ✓  | 150  | ✓  | XLF — SEKTORKONFLIKT mit JPM, RSI hot
```
> *GS K4 Vol% basiert auf gestrigem Tagesvolumen (heutige IEX-Snapshots partial).

### Watchlist morgen: AVGO (Top-Pick, alle 4 ✓), NVDA (K4 nahe), GOOGL (K4 fail), LLY (K4 fail), CAT (Industrials, RS+30%)

### Wochenstatus & Käufe
```
Käufe diese Woche: 2 / 2 (JPM 17.06., UNH 18.06.) — KEINE Käufe mehr bis Mo 22.06.
Weekly P/L:         -0,0349% (Mo-Basis 100.000 $)   [GRÜN — Limit -5%]
Weekly Loss Cap:    NICHT ausgelöst (Schwelle 95.000 $)
```

### Notification
```
ClickUp-API: CLICKUP_LIST_ID ('6-901218902364-1') wird weiterhin als ungültig
  abgewiesen (validateListIDEx INPUT_003). Memory-Files sind primäre Quelle
  → Push-Notification an Routine-Owner gesendet.
Perplexity-Marktabfrage: keine US-Tagesdaten für 18.06.2026 verfügbar
  → SPY/VIX aus Alpaca + IEX-Bars, Watchlist aus eigener K1–K4-Berechnung.
```

---

## Market-Check — 2026-06-18 (Market Open 09:30 ET)

### Market Open 09:34 ET — 2026-06-18

**Alpaca Account-Snapshot**
```
equity:           100.012,97 $
cash:              99.001,65 $
JPM-Position:      3 Shares, current $337,23, +$13,35 (+1,34%) intraday
```

**Guardrails (alle GRÜN)**
```
Daily P/L:        +0,0109%   < +/-3%
Weekly P/L:       +0,0130%   < +/-5%
VIX:              17,10      < 30
Crash-Filter:     INAKTIV    (SPY +0,3–0,5% Premarket)
Drawdown:         0,00%      < -15%
Cash:             99,0%      > 20% Reserve
Käufe Woche:      1/2 vor Scan → 1 Kauf-Slot frei
```

**JPM Verkaufssignal-Check (Open)**
```
V1 -8%  Stop $306,16  vs. $337,23  → SICHER
V2 -12% Trailing       → Position <2 Tage, kein 52w-Hoch-Tracking
V3 +20% TP1 $399,34   → nicht erreicht
V4 +35% TP2 $449,25   → nicht erreicht
V5 EMA50 308,53 > EMA200 306,97 → KEIN Death Cross
V6 RSI 72,3 < 80 → NICHT ausgelöst
→ Keine Verkaufsorder.
```

**Kandidaten-Scan (K1–K5)**
Datenbasis: Daily Bars bis Close 2026-06-17 (heutige Bar partial)
```
SYM   Close     EMA50    EMA200  K1  RSI   K2  RS63d   K3  Vol%  K4  Treffer
JPM   333,56   308,53   306,97   V  72,3   X  +3,92    V   206   V   (gehalten)
AVGO  392,91   410,42   359,38   V  46,2   X  +12,40   V   139   V   K2 fail
BAC    56,54    52,76    52,20   V  71,4   X  +8,78    V   152   V   K2 fail, +XLF-Konflikt
XOM   140,79   150,62   134,40   V  36,4   X  -22,67   X   112   X   K2/K3/K4 fail
XLK   185,74   171,11   196,46   X  54,8   V  +22,60   V   112   X   K1/K4 fail (ETF)
XLF    54,06    51,89    52,55   X  67,6   V  -1,62    X   128   V   K1/K3 fail (ETF)
XLV   150,68   147,91   149,29   X  51,5   V  -9,64    X   108   X   K1/K3/K4 fail (ETF)
NVDA  204,70   208,74   189,70   V  45,4   X  +1,47    V    71   X   K2/K4 fail
MSFT  379,05   412,86   451,98   X  34,7   X  -15,27   X   106   X   K1/K2/K3/K4 fail
AAPL  296,07   287,94   267,84   V  49,0   X  +6,45    V    74   X   K2/K4 fail
LLY  1112,10  1008,42   964,26   V  57,3   V  +9,15    V    78   X   K4 fail
V     330,36   320,73   329,22   X  57,1   V  -1,53    X    99   X   K1/K3/K4 fail
GOOGL 363,86   366,38   310,33   V  46,1   X  +6,21    V    87   X   K2/K4 fail
META  567,22   622,60   655,70   X  39,2   X  -19,86   X   140   V   K1/K2/K3 fail
UNH   399,57   370,76   333,10   V  57,7   V  +28,57   V   135   V   ALLE 4 ✓ → K5 prüfen
HD    327,48   322,98   359,07   X  56,0   V  -13,06   X   162   V   K1/K3 fail
MA    492,93   499,27   535,32   X  49,8   X  -11,04   X    54   X   K1/K2/K3/K4 fail
```

**UNH K5 (Fundamentals via Perplexity)**
```
Forward P/E:        30,63   (<= 35)  ✓
Rev Growth YoY:    +18,63%  (>= 10%) ✓
Next Earnings:    2026-07-16 → 28 Tage, KEIN Blackout
Schlagzeile:       Analysten-Konsens "Buy", letzter Kurs ~$399,53
→ K5 ✓ → UNH alle 5 Signale GRÜN
```

**Sektor-Check**
```
Aktuell offen: JPM (Financials/XLF)  → 1 Sektor
UNH = Health Care (XLV)              → unterschiedlicher Sektor, OK
Max-3-pro-Sektor: nicht tangiert.
```

**Entscheidung / Order**
```
BESTER Kandidat: UNH (höchste RS +28,57%, alle 5 Signale ✓)
Budget (VIX 17,10 < 25 → 10%): $100.012,97 × 0,10 = $10.001,30
Limit:    round($399,57 × 1,005, 2) = $401,57
Shares:   floor($10.001,30 / $401,57) = 24
Kosten:   24 × $401,57 = $9.637,68 (~9,6% des Portfolios)
Order:    BUY UNH 24 @ Limit $401,57 Day → submitted 09:34 ET
Order-ID: b9674f87-9cad-4ac0-a39f-756157f8b5ed
Status:   NEW (UNH öffnete ~$403,56, Limit erfordert Retracement)
```

**Käufe diese Woche nach Scan: 2 / 2** (JPM filled, UNH pending)
→ Nach UNH-Order keine weiteren Käufe diese Woche zugelassen.

**Notification-Hinweis**
```
ClickUp-API: CLICKUP_LIST_ID hat ungueltiges Format (validateListIDEx).
→ Per Notify-Skill Fallback: Memory-Files sind primaere Quelle.
→ Routine-Log + Trade-Log + Portfolio aktualisiert.
```

---

### Pre-Market 08:30 ET — 2026-06-18
```
VIX:              17,10   (-7,27% vs. Vortag-Close 18,44; intraday Quote Cboe 07:29 ET)
                  [Hinweis: Memory 17.06. 16:00 ET = 16,41 — VIX-Tick nach Close höher;
                   Diskrepanz notiert, alle Werte weiterhin GRÜN < 30]
SPY Premarket:    +0,3 bis +0,5 %  (indikativ → ~$743–745 vs. $741,02 Close)
10Y Treasury:     4,2–4,3 %
DXY:              ~105–106 (unverändert)
Markt-Status:     Pre-Market
```

### Guardrails Pre-Market 08:30 ET
```
Daily Loss Cap   -3 %:   Heute Equity 100.008,60 $ vs. last_equity 100.002,03 $
                          → P/L +0,0066 %  [GRÜN]
Weekly Loss Cap  -5 %:   +0,009 % vs. Mo-Basis 100.000 $   [GRÜN]
Drawdown -15 %:          ATH 100.008,60 $, DD 0,00 %        [GRÜN]
Drawdown -20 %:          nicht aktiv                         [GRÜN]
VIX-Filter > 30:         VIX 17,10                           [GRÜN]
Crash-Filter SPY -5%:    SPY gestern -1,27 %                 [INAKTIV]
Käufe diese Woche:       1 / 2                               (1 frei)
Earnings-Blackout:       keine (siehe unten)
```

### Alpaca-Konsistenz-Check
```
Alpaca portfolio_value:  100.008,60 $   (Memory Close 17.06.: 100.002,43 $)
Alpaca cash:              99.001,65 $   (Memory: 99.001,66 $)  → konsistent
Alpaca equity:           100.008,60 $   (last_equity 100.002,03 $)
JPM-Position:    3 Shares @ Entry $332,78 — current $335,65
                  unrealized P/L +8,61 $ (+0,86 %), change_today +0,66 %
→ Memory & Alpaca konsistent (Differenz Close = Pre-Market-Tick JPM).
```

### Earnings-Blackouts (offene Positionen)
```
JPM:  nächste Earnings 2026-07-14 (Q2)  → 26 Tage entfernt, KEIN Blackout
→ Stop-Loss bleibt V1 -8 % ($306,16). Kein Engsetzen nötig.
```

### Makro-Events heute 2026-06-18
```
- Kein FOMC, keine CPI/PCE, keine NFP.
- Wöchentliche Initial Jobless Claims (08:30 ET).
- Diverse Fed-Reden mittlerer Relevanz.
```

### Top-News
```
1. Niedriger VIX (~17) + Erwartung sanfter Fed-Politik stützen Risk-Assets.
2. US-Mega-Cap-Tech-Rallye treibt Indizes nahe Rekordniveau, SPY indikativ +0,3 %.
3. Markt-Narrativ: Timing & Anzahl der Fed-Zinsschritte 2026 bleibt zentral.
```

### Entscheidung Pre-Market 2026-06-18
Kaufscan bei Market Open 09:30 ET: **JA**.
Alle Guardrails GRÜN, VIX deutlich < 25, kein Crash-Filter, 1 Kauf-Slot frei.
Watchlist (aus Close-Eintrag 17.06.): AVGO (Semis), BAC (Financials — auf Sektor-
Gewichtung achten, JPM bereits XLF), XOM (Energy-Rotation).

---

## Heutiger Market-Check — 2026-06-17 (Close 16:00 ET)

### Makro-Lage (Tagesschluss)
```
VIX:              16,41   [GRÜN, unter 30]
SPY heute:        $741,02 (-1,27% vs. Vortag $750,58)
SPY Tagesspanne:  $739,26 – $752,13 (Outside-Day, rote Kerze)
Crash-Filter:     NEIN (Schwelle -5%/Tag, heute -1,27%)
Markt-Status:     CLOSED
```

### Tages-Performance Bull
```
Equity Open  ~ $100.000,00  →  Equity Close: $100.002,43
Daily P/L:        +2,43 $  (+0,0024%)
Alpha vs. SPY:    +1,27%
Treiber:          JPM-Fill +0,24% während breiter Markt -1,27% nachgab
```

### Watchlist morgen 2026-06-18 (K1–K3 vorgeprüft, K4/K5 bei Open)
```
Symbol | Today  | K1 EMA50>200 | K2 RSI Range | K3 RS vs SPY | Grund
-------|--------|--------------|--------------|--------------|------
AVGO   | +4,35% | wahrsch. ✓   | mittel       | sehr stark   | Semis-Outperformer trotz SPY -1,27%
BAC    | TBD    | TBD          | TBD          | wahrsch. ✓   | Financials-Korrelation zu JPM-Trade
XOM    | TBD    | TBD          | TBD          | TBD          | Energy-Rotation Defensive
JPM    | +0,73% | ✓            | 68 (heiß)    | ✓ heute      | bereits gehalten, kein Nachkauf
```
> Hinweis: Sektor Financials zeigt heute klare relative Stärke. Halte
> max-3-Positionen-pro-Sektor-Regel im Auge (aktuell 1 × XLF mit JPM).

### Markt-Sentiment
```
Top-Sektoren:     Technology (XLK), Financials (XLF), Health Care (XLV)
SPY 63d Return:   +11,86%
```

### Watchlist-Status (Kandidaten für Kauf, 17.06.2026 09:32 ET)
```
Symbol | EMA50>200 | RSI  | RS vs SPY | Vol%  | P/E   | Kauf?
-------|-----------|------|-----------|-------|-------|-------
AAPL   | ✓ 289>267 | 53,1 | +5,85%    |  80%  |   —   | nein (K4)
MSFT   | ✗ 412<454 | 40,2 | -13,25%   |  85%  |   —   | nein (K1/K2/K3)
NVDA   | ✓ 206>191 | 51,0 | +2,15%    |  72%  |   —   | nein (K4)
JPM    | ✓ 306>305 | 68,5 | +3,57%    | 127%  | 14,58 | JA (alle 5)
LLY    | ✓ 1040>955| 59,6 | +8,80%    |  70%  |   —   | nein (K4)
V      | ✗ 321<329 | 60,3 | -3,86%    | 117%  |   —   | nein (K1/K3)
```

### Key-News
```
1. VIX bei 16,41 — historisch niedrige Volatilität, Tech/Financials/Health führen
2. JPM Q1/2026: Net Revenue $50,5B +10% YoY, Markets-Revenue $11,6B record
3. JPM Earnings Q2 erwartet 2026-07-15 (28 Tage entfernt, kein Blackout)
```

### Entscheidung
Buy-Limit-Order JPM 3 Shares @ $332,80 (Day) platziert → **GEFÜLLT 15:20 ET @ $332,78**.
JPM-Position offen, V5/V6 nicht ausgelöst, Stop-Loss $306,16.
Watchlist morgen: AVGO, BAC, XOM (Sektor-Rotation Fin/Energy).

---

## Research-Archiv

### 2026-06-17 Close 16:00 ET
```
SPY Close: $741,02 (-1,27% vs. $750,58 Vortag) | VIX: 16,41 (GRÜN)
Bull-Equity: $100.002,43 (+$2,43 / +0,0024%) | Alpha: +1,27% vs SPY
Position offen: JPM 3@$332,78 (+0,24%), Stop $306,16, V5/V6 OK
Pending: keine
Käufe Woche: 1/2
Watchlist 18.06.: AVGO (Semis-Stärke), BAC (Fin), XOM (Energy-Rot.)
Marktbild: Mega-Cap-Tech schwach (META -5,49%, MSFT -3,79%, GOOGL -2,55%),
           Financials/Semis halten (JPM +0,73%, AVGO +4,35%).
```

### 2026-06-17 Market Open
```
VIX: 16,41 | SPY: $750,63 (+0,04%) | Sentiment: Neutral/Greed
Top-Sektoren: XLK, XLF, XLV
Kandidaten geprüft: AAPL, MSFT, NVDA, JPM, LLY, V
Treffer (alle 5 Signale): JPM
Order: Buy Limit 3@$332,80 Day (Order-ID d90de96d)
Käufe diese Woche: 0/2 (1 pending)
### 2026-06-17 Pre-Market 08:30 ET
```
VIX: 16.21 (-1.22%) | SPY Premarket: +0.3% | Treasury 10Y: 4.20-4.25% | DXY: ~105-106
Guardrails: GRÜN (Daily/Weekly 0%, DD 0%, VIX < 30, kein Crash-Filter)
Earnings-Blackouts: keine (keine offenen Positionen)
Makro-Events heute: Keine Fed-Sitzung, keine CPI/PPI. Nur Fed-Reden.
Top-News: (1) Tech-Megacap Earnings-Revisions / KI-Capex bewegen Nasdaq. (2) Mögliche Verzögerung weiterer Fed-Zinssenkungen wg. zäher Kerninflation. (3) Geopolitik Südchinesisches Meer belastet Asien-Sentiment.
Hinweis: Alpaca Paper-Account zeigt $100k (Memory: 10k €). Discrepancy notiert.
Entscheidung: Kaufscan bei Market Open: JA (alle Guardrails grün, VIX niedrig).
```

### 2026-05-31 (Erster Tag)
```
Status: Initialisierung. Keine Positionen. Watchlist wird aufgebaut.
VIX: —  |  SPY: —  |  Sentiment: —
```

---

## Research-Template (täglich eintragen)

```markdown
### [DATUM]
VIX: X | SPY: +X% | Sentiment: [Greed/Fear/Neutral]
Earnings-Blackouts aktiv: [SYMBOL, SYMBOL]
Watchlist-Kandidaten: [SYMBOL (+Grund)]
Top-News: [1-3 Zeilen]
Entscheidung: [Kaufen X / Warten / Pause wegen VIX/Crash]
```
