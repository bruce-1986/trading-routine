# Research Log

**Bot:** Bull | **Aktualisiert:** täglich

---

## Market Close 16:00 ET — 2026-08-12 (Mi, KW33 Tag 3) FINAL — Daily −0,053 % GRÜN / Alpha −0,315 pp NEG / DD −3,700 % GRÜN / Weekly KW33 Tag 3 −0,155 % GRÜN / Kauf-Slots KW33 0/2 OFFEN

### Alpaca /v2/account Close 16:04 ET
- portfolio_value/equity: **96.363,47 $** | last_equity: 96.414,68 $
- Daily P/L: **−51,21 $ = −0,053 %** [GRÜN, Cap −3 %, marginal verbessert vs Midday −0,142 %]
- cash: 56.707,49 $ (**58,85 %**, unverändert)
- long_market_value: **39.655,98 $** (5 Pos, marginal −42,73 vs Di Close 39.698,71 = −0,108 % nahezu flat)
- buying_power: 337.866,70 $ | 0 pending orders | status ACTIVE | trading_blocked false

### SPY Close 16:00 ET (Alpaca Daily-Bar IEX)
- SPY 772,54 vs Di Close 770,52 = **+0,262 % positiv** [Crash-Filter INAKTIV] — CPI-Release-Post-Reaction leicht bullish
- **Alpha vs Portfolio: −0,315 pp NEG** (Portfolio −0,053 % vs SPY +0,262 %) — Portfolio underperformt SPY-Recovery via AAPL/V-Weakness, aber P/L-Absolut nahezu flat

### V1–V6 Vollcheck EOD (Alpaca IEX 277d Bars)
| Sym | Close | chg | P/L% | V1 Std | V2 (Wick*0,88) | V5 EMA50>EMA200 | V6 RSI | RS_4w |
|-----|-------|-----|------|--------|----------------|------------------|--------|-------|
| AAPL | 302,20 | −0,88 | **−4,64 Worst** | **+3,67 % ENGSTE** (Thr 291,51) | **⚠ −0,334 % BROKEN** via Wick 344,555 (Thr 303,21) DQF **2. Tag** | 309,32>281,39 = +9,93 pp ✓ | 40,14 ✓ | −10,10 pp |
| JPM | 365,23 | **+0,88 Best** | **+9,75 Best** | **+19,29 %** (Thr 306,16) | +13,37 % via **NEUES Hoch 366,085** (Thr 322,15) | 339,54>317,87 = +6,82 pp ✓ | 68,85 ✓ | +2,89 pp |
| LLY | 1219,975 | +0,58 | +2,20 | +11,07 % (Thr 1098,38) **BO ENDED — Std-V1 primär** | +11,04 % via 1248,53 (Thr 1098,70) | 1150,95>1022,57 = +12,55 pp ✓ | 58,11 ✓ | +3,13 pp |
| UNH | 405,64 | +0,78 | +1,01 | +9,79 % (Thr 369,44) | **⚠ +0,001 % razor BROKEN** via 460,95 (Thr 405,636) DQF **13. Tag**; Alt-V2 via 437,13 = 384,67 Puffer **+5,45 % SICHER** | 407,25>362,59 = +12,32 pp ✓ | 44,01 ✓ | −5,37 pp |
| V | 359,48 | −0,84 | +0,65 | +9,40 % (Thr 328,60) | +9,24 % via 373,97 (Thr 329,09) | 350,16>338,32 = **+3,50 pp engster** ✓ | 51,33 ✓ | −1,18 pp |

### V-Trigger-Zusammenfassung
- **V1 Std:** alle 5 SICHER (min AAPL +3,67 %)
- **V2:** ⚠ **AAPL DQF Wick-BROKEN 2. Tag** −0,334 % (Std-V1 +3,67 % primär), **UNH DQF Wick-BROKEN 13. Tag** razor +0,001 % (Alt-V2 +5,45 % + Std-V1 +9,79 % primär) → Rule 5 No-Action, Owner-Entscheidung pending
- **V3/V4:** max P/L JPM +9,75 % << 20 %-TP1, kein Trigger
- **V5:** alle 5 Golden Cross intakt (V engster +3,50 pp)
- **V6:** alle 5 SICHER (max RSI JPM 68,85 << 80)
- **Sell-Order für Do 13.08.:** KEINE (0 offene Orders bestätigt via Alpaca)

### Watchlist Do 13.08. K1–K5 aus Alpaca IEX EOD Mi 12.08.
| Sym | Prio | Sektor | Close | K1 EMA-Gap | K2 RSI | K3 RS_63d | K4 Vol% Avg20 | Status |
|-----|------|--------|-------|------------|--------|-----------|---------------|--------|
| MRK | **1** | XLV | 132,90 | +12,48 % ✓ | 63,48 ✓ | +13,62 pp ✓ | **128 % ✓** | **K1-K4 alle ✓ — K5 pending**; ⚠ LEVEL 0 XLV-Cap Grenzfall 20,22 %+10 %=~30 % |
| UAL | 2 | XLI | 125,10 | +10,56 % ✓ | 51,67 ✓ | **+25,87 pp #1** ✓ | 31 % FAIL 11. Tag | K1-K3 ✓ K4 persistent FAIL |
| UNP | 3 | XLI | 293,78 | +10,08 % ✓ | 54,64 ✓ | +5,90 pp ✓ | 46 % FAIL | K1-K3 ✓ K4 FAIL |
| MU | Backup | XLK | 911,30 | +47,79 % ✓ | 51,09 ✓ | +14,35 pp ✓ | 81 % FAIL | K1-K3 ✓ K4 FAIL — XLK-Konflikt AAPL |
| PANW | REJECT | XLK | 387,11 | +30,01 % ✓ | **70,48 knapp FAIL** | +74,93 pp ✓ | 85 % FAIL | K2 knapp >70 |
| BAC | REJECT | XLF | 64,81 | +9,12 % ✓ | **73,58 FAIL** | +22,90 pp ✓ | 99 % FAIL | K2 heavy FAIL |
| NVDA | REJECT | XLK | 224,11 | +5,54 % ✓ | 62,39 ✓ | **−3,19 pp FAIL** | 81 % FAIL | K3 NEG persistent |
| TMO/ABT | REJECT | XLV | — | — | RSI >70 FAIL | — | — | K2 FAIL |
| GS/AMD | REJECT | XLF/XLK | — | — | RSI <50 FAIL | — | — | K2 FAIL |
| ORCL/LOW/HD | REJECT | mix | — | Death-Cross K1 FAIL | — | — | — | K1 FAIL |

**Watchlist morgen:** MRK Prio 1 (**alle K1–K4 ✓**, K5 morgen verifizieren, XLV-Sektor-Cap Grenzfall — Kauf nur bei K5-Bestätigung UND Sektor-Struktur-Compliance), UAL/UNP K4-Vol-Rebound-Watch (persistent FAIL), MU Backup (K1–K3 ✓ K4 FAIL, XLK-Konflikt AAPL).

### Sektor-Struktur EOD
- XLV **20,22 %** (UNH 10,10 + LLY 10,12 marginal erhöht vs Di Close 20,09 % via UNH/LLY-Recovery)
- XLF **11,21 %** (JPM 1,14 + V 10,07 marginal verschlechtert vs Di Close 11,29 % via V-Weakness)
- XLK **9,72 %** (AAPL marginal verschlechtert vs Di Close 9,80 %)
- Cash 58,85 %

### Guardrails
- 8/8 GRÜN + 2 WARN (**UNH V2 BROKEN razor +0,001 % via 52w-Wick 460,95 DQF 13. Tag persistent** — Std-V1 +9,79 % + Alt-V2 +5,45 % primär sicher, Owner-Entscheidung pending seit Di-Midday-Push; **AAPL V2 BROKEN −0,334 % via 52w-Wick 344,555 DQF 2. Tag** — Std-V1 +3,67 % ENGSTE primär sicher, Rule 5 No-Action, Owner erhielt Midday-Escalation-Push)
- Daily/Weekly/DD/Crash/VIX/Positions 5/8/Käufe-Slot 2/2 alle sicher
- Weekly Loss Cap Check: −0,155 % vs Cap −5 % — GRÜN, kein Auslöser

### Perplexity Silence-Rule
- KEIN Query Close (Watchlist-Kandidaten aus Alpaca IEX EOD-Bars vollständig; K5 morgen Pre-Market/Open für MRK verifizieren)

### Notification & ClickUp
- ClickUp Prio 3 [CLOSE] Tagesbericht — **ITEM_246 "Max usage for custom task types reached" 13. Tag persistent** → Fallback Memory-Only
- **KEINE PushNotification** (Silence-Rule: kein V-Trigger, kein Cap-Alert, Daily −0,053 % marginal, AAPL V2-DQF-Escalation-Push wurde Midday abgesetzt, UNH V2-DQF-Owner-Push steht seit Di-Midday, keine Portfolio-Earnings 3 HT, kein Owner-Handlungsbedarf; MRK-K5-Prüfung morgen früh Standard-Routine)

### Nächste Routine
- Do 13.08. 08:30 ET Pre-Market KW33 Tag 4
- **MRK K5-Verifikation** (FwdPE ≤ 35 + RevGrowth YoY ≥ 10 %) + **XLV-Sektor-Cap-Assessment** (aktuell 20,22 %, +MRK ~10 % → ~30 % Grenzfall)
- UNH V2-Wick-DQF-Verlauf (Owner-Entscheidung pending, 13. Tag)
- AAPL V2-Wick-DQF-Verlauf (2. Tag, RSI 40 Oversold-Watch)
- LLY Std-V1-Primary-Umstellung (BO ENDED Di) Ausklang

---

## Market Open 09:41 ET — 2026-08-12 (Mi, KW33 Tag 3) — Daily -0,084 % GRÜN / Alpha -0,385 pp NEG / DD -3,730 % GRÜN / Weekly KW33 Tag 3 -0,185 % GRÜN / Kauf-Slots KW33 0/2 OFFEN

### Alpaca /v2/account Live 09:41 ET
- portfolio_value/equity: **96.333,71 $** | last_equity: 96.414,68 $
- Daily P/L: **-80,97 $ = -0,084 %** [GRÜN, Cap -3 %, marginal verbessert vs Pre -0,075 %]
- cash: 56.707,49 $ (**58,86 %**, unverändert)
- long_market_value: **39.626,22 $** (5 Pos, -72,49 vs Di Close 39.698,71 = **-0,183 %** marginal-negativ)
- buying_power: 337.783,37 $ | 0 pending orders | status ACTIVE | trading_blocked false

### SPY Live 09:41 ET (Alpaca latestTrade IEX)
- SPY 772,84 vs Di Close 770,52 (Alpaca Daily-Bar) = **+0,301 % positiv** [Crash-Filter INAKTIV; Di -0,323 %] — CPI-Awaited-Recovery
- **Alpha vs Portfolio: -0,385 pp NEG** (Portfolio -0,084 % vs SPY +0,301 %) — Portfolio underperformt SPY-Recovery deutlich via AAPL/LLY/V-Weakness

### Positions V1/V2 Live-Check (V5/V6 NICHT geprüft — nur Close-Vollcheck)
| Sym | Cur | chg | P/L% | V1-Puffer Std | V2-Puffer (Wick*0,88) | Status |
|-----|-----|-----|------|---------------|------------------------|--------|
| AAPL | 303,42 | **-0,45 % Worst** | **-4,24 Worst** | **+4,09 % ENGSTE Std** (Thr 291,51 primär) verschlechtert vs Pre +4,28 % | **+0,069 % razor via Wick 344,555 (Thr 303,21)** marginal verbessert vs Pre +0,26 % | SICHER (Std-V1 primär) |
| V    | 362,27 | -0,15 % | +1,43 | +10,25 % (Thr 328,60) | +10,08 % via 373,97 (Thr 329,09) | SICHER |
| UNH  | 405,56 | **+0,76 % Best** | +0,99 | +9,78 % (Thr 369,44) verbessert vs Pre +8,95 % via UNH-Recovery | **⚠️ -0,020 % BROKEN via 460,95 (Thr 405,636)** DQF 14. Tag persistent marginal verbessert vs Pre -0,78 %; Alt-V2 via 437,13 = 384,67 Puffer +5,42 % SICHER | SICHER (Std-V1 + Alt-V2 primär, Rule 5 No-Action) |
| LLY  | 1210,00 | -0,41 % | +1,35 | +10,16 % (Thr 1098,38) verschlechtert vs Pre +10,26 % (**Blackout-V1_neu 1134,20 Bull-Konvention letzte Session Di 11.08. ABGESCHLOSSEN — ab HEUTE Std-V1 primär**) | +10,13 % via 1248,53 (Thr 1098,70) | SICHER (Std-V1 primär ab jetzt) |
| JPM  | 363,35 | +0,33 % | **+9,19 Best** | **+18,68 %** (Thr 306,16) | +13,72 % via 363,08 (Thr 319,51) | SICHER |

### V3/V4 kein Trigger
- max P/L JPM +9,19 % << 20 %-TP1

### Kaufsignal-Scan Slot 1/2 KW33 — Watchlist 6 Kandidaten (~11 min Session-Elapsed 2,82 %, K4-Linear-Pace-Threshold ≥3,38 % Prev-Full-Day-Vol für ≥120 % Avg20-Extrapolation)
- **MRK (XLV) Prio 1 K4 PASS extrapol ~125 % Avg20**: 130,75 chg +0,32 %, session_vol IEX 10.668 / 0,0282 = 378k vs Avg20 301.916 = 125,3 %; K1-K3 ✓ vorbekannt RS +12,87 pp → **LEVEL 0 SKIP XLV-Sektor-Cap 20,15 % + MRK ~10 % → 30,15 %** (verletzt strategy.md 30 %-Cap); MRK bleibt blockiert bis UNH/LLY-Reduzierung
- **UAL (XLI) Prio 2 REJECT K4-FAIL 10. Tag persistent**: 126,58 chg +0,32 %, session_vol 1.226 = 0,63 % Avg20 (extrapol ~22 %)
- **UNP (XLI) Prio 3 REJECT K4-FAIL heavy**: 292,635 chg -0,04 %, session_vol 1.627 = 0,96 % Avg20 (extrapol ~34 %)
- **BAC (XLF) K4 PASS extrapol ~179 % Avg20**: 64,06 chg +0,11 %, session_vol 114.211 / 0,0282 = 4,05M vs Avg20 2,27M; K1/K3 ✓ vorbekannt RS +22,40 pp aber **K2 RSI 70,26 Close FAIL persistent bleibt** (RSI wahrscheinlich weiter >70) → REJECT
- **PANW (XLK) Prio 4 REJECT K4-FAIL + K2 RSI 69,57 upper-border**: 383,21 chg -0,15 %, session_vol 2.962 = 1,03 % Avg20 (extrapol ~37 %), XLK-Konflikt AAPL 9,76 %
- **NVDA (XLK) Backup K4 STRONG PASS ~295 % Avg20**: 221,48 chg +1,85 %, session_vol 383.285 / 0,0282 = 13,6M vs Avg20 4,61M; K4 stark aber **K3 -3,75 pp NEG persistent** + XLK-Konflikt AAPL → REJECT
- **BLOCKIERT bleiben**: GS/AMD/MU/ABBV (K2 <50), CVS (K2 31,61), EOG/COP/XOM (K3 NEG), ORCL (K1 Death-Cross)

### Slot 1/2 + 2/2 KW33 OFFEN — kein Kandidat erfüllt alle 5 K1-K5
- MRK Sektor-Cap-Blocker, BAC K2 FAIL persistent, NVDA K3 NEG, UAL/UNP/PANW K4 heavy FAIL
- Re-Check Midday für MRK Vol-Follow-up (aber XLV-Cap bleibt Blocker), BAC RSI-Cool-down-Watch

### Sektor-Struktur Live
- XLV **20,15 %** (UNH 10,10 + LLY 10,05 marginal erhöht vs Di Close 20,09 % via UNH-Recovery)
- XLF **11,28 %** (JPM 1,13 + V 10,15 marginal verschlechtert vs Di Close 11,29 %)
- XLK **9,76 %** (AAPL leicht reduziert vs Di Close 9,80 %)
- Cash 58,86 %

### Guardrails
- 8/8 GRÜN + 1 WARN (**UNH V2 BROKEN -0,020 % via 52w-Wick 460,95 DQF 14. Tag persistent** — Std-V1 +9,78 % + Alt-V2 +5,42 % primär sicher, Owner-Entscheidung pending; LLY BO ENDET HEUTE → Std-V1 primär ab jetzt)
- Daily/Weekly/DD/Crash/VIX/Positions 5/8/Käufe-Slot 2/2 alle sicher
- Weekly Loss Cap Check: -0,185 % vs Cap -5 % — GRÜN

### Perplexity Silence-Rule
- KEIN Query Market Open (Effizienz + persistente Halluzinationen 5. Mal Serie; Watchlist aus EOD-Alpaca-Daten + Live-Session-Vol ausreichend)

### CPI-Release
- Perplexity Pre-Market bestätigte CPI-Release erwartet heute (CNBC-Snippet) → intraday-Volatilität möglich post-Release; keine strategy.md-Regel blockiert Käufe, aber Vorsicht bei Watchlist-K4-Vol-Interpretation nach Release

### Notification & ClickUp
- ClickUp Prio 4 Routine-Log ITEM_246-Fehler persistent 11. Tag → Fallback Memory-Only per notify-skill.md
- **KEINE PushNotification** (Silence-Rule Routine: kein V-Trigger, kein Cap-Alert, kein Kauf, alle V1 Std sicher, UNH V2-Wick verbessert vs Pre, AAPL V2 razor verbessert vs Pre, LLY BO-Ende ordnungsgemäß, keine Portfolio-Earnings 3 HT, kein Owner-Handlungsbedarf; Owner erhielt Fr-Wochenschluss-Push + Di-Midday-UNH-Push)

### Nächste Routine
- Mi 12.08. 13:00 ET Midday Stop-Check KW33 Tag 3
- UNH V2-Wick-DQF-Verlauf (Owner-Entscheidung pending, aktuell verbessert vs Pre aber DQF 14. Tag persistent)
- AAPL V2-Wick-Puffer-Verlauf razor +0,069 %
- LLY Std-V1-Primary-Umstellung-Ausklang (BO-Ende)
- Watchlist MRK/UAL/UNP/BAC K4-Vol-Pace-Post-CPI-Check
- CPI-Release-Reaktion-Assessment für Portfolio + SPY

---

## Pre-Market 08:30 ET — 2026-08-12 (Mi, KW33 Tag 3) — Guardrails GRÜN / VIX 15,28 / SPY Pre +0,329 % / Kaufscan Market Open JA / Earnings-Blackout keine

### Alpaca /v2/account Pre-Market 08:35 ET
- portfolio_value/equity: **96.342,43 $** | last_equity: 96.414,68 $ (Alpaca-EOD-Adjust vs Memory-Close 96.406,20 = +8,48 marginal reconciliation)
- Daily P/L: **-72,25 $ = -0,075 %** [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (**58,86 %**, unverändert)
- long_market_value: **39.634,94 $** (5 Pos, -63,77 vs Di Close 39.698,71 = -0,161 % marginal)
- buying_power: 337.807,79 $ | 0 pending orders | status ACTIVE | trading_blocked false
- DD vs ATH 100.066,47: **-3,722 %** [GRÜN, verschlechtert vs Di Close -3,658 %]
- Weekly KW33 Tag 3 vs Fr Close 96.512,65: **-0,176 %** [GRÜN, weit von Cap -5 %]

### Positions Pre-Market (Alpaca IEX ~08:35 ET, current_price)
- **AAPL** 31 Sh @ 304,00 (chg -0,30 %, P/L -4,06 % = -398,55 $ Worst; Std-V1 291,51 Puffer +4,28 % ENGSTE verschlechtert vs Di Close +4,59 %; V2 via Wick 344,56 = Thr 303,21 razor +0,26 % verschlechtert vs Di Close +0,55 %)
- **JPM** 3 Sh @ 362,35 (chg +0,09 %, P/L +8,89 % = +88,71 $ Best P/L)
- **LLY** 8 Sh @ 1.211,02 (chg -0,33 %, P/L +1,44 % = +137,06 $; **BO Bull-Konvention HT+2 ENDET → ab HEUTE Std-V1 1.098,38 primär, Puffer +10,26 % sicher**; V2 via 1.248,53 Thr 1.098,70 Puffer +10,23 %)
- **UNH** 24 Sh @ 402,50 (chg +0,08 %, P/L +0,23 % = +22,32 $; Std-V1 369,44 Puffer +8,95 % sicher; **⚠️ V2 via 52w-Wick 460,95 = Thr 405,636 BROKEN Puffer -0,78 % 13. Tag DQF persistent, Alt-V2 via 437,13 = 384,67 Puffer +4,63 % SICHER — Owner-Entscheidung pending seit Di-Midday-Push**)
- **V** 27 Sh @ 361,80 (chg -0,28 %, P/L +1,29 % = +124,80 $; Std-V1 328,60 Puffer +10,10 %; V2 via 373,97 Thr 329,09 Puffer +9,93 %)

### Perplexity Daily Macro Check (Pre-Market Request #1)
- **VIX: 15,28 Punkte** (Mo Close 11.08. WSJ/FRED, aktuell 15,29-15,38 intraday leicht höher) → **VIX-Filter GRÜN << 30**
- **SPY Pre-Market: 773,05 $** (Alpaca IEX latestTrade 08:35:59 ET) vs Di Close 770,52 = **+0,329 % marginal POSITIV** → Crash-Filter INAKTIV
- **US 10Y Treasury Yield: 4,68 %** (TradingEconomics/CNBC 08/12, Mo 4,72 % FRED DGS10 = **-0,04 pp leicht gefallen** via niedrigere Ölpreise + US-Iran-Diplomatie-Fortschritte Straße von Hormuz)
- **Wichtige Makro-Events heute:** **CPI-Release erwartet** (CNBC 08/12 "await key inflation data due later in session") — Perplexity-Query #2 hatte "KEINE" gemeldet, Query #3 via CNBC-Artikel-Snippet CPI-Release explizit bestätigt → **erhöhte Vorsicht bei intraday Preis-Bewegungen post-Release**; KEINE FOMC-Minutes, KEINE PPI, KEINE bestätigten Fed-Speeches
- **Top 3 News (Pre-Market seit gestern Abend):**
  1. **CPI-Report heute erwartet** — Yields warten flat auf Inflation-Daten
  2. **US-Iran diplomatische Bemühungen** Straße von Hormuz → Ölpreise-Stabilisierung, Yields -0,04 pp
  3. **10Y-Yield leicht rückläufig** auf 4,68 % nach Vortag 4,71 %

### Guardrail-Check nach Research
- **VIX 15,28 << 30** → GRÜN, Kauf erlaubt
- **SPY Pre +0,329 %** → nicht < -2 %, keine erhöhte Vorsicht via SPY
- **Crash-Filter INAKTIV** (SPY Di -0,323 % nicht < -5 %) → Käufe erlaubt
- **CPI-Release heute** → intraday-Volatilität möglich, aber keine strategy.md-Regel blockiert Käufe — Watchlist-Kandidaten normal per K1-K5 prüfen
- **Blackout-Kalender Portfolio + Watchlist (12.-14.08.):** AAPL/JPM/LLY/UNH/V/UAL/UNP/MRK/PANW/BAC alle **KEINE Earnings 3 HT** (PANW nächster Termin 01.09.2026; AAPL letzter 30.07.2026 vergangen) → keine Stop-Verengung auf -5 % nötig
- **Alle 8 Guardrails GRÜN + 2 WARN** (LLY BO ENDET HEUTE → Standard-V1 primär ab jetzt; **UNH V2-Wick BROKEN 13. Tag persistent — Std-V1 +8,95 % + Alt-V2 +4,63 % primär sicher, Owner-Entscheidung pending seit Di-Midday-Push**)

### Entscheidung Kaufsignal-Scan Market Open 09:30 ET
- **JA** — alle Level 0-3 Guardrails GRÜN, VIX << 30, SPY Pre marginal POSITIV, Crash-Filter INAKTIV, Blackout leer, ausreichend Cash 58,86 %, Slots 1/2 + 2/2 KW33 offen
- **Watchlist Prio Mi 12.08.:** MRK Prio 1 XLV (K1-K3 ✓ RS +12,87 pp; **LEVEL 0-SKIP XLV-Sektor-Cap** 20,09 % + MRK ~10 % → 30 %-Regel-Bruch), UAL Prio 2 XLI (K1-K3 ✓ RS +26,33 pp #1, K4 10. Tag Vol-Watch), UNP Prio 3 XLI (K1-K3 ✓ RS +6,91 pp, K4 Vol-Watch), PANW Prio 4 XLK (K1-K3 ✓ RS +75,35 pp, RSI 69,57 upper-border, XLK-Konflikt AAPL 9,79 %), BAC Backup XLF (K2 RSI 70,26 knapp FAIL persistent)
- **CPI-Vorsicht:** Bei Watchlist-K4-Vol-Beat post-CPI Perplexity-Symbol-Query zur Bestätigung von Momentum vs CPI-Reaktions-Noise (Perplexity-Halluzinations-Serie beachten → Alpaca-Daten primär)
- **Nächster Check:** Market Open 09:30 ET KW33 Tag 3

---

## Market Close 16:00 ET — 2026-08-11 (Di, KW33 Tag 2) FINAL — Daily -0,370 % GRÜN / Alpha -0,046 pp NEG marginal / DD -3,658 % GRÜN / Weekly KW33 Tag 2 -0,110 % GRÜN / Kauf-Slots KW33 0/2 OFFEN

### Alpaca /v2/account Close 16:00 ET
- portfolio_value/equity: **96.406,20 $** | last_equity: 96.763,84 $
- Daily P/L: **-357,64 $ = -0,370 %** [GRÜN, Cap -3 %, verschlechtert vs Midday -0,226 %]
- cash: 56.707,49 $ (**58,82 %**, unverändert)
- long_market_value: **39.698,71 $** (5 Pos, -358,12 vs Mo Close 40.056,83 = **-0,894 %**)
- buying_power: 337.986,35 $ | 0 pending orders | status ACTIVE | trading_blocked false

### SPY Close 16:00 ET (Alpaca Daily-Bar IEX)
- SPY 770,52 vs Mo Close 773,02 = **-0,323 % negativ** [Crash-Filter INAKTIV; Mo -0,018 %]
- **Alpha vs Portfolio: -0,046 pp NEG marginal** (Portfolio -0,370 % vs SPY -0,323 %) — Wende vs Midday +0,097 pp via UNH/LLY-Nachmittags-Give-back

### V1-V6 Vollcheck EOD (Alpaca IEX 342d Bars)
| Sym | Close | chg | P/L% | V1 Std | V2 (Wick*0,88) | V5 EMA50>EMA200 | V6 RSI | RS_4w |
|-----|-------|-----|------|--------|----------------|------------------|--------|-------|
| AAPL | 304,80 | -1,12 | -3,81 **Worst** | **+4,59 % ENGSTE** (Thr 291,51) | **+0,55 % razor-thin** via Wick 344,555 (Thr 303,21) DQF | 309,61>278,20 = +11,29pp ✓ | 41,87 ✓ | -5,66pp |
| UNH | 402,49 | **-1,66 Worst** | +0,10 | +8,94 % (Thr 369,44) | **⚠️ -0,78 % BROKEN** via 460,95 (Thr 405,64) DQF 12. Tag; **Alt-V2 via 437,13 = 384,67 Puffer +4,63 % SICHER** | 407,32>364,58 = +11,72pp ✓ | 41,53 ✓ | -7,84pp |
| LLY | 1215,02 | -1,37 | +1,77 | +10,43 % (Thr 1098,38) BO-neu 1134,20 +6,95 % **letzte Session ENDET** | +10,40 % via 1248,53 (Thr 1098,70) | 1148,13>1019,44 = +12,62pp ✓ | 57,04 ✓ | +2,61pp |
| V | 362,82 | +0,42 | +1,58 | +10,33 % (Thr 328,60) | +10,16 % via 373,97 (Thr 329,09) | 349,78>336,26 = **+4,02pp engster** ✓ | 55,06 ✓ | -0,64pp |
| JPM | 362,15 | **+0,66 Best** | **+8,83 Best** | **+18,26 %** (Thr 306,16) | +13,31 % via 363,08 (Thr 319,51) | 338,50>313,22 = +8,07pp ✓ | 66,52 ✓ | +3,09pp |

### V-Trigger-Zusammenfassung
- **V1 Std:** alle 5 SICHER
- **V2:** ⚠️ UNH BROKEN Puffer -0,78 % (Wick-DQF 12. Tag) — Alt-V2 via 437,13 = +4,63 % SICHER + Std-V1 +8,94 % primär → Rule 5 No-Action, Owner-Entscheidung pending seit Midday-Push
- **V3/V4:** max P/L JPM +8,83 % << 20 %-TP1, kein Trigger
- **V5:** alle 5 Golden Cross intakt (V engster +4,02 pp positiv)
- **V6:** alle 5 SICHER (max RSI JPM 66,52 << 80)
- **Sell-Order für Mi 12.08.:** KEINE (0 offene Orders)

### Kaufsignal-Scan KW33 Tag 2 EOD
- Slot 1/2 + 2/2 OFFEN, 0/2 Käufe bisher — Perplexity nicht durchgeführt (Silence-Rule Effizienz)

### Watchlist Mi 12.08. K1-K5 aus Alpaca IEX EOD Di 11.08.
| Sym | Prio | Sektor | Close | K1 EMA-Gap | K2 RSI | K3 RS_63d | K4 Vol% Avg20 | Status |
|-----|------|--------|-------|------------|--------|-----------|---------------|--------|
| MRK | 1 | XLV | 130,335 | +11,22 % ✓ | 58,05 ✓ | +12,87 pp ✓ | 64 % FAIL | K1-K3 ✓ **LEVEL 0 SKIP XLV-Cap** |
| UAL | 2 | XLI | 126,18 | +12,96 % ✓ | 53,18 ✓ | **+26,33 pp #1** ✓ | 73 % FAIL 9. Tag | K1-K3 ✓ K4 persistent FAIL |
| UNP | 3 | XLI | 292,74 | +9,54 % ✓ | 53,35 ✓ | +6,91 pp ✓ | 38 % heavy FAIL | K1-K3 ✓ K4 FAIL |
| PANW | 4 | XLK | 383,79 | +31,30 % ✓ | 69,57 upper ✓ | +75,35 pp ✓ | 52 % FAIL | K1-K3 ✓ XLK-Konflikt AAPL |
| BAC | Backup | XLF | 63,99 | +10,41 % ✓ | **70,26 FAIL** | +22,40 pp ✓ | 56 % FAIL | K2 knapp >70 REJECT |
| NVDA | REJECT | XLK | 217,45 | +7,55 % ✓ | 57,94 ✓ | -5,15 pp FAIL | 89 % FAIL | K3 NEG persistent |
| GS | REJECT | XLF | 1033,87 | +12,29 % ✓ | 47,58 <50 FAIL | +5,14 pp | 78 % FAIL | K2 FAIL persistent |

**Watchlist morgen:** MRK (K1-K3 stark, XLV-Cap-Blocker), UAL (K3 #1 RS_63d +26,33 pp), UNP (K1-K3 solide), PANW (starkes Momentum aber XLK-Konflikt), BAC (K2 marginal FAIL — Watch bei RSI-Cool-down)

### Sektor-Struktur EOD
- XLV **20,09 %** (UNH 10,01 + LLY 10,08 verbessert vs Midday 20,20 %)
- XLF **11,29 %** (JPM 1,13 + V 10,16 marginal verbessert vs Midday 11,26 %)
- XLK **9,80 %** (AAPL marginal verschlechtert vs Midday 9,83 %)
- Cash 58,82 %

### Guardrails
- 8/8 GRÜN + 2 WARN (LLY BO letzte Session ENDET Ende Di → ab Mi Std-V1 primär; **UNH V2 BROKEN -0,78 % via 52w-Wick 460,95 DQF 12. Tag persistent** — Std-V1 +8,94 % + Alt-V2 +4,63 % primär sicher, Owner-Entscheidung pending seit Midday-Push)
- Daily/Weekly/DD/Crash/VIX/Positions 5/8/Käufe-Slot 2/2 alle sicher
- Weekly Loss Cap Check: -0,110 % vs Cap -5 % — GRÜN, kein Auslöser

### Notification & ClickUp
- ClickUp Prio 3 Tagesbericht [CLOSE] Task erstellen — falls ITEM_246-Fehler persistent 12. Tag → Fallback Memory-Only
- KEINE neue PushNotification (Silence-Rule Routine, Owner erhielt Midday-Push mit UNH V2-Wick-Optionen — Close liefert keine neue Entscheidungsgrundlage)

### Nächste Routine
- Mi 12.08. 08:30 ET Pre-Market KW33 Tag 3
- LLY BO-Ende → Umstellung auf Standard-V1 primär
- UNH V2-Wick-DQF-Verlauf (Owner-Entscheidung pending)
- AAPL V2-Wick-Erosion-Watch (+0,55 % razor-thin)
- Watchlist MRK/UAL/UNP/PANW K4-Vol-Rebound-Check

---

## Market Open 09:47 ET — 2026-08-11 (Di, KW33 Tag 2) — Daily -0,021 % GRÜN / Alpha +0,026 pp POS marginal / DD -3,321 % GRÜN / Weekly KW33 Tag 2 +0,239 % GRÜN / Kauf-Slots KW33 0/2 OFFEN

### Alpaca /v2/account Live 09:47 ET
- portfolio_value/equity: **96.743,52 $** | last_equity: 96.763,84 $
- Daily P/L: **-20,32 $ = -0,021 %** [GRÜN, Cap -3 %, marginal verbessert vs Pre -0,057 %]
- cash: 56.707,49 $ (**58,62 %**, unverändert)
- long_market_value: **40.036,03 $** (5 Pos, -20,80 vs Mo Close 40.056,83 = **-0,052 %** marginal-flat)
- buying_power: 338.930,83 $ | 0 pending orders | status ACTIVE | trading_blocked false

### SPY Live 09:47 ET (Alpaca latestTrade IEX)
- SPY 772,66 vs Mo Close 773,02 (Alpaca Daily-Bar) = **-0,047 % essentiell flat** [Crash-Filter INAKTIV; Mo -0,018 %]
- **Alpha vs Portfolio: +0,026 pp POSITIV marginal** (Portfolio -0,021 % vs SPY -0,047 %) — Wende vs Pre -0,238 pp NEG via JPM/LLY-Recovery

### Positions V1/V2 Live-Check (V5/V6 NICHT geprüft — nur Close-Vollcheck)
| Sym | Cur | chg | P/L% | V1-Puffer Std | V2-Puffer (Wick*0,88) | Status |
|-----|-----|-----|------|---------------|------------------------|--------|
| AAPL | 306,32 | **-0,51 % Worst** | -3,33 | **+5,08 % ENGSTE Std** (Thr 291,51 primär) | +1,03 % via Wick 344,56 (Thr 303,21) marginal reduziert vs Pre +1,76 % | SICHER (Std-V1 primär) |
| V    | 361,50 | +0,04 % | +1,21 | +10,01 % (Thr 328,60) | +9,85 % via 373,97 (Thr 329,09) | SICHER |
| UNH  | 408,21 | -0,24 % | +1,65 | +10,49 % (Thr 369,44) marginal reduziert vs Pre +10,65 % | **+0,63 % RAZOR-THIN via 460,95 (Thr 405,64)** DQF persistent marginal reduziert vs Pre +0,78 % | SICHER V2-Watch |
| LLY  | 1236,35 | +0,36 % | +3,55 | +12,56 % Std verbessert vs Pre +11,93 % (Blackout-V1_neu 1134,20 Puffer +9,01 % **letzte Session heute**) | +12,53 % via 1248,53 (Thr 1098,71) | SICHER BO endet Ende Di |
| JPM  | 362,49 | **+0,75 % Best** | **+8,93 Best** | **+18,40 %** (Thr 306,16) | +12,67 % via 365,59 (Thr 321,72) | SICHER |

### V3/V4 kein Trigger
- max P/L JPM +8,93 % << 20 %-TP1

### Kaufsignal-Scan Slot 1/2 KW33 — Watchlist 6 Kandidaten (~18 min Session-Elapsed 4,62 %, K4-Linear-Pace-Threshold ≥5,54 % Prev-Full-Day-Vol für ≥120 % Avg20-Extrapolation)
- **UAL (XLI) Prio 1 REJECT K4-FAIL 8. Tag persistent**: 125,37 chg +1,31 % Recovery, IEX-Vol 6.485 = 4,30 % prev-Full-Day 150.664 (Extrapolation ~93 % Avg20) → **Downgrade Prio Backup KW34 bleibt**
- **UNP (XLI) Prio 2 REJECT K4-FAIL heavy**: 293,635 chg +0,51 %, IEX-Vol 1.773 = 3,27 % prev-Full-Day 54.224
- **BAC (XLF) Prio 3 REJECT K4-Undershoot borderline**: 64,215 chg +0,52 %, IEX-Vol 75.491 = 5,41 % prev-Full-Day 1.395.399 (Extrapolation ~117 % Avg20 knapp unter 120 %); K1-K3 ✓ (RS #1 +19,76 pp) → **Watch Midday für Vol-Pace-Anzug**
- **MRK (XLV) Prio 4 Alt REJECT XLV-Sektor-Cap-LEVEL-0-SKIP**: 132,73 chg +1,40 %, IEX-Vol 25.988 = **21,62 %** prev-Full-Day 120.228 → **K4 STRONG BEAT ~468 % Avg20 4,68x Linear-Pace (wahrscheinlich News-Catalyst)**; K1-K3 ✓ vorbekannt aber **LEVEL 0 SKIP: XLV UNH 10,13 + LLY 10,22 = 20,35 % + MRK ~10 % würde XLV auf ~30,35 % pushen → verletzt strategy.md TABU >3 Pos/Sektor + max 30 % Sektorgewicht**. MRK nur handelbar bei UNH/LLY-Reduzierung
- **PANW (XLK) REJECT K2 RSI 70,34 overheated vorbekannt Mo Close**: 379,65 chg -1,41 %, IEX-Vol 18.149 = 10,41 % prev-Full-Day (K4 STRONG PASS aber K2-FAIL)
- **NVDA (XLK) Backup REJECT K3-NEG -3,75 pp + XLK-Konflikt AAPL**: 220,265 chg +1,28 %, IEX-Vol 339.652 = 7,40 % prev-Full-Day (K4-Pass aber K3-FAIL persistent)
- **BLOCKIERT bleiben**: GS/AMD/MU/ABBV (K2 <50), CVS (K2 31,61), EOG/COP/XOM (K3 NEG), ORCL (K1 Death-Cross)

### Sektor-Struktur Live
- XLV **20,35 %** (UNH 10,13 + LLY 10,22 marginal erhöht vs Pre 20,32 %)
- XLF **11,21 %** (JPM 1,12 + V 10,09 marginal erhöht vs Pre 11,15 %)
- XLK **9,82 %** (AAPL leicht reduziert vs Pre 9,89 %)
- Cash 58,62 %

### Guardrails
- 8/8 GRÜN + 1 WARN (LLY BO letzte Session +9,01 % Bull-Konvention intakt endet Ende Di; **UNH V2 razor-thin +0,63 % via 52w-Wick 460,95 DQF persistent marginal reduziert vs Pre +0,78 %** — Std-V1 +10,49 % primär sicher, Watch Midday)
- Daily/Weekly/DD/Crash/VIX/Positions 5/8/Käufe-Slot 2/2 alle sicher

### MRK Vol-Spike-Notiz
- 21,62 % prev-Full-Day bei ~18 min Session = 4,68x Linear-Pace-Threshold → wahrscheinlich News-Catalyst
- XLV-Sektor-Cap bleibt Blocker unabhängig vom Signal-Trigger
- Midday: Perplexity 1 Symbol-Query zur Ursachen-Klärung (optional, low-cost)

### Entscheidungen
- **Kein V1-V4-Trigger** → keine Sell-Order platziert
- **Kein Kauf ausgeführt** (6/6 Watchlist-Kandidaten REJECT — MRK XLV-blockiert trotz K4 STRONG BEAT, Rest K4-FAIL oder K2/K3-FAIL)
- Slot 1/2 KW33 offen → **Midday Re-Check** BAC-K4-Watch (borderline) + MRK-News-Klärung
- Keine offenen Orders für heute platziert
- Guardrail-Status: **GRÜN**
- KEINE PushNotification (Silence-Rule: kein V/Cap-Trigger, positive Alpha marginal, DD verbessert, alle V-Signale sicher, kein Handlungsbedarf)

---

## Pre-Market 08:30 ET — 2026-08-11 (Di, KW33 Tag 2) — Daily -0,057 % GRÜN / DD -3,354 % GRÜN / Weekly KW33 Tag 2 +0,204 % GRÜN / Kauf-Slots KW33 0/2 OFFEN

### Alpaca /v2/account Pre 08:30 ET
- equity Pre: **96.709,13 $** | last_equity: 96.763,84 $ → Daily **-54,71 $ (-0,057 %)** [GRÜN, Cap -3 %]
- Cash 56.707,49 $ (58,64 %) unverändert | MV Pre **40.001,64 $** (5 Pos, -55,19 vs Mo Close 40.056,83 = -0,138 % marginal-flat)
- ATH 100.066,47 → DD **-3,354 %** [GRÜN, marginal verschlechtert vs Mo Close -3,300 %]
- Weekly KW33 Tag 2 vs Fr Close 96.512,65 = **+0,204 %** [GRÜN, weit von Cap -5 %]

### Markt-Kontext Pre 08:30 ET
- **VIX: 15,51** [GRÜN, weit von 30-Cap; leicht höher vs Mo 14,90]
- **SPY: 774,42 Alpaca-Mid** (ap 774,47 / bp 774,37 Spread 0,10) vs Mo Close 773,02 = **+0,181 % positiv-flat** [Crash-Filter INAKTIV]
- **Alpha vs SPY -0,238 pp NEG marginal** (Portfolio -0,057 % vs SPY +0,181 %)
- **10Y Treasury: n/a** (Perplexity keine Daten geliefert)
- **Makro heute: Existing Home Sales 14:00 ET** (Perplexity 1 Quelle; keine Fed/CPI/Jobs/PPI)
- **⚠️ Perplexity teilweise leer** — nur VIX konkret, SPY/Treasury/Makro-Details fehlen; Alpaca bindend für Preise (5. Mal in Serie Data-Quality-Flag)

### Positions V1/V2 Pre-Check (V5/V6 werden bei Pre NICHT geprüft — nur Open + Close)
| Sym | Cur | chg_today | P/L% | V1-Puffer Std | V2-Puffer (Wick*0,88) | Status |
|-----|-----|-----------|------|---------------|------------------------|--------|
| AAPL | 308,53 | +0,088 % | -2,63 | **+5,84 % ENGSTE Std** | +1,76 % via 344,56 | SICHER (Std-V1 primär) |
| V    | 359,66 | -0,459 % | +0,70 | +9,44 % | +9,29 % via 373,97 | SICHER |
| UNH  | 408,80 | +0,015 % | +1,80 | +10,65 % | **+0,78 % RAZOR-THIN via 460,95** DQF persistent | SICHER V2-Watch |
| LLY  | 1229,35 | -0,210 % | +2,97 | +11,93 % (Blackout-V1_neu 1134,20 Puffer +8,39 % **letzte Session heute**) | +11,89 % via 1248,53 | SICHER BO endet heute |
| JPM  | 360,13 | +0,094 % | **+8,22 Best** | +17,63 % | +12,44 % | SICHER |

### Earnings-Blackout Check (3 Handelstage)
- **AAPL/JPM/LLY/UNH/V: NONE** (Perplexity)
- **Watchlist UAL/UNP/BAC/MRK: NONE** (Perplexity)
- LLY Blackout HT+2 endet **heute Di 11.08.** (letzte Session per Bull-Konvention)

### Guardrails
- 8/8 GRÜN + 1 WARN (UNH V2 razor-thin +0,78 % via 52w-Wick 460,95 Data-Quality-Flag persistent; LLY BO endet heute — ab Mi 12.08. Standard-V1 primär)
- Daily/Weekly/DD/Crash/VIX/Positions 5/8/Käufe-Slot 2/2 alle sicher

### Watchlist Kaufscan Market Open (Slot 1/2 KW33 OFFEN)
- **UAL Prio 1 XLI** (Mo Close 123,75; K1 +11,84 % ✓; K2 RSI 50,15 borderline ✓; K3 RS_63d +19,48 pp #2 ✓; K4-Vol-Rebound-Watch Di kritisch nach K4-FAIL 7. Tag in KW32; K5 vorbekannt ✓ RevGr 16 % FwdPE 14,8x)
- **UNP Prio 2 XLI** (292,15; K1 +9,94 % ✓; K2 RSI 52,64 ✓; K3 RS +5,63 pp ✓; K4-Vol-Rebound-Watch Di)
- **BAC Prio 3 XLF** (63,88; K1 +9,29 % ✓; K2 RSI 69,79 upper-border ✓; K3 RS +19,76 pp #1 ✓; K4/K5 Di prüfen; XLF-Konflikt V/JPM sub-30 %)
- **MRK Prio 4 XLV Alt** (130,90; K1 +12,20 % ✓; K2 RSI 59,85 ✓; K3 RS +12,74 pp ✓; XLV-Konflikt UNH+LLY 20,3 % → nur bei UNH/LLY-Reduzierung)
- **REJECTS/BLOCKIERT bleiben**: PANW/NVDA (K3), GS (K2), AMD/MU/ABBV/CVS (K2), EOG/COP/XOM (K3), ORCL (K1)

### Entscheidung
- **Kein V1-V4-Trigger** → keine Sell-Order platziert
- **Kaufscan Market Open JA** (VIX GRÜN 15,51, kein Cap, Slots 2/2 offen)
- Guardrail-Status: **GRÜN**

---

## Market Close 16:00 ET — 2026-08-10 (Mo, KW33 Tag 1 FINAL) — Daily +0,236 % / Alpha +0,254 pp POS / DD -3,300 % GRÜN / Weekly KW33 Tag 1 +0,261 % GRÜN / Kauf-Slots KW33 0/2 OFFEN

### Alpaca /v2/account Close 16:00 ET
- equity Close: **96.764,32 $** | last_equity: 96.536,38 $ → Daily **+227,94 $ (+0,2361 %)** [GRÜN, Cap -3 %, deutlich verbessert vs Midday +0,028 %]
- Cash 56.707,49 $ (58,60 %) unverändert | MV Close **40.056,83 $** (5 Pos, +251,67 vs Fr Close 39.805,16 = +0,632 %)
- ATH 100.066,47 → DD -3,300 % [GRÜN, verbessert vs Midday -3,501 %]
- Weekly KW33 Tag 1 vs Fr Close 96.512,65 = **+0,261 %** [GRÜN, weit von Cap -5 %]

### SPY & Alpha
- SPY Close 773,02 Alpaca Daily-Bar IEX vs Fr Close 773,16 = **-0,018 % essentiell flat** [Crash-Filter INAKTIV]
- Alpha vs SPY = **+0,254 pp POSITIV** (Portfolio +0,236 % vs SPY -0,018 %)

### Positions V1-V6 Vollcheck (5 SICHER, kein Trigger, keine Sell-Order für Di 11.08.)
| Sym | Now | P/L% | V1-Puffer% | V2-Puffer% | RSI | EMA50>200 | RS_4w vs SPY | Status |
|-----|-----|------|------------|------------|-----|-----------|--------------|--------|
| AAPL | 307,90 | -2,83 | +5,62 ENGSTE | +1,55 razor-thin (Wick 344,56) | 44,03 | 309,81>279,00 ✓ | -6,12 pp | SICHER (V6 UND-Bedingung) |
| V    | 361,36 | +1,17 | +9,97 | +9,80 (373,97) | 53,94 | 349,26>337,39 ✓ engster | -2,14 pp | SICHER |
| UNH  | 409,18 | +1,90 | +10,76 | **+0,87 RAZOR-THIN** (Wick 460,95) | 45,23 | 407,51>360,63 ✓ | -7,92 pp | SICHER V2-Watch |
| LLY  | 1231,94 | +3,19 | +12,16 (Blackout-V1_neu 1134,20 Puffer +8,62 %) | +12,13 (52w High 1248,53) | 60,73 | 1145,49>1013,77 ✓ | +0,78 pp | SICHER BO letzte Session |
| JPM  | 359,79 | **+8,12 Best** | +17,52 | +12,63 | 64,87 | 337,53>315,57 ✓ | +4,37 pp | SICHER |

### Sektor-Struktur EOD
- XLV **20,33 %** (UNH 10,15 + LLY 10,19)
- XLF **11,20 %** (JPM 1,12 + V 10,08)
- XLK **9,86 %** (AAPL)
- Cash 58,60 %

### Watchlist morgen (Di 11.08. KW33 Tag 2)
- **UAL Prio 1 XLI** (123,75; K1 +11,84 %; K2 RSI 50,15; K3 RS_63d +19,48 pp #2; K4 Vol-Rebound-Watch Di; K5 vorbekannt ✓ RevGr 16 % FwdPE 14,8x; XLI 0 % Diversifikation)
- **UNP Prio 2 XLI** (292,15; K1 +9,94 %; K2 RSI 52,64; K3 RS +5,63 pp; K4 Vol-Rebound-Watch Di)
- **BAC Prio 3 XLF** (63,88; K1 +9,29 %; K2 RSI 69,79 upper-border; K3 RS **+19,76 pp #1**; K4/K5 Di prüfen; XLF-Konflikt V/JPM sub-30 %)
- **MRK Prio 4 XLV Alt** (130,90; K1 +12,20 %; K2 RSI 59,85; K3 RS +12,74 pp; XLV-Konflikt UNH+LLY 3-Pos-nah — nur bei UNH/LLY-Reduzierung)
- **REJECTS**: PANW (K2 RSI 70,34 overheated), NVDA (K3 -3,75 pp), GS (K2 RSI 47,58 <50)
- **BLOCKIERT**: AMD/MU/ABBV (K2 <50), CVS (K2 31,61), EOG/COP/XOM (K3 NEG), ORCL (K1 Death-Cross)

### Guardrails
- 8/8 GRÜN + 1 WARN (LLY BO HT+2 heute letzte Session Bull-Konvention intakt Ende morgen Di 11.08.; UNH V2 razor-thin +0,87 % Watch für Di)
- Weekly Loss Cap KW33 Tag 1: +0,261 % vs Fr Close → weit von -5 %; keine Order-Storno-Bedingung

### Perplexity-Halluzination 4. Mal in Serie (Data-Quality-Flag)
- Perplexity: SPY +0,61 %, Sektoren "+?" leere Werte
- Alpaca IEX Daily-Bar authoritative: SPY 773,02 vs 773,16 = -0,018 %
- Perplexity-Antwort verworfen; Alpaca ist bindende Live-Source

### Entscheidungen für Di 11.08.
- Kaufsignal-Scan Slot 1/2 KW33 offen: Watchlist UAL/UNP/BAC/MRK K4-Vol-Rebound-Check Pre + Open
- LLY Blackout endet Di → V1-Threshold zurück auf Standard 1.098,38 (Puffer +12,16 %)
- UNH V2-Wick-Puffer-Watch (+0,87 % razor-thin — kritisch bei weiterem -1 %+ Drift)
- AAPL V2-Wick-Puffer-Verlauf (+1,55 % via Recovery — Watch)
- Keine offenen Orders für Di 11.08. platziert

---

## Market Open 09:44 ET — 2026-08-10 (Mo, KW33 Tag 1) — Daily -0,015 % / Alpha +0,015 pp POS marg / DD -3,542 % GRÜN / Weekly KW33 Tag 1 +0,010 % GRÜN / Kauf-Slots KW33 0/2 OFFEN

### Alpaca /v2/account Live 09:44 ET
- portfolio_value/equity: **96.522,00 $** | last_equity: 96.536,38 $
- Daily P/L: **-14,38 $ = -0,015 %** [GRÜN, Cap -3 %, marginal verbessert vs Pre -0,101 %]
- cash: 56.707,49 $ (**58,75 %**, unverändert seit 06.06.)
- long_market_value: **39.814,51 $** (5 Pos, +9,35 vs Fr Close 39.805,16 = **+0,024 %** marginal-flat)
- buying_power: 338.310,58 $ | 0 pending orders | status ACTIVE | trading_blocked false

### SPY Live 09:45 ET (Alpaca latestTrade)
- SPY 772,99 vs Fr Close 773,22 (Alpaca Daily-Bar) = **-0,030 % essentiell flat** [Crash-Filter INAKTIV; Fr +0,596 %]
- Alpha vs Portfolio: **+0,015 pp POSITIV marginal** (Portfolio -0,015 % vs SPY -0,030 %) — Wende vs Pre -0,123 pp NEG

### Position-Check Live 09:44 ET (V1-V4 Std; V5/V6 nicht Open)
| Sym | Qty | Avg | Live | P/L $ | P/L % | Day chg | V1-Std Puffer | V2 Puffer |
|-----|-----|-----|------|-------|-------|---------|---------------|-----------|
| AAPL | 31 | 316,86 | **305,92** | -339,03 | **-3,45 %** | **-2,37 % WORST** | **+4,94 % ENGSTE** (verschl. vs Pre +5,75 %) | **⚠️ +0,89 % RAZOR** via Wick 344,56 (verschl. vs Pre +1,97 %) |
| JPM | 3 | 332,78 | 359,19 | +79,23 | **+7,94 % BEST P/L** | +0,47 % | +17,32 % | sicher |
| LLY | 8 | 1.193,89 | 1.195,67 | +14,22 | +0,15 % | +0,84 % | +8,86 % Std (**Blackout-V1_neu 1.134,20 Puffer +5,42 % HT+2 heute letzte Session**) | +8,82 % via 52w-High 1.248,53 |
| UNH | 24 | 401,57 | 411,98 | +249,72 | +2,59 % | **+1,20 % Best chg** | +11,51 % | **+1,56 %** via Wick 460,95 (verbessert vs Pre +0,36 % marg recovered) |
| V | 27 | 357,18 | 362,89 | +154,23 | +1,60 % | +0,11 % | +10,43 % | +10,27 % via 373,97 |

**V1 Std alle 5 SICHER** eng→weit: AAPL +4,94 % → LLY +8,86 % → V +10,43 % → UNH +11,51 % → JPM +17,32 %
**V3/V4**: max JPM +7,94 % << 20 % kein Trigger
**V2 razor-thin**: AAPL +0,89 % verschlechtert (Wick 344,56 Thr 303,21); UNH +1,56 % verbessert (Wick 460,95 Thr 405,636)
**V5/V6 Market Open NICHT geprüft** (Vollcheck Close)
**=> KEIN V1-V4-Trigger, KEINE Sell-/Limit-Order platziert**

### Guardrails-Status 8/8 GRÜN + 2 WARN
1. Daily -3 %: -0,015 % → GRÜN
2. Weekly -5 %: +0,010 % vs Fr 96.512,65 → GRÜN
3. DD -15 %: -3,542 % vs ATH 100.066,47 → GRÜN
4. DD -20 %: -3,542 % → GRÜN
5. Crash-Filter SPY -5 %: SPY -0,030 % flat → INAKTIV
6. VIX >30: 14,90 (aus Pre) → GRÜN
7. Earnings-Blackout: **LLY HT+2 heute letzte Session — Bull-Konvention +5,42 % intakt**; Ende morgen Di 11.08.
8. Max Käufe 2/Woche: **KW33 0/2 OFFEN**

WARN 1: LLY BO letzte Session heute (Puffer intakt)
WARN 2: **AAPL V2 razor-thin +0,89 % via 52w-Wick Data-Quality-Flag** (verschlechtert vs Pre +1,97 % via chg -2,37 %; Std-V1 +4,94 % ENGSTE sicher)

### Kaufscan Watchlist (Alpaca snapshot 09:45 ET IEX-Vol Intraday-% vs prev Full-Day-Vol)
Perplexity-Sektor-Scan NICHT durchgeführt (Silence-Rule Effizienz + Perplexity-Halluzinationen 3. Mal in Serie; existierende Watchlist aus Fr Close ausreichend).

| Sym | Prio | Sektor | Live chg | IEX-Vol % prev | K1-K3 | K4 | Entscheidung |
|-----|------|--------|----------|----------------|-------|-----|--------------|
| UAL | 1 | XLI | 126,76 **-2,20 %** | 9.251 = 11,96 % | ✓ vorbek. | K4-FAIL 7. Tag + K1-Reversal | **REJECT + DOWNGRADE Prio Backup KW34** |
| UNP | 2 | XLI | 293,83 +0,24 % | 736 = 0,64 % | ✓ vorbek. | K4 heavy FAIL | REJECT |
| BAC | 3 | XLF | 63,555 +0,64 % | 95.908 = 6,59 % | ✓ vorbek. | K4-Undershoot | REJECT (Midday-Re-Check-Watch) |
| PANW | 4 | XLK | 374,82 **+3,00 %** | 12.294 = 6,60 % | ✓ vorbek. (K3 #1 +79,44 pp) | K4-Undershoot | REJECT (Midday-Re-Check-Watch, XLK-Konflikt AAPL) |
| NVDA | Backup | XLK | 223,24 -0,31 % | 223.865 = 5,14 % | K3 razor +0,16 pp | K4-Undershoot | REJECT |

**BLOCKIERT/REJECT bleiben:** GS/AMD/MU/ABBV (K2 RSI <50), CVS (K2 31,61), EOG/COP/XOM (K3 NEG), ORCL (K1 Death-Cross), MRK (XLV-Cap-Risk 3. Pos)

### Sektor-Struktur Live
- XLV **20,17 %** (UNH 10,24 + LLY 9,91 verbessert vs Pre 20,00 %)
- XLF 11,27 % (JPM 1,12 + V 10,15)
- XLK **9,83 %** AAPL leicht reduziert vs Pre 9,94 % via -2,37 %
- Cash 58,75 %

### Entscheidung
- **KEIN Trade Market Open** (V1-V4 alle SICHER, kein K1-K5-Kandidat vollständig grün heute)
- **UAL Prio 1 → Downgrade Prio Backup KW34** (7. Tag K4-FAIL + heute Momentum-Reversal -2,20 %)
- **Kaufscan Midday Re-Check**: BAC/PANW K4-Vol-Rebound-Potential (falls intraday-Vol-Pace anzieht)
- **ClickUp Prio 4 Routine-Log FEHLER ITEM_246 persistent 8. Tag** → Fallback Memory-Only per notify-skill.md
- **KEINE PushNotification** (Silence-Rule: alle V SICHER Std, kein Cap-Alert, VIX GRÜN, SPY flat, AAPL V2 razor +0,89 % innerhalb Std-V1 +4,94 % sicher, UNH V2 verbessert, LLY BO intakt, keine Portfolio-Earnings, kein Trade, kein Owner-Handlungsbedarf, positive Alpha marginal +0,015 pp, DD verbessert vs Pre; Owner erhielt Fr-Wochenschluss-Push)

### Nächste Routine
**Mo 10.08. 13:00 ET Midday Stop-Check KW33 Tag 1** — **AAPL V2-Wick-Puffer-Erosion-Watch kritisch** (+0,89 % razor-thin — bei -1 %+ Drift Escalation), UNH V2-Wick-Puffer-Verlauf, LLY letzte Blackout-Session, BAC/PANW K4-Vol-Rebound-Potential-Watch, Post-CPI-Reaktion (falls Release bestätigt)

---

## Pre-Market 08:30 ET — 2026-08-10 (Mo, KW33 Tag 1) — Daily -0,101 % / Alpha -0,123 pp NEG marg / DD -3,625 % GRÜN / Weekly KW33 Tag 1 -0,077 % GRÜN / Kauf-Slots KW33 frisch 2/2

### Alpaca /v2/account Pre
- portfolio_value/equity: **96.438,58 $** | last_equity: 96.536,38 $ (Alpaca EOD Fr, +23,73 vs Memory Close 96.512,65 = overnight/rounding-Notiz)
- Daily P/L: **-97,80 $ = -0,101 %** [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (**58,80 %**, unverändert seit 06.06.)
- long_market_value: **39.731,09 $** (5 Pos, -74,07 vs Fr Close 39.805,16 = **-0,186 %**)
- buying_power: 338.077,00 $ | 0 pending orders | status ACTIVE | trading_blocked false

### SPY Pre (Alpaca Live-Quote 08:15:24 ET)
- SPY ap 773,44 / bp 773,34 (Mid ~**773,39**, Spread 0,10)
- vs Fr Close 773,22 (Alpaca Daily-Bar) = **+0,022 % essentiell flat** [Crash-Filter INAKTIV; Fr +0,596 %]
- Alpha vs Portfolio: **-0,123 pp NEG marginal** (Portfolio -0,101 % vs SPY +0,022 %)
- **Data-Quality-Flag**: Perplexity SPY 770,91 / -0,31 % widerspricht Alpaca 773,39 / +0,022 % → Alpaca bindend, Perplexity als Halluzination verworfen (**3. Mal in Serie** nach KW32 Do 06.08. Pre + Fr 07.08. Close)

### Position-Check Pre (V1-V4 Std; V5/V6 nicht Pre)
| Sym | Qty | Avg | Live | P/L $ | P/L % | Day chg | V1-Std Puffer | V2 Puffer |
|-----|-----|-----|------|-------|-------|---------|---------------|-----------|
| AAPL | 31 | 316,86 | **309,30** | -234,34 | **-2,39 %** | **-1,29 % WORST** | **+5,75 % ENGSTE** (verschl. vs Fr Close +7,47 %) | **+1,97 % RECOVERED** via Wick 344,56 (Fr Close +0,15 % → +1,97 %) |
| JPM | 3 | 332,78 | 357,20 | +73,26 | **+7,34 % BEST P/L** | -0,09 % | +14,29 % | sicher |
| LLY | 8 | 1.193,89 | 1.190,00 | -31,10 | -0,33 % | **+0,36 % BEST chg** | +7,70 % Std (**Blackout-V1_neu 1.134,20 Puffer +4,69 % HT+2 heute letzte Session**) | +7,68 % via 52w-High 1.248,53 |
| UNH | 24 | 401,57 | 407,10 | +132,75 | +1,38 % | +0,005 % | +9,25 % | **+0,36 % razor** via Wick 460,95 = Thr 405,636 (Fr +0,12 % → Mo +0,36 % marginal recovered, Data-Quality-Flag persistent) |
| V | 27 | 357,18 | 362,25 | +136,94 | +1,42 % | -0,07 % | +9,29 % | +9,15 % via 373,97 |

**V1 Std alle 5 SICHER** eng→weit: AAPL +5,75 % → LLY +7,70 % → UNH +9,25 % → V +9,29 % → JPM +14,29 %
**V3/V4**: max JPM +7,34 % << 20 % kein Trigger
**V5/V6 Pre NICHT geprüft** (Vollcheck Close)
**=> KEIN V1-V4-Trigger, KEINE Sell-/Limit-Order platziert**

### Perplexity Macro Check
- **VIX: 14,90** [GRÜN <25, deutlich <30-Cap]
- **SPY Pre: Perplexity 770,91 / -0,31 % HALLUZINATION** (Alpaca bindend 773,39 / +0,022 %)
- **10Y Treasury: 4,65 %** (leicht rückläufig vs Fr 4,69 %)
- **Makro heute: Core CPI YoY Jul Release 08:30 ET** (Perplexity nur 1 Quelle, CPI-Release Mo Post-Jobs plausibel — Deviation-Watch)
- **Top 3 News**: (1) Fr weak Jul jobs data → Fed-Hold-Bets, (2) SPY Fr +0,6 % / VIX -14,90, (3) Pre mildly risk-on

### Earnings-Blackout-Check (Portfolio + Watchlist, nächste 3 HT Mo/Di/Mi)
- **Portfolio 5 Pos: KEINE Earnings** (UNH/JPM/V/AAPL Q3 Ende Okt; LLY Q2 04.08. → HT+2 heute letzte Blackout-Session, Ende morgen Di 11.08.)
- **Watchlist UAL/UNP/BAC/PANW/NVDA: KEINE Earnings** (Perplexity bestätigt)

### Guardrails-Status 8/8 GRÜN + 1 WARN
1. Daily -3 %: -0,101 % → GRÜN
2. Weekly -5 %: -0,077 % vs Fr 96.512,65 → GRÜN
3. DD -15 %: -3,625 % vs ATH 100.066,47 → GRÜN
4. DD -20 %: -3,625 % → GRÜN
5. Crash-Filter SPY -5 %: Fr +0,596 % → INAKTIV
6. VIX >30: 14,90 → GRÜN
7. Earnings-Blackout: **LLY HT+2 heute WARN — letzte Session** (Blackout-V1_neu 1.134,20 Puffer +4,69 % Bull-Konvention intakt; Ende morgen Di 11.08.)
8. Max Käufe 2/Woche: **KW33 frisch 2/2 OFFEN**

WARN: UNH V2 +0,36 % via 52w-Wick 460,95 Data-Quality-Flag persistent (Fr +0,12 % → Mo +0,36 % marginal recovered)

### Kaufscan Market Open: JA
- Slots frisch 2/2, VIX GRÜN 14,90, kein Cap-Alert, kein Crash-Filter, keine Portfolio-Earnings heute
- **Watchlist Mo 10.08. KW33 Tag 1** (K1-K3 aus Fr Close; K4 heute Vol-Rebound-Prüfung):
  - **UAL Prio 1 XLI** (129,59: K1 +10,7 %, K2 RSI 58,64, K3 RS_63d +24,27 pp #2, K5 ✓ RevGr 16 %+ FwdPE 14,8x) — K4-Rebound-Watch nach 7. Tag Vol-Fail-Persistenz **kritisch**
  - **UNP Prio 2 XLI** (293,13: K1 +10,0 %, K2 RSI 53,91, K3 RS +4,95 pp) — K4-Rebound
  - **BAC Prio 3 XLF** (63,15: K1 +8,6 %, K2 RSI 66,51, K3 RS +14,06 pp) — XLF-Konflikt-Watch V+JPM (11,25 % <30 %-Cap sicher)
  - **PANW Prio 4 XLK** (363,88: K1 +21,4 %, K2 RSI 64,28, K3 RS +79,44 pp #1 Momentum) — XLK-Konflikt AAPL
  - NVDA Backup (K3 razor +0,16 pp)
- **BLOCKIERT/REJECT**: GS/AMD/MU/ABBV (K2 <50), CVS (K2 31,61), EOG/COP/XOM (K2/K3 FAIL), ORCL (K1 Death-Cross), MRK (XLV-Cap-Risk 3. Position)

### Entscheidung
- **KEIN Trade Pre-Market** (V1-V4 alle SICHER)
- **Kaufscan Market Open JA** (Slots frisch 2/2 KW33)
- **ClickUp Prio 4 Routine-Log FEHLER ITEM_246 persistent 7. Tag** → Fallback Memory-Only per notify-skill.md
- **KEINE PushNotification** (Silence-Rule Routine: alle V-Std SICHER, kein Cap-Alert, VIX GRÜN, SPY flat, UNH V2 marginal recovered, AAPL V2 recovered +1,97 %, LLY BO intakt, keine Portfolio-Earnings, kein Owner-Handlungsbedarf; Owner erhielt Fr-Wochenschluss-Push)

### Nächste Routine
**Mo 10.08. 09:30 ET Market Open KW33 Tag 1** — Kaufsignal-Scan Slot 1/2 mit UAL K4-Vol-Rebound 7. Tag **kritisch** + UNP/BAC/PANW K4-Check, V1-V6 Live-Read, AAPL -1,29 % Pre-Weakness-Watch, UNH V2-Wick-Puffer-Verlauf, LLY letzte Blackout-Session, Post-CPI-Reaktion (falls Release bestätigt)

---

## Market Close 16:00 ET — 2026-08-07 (Fr, KW32 Tag 5 FINAL) — Tagesbilanz -0,188 % / Alpha -0,784 pp NEG / DD -3,552 % GRÜN / Weekly KW32 FINAL +0,551 % GRÜN

### Alpaca /v2/account EOD
- portfolio_value/equity: **96.512,65 $** | last_equity: 96.694,59 $
- Daily P/L: **-181,94 $ = -0,188 %** [GRÜN, Cap -3 %, marginal verschlechtert vs Midday -0,172 %]
- cash: 56.707,49 $ (**58,76 %**, unverändert seit Fr 06.06.)
- long_market_value: **39.805,16 $** (5 Pos, -76,96 vs Do Close 39.882,12 = -0,193 %)
- buying_power: 338.284,41 $ | 0 pending orders | status ACTIVE

### SPY Close (Alpaca Daily-Bar)
- SPY 2026-08-07 Daily-Bar: c 773,22 / h 773,915 / l 769,61 / o 771,02 / v 37.267.372 (vw 772,347)
- SPY latestTrade @ 16:00 ET: 773,16
- vs Do Close 768,64 = **+0,596 % positiv** [Crash-Filter INAKTIV]
- Alpha vs Portfolio: **-0,784 pp NEGATIV** (Portfolio -0,188 % vs SPY +0,596 %)
- **Data-Quality-Flag**: Perplexity SPY-Antwort 745,40 $ / -3,03 % widerspricht Alpaca 773,22 / +0,596 % → Alpaca bindend, Perplexity als Halluzination verworfen (2. Mal in KW32 nach Do 06.08. Pre 746,07-Halluzination)

### Position-Check EOD (V1-V6 Vollcheck)
| Sym | Qty | Avg      | Close    | P/L $    | P/L %  | Day chg  | V1-Puffer Std | V2-Puffer | RSI14 | EMA-Diff | V5 | V6 |
|-----|-----|----------|----------|----------|--------|----------|---------------|-----------|-------|----------|-----|-----|
| AAPL | 31 | 316,86   | 313,30   | -110,25  | -1,12  | +0,29 %  | +7,47 % Std_ENGSTE | +0,15 %-**razor Wick 344,56** | 47,57 | +10,49 % | ✓ | ✓ |
| JPM  | 3  | 332,78   | 357,52   | +74,22   | **+7,43 BEST** | +0,34 %  | +16,78 %      | +11,12 %  | 63,03 | +6,36 %  | ✓ | ✓ |
| LLY  | 8  | 1193,89  | 1185,71  | -65,42   | -0,68  | **-0,52 %** | +7,95 % Std (Blackout-V1_neu 1134,20 Puffer +4,54 % HT+2 heute letzte Session) | +6,42 % via 52w-High 1248,53 | 53,79 | +12,46 % | ✓ | ✓ |
| UNH  | 24 | 401,57   | 406,13   | +109,44  | +1,14  | **+0,54 % BEST chg** | +9,94 % Std | **+0,12 % RECOVERED** via 52w-Wick 460,95 = Threshold 405,636 (Data-Quality-Flag, Puffer schrumpft vs Midday +1,00 %) | 44,00 | +12,72 % | ✓ | ✓ |
| V    | 27 | 357,18   | 362,50   | +143,70  | +1,49  | **-2,15 % WORST chg** | +10,32 %      | +11,23 %  | 55,28 | **+3,29 %** engster aber positiv | ✓ | ✓ |

**V5-Vollcheck 5 SICHER** (Golden Cross alle intakt EMA50>EMA200, Alpaca IEX 278d)
**V6-Vollcheck 5 SICHER** (max RSI JPM 63,03 << 80; SPY 20d ret +2,41 %; RS_4w NEG bei 3: UNH -6,53 pp, AAPL -3,06 pp, LLY -2,63 pp — RSI aber alle <65 → V6 sicher via UND-Bedingung)
**V1 Std alle 5 SICHER** eng→weit: AAPL +7,47 % → LLY +7,95 % → UNH +9,94 % → V +10,32 % → JPM +16,78 %
**V2 Trailing-Stop**: **UNH razor-thin +0,12 % via Wick** (Data-Quality-Flag), AAPL +0,15 % razor-thin via Wick 344,56 (Threshold 303,21 vs Close 313,30), andere >6 %
**V3/V4**: max JPM +7,43 % << 20 % kein Trigger
**=> KEIN Auto-Sell, KEINE Sell-/Limit-Order für Mo 10.08.**

### Weekly-Cap-Check KW32 FINAL
- Alpaca Portfolio-History EOD: Mo 03.08 95.984,04 → Di 04.08 96.056,40 → Mi 05.08 96.641,67 → Do 06.08 96.694,59 → **Fr 07.08 96.512,65**
- **Weekly P/L vs Mo 03.08 EOD = +0,551 %** [GRÜN, weit von Cap -5 %]
- Alt-Referenz vs Fr 31.07. Close 96.396,66 = +0,120 %
- => Kein Weekly-Cap-Alarm, keine Cancel-Aktion

### Watchlist Mo 10.08. KW33 Tag 1 (K1-K3 aus Alpaca IEX EOD Fr 07.08., SPY 63d Return +5,69 %)
| Sym | Sektor | Last  | K1 EMA50>EMA200 | K2 RSI 50-70 | K3 RS_63d vs SPY | Verdikt |
|-----|--------|-------|-----------------|--------------|------------------|---------|
| **UAL** | XLI | 129,59 | ✓ +10,7 % | ✓ 58,64 | ✓ **+24,27 pp #2** | **Prio 1 K4-Rebound-Watch Mo, K5 vorbekannt ✓ (RevGr 16 %, FwdPE 14,8x)** |
| **UNP** | XLI | 293,13 | ✓ +10,0 % | ✓ 53,91 | ✓ +4,95 pp | **Prio 2 K4-Rebound-Watch Mo** |
| **BAC** | XLF | 63,15 | ✓ +8,6 % | ✓ 66,51 upper | ✓ +14,06 pp | **Prio 3 XLF-Konflikt-Watch mit V+JPM (aber 11,26 % <30 %-Cap)** |
| **PANW** | XLK | 363,88 | ✓ +21,4 % | ✓ 64,28 | ✓ **+79,44 pp #1 Momentum** | **Prio 4 XLK-Konflikt-Watch mit AAPL** |
| NVDA | XLK | 223,93 | ✓ +5,1 % | ✓ 64,32 | ✓ +0,16 pp razor | Backup XLK-Konflikt AAPL |

**BLOCKIERT/REJECT:** GS/AMD/MU/ABBV (K2 RSI <50), CVS (K2 RSI 31,61 heavy), EOG (K2+K3 FAIL), COP/XOM (K3 NEG), ORCL (K1 Death-Cross + K3 heavy), MRK K1-K3 ✓ aber **XLV-Sektor-Cap-Risk 3 Positionen** (UNH+LLY bereits 2/3).

### Guardrails-Status 8/8 GRÜN + 1 WARN
1. Daily -3 %: -0,188 % → GRÜN
2. Weekly -5 %: +0,551 % (vs Mo) → GRÜN
3. DD -15 %: -3,552 % → GRÜN
4. DD -20 %: -3,552 % → GRÜN
5. Crash-Filter SPY -5 %: +0,596 % → INAKTIV
6. VIX >30: geerbt <25 → GRÜN
7. Earnings-Blackout: **LLY HT+2 heute WARN** (letzte Session, Ende Mo 10.08.; Blackout-V1_neu 1.134,20 Puffer +4,54 % ÜBERSCHRITTEN Bull-Konvention intakt)
8. Max Käufe 2/Woche: **KW32 FINAL 0/2** (letzter HT heute — beide Slots VERFALLEN)

### Entscheidung
- **KEIN Trade heute** (Slot 1/2 + 2/2 KW32 FINAL 0/2 — letzter HT vorbei)
- **KEINE Pending-Sell-Order für Mo 10.08.** (V5/V6 alle 5 SICHER; V1-V4 alle SICHER)
- **UNH V2-Puffer +0,12 % Watch** — Data-Quality-Flag via Wick 460,95 persistent, morgen Wochenende, Mo Recovery-Watch
- **AAPL V2-Puffer +0,15 % razor-thin** via Wick 344,56 (Threshold 303,21 vs Close 313,30 — sicher aber engster V2 nach UNH)
- **LLY Blackout endet Mo 10.08.** (HT+2 heute letzte Session)
- **ClickUp CRIT-Alert FEHLER ITEM_246 persistent 6. Tag** → Memory-Only Fallback + PushNotification an Owner
- **PushNotification JA**: Wochen-Bilanz KW32 FINAL + UNH V2-Wick-Puffer-Erosion Mo-Watch + KW32-0-Käufe-Result — Owner-Interesse plausibel

### Nächste Routine
**Mo 10.08. 08:30 ET Pre-Market KW33 Tag 1** — KW33 Kauf-Slots frisch 2/2, Watchlist UAL/UNP/BAC/PANW K4-Vol-Rebound-Check, LLY BO Ende Mo, UNH V2-Wick-Recovery-Watch, AAPL V2-Wick-Puffer-Watch

---

## Market Open 09:50 ET — 2026-08-07 (Fr, KW32 Tag 5) — Daily -0,261 % / Alpha -0,621 pp NEGATIV / DD -3,623 % GRÜN / Weekly +0,047 % GRÜN

### Alpaca /v2/account Live
- portfolio_value: **96.441,67 $** | equity: 96.441,67 $ | last_equity: 96.694,59 $
- Daily P/L: **-252,92 $ = -0,261 %** [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (**58,80 %**, unverändert)
- long_market_value: **39.734,18 $** (5 Pos, -147,94 vs Do Close 39.882,12 = **-0,371 %**)
- buying_power: 338.085,66 $ | 0 pending orders

### SPY Live (Alpaca latestTrade 09:47 ET)
- SPY 771,40 vs Do Close 768,64 = **+0,359 % positiv-flat**
- Alpha vs Portfolio: **-0,621 pp NEGATIV** (Portfolio -0,261 % vs SPY +0,359 %)
- Crash-Filter Do vs Mi: -0,149 % INAKTIV

### V1-V4 Live-Check (RSI/EMA nicht Open-Check)
- **⚠️ UNH V2 TECHNISCH GETRIGGERT**: cur 404,55 < V2-Threshold 405,636 (52w-Wick 460,95 * 0,88) Puffer -0,27 % BROKEN — Data-Quality-Flag persistent (Wick 16.07. intraday, Close-Peak 436,39 → -7,30 % vs Close-Peak << -12 % Zielintent). **Rule 3 (Strategie-Lock 460,95 wörtlich) vs Rule 5 (No-Action bei Unsicherheit)** → KEIN Auto-Sell, PushNotification CRITICAL an Owner
- **V1 Std alle 5 SICHER** (eng→weit): AAPL +7,00 % ENGSTE, LLY +7,07 % (Blackout-V1_neu 1.134,20 Puffer +3,69 % HT+2 heute), UNH +9,51 %, V +11,39 %, JPM +15,80 %
- **V3/V4 max JPM +6,54 %** << 20 % kein Trigger
- **=> KEIN Auto-Sell** (UNH V2-Wick-Trigger per Rule 5 eskaliert, kein anderer V-Trigger)

### Kaufsignal-Scan Slot 1/2 KW32 Fr — alle REJECT/SKIP
| Symbol | Sektor | K1 | K2 | K3 | K4 | K5 | Verdikt |
|--------|--------|----|----|----|-----|----|---------|
| UAL | XLI | ✓ +10,6 % | ✓ RSI 63,9 | ✓ **+35,3 pp #1 XLI** | **FAIL 6. Tag** persistent | ✓ FwdPE 14,8x | **REJECT K4 Downgrade Prio Backup KW33** |
| GS | XLF | ✓ | ✓ RSI 52,1 | ✓ +9,1 pp | **FAIL** Vol low | K5 unverifiziert | REJECT K4 |
| DELL | XLK | **FAIL K1-Bruch anhaltend** | – | – | – | – | REJECT K1 |
| HPE | XLK | **FAIL K1-Bruch anhaltend** | – | – | – | – | REJECT K1 |
| UNP | XLI Backup | ✓ | ✓ RSI 57,0 | ✓ +5,6 pp | **FAIL heavy** | – | REJECT K4 |
| NVDA | XLK | ✓ | ✓ | +5,2 pp marginal | FAIL | – | REJECT K3+XLK-Konflikt AAPL |

**BLOCKIERT:** GE (K5 FwdPE 44,72), MSFT/META (K1+K2 FAIL), ORCL (K1 FAIL), AMZN/GOOGL/AVGO (K3 NEG)

**Slot 1/2 + 2/2 KW32 bleibt OFFEN — KW32 endet mit 0/2 Käufen** (Fr letzter HT).

### Guardrails-Status 8/8 GRÜN + 2 WARN
1. Daily -3 %: -0,261 % → GRÜN
2. Weekly -5 %: +0,047 % → GRÜN
3. DD -15 %: -3,623 % → GRÜN
4. DD -20 %: -3,623 % → GRÜN
5. Crash-Filter: SPY Do -0,149 % → INAKTIV
6. VIX >30: geerbt ~16-18 (Pre gestern), heute nicht geprüft → GRÜN
7. Earnings-Blackout: **LLY HT+2 heute WARN** (Blackout-V1_neu 1.134,20 Puffer +3,69 % ÜBERSCHRITTEN Bull-Konvention intakt; Ende Mo 10.08.)
8. Max Käufe 2/Woche: **0/2 KW32 OFFEN** (heute Fr letzter Handelstag)

WARN #2: **UNH V2 -0,27 % BROKEN via Wick Data-Quality-Flag → CRIT-Alert eskaliert**

### Entscheidung
- **KEIN Trade heute** (kein Kaufkandidat erfüllt alle K1-K5; alle Watchlist REJECT/SKIP)
- **KEIN Auto-Sell UNH** (V2-Wick-Trigger per Rule 5 eskaliert, Owner-Decision erforderlich)
- **Käufe KW32 endet 0/2** (Fr letzter HT)
- **ClickUp CRIT-Alert FEHLER ITEM_246 persistent 6. Tag** → Memory-Only Fallback + PushNotification an Owner (kompensiert ClickUp-Ausfall)
- **PushNotification CRITICAL gesendet** (UNH V2 Wick-Trigger, Owner-Decision — Ausnahme Silence-Rule wegen Handlungsbedarf)

### Nächste Routine
**Fr 07.08. 13:00 ET Midday Stop-Check KW32 Tag 5** — UNH V2-Status-Watch (Owner-Antwort), LLY HT+2 letzte Blackout-Session, V-Give-back-Erosion-Watch

---

## Pre-Market 08:30 ET — 2026-08-06 (Do, KW32 Tag 4) — Daily +0,234 % / Alpha +0,077 pp POSITIV / DD -3,196 % GRÜN / Weekly +0,489 % GRÜN

### Alpaca /v2/account Pre
- portfolio_value: **96.867,82 $** | equity: 96.867,82 $ | last_equity: 96.641,67 $
- Daily P/L: **+226,15 $ = +0,234 %** [GRÜN, Cap -3 %]
- vs Memory Wed Close 96.589,61 = **+278,21 $ = +0,288 %** (last_equity-Diff +52,06 $ overnight/AH — Notiz, keine Aktion)
- cash: 56.707,49 $ (**58,54 %**, unverändert)
- long_market_value berechnet: **40.160,33 $** (5 Pos, +278,21 vs Wed Close 39.882,12 = **+0,698 %**)
- buying_power: 339.278,89 $ | status: ACTIVE | trading_blocked: false

### SPY Pre-Market (Alpaca Data)
- latestTrade: **771,00 $** @ 08:35:42 ET (Ex V, size 100)
- latestQuote: ap 771,05 / bp 770,93 (Spread 0,12)
- prevDailyBar (Tue 04.08): c 771,11 | dailyBar (Wed 05.08): c 769,79
- **SPY Pre vs Wed Close: +0,157 % flat/positiv**
- Alpha vs Portfolio: **+0,077 pp POSITIV** (Portfolio +0,234 % vs SPY +0,157 %)
- Crash-Filter Wed vs Tue: -0,171 % << -5 % Trigger → **INAKTIV**
- ⚠️ **Perplexity SPY Pre 746,07 als HALLUZINATION VERWORFEN** (widerspricht Alpaca-Live + eigener Equity-Positivität; Alpaca-latestTrade bindend per Data-Quality-Rule)

### VIX (Perplexity Multi-Query 3 Quellen)
- Query 1: **12,18** (frühe Trades Do 06.08.)
- Query 2: Range 16-19, letzt explizit **17,98** (Jul 30 12:27 CDT)
- Query 3: **VIX Wed Close 21,51 / Pre-Thu 16,50**
- ⚠️ 3-Quellen-Divergenz → konservativ **Best-Estimate ~16-18** [GRÜN <25, deutlich <30-Cap]

### 10Y Treasury Yield
- **~4,69 %** (Perplexity letzt verfügbar Aug 3, 2026)

### Makro-Events heute (Do 06.08.2026)
- **US Initial Jobless Claims** Woche endend 01.08. **Release heute 08:30 ET** (Consensus 221k, Prior 197k) — Deviation >±10k = Markt-Reaktion Watch
- Keine großen Portfolio-Position-Earnings heute
- Perplexity fand keine Mega-Cap Earnings-Blockbuster für Do 06.08.

### Top marktbewegende News (letzte 24h)
- Perplexity lieferte keine konkrete Top-3-News-Rangliste (Multiple Query-Attempts) — Quellenlage schwach
- LLY Q2-Beat (gestern BMO) noch dominante Story: EPS $8,38 vs Konsens $6-7,74 (Beat +25-35 %), Rev $22,97 Mrd, Guidance angehoben Rev 2026 $85-87 Mrd

### Earnings-Blackout Check (Nächste 3 HT vs Portfolio)
- **LLY HT+1 heute Do 06.08.** → **HT+2 Fr 07.08.** → **Ende Mo 10.08.**
- Std-V1 1.098,38 $ + Blackout-V1_neu 1.134,20 $ (Bull-Konvention intakt Puffer +2,64 % aus Wed Close)
- UNH/JPM/V/AAPL: **KEINE Earnings 3 HT** (Q3 Ende Okt bestätigt)

### Guardrails-Vollcheck (alle 8 GRÜN + 1 WARN)
1. Daily Loss Cap -3 %: **+0,234 % GRÜN**
2. Weekly Loss Cap -5 %: **+0,489 % GRÜN**
3. Drawdown-Alarm -15 % ATH: **-3,196 % GRÜN**
4. Drawdown-Stopp -20 % ATH: **-3,196 % GRÜN**
5. Crash-Filter SPY -5 %/Tag: Wed -0,171 % **INAKTIV**
6. VIX-Filter >30: **~16-18 GRÜN**
7. Earnings-Blackout: **LLY HT+1 aktiv WARN** (V1_neu 1.134,20 primär bis Mo 10.08.)
8. Max Käufe 2/Woche: **0/2 KW32 OFFEN**

### Kaufscan Market Open 09:30 ET: **JA**
- VIX GRÜN, kein Cap-Alert, kein Crash-Filter, Slot 1/2 offen
- **Watchlist Prio (aus Wed Close Vollcheck):**
  1. **UAL** XLI: K4-Vol-Rebound-Watch **5. Tag persistent** (Wed 68 %), RS_63d +35,3 pp #1 XLI ✓, K1/K2/K5 ✓; K4-Rebound Do Open kritisch
  2. **GS** XLF: K4 107 % nahe 120 %-Trigger, K1/K2/K3 ✓; K5 Multi-Source Pre-Open prüfen
  3. **DELL** XLK: K1 ✓✓✓ +49,8 %, K3 RS **+107,4 pp #1 Gesamt-Momentum**, K4 101 % nahe Trigger, **XLK-Konflikt mit AAPL**
  4. **HPE** XLK Watch: K4 74 % FAIL, XLK-Konflikt
  5. **UNP** XLI Backup: K4 59 % FAIL heavy
- BLOCKIERT: GE (K5 FwdPE 44,72), MSFT/META (K1+K2 FAIL), AMZN/GOOGL/AVGO (K3 NEG)

### Notifications
- ClickUp Prio 4 Routine-Log FEHLER ITEM_246 **persistent 4. Tag** → Fallback Memory-Only
- KEINE PushNotification (Silence-Rule: alle SICHER erwartet, kein Cap-Alert, positive Alpha, VIX GRÜN, LLY BO intakt, kein Owner-Handlungsbedarf)

### Nächste Routine
**Do 06.08. 09:30 ET Market Open KW32 Tag 4** — Kaufsignal-Scan Slot 1/2, UAL K4-Vol-Rebound 5. Tag, GS K4-Trigger-Check, LLY HT+1 Post-Earnings-Trend-Watch

---

## Market Close 16:00 ET — 2026-08-05 (Mi, KW32 Tag 3) — Daily +0,555 % / Alpha +0,726 pp POSITIV / DD -3,475 % GRÜN / Weekly +0,200 % GRÜN

### Alpaca /v2/account Close
- portfolio_value: **96.589,61 $** | equity: 96.589,61 $ | last_equity: 96.056,40 $
- Daily P/L: **+533,21 $ = +0,555 %** [GRÜN, Cap -3 %, verbessert vs Midday +0,495 %]
- cash: 56.707,49 $ (**58,71 %**, unverändert)
- long_market_value: **39.882,12 $** (5 Pos, +436,57 vs Mo Close 39.445,55 = **+1,107 %**)

### SPY EOD (Alpaca IEX Daily Bar)
- Close: **769,79 $** vs Di Close 771,11 = **-0,171 %** Post-Rally-Give-back marktweit
- Alpha vs Portfolio: **+0,726 pp POSITIV** (Portfolio +0,555 % vs SPY -0,171 %)
- SPY 20d %: +3,29 % (RS_4w-Baseline für V6-Check)

### V1-V6 Vollcheck EOD-Bars (Alpaca IEX 276d)
- **V5 EMA50>EMA200 Golden Cross alle 5 intakt**: V +3,79 % (engster aber positiv, verb. vs Mo +3,01 %), JPM +6,11 %, AAPL +10,85 %, LLY +11,31 %, UNH +15,23 %
- **V6 RSI<80 UND-Bedingung alle 5 sicher**: max JPM RSI 65,8 (V 64,0, LLY 51,2, UNH 46,7, AAPL 45,8); LLY RS_4w -7,15 pp NEG aber RSI 51,2 → sicher via UND; UNH -6,31 pp, AAPL -4,05 pp beide sicher via RSI
- **V1 Std-V1 alle 5 SICHER**: min AAPL +6,66 %, LLY +6,46 % (Blackout-V1_neu 1.134,20 ÜBERSCHRITTEN +2,64 % Bull-Konvention intakt), UNH +11,71 %, V +12,11 %, JPM +17,32 %
- **V2 Trailing-Stop 88 %**: UNH razor-thin +1,75 % via 52w-Wick 460,95 Data-Quality-Flag, AAPL +2,55 % via 52w-Wick 344,56, LLY +6,42 %, UNH-Rest >11 %
- **V3/V4 Gewinn-TP**: max JPM +7,94 % Best P/L << 20 % kein Trigger
- **=> KEIN Trigger. KEINE Sell-/Limit-Order für Do 06.08. platziert. 0 offene Orders.**

### Weekly Loss Cap Check
- Fr 31.07 Close: 96.396,66 $ | Mi 05.08 Close: 96.589,61 $
- Weekly KW32 Tag 3: **+0,200 %** [GRÜN, weit von Cap -5 % @ 91.576,83]

### Guardrails EOD 8/8 GRÜN + 1 WARN
- Daily +0,555 % (Cap -3 %) | Weekly +0,200 % (Cap -5 %) | DD -3,475 % (Alarm -15 %) | Crash-Filter INAKTIV (SPY -0,17 %) | VIX Pre 18,29 <25 | Käufe 0/2 | Max-Pos 10 % OK | Sektor XLV 19,89 % <30 %
- WARN: LLY BO HT+1 morgen (Blackout-V1_neu 1.134,20 ÜBERSCHRITTEN +2,64 %, Bull-Konvention intakt; Rest-Blackout bis Mo 10.08.); UNH V2 razor-thin +1,75 % via 52w-Wick Data-Quality-Flag Monitoring

### Watchlist Do 06.08. K1-K3 (K4/K5 morgen Vollcheck)
- **UAL 132,72 $ XLI** — K1 EMA-Diff +10,6 % ✓, K2 RSI 63,9 ✓, K3 RS_63d **+35,3 pp #1 XLI** ✓, K4 68 % <120 % FAIL 4. Tag Vol-Rebound-Watch, K5 vorbekannt ✓ FwdPE 14,8x + RevGr 16 %, XLI 0 % Diversifikation → **Prio 1**
- **GS 1.060,53 $ XLF** — K1 ✓ +10,6 %, K2 RSI 52,1 ✓, K3 RS +9,1 pp ✓, K4 107 % nahe 120 %-Trigger, K5 morgens prüfen → **Prio 2** (XLF-Cap noch OK JPM+V)
- **DELL 462,38 $ XLK** — K1 ✓✓✓ +49,8 %, K2 RSI 59,7 ✓, K3 RS **+107,4 pp #1 Gesamt** ✓, K4 101 %, XLK-Konflikt mit AAPL beachten → **Prio 3**
- **HPE 53,21 $ XLK** — K1 ✓ +34,6 %, K2 RSI 64,9 ✓, K3 RS +70,8 pp ✓, K4 74 % FAIL, XLK-Konflikt → **Prio 4 Watch**
- **UNP 295,50 $ XLI Backup** — K1 ✓ +9,4 %, K2 RSI 57,0 ✓, K3 RS +5,6 pp ✓, K4 59 % FAIL heavy → **Prio 5 Backup**
- **GE BLOCKIERT K5-FAIL persistent FwdPE 44,72 >35** (K1-K3 ✓ K4 65 %)
- **NVDA K1-K3 ✓ K4 98 %** aber XLK-Konflikt AAPL
- **MSFT K1 Death-Cross-nah (diff -5,3 %) + K2 RSI 76,3 FAIL**, **ORCL K1 Death-Cross + K3 -28,5 pp FAIL heavy**, **META/NFLX K1 Death-Cross FAIL**, **AMZN/GOOGL/AVGO/CAT K3 NEG FAIL**

**Watchlist morgen: UAL (Prio 1 XLI, K4-Rebound-Watch), GS (Prio 2 XLF K4 nahe 120 %), DELL (Prio 3 XLK #1 Momentum XLK-Konflikt), HPE (Prio 4 XLK-Konflikt), UNP (Prio 5 Backup XLI)**

### Aktionen für Do 06.08. Pre-Market 08:30 ET
- VIX-Read Perplexity (aktueller Stand + 3-Tage-Schnitt)
- Earnings-Blackout LLY HT+1 (Blackout-V1_neu 1.134,20 überwachen)
- Alpaca Live-Read auf UAL, GS, DELL für K4 Vol-Ratio Update (Pre-Market Vol schwer belastbar aber Approximation)
- SPY Pre-Read für Crash-Filter-Watch (nach heutigem Give-back)

---

## Market Open 09:40 ET — 2026-08-05 (Mi, KW32 Tag 3) — Daily +0,595 % Live / DD -3,436 % GRÜN / Weekly +0,240 % GRÜN gedreht positiv

### Alpaca /v2/account Live
- portfolio_value: **96.628,15 $** | equity: 96.628,15 $ | last_equity: 96.056,40 $
- Daily P/L: **+571,75 $ = +0,595 %** [GRÜN, Cap -3 %, weiter verbessert vs Pre +0,526 %]
- cash: 56.707,49 $ (**58,68 %**, unverändert)
- long_market_value: **39.920,66 $** (5 Pos, +475,11 vs Mo Close 39.445,55 = **+1,204 %** LLY-Post-Earnings-Rally dominant)
- **DD vs ATH 100.066,47: -3,436 %** [GRÜN, verbessert vs Pre -3,502 %]
- **Weekly KW32 Tag 3: +0,240 %** vs Fr 31.07. Close 96.396,66 [GRÜN, gedreht positiv Vertiefung vs Pre +0,172 %]
- 0 offene Orders

### Positionen Live (Alpaca /v2/positions + latest trades)
| Symbol | Cur Live | chg_today | P/L $ | P/L % | V1 Std | V1 Puf | Blackout |
|--------|----------|-----------|-------|-------|--------|--------|----------|
| AAPL | 307,78 | **-0,760 % Worst chg** | -304,62 | **-3,10 % Worst P/L neu** | 291,51 | **+5,58 % ENGSTE Std** | frei |
| LLY  | 1.196,825 | **+7,449 % Best chg** | +39,18 | **+0,41 % Recovery +6,81 pp vs Close -6,40 %** | 1.098,38 | +8,96 % | **HT+0 Post-Report; Blackout-V1_neu 1.134,20 Puffer +5,52 % ÜBERSCHRITTEN** |
| UNH  | 406,56 | -0,250 % | +119,04 | +1,23 % | 369,44 | +10,04 % (V2 razor-thin +0,23 %) | – |
| V    | 371,05 | +0,200 % | +355,11 | +3,68 % | 328,60 | +12,92 % | – |
| JPM  | 360,73 | +0,931 % | +84,21 | **+8,43 % Best P/L** | 306,16 | +17,82 % | – |

**V1-V6 alle 5 SICHER Std-V1 Live-Read** (RSI/EMA werden im Open nicht geprüft, Vollcheck bei Close). Kein V-Trigger, KEINE Sell-Order platziert.

**V2 UNH razor-thin +0,23 %** — 460,95 * 0,88 = 405,64, cur 406,56. Data-Quality-Flag 52w-Wick beibehalten. Strategie-Lock strategy.md wörtlich → V2 nicht getriggert.

### SPY + Makro Live
- **SPY Live 775,70 Alpaca latestTrade** vs Mo Close 771,11 = **+0,595 % Post-Rally-Fortsetzung** (Crash-Filter INAKTIV)
- **Alpha vs SPY 0,000 pp neutral** (LLY-Post-Earnings-Rally kompensiert SPY-Beta vollständig — beste Alpha-Session KW32 bislang)
- VIX 18,29 [GRÜN <25]
- LLY-Blackout-Bruch aus Vorwochen komplett aufgehoben (3-Tage-Bruch Mo/Di/Pre-Mi durch Post-Earnings-Rally gelöst)

### Kaufsignal-Scan Slot 1/2 KW32 — Alpaca IEX EOD Bars Di 04.08.

| Symbol | K1 EMA | K2 RSI | K3 RS_63d | K4 Vol | K5 | Verdikt |
|--------|--------|--------|-----------|--------|----|----|
| **UAL** #1 XLI | +9,01 % ✓ | 63,8 ✓ | **+39,77 pp #1 TOP** ✓ | 71 % **FAIL 3. Tag** | vorbekannt ✓ | **REJECT K4 Vol-Rebound nicht bestätigt** |
| UNP #2 XLI Backup | +10,54 % ✓ | 58,2 ✓ | +5,10 pp ✓ | 66 % **FAIL** | vorbekannt ✓ | REJECT K4 |
| MRK Post-Earnings | +12,20 % ✓ | 53,1 ✓ | +5,81 pp ✓ | 115 % **FAIL** | Q2 Post-Report Mo 04.08. Reaktion Watch | REJECT K4 + XLV-Cap Owner-pending |
| ABBV #4 XLV | +6,15 % ✓ | 44,1 **FAIL <50** | +9,65 pp ✓ | 165 % ✓ | K5 ✓ | **REJECT K2** + XLV-Cap Owner-pending 5. Woche |
| GE | +8,47 % ✓ | 64,4 ✓ | **+27,09 pp** ✓ | 103 % **FAIL** | **FwdPE 44,72 >35 FAIL persistent** | REJECT K4 + K5 |
| EOG | +9,42 % ✓ | 54,8 ✓ | **-6,02 pp NEG FAIL** | 122 % ✓ | vorbekannt ✓ | REJECT K3 |
| NVDA | +4,94 % ✓ | 56,9 ✓ | -0,63 pp marginal NEG **FAIL** | 78 % FAIL | – | REJECT K3+K4 |
| AMZN | +4,26 % ✓ | 67,1 ✓ | -5,44 pp NEG FAIL | 118 % FAIL | – | REJECT K3+K4 |
| GOOGL | +10,62 % ✓ | 62,6 ✓ | -8,83 pp NEG FAIL | 138 % ✓ | – | REJECT K3 |
| MSFT | -7,28 % **FAIL Death Cross** | 79,2 FAIL | +11,76 pp ✓ | 100 % FAIL | – | REJECT K1+K2+K4 |
| META | -5,89 % **FAIL Death Cross** | 46,4 FAIL | -11,07 pp NEG FAIL | 80 % FAIL | – | REJECT 4/4 |

**Slot 1/2 KW32 bleibt OFFEN** — kein Kandidat erfüllt alle 5 K1-K5.

**Bemerkenswert:** UAL Prio-1 K4-Vol-Rebound-Watch scheiterte 3. Tag in Folge (Mo 73 % → Di 71 % → Vollcheck EOD 71 %). RS +39,77 pp #1 TOP bleibt aber Bull-Konvention Overrides nicht Volumenerfordernis (strategy.md K4 wörtlich).

### Sektor-Struktur Live 09:40 ET
- XLV: UNH 9.756,72 + LLY 9.590,28 = **19.347,00 = 20,02 %** (LLY-Rally hebt XLV-Anteil moderat vs Mo Close 19,58 %)
- XLF: JPM 1.082,55 + V 9.998,91 = 11.081,46 = **11,47 %**
- XLK: AAPL 9.517,93 = **9,85 %**
- Cash: **58,68 %**

### Guardrails-Status Live 09:40 ET
1. Daily Loss Cap -3 %: **+0,595 %** → GRÜN
2. Weekly Loss Cap -5 %: **+0,240 %** → GRÜN gedreht positiv Vertiefung
3. Drawdown-Alarm -15 % ATH: -3,436 % → GRÜN
4. Drawdown-Stopp -20 % ATH: -3,436 % → GRÜN
5. Crash-Filter (SPY -5 %/Tag): SPY +0,595 % → INAKTIV
6. VIX-Filter (>30): 18,29 → GRÜN <25
7. Earnings-Blackout: LLY HT+0 heute Post-Report POSITIV, keine anderen Portfolio-Blackouts
8. Max neue Käufe 2/Woche: KW32 0/2 → GRÜN

**→ 8/8 GRÜN, 0 WARN.** LLY BO-Bruch aufgehoben (Puffer +5,52 % ÜBERSCHRITTEN), UNH V2 razor-thin +0,23 % via 52w-Wick Monitoring aber keine WARN.

### Entscheidung
- **KEIN Trade heute Market Open** (kein Kaufkandidat erfüllt alle K1-K5)
- **KEINE Sell-Order** (alle 5 V1-V6 SICHER Live)
- **Käufe KW32 0/2 unverändert**
- **ClickUp Prio 4 Routine-Log FEHLER "Max usage for custom task types reached"** → Fallback Memory-Only (2. Tag persistent)
- **KEINE PushNotification** (Silence-Rule Routine: kein Cap-Alert, kein neuer Trade, LLY-Post-Earnings-Sichtbarkeit bereits im Pre-Market abgedeckt, LLY-Rally-Fortsetzung Post-Open keine neue Handlungsaufforderung)
- Nächste Routine: 13:00 ET Midday Stop-Check KW32 Tag 3

---

## Pre-Market 08:35 ET — 2026-08-05 (Mi, KW32 Tag 3) — Daily +0,526 % Pre / DD -3,502 % GRÜN / Weekly +0,172 % GRÜN gedreht positiv

### Alpaca /v2/account Pre
- portfolio_value: **96.562,01 $** | equity: 96.562,01 $ | last_equity: 96.056,40 $
- Daily P/L: **+505,61 $ = +0,526 %** Pre-Read [GRÜN, Cap -3 %]
- vs Memory Close 96.153,04: +408,97 = +0,425 % (LLY-Post-Earnings-Rally)
- cash: 56.707,49 $ (58,73 %, unverändert)
- long_market_value: 39.854,52 $ (5 Pos, +408,97 vs Mo Close 39.445,55 = +1,037 %)
- **DD vs ATH 100.066,47: -3,502 %** [GRÜN, deutlich verbessert vs Mo Close -3,911 %]
- **Weekly KW32 Tag 3: +0,172 %** vs Fr 31.07. Close 96.396,66 [GRÜN, gedreht positiv vs Mo Close -0,253 %]
- 0 offene Orders

### Positionen Pre (Alpaca /v2/positions Live)
| Symbol | Cur | chg_today | P/L $ | P/L % | V1 Std | V1 Puf | Blackout |
|--------|-----|-----------|-------|-------|--------|--------|----------|
| AAPL | 308,90 | -0,155 % | -246,65 | **-2,51 % ENGSTE Std verschlechtert Worst neu** | 291,51 | **+5,90 % ENGSTE** | frei (HT+2 seit Di 04.08. beendet) |
| LLY  | 1.168,00 | **+4,69 % Best chg** | -207,10 | **-2,17 % verbessert vs Close -6,40 %** | 1.098,38 | +6,34 % | **HT+0 heute BMO Post-Report POSITIV; Blackout-V1_neu 1.134,20 Puffer +2,98 % ÜBERSCHRITTEN** |
| V    | 372,10 | +0,68 % | +402,90 | **+4,18 %** | 328,60 | +13,24 % | – |
| UNH  | 409,01 | +0,36 % | +178,56 | +1,85 % | 369,44 | +10,71 % | – |
| JPM  | 358,99 | +0,41 % | +78,63 | **+7,88 % Best P/L** | 306,16 | +17,26 % | – |

**V1-V6 Pre-Read alle SICHER Std-V1** (RSI/EMA werden im Pre nicht geprüft). Kein V-Trigger, keine Sell-Order.

### 🟢 LLY Q2 2026 Earnings Report (Mi 05.08. BMO) — MASSIVER BEAT + GUIDANCE-ANHEBUNG

| KPI | Actual Q2 26 | Konsens | Beat |
|-----|--------------|---------|------|
| EPS Non-GAAP (adj.) | **$8,38** | $6,00–7,74 | **+25-35 %** |
| Revenue | **$22,97 Mrd.** | $20,5–20,7 Mrd. | **+11 %** |
| YoY Rev-Growth | **+48 %** | – | – |
| Mounjaro Q2 | **$9,94 Mrd.** | – | ~Verdoppelung YoY |

**Guidance 2026 angehoben:**
- Revenue: **$85–87 Mrd.** (vorher $82–85 Mrd.)
- EPS Non-GAAP: **$35,50–36,50** (aktualisiert; Q2 IPR&D-Charges $3,03/Aktie drücken Berichtsspanne)
- Mounjaro/Zepbound Volumen-Treiber, Retatrutide Pipeline fortschreitend (kein separates Revenue-Guidance)

**LLY Kursreaktion Pre-Market:**
- Alpaca Positions Live cur: **1.168,00** (vs Mo Close 1.117,47 = **+4,52 % Gap-Up**)
- **Blackout-V1_neu 1.134,20 (Bull-Konvention) Puffer +2,98 % ÜBERSCHRITTEN** — 3-Tage-Bruch (Mo/Di/Pre-Mi) aufgehoben
- P/L verbessert von Close -6,40 % auf Pre -2,17 % (+4,23 pp Recovery)
- Worst-P/L-Titel wechselt zu AAPL -2,51 %
- Blackout-Kalender: HT+0 heute → HT+1 Do 06.08. → HT+2 Fr 07.08. → **Blackout beendet ab Mo 10.08.**

### Perplexity Daily Macro Check (05.08. Pre-Market)
- **VIX Close 04.08.:** 18,29 [GRÜN <25, leicht erhöht vs Fr 16,02 / Mo 15,86 aber weit von Cap]
- **SPY Pre 774,59 Alpaca latestTrade** vs Mo Close 771,11 = **+0,451 % Post-Rally-Fortsetzung** (Perplexity keine SPY Pre-Angabe)
- **10Y US Treasury Yield:** ~4,25 % (aus Marktdaten abgeleitet)
- **Makro-Events heute:** Kein FOMC-Meeting, kein CPI/PCE-Release; Standard Weekly-Claims. Earnings-Highlight: **LLY Q2 BMO** (siehe oben)
- **MRK Post-Earnings (gestern Di 04.08. BMO):** Perplexity keine belastbaren EPS/Revenue-Zahlen, Reaktion nach Open zu prüfen

### Earnings-Blackout Nächste 3 HT (Portfolio)
- **LLY Mi 05.08. BMO** — HT+0 heute, Report bereits erfolgt (positiv, siehe oben)
- **AAPL** — HT+2 seit Di 04.08. beendet, keine Portfolio-Blackouts weitere 3 HT
- **UNH, JPM, V** — nächste Earnings Q3 Ende Okt 2026
- **MRK** — nicht Portfolio (gestern Di 04.08. BMO Report, blockiert weiter als Watchlist-Kandidat)
- Do 06.08. + Fr 07.08. **keine** Portfolio-Position mit Earnings

### Guardrails-Status Pre 08:35 ET
1. Daily Loss Cap -3 %: **+0,526 %** → GRÜN
2. Weekly Loss Cap -5 %: **+0,172 %** → GRÜN gedreht positiv
3. Drawdown-Alarm -15 % ATH: -3,502 % → GRÜN
4. Drawdown-Stopp -20 % ATH: -3,502 % → GRÜN
5. Crash-Filter (SPY -5 %/Tag): SPY Mo +1,77 %, Pre +0,45 % → INAKTIV
6. VIX-Filter (>30): VIX 18,29 → GRÜN <25
7. Earnings-Blackout: LLY HT+0 heute Report erfolgt positiv, keine anderen Portfolio-Blackouts
8. Max neue Käufe 2/Woche: KW32 0/2 → GRÜN

**→ 8/8 GRÜN, 0 WARN.** LLY Blackout-Bruch aus Vorwochen aufgehoben (Puffer +2,98 % ÜBERSCHRITTEN nach Post-Earnings-Rally).

### Entscheidung
- **Kaufscan Market Open 09:30 ET: JA** — LLY-Post-Earnings-Momentum-Watch für Portfolio, UAL K4-Vol-Rebound 3. Tag Re-Check als Slot 1 Prio 1, MRK Post-Earnings Mo BMO Reaktion Watch, ABBV XLV-Cap Owner-pending 5. Woche bleibt blockiert
- **ClickUp Routine-Log Prio 4 FEHLER "Max usage for custom task types reached" ITEM_246** → Fallback Memory-Only per notify-skill.md
- **PushNotification Prio 2 Owner** — positive Post-Earnings-Sichtbarkeit LLY (Beat + Guidance-Anhebung + Blackout-Bruch aufgehoben + Weekly gedreht positiv)

---

## Market Close 16:00 ET — 2026-08-04 (Di, KW32 Tag 2) — Tagesbilanz +0,176 % / Alpha -1,591 pp NEG / DD -3,911 % GRÜN / Weekly -0,253 % GRÜN

### Alpaca /v2/account Close
- portfolio_value: **96.153,04 $** | equity: 96.153,04 $ | last_equity: 95.984,04 $
- Daily P/L: **+169,00 $ = +0,176 %** [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (58,98 %, unverändert)
- long_market_value: 39.445,55 $ (5 Pos)
- **DD vs ATH 100.066,47: -3,911 %** [GRÜN, verbessert vs Midday -3,884 %]
- **Weekly KW32 Tag 2: -0,253 %** vs Fr 31.07. Close 96.396,66 [GRÜN, Cap -5 %]
- 0 offene Orders

### Positionen Close (Alpaca IEX Daily Bars)
| Symbol | Close | chg_today | P/L $ | P/L % | V1 Std | V1 Puf | V2 Trail | V2 Puf | RSI14 | EMA-Diff | RS_4w | RS_63d |
|--------|-------|-----------|-------|-------|--------|--------|----------|--------|-------|----------|-------|--------|
| LLY  | 1.117,47 | -0,33% | -611,34 | **-6,40 % Worst** | 1.098,38 | **+1,74 % ENGSTE Std** | 1.098,70 | +1,71% | 40,4 | +11,90% | **-12,66 pp NEG** | +8,04 pp |
| AAPL | 309,335 | **+1,95 % Best chg** | -233,17 | -2,37% | 291,51 | +6,12% | 303,21 | +2,02% | 44,6 | +10,37% | -3,56 pp | +4,34 pp |
| UNH  | 407,73 | **-1,84 % Worst chg** | +147,84 | +1,53% | 369,44 | +10,36% | **405,64** | **+0,52 %** | 43,1 | +13,65% | -7,87 pp | +2,61 pp |
| V    | 369,53 | +1,06% | +333,51 | +3,46% | 328,60 | +12,45% | 329,09 | +12,29% | 65,5 | **+3,01 % engster V5** | +1,83 pp | +5,65 pp |
| JPM  | 357,52 | +1,38% | +74,22 | **+7,43 % Best P/L** | 306,16 | +16,78% | 319,43 | +11,93% | 64,6 | +5,74% | +2,36 pp | +8,80 pp |

**V5-Vollcheck 5 SICHER** (Alpaca IEX 253d, alle Golden Cross): V engster +3,01 % (verb. vs Mo +3,92 %), JPM +5,74 %, AAPL +10,37 %, LLY +11,90 %, UNH +13,65 %.
**V6-Vollcheck 5 SICHER** (max RSI V 65,5 << 80): LLY RS_4w -12,66 pp NEG aber RSI 40,4 → sicher via UND.
**V2 UNH razor-thin Puffer +0,52 %** — 52w-High 460,95 vom 2026-07-16 = intraday-Wick (Close-basis 423,28 = -8,17 % below), ohne Wick nächst-höchster ~437,13 → V2 Puffer +5,99 %. Strategie-Lock strategy.md wörtlich → 460,95 bindend, V2 nicht getriggert.
**V3/V4 kein Trigger** (max JPM +7,43 % << 20 %-TP1).

### Makro-Research (Perplexity + Alpaca IEX)
- **SPY Close 771,11 Alpaca IEX** vs Mo 757,72 = **+1,767 % Post-Rally-Beschleunigung** (Snapshot Daily-Bar h=773,41 l=760,53 vol=2,27M verified)
- Perplexity divergiert bei 1,48 % → IEX bindend (Konvention Memory-etabliert)
- **VIX Perplexity 15,86** [GRÜN <25, weiter reduziert vs Mo 16,02 = Vola-Entspannung Fortsetzung]
- **Alpha vs SPY -1,591 pp NEGATIV** (Cash 58,98 % struktureller Drag + UNH Give-back vs SPY-Beta-Beschleunigung)

### Guardrail-Check nach Close
1. Daily Loss Cap -3 %: **GRÜN** (+0,176 %)
2. Weekly Loss Cap -5 %: **GRÜN** (-0,253 % Tag 2)
3. Drawdown-Alarm -15 % ATH: **GRÜN** (-3,911 %)
4. Drawdown-Stopp -20 % ATH: **GRÜN**
5. Crash-Filter SPY -5 %: **INAKTIV** (Di +1,77 %)
6. VIX-Filter >30: **GRÜN** (15,86)
7. Earnings-Blackout: **LLY HT-0 morgen BMO** aktiv Bull-Konvention + AAPL beendet
8. Max. Käufe/Woche 2: **0/2 KW32 verbraucht** — Slot 1/2 + 2/2 OFFEN

### Watchlist morgen Mi 05.08. (K1-K4 aus Alpaca IEX EOD 04.08.)
1. **UAL** #1 XLI (132,63 chg +3,29 %, K1 EMA-Diff +9,01 % ✓, K2 RSI 63,8 ✓, K3 RS_63d **+39,77 pp #1 TOP** ✓ verb. vs Mo +33,61 pp, K4 71 % <120 % FAIL **Vol-Rebound-Watch Mi 3. Tag**, K5 vorbekannt ✓ RevGr 16 % + FwdPE 14,8x, XLI 0 % Diversifikation) — **Prio 1 wenn K4-Rebound**
2. **UNP** #2 XLI Backup (296,51 chg +1,64 %, K1-K3 ✓ RS +5,10 pp, K4 66 % FAIL Rebound-Watch)
3. **NVDA** #3 XLK Watch (211,96 chg +2,53 %, K1 +4,94 % ✓, K2 RSI 56,9 ✓, K3 RS -0,63 pp marginal NEG FAIL, K4 77 % FAIL, XLK-Konzentration mit AAPL beachten)
4. **GE** BLOCKIERT K5 persistent (FwdPE 44,72 >35)
5. **ABBV** BLOCKIERT XLV-Cap Owner pending 5. Woche + K2 RSI 44,1 FAIL
6. **EOG** K3 -6,02 pp NEG FAIL (Rebound weiter abgebrochen)
7. **AMZN/GOOGL** K3 persistent FAIL
8. **MSFT/ORCL** K1 FAIL (Death-Cross)
9. **MRK** Post-Earnings-Reaktion Mi Open prüfen (heute BMO)
10. **LLY** BMO Report morgen HT-0 kritisch für Portfolio

### Entscheidung
- **KEIN Trade heute** (5 V1-V6 SICHER, kein Kauf-Signal, 0 offene Orders)
- **KEINE Sell-/Limit-Order für Mi 05.08. platziert**
- **LLY BMO Report morgen früh** — Blackout-V1_neu 1.134,20 wird nach Report neu bewertet
- **Slot 1/2 KW32 bleibt OFFEN** — UAL Top-Kandidat wartet auf K4-Vol-Rebound (3. Tag)
- Nächste Routine: Mi 05.08. 08:30 ET Pre-Market KW32 Tag 3

---

## Pre-Market 08:30 ET — 2026-08-04 (Di, KW32 Tag 2) — Guardrails GRÜN, VIX 18,9 leicht erhöht vs Fr 16,02 aber <25, SPY Pre +0,34 %, LLY HT-1 letzter Tag vor BMO Earnings Mi 05.08., AAPL Blackout HT+2 → beendet Std-V1 alleine primär, Kaufscan JA mit UAL K4-Rebound-Watch Prio 1

### Alpaca /v2/account Pre
- portfolio_value: **95.986,04 $** | equity: 95.986,04 $ | last_equity: 95.984,04 $
- Daily Pre: **+0,002 %** (essentiell flat) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (59,08 %, unverändert)
- long_market_value: 39.278,55 $ (5 Pos)
- **DD vs ATH 100.066,47: -4,078 %** [GRÜN, marginal verbessert vs Mo Close -4,091 %]
- **Weekly KW32 Tag 2 = +0,014 %** vs Fr 24.07. Close (Referenz Bot-Reset Wochenanfang Mo Close 95.972,60 → +13,44 $) [GRÜN weit von Cap -5 %]
- Konsistenz-Check vs Memory Mo Close 95.972,60: Alpaca 95.986,04 = +13,44 $ (0,014 %) Pre-Market-Aufwärtsbewegung, plausibel
- 0 offene Orders

### Pre-Market Positionen (Alpaca Live)
| Symbol | Cur | chg_today | P/L % | Std-V1 | Std-V1 Puffer | Blackout BO | BO Puffer |
|--------|-----|-----------|-------|--------|---------------|-------------|-----------|
| LLY   | 1.123,50 | +0,19 % | -5,90 % | 1.098,38 | +2,29 % **ENGSTE Std** verb. vs Mo +2,06 % | **1.134,20 HT-1** | **-0,94 % UNTERSCHRITTEN** verb. vs Mo -1,16 % |
| AAPL  | 302,894 | -0,17 % | -4,41 % | 291,51 | **+3,90 %** | n/a HT+2 **beendet** | n/a (Std alleine primär) |
| V     | 366,00 | +0,09 % | +2,47 % | 328,60 | +11,38 % | n/a | n/a |
| UNH   | 415,01 | -0,08 % | +3,35 % | 369,44 | +12,33 % | n/a | n/a |
| JPM   | 352,9075 | +0,08 % | +6,05 % **Best P/L** | 306,16 | +15,26 % | n/a | n/a |

**RSI/EMA werden im Pre-Market NICHT geprüft (nur Market Open + Close per Routinen).** Alle 5 Std-V1 SICHER Pre-Read.

### Makro-Research (Perplexity + Alpaca Snapshot)
- **VIX**: **18,9** (Perplexity Intraday-Print) [GRÜN <25, leicht erhöht vs Fr Close 16,02 = Vola-Anstieg Post-Weekend-Rally-Konsolidierung, aber weit von 25-Cap]
- **SPY Pre-Market 08:34 ET**: **760,30 Alpaca latestTrade** vs Mo Close 757,72 = **+0,341 % Post-Rally-Fortsetzung Konsolidierung** [Crash-Filter INAKTIV]
- **10Y Treasury Yield**: n/a (Perplexity nicht sourceable heute)
- **Makro-Events heute**: nicht bestätigt via Perplexity (keine belastbaren Angaben zu Trade Balance/JOLTS/Factory Orders)
- **Top 3 marktbewegende News**: nicht sourceable via Perplexity heute Pre-Market
- **SPY Vortag Mo -1,46 %**: **INAKTIV — kein Crash-Filter** (SPY Mo +1,46 % Post-Weekend-Rally)

### Guardrail-Check nach Research
1. Daily Loss Cap -3 %: **GRÜN** (Pre +0,002 %)
2. Weekly Loss Cap -5 %: **GRÜN** (Tag 2 +0,014 %)
3. Drawdown-Alarm -15 % ATH: **GRÜN** (-4,078 %)
4. Drawdown-Stopp -20 % ATH: **GRÜN** (-4,078 %)
5. Crash-Filter SPY -5 %: **INAKTIV** (Mo +1,46 %)
6. VIX-Filter >30: **GRÜN** (18,9)
7. Earnings-Blackout: **LLY HT-1 aktiv** BMO Mi 05.08. + AAPL HT+2 **beendet** heute
8. Max. Käufe/Woche 2: **0/2 KW32 verbraucht** — Slot 1/2 + 2/2 OFFEN

### Earnings-Blackout Nächste 3 HT (04./05./06.08.)
- **MRK** Di 04.08. **BMO HT-0 (heute)** — nicht Portfolio, blockiert Kauf-Watchlist bis Post-Report (Perplexity bestätigt)
- **AMD** Di 04.08. AMC — nicht Portfolio
- **MCD** Di 04.08. BMO — nicht Portfolio
- **LLY** Mi 05.08. **BMO HT-1 (morgen)** — **PORTFOLIO-POSITION** ⚠️ Blackout-V1_neu 1.134,20 bleibt primäre Bull-Konvention-Referenz bis Post-Report (Memory-Konvention seit Wochen etabliert, Perplexity divergiert = konservativ Blackout beibehalten per CLAUDE.md Rule 5 No-Action bei Unsicherheit)
- **AAPL**: HT+2 heute → Blackout **beendet**, Std-V1 291,51 wieder alleine primär
- **UNH, JPM, V**: keine Earnings in 3 HT (nächste Q3 Ende Okt)

### Watchlist Di 04.08. (aus Mo Close K1-K3)
1. **UAL** #1 XLI NEUE (128,40 Mo Close chg +5,84 % Best chg, K1 EMA-Diff +9,26 % ✓, K2 RSI 52,8 ✓, K3 RS_63d **+33,61 pp #1 TOP** ✓, K4 Mo 72 % <120 % FAIL **Vol-Rebound-Watch Di**, K5 vorbekannt ✓ RevGr 16 % + FwdPE 14,8x + Next-Earnings Okt 2026 = keine Blackout, XLI 0 % neue Diversifikation) — **Prio 1 wenn K4 Vol-belastbar Open**
2. **UNP** #2 XLI Backup (Fr K4 116 % borderline → Mo Momentum-Bruch, Re-Check Di Pre-Market/Open)
3. **EOG** #3 XLE Rebound-Watch (K3 Mo -0,11 pp marginal NEG, K5 vorbekannt ✓)
4. **ABBV** #4 XLV **BLOCKIERT XLV-Cap-Klärung Owner pending 4. Woche**
5. **MRK** BLOCKIERT Earnings Di 04.08. BMO HT-0 heute (evtl. Post-Report-Reaktion nach 10:00 ET verfügbar)
6. **GE/META/TSLA/CAT** REJECT persistent (K1/K2/K5-FAIL)

### Entscheidung
**Kaufscan bei Market Open: JA** — alle Vola-Guardrails GRÜN, VIX 18,9, SPY Pre +0,34 %, keine Portfolio-Blackout blockiert Kauf. **Bedingungen:** UAL Prio 1 nur wenn K4-Session-Vol Open-Handel belastbar UND K5-Multi-Source-Verifikation. UNP nur wenn Momentum-Turnaround. ABBV weiter BLOCKIERT bis Owner-Klärung XLV-Cap. **Slot 1/2 KW32 primär, Slot 2/2 sekundär falls 2 Kandidaten qualifizieren.**

**LLY-Blackout HT-1 letzter Tag vor Report:** Std-V1 1.098,38 SICHER +2,29 % (verbessert), Blackout-V1_neu 1.134,20 **UNTERSCHRITTEN -0,94 %** (verbessert vs Mo -1,16 %). Strategie-Lock CLAUDE.md Rule 3 → nur strategy.md V1 bindend → HALTEN. Report morgen früh entscheidet Post-Blackout-Recovery oder Escalation.

### ClickUp-API-Status
**⚠️ ClickUp Task-Create FEHLGESCHLAGEN**: `{"err":"Max usage for custom task types reached","ECODE":"ITEM_246"}` — Workspace-Kontingent für Custom Task Types erreicht, kein API-Down, kein 401/429. Notify-Skill-Fallback greift: Memory-Files geschrieben (research-log + portfolio + trade-log). **PushNotification an Owner** wegen ClickUp-Alert-Kanal-Ausfall + LLY HT-1 letzter Tag vor Report gerechtfertigt (strukturelle Unterbrechung des Standard-Notify-Kanals, Owner-Klärung nötig).

---

## Market Open 09:38 ET — 2026-08-04 (Di, KW32 Tag 2) — KEIN Kauf (alle 10 Watchlist-Kandidaten REJECT/SKIP), 5 V1-V6 SICHER Std, Daily -0,134 %, SPY +0,52 % Post-Rally-Fortsetzung, LLY HT-1 letzter Tag Std sicher +2,03 % ENGSTE (BO -1,20 % UNTERSCHRITTEN aber Strategie-Lock HALTEN), AAPL HT+2 Blackout beendet Std alleine primär +3,84 %, Slot 1/2 KW32 OFFEN

### Alpaca /v2/account 09:38 ET
- equity: **95.855,86 $** (vs last_equity 95.984,04 = **-0,134 %** Daily) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (**59,16 %** unverändert)
- MV Live: **39.148,37 $** (5 Pos, -113,21 vs Mo Close 39.261,58 = -0,288 %)
- **DD vs ATH 100.066,47: -4,208 %** [GRÜN, marginal verschlechtert vs Pre -4,078 %]
- **Weekly KW32 Tag 2: -0,561 %** vs Fr 31.07. Close 96.396,66 [GRÜN weit von Cap -5 %]
- **SPY Live 761,55 Alpaca IEX** vs Mo Close 757,72 = **+0,506 % Post-Rally-Fortsetzung Konsolidierung** [Crash-Filter INAKTIV]
- **Alpha vs SPY -0,640 pp NEGATIV** (Portfolio underperformt marginal SPY-Rally)
- **VIX 18,9 Pre-Read** (Perplexity Intraday nicht neu abgefragt Open) [GRÜN <25]
- 0 offene Orders

### Guardrail-Check
1. Daily Loss Cap -3 %: **GRÜN** (-0,134 %)
2. Weekly Loss Cap -5 %: **GRÜN** (-0,561 %)
3. Drawdown-Alarm -15 % ATH: **GRÜN** (-4,208 %)
4. Drawdown-Stopp -20 % ATH: **GRÜN**
5. Crash-Filter SPY -5 %: **INAKTIV** (SPY +0,52 %)
6. VIX-Filter >30: **GRÜN** (18,9)
7. Earnings-Blackout: **LLY HT-1 aktiv** BMO Mi 05.08. + AAPL HT+2 **beendet heute**
8. Max. Käufe/Woche 2: **0/2 KW32** — Slot 1/2 + 2/2 OFFEN
→ **Alle 8 Guardrails GRÜN + 2 WARN**, Kaufen erlaubt.

### V1-V6 Portfolio-Check (Alpaca latest+Bars EOD Mo)
| Symbol | Live | chg | P/L | Std-V1 Puffer | Blackout | EMA-Diff | RSI | RS_4w |
|--------|------|-----|-----|---------------|----------|----------|-----|-------|
| LLY   | 1.120,645 | +0,04 % | -5,72 % Worst | +2,03 % **ENGSTE Std** | **-1,20 % UNTERSCHRITTEN** HT-1 letzter Tag | +11,90 % | 40,9 | -11,12 pp NEG |
| AAPL  | 302,71 | -0,01 % | -4,25 % | +3,84 % Std | HT+2 **beendet** heute → Std alleine primär | +10,30 % | 39,8 | -4,46 pp NEG |
| V     | 363,625 | -0,86 % | +1,49 % | +10,66 % | n/a | +2,96 % engster aber positiv | 60,0 | +1,45 pp |
| UNH   | 412,82 | -0,91 % | +2,49 % | +11,74 % | n/a | +13,69 % | 46,0 | -5,40 pp NEG |
| JPM   | 360,00 | **+2,09 % Best chg** | **+8,18 % Best P/L** | +17,58 % | n/a | +5,76 % | 66,3 | +4,42 pp |

**V3/V4 kein Trigger** (max JPM +8,18 % << 20 %-TP1). **V5 alle Golden Cross intakt** (V engster +2,96 % positiv). **V6 alle SICHER** (max JPM RSI 66,3 << 80, LLY RSI 40,9 UND RS_4w -11,12 pp NEG → V6 sicher via UND-Bedingung da RSI<<80). **→ KEIN V-Trigger, KEINE Sell-/Limit-Order platziert.**

### Kaufsignal-Scan Slot 1/2 KW32 — alle 10 Watchlist-Kandidaten REJECT/SKIP
| Kandidat | K1 EMA-Diff | K2 RSI | K3 RS_63d | K4 Vol (Mo/live) | K5 | Verdict |
|----------|-------------|--------|-----------|-------------------|-----|---------|
| **UAL** #1 | +9,00 % ✓ | 63,5 ✓ | **+40,67 pp #1 TOP** ✓ | **Mo 73 % <120 % FAIL** + Live 4 % pro-rata unbelastbar | vorbekannt ✓ | **REJECT K4** (Vol-Rebound Mo bestätigt nicht → nicht handelbar heute) |
| UNP | +10,46 % ✓ | 50,6 ✓ | +3,48 pp ✓ | **Mo 46 % <<120 % FAIL** heavy | Q2 26 +11,53 % ✓ | REJECT K4 |
| EOG | +9,36 % ✓ | 50,9 ✓ | **-6,44 pp NEG FAIL** (Rebound abgebrochen) | Mo 118 % marginal | vorbekannt ✓ | REJECT K3 |
| ABBV | +6,16 % ✓ | **44,8 <50 FAIL** | +11,40 pp ✓ | Mo 161 % ✓ | Q2 26 +10,16 % ✓ | **REJECT K2** + XLV-Cap-Block |
| MRK | +12,18 % ✓ | 51,4 ✓ | +6,45 pp ✓ | Mo 136 % ✓ | zwingend | **BLOCKIERT Earnings HT-0 heute BMO** |
| GE | +8,41 % ✓ | 61,4 ✓ | +26,14 pp ✓ | Mo 80 % FAIL | **K5 FAIL persistent FwdPE 44,72 >35** | REJECT K5 |
| CAT | +20,78 % ✓ | 54,7 ✓ | -0,75 pp marginal NEG | n/a | pending | REJECT K3 |
| AMZN | +4,26 % ✓ | 66,7 ✓ nah 70 | **-4,27 pp NEG FAIL** | Mo 176 % ✓ | pending | REJECT K3 |
| GOOGL | +10,57 % ✓ | 60,3 ✓ | **-8,98 pp NEG FAIL** | Mo 135 % ✓ | pending | REJECT K3 |
| META/TSLA | **-5,92 % / -6,38 % K1 FAIL Death-Cross** | — | — | — | — | REJECT K1 |

**Slot 1/2 KW32 bleibt OFFEN.** UAL Top-RS-Kandidat weiter blockiert durch K4-Vol-Rebound-FAIL (Mo 73 % Rebound nicht bestätigt, live 4 % pro-rata weit unter 120 %-Cap). ABBV Top-RS-Kandidat blockiert durch RSI-Cool-off unter 50 (K2 FAIL erstmals vs KW31 wo K2 ✓) + XLV-Cap-Klärung Owner-pending 5. Woche in Folge.

### Blackout-Monitoring
- **AAPL HT+2 heute Blackout beendet** — Std-V1 291,51 wieder alleine primär, Puffer +3,84 % SICHER, Übergang regelkonform.
- **LLY HT-1 letzter Tag vor Report Mi 05.08. BMO** — Blackout-V1_neu 1.134,20 weiter **UNTERSCHRITTEN -1,20 %** vs Live 1.120,645 (marginal verschlechtert vs Pre -0,94 %). Std-V1 1.098,38 SICHER +2,03 %. Strategie-Lock CLAUDE.md Rule 3 → nur Std bindend → HALTEN. Report morgen früh vor Open bringt Post-Blackout-Recovery oder V1-Escalation.

### Entscheidung
**KEIN Trade Market Open 09:38 ET.** V1-V6 alle 5 SICHER Std, keine Sell-/Limit-Order platziert, 0 offene Orders. Kein Kauf (alle 10 Watchlist-Kandidaten REJECT/SKIP wegen K2/K3/K4/K5/Earnings/XLV-Cap-Blockern). Käufe KW32 0/2 unverändert. Slot 1/2 KW32 primär OFFEN, Re-Check Midday 13:00 ET (UAL K4-Session-Vol Halbtags-belastbar bei anhaltendem Momentum, MRK Post-Report-Reaktion nach 10:00 ET).

### ClickUp + PushNotification
- **ClickUp Prio 4 Routine-Log** (Fallback bei Kontingent-Fehler: Memory-Only-Log)
- **PushNotification Silence-Rule Routine** (Std-V1 alle SICHER, kein V-Trigger, kein Kauf, kein Cap-Alert, LLY BO -1,20 % innerhalb Konvention-Toleranz vs Vorwochen -1,49 % Midday KW32 Tag 1; Owner-Sichtbarkeit nicht gerechtfertigt für unverändertes Muster, Report morgen bringt Post-Blackout-Klärung).

**Nächste Routine:** Di 04.08. 13:00 ET Midday Stop-Check — LLY Blackout-V1 Recovery-Watch (Std sicher aber BO -1,20 %), UAL K4-Session-Vol Halbtags-belastbar Re-Check + Live-Momentum, AAPL Std-V1 alleine primär Verifikation, MRK Post-Report-Reaktion nach 10:00 ET.

---

## Market Close 16:00 ET — 2026-08-03 (Mo, KW32 Tag 1 FINAL) — KEIN Trade, 5 V1-V6 SICHER Vollcheck EOD-Bars, Daily -0,403 % [GRÜN], SPY +1,464 % Post-Weekend-Rally-Fortsetzung, Alpha -1,87 pp NEG, Watchlist Di 04.08. UAL #1 XLI RS +33,61 pp #1 TOP, Slot 1/2 KW32 OFFEN, VIX 16,02 stark reduziert

### Alpaca /v2/account Close
- equity: **95.972,60 $** (vs last_equity 96.360,90 = **-0,403 %** Daily) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (59,09 %, unverändert seit GS-Stop 27.07.)
- MV Close: 39.261,58 $ (5 Pos, -359,21 vs Open 39.620,79 = -0,907 %)
- **DD vs ATH 100.066,47: -4,091 %** [GRÜN, verschlechtert vs Midday -4,043 %]
- **Weekly KW32 Tag 1 = Daily -0,403 %** [GRÜN, weit von Cap -5 %]
- **SPY Close Alpaca IEX 757,72** vs Fr Close 746,79 = **+1,464 % Post-Weekend-Rally-Fortsetzung** (Snapshot Daily-Bar h=758,58 l=749,21 vol=1,93M verified) [Crash-Filter INAKTIV]
- Perplexity SPY divergiert bei -0,13 % → **IEX bindend** (Konsistenz Bull-Konvention)
- **Alpha vs SPY -1,867 pp NEGATIV**
- **VIX Perplexity 16,02** [GRÜN <25, deutlich reduziert vs Fr ~19,8 = Vola-Entspannung Post-Weekend]
- 0 offene Orders

### V1-V6 Portfolio-Vollcheck EOD-Bars (alle 5 SICHER Std)
| Symbol | Close | chg | P/L | Std-V1 Puffer | Blackout BO | EMA-Diff | RSI | RS_4w |
|--------|-------|-----|-----|---------------|-------------|----------|-----|-------|
| LLY   | 1.121,00 | **-2,42 % Worst** | **-6,11 % Worst** | +2,06 % **ENGSTE** | **-1,16 % UNTERSCHRITTEN** verb. vs Midday -1,49 % | +11,69 % | **30,8 Oversold** | -7,52 pp NEG |
| AAPL  | 303,03 | -1,90 % | -4,36 % | +3,95 % | **+0,67 % kritisch nah 0 %** HT+1 letzter Tag | +10,89 % | 41,3 | -3,84 pp NEG |
| V     | 365,67 | -0,13 % | +2,38 % | +11,28 % | n/a | **+3,92 % engster aber positiv verb. vs Fr +2,45 %** | 59,8 Cool-off vs Fr 66,2 | +1,47 pp |
| UNH   | 415,36 | **+0,23 % Best** | +3,43 % | +12,43 % | n/a | +13,35 % | 43,2 | -1,51 pp NEG |
| JPM   | 352,64 | +0,24 % | **+5,97 % Best P/L** | +15,18 % | n/a | +5,49 % | 58,8 | +3,53 pp |

**V3/V4 kein Trigger** (max JPM +5,97 % << 20 %-TP1). **V5 alle Golden Cross intakt** (V engster +3,92 % positiv). **V6 alle SICHER** (max RSI V 59,8 << 80; LLY RSI 30,8 nah Oversold, kein Sell-Signal; UND-Bedingung mit RS<0 nicht erfüllt für alle da RSI << 80). **→ KEIN V-Trigger, KEINE Sell-/Limit-Order für Di 04.08. platziert.**

### Blackout-Monitoring
- **AAPL HT+1 letzter Tag** Puffer +0,67 % kritisch nah 0 % verschlechtert vs Midday +1,94 %. **Ab morgen Di 04.08. HT+2 → Blackout beendet, Std-V1 291,51 wieder alleine primär.**
- **LLY HT-2** Blackout-V1_neu 1.134,20 weiter UNTERSCHRITTEN -1,16 % (verbessert vs Midday -1,49 %). Strategie-Lock CLAUDE.md Rule 3 → nur Std-V1 1.098,38 bindend → HALTEN. Bis Mi 05.08. BMO Earnings-Release primäre Bull-Konvention-Referenz.
- **MRK Di 04.08. BMO HT-0** — nicht Portfolio-Position, aber blockiert Kauf-Kandidat.

### Watchlist Di 04.08. K1-K3 (Alpaca IEX EOD Mo 03.08.)
| Kandidat | Sektor | Close | chg heute | K1 EMA-Diff | K2 RSI | K3 RS_63d | K4 Vol Mo | K5 | Prio |
|----------|--------|-------|-----------|-------------|--------|-----------|-----------|-----|------|
| **UAL** | XLI | 128,40 | **+5,84 %** | +9,26 % ✓ | 52,8 ✓ | **+33,61 pp #1 TOP** ✓ | 72 % FAIL Rebound-Watch Di | vorbekannt ✓ RevGr 16 %, FwdPE 14,8x, Next-Earnings Okt 2026 ✓ | **#1 NEUE XLI-Diversifikation Airlines Post-Rally** |
| UNP | XLI | 290,94 | -0,28 % | +9,85 % ✓ | 57,4 ✓ | +4,90 pp ✓ | Fr 116 % borderline, Mo Momentum-Bruch | Q2 26 +11,53 % ✓ (SEC 10-Q) | #2 Backup Re-Check Di Pre-Market |
| EOG | XLE | 144,85 | -2,55 % | +8,34 % ✓ | 58,0 ✓ | -0,11 pp marginal NEG | Fr 84 % FAIL | vorbekannt ✓ FwdPE 9,98 + RevGr +15,63 % | #3 XLE Rebound-Watch |
| ABBV | XLV | 250,42 | -0,18 % | +7,44 % ✓ | 53,4 ✓ | **+16,86 pp #1 XLV** ✓ | Fr 135 % ✓ | Q2 26 +10,16 % ✓ marginal | **#4 BLOCKIERT XLV-Cap-Klärung Owner pending 4. Woche in Folge** |
| GE | XLI | 369,00 | +2,46 % | +7,80 % ✓ | 53,1 ✓ | +23,61 pp #2 ✓ | 79,8 % FAIL | **FAIL FwdPE 44,72 >35 persistent** | **BLOCKIERT K5-FAIL** |
| META | XLC | 590,15 | +6,03 % | **-4,87 % FAIL** Death-Cross-nah | 47,5 | -8,20 pp | 127 % ✓ | — | **REJECT K1-FAIL** |
| TSLA | XLY | 322,08 | +3,50 % | **-6,51 % FAIL** | 30,2 <50 FAIL | -22,73 pp FAIL | 65 % FAIL | — | **REJECT K1/K2/K3-FAIL** |
| CAT | XLI | 831,04 | +2,02 % | +16,19 % ✓ | **34,8 <50 FAIL** | **-11,83 pp FAIL** | 104 % FAIL | — | **REJECT K2/K3-FAIL** |
| MRK | XLV | 130,21 | — | — | — | — | — | — | **BLOCKIERT Earnings Di 04.08. BMO HT-0** |

**Slot 1/2 KW32 bleibt OFFEN** — **UAL Prio 1 wenn K4-Vol-Rebound Di Pre-Market/Open belastbar + K5-Multi-Source-Verifikation bestätigt**, XLV-Cap-Klärung Owner-Prio 1 blockiert weiter ABBV Top-RS-XLV-Kandidat.

### Sektor-Struktur Close
| Sektor | Anteil | Pos | Notes |
|--------|--------|-----|-------|
| XLV | 19,74 % | UNH 10,39 + LLY 9,35 | LLY-Sell-off senkt marginal |
| XLF | 11,39 % | JPM 1,10 + V 10,29 | stabil |
| XLK | 9,79 % | AAPL | Post-Earnings-Konsolidierung |
| Cash | 59,09 % | — | unverändert seit GS-Stop 27.07. |

### Guardrails Close (alle GRÜN + 2 WARN)
```
Daily -3 %:   -0,403 %                                  [GRÜN]
Weekly -5 %:  KW32 Tag 1 = Daily -0,403 %              [GRÜN]
DD -15 %:     -4,091 % vs ATH 100.066,47                [GRÜN]
VIX >30:      16,02 (Perplexity)                        [GRÜN, deutlich reduziert vs Fr]
Crash SPY -5%: SPY +1,464 %                             [INAKTIV]
Käufe KW32:   0/2 [Slot 1/2 + 2/2 OFFEN]
Blackout:     LLY HT-2 (V1_neu 1134.20 UNTERSCHRITTEN -1,16 %) [WARN]
              AAPL HT+1 letzter Tag Puffer +0,67 % kritisch     [WARN]
              MRK HT-0 morgen Di 04.08. BMO (nicht Position)    [Kauf-Sperre MRK]
```

### Nächster Check
Di 04.08. **08:30 ET Pre-Market KW32 Tag 2** — **UAL K4-Vol-Rebound + K5-Multi-Source-Verifikation Prio 1** (falls Vol Pre-Market/Open belastbar → Kauf-Kandidat Slot 1/2), MRK BMO Earnings-Report + Post-Earnings-Reaktion, **LLY HT-1 letzte Bewegung vor Report Mi**, **AAPL Blackout HT+2 Beendigung + Std-V1 291,51 wieder alleine primär**, XLV-Cap-Klärung Owner-Watch (blockiert ABBV 4. Woche).

---

## Market Open 09:42 ET — 2026-08-03 (Mo, KW32 Tag 1) — KEIN Kauf (alle 6 Watchlist-Kandidaten REJECT/SKIP), Daily -0,030 % [GRÜN], SPY +0,639 % Post-Weekend-Rally, LLY Blackout-V1 unterschritten -0,28 % (Std sicher +2,97 %), Slot 1/2 KW32 OFFEN

### Kaufsignal-Scan Ergebnis (Slot 1/2 KW32)

| Kandidat | Sektor | Live | K1 | K2 | K3 | K4 | K5 | Entscheidung |
|----------|--------|------|-----|-----|-----|-----|-----|--------------|
| **UNP** | XLI | 290,94 (-0,28 % vs SPY +0,64 % Divergenz -0,92 pp) | +9,85 % ✓ | RSI 57,4 ✓ | +4,90 pp ✓ | **Fr 116 % <120 % FAIL** + Live 22 % pro-rata | Q2 2026 +11,53 % ✓ (SEC 10-Q) | **SKIP K4-FAIL + Momentum-Bruch** |
| **ABBV** | XLV | 250,42 (-0,18 %) | +7,44 % ✓ | RSI 53,4 ✓ | **+16,86 pp #1 Top** ✓ | Fr 135 % ✓ | Q2 2026 +10,16 % ✓ marginal (SEC 10-Q, FwdPE 13,72) | **SKIP XLV-Cap Owner-Klärung pending** (Strategie-Lock Rule 3) |
| **EOG** | XLE | 144,85 (-2,55 %) | +8,34 % ✓ | RSI 58,0 ✓ | **-0,11 pp marginal NEGATIV FAIL** | Fr 84 % FAIL | vorbekannt ✓ | **REJECT K3-FAIL** |
| **AMZN** | XLY | 285,78 (+5,37 % Gap-Up) | +3,01 % ✓ | **RSI 75,6 >70 FAIL** | +2,20 pp ✓ | — | — | **REJECT K2-FAIL Overbought** |
| **GOOGL** | XLC | 370,39 (+3,94 % Gap-Up) | +10,60 % ✓ | RSI 62,0 ✓ | **-8,31 pp << 0 FAIL** | — | — | **REJECT K3-FAIL** |
| **MRK** | XLV | 130,21 | — | — | — | — | — | **BLOCKIERT Earnings Di 04.08. BMO HT-1** |

### K5 Multi-Source Verifikation (Perplexity 2 Queries)
- **UNP**: Erste Query fehlerhaft (+4,0 % Q1 2026). Zweite Query mit SEC 10-Q: **Q2 2026 Rev $6.864M vs Q2 2025 $6.154M = +11,53 % YoY** → K5 PASS (aber irrelevant wegen K4-FAIL)
- **ABBV**: Q2 2026 Rev **$16.990M vs Q2 2025 $15.423M = +10,16 %** (SEC Form 8-K + Press Release) → K5 PASS marginal (0,16 pp über Cap)

### V1-V6 Portfolio-Vollcheck Live (alle 5 SICHER Std)
- V1 min: LLY +2,97 % ENGSTE Std (Blackout-V1_neu 1.134,20 UNTERSCHRITTEN -0,28 % aber Strategie-Lock → HALTEN)
- V5 min EMA-Diff: V +2,75 % (positiv), alle Golden Cross intakt
- V6 max RSI: V 69,3 (< 80)
- V3/V4 max P/L: JPM +6,03 % (<< 20 %)

### Guardrails Live (alle GRÜN)
```
Daily -3 %:   -0,030 % (essentiell flat) [GRÜN]
Weekly -5 %:  KW32 Tag 1 frisch [GRÜN]
DD -15 %:     -3,378 % vs ATH [GRÜN]
VIX >30:      19,31 Pre-Read [GRÜN]
Crash SPY -5%: SPY +0,639 % [INAKTIV]
Käufe KW32:   0/2 [Slot 1/2 + 2/2 OFFEN]
Blackout:     LLY HT-2 (V1_neu 1134.20 UNTERSCHRITTEN), AAPL HT+1 auslaufend [WARN]
```

### Nächster Check
Mo 03.08. **13:00 ET Midday Stop-Check** — LLY Blackout-V1 Stabilisierung Prio 1, UNP K4-Session-Vol Halbtags-belastbar Re-Check (falls Momentum-Bruch abgefangen), AAPL Blackout HT+1 auslaufend, XLV-Cap-Klärung Owner-Watch.

---

## Pre-Market 08:30 ET — 2026-08-03 (Mo, KW32 Tag 1) — 8/8 GRÜN + 2 WARN (AAPL BO HT+1 auslaufend +3,42 % / LLY BO HT-2 +2,36 % ENGSTE), VIX 19,31 [GRÜN <25], SPY Futures +0,88 % vs Fr Close 746,79, Daily Pre +0,360 %, DD -3,357 %, MRK BLOCKIERT (Earnings Di 04.08. BMO HT-1), Watchlist UNP/ABBV/EOG + AMZN/GOOGL neu Prüfen, Kauf-Slots KW32 2/2 frisch

### Alpaca /v2/account Pre-Market
- portfolio_value: **96.707,72 $** (vs last_equity 96.360,90 = **+0,360 %** Pre) [GRÜN, Cap -3 %]
- cash: **56.707,49 $** (58,64 %, unverändert seit GS-Stop 27.07.)
- MV Pre: **40.000,53 $** (5 Pos, +311,36 vs Fr Close 39.689,17 = +0,784 % Post-Weekend-Recovery, alle 5 positiv change_today)
- last_equity: 96.360,90 $ (Alpaca EOD-Reconciliation Fr)
- **DD vs ATH 100.066,47: -3,357 %** [GRÜN, verbessert vs Fr Close -3,667 %]
- Konsistenz mit memory/portfolio.md Fr Close: **✓** (Equity Delta +311,06 = 5 Pos-Recovery, Cash exakt gleich)
- **0 offene Orders** Alpaca

### Positionen Live Pre (5) — change_today alle positiv
| Symbol | Qty | Price Pre | change_today | P/L $ | P/L % | Std-V1 Puffer | Blackout-V1 | BO-Puffer |
|--------|-----|-----------|--------------|-------|-------|----------------|-------------|-----------|
| AAPL   | 31  | 311,31    | +0,777 %     | -171,94 | -1,75 % | +6,79 % (291,51) | 301,02 HT+1 auslaufend | **+3,42 %** |
| JPM    |  3  | 355,02    | +0,918 %     | +66,72  | +6,68 % | +15,96 % (306,16) | n/a | n/a |
| LLY    |  8  | 1.161,00  | +1,058 %     | -263,10 | -2,76 % | +5,70 % (1.098,38) | 1.134,20 HT-2 | **+2,36 % ENGSTE** |
| UNH    | 24  | 416,38    | +0,478 %     | +355,41 | +3,69 % | +12,71 % (369,44) | n/a | n/a |
| V      | 27  | 370,51    | +1,196 %     | +359,97 | +3,73 % | +12,75 % (328,60) | n/a | n/a |

### Guardrails (alle GRÜN Pre)
```
Daily Loss Cap  -3 %:  +0,360 % (vs last_equity 96.360,90)                   [GRÜN]
Weekly Loss Cap -5 %:  KW32 Tag 1 frisch, Reset erfolgt                       [GRÜN]
Drawdown -15 %:        -3,357 % vs ATH 100.066,47                             [GRÜN]
Drawdown -20 %:        nicht aktiv                                             [GRÜN]
VIX-Filter > 30:       VIX 19,31 (Perplexity Live)                            [GRÜN, <25 volle Pos-Size]
Crash-Filter SPY -5 %: SPY Fr +0,696 %, SPY Pre +0,88 % Futures               [INAKTIV]
Käufe diese Woche:     0 / 2 (frisch KW32)                                    [2 Slots frei]
Earnings-Blackout:     LLY Q2 CY26 Aug 5-7 est. → **HT-2** (V1_neu 1.134,20)  [WARN]
                       AAPL Q3 FY26 released 30.07. → HT+1 auslaufend         [WARN]
                       MRK Tue 04.08. BMO → HT-1 → **Kauf-Sperre MRK**        [SKIP]
Max. neue Käufe:       2 pro Woche                                            [0/2]
```

### Markt-Daten Pre-Market (Perplexity Live)
```
VIX:                19,31            [GRÜN <25]
SPY Futures:        E-mini +0,44 % (~+0,88 % Index-Äquiv. vs Fr Close 746,79)  → ~753 SPY-Äquiv.
10Y Treasury:       4,28 %
DXY:                n/a Live (keine Perplexity-Angabe)
Sentiment:          neutral-positiv (Tech/AI-führung Pre)
```

### Makro-Ereignisse Woche (Perplexity, mit Skepsis wg. FOMC-Konflikt)
```
Mo 03.08.:  keine Top-Tier-Events
Di 04.08.:  MRK Earnings BMO, PFE + CAT + MCD + AMGN Earnings
Mi 05.08.:  LLY Earnings (est.) BMO, CVS + DIS + FOXA Earnings, **evtl. FOMC-Nachwehen** (Perplexity meldet FOMC Mi — aber FOMC 29.07. war letzte Sitzung, nächste erst Sep → Skepsis, keine Aktion)
Do 06.08.:  CPI Juli (Perplexity-Angabe — historisch aber typisch 10-13. → Skepsis)
Fr 07.08.:  PPI + NFP (NFP = 1. Fr Aug, plausibel ✓)
```

### Earnings-Blackouts (offene Positionen)
- **LLY** Q2 CY26 est. **Aug 5-7 BMO** → **HT-2 (heute)** aktiv, Blackout-V1_neu **1.134,20** = -5,00 % Kaufkurs, primäre Stop-Referenz bis Report
- **AAPL** Q3 FY26 released 30.07. AMC → **HT+1** letzter Tag Blackout-Konvention, morgen normal V1 291,51 (Standard)
- JPM/UNH/V: keine Earnings 10 Handelstage

### Watchlist Mo Open Kaufsignal-Scan (KW32 Slot 1/2)
| Kandidat | Sektor | Fr Close | Pre-Read | Status | Prio |
|----------|--------|----------|----------|--------|------|
| **UNP**  | XLI    | 292,15   | K1-K3 ✓ Fr EOD, K4 116 % borderline, K5 zwingend Multi-Source Open | XLI 0 % neue Diversifikation | **#1** |
| **ABBV** | XLV    | 250,88   | K1-K3 ✓ Fr EOD (RS +14,73 pp #2), K4 135 % ✓, K5 zwingend | **XLV-Cap-Warnung** (bereits 19,88 %, ABBV pusht +10 % → ~30 %) | **#2** conditional |
| **EOG**  | XLE    | 148,65   | K1-K3 ✓ Fr EOD, K4 84 % FAIL Watch, K5 vorbekannt ✓ | XLE 0 % neue Diversifikation | **#3** K4-Rebound-Watch |
| **MRK**  | XLV    | 130,21   | K1-K3 ✓ Fr EOD (RS +15,32 pp #3), K4 69 % FAIL | **BLOCKIERT Earnings Di 04.08. BMO HT-1** | **SKIP** |
| **AMZN** | XLY    | 271,46   | Weekly +16,96 % KW31, Post-Q2-Rally, K1-K3 zu prüfen Mo | Earnings est. 6-13.08. → **Blackout-Risk** | **#4 conditional** — Earnings-Datum vor Kauf klären |
| **GOOGL**| XLC    | 356,06   | Weekly +11,36 %, Post-Q2-Rebound (schon released) | K1-K3 zu prüfen, KW30-V1-Präzedenz -12,65 % → **Fill-Day-Puffer** | **#5** conditional |

### Cascade-Framework Check
AAPL BO-Puffer +3,42 % (auslaufend HT+1) + LLY BO-Puffer +2,36 % ENGSTE (aktive HT-2) — beide **über 1 %-Konvention-Grenze** → Cascade-Framework INAKTIV, Kauf-Slot 1/2 grundsätzlich zulässig. K4/K5-Multi-Source am Open zwingend, Sektor-Cap-Check ABBV vor XLV-Push.

### Entscheidung Pre-Market 2026-08-03
**Kaufscan bei Market Open 09:30 ET: JA (mit Bedingungen).**
Begründung: Alle 8 Guardrails GRÜN, VIX 19,31 < 25 (volle Pos-Size 10 %), SPY Futures +0,88 % kein Crash-Filter, LLY/AAPL Blackout-Puffer > 1 % (Cascade-Framework INAKTIV), 2 frische Kauf-Slots KW32, 0 offene Orders. MRK blockiert (Earnings HT-1), AMZN conditional bis Earnings-Datum bestätigt. Primär-Watch: UNP (XLI-Diversifikation), ABBV (XLV-Cap-Diskussion beim Open klären), EOG (K4-Rebound Watch).

**Prio-1 Watches Market Open:**
1. LLY Blackout HT-2 Puffer +2,36 % (verschlechtert vs Fr Close +1,18 %? — check Live Open)
2. AAPL Blackout HT+1 auslaufend Post-Earnings-Konsolidierung
3. K4/K5-Multi-Source UNP/ABBV/EOG für Sauberkeitsprüfung
4. XLV-Cap-Diskussion ABBV: Owner-Klärung ob 3. XLV zulässig (aktuell 19,88 % → ~30 %)

### Notification
```
ClickUp Prio 4 Routine-Log wird gesendet (Pre-Market Standard-Priorität).
PushNotification: KEINE (kein Cap-Alert, kein <1 %-Blackout, positive Pre-Metrics — Silence-Rule Routine).
```

---

## Market Close 16:00 ET — 2026-07-31 (Fr, KW31 Tag 5 FINAL) — 5 V1-V6 SICHER Vollcheck EOD-Bars, AAPL Blackout-Puffer +2,70 % Recovery (Std +6,05 %), LLY Blackout +1,18 % (Std +4,48 % ENGSTE), Daily -1,090 % / Alpha -1,785 pp NEG, Weekly KW31 FINAL -1,159 %, Watchlist Mo UNP/ABBV/MRK/EOG

**Alpaca Clock:** is_open=false, 16:02 ET, next_open Mo 03.08. 09:30 ET.

**Alpaca /v2/account Market Close:**
- portfolio_value: **96.396,66 $** (vs Do Close 97.458,61 = **-1,090 %** Daily) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (58,83 %, unverändert seit 27.07. GS-Stop)
- MV Close: 39.689,17 $ (5 Positionen, +217,90 vs Midday 39.471,27 = AAPL-Recovery intraday +7,72 $/Share dominant)
- last_equity: 97.340,70 $ (Alpaca EOD-Reconciliation)
- ATH 100.066,47 | DD **-3,667 %** [GRÜN, verbessert vs Midday -3,885 %]
- Weekly KW31 Tag 5 FINAL **-1,159 %** (vs Fr 24.07. Close 97.526,60) [GRÜN, weit von Cap -5 %]
- Open Orders: **KEINE** (0 offene Orders, KEINE Sell-/Limit-Order für Mo 03.08.)

**Marktdaten Close (Alpaca IEX Bars 31.07. 16:00 ET):**
- **SPY Close 746,79** (Alpaca IEX Snapshot Last-Trade 15:59:59 ET verified, Daily bar o=744,685 h=748,86 l=737,70 c=746,79 v=1.909.254 vw=744,10) vs Do Close 741,63 = **+0,696 %** Post-FOMC-Recovery-Fortsetzung [Crash-Filter INAKTIV]
- **⚠️ Perplexity divergiert bei SPY 741,69 chg -0,13 %** — konservative Verifikation: Alpaca IEX Bar + Snapshot Last-Trade + Daily Volume 1,91M zeigen konsistent 746,79 → **IEX bindend für Konsistenz mit prior routines (Weekly-Baseline auch IEX)**
- **VIX Perplexity n/a Fr Close** (Perplexity kann nicht sourcen), Do-Referenz ~19,8 [GRÜN <25]
- SPY 20d perf +0,26 %, SPY 63d perf +3,95 % (für RS_4w/RS_63d Berechnungen)
- **Alpha vs SPY -1,785 pp NEGATIV** (Portfolio-Recovery unzureichend gegen SPY-Beta-Rally, LLY -0,60 % + UNH -1,71 % dämpfen, JPM +0,28 % nur teilweise Kompensation)

**V1-V6-Vollcheck Market Close EOD-Bars (Positionen sortiert nach ENGSTEM V1-Std-Puffer):**

| Sym  | Close  | Qty | Entry     | P/L %      | chg vs Do Close Bar | V1-Std   | V1-Puffer      | V1-Blackout | Blackout-Puffer   | V5 EMA-Diff | V6 RSI | RS_4w vs SPY | Blackout |
|------|--------|-----|-----------|------------|---------------------|----------|----------------|-------------|-------------------|-------------|--------|--------------|----------|
| LLY  | 1.147,61 | 8 | 1.193,89 | **-3,88 % Worst P/L** | -0,60 % | 1.098,38 | **+4,48 % ENGSTE Std** | 1.134,20 | +1,18 % ENGSTE Blackout, marginal Recovery vs Midday +0,78 % | +11,98 % ✓ | 49,0 ✓ | -5,37 pp NEG | 🔴 HT-3 aktiv, HT-2 ab Mo, V6 sicher via UND |
| AAPL |   309,15 | 31 |  316,857 | -2,43 %    | **-7,31 % Worst chg** Post-Earnings Sell-off Do Bar 333,07 | 291,51 | +6,05 % Std | 301,02 | **+2,70 % Recovery** vs Midday +0,111 % razor-thin | +10,30 % ✓ | 43,6 ✓ | -0,10 pp marginal NEG | 🟡 HT+0 Post-Earnings-Konsolidierung, V1_neu wieder klar über |
| V    |   366,13 | 27 |  357,178 | +2,51 %    | -0,04 %             | 328,60   | +11,42 %       | —           | —                 | **+2,45 % engster** | 66,2 max | +0,96 pp | inaktiv (Q3 ✓ RELEASED) |
| UNH  |   415,99 | 24 |  401,57  | +3,59 %    | -1,71 % XLV-Sell-off | 369,44  | +12,60 %       | —           | —                 | +13,20 % ✓ | 48,7 ✓ | -2,73 pp NEG | inaktiv, V6 sicher via UND |
| JPM  |   351,79 |  3 |  332,78  | **+5,71 % Best P/L** | +0,28 % Best chg | 306,16 | +14,90 % | —      | —                 | +5,28 % ✓ | 60,7 ✓ | +5,01 pp     | inaktiv |

**V1-V6 Detail-Check:**
- **V1 (Stop -8 %):** 5 SICHER per strategy.md Std-V1, min LLY +4,48 % ENGSTE, alle über 4 % Puffer.
- **V2 (Trailing -12 %):** 5 SICHER, Trailing weniger restriktiv als Std-V1.
- **V3 (P/L ≥ 20 %):** max JPM +5,71 % << 20 % — kein Trigger.
- **V4 (P/L ≥ 35 %):** kein Trigger.
- **V5 (Death Cross EMA50<EMA200):** 5 SICHER, alle Golden Cross intakt. V engster EMA-Diff +2,45 % positiv (marginal verschlechtert vs Do +2,92 %). AAPL trotz Post-Earnings-Sell-off -7,31 % noch +10,30 % Puffer bis Death Cross.
- **V6 (RSI>80 UND RS_4w<0):** 5 SICHER. Max RSI V 66,2 (verschlechtert vs Do 63,3). RSIs unter 70. LLY RS_4w -5,37 pp NEG aber RSI 49 → V6 sicher via UND-Bedingung. UNH -2,73 pp NEG aber RSI 49. AAPL -0,10 pp marginal NEG aber RSI 44.

**→ KEIN V1-V6-Trigger per strategy.md. KEINE Sell-/Limit-Order für Mo 03.08. platziert. 0 offene Orders.**

**Guardrails Market Close 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     -1,090 %                                                [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 FINAL -1,159 %                                     [GRÜN]
3. Drawdown-Alarm (-15 %):    -3,667 %                                                [GRÜN]
4. Drawdown-Stopp (-20 %):    -3,667 %                                                [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,696 %                                            [INAKTIV]
6. VIX-Filter (>30):          VIX Do-Referenz ~19,8 (Fr Perplexity n/a)               [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT+0 +2,70 % + LLY HT-3 +1,18 %                    [WARN 2, beide >1 %]
8. Max Käufe KW31 FINAL:      0/2                                                     [GRÜN]
```

**Watchlist Mo 03.08. K1-K3 aus Alpaca IEX Bars EOD Fr 31.07. (K4/K5 zwingend Multi-Source Pre-Market/Open Mo):**

| Kand | Sektor | Fr-Close | K1 EMA-Diff | K2 RSI | K3 RS_63d | K4 Vol Fr (%) | K5 | Prio | Notiz |
|------|--------|----------|-------------|--------|-----------|---------------|----|------|-------|
| **UNP** | XLI | 292,15 chg +0,94 % | +10,26 % ✓ | 59,1 ✓ | +4,45 pp ✓ | 116 % ✓ borderline | zwingend Multi-Source | **#1** | XLI 0 % **neue Diversifikation Rails-Wide-Moat** |
| **ABBV** | XLV | 250,88 chg **-2,57 %** | +6,10 % ✓ | 57,4 ✓ | **+14,73 pp #2** ✓ | **135 % ✓ Best K4** | zwingend Multi-Source | **#2** | **XLV-Cap-Warnung** bei 19,88 %, 3. XLV pusht auf ~29 % Grenze |
| **MRK** | XLV | 130,21 chg +0,32 % | +12,40 % ✓ | 63,7 ✓ | **+15,32 pp #3** ✓ | **69 % FAIL** | zwingend Multi-Source | **#3** | K4-Rebound-Watch Mo Session-Vol, XLV-Cap-Warnung |
| **EOG** | XLE | 148,65 chg **+2,10 %** | +9,72 % ✓ | 67,1 ✓ knapp | +1,75 pp ✓ marginal | **84 % FAIL** | **vorbekannt ✓** FwdPE 9,98 + RevGr +15,63 % | **#4** | K5-known K4-Rebound-Watch, XLE 0 % Diversifikation |
| CVS | XLV | 104,42 chg -0,65 % | +15,51 % ✓ | 50,6 ✓ | +21,40 pp #1 ✓ | 117 % ✓ borderline | **REJECT K5 FAIL persistent** RevGr +6,2 % Q1 26 | REJECT | Nur wenn K5 sich ändert |
| BAC | XLF | 61,98 chg +0,36 % | +7,26 % ✓ | 63,2 ✓ | +11,97 pp ✓ | **50 % FAIL** | nicht recherchiert | SKIP | K4 FAIL Fr |

**Watchlist morgen (Mo 03.08.):** UNP (XLI-Diversifikation, K4/K5 zwingend), ABBV (XLV-Cap-Warnung + K5 zwingend), MRK (K4-Rebound-Watch + K5 zwingend), EOG (K5-known K4-Rebound-Watch).

**REJECT-persistente Kandidaten (nicht neu prüfen bis Datenänderung):**
- CVS (K5 FAIL Q1 26 RevGr +6,2 %)
- GE (K5 FwdPE 44,72 >35), PSX (K5 RevGr +6,9 %), HON (K5 RevGr +2,4 %), DE (K5 RevGr +9,6 %), D (K5 +7,49 %)
- NEE/DUK (K3 FAIL persistent), MSFT (K1 EMA-Diff -8,72 % FAIL + RSI >70), META (K1 FAIL + RSI 32,1), CAT (RSI 34,9 <50 + RS -12,49 pp Fr)

**Cascade-Framework über Wochenende:** AAPL Blackout HT+1 auslaufend Mo (Post-Earnings-Konsolidierung noch aktiv aber Puffer wieder komfortabel), LLY HT-2 ab Mo primäre Stop-Referenz bis Mi 05.08. BMO Earnings-Release. Neue Kauf-Entscheidung Mo Pre-Market/Open frühestens nach K4/K5-Multi-Source-Verifikation + XLV-Cap-Prüfung.

**Sektor-Struktur Market Close:**
- XLV: **19,88 %** (UNH 10,36 + LLY 9,52, marginal reduziert vs Midday 20,00 %)
- XLF: 11,35 % (JPM 1,09 + V 10,26)
- XLK: 9,94 % (AAPL, Recovery vs Midday 9,71 %)
- Cash: 58,83 %

**Earnings-Blackout-Kalender:**
- **AAPL Q3 FY26 ✓ RELEASED** (Do 30.07. AMC), Blackout-V1_neu 301,02 aktiv bis Fr Close, **HT+1 ab Mo 03.08. auslaufend**. Post-Earnings-Konsolidierung mit intraday Recovery-Fortsetzung (+7,72 $/Share von Midday 301,355 auf Close 309,15).
- **LLY Q2 CY26 Mi 05.08.2026 BMO**, HT-3 aktiv seit HEUTE (Fr 31.07.), HT-2 ab Mo 03.08., HT-1 Di 04.08., Earnings-Release Mi 05.08. BMO. Blackout-V1_neu 1.134,20 primäre Stop-Referenz.

**Nächster Check:** Mo 03.08. 08:30 ET Pre-Market KW32 Tag 1 — **K4/K5-Multi-Source UNP/ABBV/MRK/EOG (XLV-Cap-Check ABBV/MRK), AAPL Blackout HT+1 auslaufend + LLY Blackout HT-2 primäre Stop-Referenz, VIX-Recalc Perplexity, SPY-Rally-Fortsetzung Watch, Weekly-Reset KW32.**

---

## Market Open 09:42 ET — 2026-07-31 (Fr, KW31 Tag 5) — 🔴 AAPL Blackout-V1_neu 301,02 intraday UNTERSCHRITTEN 09:41 ET Dip 300,535 (Recovery 301,71 razor-thin +0,23 %), LLY Blackout HT-3 aktiviert Puffer +0,62 % ENGSTE, kein V-Trigger per strategy.md, Slot 1/2 KW31 bleibt OFFEN (alle 4 Kandidaten REJECT/SKIP)

**Alpaca Clock:** is_open=true, 09:42 ET, next_open Mo 03.08. 09:30 ET.

**Alpaca /v2/account Market Open Live:**
- portfolio_value: **96.117,58 $** (vs Do Close 97.458,61 = **-1,376 %** Daily) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (58,99 %, unverändert)
- MV Live: 39.410,09 $ (5 Positionen, -1.341,03 $ vs Do Close 40.751,12 = -3,290 %, AAPL-Sell-off dominant)
- last_equity: 97.340,70 $ (Alpaca EOD-Reconciliation)
- ATH 100.066,47 | DD **-3,947 %** [GRÜN, verschlechtert vs Do -2,606 %]
- Weekly KW31 Tag 5 **-1,444 %** (vs Fr 24.07. Close 97.526,60) [GRÜN, weit von Cap -5 %]
- Open Orders: **KEINE**

**Marktdaten Live (Alpaca IEX 09:39-09:42 ET):**
- **SPY Live 743,51** (vs Do Close 741,63 = **+0,253 %** milde Post-FOMC-Konsolidierung) [Crash-Filter INAKTIV]
- **VIX Perplexity 17,98** (leicht Vola-Rückgang vs Do Close ~19,8) [GRÜN <25 volle Pos-Size]
- **Alpha vs SPY -1,629 pp NEGATIV** (AAPL -9,72 % Post-Earnings Guidance-Sell-off dominant)

**🔴 AAPL Blackout-V1_neu 301,02 Bull-Konvention intraday UNTERSCHRITTEN 09:41 ET:**
- Dip auf **300,535 $** (Alpaca IEX 13:41:02 UTC = 09:41:02 ET)
- Recovery **301,71 $** um 09:42 ET (razor-thin über Blackout-V1_neu = +0,23 %)
- Standard-V1 291,51 SICHER (aktueller Puffer +3,50 %)
- **Strategie-Lock (CLAUDE.md Rule 3):** Nur strategy.md V1 bindend, Bull-Konvention Blackout-V1_neu ist konservative Zusatz-Watch. → **HALTEN, keine Sell-Order.**
- Owner-Push Prio 1 zwingend wegen Blackout-Konvention-Bruch + zeitgleicher LLY Blackout-Aktivierung ENGSTE +0,62 %.

**V1-V6-Vollcheck Market Open Live (Positionen sortiert nach ENGSTEM V1-Std-Puffer):**

| Sym  | Live 09:42 | Qty | Entry     | P/L %    | chg vs Do Close | V1-Std   | V1-Blackout | V1-Puffer                              | Blackout-Status |
|------|------------|-----|-----------|----------|-----------------|----------|-------------|----------------------------------------|-----------------|
| AAPL |  301,71    | 31  |  316,857  | **-4,78 % Worst P/L** | **-9,72 % Worst chg** Guidance-Sell-off | 291,51 | **301,02** | **Std +3,50 % ENGSTE / Blackout +0,23 % razor-thin** | **🔴 HT+0 Post-Earnings, Blackout-V1 intraday gebrochen** |
| LLY  | 1.141,25   |  8  | 1.193,89  | **-4,41 % Worst P/L 2** | -1,36 % | 1.098,38 | **1.134,20** | Std +3,90 % / **Blackout +0,62 % ENGSTE Blackout** | **🔴 HT-3 AKTIVIERT ab HEUTE — V1_neu primäre Stop-Referenz** |
| V    |  362,68    | 27  |  357,178  | +1,54 %  | -0,98 %         | 328,60   | —           | +10,36 %                               | inaktiv (Q3 ✓ RELEASED) |
| UNH  |  419,59    | 24  |  401,57   | +4,49 %  | -1,20 % XLV-Sell-off | 369,44 | —         | +13,57 %                               | inaktiv |
| JPM  |  350,55    |  3  |  332,78   | +5,34 %  | **-0,09 % Best chg** | 306,16 | —         | +14,50 %                               | inaktiv |

**V1-V6 Sub-Check:**
- **V1:** **5 SICHER per strategy.md**, min AAPL +3,50 %. Blackout-V1_neu (Bull-Konvention) AAPL intraday-Break — konservative Watch, kein Sell-Trigger per Strategie-Lock.
- **V2-V6:** kein Trigger. V engster V5-Spread +3,96 %, max RSI V ~63 << 80. AAPL RSI ~40 nach -9,72 %.

**→ KEINE Sell-/Limit-Order platziert. 0 offene Orders.**

**Guardrails Market Open 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     -1,376 % vs Do Close                                    [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 5 -1,444 %                                     [GRÜN]
3. Drawdown-Alarm (-15 %):    -3,947 % vs ATH 100.066,47                              [GRÜN]
4. Drawdown-Stopp (-20 %):    -3,947 %                                                [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Live +0,253 %                                       [INAKTIV]
6. VIX-Filter (>30):          VIX 17,98                                               [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT+0 Blackout-V1 intraday gebrochen + LLY HT-3     [WARN 2 aktiv]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                              [GRÜN]
```

**Kaufsignal-Scan Watchlist Live (K1-K4 aus Alpaca IEX Bars 30.07. Close, K5 Perplexity Multi-Source):**

| Kand | Sektor | Do-Close | K1 EMA50/200 | K2 RSI | K3 RS_63d | K4 Vol Do (%) | K5 | Entscheidung |
|------|--------|----------|--------------|--------|-----------|---------------|----|--------------|
| CVS  | XLV    | 105,11   | +17,23 % ✓   | 52,2 ✓ | +21,57 pp ✓ #1 | 157 % ✓ | **FAIL** Q1 2026 RevGr **+6,2 % YoY** < 10 % (Perplexity, Annual +7,8 %). FwdPE 11,95-13,68 ✓. | **REJECT K5 definitiv** |
| BAC  | XLF    |  61,76   | +8,18 % ✓    | 61,7 ✓ | +12,86 pp ✓    | **74 % FAIL** | nicht recherchiert (nicht ökonomisch bei K4-FAIL) | **SKIP K4-FAIL** |
| UNP  | XLI    | 289,42   | +10,41 % ✓   | 51,9 ✓ | +5,38 pp ✓     | **99 % FAIL** | nicht recherchiert | **SKIP K4-FAIL** |
| EOG  | XLE    | 145,59   | +9,90 % ✓    | 61,4 ✓ | +0,94 pp ✓     | **81 % FAIL** | vorbekannt ✓ FwdPE 9,98 + RevGr +15,63 % | **SKIP K4-FAIL** |

**K4-Session-Vol pro-rata 12 Min nach Open nicht belastbar** — für Halbtags-K4-Bewertung: Midday-Recheck 13:00 ET.

**Cascade-Framework Aktivierung — defensiv NO BUY:**
- AAPL Blackout-Puffer +0,23 % + LLY Blackout-Puffer +0,62 % — beide unter 1 % zur Bull-Konvention-Grenze
- Selbst wenn Kandidat qualifiziert wäre: neue Position reduziert Cash-Puffer, während 47,4 % MV (AAPL+LLY) unter Blackout-Stress stehen
- **NO BUY unabhängig von Signal-Qualität**, Slot 1/2 KW31 bleibt OFFEN
- Re-Check Midday 13:00 ET: K4 dann belastbar, AAPL/LLY-Stabilisierungs-Watch

**Sektor-Struktur Market Open Live:**
- XLV: 19,98 % (UNH 10,47 + LLY 9,51)
- XLF: 11,29 % (JPM 1,10 + V 10,19)
- XLK: 9,73 % (AAPL gedrückt von 10,63 % Do Close durch -9,72 %)
- Cash: 58,99 %

**Earnings-Blackout-Kalender:**
- **AAPL Q3 FY26 ✓ RELEASED** — Blackout-V1_neu 301,02 konservativ aktiv bis Fr Close, **intraday 09:41 ET UNTERSCHRITTEN**.
- **LLY Q2 CY26 Mi 05.08.2026 BMO** — Blackout HT-3 **AKTIVIERT ab HEUTE**, V1_neu 1.134,20 primäre Stop-Referenz.

**Nächster Check:** Fr 31.07. 13:00 ET Midday Stop-Check — **Prio 1 AAPL/LLY Blackout-Puffer Stabilisierung**, K4-Halbtags-Recheck Watchlist (falls Portfolio stabilisiert), XLV-Sell-off Fortsetzung Watch.

---

## Pre-Market 08:36 ET — 2026-07-31 (Fr, KW31 Tag 5) — 🔴 AAPL Post-Earnings-Sell-off Pre-Market -8,10 % (Guidance-Supply-Constraints), LLY-Blackout HT-3 aktiviert V1_neu 1.134,20 Puffer +1,48 % ENGSTE, alle 5 V1-V6 SICHER

**Alpaca Clock:** is_open=false, 08:36 ET, next_open Fr 31.07. 09:30 ET.

**Alpaca /v2/account Pre-Market:**
- portfolio_value: **96.473,12 $** (vs Do Close 97.458,61 = **-1,011 %** Daily) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (58,78 %, unverändert)
- MV Pre: 39.765,63 $ (5 Positionen, -985,49 $ vs Do Close 40.751,12 = -2,418 %, AAPL-Sell-off treibt)
- last_equity: 97.340,70 $ (Alpaca EOD-Reconciliation, -118 $ vs Memory Do Close 97.458,61 marginal)
- ATH 100.066,47 | DD **-3,591 %** [GRÜN, verschlechtert vs Do -2,606 %]
- Weekly KW31 Tag 5 **-1,081 %** (vs Fr 24.07. Close 97.526,60, -1.053,48 $, verschlechtert vs Do +0,070 %) [GRÜN, weit von Cap -5 %]
- Open Orders: **KEINE**

**Marktdaten Pre-Market (Alpaca IEX 08:24-08:34 ET):**
- **SPY Pre 743,68** (vs Do Close 741,63 = **+0,276 %** milde Post-FOMC-Recovery-Konsolidierung) [Crash-Filter INAKTIV]
- **VXX letzte 21,91** (Do 19:59 ET Close, VIX-Proxy ~19-20)
- **VIX Do Close ~19,8** (Memory-Referenz, Perplexity keine belastbare Pre-Zahl) [GRÜN <25]
- **Alpha vs SPY -1,287 pp NEGATIV** (AAPL -8,10 % Post-Earnings dämpft Portfolio-Beta massiv trotz SPY-Konsolidierung positiv)
- 10Y Yield: Perplexity nicht verfügbar, Memory-Referenz Do Pre ~4,12 %

**🔴 AAPL Q3 FY26 Post-Earnings Do 30.07. AMC (kritisches Signal):**
- **Beat auf Ist-Zahlen:** Umsatz **109,42 Mrd. $** (+16 % y/y, Konsens 108,86 Mrd. beat), **EPS 2,02 $** (+29 % y/y, Konsens 1,89 beat)
- **iPhone-Rekord:** 54,3 Mrd. $ (+22 % y/y), 49,6 % Umsatzanteil
- **Services:** 30,7 Mrd. $ (+12 %)
- **Guidance Sep-Q Sell-off-Trigger:** Umsatzwachstum 9-11 % y/y + Bruttomarge 47-48 %, ABER **Supply Constraints + FX Headwinds** (Reuters "disappoints with forecast dogged by supply chain struggles")
- **Pre-Market-Reaktion:** 307,14 $ (Alpaca IEX 08:34) vs Do Close 334,20 = **-8,10 %** massiver Guidance-Sell-off
- **AAPL Blackout HT-0 gestern gefeuert → heute Post-Earnings-Konsolidierungs-Watch** (Bull-Convention Blackout V1_neu 301,02 bleibt aktiv bis Fr Close, konservativ)

**V1-V6-Vollcheck Pre-Market (Positionen sortiert nach ENGSTEM V1-Puffer):**

| Sym  | Pre Kurs | Qty | Entry     | P/L %    | chg vs Do Close | V1-Std   | V1-Blackout | V1-Puffer                     | Blackout-Status |
|------|----------|-----|-----------|----------|-----------------|----------|-------------|-------------------------------|-----------------|
| LLY  | 1.151,00 |  8  | 1.193,89  | **-3,59 % Worst P/L verschlechtert** | -0,34 % | 1.098,38 | **1.134,20** | **+1,48 % ENGSTE Blackout** / +4,79 % Std | **🔴 AKTIV HT-3 Q2 CY26 Mi 05.08. BMO — V1_neu = primäre Stop-Referenz heute** |
| AAPL |  307,14  | 31  |  316,857  | **-3,06 % Post-Earnings** | **-8,10 % Worst chg** Guidance-Sell-off | 291,51 | **301,02** | **+2,03 % Blackout Post-Earnings** / +5,36 % Std | **🔴 HT+0 Post-Earnings Konsolidierung, Blackout-V1 konservativ aktiv bis Fr Close** |
| V    |  366,21  | 27  |  357,178  | +2,53 %  | -0,02 %         | 328,60   | —           | +11,44 %                      | inaktiv Post-Earnings (Q3 CY26 Di 28.07. AMC ✓ RELEASED) |
| JPM  |  351,00  |  3  |  332,78   | +5,47 %  | +0,04 %         | 306,16   | —           | +14,65 %                      | inaktiv (Q3 ~Mitte Okt) |
| UNH  |  420,586 | 24  |  401,57   | +4,74 %  | -0,21 %         | 369,44   | —           | +13,84 %                      | inaktiv (Q3 ~Mitte Okt) |

**V1-V6 Sub-Check (aus EOD-Bars Do 30.07.):**
- **V1:** **5 SICHER**, aber AAPL +2,03 % Blackout ENGSTE + LLY +1,48 % Blackout ENGSTE-2 — beide unter 3 %-Puffer. Bei Open weiterer Rutsch → V1-Trigger möglich (Watch-Item Prio 1).
- **V2 Trailing:** V-52w-Hoch 369,12 × 0,88 = 324,83 → 366,21 SAFE. Keine anderen Trailing-Trigger.
- **V3 (+20 %):** max JPM +5,47 % / UNH +4,74 % / AAPL Post-Earnings jetzt negativ << 20 %, kein Trigger.
- **V4 (+35 %):** kein Trigger.
- **V5 Death Cross:** aus Do EOD-Bars alle 5 SICHER, engster V +2,92 %. Post-Sell-off AAPL EMA50 könnte sich morgen leicht drücken aber >EMA200 bei aktuellem Kurs 307 vs ca. EMA200 ~278.
- **V6 (RSI>80 UND RS<0):** max RSI V 63,3 aus Do EOD, AAPL RSI wird nach -8,10 % deutlich fallen (Do 61,5 → geschätzt ~40 heute) — V6 nicht ausgelöst.

**→ KEINE Sell-/Limit-Order für heute Open platziert. Kein V1-Break, aber Puffer AAPL/LLY beide < 3 % → **Market-Open-Watch Prio 1 auf AAPL 301,02 und LLY 1.134,20** (Blackout-V1_neu als primäre Stop-Referenz).

**Guardrails Pre-Market 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     -1,011 % vs Do Close                                   [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 5 -1,081 %                                    [GRÜN]
3. Drawdown-Alarm (-15 %):    -3,591 % vs ATH 100.066,47                              [GRÜN]
4. Drawdown-Stopp (-20 %):    -3,591 %                                                [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Pre +0,276 %                                        [INAKTIV]
6. VIX-Filter (>30):          VIX ~19,8 Do Close-Referenz                             [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT+0 Post-Earnings + LLY HT-3 Aktivierung          [WARN 2 aktiv]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                              [GRÜN]
```

**Earnings-Blackout-Kalender:**
- **AAPL Q3 FY26 Do 30.07. AMC ✓ RELEASED** (EPS 2,02 / Umsatz 109,42 Mrd., beat aber Guidance-enttäuschung) — Blackout-V1 301,02 konservativ aktiv bis Fr Close.
- **LLY Q2 CY26 Mi 05.08.2026 BMO** → **Blackout ab HEUTE Fr 31.07. HT-3 aktiv** V1_neu 1.134,20 = Puffer +1,48 % (aktueller Kurs 1.151). Primäre Stop-Referenz für Watching heute + Mo/Di.
- V (Q3 CY26 Di 28.07. AMC ✓ RELEASED), JPM/UNH Q3 CY26 ~Mitte Okt weit weg.
- **Watchlist CVS/BAC/UNP/EOG:** Perplexity keine belastbare Earnings-Termin-Bestätigung 3 HT-Fenster, aber vorherige Recherche keine Konflikte → K5-Multi-Source zwingend beim Kauf-Scan Open.

**Makro-Events heute (Perplexity keine Konsens-Zahlen):**
- Erwartet: **PCE Juni Deflator** (Fed-Inflations-Ziel-Barometer), **Employment Cost Index Q2**, **Michigan Consumer Sentiment final Juli**
- Vor Börsenöffnung Vol-Katalysator PCE 08:30 ET (falls Termin bestätigt) → SPY-Pre-Market kann kippen

**Watchlist Fr 31.07. Market Open — K1-K3 EOD-Bars Do 30.07. bestätigt, K4/K5 zwingend Multi-Source (unverändert vs Do Close):**

| Kand | Sektor | Do-Close | K1 EMA50/200 | K2 RSI | K3 RS_63d | K5-Status |
|------|--------|----------|--------------|--------|-----------|-----------|
| CVS  | XLV    | 105,11   | +17,69 % ✓   | 52,2 ✓ | +21,57 pp #1 ✓ | K5 zwingend Multi-Source (XLV-Cap-Warnung 19,95 % → 3. XLV pusht auf ~29 %) |
| BAC  | XLF    | 61,76    | +7,68 % ✓    | 61,7 ✓ | +12,86 pp ✓ | K5 zwingend Multi-Source |
| UNP  | XLI    | 289,42   | +11,45 % ✓   | 51,9 ✓ | +5,38 pp ✓ | K5 zwingend Multi-Source (neue XLI Sektor-Diversifikation) |
| EOG  | XLE    | 145,59   | +11,29 % ✓   | 61,4 ✓ | +0,94 pp ✓ | K5 **vorbekannt ✓** (FwdPE 9,98 + RevGr +15,63 %) |

**Sektor-Struktur Pre-Market (AAPL-Sell-off senkt XLK):**
- XLV: 20,03 % (UNH 10,46 + LLY 9,55)
- XLF: 11,34 % (JPM 1,09 + V 10,25)
- XLK: 9,87 % (AAPL, gedrückt von 10,63 % Do Close durch -8,10 %)
- Cash: 58,78 %

**Entscheidung Market-Open-Scan: JA — aber Prio 1 AAPL/LLY-Puffer-Watch vor Kauf-Scan.**
Slot 1/2 KW31 offen, Watchlist K1-K3 sauber, VIX <25, SPY +0,28 %. Bei Open: (1) AAPL Puffer-Monitoring 301,02, (2) LLY Puffer-Monitoring 1.134,20, (3) K4/K5-Multi-Source für CVS/BAC/UNP/EOG. Kauf nur bei sauberer Blackout-Aktivierung und stabilem Portfolio (kein Cascade-Sell-off).

**Nächster Check:** Fr 31.07. 09:30 ET Market Open + Kaufsignal-Scan — **AAPL Open-Konsolidierung V1_neu 301,02 Watch**, **LLY Blackout HT-3 V1_neu 1.134,20 Watch**, Watchlist CVS/BAC/UNP/EOG K4/K5-Multi-Source-Verifikation.

---

## Market Close 16:00 ET — 2026-07-30 (Do, KW31 Tag 4) — Post-FOMC-Recovery SPY +1,653 % Close-Fest, LLY XLV-Sell-off -4,38 % Worst-Fortsetzung dominant, 5 V1-V6 SICHER Vollcheck, Watchlist Fr CVS/BAC/UNP/EOG K1-K3 ✓

**Alpaca Clock:** is_open=false, 16:02 ET, next_open Fr 31.07. 09:30 ET.

**Alpaca /v2/account Market Close 16:00 ET:**
- portfolio_value: **97.458,61 $** (vs Mi Close 97.970,67 = **-0,523 %** Daily, vs last_equity 98.276,07 = -0,832 %) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (58,19 %, unverändert)
- MV Close: 40.751,12 $ (5 Positionen, +51,49 $ vs Midday 40.699,63, -512,06 $ vs Mi Close 41.263,18 = -1,240 %)
- Buying_power: 340.933,11 $ (Paper-Margin)
- ATH 100.066,47 | DD **-2,606 %** [GRÜN, minimal verbessert vs Open -2,758 %]
- Weekly KW31 Tag 4 **-0,070 %** (vs Fr Close 97.526,60, -67,99 $) [GRÜN, weit von Cap -5 %]
- Open Orders: **KEINE**

**Marktdaten Close (Alpaca IEX 16:00 ET):**
- **SPY Close 741,63** (vs Mi Close 729,57 = **+1,653 % Post-FOMC-Recovery Close-Fest**) [Crash-Filter INAKTIV]
- **VIX ~19,8** (Perplexity Close-Read, leicht Vola-Anstieg vs Pre 15,8 aber [GRÜN <25])
- **Alpha vs SPY -2,176 pp NEGATIV** (LLY XLV-Sell-off dominant, UNH+JPM-Rebound unzureichend)

**V1-V6-Vollcheck EOD-Bars 30.07. (Alpaca IEX 229d):**

| Sym  | Close    | Qty | Entry     | P/L %    | chg_today | V1-Puffer   | V5 EMA50/200 Diff | V6 RSI(14) | RS_4w vs SPY |
|------|----------|-----|-----------|----------|-----------|-------------|-------------------|------------|--------------|
| LLY  | 1.157,00 |  8  | 1.193,89  | **-3,09 % Worst P/L** weiter verschlechtert | **-4,382 % Worst chg** | **+5,34 % ENGSTE weiter verschlechtert** | +11,95 % ✓ | 47,0 ✓ | **-2,51 pp NEG** (RSI<80 → V6 sicher) |
| AAPL |  334,20  | 31  |  316,857  | +5,47 %  | -1,18 %   | +11,02 % Blackout HT-0 | +10,90 % ✓ | 61,5 ✓ | +13,67 pp |
| V    |  366,27  | 27  |  357,178  | +2,55 %  | -0,67 %   | +11,46 %    | **+2,92 % engster Spread ✓** | 63,3 max ✓ | +4,79 pp |
| JPM  |  350,85  |  3  |  332,78   | +5,43 %  | **+1,78 % Best chg** XLF | +14,60 %    | +5,73 % ✓ | 60,1 ✓ | +6,05 pp |
| UNH  |  424,686 | 24  |  401,57   | **+5,76 % Best P/L** | +0,98 % XLV-Divergenz | +14,95 % | +15,31 % ✓ | 51,6 ✓ | -0,61 pp NEG (RSI<80 → V6 sicher) |

**5 SICHER — kein V1-V6-Trigger, keine Sell-Order, 0 offene Orders.**

**Watchlist Fr 31.07. — K1-K3 EOD-Bars 30.07. Close bestätigt, K4/K5 zwingend Pre-Market/Open:**

| Kand | Sektor | Close  | chg %  | K1 EMA50/200 Diff | K2 RSI | K3 RS_63d vs SPY | K5 Status |
|------|--------|--------|--------|-------------------|--------|-------------------|-----------|
| CVS  | XLV    | 105,11 | -0,72 %| +17,69 % ✓        | 52,2 ✓ | **+21,57 pp #1 Top-Rank** ✓ | K5 zwingend Multi-Source (XLV-Cap knapp) |
| BAC  | XLF    |  61,76 | +1,13 %| +7,68 % ✓         | 61,7 ✓ | +12,86 pp ✓       | K5 zwingend Multi-Source |
| UNP  | XLI    | 289,42 | -1,01 %| +11,45 % ✓        | 51,9 ✓ | +5,38 pp ✓        | K5 zwingend Multi-Source (neue Sektor-Diversifikation) |
| EOG  | XLE    | 145,59 | -0,25 %| +11,29 % ✓        | 61,4 ✓ | +0,94 pp ✓        | K5 **vorbekannt ✓** (FwdPE 9,98 + RevGr +15,63 %) |

**Begründung Watchlist:**
- **CVS RS #1** aber XLV-Sektor-Cap knapp (aktuell 19,95 %, 3. XLV pusht auf ~29 % OK aber Watch)
- **BAC** Post-FOMC Bank-Rebound intakt, XLF-Diversifikation
- **UNP** XLI Rails 0 % neue Sektor-Diversifikation, Wide-Moat-Qualität
- **EOG** K5 vorbekannt sauber, Rebound-Watch nach 27.-29.07. Konsolidierung
- **REJECT-persistente Kandidaten:** GE/PSX/HON/DE/D (K5 FAIL), NEE/DUK (K3 FAIL), MSFT (heute chg +15,48 % aber K1 FAIL + RSI 72,1 >70 nach Q4-Earnings-Bid), META (chg -8,29 % + K1 FAIL), CAT (RSI 34,9 + RS FAIL)

**Post-FOMC Marktreaktion Close:**
- SPY +1,653 % Close-Fest, Recovery-Bestätigung nach Mi -1,515 % hawkish-Sell-off
- VIX ~19,8 leicht Vola-Anstieg vs Pre 15,8, aber [GRÜN <25]
- Sektor-Rotation: **XLV verkauft (LLY -4,38 %, JNJ/MRK/ABBV -1,5 bis -3,0 %)**, XLF stark (JPM +1,78 %, BAC +1,13 %), XLK gemischt (MSFT +15,48 % nach Q4 Earnings, AAPL -1,18 % Pre-Earnings-Give-back, META -8,29 % Post-Earnings)
- **AAPL Q3 FY26 Earnings AMC ~5:00 PM ET HEUTE nach Close** → Post-Earnings-Reaktion Fr Pre-Market
- **AMZN Q2 CY26 Earnings AMC HEUTE** (nicht Portfolio)

**Guardrails Close 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     -0,523 % vs Mi Close                                 [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 4 -0,070 %                                  [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,606 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,606 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Close +1,653 % Recovery                          [INAKTIV]
6. VIX-Filter (>30):          VIX ~19,8                                            [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT-0 Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE    [WARN aktiv nach Close]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                            [GRÜN]
```

**Entscheidung Market Close Do 30.07.:**
- **KEIN Trade heute** (kein Buy, kein Sell)
- **KEINE Sell-/Limit-Order für Fr 31.07. platziert** (5 V1-V6-Vollcheck SICHER)
- **Slot 1/2 + 2/2 KW31 bleiben OFFEN** — Re-Check Fr Pre-Market/Open mit CVS/BAC/UNP/EOG K4/K5-Verifikation
- **AAPL Post-Earnings-Watch** — Blackout HT-0 aktiv, V1_neu 301,02 Puffer +11,02 %, Fr Pre-Market K5-Multi-Source
- **LLY Watch** — Puffer +5,34 % ENGSTE (weiter verschlechtert vs Midday +5,80 %), **Blackout ab morgen Fr 31.07. HT-3 aktiv V1_neu 1.134,20** wird primäre Stop-Referenz (Close 1.157,00 = +1,97 % Puffer wenn Blackout aktiv, marginal aber positiv)
- **ClickUp Tagesbericht Prio 3 (Normal)** wird gesendet (negativer Tag mit LLY -4,38 % + Alpha -2,18 pp NEG)
- **PushNotification Prio 2 Owner** — LLY -4,38 % + Puffer +5,34 % ENGSTE + Blackout-Aktivierung morgen HT-3 rechtfertigen Owner-Sichtbarkeit (nicht Silence, weil Watch-Item mit Handlungsrelevanz)

**Nächste Routine:** Fr 31.07. 08:30 ET Pre-Market — AAPL Post-Earnings-Reaktion K5-Multi-Source, LLY Blackout HT-3 Aktivierung V1_neu 1.134,20 primäre Stop-Referenz, Watchlist CVS/BAC/UNP/EOG K4/K5-Multi-Source-Verifikation, XLV-Sell-off Konsolidierungs-Prüfung.

---

## Market Open 09:37 ET — 2026-07-30 (Do, KW31 Tag 4) — Post-FOMC-Recovery SPY +0,801 % bestätigt, XLV-Sektor-Sell-off breit (5 XLV -1,5 bis -3,0 %), 5 V1-V6 SICHER Live (LLY chg -2,745 % Worst + P/L -1,23 % Worst verschlechtert), LEVEL 0 SKIP JNJ/MRK/ABBV wg. Gap-Down bei Open

**Alpaca Clock:** is_open=true, 09:37 ET, next_close Do 30.07. 16:00 ET.

**Alpaca /v2/account Market Open 09:37 ET:**
- portfolio_value: **97.306,66 $** (vs Mi Close 97.970,67 = **-0,678 %** Give-back, vs last_equity 98.276,07 = -0,987 %) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (58,28 %, unverändert)
- MV Live: 40.599,17 $ (5 Positionen, -664,01 $ vs Mi Close 41.263,18 = -1,609 %)
- Buying_power: 340.507,62 $ (Paper-Margin)
- ATH 100.066,47 | DD **-2,758 %** [GRÜN, verschlechtert vs Pre -2,488 %]
- Weekly KW31 Tag 4 **-0,225 %** (vs Fr Close 97.526,60, -219,94 $) [GRÜN, weit von Cap -5 %]
- Open Orders: **KEINE**

**Marktdaten Live (Alpaca IEX 09:37 ET):**
- **SPY Live 735,41** (Alpaca IEX latest trade) vs Mi Close 729,57 = **+0,801 % Post-FOMC-Recovery bestätigt** [Crash-Filter INAKTIV]
- **VIX ~15,8** (Pre-Market carry-over, keine frische Bar) [GRÜN <25 volle Pos-Size]
- **Alpha vs SPY -1,479 pp NEGATIV** (Portfolio-XLV/XLK/XLF-Positionen alle im Give-back trotz SPY-Recovery)

**V1-V6-Vollcheck Live (Market Open Kurse + Mi EOD-Bars für V5/V6):**

| Sym  | Live-Cur | Qty | Entry     | P/L %    | chg_today | V1-Puffer   | V5 (EMA50/200 Mi EOD) | V6 (RSI Mi EOD) |
|------|----------|-----|-----------|----------|-----------|-------------|----------------------|-----------------|
| LLY  | 1.179,18 |  8  | 1.193,89  | **-1,23 % Worst P/L** verschlechtert | **-2,745 % Worst chg** | **+7,36 % ENGSTE** vs Std | 1.137,11>1.016,80 ✓ | 58,9 ✓ |
| AAPL |  332,44  | 31  |  316,857  | **+4,92 %** Best P/L | -1,641 % | +10,44 % vs Blackout | 308,93>279,15 ✓ | 67,2 (max, << 80) |
| V    |  365,43  | 27  |  357,178  | +2,31 %  | -0,895 %  | +11,20 %    | 342,87>334,50 ✓ engster Spread +2,50 % | 66,8 |
| UNH  |  414,07  | 24  |  401,57   | +3,11 %  | -1,545 % XLV-Sell-off | +12,07 %    | 406,18>354,79 ✓ | 50,8 |
| JPM  |  346,28  |  3  |  332,78   | +4,06 %  | **-0,320 % Best chg** XLF-Recovery | **+13,05 %** | 330,57>314,96 ✓ | 55,3 |

**5 SICHER — kein V1-V6-Trigger, keine Sell-Order, 0 offene Orders.**

**Kaufsignal-Scan Watchlist Market Open — LEVEL 0 SKIP alle 3 XLV-Kandidaten:**

| Kand | Open   | Live   | Mi Close | Gap %   | vs SPY  | K4-Session-Vol | K5 status | Entscheidung |
|------|--------|--------|----------|---------|---------|---------------|-----------|--------------|
| JNJ  | 259,45 | 259,33 | 265,67   | -2,34 % | -3,14 pp | 14.547 / avg20 394.756 (3,68 % bei ~1,79 % Session-Zeit) pro-rata unzuverlässig | nicht verifiziert | **REJECT LEVEL 0 Momentum-Bruch** |
| MRK  | 128,195| 128,82 | 130,40   | -1,69 % | -2,49 pp | 7.120 / avg20 316.358 (2,25 %) unzuverlässig | nicht verifiziert | **REJECT LEVEL 0 Momentum-Bruch** |
| ABBV | 255,66 | 258,865| 263,62   | **-3,02 % worst** | **-3,82 pp** stark negativ | 7.523 / avg20 266.590 (2,82 %) unzuverlässig | nicht verifiziert | **REJECT LEVEL 0 Momentum-Bruch STARK trotz RS #1** |

**Begründung LEVEL 0 SKIP alle 3:**
- K1-K3 alle 3 ✓ (Pre-Read Mi EOD-Bars bestätigt), aber intraday-Momentum am potenziellen Kauftag stark negativ vs SPY +0,801 % Post-FOMC-Recovery → Momentum-Quality-Thesis verletzt analog EOG 27./28./29.07. + GS Fill-Day+7-Reversal
- K4-Session-Vol pro-rata bei ~1,79 % Session-Zeit (7 Min) nicht belastbar (Muster wie EOG 27.07.)
- K5 (FwdPE + RevGr Multi-Source) nicht verifiziert wg. LEVEL 0 SKIP (Perplexity-Call nicht ökonomisch)
- **XLV-Sektor-Sell-off Post-FOMC breit** (UNH -1,545 % + LLY -2,745 % + JNJ -2,34 % + MRK -1,69 % + ABBV -3,02 % + XLV-Sektor allgemein rot) → auch ohne Sektor-Cap-Warnung wäre 3. XLV-Position falsches Timing
- ABBV RS #1 +30,94 pp bleibt strukturell attraktiv, aber Fill-Day-Timing bei -3,02 % Gap-Down = sofort Fill-Day+1-Reversal-Risk

**Post-FOMC Marktreaktion Update:**
- SPY +0,801 % Recovery bestätigt (vs Pre +0,65 % → intraday leicht besser)
- Aber Sektor-Rotation: XLV wird verkauft, XLF (JPM Best chg -0,320 %) leicht besser als SPY, XLK (AAPL -1,641 %) Give-back Pre-Earnings
- Beobachtung: Rotation aus defensiven Healthcare in zyklische Sektoren nach hawkish-Fed?

**Guardrails Market Open 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     -0,678 % vs Mi Close                                 [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 4 -0,225 %                                  [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,758 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,758 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   Live +0,801 % Recovery                               [INAKTIV]
6. VIX-Filter (>30):          VIX ~15,8                                            [GRÜN <25]
7. Earnings-Blackout (3 HT):  AAPL HT-0 Q3 FY26 Do 30.07. AMC HEUTE V1_neu 301,02  [WARN]
8. Max Käufe KW31:            0/2 (Slot 1/2 bleibt OFFEN + 2/2 offen)              [GRÜN]
```

**Entscheidung Market Open Do 30.07.:**
- **KEIN Kauf ausgeführt** (LEVEL 0 SKIP JNJ/MRK/ABBV)
- **KEINE Sell-Order** (5 V1-V6 SICHER, LLY -1,23 % P/L noch +7,36 % vom V1-Stop)
- **Slot 1/2 KW31 bleibt OFFEN** — Re-Check Fr 31.07. Pre-Market (Post-AAPL-Earnings + Post-XLV-Sell-off-Konsolidierung)
- **AAPL HT-0 Watch** — V1_neu 301,02 sicher aktiv Puffer +10,44 %, AMC ~5:00 PM ET
- **LLY Watch** — Puffer +7,36 % ENGSTE nach Post-FOMC-Sell-off, Blackout Aktivierung Fr 31.07. HT-3
- **ClickUp Routine-Log Prio 4** wird gesendet
- **PushNotification Silence** (empty run: kein Trade, alle 5 V1-V6 SICHER, LEVEL 0 SKIP korrekt begründet, XLV-Sell-off im Rahmen aber Puffer sicher → Silence-Rule)

**Nächste Routine:** Do 30.07. 13:00 ET Midday Stop-Check — LLY Puffer +7,36 % ENGSTE Watch, AAPL AMC-Countdown, XLV-Sell-off-Fortsetzung Watch, potenzielles Slot-1/2-Rebound-Fenster.

---

## Pre-Market 08:37 ET — 2026-07-30 (Do, KW31 Tag 4) — Post-FOMC-Konsolidierung SPY Pre +0,65 % Recovery, VIX 15,8 (-6 % vs Vortag), 5 V1-V6 SICHER Pre-Read (LLY Pre-Read -1,82 % Worst chg engste), AAPL HT-0 Q3 FY26 AMC HEUTE, LLY Blackout Aktivierung Fr 31.07 HT-3 (Präzisierung: heute HT-4), Kaufsignal-Scan JNJ/MRK/ABBV bei Market Open erlaubt (max 1 XLV wg. Sektor-Cap)

**Alpaca Clock:** is_open=false, 08:37 ET, next_open Do 30.07. 09:30 ET.

**Alpaca /v2/account Pre-Market 08:37 ET:**
- portfolio_value: **97.576,68 $** (vs Mi Close 97.970,67 = **-0,402 %** Overnight-Delta, vs last_equity 98.276,07 = -0,712 %) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (58,12 %, unverändert)
- MV Pre: 40.868,88 $ (5 Positionen, -394,30 $ vs Mi Close 41.263,18)
- Buying_power: 341.263,69 $ (Paper-Margin)
- ATH 100.066,47 | DD **-2,488 %** [GRÜN, marginal verschlechtert vs Mi Close -2,094 %]
- Weekly KW31 Tag 4 **+0,051 %** (vs Fr Close 97.526,60, +50,08 $) [GRÜN, weit von Cap -5 %]
- Open Orders: **KEINE**

**Marktdaten Pre-Market:**
- **SPY Pre 734,30** (Alpaca IEX latest trade 08:33 ET) vs Mi Close 729,57 = **+0,65 % Post-FOMC-Recovery** [Crash-Filter INAKTIV]
- **VIX 15,8** (Perplexity, -6 % vs Vortag) [GRÜN <25 volle Pos-Size]
- **VXX 23,44** (Alpaca IEX letzte Notierung Mi 19:59 ET, keine frische Vor-Open-Bar)
- **10Y Treasury Yield ~4,12 %** (Perplexity)

**V1-V6 Pre-Read (Pre-Market Kurse, EOD-Vollcheck bei Market Close):**

| Sym  | Pre-Cur  | Qty | Entry     | P/L %    | chg_today | V1-Std   | V1-Blackout    | V1-Puffer    | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|----------|----------------|--------------|-----------------|
| LLY  | 1.188,00 | 8   | 1.193,89  | **-0,49 %** | **-1,82 % Worst chg** | 1.098,38 | — (HT-4 noch inaktiv) | **+8,16 % ENGSTE** vs Std | inaktiv HT-4 (Q2 CY26 Mi 05.08. BMO, Blackout ab Fr 31.07. HT-3 aktivierbar V1_neu 1.134,20 = +4,74 % dann) |
| AAPL |  335,13  | 31  |  316,857  | +5,77 %  | -0,91 %  | 291,51 | **301,02 🔴** | **+11,33 %** Blackout HT-0 | **🔴 AKTIV HT-0 Q3 FY26 Do 30.07. AMC ~5:00 PM ET** |
| V    |  368,25  | 27  |  357,178  | +3,10 %  | -0,13 %  | 328,60 | — | +12,06 % | inaktiv Post-Earnings-Reaktion (Q3 Di 28.07. AMC ✓) |
| UNH  |  416,50  | 24  |  401,57   | +3,72 %  | -0,97 %  | 369,44   | —              | +12,74 %     | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  345,70  |  3  |  332,78   | +3,88 %  | +0,29 % Best chg  | 306,16   | —              | +12,91 %     | inaktiv (Q3 ~Mitte Okt) |

**V1-Puffer Übersicht (eng→weit):** LLY **+8,16 % ENGSTE** vs Std (P/L -0,49 % Overnight-Give-back, Puffer verschlechtert vs Mi Close +9,41 % um -1,25 pp) | AAPL +11,33 % Blackout HT-0 | V +12,06 % | UNH +12,74 % | JPM +12,91 %

**V5/V6-Pre-Read (aus Mi EOD-Bars, keine neue EOD-Bar heute):** Alle Golden Cross intakt (V EMA-Spread +2,50 % engster aber positiv), max RSI AAPL 67,2 << 80. V3/V4: max P/L AAPL +5,77 % << 20 %. **Keine Sell-/Limit-Order platziert** (nicht dringend Pre-Market ohne Break, EOD-Vollcheck bei Market Close).

**Earnings-Kalender heute + nächste 3 HT (Perplexity Multi-Source):**
- **AAPL Q3 FY26 Do 30.07. AMC ~5:00 PM ET HEUTE HT-0** (Portfolio-Position, V1_Blackout 301,02 aktiv) — Post-Earnings-Reaktion Fr 31.07. Watch
- AMZN Q2 CY26 Do 30.07. AMC (nicht im Portfolio, aber SPY-Vol-Impact)
- **KEINE anderen Portfolio-Positionen im 3-HT-Fenster:** JPM/UNH ~Mitte Oktober, V bereits released Di 28.07., **LLY Q2 CY26 Mi 05.08. BMO** (Blackout ab Fr 31.07. HT-3 aktivierbar V1_neu 1.134,20 — Präzisierung: HT-Zählung Mi 05.08.=HT-0, Di 04.08.=HT-1, Mo 03.08.=HT-2, Fr 31.07.=HT-3 → **heute Do 30.07. ist HT-4, noch INAKTIV**)
- Watchlist-Kandidaten JNJ/MRK/ABBV: keine im 3-HT-Fenster (K5-Recheck bei Market Open bestätigt)

**Post-FOMC Marktreaktion Update:**
- SPY Pre +0,65 % Recovery nach Mi -1,515 % hawkish-Sell-off (leichte technische Konsolidierung)
- VIX 15,8 -6 % → Vola-Rückgang, Cash-Puffer 58,12 % weiter defensiv gerechtfertigt
- Perplexity zitiert Futures-Indikation "-0,3 %" widersprüchlich zu Alpaca IEX +0,65 % — Alpaca IEX authoritative (latest trade 12:33 UTC = 08:33 ET)
- 10Y Yield 4,12 % (leicht runter vs Mi ~4,20+ % Post-Fed) → Rate-Cut-Erwartungen minimal wiederhergestellt

**Makro-Ereignisse heute:**
- **08:30 ET Q2 GDP Advance Estimate** (primärer Vol-Katalysator Pre-Market, wird beim Market Open verarbeitet sein)
- **08:30 ET Core PCE Q2** (Inflations-Signal Post-Fed)
- **10:00 ET Pending Home Sales**
- **AAPL AMC ~5:00 PM ET**

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

**Watchlist Market Open — K1-K3 EOD-Bar Mi 29.07. bestätigt, K4/K5 zwingend Multi-Source Market Open:**
- **JNJ (XLV Healthcare)**: c=265,67 EMA50 247,96>EMA200 225,01 K1 ✓ / RSI 63,6 K2 ✓ / RS +14,14 pp K3 ✓ — K4-Vol + K5 FwdPE/RevGr Multi-Source
- **MRK (XLV Healthcare)**: c=130,40 K1 ✓ / RSI 59,3 K2 ✓ / RS +16,05 pp K3 ✓ — K4/K5 zwingend
- **ABBV (XLV Healthcare)**: c=263,62 K1 ✓ / RSI 67,8 K2 ✓ **nah 70-Cap** / RS +30,94 pp **#1 Top-Rank** K3 ✓ — K4/K5 zwingend, evtl. RS-Prio
- **XLV-Sektor-Cap-Warnung:** Aktuell 20,20 % XLV (UNH+LLY), 3. XLV-Position pusht auf ~30 % → **Max 1 der 3 kaufbar**, bevorzugt ABBV (RS #1) oder JNJ/MRK bei besserer K5-Fundamentaldiversifikation

**Entscheidung Pre-Market Do 30.07.:**
- **Kaufsignal-Scan JA bei Market Open 09:30 ET** — JNJ/MRK/ABBV K4/K5-Vollprüfung (max 1 kaufbar wg. Sektor-Cap)
- **KEINE Sell-Order** (5 V1-V6 SICHER Pre-Read, LLY -0,49 % P/L noch weit von V1-Stop, kein V5/V6-Trigger)
- **AAPL HT-0 Watch** — V1_neu 301,02 sicher aktiv Puffer +11,33 %, Post-Earnings-Reaktion Fr 31.07.
- **LLY Blackout Aktivierung Fr 31.07. HT-3** (Memory-Präzisierung: heute HT-4, noch inaktiv, V1_neu 1.134,20 = +4,74 % dann)
- **ClickUp Routine-Log Prio 4** wird gesendet
- **PushNotification Silence** (empty run: kein Trade, alle safe, Post-FOMC-Recovery-Signal grün → Silence-Rule)

**Nächste Routine:** Do 30.07. 09:30 ET Market Open + Kaufsignal-Scan JNJ/MRK/ABBV K4/K5-Multi-Source, dann 13:00 ET Midday Stop-Check + AAPL AMC-Countdown, 16:00 ET Market Close + Post-AAPL-Earnings-Watch Fr 31.07.

---

## Market Close 16:00 ET — 2026-07-29 (Mi, KW31 Tag 3, Fed-Day EOD) — Post-FOMC hawkish SPY -1,515 %, Portfolio Alpha +1,204 pp POSITIV, 5 V1-V6 SICHER, Watchlist morgen: JNJ / MRK / ABBV (3 XLV K1-K3 ✓)

**Alpaca Clock:** is_open=false Post-Close 16:00 ET, next_open Do 30.07. 09:30 ET.

**Alpaca /v2/account Market Close 16:00 ET:**
- portfolio_value: **97.970,67 $** (Daily **-0,311 %** vs last_equity 98.276,07, -305,40 $) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (57,88 %, unverändert)
- MV Close: 41.263,18 $ (5 Positionen, -312,37 $ vs Open 41.575,55)
- Buying_power: 342.366,85 $
- ATH 100.066,47 | DD **-2,094 %** [GRÜN]
- Weekly KW31 Tag 3 **+0,455 %** (vs Fr Close 97.526,60, +444,07 $) [GRÜN, weit von Cap -5 %]
- Open Orders: **KEINE**

**Marktdaten Close (Alpaca IEX + Perplexity):**
- **SPY Close 729,57** (Alpaca IEX Daily Bar) vs Di Close 740,795 = **-1,515 %** Post-FOMC hawkish-Sell-off [Crash-Filter INAKTIV]
  - Perplexity Cross-Check widersprüchlich: Sonar zitiert "744,78 +0,78 %" aus veralteten Investing.com/etf.com-Snapshots (verschiedene Datumsangaben), Alpaca IEX-Bar-Close 729,57 authoritative (Bar timestamp 2026-07-29T04:00:00Z = Tages-EOD)
- **VXX Close 23,44** (VIX-Proxy ~17-18, leichter Vola-Anstieg vs Midday 22,63 durch Post-Fed-Reaktion) [GRÜN <25]

**V1-V6-Vollcheck Market Close (aus heute EOD-Bars):**

| Sym  | Cur      | Qty | Entry     | P/L %    | chg_today | V1-Puffer    | V5 (EMA50/200) | V6 (RSI/RS-4w) |
|------|----------|-----|-----------|----------|-----------|--------------|----------------|-----------------|
| LLY  | 1.212,47 | 8   | 1.193,89  | +1,56 %  | -0,671 %  | **+9,41 % ENGSTE** | 1.137,11>1.016,80 ✓ | RSI 58,9 / RS +3,25 pp ✓ |
| V    |  368,73  | 27  |  357,178  | +3,23 %  | **+0,584 % Best chg** Post-Earnings-Bid | +10,89 % | 342,87>334,50 ✓ engster Spread +2,50 % | RSI 66,8 / RS +10,03 pp ✓ **Close bei 52w-Hoch 369,12** |
| AAPL |  337,99  | 31  |  316,857  | **+6,67 %** Best P/L | -0,615 %  | +10,94 % vs Blackout | 308,93>279,15 ✓ | RSI 67,2 / RS +19,23 pp ✓ **HT-0 morgen Q3 FY26** |
| JPM  |  347,39  | 3   |  332,78   | +4,39 %  | **-2,776 % Worst chg** XLF Post-FOMC | +11,87 % | 330,57>314,96 ✓ | RSI 55,3 / RS +7,72 pp ✓ |
| UNH  |  420,57  | 24  |  401,57   | +4,73 %  | -1,917 % XLV-Sell-off | +12,16 % | 406,18>354,79 ✓ | RSI 50,8 / RS +3,55 pp ✓ |

**5 SICHER — kein V1-V6-Trigger, keine Sell-Order für morgen.**

**Post-FOMC Marktreaktion (Alpaca-Kursbewegung inferred):**
- SPY -1,515 % — hawkish-Interpretation der Fed-Entscheidung (Konsens erwartete HOLD, aber Powell-Pressekonferenz-Sprache offenbar restriktiver als erhofft)
- Sektor-Verlierer: XLF (Banks) getroffen — JPM chg -2,776 % Worst chg; XLV moderat -1,5 %-Bereich — UNH chg -1,917 %, LLY chg -0,671 %; XLK gemischt AAPL chg -0,615 %
- Sektor-Gewinner: V chg **+0,584 % Best chg** Post-Earnings-Bid Fortsetzung (Zahlungsverkehr defensiv)
- VXX +0,81 vs Midday (22,63 → 23,44) — Vol-Response moderat, kein VIX-Spike

**Watchlist Do 30.07. Pre-Market (K1-K3 EOD-Bar Pre-Check — K4/K5 zwingend Multi-Source Market Open):**

**Watchlist morgen: JNJ (XLV, RS +14,14pp), MRK (XLV, RS +16,05pp), ABBV (XLV, RS +30,94pp #1)**

| Ticker | Sektor | Close   | K1 (EMA50>200) | K2 (RSI 50-70) | K3 (RS_63d vs SPY) | K5-Prep (K4/K5 morgen prüfen) |
|--------|--------|---------|----------------|----------------|--------------------|-------------------------------|
| JNJ    | XLV    | 265,67  | 247,96>225,01 ✓ | RSI 63,6 ✓ | RS **+14,14 pp** ✓ | Pharma-Konzern Global, K5 FwdPE + RevGr TBD |
| MRK    | XLV    | 130,40  | 123,29>110,32 ✓ | RSI 59,3 ✓ | RS **+16,05 pp** ✓ | Pharma Onko-Focus (Keytruda), K5 FwdPE + RevGr TBD |
| ABBV   | XLV    | 263,62  | 240,31>227,86 ✓ | RSI 67,8 ✓ **nah 70-Cap Watch** | RS **+30,94 pp #1 Top-Rank** ✓ | Pharma (Humira/Skyrizi/Rinvoq), K5 FwdPE + RevGr TBD |

**Alternative Sektor-Kandidaten (K1-K3-FAIL EOD, kein Kandidat):**
- MSFT (XLK) c=391,00 K1 FAIL (EMA50 394,32 < EMA200 435,49) + K3 FAIL (-11,46 pp) → SKIP
- NVDA (XLK) c=190,10 K2 FAIL (RSI 38,1) + K3 FAIL (-13,33 pp) → SKIP
- AVGO (XLK) c=370,33 K2 FAIL (RSI 43,5) + K3 FAIL (-9,89 pp) → SKIP
- GOOGL (XLK) c=336,49 K2 FAIL (RSI 43,5) + K3 FAIL (-6,31 pp) → SKIP
- META (XLK) c=587,39 K1 FAIL + K2 FAIL + K3 FAIL → SKIP
- CRM (Software) K1 FAIL → SKIP; LMT (Defense) K1 FAIL → SKIP; NOW (Software) K1 FAIL → SKIP; INTU K1 FAIL → SKIP
- KLAC (Semi) K2+K3 FAIL → SKIP; ANET (Netzwerk) K2+K3 FAIL → SKIP; GE (Industrials) K2 FAIL (RSI 49,4) → SKIP
- WMT/COST (Konsum) K3 FAIL → SKIP; PG K1+K2+K3 FAIL → SKIP; ORCL K1+K2+K3 FAIL → SKIP

**XLV-Sektor-Cap-Warnung Watchlist:**
- Aktuell XLV 20,20 % (UNH 10,30 % + LLY 9,90 %)
- 3. XLV-Position pusht Sektor-Cap auf ~30 % (Grenze max 30 %)
- **Max 1 der 3 Kandidaten kaufbar** — bevorzugt ABBV (RS-Prio #1) oder Alternative bei Sektor-Diversifikationswunsch nächste Woche
- Bei 3. XLV: Sektor-Cap-Verletzungs-Watch aktiv, kein 4. XLV mehr möglich

**Earnings-Kalender Do 30.07. (Wall Street Horizon carry-over):**
- **AAPL Q3 FY26 Do 30.07. AMC ~5:00 PM ET** (HT-0 morgen, Post-Earnings-Reaktion Fr 31.07. Watch)
- AMZN Q2 CY26 Do 30.07. AMC (nicht im Portfolio, aber SPY-Vol-Impact)
- INTC Q2 CY26 Do 30.07. AMC (nicht im Portfolio)
- **Do 30.07. 08:30 ET GDP Q2 Advance Estimate + Core PCE Q2** (Makro Vol-Risiko Pre-Market)

**Fed-Meeting Ergebnis (inferred aus SPY -1,515 % Reaktion):**
- Konsens erwartete HOLD unverändert
- SPY-Reaktion suggeriert hawkish-Interpretation Powell-Sprache
- Zinssenkungs-Timing-Signale wohl weiter nach hinten geschoben
- Cash-Position 57,88 % erweist sich als defensiv gerecht

**Entscheidung Market Close Mi 29.07.:**
- **KEIN Stop ausgelöst** (5 V1-V6 SICHER)
- **KEINE Sell-/Limit-Order** für morgen
- **KEIN Kauf** (Slot 1/2 bleibt OFFEN)
- **KEIN ClickUp Critical-Alert** (keine Stops, keine Cap-Verletzung, Weekly +0,455 % GRÜN)
- **ClickUp Prio 3 Tagesbericht** (Daily neg im Rahmen, kein DAILY_CAP)
- **PushNotification Silence** (empty run: negativer Tag im Rahmen mit POSITIVEM Alpha, kein Trade, kein Stop → Silence-Rule)
- **Slot 1/2 KW31 bleibt OFFEN** — Do 30.07. Pre-Market K4/K5-Vollprüfung Watchlist (max 1 XLV kaufbar wg. Sektor-Cap)

**Nächste Routine:** Do 30.07. 08:30 ET Pre-Market — Post-FOMC-Konsolidierung, GDP+PCE 08:30 ET (Makro-Watch), AAPL HT-0 Q3 AMC-Countdown, JNJ/MRK/ABBV K4/K5-Multi-Source-Verifikation (Perplexity + Alpaca-Vol), LLY Blackout ab Do 30.07. HT-3 aktivierbar V1_neu 1.134,20 (nur Info), V Post-Earnings-Bid-Fortsetzung Watch (Close bei 52w-Hoch).

---

## Pre-Market 08:36 ET — 2026-07-29 (Mi, KW31 Tag 3) — 🟡 V Post-Earnings Give-back ~-2,0 % (Puffer +5,86 % ENGSTE Blackout, SICHER aber verschlechtert vs Di Close +8,38 %). AAPL Blackout HT-1 (Do 30.07. AMC). Fed-Meeting HEUTE 14:00 ET FOMC + 14:30 ET Powell → LEVEL 0 restriktiv default. 5 V1-V6 SICHER, Slot 1/2 offen — Kaufsignal-Scan bei Market Open erlaubt aber vor 14:00 ET zwingend, VIX <25 volle Pos-Size möglich.

**Alpaca Clock:** is_open=false, 08:36 ET, next_open Mi 29.07. 09:30 ET.

**Alpaca /v2/account Pre-Market 08:36 ET:**
- portfolio_value: **98.019,76 $** (Daily **-0,261 %** vs last_equity 98.276,07, -256,31 $) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (57,85 %, unverändert vs Di Close)
- MV live: 41.312,27 $ (5 Positionen, -227,64 $ vs Di Close 41.539,91)
- Buying_power: 342.504,32 $ (Paper-Margin)
- **Reconciliation-Delta:** last_equity Alpaca 98.276,07 vs Memory Close 98.247,40 = +28,67 $ marginal (Alpaca Overnight-Reconciliation, unter Rundungs-Toleranz)
- ATH 100.066,47 | DD **-2,045 %** [GRÜN, Alarm bei -15 %]
- Weekly KW31 Tag 3 **+0,506 %** (vs Fr Close 97.526,60, +493,16 $) [GRÜN, Cap -5 %]
- Trading_blocked: false | Open Orders: **KEINE**

**Marktdaten Pre-Market (Alpaca IEX + Perplexity):**
- **SPY Pre 740,63** (Alpaca IEX Trade 08:36 ET) vs Di Close 740,795 = **-0,022 %** effektiv flat [Crash-Filter INAKTIV]
- **VIX ~16-17** (Perplexity Sonar-Pro Realtime-Indikation 16,3, VXX Alpaca IEX 22,08-22,29 Pre stabil vs Di 22 carry-over) [GRÜN <25 volle Pos-Size erlaubt]
- **10Y Treasury Yield ~4,0 %** (Perplexity grob, marginale Bewegung vs Vortag ~4,24 %)
- **VXX Pre 22,08-22,29** | **UVXY Di Close 24,64** (Vol-Contango neutral)

**V1-V6-Vollcheck Pre-Market 5 SICHER (Alpaca Cur Prices 08:36 ET):**

| Sym  | Cur      | Qty | Entry     | P/L %    | chg_today | V1-Standard | V1-Blackout  | V1-Puffer      | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|-------------|--------------|----------------|-----------------|
| V    |  359,21  | 27  |  357,178  | +0,57 %  | **-2,013 %** | 328,60 | **339,32 🟡** | **+5,86 %** ENGSTE **Post-Earnings-Give-back** verschlechtert vs Di Close +8,38 % um -2,52 pp | Blackout Post-Earnings-Reaktion Watch (V berichtete gestern Di AMC ~17:00 ET) |
| LLY  | 1220,21  | 8   | 1193,89   | +2,21 %  | -0,037 %  | 1.098,38    | —            | +11,09 %       marginal verschlechtert vs Di Close +11,31 % | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07.) |
| AAPL |  339,10  | 31  |  316,857  | +7,02 %  | -0,288 %  | 291,51      | **301,02 🟡** | **+12,65 %**   marginal verschlechtert vs Di Close +13,03 % | **🔴 AKTIV HT-1 Q3 FY26 Do 30.07. AMC** |
| UNH  |  427,80  | 24  |  401,57   | +6,53 %  | -0,231 %  | 369,44      | —            | +15,79 %       verbessert vs Di Close +15,16 % (Cur 427,80 vs Di Close 425,44 = +0,55 %) | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  357,54  | 3   |  332,78   | +7,44 %  | +0,064 %  | 306,16      | —            | +16,78 %       marginal verbessert vs Di Close +16,72 % Best P/L | inaktiv (Q3 ~Mitte Okt) |

**V1-Puffer Übersicht (eng→weit, mit Blackout-V1_neu wo aktiv):** V **+5,86 % ENGSTE** Post-Earnings-Give-back Blackout | LLY +11,09 % | AAPL +12,65 % Blackout **HT-1** | UNH +15,79 % | JPM +16,78 %

**Alle 5 V1-Puffer SICHER, kein Sofort-Stop-Risiko.** V-Post-Earnings-Give-back ~-2,3 % (Cur 359,21 vs Di Close 367,748) verringert Blackout-Puffer auf +5,86 % ENGSTE — noch komfortabel, aber Post-Earnings-Fortsetzungs-Watch Market Open zwingend. AAPL Blackout schaltet HT-1 aktiv (Regel: 3 HT vor Earnings, HT-2 gestern Di, HT-1 heute Mi, Earnings Do AMC).

**Earnings-Blackout-Check (Perplexity Multi-Source-Verifikation Fenster Mi 29.07. — Fr 31.07.):**
- **V (Visa)** Q3 CY26 **Di 28.07.2026 AMC ~17:00 ET RELEASED** (Perplexity: Investing/eToro/Visa-IR bestätigen) → Blackout technisch beendet, aber **Post-Earnings-Reaktion Watch** (Kurs -2,013 % Pre-Market)
- **AAPL** Q3 FY26 **Do 30.07.2026 AMC ~5:00 PM ET** (Perplexity heute keine harte Confirmation, aber 7+ Quellen von gestern bestätigt Memory: Apple IR, 9to5Mac, MacDailyNews, Wall Street Horizon, MarketBeat, MarketChameleon, Investing.com) → **HT-1 AKTIV HEUTE**, V1_neu 301,02, Puffer +12,65 % sicher
- **LLY** Q2 CY26 **Mi 05.08.2026 BMO** BESTÄTIGT (Memory carry-over Perplexity Di) → Heute noch inaktiv, Blackout aktivierbar ab Do 30.07. (HT-3), V1_neu 1.134,20 dann
- **UNH** Q3 CY26 ~Mitte Oktober 2026 (Historik) → kein Blackout im Fenster
- **JPM** Q3 CY26 ~Mitte Oktober 2026 (Historik) → kein Blackout im Fenster

**Makro-Kalender heute Mi 29.07. (FED-DAY):**
- **14:00 ET FOMC-Statement + Zinsentscheid** (Konsens: HOLD unverändert)
- **14:30 ET Powell-Pressekonferenz** (Fokus: Timing erster Zinssenkung + Inflation-Ausblick)
- Erwartete Vol-Peak 14:00-15:30 ET, VIX-Spike-Risiko
- Fed-Reaktion: dovish → Aktien hoch/Renditen runter/USD schwach; hawkish → Aktien runter/Renditen hoch/USD stark

**Watchlist Kandidaten Slot 1/2 KW31 (K1-K3 zwingend Market Open, K4/K5 vollständig dort):**
- **EOG** (Energy, carry-over aus Mo/Di, K1-K3 ✓ pre-verifiziert, K4 EOD Rebound-Bestätigung fehlt, K5 vorbekannt sauber FwdPE 9,98 + RevGr +15,63 %)
- **PANW** (Software, Perplexity Momentum, K1-K3 + Earnings-Check zwingend)
- **GH** (Health Care Non-Pharma, +66,30 % 3M)
- **ILMN** (Health Care Non-Pharma, +50,52 % 3M)
- **ICLR** (Health Care Non-Pharma, +58,97 % 3M)
- Perplexity heute keine harten Earnings-Termine für Watchlist-Kandidaten → K5-Earnings-Check bei Market Open Multi-Source zwingend
- **XLV-Sektor-Cap Grenzwertig:** UNH+LLY = 10,4+9,96 = 20,3 %; GH/ILMN/ICLR wären 3. XLV-Position und würden Cap auf ~30 % pushen → K5-Prio-Filter greift, PANW/EOG Diversifikationsvorteil

**Entscheidung Market Open Mi 29.07. (Kaufsignal-Scan):**
- **LEVEL 0 restriktiv default vor Fed 14:00 ET** — Kauf ggf. NUR wenn K1-K5 alle stark UND V-Post-Earnings stabilisiert; bei Half-Signal SKIP wie EOG gestern
- **V-Post-Earnings-Reaktion Watch:** Break unter Blackout 339,32 (-5,54 % vom Cur 359,21) triggert V1-Blackout-Market-Sell sofort
- **AAPL Blackout V1_neu 301,02:** Puffer +12,65 % sicher, keine Order-Änderung, nur Info
- Slot 1/2 KW31 bleibt OFFEN — Kaufsignal-Scan Market Open 09:30 ET dann Re-Check Midday
- Bei Fed-Reaktion dovish + starkem K1-K5-Signal → möglich Kauf nach 15:30 ET; hawkish → SKIP KW31 komplett möglich

**Guardrails Pre-Market 8/8 GRÜN + 3 WARN:**
```
1. Daily Loss Cap (-3 %):     Daily -0,261 %                                              [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 3 +0,506 %                                         [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,045 %                                                    [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,045 %                                                    [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,022 %                                                [INAKTIV]
6. VIX-Filter (>30):          VIX ~16-17 (VXX 22,08-22,29)                                [GRÜN <25 volle Pos-Size]
7. Earnings-Blackout (3 HT):  V Post-Earnings Watch + AAPL HT-1 + LLY ab Do HT-3          [WARN x3]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                                  [GRÜN]

WARN: Fed-Meeting HEUTE 14:00 ET FOMC + 14:30 ET Powell → LEVEL 0 restriktiv Vol-Peak 14:00-15:30 ET
```

**Entscheidung Pre-Market Mi 29.07.:**
- **KEINE Sell-Order** (alle 5 V1-V6 SICHER, kein Break-Trigger)
- **KEINE Kauf-Order** Pre-Market (Regel: Kaufsignal-Scan erst Market Open)
- **V-Post-Earnings-Watch aktiv** — Kurs 359,21 vs Di Close 367,748 = -2,32 % (Puffer +5,86 % ENGSTE aber sicher)
- **AAPL Blackout HT-1 heute aktiv** — Info only, keine Order-Änderung nötig
- **Market-Open-Scan JA** (K1-K5 EOG/PANW/GH/ILMN/ICLR, aber LEVEL 0 restriktiv wegen Fed-Meeting)
- **ClickUp Routine-Log Prio 4** wird gesendet
- **PushNotification Prio 3 Owner** — V-Post-Earnings-Give-back (Puffer verringert auf ENGSTE +5,86 %) + AAPL Blackout HT-1 + Fed-Meeting-Warnung Owner-relevant

**Nächste Routine:** Mi 29.07. 09:30 ET Market Open + Kaufsignal-Scan — V-Post-Earnings-Fortsetzung Watch, EOG/PANW/GH/ILMN/ICLR K1-K5 vollständig, LEVEL 0 restriktiv vor Fed 14:00 ET.

---

## Market Close 16:00 ET — 2026-07-28 (Di, KW31 Tag 2) — Tagesbilanz +0,651 % [GRÜN], Alpha +0,388 pp POSITIV, V5/V6-Vollcheck alle 5 SICHER, KEINE Pending-Order, Watchlist morgen: EOG carry-over + PANW/GH/ILMN/ICLR.

**Alpaca /v2/account Market Close 16:00 ET:**
- equity: **98.247,40 $** (Daily +635,19 $ / **+0,651 %** vs last_equity 97.612,21) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (57,72 %, unverändert)
- MV: 41.539,91 $ (5 Positionen, -39,69 $ vs Midday 41.579,60)
- Weekly KW31 Tag 2: **+0,739 %** (vs Fr Close 97.526,60, +720,80 $) [GRÜN, Cap -5 %]
- DD vs ATH: **-1,818 %** [GRÜN, Alarm bei -15 %]
- Open Orders: KEINE

**SPY Close 740,795** (Alpaca IEX 1D-Bar vs Mo Close 738,85 = **+0,263 %**) [Crash-Filter INAKTIV]
**Alpha: +0,388 pp POSITIV** (Portfolio +0,651 % > SPY +0,263 %; LLY +2,09 % XLV-Rebound + UNH +1,87 % + V +1,44 % Post-Earnings-Bid + AAPL +0,99 % + JPM +0,32 % zieht Portfolio hoch trotz 57,72 % Cash-Puffer-Dämpfung)

*Perplexity SPY-Query: 744,78 -0,13 % zeigt Stale-Data-Issue (letzte Datenpunkte in Search-Results zeitlich abweichend), Alpaca IEX 740,795 als primäre Quelle verwendet.*

**Positions-Snapshot Close:**

| Sym  | Cur      | chg_today | P/L %   | V1-Puffer | V5 EMA50>200 | V6 RSI/RS4w |
|------|----------|-----------|---------|-----------|--------------|-------------|
| V    |  367,748 | +1,439 %  | +2,96 % | +8,38 % Blackout ENGSTE | 341,72>330,48 ✓ | 65,34 / +7,36 pp |
| LLY  | 1.222,608| +2,094 %  | +2,41 % | +11,31 %  | 1.133,84>1.017,57 ✓ | 61,78 / -0,58 pp (knapp neg) |
| AAPL |  340,234 | +0,986 %  | +7,38 % | +13,03 % Blackout | 307,70>277,53 ✓ | 69,19 / +20,71 pp |
| UNH  |  425,44  | +1,868 %  | +5,94 % | +15,16 %  | 404,92>343,39 ✓ | 56,32 / +2,19 pp |
| JPM  |  357,35  | +0,323 %  | +7,38 % | +16,72 %  | 329,20>309,71 ✓ | 71,00 / +8,99 pp |

Ø P/L +5,21 %, Best AAPL/JPM +7,38 %, Worst LLY +2,41 %.

**V5/V6-Vollcheck (Alpaca IEX 200d-Historie, Wilder-RSI):**
- V5 (EMA50<EMA200 Death Cross): alle 5 SICHER, engster Spread V +11,24 (V EMA50 341,72 > EMA200 330,48). **Kein Trigger.**
- V6 (RSI>80 UND RS4w<0): kein Trigger. Max RSI JPM 71,00 (<80). Einziger RS4w<0 = LLY -0,58 pp knapp, aber RSI 61,78 << 80. V6 verlangt BEIDES.
- **→ KEINE V5/V6-Sell-Limit-Order für Mi 29.07. platziert.**

**Weekly Loss Cap Check:**
- Weekly +0,739 % (Portfolio 98.247,40 vs Fr 97.526,60 = +720,80 $) [GRÜN, weit von -5 %-Cap]
- Keine Aktion, keine Order-Stornierung, kein WEEKLY_CAP-Alert.

**Watchlist Mi 29.07. — Kandidaten für Slot 1/2 KW31 (K4/K5 vollständig bei Market Open):**

| Symbol | Sektor | Grund | K1-K3 Status | Nächste Earnings |
|--------|--------|-------|--------------|------------------|
| EOG    | XLE Energy | Carry-over aus heute — K1-K3 ✓ pre-verifiziert (EMA50 136,54>EMA200 125,52 +8,78 %, RSI 54,53, RS_63d +2,54 pp). K4 EOD zu verifizieren, Fed-Uncertainty-Watch | ✓✓✓ | ~Anfang August (Q2 FY26, zu prüfen) |
| PANW   | XLK Software | Perplexity Momentum-Scanner Top-Rank, +125,60 % 3M | K1-K3 zu verifizieren Mi Open | zu verifizieren |
| GH     | XLV Health Care Non-Pharma | Perplexity #1 Momentum, +66,30 % 3M | K1-K3 zu verifizieren | zu verifizieren |
| ILMN   | XLV Health Care Non-Pharma | +50,52 % 3M composite momentum score | K1-K3 zu verifizieren | zu verifizieren |
| ICLR   | XLV Health Care Non-Pharma | +58,97 % 3M scanner rank | K1-K3 zu verifizieren | zu verifizieren |

**Constraint-Check Watchlist:**
- **XLV-Sektor-Cap 30 %** — aktuell UNH 10,4 % + LLY 9,96 % = 20,3 %. GH/ILMN/ICLR wären 3. XLV-Position + Cap-Check bei Fill nötig (Fill-Wert würde XLV auf ~30-31 % pushen — GRENZWERTIG, K5-Sektor-Prio muss dann filtern).
- **PANW** würde 1. XLK-Position (nach MU-Verkauf 07.07. leer) → XLK-Diversifikation ✓
- **EOG** wäre 1. XLE-Position → XLE-Diversifikation ✓ (aktuell keine Energy-Exposure)
- **Fed-Meeting Mi 29.07.**: FOMC-Statement 14:00 ET + Powell-Pressekonferenz 14:30 ET → **LEVEL 0 restriktiv default** vor Event-Volatilität. Kauf ggf. Do 30.07. nach Fed-Reaktion; Market Open Mi 29.07. voraussichtlich EXPLICIT NO-BUY analog GS Fill-Day+7-Präzedenz.

**V-Post-Earnings-Reaktion Watch Mi 29.07. Pre-Market 08:30 ET zwingend:**
- V berichtete heute AMC ~17:00 ET (Q3 CY26 letzter HT)
- Alpaca Close-Snapshot 16:00 ET (equity 98.247,40) enthält Post-Earnings-Bewegung NICHT
- Pre-Market-Kurs Mi 29.07. zeigt Post-Earnings-Reaktion; Break unter Blackout 339,32 (-7,7 % vom Close 367,748) → V1-Blackout-Sell Market-Order sofort
- Bei starkem Post-Earnings-Rally (>+3 %) → RSI-Watch für V6 (aktuell 65,34), aber V6 verlangt RS<0 → wahrscheinlich weiter SICHER

**AAPL Blackout HT-1 aktiv ab Mi 29.07. Open** (Q3 FY26 Do 30.07. AMC):
- V1_neu 301,02 (statt Std 291,51), Close-Puffer +13,03 %
- Bei starkem Pre-Market-Drop (<-4 %) → Break-Watch aktivieren

**Entscheidung Market Close Di 28.07.:**
- **KEINE Sell-Order** — alle 5 V1-V6 SICHER
- **KEINE Kauf-Order** — Market Close-Routine nur für Tagesbilanz + Watchlist
- **Watchlist aktiviert** für Mi 29.07. Pre-Market 08:30 ET Erst-Screening
- **Fed-Meeting-Warnung** für Mi 29.07. dokumentiert
- **ClickUp Tagesbericht Prio 4** (positive Performance) — CLICKUP_LIST_ID Standard-Liste
- **PushNotification** — JA (Watchlist neu + V-Post-Earnings-Watch + Fed-Meeting-Reminder Owner-relevant für Mi Pre-Market)

**Nächste Routine:** Mi 29.07. 08:30 ET Pre-Market — V-Post-Earnings-Reaktion + AAPL Blackout HT-1 + EOG-Rebound-Watch + Watchlist K1-K3 Erst-Screening + Fed-Meeting-Vorbereitung.

---

## Market Open 09:38 ET — 2026-07-28 (Di, KW31 Tag 2) — KEIN Kauf: EOG SKIP LEVEL 0 (K4 formal offen bei 8 Min Session, chg +0,74 % Rebound zu schwach, Fed Mi 29.07. Unsicherheit). 5 V1-V6 SICHER, Alpha +0,503 pp POSITIV, Slot 1/2 OFFEN Re-Check Midday.

**Alpaca Clock:** is_open=true, 09:38 ET, next_close Di 28.07. 16:00 ET.

**Alpaca /v2/account Market Open 09:38 ET:**
- portfolio_value: **98.026,26 $** (Daily **+0,424 %** vs last_equity 97.612,21, +414,05 $) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (57,85 %, unverändert)
- MV Live: 41.318,77 $ (5 Positionen, -46,20 $ vs Pre 41.364,97)
- Buying_power: 342.522,52 $ (Paper-Margin)
- ATH 100.066,47 | DD **-2,039 %** [GRÜN, Alarm bei -15 %]
- Weekly KW31 Tag 2 **+0,512 %** (vs Fr Close 97.526,60, +499,66 $) [GRÜN, Cap -5 %]
- Trading_blocked: false | Open Orders: **KEINE**

**Marktdaten Market Open (Alpaca IEX):**
- **SPY Live 09:38 738,27** vs Mo Close 738,85 = **-0,079 %** effektiv flat [Crash-Filter INAKTIV]
- **Alpha vs SPY: +0,503 pp POSITIV** (Portfolio +0,424 % vs SPY -0,079 %; LLY +1,78 % XLV-Rebound Best chg + AAPL +0,86 % XLK-Bid + V +0,94 % + UNH +0,47 % > JPM -0,20 % Give-back — Cash-Puffer 57,85 % dämpft, aber Position-Beta liefert positives Alpha bei SPY-Flat)
- **VXX Live 22,38** (VIX-Proxy, vs Mo Close 22,225 = +0,7 % marginal Vol-Tick) [GRÜN <25 volle Pos-Size]

**V1-V6-Vollcheck Market Open 5 SICHER (Alpaca Cur Prices 09:38 ET):**

| Sym  | Cur      | Qty | Entry     | P/L %    | chg_today | V1-Standard | V1-Blackout  | V1-Puffer      | Blackout-Status |
|------|----------|-----|-----------|----------|-----------|-------------|--------------|----------------|-----------------|
| V    |  365,93  | 27  |  357,18   | +2,45 %  | +0,94 %   | 328,60      | **339,32 🟡** | **+7,84 %** ENGSTE verschlechtert vs Pre +9,04 % (Post-Open Give-back von Pre-Peak 370,00) | AKTIV letzter HT Q3 CY26 HEUTE AMC 5:00 PM ET |
| LLY  | 1.218,81 | 8   | 1.193,89  | +2,09 %  | +1,78 %   | 1.098,38    | —            | +10,96 %       verbessert vs Pre +10,41 % XLV-Rebound Best chg | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07.) |
| AAPL |  339,79  | 31  |  316,86   | +7,24 %  | +0,86 %   | 291,51      | **301,02 🟡** | **+12,88 %**   verbessert vs Pre +12,59 % XLK-Bid | **AKTIV Q3 FY26 Do 30.07. AMC HT-2 HEUTE** |
| UNH  |  419,60  | 24  |  401,57   | +4,49 %  | +0,47 %   | 369,44      | —            | +13,58 %       verschlechtert vs Pre +13,85 % XLV-Divergenz | inaktiv (Q3 ~Mitte Okt) |
| JPM  |  355,48  | 3   |  332,78   | +6,82 %  | -0,20 %   | 306,16      | —            | +16,11 %       verschlechtert vs Pre +17,11 % **Best P/L** XLF-Give-back Worst chg | inaktiv (Q3 ~Mitte Okt) |

**V1-Puffer Übersicht (eng→weit):** V +7,84 % Blackout **ENGSTE** | LLY +10,96 % | AAPL +12,88 % Blackout | UNH +13,58 % | JPM +16,11 %

**V3/V4-Check:** max P/L JPM +6,82 % / AAPL +7,24 % << 20 %-TP1, kein Trigger.
**V5-Check:** aus Mo Close-Bars Golden Cross alle intakt (V EMA-Diff +1,85 % engste aber intakt, keine EOD-Bar heute).
**V6-Check:** aus Mo Close max RSI JPM 69,94 << 80.
**→ KEINE Sell-/Limit-Order platziert.**

**Kaufsignal-Scan EOG Slot 1/2 KW31 — SKIP LEVEL 0 No-Action:**

| Kriterium | EOG Wert | Cap | Erfüllt |
|-----------|----------|-----|---------|
| K1 EMA50>EMA200 | 136,54 / 125,52 diff +8,78 % | > 0 | ✓ |
| K2 RSI(14) | 54,53 (aus Mo Close-Bars) | 50-70 | ✓ |
| K3 RS_63d vs SPY | +2,54 pp (EOG +6,12 % vs SPY +3,58 %) | > 0 | ✓ |
| K4 Volumen | Session 1.302 / avg20 128.200 = 1,02 % bei 8 Min Session-Zeit. Pro-rata Extrapolation 63.472 = ~49 % avg20 UNZUVERLÄSSIG zu früh | ≥ 120 % | **✗ formal offen** |
| K5 FwdPE / RevGr YoY | 9,98 / +15,63 % vorbekannt Mo Multi-Source | ≤ 35 / ≥ 10 % | ✓ |

- **EOG chg today +0,74 %** (Cur 141,36 vs Mo Close 140,32) → milder Rebound, aber Mo Momentum-Bruch -4,14 % NICHT überwunden. Kauf bei Half-Rebound = kein klares Momentum-Signal, Momentum-Quality-Thesis verletzt
- **Fed-Meeting Mi 29.07.** → zusätzliche 24h-Volatilität-Unsicherheit vor primärem Katalysator, LEVEL 0 restriktiv analog GS Fill-Day+7-Präzedenz (Kauf vor Event-Volatilität = zusätzliches Risiko)
- **Watchlist-Rest** GE/PSX/HON/DE/D K5-persistent-FAIL, F SKIP Blackout AMC heute, NEE/DUK K3-FAIL — kein Alternativ-Kandidat verfügbar

**→ EOG SKIP: Re-Check Midday 13:00 ET (K4 EOD-realistisch bewertbar + Intraday-Rebound-Konsolidierung), evtl. Nachmittag-Kauf-Fenster wenn Rebound klar bestätigt + K4 ≥ 120 % avg20. Slot 1/2 KW31 bleibt OFFEN.**

**Guardrails Market Open 8/8 GRÜN + 2 WARN:**
```
1. Daily Loss Cap (-3 %):     Daily +0,424 %                                             [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 2 +0,512 %                                        [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,039 %                                                   [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,039 %                                                   [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,079 %                                               [INAKTIV]
6. VIX-Filter (>30):          VXX 22,38 (Proxy VIX ~16-19)                               [GRÜN <25]
7. Earnings-Blackout (3 HT):  **V AKTIV letzter HT + AAPL AKTIV HT-2**                   [WARN x2]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                                 [GRÜN]
```

**Entscheidung Market Open Di 28.07.:**
- **KEIN Kauf** — EOG K4 formal offen + Rebound zu schwach → LEVEL 0 No-Action
- **KEINE Sell-/Limit-Order** — alle 5 V1-V6 SICHER
- **Slot 1/2 KW31 bleibt OFFEN** — Re-Check Midday 13:00 ET zwingend
- **AAPL Blackout V1_neu 301,02** Info-only, Puffer +12,88 % sicher aktivierbar
- **V-Blackout letzter HT** — Post-Earnings-Reaktion Mi 29.07. Pre-Market Watch zwingend
- **ClickUp Routine-Log Prio 4** wird gesendet
- **PushNotification Silence** (empty run: kein Trade, alle safe, EOG deferred, Silence-Rule respektiert)

**Nächste Routine:** Di 28.07. 13:00 ET Midday Stop-Check — EOG K4 EOD-realistisch bewertbar + Intraday-Rebound-Konsolidierung, V-Blackout Post-Earnings-Bid Watch (ENGSTE Puffer +7,84 %), AAPL Blackout V1_neu 301,02 Info-only, Fed-Meeting Mi 29.07. Vorbereitung.

---

## Pre-Market 08:36 ET — 2026-07-28 (Di, KW31 Tag 2) — 🔴 AAPL-Blackout NEU AKTIVIERT (Q3 FY26 Do 30.07. AMC bestätigt Multi-Source, HT-2 vor Earnings, Memory-Fehler von Fr 24.07. korrigiert), V-Blackout Q3 CY26 AMC HEUTE 5:00 PM ET letzter Tag. 5 V1-V6 SICHER Pre-Drift +0,472 %, Slot 1/2 KW31 offen — EOG Rebound-Watch Market Open zwingend.

**Alpaca Clock:** is_open=false, 08:36 ET, next_open Di 28.07. 09:30 ET.

**Alpaca /v2/account Pre-Market 08:36 ET:**
- portfolio_value: **98.072,46 $** (Pre-Drift **+0,472 %** vs last_equity 97.612,21, +460,25 $) [GRÜN, Cap -3 %]
- cash: 56.707,49 $ (57,82 %, unverändert vs Mo Close)
- MV live: 41.364,97 $ (5 Positionen, +469,58 $ vs Mo Close 40.895,39)
- Buying_power: 342.651,88 $ (Paper-Margin)
- **Reconciliation-Delta:** last_equity Alpaca 97.612,21 vs Memory Close 97.602,90 = +9,31 $ marginal (Alpaca Overnight/Corporate-Action-Reconciliation, unter Rundungs-Toleranz, kein Konflikt)
- ATH 100.066,47 | DD **-1,993 %** [GRÜN, Alarm bei -15 %]
- Weekly KW31 Tag 2 **+0,559 %** (vs Fr Close 97.526,60, +545,86 $) [GRÜN, Cap -5 %]
- Trading_blocked: false | Open Orders: **KEINE**

**Marktdaten Pre-Market (Alpaca IEX + Perplexity):**
- **SPY Pre 739,87** (Alpaca Trade 08:34 ET) vs Mo Close 738,85 = **+0,138 %** leicht positiv [Crash-Filter INAKTIV]
- **VIX ~16-19 Bandbreite** (Perplexity Sonar-Pro Realtime-Indikation 16,3, carry-over Mo Pre 19-21, VXX Mo Close 22,225 UVXY Pre 24,68 → Vol-Regime **GRÜN <25** → volle 10 %-Pos-Size erlaubt)
- **10Y Treasury Yield ~4,24 %** (Perplexity, minimale Bewegung vs Vortag)
- **VXX Mo Close 22,225** | **UVXY Pre 24,68** (Vol-Contango neutral)

**V1-V6-Vollcheck Pre-Market 5 SICHER (Alpaca Cur Prices 08:35 ET):**

| Sym  | Cur      | Qty | Entry     | P/L %    | V1-Standard | V1-Blackout  | V1-Puffer      | Blackout-Status |
|------|----------|-----|-----------|----------|-------------|--------------|----------------|-----------------|
| V    |  370,00  | 27  |  357,18   | +3,59 %  | 328,60      | **339,32 🟡** | **+9,04 %** ENGSTE verbessert vs Mo Close +6,86 % | AKTIV letzter HT Q3 CY26 HEUTE AMC 5:00 PM ET |
| LLY  | 1.212,73 | 8   | 1.193,89  | +1,58 %  | 1.098,38    | —            | +10,41 %       | inaktiv (Q2 Mi 05.08. BMO, Blackout ab Do 30.07.) |
| UNH  |  420,60  | 24  |  401,57   | +4,74 %  | 369,44      | —            | +13,85 %       | inaktiv (Q3 ~Mitte Okt) |
| AAPL |  338,92  | 31  |  316,86   | +6,96 %  | 291,51      | **301,02 🟡** | **+12,59 %**   | **NEU AKTIV Q3 FY26 Do 30.07. AMC, HT-2 HEUTE** |
| JPM  |  358,54  | 3   |  332,78   | +7,74 %  | 306,16      | —            | +17,11 %       | inaktiv (Q3 ~Mitte Okt) |

**V1-Puffer Übersicht (eng→weit, mit Blackout-V1_neu wo aktiv):** V +9,04 % Blackout **ENGSTE** | LLY +10,41 % | AAPL +12,59 % Blackout **NEU** | UNH +13,85 % | JPM +17,11 %

**Alle 5 V1-Puffer verbessert vs Mo Close** (Pre-Market-Drift +0,472 %). Kein Sofort-Stop-Risiko. V/AAPL Blackout-V1_neu funktional nicht wirksam bei aktueller Kurslage (Puffer +9,04 % / +12,59 % beide sicher).

**Earnings-Blackout-Check (Perplexity Multi-Source-Verifikation Fenster Di 28.07. — Fr 31.07.):**
- **V (Visa)** Q3 CY26 **Di 28.07.2026 AMC HEUTE ~5:00 PM ET** BESTÄTIGT (Perplexity Wall Street Horizon + MarketBeat) → **Blackout letzter Tag AKTIV**, V1_neu 339,32 Puffer +9,04 % sicher, Post-Earnings-Reaktion Mi 29.07. Pre-Market Watch zwingend
- **AAPL** Q3 FY26 **Do 30.07.2026 AMC 5:00 PM ET** MULTI-SOURCE BESTÄTIGT (Perplexity: Apple IR, 9to5Mac, MacDailyNews, Wall Street Horizon, MarketBeat, MarketChameleon, Investing.com — 7+ Quellen konvergent) → **NEUE AKTIVIERUNG HEUTE HT-2** (Regel: 3 HT vor Earnings, HT-3 war Mo 27.07. verpasst → **Memory-Fehler von Fr 24.07. korrigiert** ["nächste Q3 ~Ende Oktober" WAR FALSCH — Apple Fiscal Q3 = CY Apr-Jun 2026 → Report Ende Juli, nicht Oktober]), V1_neu = 316,86 × 0,95 = **301,02** (statt 291,51), Puffer +12,59 % sicher aktivierbar
- **LLY** Q2 CY26 **Mi 05.08.2026 BMO 10:00 AM ET Call** BESTÄTIGT (Lilly IR + Pressemitteilung + MarketBeat/MarketScreener) → **Blackout aktivierbar ab Do 30.07.** (Do=HT-3, Fr=HT-2, Mo 04.08.=HT-1, Di 05.08.=BMO). Heute noch inaktiv. Watchlist Do 30.07. Pre-Market V1_neu 1.193,89 × 0,95 = 1.134,20 (statt 1.098,38).
- **UNH** Q3 CY26 ~Mitte Oktober 2026 (Historik) → weit weg, kein Blackout
- **JPM** Q3 CY26 ~Mitte Oktober 2026 (Historik) → weit weg, kein Blackout

**Makro-Kalender heute Di 28.07.:**
- **14:30 ET Consumer Confidence** (Conference Board, sekundärer Katalysator)
- **22:40 ET API Rohöllagerbestände** (relevant für XLE-Sektor / EOG-Watch)
- Kein FOMC/PCE/CPI/NFP/PMI heute
- **Wichtig Wochenausblick:** **Mi 29.07. FOMC-Statement + Pressekonferenz** (Fed-Zinsentscheid, primärer Volatilitäts-Katalysator KW31), **Do 30.07. 14:30 ET GDP + PCE** (Kern-Inflation), **Do 30.07. AMC AAPL + AMZN Earnings** (Megacap-Cluster)
- Mi 29.07. AMC Earnings: **MSFT, META, SBUX** (Megacap-XLK/XLC Volatilität)

**Top News heute (Perplexity keine belastbare Realtime-Trend-Ableitung, sonst persistent Pre-FOMC risk-on-Konsens):** Fed-Meeting-Erwartungen dominieren (Konsens Zinsentscheidung Mi 29.07.), Post-Q2-Earnings-Momentum bei Megacap (V/BA/KO heute AMC), Öl-Sektor konsolidiert nach Mo EOG -4,14 %.

**Watchlist Slot 1/2 KW31 (aus Mo Close K1-K3-Screener, K4/K5 zwingend Market Open):**

| Sym | Mo Close | Entscheidung Di | Rationale |
|-----|----------|-----------------|-----------|
| **EOG** | 140,32 (-4,14 %) | **PRIMÄR — Rebound-Watch Market Open** | K1-K3 ✓, K5 vorbekannt ✓ (FwdPE 9,98 + RevGr +15,63 %). **Wenn Di Rebound + Volumen ≥120 % avg20 + K5-Multi-Source-Recheck sauber → Kauf Slot 1/2.** Wenn intraday Weakness Fortsetzung → LEVEL 0 SKIP (Falling Knife) |
| GE | 361,66 | REJECT persistent | K5-FAIL FwdPE Median 44,72 (>35), 4-Source-Konsens Mo bestätigt |
| PSX | 207,75 | REJECT persistent | K5-FAIL RevGr Q +6,9 % (<10 %) |
| F | 14,69 | SKIP Blackout | Q2 Di 28.07. AMC HEUTE bestätigt (Perplexity gruppiert mit V/BA/KO), Kauf-Timing Tag-0 unmöglich |
| HON | 245,76 | REJECT persistent | K5-FAIL RevGr +2,4 % (<10 %) |
| DE | 624,78 | REJECT persistent | K5-FAIL RevGr +9,6 % (<10 %) |
| D | 70,27 | REJECT persistent | K5-FAIL RevGr +7,49 % (<10 %) |
| NEE/DUK | — | DROP K3-FAIL | RS_63d vs SPY negativ |

**Guardrails Pre-Market 8/8 GRÜN + 2 WARN (V/AAPL Blackout aktiv):**
```
1. Daily Loss Cap (-3 %):     Pre-Drift +0,472 %                                     [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 2 +0,559 %                                    [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,993 %                                               [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,993 %                                               [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Mo -0,007 % / Pre +0,138 %                        [INAKTIV]
6. VIX-Filter (>30):          VIX ~16-19 Bandbreite                                  [GRÜN <25]
7. Earnings-Blackout (3 HT):  **V AKTIV letzter HT + AAPL NEU AKTIV HT-2**          [WARN x2]
8. Max Käufe KW31:            0/2 (Slot 1/2 + 2/2 offen)                             [GRÜN]
```

**Entscheidung Pre-Market Di 28.07.:**
- **AAPL Blackout ACTION**: V1-Watch verengen auf **301,02 $** (Puffer +12,59 % sicher, keine Alpaca-Order-Änderung nötig — Alpaca hat keine offenen Stop-Orders). Blackout aktiv bis Fr 31.07. (Post-AAPL-Earnings Do AMC + 1 HT Konsolidierung).
- **Market-Open-Scan JA** — EOG Rebound-Watch Primärkandidat für Slot 1/2 KW31 (K4-Volumen + K5-Multi-Source-Recheck 09:30 ET zwingend), alle anderen K1-K3-Kandidaten K5-persistent-FAIL oder Blackout.
- **Kauf-Wahrscheinlichkeit heute:** GERING (EOG braucht Rebound-Bestätigung, Fed-Meeting Mi 29.07. schafft zusätzliche Unsicherheit → LEVEL 0 restriktiv).
- **ClickUp Routine-Log Prio 4** wird gesendet.
- **PushNotification Prio 2 Owner** — AAPL-Blackout-Neuaktivierung ist echtes Signal (Memory-Fehler korrigiert), Owner-Sichtbarkeit gerechtfertigt.

**Nächste Routine:** Di 28.07. 09:30 ET Market Open + Kaufsignal-Scan — EOG K4-Volumen + K5-Recheck, V-Blackout letzter Tag Post-Earnings-Bid Watch, AAPL Blackout V1_neu 301,02 nur Info (kein Sofort-Stop-Risiko), Fed-Meeting Mi 29.07. Vorbereitung.

---

## Market Close 16:03 ET — 2026-07-27 (Mo, KW31 Tag 1) — Tagesbilanz + Watchlist Di: 5 V1-V6 SICHER, Daily +0,075 %, Alpha +0,082 pp POSITIV knapp, EOG Primärkandidat mit Rebound-Watch (chg -4,14 % Momentum-Bruch heute), alle klassischen RS-Leader (GE/PSX/HON/D/DE) K5-persistent-FAIL

**Alpaca Clock:** is_open=false, 16:03 ET, next_open Di 28.07. 09:30 ET.

**Alpaca /v2/account Close 16:03 ET:**
- portfolio_value: **97.602,90 $** (Daily **+0,075 %** vs last_equity 97.529,58, +73,32 $) [GRÜN, Cap -3 %]
- cash: 56.707,51 $ (58,10 %, unverändert vs Midday nach GS-Sell)
- MV Close: 40.895,39 $ (5 Positionen, -26,81 vs Midday 40.922,20)
- ATH 100.066,47 | DD **-2,462 %** [GRÜN, Alarm bei -15 %]
- Weekly KW31 Tag 1 **+0,078 %** (vs Fr Close 97.526,60) [GRÜN, Cap -5 %]

**Marktdaten Market Close Alpaca IEX:**
- **SPY Close 27.07. 738,85** vs Fr Close 738,90 = **-0,007 % effektiv flat** [Crash-Filter INAKTIV]
- **Alpha vs SPY: +0,082 pp POSITIV** (Portfolio +0,075 % vs SPY -0,007 %, defensiver Cash-Puffer 58,10 % nach GS-Sell + AAPL/JPM/V-Gain vs UNH/LLY-Give-back = leicht positives Alpha)
- **VIX carry-over 19-21** (kein Realtime-Update, letzter Stand Mo Pre-Market) [GRÜN <25]

**V1-V6-Vollcheck Market Close 5 SICHER (Alpaca IEX Bars bis 27.07.):**

| Sym  | Close    | Qty | V1        | V1-Puffer     | chg_today | EMA50/EMA200 diff | RSI(14) | RS_4w vs SPY | Status |
|------|----------|-----|-----------|---------------|-----------|--------------------|---------|--------------|--------|
| V    |  362,60  | 27  | **339,32** 🟡BLACKOUT | **+6,86 %** ENGSTE | +1,93 % | +1,85 % engste EMA-Diff intakt | 62,48   | +6,70 pp     | SICHER Blackout Tag+2/2 vor Q3 Di 28.07. AMC 5:00 PM ET, EMA-Diff engste aber intakt |
| LLY  | 1.197,88 | 8   | 1.098,38  | +9,06 %       | +0,15 %   | +12,38 %          | 57,44   | -2,06 pp     | SICHER stabil, RS_4w negativ aber RSI << 80 → V6 nicht ausgelöst |
| UNH  |  416,80  | 24  |   369,44  | +12,82 %      | -0,94 % Worst chg | +13,92 % | 49,41 | -3,61 pp | SICHER XLV-Give-back verschlechtert, RS_4w negativ aber RSI << 80 |
| AAPL |  337,15  | 31  |   291,51  | +15,66 %      | +1,24 %   | +10,30 %          | 67,61   | +18,47 pp    | SICHER XLK-Rebound |
| JPM  |  355,78  | 3   |   306,16  | +16,21 % Best P/L | +0,73 % | +4,95 %         | 69,94   | +7,45 pp     | SICHER **Best P/L** XLF-Rebound, RSI 69,94 näher 80-Watch aber weit unter |

**V1-Puffer Übersicht (eng→weit):** V +6,86 % Blackout **ENGSTE** | LLY +9,06 % | UNH +12,82 % | AAPL +15,66 % | JPM +16,21 %

**Watchlist Di 28.07. (K1-K3 aus Alpaca IEX Bars 27.07. Close, SPY 20d +1,30 % / SPY 63d +3,48 %):**

| Sym | Close   | chg     | EMA50/200 diff | RSI    | ret_63d | RS_63d | K1 | K2 | K3 | K5 vorbekannt | Decision Tue |
|-----|---------|---------|----------------|--------|---------|--------|----|----|----|--------------|--------------|
| GE  | 361,66  | +2,24 % | +8,15 %        | 58,17  | +27,04 % | **+23,55 pp #1** | ✓ | ✓ | ✓ | ✗ FwdPE Median 44,72 (>35) | REJECT persistent |
| PSX | 207,75  | +0,47 % | +15,82 %       | 68,09  | +27,59 % | **+24,10 pp #2** | ✓ | ✓ | ✓ | ✗ RevGr Q +6,9 % (<10 %) | REJECT persistent |
| F   |  14,69  | +2,30 % | +5,49 %        | 59,43  | +18,61 % | +15,13 pp | ✓ | ✓ | ✓ | K5 offen | SKIP Blackout Q2 Di 28.07. AMC |
| HON | 245,76  | +1,10 % | +3,37 %        | 67,03  | +15,30 % | +11,81 pp | ✓ | ✓ | ✓ | ✗ RevGr +2,4 % (<10 %) | REJECT persistent |
| **EOG** | 140,32 | **-4,14 %** | +8,75 %  | 53,54  | +5,38 % | +1,90 pp | ✓ | ✓ | ✓ | ✓ FwdPE 9,98 + RevGr +15,63 % | **WATCH Rebound Di Pre-Market** |
| DE  | 624,78  | -0,55 % | +8,52 %        | 60,83  | +11,05 % | +7,56 pp | ✓ | ✓ | ✓ | ✗ RevGr +9,6 % (<10 %) | REJECT persistent |
| D   |  70,27  | -1,15 % | +6,78 %        | 53,41  | +12,31 % | +8,82 pp | ✓ | ✓ | ✓ | ✗ RevGr +7,49 % | REJECT persistent |
| NEE |  88,81  | -1,07 % | +3,64 %        | 52,24  | -6,80 % | **-10,29 pp** | ✓ | ✓ | ✗ | offen | DROP K3-FAIL |
| DUK | 128,84  | -1,23 % | +1,35 %        | 56,32  | +1,23 % | **-2,26 pp** | ✓ | ✓ | ✗ | offen | DROP K3-FAIL |

**Watchlist morgen: EOG (Rebound-Watch nach -4,14 %, einzige mit K5 vorbekannt ✓), GE (RS #1 aber K5-FAIL persistent), PSX (RS #2 aber K5-FAIL persistent), F (SKIP Blackout Q2 AMC), HON (K5-FAIL persistent)**

**Rationale Watchlist Di 28.07.:**
- **EOG Primärkandidat** — einzige Aktie im gescreenten Universum mit sauberem K5 (FwdPE 9,98 + RevGr +15,63 % aus Fr-Screener), technische K1-K3 alle ✓ (EMA-Diff +8,75 %, RSI 53,54 im Cap 50-70, RS_63d +1,90 pp positiv), aber **heute Momentum-Bruch chg -4,14 %** (Öl-Reversal nach Iran-Bull-Thesis-Fehlschlag). **Kauf bei Weakness = Falling Knife → LEVEL 0 No-Action bis Rebound bestätigt**. Di 28.07. Pre-Market: Wenn EOG Rebound + Volumen ≥120 % avg20 → K4-Vollcheck + Kauf-Fenster, sonst Verzicht.
- **GE / PSX RS-Leader (#1 und #2)** — K5-Multi-Source-FAIL persistent (GE FwdPE Median 44,72 aus 4 Sources; PSX RevGr Q +6,9 % <10 %-Cap), strikte Regel-Anwendung ohne Override rechtfertigbar (MMM/KO-Präzedenz).
- **F** — SKIP Blackout Q2 Di 28.07. AMC bestätigt (Kauf heute = Tag-0 = sofortige Aktivierung Blackout unmöglich).
- **HON/D/DE** — K5 RevGr <10 % persistent (mehrfach reviewed, kein Override).
- **NEE/DUK** — K3 RS negativ, kein Momentum-Signal.
- **Zusatz-Sektor-Perplexity-Check nicht belastbar** (Perplexity Sonar liefert keine sauberen K5-Multi-Source-Daten für S&P500-Momentum-Kandidaten). Alpaca IEX-Bars-basierter deterministischer Screen ist Kern-Datengrundlage für morgen.

**Entscheidung Market Close Mo 27.07.:**
- **KEINE Sell-/Limit-Order für Di 28.07. platziert** (5 V1-V6 alle SICHER, kein V5/V6-Trigger)
- **Slot 1/2 KW31 bleibt OFFEN** — EOG Primär-Fokus mit Rebound-Watch Di Pre-Market
- **Weekly Loss Cap** GRÜN weit von -5 %-Cap (+0,078 %)
- **ClickUp Tagesbericht Prio 4** (positive Perf) wird gesendet
- **PushNotification Silence** (empty run: kein Trade, alle safe, kein Alert nötig — Routine-Silence-Regel)

**Nächste Routine:** Di 28.07. 08:30 ET Pre-Market KW31 Tag 2.

---

## Market Open 09:30 ET — 2026-07-27 (Mo, KW31 Tag 1) — KEIN Kauf: EOG intraday-Weakness -1,71 % + K4 formal offen + XLE-Sektor -0,90 %, GE K5-Multi-Source-Median 44,72 REJECT, XLU/XLI-Screener alle intraday flat/negativ. 6 V1-V6 SICHER, Slot 1/2 OFFEN.

**Alpaca Clock:** is_open=true, 09:39 ET (Handel läuft), next_close Mo 27.07. 16:00 ET.

**Alpaca /v2/account Market Open 09:38 ET:**
- portfolio_value: **97.903,67 $** (Daily **+0,384 %** vs last_equity 97.529,58) [GRÜN, Cap -3 %]
- cash: 48.385,51 $ (49,42 %, unverändert vs Fr Close)
- MV live: 49.518,16 $ (6 Positionen, +377,07 $ vs Fr Close 49.141,09)
- ATH 100.066,47 | DD **-2,161 %** [GRÜN, Alarm bei -15 %]
- Weekly KW31 Tag 1 **+0,387 %** (vs Fr Close 97.526,60, frischer Start) [GRÜN, Cap -5 %]

**Marktdaten Market Open Alpaca IEX:**
- **SPY Live 09:39 745,05** vs Fr Close 738,90 = **+0,832 %** [Crash-Filter INAKTIV]
- **Alpha vs SPY: -0,448 pp NEGATIV** (Portfolio +0,384 % < SPY +0,832 %, Cash-Puffer 49,42 % dämpft Rebound-Beta gegenüber Breit-Markt-Anstieg — erwartetes Alpha-Muster bei defensiver Cash-Quote)
- **VIX Mo Pre 19-21** carry-over (kein Realtime-Update) [GRÜN <25 volle 10 %-Pos-Size erlaubt]

**V1-V6-Vollcheck Market Open 6 SICHER (Alpaca IEX Bars bis 27.07.):**

| Sym  | Cur Live | Qty | V1        | V1-Puffer     | chg_today | EMA50/EMA200 diff | RSI(14) | Status |
|------|----------|-----|-----------|---------------|-----------|--------------------|---------|--------|
| **GS**   | 1.084,34 | 8   | 1.050,40  | **+3,23 %** ENGSTE | **+2,18 %** Best | +14,11 % | 54,20 | SICHER Rebound-Tag+1 Fill-Day+7 überstanden |
| V    |   360,61 | 27  | **339,32** 🟡BLACKOUT | +6,27 % | +1,37 % | +2,82 % engste EMA-Diff aber intakt | 61,07 | SICHER Blackout Tag+1/2 vor Q3 Di 28.07. AMC 5:00 PM ET |
| LLY  | 1.197,54 | 8   | 1.098,38  | +9,03 %       | +0,13 %   | +11,59 % | 57,22 | SICHER XLV-Konsolidierung |
| UNH  |   419,00 | 24  |   369,44  | +13,41 %      | -0,41 % Worst chg | +11,48 % | 50,49 | SICHER XLV-Konsolidierung Divergenz vs LLY |
| AAPL |   335,44 | 31  |   291,51  | +15,07 %      | +0,73 %   | +10,91 % | 66,80 | SICHER XLK stabil |
| JPM  |   357,75 | 3   |   306,16  | **+16,85 %** weit | +1,29 % | +7,16 % | **71,68** Watch | SICHER XLF-Rebound Fortsetzung, RSI näher am 80-Threshold aber weit unter |

**V3/V4-Check:** max P/L JPM +7,51 % << 20 %-TP1, kein Trigger. **V5-Check:** V EMA-Diff +2,82 % engste aber intakt + verbessert vs Fr-Close +1,76 %. **V6-Check:** max RSI JPM 71,68 << 80-Threshold. **→ KEINE Sell-/Limit-Order platziert.**

**Kaufsignal-Scan Slot 1/2 KW31 — LEVEL 0 No-Action bei Unsicherheit:**

**EOG (Hauptkandidat XLE) — REJECT LEVEL 0 Intraday-Weakness:**
- K1 EMA50 136,25 > EMA200 126,75 diff +7,49 % ✓
- K2 RSI 61,72 (50 ≤ 61,72 ≤ 70) ✓
- K3 RS_63d +4,25 pp ✓ (EOG +8,86 % vs SPY +4,61 %)
- **K4 formal offen** (Session-Vol 3.735 / avg20 132.445 = 2,8 % bei 09:38 = 9/390 Min Session-Zeit; pro-rata Extrapolation 3.735×43,33 ~161.850 = ~122 % avg20 grenzwertig unzuverlässig zu früh in Session)
- K5 Prä-Screen ✓ FwdPE 9,98 + RevGr +15,63 % (multi-source verifiziert Fr Close-Screen)
- **Intraday-Weakness dominierend**: chg -1,71 % (Cur 143,88 vs Fr Close 146,385), Gap-Down Open 143,34 = -2,08 % vs Fr Close, Session-Range 143,04-144,31
- **XLE-Sektor heute -0,90 %** (Cur 59,08 vs Fr Close 59,61) → **kontra Pre-Market Iran/Oil-Bull-Narrative**, keine Sektor-Rückenwind aktuell
- **→ Momentum-Quality-Thesis intraday verletzt** (Kauf bei Gap-Down = "Falling Knife"-Muster nicht regelkonform mit Momentum-Strategie); LEVEL 0 "No-Action bei Unsicherheit" + Re-Check Midday 13:00 ET (Intraday-Reversal-Potenzial) oder Di Pre-Market (K4 EOD-Volumen-Verifikation Mo)

**GE (Industrials, Watchlist Backup) — REJECT K5-Multi-Source-Median FAIL:**
- Perplexity Multi-Source FwdPE Recheck: **Yahoo 34,72** (knapp unter 35-Cap) / **Zacks 45,19** / **StockAnalysis 47,61** / **GuruFocus 44,72** → **Median 44,72**, 3 von 4 Sources > 35-Cap → strikte Regel-Anwendung REJECT analog **MMM-Präzedenz** (Q2 22.07. K5-FAIL RevGr +2,4 %); LEVEL 0 "No-Action bei Unsicherheit" bei nur 1 Multi-Source-Ausreißer unter Cap kein Override rechtfertigbar
- RevGr Q2 2026 +24,6 % ✓ solide
- chg today **+3,16 %** stark (Best chg Watchlist) — momentum-mäßig attraktiv aber K5 dominiert Signal-Hierarchie
- RS_63d +21,0 pp #1 wäre Top-Score aber K5 blockiert

**HON (Industrials) — REJECT K5-FAIL:** RevGr +2,40 % persistent << 10 %-Cap (Q2 22.07. bestätigt); chg today +1,33 % (nicht relevant)

**F (Consumer Discretionary) — SKIP Blackout:** Q2 2026 Earnings Di 28.07. AMC 4:05 PM ET bestätigt (Ford BusinessWire IR / MarketBeat / Nasdaq) → Blackout Aktivierung Tag+1 nach Kauf zwingend → **LEVEL 0 "No-Action bei Unsicherheit"** (analog FTI-Präzedenz Fr 24.07. Rejection, Kauf direkt vor Earnings nicht rechtfertigbar); chg today +2,40 % (nicht relevant)

**D (Utilities) — REJECT K5-FAIL:** RevGr +7,49 % persistent knapp <10 %-Cap (Fr Screener bestätigt); chg today -0,19 % XLU-flat (kein Momentum)

**XLU-Zusatz-Screener frische Runde (NEE/DUK/SO/AEP/EXC):**
- NEE +0,01 %, DUK -0,60 %, SO -0,13 %, AEP -0,30 %, EXC -0,29 %
- **Alle flat/negativ intraday** → kein Momentum-Signal, K1-K3-Vollcheck nicht sinnvoll ohne Momentum-Basis (Zeit-/Token-Kosten unverhältnismäßig)
- **→ XLU-Universe kein aktueller Kauf-Kandidat KW31**

**XLI-Zusatz-Screener frische Runde (UNP/CAT/DE):**
- UNP -1,23 %, CAT -0,57 %, DE -0,19 %
- **Alle negativ intraday trotz XLI-Rebound +0,94 %** (XLI-Rebound dominiert von GE +3,16 % [K5-FAIL] und HON +1,33 % [K5-FAIL])
- **→ XLI-Universe kein aktueller Kauf-Kandidat KW31**

**Sektor-Snapshot heute 09:38 (Alpaca IEX):**

| Sektor-ETF | Cur | chg vs Fr Close | Bemerkung |
|------------|-----|-----------------|-----------|
| XLE | 59,08 | **-0,90 %** | Kontra Pre-Market Iran/Oil-Bull-Narrative |
| XLU | 46,18 | -0,19 % | Flat, defensiv-Rotation vom Fr pausiert |
| XLI | 184,34 | **+0,94 %** | Leading, dominiert von GE/HON (beide K5-FAIL) |

**Entscheidung Kauf: KEIN Kauf Slot 1/2 KW31.**
- Kein Kandidat erfüllt alle 5 K-Signale mit sauberer Intraday-Momentum-Bestätigung
- EOG einziger K1-K3+K5-✓-Kandidat wg Intraday-Weakness auf Midday/Di-Pre-Market verschoben
- LEVEL 0 "No-Action bei Unsicherheit" respektiert (nicht bei Weakness kaufen, K4 nicht robust messbar)
- Slot 1/2 bleibt offen (bis Fr 31.07. Ende der KW31)

**Guardrail-Status 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     +0,384 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 1 +0,387 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,161 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,161 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,832 %                                        [INAKTIV]
6. VIX-Filter (>30):          Mo Pre 19-21                                        [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV V1_neu 339,32 (Puffer +6,27 % sicher)       [WARN]
8. Max Käufe KW31:            0/2 (Slot 1/2 offen, Slot 2/2 offen)                [GRÜN]
```

**ClickUp Routine-Log Prio 4** wird nach Fertigstellung gesendet.

**PushNotification Silence** (Silence-Rule respektiert — kein Trade, alle safe, EOG deferred; kein Owner-Actionable).

**Nächster Check:** Mo 27.07. 13:00 ET Midday Stop-Check — GS V1 1.050,40 Puffer +3,23 % ENGSTE Rebound-Fortsetzung Watch, V-Blackout letzter HT vor Q3 (Di 28.07. AMC) nur Info, **EOG Intraday-Reversal-Watch für Slot 1/2 potenzielles Nachmittag-Kauf-Fenster** (K4 gegen EOD besser bewertbar), JPM RSI 71,68 Watch (näher am 80-Threshold).

---

## Pre-Market 08:30 ET — 2026-07-27 (Mo, KW31 Tag 1) — Alle 8 Guardrails GRÜN + 1 WARN (V-Blackout Tag+1/2 vor Q3 Di 28.07. AMC), SPY Pre +0,81 %, VIX leicht hoch 19-21 aber <25, EOG-Hauptkandidat + XLU/XLI-Screener Market Open

**Alpaca Clock:** is_open=false, next_open Mo 27.07. 09:30 ET.

**Alpaca /v2/account Pre-Market 08:37 ET:**
- portfolio_value: **97.886,97 $** (vs last_equity 97.529,58 = **+357,39 $ / +0,366 % Pre-Drift**) [GRÜN, Cap -3 %]
- cash: 48.385,51 $ (49,43 %, unverändert vs Fr Close)
- MV live: 49.501,46 $ (6 Positionen, +360,37 $ vs Fr Close 49.141,09)
- buying_power: 332.146,14 $ (Paper-Margin)
- status: ACTIVE, trading_blocked=False, account_blocked=False
- ATH: 100.066,47 $ | DD **-2,178 %** [GRÜN — Alarm bei -15 %]
- **Konsistenz Alpaca vs portfolio.md:** ✓ (Fr Close 97.526,60 → Alpaca last_equity 97.529,58, Delta +2,98 $ Rundungsdrift, alle 6 Positionen mit exakter Qty/Entry deckungsgleich)

**Marktdaten Pre-Market Alpaca IEX:**
- **SPY Pre 744,90** (Alpaca last trade 08:31 ET) vs Fr Close 738,90 = **+0,812 %** [Crash-Filter INAKTIV]
- **QQQ Pre 693,78** (Alpaca last trade 08:10 ET)
- **VXX Pre 22,32** (Fr Close carry, kein Pre-Trade)
- **VIX Perplexity Multi-Source:** Fr Close ~18,70 (+12,4 % chg Fr) → Mo Pre **19-21 Range** (Investing.com Snapshot 19,31 [6] / MarketWatch 20,95 [4]) → **Anstieg vs Fr um +0,6 bis +2,3 pp aber weit <25** [GRÜN, volle 10 %-Pos-Size erlaubt]
- **US 10Y Treasury:** Perplexity liefert ~4,27 % (indikativ, kein sauberer Zeitstempel) [neutral, kein Katalysator]
- **Alpha vs SPY Pre-Drift:** +0,366 % Depot vs SPY +0,812 % = **-0,446 pp NEGATIV Pre-Drift** (Cash-Puffer 49,43 % dämpft Rebound-Beta gegenüber Breit-Markt-Anstieg)

**Makro-Ereignisse heute (Mo 27.07.):**
- Perplexity findet KEINE spezifischen Fed/CPI/PCE/NFP-Releases für 27.07.2026 (Kalender-Datenlücke). Typisches Mo-Muster: Dallas Fed Manufacturing möglich, Fed-Speaker sekundär. **Kein primärer Katalysator identifiziert.**
- **Top-Themen seit Fr Close:** (1) Oil-Preise >$100 (Brent), Middle East Tensions → **Energy-Rotation weiter aktiv** ✓ EOG-Priorität; (2) AI-Spending-Sorgen trotz Q2-Earnings-Beats (Semiconductor-Selloff-Fortsetzung); (3) Rate-Erwartungen leicht neu justiert.

**V1-V6-Vollcheck Pre-Market 6 SICHER (sortiert eng→weit):**

| Sym  | Pre 08:37 | Qty | V1        | V1-Puffer     | chg vs Fr Close | Status |
|------|-----------|-----|-----------|---------------|-----------------|--------|
| **GS**   | 1.079,05  | 8   | 1.050,40  | **+2,73 %**   | **+1,68 %** ENGSTE VERBESSERT | SICHER Fill-Day+7 Rebound, +1,70 pp vs Close +1,03 % |
| V    |   359,99  | 27  | **339,32** 🟡BLACKOUT | +6,09 %     | +1,19 %        | SICHER V-Blackout Tag+1/2 vor Q3 Di 28.07. AMC 5:00 PM ET [1][2] |
| LLY  | 1.199,89  | 8   | 1.098,38  | +9,24 %       | +0,32 %        | SICHER XLV-Rebound Tag+3 |
| UNH  |   421,80  | 24  |   369,44  | +14,17 %      | +0,34 %        | SICHER XLV-Rebound |
| AAPL |   334,29  | 31  |   291,51  | +14,68 %      | +0,33 %        | SICHER XLK stabil |
| JPM  |   356,33  | 3   |   306,16  | **+16,39 %**  | +0,88 %        | SICHER (weiteste), XLF-Rebound Fortsetzung |

**V5/V6 aus Fr-Close-Basis alle 6 SICHER carry-over** (EMA50>EMA200 überall Golden Cross intakt, max RSI JPM 68,01 << 80).

**Earnings-Blackout 3 HT (Perplexity Multi-Source Fenster Mo/Di/Mi):**
- **V Q3 FY26 Di 28.07. AMC BESTÄTIGT 5:00 PM ET** [Visa IR release 07.07.2026, MarketBeat, Investing.com, MarketScreener] → **V-Blackout AKTIV Tag+1/2 vor Earnings**, V1_neu 339,32 unverändert, Puffer +6,09 % sicher — kein Aktion nötig, keine Sell-Order
- **UNH/JPM/GS/LLY/AAPL:** kein Q3 CY26 Datum in Perplexity-Sources confirmed (nur estimated Mitte-Oktober), **kein Blackout in nächsten 3 HT**
- **Watchlist F (Ford) Q2 2026 Di 28.07. AMC BESTÄTIGT 4:05 PM ET** [Ford BusinessWire IR, MarketBeat, Nasdaq] → **F NICHT KAUFBAR KW31 (SKIP)** wie in portfolio.md notiert
- GE/HON/D/EOG: KEIN Earnings-Release im Fenster 27.-31.07.2026 (GE Q2 bereits 16.07. released) → **KAUFBAR ohne Blackout**

**Watchlist KW31 Slot 1/2 + 2/2 (aus Fr-Close-Screener K1-K3 ✓, K4/K5 zwingend Market Open):**
1. **EOG** (Energy XLE #1 KW30, K1-K3 3/3 ✓, RSI 67,1 Cap-nah, RS_63d +5,1 pp, K5-Prä-Screen ✓ FwdPE 9,98 + RevGr +15,63 %) — **HAUPTKANDIDAT KW31** (Oil-Rally-Rückenwind ✓)
2. **GE** (Industrials, K1-K3 3/3, RS_63d +21,0 pp #1) — K5-Recheck Mo Market Open (Fr-Screener FwdPE 47,61 K5-FAIL → prüfen ob Multi-Source-Override)
3. **HON** (Industrials, K1-K3 3/3, RSI 65,2, RS_63d +9,1 pp) — K5 Fr-Screener FAIL RevGr +2,4 %, DROP
4. **D** (Utilities, K1-K3 3/3, RSI 59,0, RS_63d +9,4 pp) — K5 Fr-Screener FAIL RevGr +7,49 %, DROP
5. **F** (Consumer Disc, K1-K3 3/3) — **Blackout Di 28.07. AMC → SKIP KW31**
- **Zusatz-Screener zwingend Mo Market Open:** frische XLU-Kandidaten (NEE/DUK/SO/AEP/EXC) + XLI (UNP/CAT/DE Re-Check)

**Guardrail-Status 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     Pre-Drift +0,366 %                                    [GRÜN]
2. Weekly Loss Cap (-5 %):    KW31 Tag 1 startet frisch (+0,462 % vs Fr Close)      [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,178 % vs ATH 100.066,47                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,178 %                                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Pre +0,812 %                                      [INAKTIV]
6. VIX-Filter (>30):          Mo Pre 19-21 (Anstieg vs Fr 18,7, aber <25)           [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV V1_neu 339,32 (Puffer +6,09 % sicher)         [WARN]
8. Max Käufe KW31:            0/2 (Reset heute)                                     [GRÜN]
```

**Entscheidung Market-Open-Scan:** **JA** — KW31 Slot 1/2 EOG-Priorität (Energy-Rotation-Rückenwind ✓ + K1-K5 alle ✓ Prä-Screen), Slot 2/2 XLU/XLI-Screener frische Runde Mo Market Open zwingend. GE K5-Recheck (FwdPE-Multi-Source), HON/D K5-FAIL bereits konfirmiert DROP, F Blackout SKIP.

**ClickUp Routine-Log Prio 4** wird nach Fertigstellung dieser Routine gesendet.

**PushNotification Prio 4 Owner** — Routine-Zusammenfassung.

**Nächster Check:** Mo 27.07. 09:30 ET Market Open + Kaufsignal-Scan — **EOG K4/K5-Vollcheck + Limit-Order (Slot 1/2)**, GS V1 1.050,40 Puffer +2,73 % Rebound-Fortsetzung Watch, V-Blackout letzter Tag vor Q3 (Di 28.07. AMC) nur Info, XLU/XLI-Frisch-Screener für Slot 2/2.

---

## Market Close 16:00 ET — 2026-07-24 (Fr, KW30 Tag 5 letzter HT) — Tagesbilanz + Watchlist Mo 27.07.: GE HON F D EOG (K1-K3 ✓)

**Alpaca Clock Close:** is_open=false, next_open Mo 27.07. 09:30 ET.

**Alpaca /v2/account Close 16:00 ET:**
- equity_end: **97.526,60 $** (vs last_equity 97.150,03 = **+376,57 $ / +0,388 % Daily**) [GRÜN]
- cash: 48.385,51 $ (49,61 %, unverändert)
- long_market_value: 49.141,09 $ (6 Positionen)

**Marktdaten Close 24.07.:**
- **SPY Close 738,90** (Alpaca IEX, n=21.063 Trades) vs Do-Close 738,06 = **+0,114 %** (Perplexity meldete abweichende Werte 744,78 — Alpaca IEX authoritative für Alpha-Berechnung) [Crash-Filter INAKTIV]
- **VIX/VXX** ~18 / ~22 (carry-over) [GRÜN, <25]
- **Alpha vs SPY:** Daily +0,388 % vs SPY +0,114 % = **+0,274 pp POSITIV** (AAPL XLK-Rebound-Beitrag dominant)

**V1-V6-Vollcheck Close 6 SICHER (Alpaca IEX 260d Bars):**

| Sym  | Close    | Qty | V1        | V1-Puffer   | RSI14  | EMA50/EMA200 Diff | Status |
|------|----------|-----|-----------|-------------|--------|-------------------|--------|
| GS   | 1.061,23 | 8   | 1.050,40  | **+1,03 % ENGSTE** | 49,76 | +13,39 % | SICHER Fill-Day+7 Give-back Close, 10,83 $ vom V1 |
| V    |   355,74 | 27  | **339,32** 🟡BLACKOUT | +4,84 % | 57,66 | +1,76 % | SICHER V-Blackout Tag+1/3 Q3 Di 28.07. AMC |
| LLY  | 1.196,04 | 8   | 1.098,38  | +8,89 %     | 57,21 | +13,38 % | SICHER XLV-Rebound Tag+2 |
| UNH  |   420,38 | 24  |   369,44  | +13,79 %    | 51,42 | +14,02 % | SICHER XLV-Divergenz vs LLY |
| AAPL |   333,20 | 31  |   291,51  | +14,30 %    | 65,55 | +11,24 % | SICHER **Best chg +3,59 % XLK-Rebound** |
| JPM  |   353,21 | 3   |   306,16  | +15,37 %    | 68,01 | +5,39 %  | SICHER XLF-Rebound Close |

**V5 (EMA50<EMA200) 6 SICHER** — kein Death Cross, keine Sell-Order für Mo platziert.
**V6 (RSI>80 & RS<0) 6 SICHER** — max RSI JPM 68,01 << 80.

**Weekly KW30 Final:** -0,722 % (vs Fr-Close 18.07. 98.236,14) [GRÜN, Cap -5 %]. Käufe KW30 Final: 1/2 (V 20.07.).

**Watchlist Mo 27.07. — K1-K3 ✓ Screening (Alpaca IEX 260d, 40 Kandidaten Non-Tech/Non-Healthcare):**

| Sym  | Sektor           | Close    | EMA50    | EMA200   | RSI14 | RS_63d pp | Notes |
|------|------------------|----------|----------|----------|-------|-----------|-------|
| **GE** | Industrials     | 353,74   | 341,07   | 311,31   | 53,0  | **+21,0**  | **#1 RS**, sauber Momentum, KL4/K5 Prüfung Mo Open |
| HON  | Industrials      | 243,09   | 226,44   | 221,40   | 65,2  | +9,1      | RSI Cap-nah, K4-Vol/K5-Fundamentals Prüfung |
| F    | Consumer Disc    |  14,36   |  13,98   |  13,09   | 54,6  | +10,8     | Auto-Sektor, K5-RevGrowth kritisch (F Marge historisch niedrig) |
| D    | Utilities        |  71,09   |  68,29   |  63,75   | 59,0  | +9,4      | Utilities-Diversifikation gut vs Portfolio, K5-Div-freundlich |
| EOG  | Energy           | 146,38   | 136,79   | 127,93   | 67,1  | +5,1      | Energy-Diversifikation, RSI Cap-nah, K5-Oil-preis-abhängig |

**Rejects K1-K3 aus 40er-Screen:**
- MU/AMAT/LRCX/CVX/XOM RSI außer Cap 50-70 oder Tech-Ausschluss
- NCLH/COR/BSX K1-FAIL (EMA50<EMA200)
- WFC/BAC K1-K3 ✓ aber Financials-Sektorlimit (2 im Portfolio JPM+GS, +V=3 → max erreicht)

**Sektor-Diversifikation Watchlist:** Bewusst Non-Tech/Non-Healthcare/Non-Financials — Portfolio bereits XLV 20,15 % (LLY+UNH), XLF 19,73 % (GS+JPM+V), XLK 10,59 % (AAPL). Neue Käufe Mo idealerweise Industrials (GE/HON), Utilities (D), Energy (EOG), Consumer Disc (F) für Diversifikations-Boost.

**Guardrail-Status 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     +0,388 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Final -0,722 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,538 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,538 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,114 %                                        [INAKTIV]
6. VIX-Filter (>30):          ~18                                                 [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV V1_neu 339,32 (kein Sofort-Stop-Risiko)     [WARN]
8. Max Käufe KW30:            1/2 Final                                           [GRÜN]
```

**Entscheidung Close 16:00 Fr 24.07.:**
- **KEINE Sell-/Limit-Order für Mo 27.07. platziert** (6 V1-V6 SICHER)
- **KEIN Stop ausgelöst**
- **ClickUp Task erstellt**: [CLOSE] Tagesbilanz 869e97vn8 Prio 4 (Low, positive Perf)
- **PushNotification Prio 4 Owner**: Routine-Spec Close-Notification

**Tages-Highlights:**
- Best chg: AAPL +3,59 % (XLK-Rebound, dominiert Alpha +0,27 pp)
- Worst chg: GS -1,26 % (Fill-Day+7 Give-back Close, Puffer +1,03 % ENGSTE)
- Best P/L: JPM +6,14 %
- Worst P/L: GS -7,05 %
- V-Blackout Tag+1/3 aktiv, Rebound Close +1,18 %

**Watchlist morgen (Mo 27.07.):** GE (Industrials, RS +21 pp #1), HON (Industrials, RS +9,1 pp), F (Consumer Disc, RS +10,8 pp), D (Utilities, RS +9,4 pp), EOG (Energy, RS +5,1 pp)

**Nächste Routine:** Mo 27.07. 08:30 ET Pre-Market Check KW31 Tag 1 — GS V1-Puffer +1,03 % ENGSTE Wochenend-Watch zwingend, V-Blackout letzter Tag vor Q3 (Di 28.07. AMC), Watchlist K4/K5 Prüfung 09:30 Market Open.

---

## Market Open 09:38 ET — 2026-07-24 (Fr, KW30 Tag 5 letzter Handelstag) — KEIN Kauf: PSX K5-FAIL RevGrowth +6,9 %, FTI Timing-Blockiert, DE K5-FAIL +9,6 %

**Alpaca Clock:** is_open=true, timestamp 2026-07-24 09:38:07 ET, next_close Fr 24.07. 16:00 ET.

**Alpaca /v2/account (Live 09:38 ET):**
- portfolio_value: **97.282,89 $** (vs Do-Close 97.152,97 = **+129,92 $ / +0,137 % Daily**) [GRÜN]
- cash: **48.385,51 $** (49,74 %, unverändert)
- long_market_value: 48.897,38 $ (6 Positionen)
- buying_power: 330.451,47 $ (Paper-Margin-Artefakt)

**Marktdaten Live 09:38 ET:**
- **SPY Live 739,46** vs Do-Close 738,06 = **+0,189 %** (leichter Rebound, Pre-Prognose bestätigt +0,35 % → -0,16 pp fadding) [Crash-Filter INAKTIV]
- **VIX/VXX** ~18 / 22,2 (carry-over Pre) [GRÜN, <25 volle Pos-Size]
- **Alpha vs SPY:** Daily +0,137 % vs SPY +0,189 % = **-0,056 pp NEUTRAL** (Cash-Puffer 49,74 % dämpft Rebound)

**V1-V6 Vollcheck 6 SICHER (Live 09:38 ET):**
| Sym  | Cur Live | Qty | V1        | V1-Puffer   | Δ$ zum V1 | Status |
|------|----------|-----|-----------|-------------|-----------|--------|
| GS   | 1.069,68 | 8   | 1.050,40  | **+1,84 %** | 19,28 $   | SICHER **ENGSTE**, Fill-Day+7 Give-back-Fortsetzung verschlechtert vs Pre +3,39 % um -1,55 pp |
| V    |   352,26 | 27  | **339,32** 🟡BLACKOUT | +3,81 % | 12,94 $   | SICHER, Blackout Standard 328,60 → 339,32 aktiviert Q3 Di 28.07. AMC, kein Sofort-Stop-Risiko |
| LLY  | 1.192,00 | 8   | 1.098,38  | +8,52 %     | 93,62 $   | SICHER |
| AAPL |   325,46 | 31  |   291,51  | +11,64 %    | 33,95 $   | SICHER |
| JPM  |   348,51 | 3   |   306,16  | +13,83 %    | 42,35 $   | SICHER |
| UNH  |   423,25 | 24  |   369,44  | +14,56 %    | 53,81 $   | SICHER |

**V5/V6 auf Vortag-Basis 6 SICHER** (EMA50>EMA200 alle Golden Cross intakt, max RSI 65,76 JPM << 80).

**Kaufsignal-Scan Slot 2/2 KW30 — LEVEL 0 No-Action bei Unsicherheit — alle 3 Kandidaten REJECT:**

**(1) PSX (Hauptkandidat) — REJECT K5-FAIL:**
- K1 EMA50>EMA200 ✓ (Vortag-Basis 185/163 diff +22)
- K2 RSI(14) 67,60 ✓ (im Cap 50-70)
- K3 RS_63d vs SPY +25,0 % #1 ✓
- K4 Vol so früh (09:38) nicht belastbar → offen
- **K5 FAIL**: Multi-Source Perplexity **FwdPE 10,8-11,9x** (Zacks 11,88 / Yahoo 10,9 / GuruFocus 10,78) ✓ ≤35, aber **RevGrowth YoY letztes berichtetes Quartal +6,9 %** (MarketBeat) → **klar <10 %-Cap**
- Blackout: kein Q2 CY26-Datum sauber belegbar (StockAnalysis nur veraltet-inkonsistent, nicht verifizierbar) → Blackout-Risiko offen, aber K5-Fail dominierend
- **Analog KO 21.07. (TTM +5,1 % K5-Konflikt) / MMM 22.07. (TTM +2,4 % K5-Fail) / UPS-Präzedenz (-2,65 % permanent-blocked)** → strikte Regel-Anwendung

**(2) FTI (Backup #1) — REJECT LEVEL 0 Timing:**
- K1-K3 ✓ (Vortag-Basis)
- K4 Vol offen (09:38)
- K5 ✓: **FwdPE 19,4x + RevGrowth Q1 CY26 +11,6 %** (Perplexity Multi-Source belastbar)
- **Blackout-Timing kritisch**: Earnings **30.07.2026 Do bestätigt** → **HT-4 heute** (Fr 24., Mo 27., Di 28., Mi 29., Do 30.)
  - Blackout-Regel: 3 HT vor Earnings → **Aktivierung Mo 27.07. am Tag+1 nach Kauf**
  - Vergleich V-Kauf 20.07.: hatte 6 HT Buffer bis Blackout, jetzt 4 HT nach Kauf aktiv → weit weniger kritisch
  - FTI hätte nur 1 HT Buffer → sofortige V1-Verengung -5 % + Fill-Day+1 Give-back-Muster (analog AVGO/MU/GS/LLY-Präzedenz) + Earnings-Volatilitäts-Risiko
- **LEVEL 0 "No-Action bei Unsicherheit"**: Timing zu knapp, Sofort-Blackout-Aktivierung erhöht Sofort-Stop-Risiko drastisch
- **Alternative Timing**: Post-Earnings-Fenster Fr 31.07. / Mo 03.08. (nach Earnings-Reaction) für sauberen Einstieg

**(3) DE (Backup #2) — REJECT K5-FAIL:**
- K1-K3 ✓ (Vortag-Basis)
- K4 Vol offen (09:38)
- **K5 FAIL**: FwdPE 23x ✓, aber **RevGrowth Q3 FY25 +9,6 %** → **knapp <10 %-Cap** (nur -0,4 pp Diff)
- Kein Multi-Source-Override rechtfertigbar bei so kleiner Diff (analog KO-Ambiguität → LEVEL 0)
- Blackout: Earnings 14.08.2026 → 15 HT weg, kein Blackout-Risiko (irrelevant wegen K5)

**Weitere Kandidaten aus Do-Close-Screener bereits Rejects:**
- CVX RSI 71,0 K2-FAIL (>70)
- UNP RSI 71,0 K2-FAIL
- EQNR RSI 76,4 K2-FAIL
- CAT RSI 43,9 K2-FAIL (<50)
- LMT EMA50 521 < EMA200 542 K1-FAIL
- TPR RS -8,6 % K3-FAIL
- NEE RS -4,0 % K3-FAIL

**Guardrail-Status 8/8 GRÜN + 1 WARN:**
```
1. Daily Loss Cap (-3 %):     +0,137 %                                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 5 -0,972 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,783 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,783 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,189 %                                        [INAKTIV]
6. VIX-Filter (>30):          ~18 / VXX 22,2                                      [GRÜN <25]
7. Earnings-Blackout (3 HT):  V AKTIV V1_neu 339,32 (kein Sofort-Stop-Risiko)     [WARN]
8. Max Käufe KW30:            1/2 (Slot 2/2 verfällt ohne K1-K5 ✓)                [GRÜN]
```

**Entscheidung Market Open 09:38 Fr 24.07.:**
- **KEIN Kauf** (LEVEL 0 No-Action: alle 3 Kandidaten K5-blockiert oder Timing-blockiert)
- **KEINE Sell-/Limit-Order** (6 V1-V6 SICHER, keine V5/V6-Trigger)
- **V-Blackout dokumentiert** (V1_neu 339,32 aktiviert, Puffer +3,81 % ohne Sofort-Stop-Risiko)
- **Slot 2/2 KW30 verfällt Ende Fr 24.07.** ohne 2. Kauf. KW30 Final: 1 Kauf (V 20.07.)
- **ClickUp Routine-Log Prio 4** + **PushNotification Prio 3 Owner**

**Nächste Routine:** Fr 24.07. 13:00 ET Midday Stop-Check — GS V1 1.050,40 Puffer +1,84 % ENGSTE zwingender Watch, V Blackout-Puffer +3,81 % Konsolidierung, LLY XLV-Fortsetzung.

---

## Pre-Market 08:36 ET — 2026-07-24 (Fr, KW30 Tag 5 letzter Handelstag) — Alle 6 V1 SICHER, V-Blackout-AKTIVIERUNG (Q3 Di 28.07. AMC), GS-Rebound Tag+2, Slot 2/2 offen, PSX-Hauptkandidat

**Alpaca Clock:** is_open=false, timestamp 2026-07-24 08:36:19 ET, next_open Fr 24.07. 09:30 ET, next_close Fr 24.07. 16:00 ET.

**Alpaca /v2/account (Pre-Market 08:36 ET):**
- portfolio_value: **97.330,71 $** (vs Do-Close 97.152,97 = **+177,74 $ / +0,183 % Pre-Drift**) [GRÜN]
- cash: **48.385,51 $** (49,71 %, unverändert)
- long_market_value: 48.945,20 $ (6 Positionen)
- buying_power: 330.588,60 $ (Paper-Margin-Artefakt, effektiv Cash-Budget)
- Konsistenz mit portfolio.md Close 23.07. bestätigt ✓

**Marktdaten Pre-Market 08:30-08:36 ET:**
- **SPY Pre 740,66 $** vs Do-Close 738,06 = **+0,352 %** (leichter Rebound nach Do -1,26 %) [Crash-Filter INAKTIV]
- **VXX Pre 22,21** vs Do-Close 22,61 = **-1,77 %** (Vol-Compression, VIX-Proxy → VIX ~17-18) [GRÜN <30]
- **VIX Perplexity: 18,24** (Realtime ET) [GRÜN, weit <25 → volle 10 %-Position-Size erlaubt]
- **10Y Treasury Yield:** keine belastbare Realtime-Quote (Perplexity)
- **Makro heute:** KEINE FOMC/CPI/PCE/NFP-Release, Perplexity nennt keine hochrangigen Katalysatoren; Earnings-Highlights Fr **AXP, VZ, NEE, SLB, CNI** (nicht im Portfolio, marktbewegend Financials/Utilities/Energy)
- **Top-News:** Perplexity liefert keine belastbaren Overnight-Top-News (nur allgemeine Vol-/KI-Kommentare)

**Pre-Market V1-Puffer alle 6 SICHER (sortiert eng→weit):**
| Sym  | Pre-Cur  | chg_pre% | V1        | V1-Puffer   | Δ$ zum V1 | Status |
|------|----------|----------|-----------|-------------|-----------|--------|
| GS   | 1.086,00 | +1,05 %  | 1.050,40  | **+3,39 %** | 35,60 $   | SICHER **ENGSTE**, Rebound-Tag+2 verbessert vs Do-Close +2,32 % um +1,07 pp |
| V    |   353,39 | +0,44 %  | 328,60→**339,32** | +7,54 % / +4,15 % neu | 24,79 / 14,07 $ | SICHER, **BLACKOUT-AKTIVIERUNG V1_neu 339,32 $** (Kaufkurs 357,178 × 0,95, Q3 Di 28.07. AMC bestätigt) |
| LLY  | 1.183,63 | -0,14 %  | 1.098,38  | +7,76 %     | 85,25 $   | SICHER, marginale Konsolidierung vs Do-Close +7,92 % |
| AAPL |   322,53 | +0,27 %  |   291,51  | +10,64 %    | 31,02 $   | SICHER, marginale Verbesserung vs Do-Close +10,34 % |
| JPM  |   351,12 | +0,35 %  |   306,16  | +14,69 %    | 44,96 $   | SICHER, marginale Verbesserung vs Do-Close +14,29 % |
| UNH  |   424,79 | +0,28 %  |   369,44  | +14,98 %    | 55,35 $   | SICHER, marginale Verbesserung vs Do-Close +14,65 % |

**Earnings-Blackout 3 HT (Fr 24., Mo 27., Di 28.07.) — Perplexity Multi-Source-Check:**
- **V (Visa): Q3 FY26 Di 28.07. AMC BESTÄTIGT** [1][2] → Fr 24.07. = HT-3 vor Earnings → **3-HT-Blackout AKTIV** → **Stop verengen auf -5 % (V1_neu 339,32 $)**, Owner-Info-Level (kein Sofort-Stop-Risiko, Kurs 353,39 > V1_neu +4,15 %)
- AAPL, JPM, UNH, LLY, GS — kein Blackout in Fenster (Perplexity NEIN, alle Q2 CY26 bereits gemeldet Mitte Juli, nächste Q3 ~Ende Oktober)
- Watchlist PSX, FTI, DE — kein Blackout in Fenster (Perplexity NEIN)

**Guardrail-Status 8/8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     Pre +0,183 % (vs Do-Close 97.152,97)                 [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 5 -0,922 % (vs Fr-Close 98.236,14)          [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,734 %                                             [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,734 %                                             [GRÜN]
5. Crash-Filter (SPY -5 %):   Do -1,26 % / Pre +0,35 %                             [GRÜN INAKTIV]
6. VIX-Filter (>30):          VIX 18,24 / VXX 22,21                                [GRÜN <25 volle Pos-Size]
7. Earnings-Blackout (3 HT):  V AKTIV (Q3 Di 28.07. AMC) → V1_neu 339,32 $         [WARN → Aktion]
8. Max. Käufe (2/Woche):      KW30 1/2 (Slot 2/2 offen letzter HT)                 [GRÜN]
```

**Kaufsignal-Watchlist Fr 24.07. Market Open — Slot 2/2 KW30 letzter Handelstag (aus Do-Close Screener K1-K3):**
| Sym | Sektor | Ref-Kurs | RSI14 | RS_63d | ret_20d | K1 | K2 | K3 | K4/K5 | Bemerkung |
|-----|--------|----------|-------|--------|---------|----|----|----|-------|-----------|
| **PSX** | XLE | 206,92 | 67,60 | **+25,0 %** #1 | +22,6 % | ✓ | ✓ | ✓ | zwingend Market Open | **Hauptkandidat**, Refining/Marketing-Leader, XLE 0 % im Depot (Post-GOOGL), kein Blackout, unkritisch |
| FTI | XLE | 76,03 | 66,80 | +1,5 % | +18,3 % | ✓ | ✓ | ✓ | zwingend Market Open | Backup Energy Services, kein Blackout |
| DE  | XLI | 610,05 | 56,40 | +1,4 % | +1,4 % | ✓ | ✓ | ✓ | zwingend Market Open | Backup Industrials, kein Blackout |

**Entscheidung Pre-Market:**
- **Kaufscan bei Market Open 09:30 ET: JA** (letzter Handelstag KW30 Slot 2/2, alle Guardrails GRÜN, VIX <25 volle Pos-Size, 3 K1-K3-Kandidaten kein Blackout)
- **V-Blackout-Aktivierung: JA** (V1_neu 339,32 $ statt 328,60, ohne Sofort-Stop-Risiko da Kurs 353,39 > 339,32 = +4,15 % Puffer)
- **PSX Priorität 1** (RS #1 +25 %, XLE-Sektor 0 % Portfolio = maximaler Diversifikations-Nutzen, kein Sektor-Cap-Risiko)
- **KEINE offenen Sell-Orders**, keine Limit-Order für heute pre-Open platziert

---

## Market Close 16:03 ET — 2026-07-23 (Do, KW30 Tag 4) — Tagesbilanz: 6 V1-V6 SICHER, Alpha +0,31 pp POSITIV, keine Limit-Order Fr, PSX-Watchlist Slot 2/2 letzter Handelstag

**Alpaca Clock:** is_open=false, timestamp 2026-07-23 16:02:52 ET, next_close Fr 24.07. 16:00 ET.

**Alpaca /v2/account (Close 16:00 ET):**
- portfolio_value: **97.152,97 $** (vs Mi-Close 98.087,79 = **-934,82 $ / -0,953 % Daily**) [GRÜN]
- cash: **48.385,53 $** (49,80 %, unverändert seit Open Post-GOOGL-Sell)
- long_market_value: 48.767,44 $ (6 Positionen)
- buying_power: 48.385,53 $

**Marktdaten (Alpaca IEX Close):**
- **SPY Close 23.07.:** 738,06 $ vs Mi-Close 747,49 = **-1,262 %** [Crash-Filter INAKTIV]
- **VXX Close:** 22,61 (VIX-Proxy → VIX ~17-18 carry-over) [GRÜN, <30]
- **Alpha vs SPY:** Daily -0,953 % vs SPY -1,262 % = **+0,309 pp POSITIV** (Cash-Puffer 49,80 % dämpft SPY-Breitmarkt-Sell, Portfolio-Fokus-Positionen mildere Give-back)

**Vollcheck V1-V6 6 SICHER (Close):**
| Sym  | Cur     | V1-Puffer | EMA50   | EMA200  | V5 diff  | RSI14 | RS_4w vs SPY | V5    | V6    |
|------|--------|-----------|---------|---------|----------|-------|--------------|-------|-------|
| GS   | 1.074,72| **+2,32 %** | 1.042  | 933    | +109     | 51,86 | -0,91 %      | SICHER | SICHER (RSI<80) |
| V    |   351,85| +7,08 %   | 341    | 332    | +8,4     | 54,27 | +5,09 %      | SICHER | SICHER |
| LLY  | 1.185,31| +7,92 %   | 1.131  | 1.020  | +111     | 55,30 | +5,45 %      | SICHER | SICHER |
| AAPL |   321,66| +10,34 %  | 308    | 280    | +27      | 58,25 | +8,98 %      | SICHER | SICHER |
| JPM  |   349,90| +14,29 %  | 327    | 313    | +13      | 65,76 | +4,23 %      | SICHER | SICHER |
| UNH  |   423,59| +14,65 %  | 413    | 360    | +53      | 53,27 | +3,69 %      | SICHER | SICHER |

**→ Keine V5/V6-Trigger, KEINE Limit-Order für Fr 24.07. platziert**

**Kaufsignal-Watchlist Fr 24.07. — Slot 2/2 KW30 letzter Handelstag (Alpaca-Screener K1-K3):**
| Sym | Sektor | Cur    | RSI14  | RS_63d vs SPY | ret_20d | EMA50/200 diff | K1 | K2 | K3 | Bemerkung |
|-----|--------|--------|--------|---------------|---------|-----------------|----|----|----|-----------|
| **PSX** | XLE | 206,92 | 67,60 | **+25,0 %** #1 | +22,6 % | +21,9 | ✓ | ✓ | ✓ | **Hauptkandidat**, Refining/Marketing-Leadership |
| FTI | XLE | 76,03 | 66,80 | +1,5 %       | +18,3 % | +9,5 | ✓ | ✓ | ✓ | Backup Energy Services |
| DE  | XLI | 610,05 | 56,40 | +1,4 %       | +1,4 %  | +40 | ✓ | ✓ | ✓ | Backup Industrials |
| CVX | XLE | 194,42 | 71,00 | +0,6 %       | +13,3 % | +5,6 | ✓ | ✗ | ✓ | K2-FAIL (RSI>70) |
| UNP | XLI | 303,95 | 71,00 | +18,1 %      | +16,9 % | +21,7 | ✓ | ✗ | ✓ | K2-FAIL (RSI=70,04 knapp) |
| EQNR| XLE | 40,94 | 76,40 | +4,0 %       | +29,5 % | +3,6 | ✓ | ✗ | ✓ | K2-FAIL (RSI>>70) |
| CAT | XLI | 893,86 | 43,90 | +6,7 %       | -10,1 % | +164 | ✓ | ✗ | ✓ | K2-FAIL (RSI<55) |
| LMT | XLI | 567,78 | 68,10 | -1,6 %       | +15,5 % | -20,9 | ✗ | ✓ | ✗ | K1-Death-Cross + K3-negativ |
| TPR | XLY | 139,14 | 44,70 | -8,6 %       | -7,1 %  | +5   | ✓ | ✗ | ✗ | K2+K3-FAIL |
| NEE | XLU | 89,82 | 57,90 | -4,0 %       | +2,5 %  | +1,1 | ✓ | ✓ | ✗ | K3-FAIL |

**Sektor-ETF-Momentum (Close, Ref: Wahl neuer Sektoren):**
- **XLE +5,08 % 63d (RS +1,30 % vs SPY)** RSI 68,3 — Momentum-Leader Sektor
- **XLI +6,38 % 63d (RS +2,60 % vs SPY)** RSI 55,96 — Momentum-Sektor #1
- XLU +2,96 % 63d (RS -0,82 %) RSI 59,2 — schwächer
- XLP +1,38 % 63d (RS -2,40 %) — schwach
- XLB -2,93 % 63d — schwach
- XLY -8,61 % 63d — schwächster

**Sektor-Struktur Post-GOOGL-Sell (Close):**
- XLV 20,23 % Portfolio (UNH+LLY)
- XLF 19,71 % Portfolio (GS+JPM+V, 3-Pos-Cap intakt)
- XLK 10,26 % Portfolio (AAPL)
- XLE/XLI/XLU/XLP/XLB/XLY/XLC = 0 % (PSX/FTI/DE Add unkritisch)

**Guardrails Close 16:03 ET:**
```
1. Daily Loss Cap (-3 %):     -0,953 % (vs Mi-Close 98.087,79)                    [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 4 -1,103 % (vs Fr-Close 98.236,14)         [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,912 % (vs ATH 100.066,47)                        [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,912 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Close -1,262 %                                  [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (VXX 22,61 Proxy)                            [GRÜN]
7. Earnings-Blackout (3 HT):  Keine bestätigt                                     [GRÜN]
8. Max Käufe KW30:            1/2 (Slot 2/2 offen letzter Handelstag Fr 24.07.)   [FREI 1]
V-Regel: 6/6 V1-V6 SICHER (Vollcheck V5+V6 Close-Signal-Prüfung)
```

**Entscheidung Market Close 16:03:**
- **Keine Sell-/Limit-Order** (6 V1-V6 SICHER, keine V5/V6-Trigger)
- **Weekly Loss Cap nicht ausgelöst** (-1,103 % > -5 %) → keine pending-Order-Storno, kein Kauf-Sperre
- **ClickUp Tagesbericht Prio 4** (positive Alpha trotz negativer absoluter Perf)
- **PushNotification Prio 3 an Owner** (Tages-Zusammenfassung, GS-Puffer-Watch Fr Pre-Market Fill-Day+7)

**Watchlist morgen (Fr 24.07.):** PSX (XLE, K1-K3 3/3 ✓, Hauptkandidat) | FTI (XLE, K1-K3 3/3 ✓, Backup) | DE (XLI, K1-K3 3/3 ✓, Backup) — K4/K5 zwingend Fr Market Open (Volumen ≥125 % Avg20 + FwdPE≤35 + RevGrowth≥10 % + kein Earnings-Blackout 3 HT).

**Nächster Check:** Fr 24.07. 08:30 ET Pre-Market Check — **GS V1 1.050,40 Puffer +2,32 % ENGSTE Watch** (Fill-Day+7 Give-back-Risiko), LLY XLV-Rebound-Fortsetzung, PSX K4/K5-Multi-Source-Recheck, Alpaca-Bar-Update.

---

## Market Open 09:38 ET — 2026-07-23 (Do, KW30 Tag 4) — ✅ GOOGL V1-Market-Sell ausgeführt, 6 V1-V6 SICHER, kein neuer Kauf (Slot 2/2 offen)

**Alpaca Clock:** is_open=true, timestamp 2026-07-23 09:37:43 ET, next_close 16:00 ET.

**Alpaca /v2/account (Post-GOOGL-Sell 09:38 ET):**
- portfolio_value: **97.176,52 $** (vs Mi-Close 98.087,79 = **-911,27 $ / -0,929 % Daily**) [GRÜN]
- cash: **48.385,53 $** (49,79 %, +8.359,26 vs Pre nach GOOGL-Sell)
- long_market_value: 48.790,99 $ (6 Positionen)
- buying_power: 48.385,53 $

**GOOGL V1-Market-Sell-Ausführung:**
- Alpaca Order ID: 73cac698-9a42-465c-9e5f-32c754eff1c5
- Submission: 09:38:05.232 ET (Market Order, Day, position_intent=sell_to_close)
- Fill: 09:38:05.726 ET (0,5 sec Fill-Latency, 26 Sh × **321,51 $** = **8.359,26 $** Erlös)
- **Realisierter Verlust: -1.211,34 $ (-12,65 %)** vs Entry 368,10 $ (07.07.2026)
- V1-Trigger: Pre-Market 324,23 vs V1 338,65 = -4,26 % / Open 322,00 = -4,91 % unter Stop
- Grund: Q2 CY26 Earnings-Beat-Selloff (EPS 9,11 / Rev 119,8 Mrd BEAT, aber Aftermarket -4,2 % + Pre -4,6 % wegen Capex-Guidance-Sorge — Marktreaktion NEGATIV überwiegt Fundamentals)

**V1-Puffer 6 SICHER Live 09:38 ET (Alpaca /v2/positions current_price, sortiert eng→weit):**
| Sym    | Cur Live   | Entry      | P/L %    | V1-Stop     | Puffer     | Status                    |
|--------|-----------|-----------|---------|------------|-----------|---------------------------|
| **GS** | 1.080,55  | 1.141,74  | -5,36 % | 1.050,40   | **+2,87 %** | SICHER **ENGSTE**, Fill-Day+6 Give-back chg -1,61 % |
| V      |   349,19  |   357,18  | -2,24 % |   328,60   | +6,27 %   | SICHER (Fill-Day+3 Konsolidierung, V5 EMA-Spread +5,63 marginal) |
| LLY    | 1.170,00  | 1.193,89  | -2,00 % | 1.098,38   | +6,52 %   | SICHER (XLV-Rebound chg +0,60 %, RSI-Watch) |
| AAPL   |   322,21  |   316,86  | +1,69 % |   291,51   | +10,53 %  | SICHER (chg -1,13 %) |
| JPM    |   348,44  |   332,78  | +4,71 % |   306,16   | +13,81 %  | SICHER (chg +0,07 % flat) |
| UNH    |   429,42  |   401,57  | +6,94 % |   369,44   | +16,24 %  | SICHER (chg -0,44 %) |

**Makro & Perplexity (Do 23.07. Market Open):**
- **SPY Live 09:39 ET:** Alpaca /v2/stocks/SPY/trades/latest **741,61 $** vs Mi-Close 747,49 = **-0,787 %** [Crash-Filter INAKTIV]
- **VXX Live 09:39:** 22,55 (VIX-Proxy) → VIX ~17-18 carry-over [GRÜN, <30]
- **Perplexity Sektor-Check:** keine belastbaren 3M-RS-Daten geliefert (nur allgemeine ETF-Informationen ohne konkrete 3M-Performance je Sektor). Dominant-Thema laut Perplexity: "Warten auf Tech-Zahlen" → Earnings-Hauptkatalysator
- **Makro:** keine FOMC/CPI/PPI/NFP-Meldung heute (Perplexity kein detaillierter Kalender)

**Kaufsignal-Scan Slot 2/2 KW30 — LEVEL 0 No-Action bei Unsicherheit:**
- Watchlist Do 23.07. (aus Pre-Market): ABBV/MRK/JNJ (XLV, 3/3 K1-K3) — **XLV nach GOOGL-Sell = 20,24 % Portfolio** (UNH 10,61 % + LLY 9,63 %) + neuer XLV ~9 % = ~29,24 % knapp <30 %-Cap
- **Owner-Sektor-Cap-Ambiguität persistiert** — keine Owner-Freigabe zwischen Pre-Market und Market Open erhalten
- XLK-Backup: NVDA/META/MSFT/AMZN blockiert oder AVGO/MU K5-anfällig
- XLE-Kandidaten K3-FAIL, XLI MMM/UPS K5-FAIL
- **Slot 2/2 KW30 bleibt OFFEN bis Fr 24.07.** — kein neuer Kauf ausgeführt, Kauf-Wahrscheinlichkeit weiter GERING

**Sektor-Struktur Post-GOOGL-Sell (Live 09:38 ET):**
- XLC 0 % (GOOGL raus)
- XLF 19,67 % Portfolio (GS+JPM+V)
- XLV 20,24 % Portfolio (UNH+LLY)
- XLK 10,28 % Portfolio (AAPL)

**Guardrails Market Open 09:38 ET:**
```
1. Daily Loss Cap (-3 %):     -0,929 % (vs Mi-Close 98.087,79)                    [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 4 -1,079 % (vs Fr-Close 98.236,14)         [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,888 % (vs ATH 100.066,47)                        [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,888 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Live -0,787 %                                   [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (VXX 22,55 Proxy)                            [GRÜN]
7. Earnings-Blackout (3 HT):  Keine bestätigt (Perplexity)                        [GRÜN]
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                  [FREI 1]
V-Regel: GOOGL V1 AUSGEFÜHRT (Fill @ 321,51 × 26 Sh) — sonstige 6 V1-V6 SICHER
```

**Entscheidung Market Open Do 23.07.:**
- **PRIO 1 (Ausgeführt):** GOOGL V1-Market-Sell Fill @ 321,51 × 26 Sh ✅ (0,5 sec Latency)
- **PRIO 2:** Keine weiteren Trades — 6 V1-V6 SICHER, Slot 2/2 KW30 offen aber No-Action wegen Owner-XLV-Sektor-Cap-Ambiguität + K5-Blockade außerhalb XLV
- **PRIO 3:** GS V1 1.050,40 Puffer +2,87 % ENGSTE, Give-back-Fortsetzung-Watch, Fill-Day+6 Muster

**ClickUp:** Critical-Alert Prio 1 (GOOGL V1) → ITEM_246 persistent → PushNotification Fallback Prio 1 ausgeführt. Routine-Log Prio 4 folgt.

**PushNotification Owner Prio 1 ausgeführt** (GOOGL Fill-Details, Realisierter Verlust, Post-Sell-Status).

**Nächster Check:** Do 23.07. 13:00 ET Midday Stop-Check — GS V1 1.050,40 Puffer +2,87 % ENGSTE zwingend, V/LLY-Watch, UNH XLV-Konsolidierung.

---

## Pre-Market 08:36 ET — 2026-07-23 (Do, KW30 Tag 4) — 🔴 GOOGL V1 VERLETZT Pre-Market nach Q2-Beat-Aftermarket-Selloff, Market-Open-Sell ZWINGEND, sonstige 6 V1-V6 SICHER

**Alpaca Clock:** is_open=false, next_open Do 23.07. 09:30 ET, next_close Do 23.07. 16:00 ET, timestamp 2026-07-23 08:36:03 ET.

**Alpaca /v2/account (08:36 ET Pre-Market):**
- portfolio_value: **97.267,18 $** (vs Mi-Close 98.087,79 = **-820,61 $ / -0,837 % overnight**)
- cash: 40.026,27 $ (41,15 %, unverändert)
- equity: 97.267,18 $
- buying_power: 40.026,27 $ (last_equity 0 = Pre-Market-Reset-Artefakt)
- status: ACTIVE

**Portfolio MV Live: 57.240,81 $ (Alpaca /v2/positions, 7 Pos).**

**GOOGL Q2 CY26 Earnings (Perplexity Multi-Source, Mi 22.07. AMC released):**
- **EPS 9,11 $** (Konsens 2,88–2,89 → **BEAT +216 %**, aber Multi-Source-Konsens war ~2,88 vor Split/Adjustments — Split-Faktor prüfen offen)
- **Revenue 119,8 Mrd. $** (Konsens 116,5–116,9 → **BEAT +2,5 %**)
- **Aftermarket Mi 22.07.:** ~327,40 $ (**-4,2 %** vs Close 341,91)
- **Pre-Market Do 23.07. 08:15 ET:** ~326,10 $ (**-4,6 %**); Alpaca /v2/stocks/GOOGL/trades/latest 08:36 ET → **324,23 $ × 50 Sh** (**-5,26 %** vs Mi-Close, **-11,96 % vs Entry 368,10**)
- **Interpretation:** Trotz Earnings-BEAT-Sell-off (typisch bei hohem Erwartungs-Setup + Capex-Guidance-Sorge) — Marktreaktion NEGATIV überwiegt Fundamentals

**V1-Puffer Pre-Market alle 7 (sortiert eng→weit, Alpaca /v2/positions current_price):**
| Sym    | Cur Pre    | Entry      | P/L %    | V1-Stop     | Puffer     | Status                    |
|--------|-----------|-----------|---------|------------|-----------|---------------------------|
| **GOOGL** | 324,06 (Alpaca current_price) / 324,23 (latest trade) | 368,10 | **-11,96 %** | 338,65 | **-4,26 %** 🔴🔴🔴 | **V1 VERLETZT Pre-Market → Market-Sell 09:30 ET Sofort-Öffnung ZWINGEND** |
| GS     | 1.086,01  | 1.141,74  | -4,88 % | 1.050,40   | +3,39 %   | SICHER (verschlechtert vs Mi-Close +4,55 % um -1,16 pp overnight-Drift) |
| LLY    | 1.151,00  | 1.193,89  | -3,59 % | 1.098,38   | +4,79 %   | SICHER (leicht verschlechtert vs Mi-Close +5,53 % um -0,74 pp) |
| V      | 353,38    | 357,18    | -1,06 % | 328,60     | +7,54 %   | SICHER (marginal verschlechtert vs Mi-Close +7,55 %) |
| AAPL   | 324,33    | 316,86    | +2,36 % | 291,51     | +11,26 %  | SICHER (leicht verschlechtert vs Mi-Close +11,87 % um -0,61 pp) |
| JPM    | 349,12    | 332,78    | +4,91 % | 306,16     | +14,03 %  | SICHER (marginal verbessert vs Mi-Close +13,96 %) — **HINWEIS: Nur 3 Shares in Alpaca (Alpaca /v2/orders bestätigt Original-Fill 17.06. 3 Sh @ 332,78), Portfolio/Trade-Log-Discrepancy pre-existing, MV 1.047,36** |
| UNH    | 428,18    | 401,57    | +6,63 % | 369,44     | +15,90 %  | SICHER (leicht verschlechtert vs Mi-Close +16,74 % um -0,84 pp) |

**Makro & Perplexity (Do 23.07. Pre):**
- **VIX:** ~17–18 (Perplexity, Realtime-Bandbreite 17,6-18,8) [GRÜN, <30]
- **SPY Pre-Market:** Alpaca /v2/stocks/SPY/trades/latest 08:28 ET **742,12 $** vs Mi-Close 747,49 = **-0,718 %** (Perplexity Realtime-% nicht verfügbar, harte Alpaca-Trade-Quote genommen)
- **10Y Treasury:** Perplexity keine harte Realtime-Zahl (~3,9-4,0 % carry-over)
- **Makro heute (US):** Jobless Claims wöchentlich, ggf. PMI-Flash, keine FOMC/CPI/PPI/NFP (Perplexity kein konkreter Kalender)
- **Top-News:** GOOGL Q2 Post-Release Marktreaktion dominant; keine anderen konkreten Katalysatoren aus Perplexity

**Earnings-Blackout 3 HT (Do 24.07. - Mo 28.07.) Perplexity:**
- **Kein detaillierter S&P-500-Kalender für 24./25./28.07. verfügbar** (Perplexity: "Anbieter veröffentlichen Tageslisten erst wenige Wochen vor Quartal")
- Position-Watch: AAPL/JPM/GS/UNH/LLY/V/GOOGL — **kein bestätigter Blackout-Eintrag** in Perplexity-Multi-Source für diesen Zeitraum
- Bei Unsicherheit: **Stop-Loss -8 % V1-Standard beibehalten**, keine unnötige V1-Tightening auf -5 %
- Owner-Notification bei tagesgenauer Info empfohlen

**Guardrails Pre-Market 08:36 ET:**
```
1. Daily Loss Cap (-3 %):     -0,837 % (vs Mi-Close 98.087,79)                  [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 4 -0,986 % (vs Fr-Close 98.236,14)       [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,797 % (vs ATH 100.066,47)                      [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,797 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Pre -0,718 % vs Mi-Close                      [INAKTIV]
6. VIX-Filter (>30):          ~17-18                                            [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Post-Release obsolet, keine neuen bestätigt [GRÜN]
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                [FREI 1]
V-Regel: **GOOGL V1 VERLETZT Pre-Market** → Market-Sell 09:30 ET Öffnung ZWINGEND
```

**Entscheidung Market-Open-Scan Do 23.07.:**
- **PRIO 1 (Kritisch):** **GOOGL V1 338,65 VERLETZT Pre-Market (324,23 = -4,26 % unter Stop)** → **Market-Sell 26 Shares @ Open 09:30 ET SOFORT** (V1-Regel: Market Order SOFORT). Cash-Zufluss geschätzt ~8.430 $ bei Open-Preis ~324, Realisierter Verlust geschätzt **-1.140 $ (-11,96 %)** vs Entry 368,10.
- **PRIO 2:** Nach GOOGL-Sell: 6 Positionen offen, Cash ~48.460 $ (~49,8 %), Slot 2/2 KW30 offen bis Fr 24.07. — **Kauf-Wahrscheinlichkeit weiterhin GERING** ohne Owner-XLV-Freigabe (ABBV/MRK/JNJ 3/3 K1-K3 Sektor-Cap-Pending) oder frischen K5-Kandidaten außerhalb XLK/XLC/XLV
- **PRIO 3:** GS Rebound-Fortsetzung (Puffer +3,39 % erholt vs Mo-Tief), LLY RSI-Watch, kein weiterer V1-Alarm

**GOOGL-Post-Sell Sektor-Struktur (nach Market-Open-Execution):**
- XLC-Sektor: 0 % (GOOGL war einzige XLC-Position)
- XLF unverändert 33,37 % investiert / 19,75 % Portfolio (GS+JPM+V)
- XLV unverändert 33,80 % investiert / 20,00 % Portfolio (UNH+LLY)
- XLK unverändert (AAPL)

**ClickUp:** Critical-Alert Prio 1 (V1-Trigger GOOGL) + Routine-Log Prio 4 (Pre-Market fertig). Fallback PushNotification bei ClickUp-"Team not authorized"-Persistenz.

**PushNotification Owner Prio 1** (V1 GOOGL Pre-Market Trigger, Sofort-Sell Market Open zwingend, Realisierter Verlust ~-1.140 $).

**Nächster Check:** Do 23.07. 09:30 ET Market Open — **GOOGL V1-Market-Sell Sofort-Öffnung Ausführung**, danach Kaufsignal-Scan Slot 2/2 KW30 (Kauf-Wahrscheinlichkeit GERING).

---

## Market Close 16:03 ET — 2026-07-22 (Mi, KW30 Tag 3) — Alle 7 V1-V6 SICHER, KEINE Limit-Order Do 23.07., GOOGL Q2 AMC Post-Close released, Puffer +1,07 % KRITISCH

**Alpaca Clock:** is_open=false, next_open Do 23.07. 09:30 ET, next_close Do 23.07. 16:00 ET, timestamp 2026-07-22 16:02:52 ET.

**Account Close 16:03 ET (Alpaca /v2/account):**
```
Equity End:        98.087,79 $   (portfolio_value)
Cash:              40.026,27 $   (40,81 %)
Portfolio_MV:      58.061,52 $   (59,19 %, 7 Positionen, Alpaca /v2/positions)
Buying_power:     322.677,33 $
Käufe KW30:        1/2           (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Pending Orders:    0
Daily P/L:         -0,3326 %     (vs last_equity 98.415,10, -327,31 $)
Weekly KW30 Tag 3: -0,1510 %     (vs Fr-Close 98.236,14, -148,35 $)
DD vs ATH:         -1,9774 %     (ATH 100.066,47)
```

**Positionen Close 16:03 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**
- **GOOGL 342,27** (P/L -7,02 %, chg -1,41 %) V1-Puffer **+1,069 % KRITISCH ENGSTE ALLER ZEITEN** (verschlechtert vs Open +2,40 %)
- **GS 1.098,20** (P/L -3,81 %, chg +1,16 %) V1-Puffer **+4,55 %** (Rebound-Tag+2 verbessert vs Open +4,16 %)
- LLY 1.159,11 (P/L -2,91 %, chg -1,39 %) V1-Puffer +5,53 % (verschlechtert vs Open +6,17 %, XLV-Konsolidierung, RSI unter 50)
- V 353,42 (P/L -1,05 %, chg -0,67 %) V1-Puffer +7,55 % (Fill-Day+2)
- AAPL 326,12 (P/L +2,92 %, chg -0,49 %) V1-Puffer +11,87 %
- JPM 348,90 (P/L +4,84 %, chg +1,06 %) V1-Puffer +13,96 % (XLF-Rebound-Tag+2)
- UNH 431,31 (P/L +7,41 %, chg -1,16 %) V1-Puffer **+16,74 %** (Beste-P/L)

**SPY IEX Close 747,49** (vs Di-Close 748,155 = **-0,089 %**; vs Fr-Close 743,28 = **+0,566 %**) → **Crash-Filter INAKTIV**. **Alpha Daily -0,244 pp** (Portfolio -0,333 % vs SPY -0,089 %) [LEICHT NEGATIV]. **Alpha Weekly KW30 -0,717 pp** (Portfolio -0,151 % vs SPY +0,566 %) [NEGATIV Wochen-Alpha].

**GOOGL Q2 2026 Earnings AMC HEUTE Post-Close (Perplexity Multi-Source):**
- **Released Post-4pm ET** — Call 4:30 pm ET (nicht vor 4pm)
- Preview-Konsens: **EPS ~$2,87 / Revenue $116,5–116,9 Mrd / Capex-Guidance höher erwartet**
- Actual EPS/Rev noch nicht in Feed (bei Routinen-Ausführung 16:03 ET)
- **Blackout jetzt obsolet** (Post-Release), Owner-Freigabe LETZTE CHANCE 15:59 ET **VERPASST**
- V1 338,65 Puffer nur +1,07 % → **jede -1,08 %-Öffnungs-Reaktion morgen triggert Sofort-Sell**
- Historische GOOGL-Post-Q2-Vola: Median-Move ±3-5 % typisch → **Öffnungs-Reaktion ≥ ±3 % wahrscheinlich**

**Perplexity Sektor-Strength-Check (Mi 22.07. Close-Fenster) — Watchlist Do 23.07.:**
- **Sektor-RS 4w:** XLK (#1), XLI, XLE, XLF, XLV
- **Sektor-RS 3M:** XLK (#1), XLE, XLV, XLI, XLB
- **Top-3M-Momentum-Stocks Perplexity:** NVIDIA, Broadcom (AVGO), Meta Platforms, Microsoft, Amazon
- **Bewertung:** ALLE 5 aus XLK/XLC → K5-anfällig (AVGO/NVDA historisch FwdPE-Range grenzwertig 20-41+, wie AMD-Reject 14.07.) oder Doppel-Sektor-Belegung (META vs GOOGL XLC bereits belegt, AMZN XLC)

**K1-K5-Kompatibilität der starken Sektoren (Kurzform-Prüfung):**
- **XLE-Top-Holdings** (XOM/CVX/COP): alle K3-FAIL Vortag-Screener (Ret63 vs SPY negativ -1,29 % bis -4,63 %) → REJECT
- **XLI-Top-Kandidaten** (MMM/UPS/HON/RTX/CAT/DE/LMT/NOC): MMM K5-FAIL (TTM Rev +2,4 %), UPS K5-permanent-FAIL (-2,65 %), HON/RTX/CAT/DE/LMT/NOC K3-FAIL Vortag → REJECT alle
- **XLB**: nicht gescreent frisch (Zeit-Constraint 16:03 ET), typische Top-Holdings LIN/APD/SHW → K3-Risiko historisch hoch
- **XLV-Backup** (ABBV 256,14 / MRK 126,26 / JNJ 250,66): alle 3/3 K1-K3 ✓, aber **XLV-Sektor-Cap-Owner-Entscheidung weiter Pending** (aktuell 20,00 % + neu ~9 % = ~29 % formal <30 %-Cap, aber Owner-Ambiguität seit KW29 → LEVEL 0)

**Entscheidung Market-Close-Watchlist Do 23.07.:**
- Kein 5/5 K-Signal-Kandidat außerhalb XLV bestätigt
- XLV-Trio Owner-Pending → **LEVEL 0 "No-Action bei Unsicherheit"**
- Slot 2/2 KW30 bleibt OFFEN bis Fr 24.07. — Kauf-Wahrscheinlichkeit gering

**V1-V6-Sell-Check alle 7 SICHER (Alpaca Bars 210d Recompute Close):**
- V1 (Stop -8 %): GOOGL **+1,07 % KRITISCH ENGSTE ALLER ZEITEN**, alle anderen >4 %
- V2 (52w × 0,88): keine Verletzung
- V3/V4 (Gewinn ≥ 20/35 %): max UNH +7,41 % << 20 %
- V5 (EMA50 < EMA200): alle sicher (Golden Cross intakt): GOOGL Spread +38,06 / GS +119,99 / LLY +115,24 / AAPL +26,98 / V +5,63 (marginal) / JPM +12,73 / UNH +51,28
- V6 (RSI > 80 UND RS_4w < 0): max RSI 66,01 (JPM) << 80, GOOGL RSI 40,23 + RS_4w -3,10 % erfüllt V6-Teil aber RSI << 80, GS RSI 56,56 + RS_4w -1,57 % analog → V6 verlangt BEIDES → nicht ausgelöst
- **→ KEINE Sell-Order 16:03 ET, KEINE Limit-Order für Do 23.07.** platziert

**Weekly Loss Cap Check KW30 Tag 3 = -0,151 %** [GRÜN, Cap -5 % weit entfernt] → **keine Cash-Aktion, keine Order-Stornierung** (auch nichts pending, 0 open orders).

**PushNotification Prio 2 an Owner:** GOOGL Puffer +1,07 % KRITISCH ENGSTE ALLER ZEITEN + Q2 AMC Post-Release HEUTE → morgen Öffnungs-Reaktion kritisch, V1 338,65 Sofort-Sell bei -1,08 %-Move. **ClickUp Tagesbericht Prio 3** (negative Perf) — Fallback PushNotification bei API-Fehler.

**Nächste Routine:** Do 23.07. 08:30 ET Pre-Market — GOOGL V1 338,65 zwingender Sofort-Sell-Watch nach Q2-Post-Release, GS V1 1.050,40 Rebound-Fortsetzung, LLY RSI-Watch.

---

## Market Open 09:40 ET — 2026-07-22 (Mi, KW30 Tag 3) — Alle 7 V1-V6 SICHER, KEIN Kauf (LEVEL 0), Sektor-RS XLE #1 aber K3-blocked

**Alpaca Clock:** is_open=true, next_close Mi 22.07. 16:00 ET.

**Account Live 09:40 ET (Alpaca /v2/account):**
```
Equity:            98.406,07 $   (portfolio_value)
Cash:              40.026,27 $   (40,67 %)
Portfolio_MV:      58.379,80 $   (59,33 %, 7 Positionen, Alpaca /v2/positions live)
Buying_power:     323.568,52 $
Käufe KW30:        1/2           (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Pending Orders:    0
Daily P/L:         -0,009 %      (vs last_equity 98.415,10, -9,03 $)
Weekly KW30 Tag 3: +0,173 %      (vs Fr-Close 98.236,14, +169,93 $)
DD vs ATH:         -1,659 %      (ATH 100.066,47)
```

**Positionen Live 09:40 ET (Alpaca latest trades IEX) — sortiert Puffer ENG→WEIT:**
- GOOGL 346,78 (P/L -5,79 %) V1-Puffer **+2,40 % ENGSTE**, Blackout Tag 0 AMC HEUTE V1_neu 349,70 > Kurs = -0,84 % neg
- GS 1.094,14 (P/L -4,17 %) V1-Puffer +4,16 % (Rebound-Tag+2)
- LLY 1.166,11 (P/L -2,33 %) V1-Puffer +6,17 %
- V 355,11 (P/L -0,58 %) V1-Puffer +8,07 %
- AAPL 327,755 (P/L +3,44 %) V1-Puffer +12,43 %
- JPM 345,355 (P/L +3,78 %) V1-Puffer +12,80 %
- UNH 435,73 (P/L +8,51 %) V1-Puffer **+17,94 %**, Beste-P/L

**SPY Live 747,295 vs Fr-Close 743,28 = +0,540 %** (Crash-Filter INAKTIV). Alpha vs SPY -0,549 pp (Portfolio ±0 vs SPY +0,540 %) [LEICHT NEGATIV Momentaufnahme 10min in Session].

**Perplexity Sektor-Strength-Check (Mi 22.07. 09:40 ET):**
- **XLE** — 3M-Return **+6,23 %** klar #1 (momentum-trend positiv/führend)
- **XLI** — Leading-Quadrant im RS-Schema (kein exakter 3M-Wert belegt)
- **XLU** — defensiv-vorne (kein exakter 3M-Wert belegt)
- Top-News: Mittelost-Spannungen US/Iran-Öl (XLE-treibend), VIX-Regime neutral/chop, S&P nahe Hoch

**K1-K5-Kompatibilität der starken Sektoren (vs Pre-Market-Screener):**
- **XLE-Top-Holdings** (XOM/CVX/COP): alle **K3-FAIL** (Ret63 vs SPY negativ -1,29 % bis -4,63 %) — Sektor läuft jetzt, aber 63d-Rückblick noch negativ → REJECT alle
- **XLI-Top-Kandidaten** (MMM/UPS/HON/RTX/CAT/DE/LMT/NOC): MMM heute **K5-REJECT** (TTM Rev +2,4 % << 10 %), UPS K5-permanent-FAIL (-2,65 %), HON K3 -55,55 %, RTX K3 -6,62 %, CAT K2 43,00 <50, DE K3 -6,84 %, LMT K3 -18,33 %, NOC K3 -27,76 % → REJECT alle
- **XLU**: nicht gescreent (Zeit-Constraint 09:40 ET, aber typische Top-Holdings NEE/DUK/SO defensiv-langsam → K3-Risiko hoch)
- **XLV-Backup** (ABBV 256,14 / MRK 126,26 / JNJ 250,66): alle 3/3 K1-K3 ✓, aber **XLV-Sektor-Cap-Owner-Entscheidung Pending** (aktuell 20,10 % + neu ~9 % = ~29 % formal <30 %-Cap, aber Owner-Ambiguität dauert seit KW29 an → LEVEL 0)

**Entscheidung Market-Open-Scan Mi 09:40 ET:** **KEIN Kauf**
- Kein 5/5 K-Signal-Kandidat außerhalb XLV bestätigt
- XLV-Trio Owner-Pending → **LEVEL 0 "No-Action bei Unsicherheit"**
- Slot 2/2 KW30 bleibt OFFEN bis Fr 24.07.

**V1-V6-Sell-Check alle 7 SICHER:**
- V1 (Stop-Loss -8%): engste GOOGL +2,40 %, alle >4 %
- V2 (52w-Trailing): keine Verletzung
- V3/V4 (Gewinn ≥20/35%): max UNH +8,51 % << 20 %-Schwelle
- V5 (EMA50<EMA200): alle negativ (Golden Cross intakt, Details siehe Close 21.07.)
- V6 (RSI>80 UND RS_4w<0): max RSI ~64 (AAPL/V) << 80-Threshold
- **→ KEINE Sell-Order 09:40 ET**

**GOOGL Blackout-Verlauf HEUTE (Timeline):**
- Mo-Close +0,69 % pos → Di-Pre +0,41 % → Di-Open -0,05 % → Di-Close -0,67 % → Mi-Pre -0,47 % → **Mi-Open 09:40 -0,84 % NEGATIV** (weiter verschlechtert)
- V1_neu Blackout 349,70 > Kurs 346,78 → Aktivierung würde AKTUELL Sofort-Stop auslösen
- **Owner-Freigabe LETZTE CHANCE bis 15:59 ET** vor AMC Q2 Earnings
- Empfehlung: Option A Strategie-Lock beibehalten (funktional wirkungslos bei aktueller Kurslage)

**Nächste Routine:** Mi 22.07. 13:00 ET Midday Stop-Check.

---

## Pre-Market 08:36 ET — 2026-07-22 (Mi, KW30 Tag 3) — Alle 7 V1 Pre SICHER (Puffer erholt), GOOGL Blackout-Sensitivität HEUTE LETZTE CHANCE Owner-Freigabe, MMM K5-FAIL Multi-Source, Slot 2/2 Owner-Pending

**Alpaca Clock:** is_open=false, next_open Mi 22.07. 09:30 ET, timestamp 2026-07-22 08:36:08 ET.

**Account Pre-Market 08:36 ET (Alpaca /v2/account):**
```
Equity:            98.500,63 $   (portfolio_value)
Cash:              40.026,27 $   (40,64 %)
Portfolio_MV:      58.471,25 $   (59,36 %, 7 Positionen, Alpaca /v2/positions live)
Buying_power:     323.833,30 $
Käufe KW30:        1/2           (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Pending Orders:    0
Daily P/L Pre:     +0,087 %      (vs Alpaca last_equity 98.415,10, +85,53 $)
                   +0,085 %      (vs Memory Close 21.07. 98.417,11, +83,52 $)
Weekly KW30 Tag 3: +0,269 %      (vs Fr-Close 98.236,14, +264,49 $)
DD vs ATH:         -1,566 %      (ATH 100.066,47, verbessert vs Close -1,648 %)
```

**Positionen Pre-Market 08:36 ET (Alpaca /v2/positions) — sortiert Puffer ENG→WEIT:**

| Sym    | Pre-Kurs   | Entry      | P/L %    | V1-Stop     | V1-Puffer       | Δ vs Close | Status |
|--------|------------|------------|----------|-------------|-----------------|------------|--------|
| **GOOGL**|  348,07  | 368,10     | -5,44 %  | 338,65      | **+2,78 %** 🔴  | +0,21 pp   | SICHER ENGSTE (Blackout Tag 0 AMC HEUTE, V1_neu 349,70 > Kurs = **-0,47 % negativ** → Aktivierung würde Sofort-Stop; verbessert vs Close -0,67 %; Option A Strategie-Lock aktiv, **Owner-Freigabe LETZTE CHANCE bis 15:59 ET**) |
| **GS** | 1.088,27   | 1.141,74   | -4,68 %  | 1.050,40    | **+3,60 %**     | +0,25 pp   | SICHER (leicht erholt vs Close +3,35 %, Fill-Day+4-Muster überwunden, Rebound Tag +1) |
| LLY    | 1.173,00   | 1.193,89   | -1,75 %  | 1.098,38    | +6,79 %         | -0,17 pp   | SICHER (marginal verschlechtert vs Close +6,96 %, aber RSI-Watch nach gestrigem Rebound +2,43 %) |
| V (NEU)|   356,40   |   357,18   | -0,22 %  |   328,60    | **+8,46 %**     | +0,18 pp   | SICHER (Fill-Day+2, Konsolidierung nach Vortag-Drop, V5 EMA-Spread bleibt marginal aber Golden Cross intakt) |
| AAPL   |   327,75   |   316,86   | +3,44 %  |   291,51    | +12,43 %        | +0,15 pp   | SICHER (leicht verbessert vs Close +12,28 %) |
| JPM    |   345,40   |   332,78   | +3,79 %  |   306,16    | +12,82 %        | +0,13 pp   | SICHER (leicht verbessert vs Close +12,69 %) |
| UNH    |   438,00   |   401,57   | +9,07 %  |   369,44    | **+18,56 %**    | +0,27 pp   | SICHER (Beste-P/L komfortabel, verbessert vs Close +18,29 %) |

**Perplexity Makro-Check (Mi 22.07. Pre-Market):**
- **VIX:** ~17–18 (Realtime-Bandbreite 17,5–18,8) → GRÜN (<30, unter Filter)
- **SPY Pre-Market:** keine harte Realtime-Quote in Perplexity-Feeds, Futures-Indikation **±0,3 %** → **Crash-Filter INAKTIV** (weit von -5 %)
- **10Y Treasury Yield:** ~3,9–4,0 % (leicht niedriger vs Vortag 4,25-4,35 %)
- **Makro-Ereignisse heute:** KEINE FOMC/CPI/PPI (nur Wochen-Housing/Mortgage-Applications sekundär, mögliche Flash-PMIs, Jobless Claims erst Do) → **kein primärer Katalysator**
- **Top-News:** (1) Mittelost-Spannungen US/Iran-Öl-Infrastruktur, Brent höher; (2) VIX-Regime "neutral/chop" nach jüngstem Sprung; (3) S&P 500 nahe Hoch, VIX-Termstruktur Contango, taktisches Risk-On

**Earnings-Blackout Check (Perplexity Multi-Source, Fenster Mi-Fr 22.-24.07.):**
- **GOOGL:** Mi 22.07. AMC bestätigt (Multi-Source [1][2][6][10][16]) → **Tag 0 heute AMC** — Blackout aktivierungssensitiv negativ -0,47 %
- **UNH/JPM/AAPL/LLY/GS/V/MMM:** kein Earnings in diesem Fenster → keine Blackout-Aktion nötig
- **MMM Q2 CY2026 BMO Di 21.07.** bereits gemeldet (Perplexity [1][3][15]) — **kein Blackout mehr aktiv**

**MMM K5-Multi-Source-Recheck (Watchlist-Prio Slot 2/2 KW30) — REJECT:**
- FwdPE: GuruFocus ~19,0x / StockAnalysis ~18,5x / AlphaSpread ~18,0x → alle ≤ 35 ✓
- **TTM Revenue-Growth YoY: +2,4 %** (Q2 2026: 6,5 Mrd $) → **K5-FAIL** (Kriterium ≥ +10 %)
- → **MMM REJECT** (analog UPS K5 dauerhaft-blocked); Watchlist-Prio-Kandidat entfällt

**Guardrails Pre-Market alle 7 GRÜN + 1 WARN (GOOGL Blackout zeitkritisch):**
```
1. Daily Loss Cap (-3 %):     Pre +0,087 %                                        [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 3 +0,269 %                                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,566 %                                            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,566 %                                            [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Pre ±0,3 %                                      [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (Perplexity)                                 [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi 22.07. AMC Tag 0 aktivierungssensitiv -0,47 % (Owner-Pending LETZTE CHANCE) | [WARN — GOOGL zeitkritisch] |
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                  [FREI 1]
```

**Entscheidung Market-Open-Scan 09:30 ET:** **JA** (7/8 GRÜN, Slot 2/2 offen)
- **Kandidaten-Update Slot 2/2:** MMM entfällt (K5-FAIL), UPS entfällt (K5-FAIL); nur noch **ABBV/MRK/JNJ (XLV)** verfügbar → **Owner-Sektor-Cap-Entscheidung zwingend** vor Kauf (aktuell XLV 20,21 % + neu ~9 % = 29 % knapp am 30 % Cap)
- Alternative Screener: neue Non-XLK/XLV/XLF/XLC-Symbole (XLI/XLP/XLE/XLU/XLB) Mi Pre-Market prüfen, aber alte Rejects K3-negativ/K5-Fail

**GOOGL Blackout-Aktivierungssensitivität Verlauf — LETZTE ENTSCHEIDUNGSCHANCE:**
- Mo-Close +0,69 % pos → Di-Pre +0,41 % pos → Di-Open -0,05 % neg → Di-Close -0,67 % neg → **Mi-Pre -0,47 % neg**
- V1_neu Blackout 349,70 > Kurs 348,07 → Aktivierung würde Sofort-Stop auslösen
- Q2 CY26 Earnings HEUTE Mi 22.07. AMC bestätigt Multi-Source
- **Owner-Freigabe muss bis 15:59 ET heute erfolgen** — danach ist Blackout obsolet (Earnings-Ereignis eingetreten)
- Empfehlung: **Option A Strategie-Lock beibehalten** (Standard V1 338,65) — Aktivierung wäre bei aktueller Kurslage sofort-Stop-auslösend, damit funktional wirkungslos für Schutz vor Earnings-Move

**Nächste Routine:** Mi 22.07. 09:30 ET Market Open + Kaufsignal-Scan (Slot 2/2 KW30 Owner-Pending XLV-Sektor-Cap; V1-Watch GOOGL/GS; Post-Open Bestätigung SPY-Bewegung + VIX).

---

## Market Close 16:03 ET — 2026-07-21 (Di, KW30 Tag 2) — Alle 7 V1-V6 SICHER, GS Rebound-Tag +2,89 %, Daily +0,64 %, Alpha -0,16 pp, MMM NEUER 3/3-Lead

**Alpaca Clock:** is_open=false, next_open Mi 22.07. 09:30 ET.

**Account Close 16:03 ET (Alpaca /v2/account):**
```
Equity:            98.417,11 $   (portfolio_value)
Cash:              40.026,27 $   (40,67 %)
Portfolio_MV:      58.390,84 $   (59,33 %, 7 Positionen)
Buying_power:     323.599,42 $
Käufe KW30:        1/2           (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Pending Orders:    0             (keine V5/V6-Trigger → keine Limit-Order Mi)
Daily P/L:         +0,6444 %     (vs last_equity 97.786,94, +630,17 $)
Weekly KW30 Tag 2: +0,184 %      (vs Fr-Close 98.236,14)
DD vs ATH:         -1,648 %      (ATH 100.066,47)
SPY Close IEX:     748,155       (+0,8091 % vs Mo-Close 742,15)
Alpha vs SPY:      -0,165 pp     (leicht negativ, Portfolio-Rebound aber SPY-Rebound stärker)
```

**Positionen Close 16:03 ET — sortiert Puffer ENG→WEIT:**

| Sym    | Close      | Entry      | Chg    | P/L %    | V1-Stop     | V1-Puffer     | Status |
|--------|------------|------------|--------|----------|-------------|---------------|--------|
| **GOOGL**|  347,36  | 368,10     | -1,32% | -5,63 %  | 338,65      | **+2,57 %**   | SICHER **ENGSTE** (Mo +3,97 % → -1,40 pp, Blackout-Aktivierungssensitivität -0,67 % neg V1_neu 349,70 > Kurs, Option A Lock, Owner-Freigabe LETZTE CHANCE Mi Vormittag) |
| **GS** | 1.085,56   | 1.141,74   | +2,89% | -4,92 %  | 1.050,40    | **+3,35 %**   | SICHER **REBOUND-TAG** (Mo +0,50 % → +2,85 pp, Fill-Day+4-Muster AVGO/MU-Präzedenz überwunden) |
| LLY    | 1.174,80   | 1.193,89   | +2,43% | -1,60 %  | 1.098,38    | +6,96 %       | SICHER REBOUND (Mo -2,78 % → +2,43 % chg, RSI ~49 XLV-Watch stabilisiert) |
| V (NEU)|   355,82   |   357,18   | -1,32% | -0,38 %  |   328,60    | +8,28 %       | SICHER (Fill-Day+1 -1,32 % Konsolidierung, V5 EMA-Spread +4,17 marginal aber intakt) |
| AAPL   |   327,305  | 316,86     | +0,22% | +3,30 %  |   291,51    | +12,28 %      | SICHER (leicht verbessert vs Mo +12,05 %) |
| JPM    |   345,00   |   332,78   | +1,81% | +3,67 %  |   306,16    | +12,69 %      | SICHER (verbessert vs Mo +10,69 %) |
| UNH    |   437,00   |   401,57   | +3,67% | +8,82 %  |   369,44    | **+18,29 %**  | SICHER **BESTE Chg heute + beste P/L Portfolio** |

**V1-V6-Check alle 7 SICHER:** kein V1-Break (engste GOOGL +2,57 %), V2-Trail weit vom 52w-Hoch, V3/V4 max UNH +8,82 % (<< +20 % TP-Schwelle), V5/V6 alle SICHER (EMA50>EMA200 überall, RSI max ~64 << 80). **→ KEINE Limit-Order für Mi 22.07.**

**GOOGL Blackout-Aktivierungssensitivität Verlauf (LETZTE CHANCE Mi Vormittag):**
- Mo-Close +0,69 % positiv → Di-Pre +0,41 % positiv → Di-Open -0,05 % negativ → **Di-Close -0,67 % negativ**
- V1_neu Blackout = 349,70 (368,10 × 0,95 = -5 %) > Kurs 347,36
- Aktivierung würde JETZT Sofort-Stop auslösen → Option A Strategie-Lock beibehalten
- Q2 CY26 Earnings Mi 22.07. AMC bestätigt (Perplexity Multi-Source Vortag)
- **PushNotification Prio 3 an Owner** zwingend (Blackout-Entscheidung morgen Vormittag zeitkritisch)

**Sektor-Gewichte Close (alle unter 30 %-Portfolio-Cap):**
- XLF: GS+JPM+V 19.327 (33,10 % invest / 19,64 % Portfolio) ⚠ investiert>30% SAFE Portfolio
- XLV: UNH+LLY 19.886 (34,06 % invest / 20,21 % Portfolio) ⚠ investiert>30% SAFE Portfolio
- XLK: AAPL 10.146 (17,38 % invest / 10,31 % Portfolio) GRÜN
- XLC: GOOGL 9.031 (15,47 % invest / 9,18 % Portfolio) GRÜN

**Kandidaten-Scan Slot 2/2 KW30 (Alpaca-Screener 20 Non-XLK/XLV/XLF/XLC-Symbole, Di-Close als Basis, 306 komplette Bars):**

| Sym | Close | EMA50 | EMA200 | Spread | RSI(14) | Ret63 | RS_63d | K1 | K2 | K3 | K/3 |
|-----|-------|-------|--------|--------|---------|-------|--------|----|----|----|-----|
| **MMM (NEU)** | 170,72 | 157,27 | 155,14 | +2,12 | **68,72** | +12,73 % | **+7,18** | ✓ | ✓ | ✓ | **3/3** |
| **UPS** | 116,33 | 108,65 | 102,55 | +6,10 | 61,49 | +8,57 % | +3,02 | ✓ | ✓ | ✓ | **3/3** |
| **ABBV** | 256,14 | 235,22 | 219,87 | +15,35 | 65,16 | +25,76 % | +20,21 | ✓ | ✓ | ✓ | **3/3** |
| **MRK** | 126,26 | 121,36 | 109,05 | +12,31 | 54,94 | +7,85 % | +2,30 | ✓ | ✓ | ✓ | **3/3** |
| **JNJ** | 250,66 | 243,87 | 220,34 | +23,53 | 51,92 | +8,66 % | +3,11 | ✓ | ✓ | ✓ | **3/3** |
| KO | 81,96 | 81,11 | 76,45 | +4,66 | 49,55 ✗ | +8,57 % | +3,02 | ✓ | ✗ | ✓ | 2/3 |
| CVX | 191,06 | 181,53 | 174,64 | +6,89 | 67,69 | +4,26 % | -1,29 | ✓ | ✓ | ✗ | 2/3 |
| XOM | 151,70 | 145,15 | 137,48 | +7,67 | 65,99 | +2,76 % | -2,80 | ✓ | ✓ | ✗ | 2/3 |
| CAT | 889,77 | 913,54 | 735,71 | +177,83 | 43,00 ✗ | +11,42 % | +5,87 | ✓ | ✗ | ✓ | 2/3 |
| GE  | 340,64 | 340,17 | 309,34 | +30,83 | 42,71 ✗ | +12,24 % | +6,68 | ✓ | ✗ | ✓ | 2/3 |
| HON,RTX,COP,DE,LMT,NOC,WMT,PG,PEP,COST | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | 0-1/3 |

**Kandidaten-Bewertung Slot 2/2 KW30:**
- **MMM (NEU) 170,72** (XLI Industrials) — echter neuer Fund, K1-K3 3/3, RSI 68,72 knapp am Cap 70 (K2 grenzwertig). **K5-Recheck + Earnings-Blackout Mi Pre-Market zwingend** (Q2 typisch Ende Juli, 5-8 HT-Fenster kritisch). Priorität 1 für Mi.
- **UPS 116,33** (XLI Industrials) — 3/3 K1-K3, aber **K5-permanent-FAIL** (Multi-Source-TTM -2,65 %, MRQ -0,3 % — alle Sources negativ, dokumentiert Di 21.07. Market Open) → REJECT stabil, kein Recheck nötig
- **ABBV/MRK/JNJ** (XLV Healthcare, alle 3/3) — XLV-Sektor-Cap-Deutungsfrage weiter Owner-Pending. Aktuell XLV 20,21 % Portfolio + ~9 % Neuposition = ~29 % knapp am 30 %-Cap → nur bei Owner-Freigabe möglich.
- **KO 81,96** — gefallen aus 3/3 (RSI 49,55 K2-Fail durch heutigen leichten Rücksetzer -0,18 %). K5-Konflikt aus Di Market Open weiter dokumentiert.
- **AMD/PANW** — K5-permanent-blocked FwdPE > 35 Multi-Source (dokumentiert 14.07./17.07./20.07.)

**Guardrail-Check alle 8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     +0,644 %                                          [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 2 +0,184 %                               [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,648 %                                          [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,648 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,809 %                                      [INAKTIV]
6. VIX-Filter (>30):          ~17-18 (carry-over Pre-Market Perplexity)         [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi AMC Tag 0 (Option A Owner-Pending, aktivierungssensitiv -0,67 % negativ) | MMM Q2 ~Ende Juli (5-8 HT — Recheck Mi Pre-Market) | [WARN — GOOGL zeitkritisch] |
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07.)                [FREI 1]
```

**Entscheidung Market Close 16:03 Di 21.07.:**
- **Sell-Seite: keine Aktion** (alle 7 V1-V6 SICHER, keine V5/V6-Trigger, GS/LLY Rebound-Tag)
- **Limit-Order Mi: KEINE** (kein V5/V6-Signal ausgelöst)
- **GOOGL Blackout-Owner-Freigabe: PushNotification erneut Prio 3** (LETZTE CHANCE Mi Vormittag zwingend, Aktivierungssensitivität negativ)
- **Slot 2/2 KW30 OFFEN** bis Fr 24.07. — MMM als neuer Top-Kandidat, K5-Recheck Mi Pre-Market

**Nächste Routine:** Mi 22.07. 08:30 ET Pre-Market Check — GOOGL V1 338,65 + Blackout-Entscheidung LETZTE CHANCE, GS V1 1.050,40 (Rebound-Fortsetzung?), LLY V1 1.098,38 (Rebound-Fortsetzung?), MMM K5-Multi-Source-FwdPE + Rev-Growth + Q2-Earnings-Datum.

---

## Market Open 09:40 ET — 2026-07-21 (Di, KW30 Tag 2) — Alle 7 V1-V6 SICHER, GS Puffer +2,17 % ERHOLT, KO+UPS K5-FAIL → KEIN Kauf

**Alpaca Clock:** is_open=true, next_close Di 21.07. 16:00 ET.

**Account Live 09:40 ET (Alpaca /v2/account + latest trades):**
```
Equity:            97.780,68 $   (Live-Kalk aus Cash + Positions-MV)
Cash:              40.026,27 $   (40,93 %)
Portfolio_MV:      57.754,41 $   (59,07 %, 7 Positionen)
Buying_power:     321.784,23 $
Käufe KW30:        1/2           (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Pending Orders:    0
Daily P/L:         -0,006 %      (vs last_equity 97.786,94, Reset bei Open)
Weekly KW30 Tag 2: -0,464 %      (vs Fr-Close 98.236,14)
DD vs ATH:         -2,284 %      (ATH 100.066,47)
SPY Live:          745,67 (+0,474 % vs Mo-Close 742,15)
```

**Positionen Live 09:40 ET — sortiert Puffer ENG→WEIT:**

| Sym    | Live       | Entry      | P/L %   | V1-Stop     | V1-Puffer     | Status |
|--------|------------|------------|---------|-------------|---------------|--------|
| **GS** | 1.073,235  | 1.141,74   | -6,00 % | 1.050,40    | **+2,17 %**   | SICHER, **ERHOLT vs Mo-Close +0,50 %** um +1,67 pp (Fill-Day+4-Fenster AVGO/MU Präzedenz überstanden) |
| **GOOGL**| 349,515   | 368,10     | -5,05 % | 338,65      | **+3,21 %**   | SICHER, aber Blackout-**AKTIVIERUNGSSENSIBEL:** V1_neu 349,70 > Kurs = -0,05 % neg |
| LLY    | 1.145,55   | 1.193,89   | -4,05 % | 1.098,38    | +4,29 %       | SICHER, RSI < 50 Momentum-Watch (XLV) |
| V (NEU)|   357,190  |   357,18   | +0,00 % |   328,60    | +8,70 %       | SICHER, Fill-Day+1 flat (kein Sofort-Drop-Muster wie AVGO/MU/GS) |
| JPM    |   338,870  |   332,78   | +1,83 % |   306,16    | +10,68 %      | SICHER |
| AAPL   |   324,720  |   316,86   | +2,48 % |   291,51    | +11,39 %      | SICHER |
| UNH    |   424,570  |   401,57   | +5,73 % |   369,44    | +14,92 %      | SICHER, beste heute |

**V1-V6-Check alle 7 SICHER (Live-Trade-Preise Alpaca 09:38-09:39 ET):** Kein V1-Break (engste GS +2,17 % erholt), V2-Trail weit vom 52w-Hoch, V3/V4 max UNH +5,73 % (<< +20 % TP-Schwelle), V5/V6 stabil (aus Mo-Close-Analyse: alle 7 EMA50>EMA200, RSI max 64 << 80). **→ Keine Sell-Order platziert.**

**Kandidaten-Scan Slot 2/2 KW30 — Watchlist KO + UPS (K1-K5 Recheck):**

**Alpaca Bars (Mo-Close 20.07. Basis für K1-K3, 284 komplette Bars ohne heutige Di-Session):**

| Sym | Mo-Close | EMA50 | EMA200 | Spread | RSI(14) | Ret_63d | RS vs SPY | K1 | K2 | K3 |
|-----|----------|-------|--------|--------|---------|---------|-----------|----|----|-----|
| KO  | 82,11    | 81,12 | 75,53  | +5,59  | 50,36   | +9,12 % | **+4,33 pp** | ✓ | ✓ | ✓ |
| UPS | 113,16   | 107,59| 100,17 | +7,42  | 56,16   | +8,09 % | **+3,30 pp** | ✓ | ✓ | ✓ |
| SPY | 742,15   | 742,72| 702,94 | +39,78 | 47,88   | +4,79 % | Baseline    | -  | -  | -  |

→ Beide 3/3 K1-K3 wie im Pre-Market-Scan bestätigt.

**K4-Volumen:** Nicht evaluierbar (nur ~10 min in Session, keine repräsentative Extrapolation möglich).

**K5-Recheck Multi-Source Perplexity:**

**KO (Coca-Cola):**
- **Forward P/E:** Yahoo 24-26x | StockAnalysis 23,93 / 25,46 | GuruFocus 23,59 | AlphaSpread TTM P/E 24,1 → **Median ~24, alle < 35** ✓
- **Revenue Growth YoY:** StockAnalysis TTM **+5,1 %** ✗ | GuruFocus 3Y CAGR +6,9 % ✗ | Yahoo full-year +0,6-1,87 % ✗ | **ABER Perplexity Recheck Q1 FY26 MRQ +12,1 %** ✓ (Recheck-Widerspruch)
- **Q2 CY26 Earnings:** **28.07.2026 BMO** bestätigt (StockAnalysis + Business Wire) — **5 HT weg, Standard-Blackout aktivierbar ab Do 23.07. Close** → nur Di+Mi Kauf-Fenster
- **K5-Entscheidung: KONFLIKT** — TTM/Annual ✗ vs MRQ ✓, Multi-Source-Diskrepanz → **REJECT** nach LEVEL-0-Regel "No-Action bei Unsicherheit"
- **Zusatzsignal:** KO Fr 17.07. **-4,58 % Drop** (85,48 Open → 81,565 Close, intraday-Range -5,47 %) unerklärt durch Perplexity — pre-Earnings-Weakness / News-Leak / -Sektor-Rotation möglich

**UPS (United Parcel Service):**
- **Forward P/E:** Yahoo/Zacks 14,23 | StockAnalysis 14,59 | GuruFocus 14,32 | → **Median ~14,4, alle < 35** ✓
- **Revenue Growth YoY:** StockAnalysis TTM **-2,65 %** ✗ (2025 88,66 Mrd vs 2024 91,07 Mrd) | Perplexity Recheck MRQ **-0,3 %** ✗ | Q2 2025 -0,8 % ✗ | **alle Sources negativ** ✗
- **Q2 CY26 Earnings:** **28.07.2026 BMO** bestätigt (StockAnalysis) — **5 HT weg, Standard-Blackout aktivierbar ab Do 23.07. Close**
- **K5-Entscheidung: klar FAIL** — Multi-Source einig < 10 % (sogar negativ) → **REJECT**
- **Zusatzsignal:** UPS Mo 20.07. **-3,88 % Drop** (117,73 Fr-Close → 113,16 Mo-Close, intraday-Low 112,68) unerklärt durch Perplexity — pre-Earnings-Weakness möglich

**GOOGL-Blackout-Sensitivitätscheck Tag -1 (Perplexity Multi-Source):**
- Q2 CY26 Earnings **Mi 22.07.2026 AMC** bestätigt
- V1_neu Blackout = 368,10 × 0,95 = **349,70** vs Live 349,515 = **-0,05 % negativ**
- → Blackout-Tightening würde JETZT einen Sofort-Stop auslösen (vs Pre-Market 08:36 +0,41 % pos, Mo-Close +0,69 % pos)
- Option A Strategie-Lock (V1 = Standard 338,65) weiter aktiv → nicht auto-aktiviert
- **Letzte Chance Owner-Freigabe HEUTE Di + morgen Mi Vormittag** vor Mi-Close-Earnings

**Guardrail-Check alle 8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     -0,006 % Reset bei Open                            [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 2 -0,464 %                                [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,284 %                                           [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,284 %                                           [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,474 % (weit von -5 %)                       [INAKTIV]
6. VIX-Filter (>30):          17,6-18,0 carry-over                               [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi AMC Tag -1 (Option A Owner-Pending, aktivierungssensibel) | KO/UPS 28.07. BMO (>3 HT, aber Kauf-Fenster eng) | [WARN — GOOGL] |
8. Max Käufe KW30:            1/2 (Slot 2/2 offen bis Fr 24.07., aber K5-Blockade Top-Kandidaten) [FREI 1]
```

**Entscheidung Market Open 09:40 Di 21.07.:**
- **Buy-Seite: KEIN Kauf** (KO K5-Konflikt Multi-Source + UPS K5-FAIL Multi-Source einig + beide pre-Q2-Earnings 28.07. + unerklärte 3-5 %-Drops → regelkonform REJECT)
- **Sell-Seite: keine Aktion** (alle 7 V1-V6 SICHER, GS erholt auf +2,17 %)
- **GOOGL Blackout-Owner-Freigabe: PushNotification erneut** (Aktivierungssensitivität erreicht, letzte Chance heute+morgen)
- **Slot 2/2 KW30 bleibt OFFEN** bis Fr 24.07. (aber Kauf-Wahrscheinlichkeit KW30 gering wegen K5-Blockade der Top-Kandidaten)

**Nächste Routine:** Di 21.07. 13:00 ET Midday Stop-Check — GS V1 1.050,40 (+2,17 % erholt), GOOGL V1 338,65 + Blackout-Sensitivität + Owner-Freigabe-Status, LLY RSI < 50 XLV-Watch, KO/UPS-Watchlist bleibt beobachtet aber K5 dauerhaft geblockt.

---

## Pre-Market 08:30 ET — 2026-07-21 (Di, KW30 Tag 2) — Alle 8 Guardrails GRÜN, GS pre-Puffer ~+1,4% (entspannt vs Fr-Close +0,50%), Market-Open-Scan JA

**Alpaca Clock:** is_open=false, next_open Di 21.07. 09:30 ET (in ~55 min).

**Account Pre-Market 08:36 ET (Alpaca /v2/account):**
```
Equity:            97.656,39 $   (vs last_equity 97.786,94 → -0,133 %)         [GRÜN, overnight-Drift]
Cash:              40.026,27 $   (40,99 %)
Portfolio_MV:      57.630,12 $   (59,01 %, 7 Positionen)
Buying_power:     321.469,41 $
Käufe KW30:        1/2           (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Pending Orders:    0
Status:            ACTIVE, trading_blocked=false, PDT=None
```

Konsistenzcheck vs Mo-Close (97.777,22): Δ -120,83 $ = -0,124 % overnight-Repricing durch stale/pre-market Quotes auf Positionen (GS current_price 1.064,88 vs Close 1.055,66 = +0,87 %; GOOGL 351,14 vs 352,11 = -0,28 %; LLY 1.140,13 vs 1.146,38 = -0,55 %). Werte grundsätzlich konsistent — keine Alpaca-vs-Memory-Diskrepanz.

**Positionen aktuell (Alpaca /v2/positions, current_price ist stale/pre-market letzter Trade):**

| Sym    | Cur.Price  | Entry      | P/L %   | V1-Stop     | V1-Puffer     | Status |
|--------|------------|------------|---------|-------------|---------------|--------|
| **GS** | 1.064,88   | 1.141,74   | **-6,73 %** | 1.050,40 | **~+1,38 %**  | pre-Puffer entspannt vs Mo-Close +0,50 % (aber Alpaca-Quote ap=1.108/bp=1.014 SEHR breit → unzuverlässig, Bestätigung erst Open 09:30) |
| **GOOGL**| 351,14   | 368,10     | -4,61 % | 338,65      | ~+3,69 %      | Q2-Blackout Tag -1 (Earnings Mi 22.07. AMC bestätigt via Perplexity — Owner-Pending Blackout-Aktivierung) |
| LLY    | 1.140,13   | 1.193,89   | -4,50 % | 1.098,38    | ~+3,80 %      | (leicht verschlechtert vs Close +4,37 %) |
| V (NEU)|   358,07   |   357,18   | +0,25 % |   328,60    | ~+8,97 %      | Fill-Day+1 (kein Sofort-Drop-Muster) |
| JPM    |   339,00   |   332,78   | +1,87 % |   306,16    | ~+10,73 %     | |
| AAPL   |   325,00   |   316,86   | +2,57 % |   291,51    | ~+11,49 %     | |
| UNH    |   421,06   |   401,57   | +4,85 % |   369,44    | ~+13,97 %     | |

**Guardrail-Check alle 8 GRÜN:**
```
1. Daily Loss Cap (-3 %):     -0,133 % overnight (Reset bei Open)              [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 2 -0,590 % (vs Fr-Close 98.236,14)      [GRÜN]
3. Drawdown-Alarm (-15 %):    -2,409 % vs ATH 100.066,47                       [GRÜN]
4. Drawdown-Stopp (-20 %):    -2,409 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Mo -0,152 % (weit von -5 %)                  [INAKTIV]
6. VIX-Filter (>30):          VIX 17,6-18,0 (Perplexity spot, -5-6 % vs Vt.)   [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Mi 22.07. AMC bestätigt → Blackout aktiv Owner-Pending Option A Strategie-Lock (V1_neu 349,70 < Kurs 351,14 = +0,41 % positiv, kein Sofort-Stop-Risiko) | V Q3 ~28-29.07. AMC (~5-6 HT weg, kein Blackout) | [WARN — GOOGL Owner-Pending] |
8. Max Käufe KW30:            1/2 (V gefüllt, Slot 2/2 offen bis Fr 24.07.)    [FREI 1]
```

**Perplexity Daily Macro Check (Di 21.07.2026):**
- **VIX:** 17,6–18,0 (Vortagesschluss 18,65 → -5-6 %) — GRÜN
- **SPY Pre-Market:** +0,2 bis +0,4 % (aus ES-Futures abgeleitet; Alpaca Live-Quote SPY 744,91 vs Mo-Close 742,15 = **+0,37 %**)
- **10Y Treasury:** 4,25-4,35 % (leicht höher vs Vortag)
- **Makro-Events heute:** KEINE FOMC, KEINE Powell-Rede, KEINE CPI/PCE/NFP. Nur PMI/Regional Fed Surveys + Housing-Daten (sekundär, geringes Marktbewegungspotenzial)
- **Top 3 News:** (1) Q2-Earnings Large-Caps Tech/Consumer prägen Index (2) Anstieg Langfrist-Renditen nach robusten US-Daten → Fed-Cut-Repricing (3) US-China Tech-Restriktionen + US-Haushalt-Blockaden belasten Sentiment
- **Guardrail-Check:** VIX < 30 ✓, SPY Pre-Market > -2 % ✓ (+0,37 %), Crash-Filter INAKTIV → **Kaufscan Market Open ERLAUBT**

**Earnings-Blackout-Check (Perplexity, nächste 3 HT = Di 21.07., Mi 22.07., Do 23.07.):**
- AAPL, GS, JPM, LLY, UNH, V, KO, UPS: **NEIN** (alle bereits berichtet / >3 HT weg)
- **GOOGL: JA Mi 22.07. AMC bestätigt** (Perplexity Multi-Source-Check) → Blackout-Situation heute Tag -1:
  - Option A Strategie-Lock (V1 = Standard 338,65) weiter aktiv, Owner-Freigabe für V1_neu 349,70 pending
  - Kurs 351,14 > V1_neu 349,70 = +0,41 % positiv → Blackout-Tightening würde AKTUELL keinen Sofort-Stop auslösen
  - **Letzte Chance heute Di + Mi Vormittag für Owner-Blackout-Entscheidung vor Mi-Close-Earnings**
- **Aktion:** GOOGL Stop bleibt 338,65 (Option A Strategie-Lock), erneute PushNotification an Owner mit Blackout-Erinnerung

**GS Fill-Day+4 Watch (kritischste Position):**
- Entry 15.07. 1.141,74 → Fill-Day+3 Mo-Close 1.055,66 (-7,53 %) → Pre-Market Di ~1.064,88 (Alpaca Quote unzuverlässig, +0,87 % overnight)
- V1-Puffer pre-Open **~+1,38 %** — deutlich entspannter als Mo-Close +0,50 %, aber Alpaca Quote-Spread bp 1.014,79 / ap 1.108,17 extrem breit (nicht handelbar)
- **Bestätigung erst Market Open 09:30 ET** — bei Break V1 1.050,40 sofort Market-Sell
- Präzedenz-Warnung: AVGO Fill-Day+3 V1-Stop / MU Fill-Day+4 V1-Stop — GS aktuell im Muster-Fenster, Watch bleibt kritisch

**Watchlist Market Open Scan (Slot 2/2 KW30 offen bis Fr 24.07.):**
- **KO 82,11** (XLP, K1-3 3/3 aus Mo-Screener): K4/K5 zwingend Market Open bestätigen (Volume, FwdPE Multi-Source, Q2-Blackout Historik-Check)
- **UPS 113,16** (XLI, K1-3 3/3 aus Mo-Screener): K4/K5 zwingend Market Open bestätigen (Volume, FwdPE Multi-Source, Q2-Blackout Historik-Check)
- **Backup 2/3 (K3-Fail RS negativ):** HON, RTX, CVX, XOM, COP, MMM
- **XLV-Backup Owner-Pending:** ABBV/MRK/JNJ (Sektor-Cap-Deutungs-Frage)
- **Permanent-blockiert:** PANW (K5 FwdPE 42-78), AMD (K5)

**Entscheidung Pre-Market Di 21.07.:**
- **Guardrail-Status:** GRÜN (alle 8)
- **Kauf heute:** Market Open Scan JA — Slot 2/2 verfügbar, Prio KO + UPS (K4/K5 Bestätigung zwingend)
- **GS-Watch:** V1 1.050,40 Sofort-Sell-Bereitschaft bei Break (Puffer pre ~+1,38 %)
- **GOOGL-Blackout:** Owner-Pending, PushNotification-Erinnerung (letzte Chance vor Mi AMC)
- **Nächster Check:** Di 21.07. 09:30 ET Market Open + Kaufsignal-Scan

---

## Market Close 16:02 ET — 2026-07-20 (Mo, KW30 Tag 1) — Alle 7 V1-V6 SICHER, GS Puffer +0,50% RAZOR-THIN, KO+UPS Watchlist Di

**Alpaca Clock:** is_open=false, next_open Di 21.07. 09:30 ET.

**Account Close 16:02 ET (Alpaca /v2/account):**
```
Equity:            97.777,22 $   (vs last_equity 98.236,14 → -0,467 %)         [GRÜN, Cap -3 %]
Cash:              40.026,28 $   (40,94 %)
Portfolio_MV:      57.750,94 $   (59,06 %, 7 Positionen)
Buying_power:     321.807,75 $
Käufe KW30:        1/2           (V gefüllt Mo 20.07., Slot 2/2 offen bis Fr 24.07.)
Pending Orders:    0             (V1-V6 alle 7 SICHER, keine Limit-Order Di)
```

**SPY & Market:**
- SPY IEX Close 742,15 vs Fr-Close 743,28 = **-0,152 %** (Perplexity spot 743,76 intraday, aber Alpaca IEX ist bindend für Daily-Perf-Berechnung)
- **Alpha vs SPY: -0,315 pp NEGATIV** (Portfolio -0,467 % vs SPY -0,152 %)
- Größte Drags: LLY -2,777 % + AAPL -2,067 % + UNH -1,312 % + GS -0,957 %
- Positive Rebounds: GOOGL +1,606 % + V +0,561 %

**V5/V6-Check alle 7 SICHER (Standard-EMA 2/(N+1), Wilder-RSI, 264d Bars):**

| Sym    | Close    | EMA50    | EMA200   | Spread   | RSI    | RS_4w   | RS_63d  | V5     | V6     |
|--------|----------|----------|----------|----------|--------|---------|---------|--------|--------|
| AAPL   |  326,65  |  301,36  |  274,18  |  +27,19  | 64,28  | +10,28% | +16,37% | SAFE   | SAFE   |
| GOOGL  |  352,11  |  358,57  |  316,42  |  +42,14  | 45,82  | -3,68 % | -1,47 % | SAFE   | SAFE   |
| GS     | 1055,66  | 1029,28  |  913,17  | +116,11  | 49,77  | -3,15 % | +9,50 % | SAFE   | SAFE   |
| JPM    |  338,90  |  324,02  |  311,00  |  +13,02  | 57,66  | +4,82 % | +4,72 % | SAFE   | SAFE   |
| LLY    | 1146,38  | 1118,70  |  991,60  | +127,10  | 47,72  | +4,95 % | +19,14% | SAFE   | SAFE   |
| UNH    |  421,85  |  400,00  |  352,94  |  +47,06  | 54,62  | +5,78 % | +25,47% | SAFE   | SAFE   |
| V      |  361,05  |  337,44  |  333,77  |  **+3,67 engste** | 64,29 | +10,95%| +9,32 % | SAFE   | SAFE   |

→ **KEINE V5/V6-Trigger, KEINE Limit-Order für Di 21.07.**

**GS Fill-Day+3 Drop-Muster VOLLBILD (kritischste Position):**
- Entry 15.07. 1.141,74 → Fill-Day+3 Close 1.055,66 = **kumuliert -7,53 %**
- V1-Puffer +0,50 % (5,26 $) = **engste aller Zeiten**, marginal besser als Midday +0,41 %
- Präzedenz: AVGO Fill-Day+3 V1-Stop -8,69 % / MU Fill-Day+4 V1-Stop -10,92 %
- **Pre-Market Di 21.07. 08:30 ET Watch zwingend** — Market-Sell-Bereitschaft bei Break < 1.050,40

**GOOGL Blackout-Konflikt Fortsetzung (Owner-Pending):**
- Q2 22.07.2026 AMC Earnings → nur noch **Di 21.07. + Mi 22.07.** Blackout-Fenster
- V1_neu Blackout = 368,10 × 0,95 = **349,70** vs Standard V1 338,65
- Close 352,11 > V1_neu 349,70 = **+0,69 % positiv** (entspannt vs Fr-Close -0,84 % negativ)
- **Blackout-Tightening würde AKTUELL keinen Sofort-Stop auslösen** → Owner-Freigabe für Aktivierung möglich, aber weiter pending

**Watchlist-Scan Di 21.07. (lokaler Alpaca-Screener über 20 Non-XLK/XLV/XLF/XLC Blue-Chips):**

| Sym  | Sektor | Close   | K1 (EMA50>EMA200) | K2 (RSI 50-70) | K3 (RS_63d>0) | K1-3 |
|------|--------|---------|-------------------|----------------|---------------|------|
| **KO** | XLP | 82,11   | ✓ (Spread +5,22) | ✓ (50,08)     | ✓ (+3,89 %)   | **3/3 LEAD** |
| **UPS**| XLI | 113,16  | ✓ (Spread +6,58) | ✓ (56,00)     | ✓ (+1,78 %)   | **3/3 LEAD** |
| CAT  | XLI | 864,00  | ✓                | ✗ (37,89)     | ✓ (+4,22 %)   | 2/3  |
| HON  | XLI | 226,20  | ✓                | ✓ (51,80)     | ✗ (-7,62 %)   | 2/3  |
| RTX  | XLI | 194,44  | ✓                | ✓ (55,99)     | ✗ (-5,53 %)   | 2/3  |
| GE   | XLI | 341,26  | ✓                | ✗ (43,12)     | ✓ (+7,76 %)   | 2/3  |
| MMM  | XLI | 159,31  | ✓                | ✓ (52,00)     | ✗ (-1,43 %)   | 2/3  |
| XOM  | XLE | 148,40  | ✓                | ✓ (61,15)     | ✗ (-3,19 %)   | 2/3  |
| CVX  | XLE | 189,25  | ✓                | ✓ (65,78)     | ✗ (-1,66 %)   | 2/3  |
| COP  | XLE | 115,69  | ✓                | ✓ (59,50)     | ✗ (-4,83 %)   | 2/3  |

**Slot 2/2 KW30 Prio-Kandidaten Di 21.07.:**
- **Priorität 1:** KO + UPS (kein Sektor-Cap, K4/K5 zwingend Pre-Market — beide Q2 Earnings Ende Juli Historik → **Blackout-Risiko-Check** zwingend, K5 FwdPE-Multi-Source)
- **Priorität 2:** XLV-Trio (ABBV/MRK/JNJ) nur bei Owner-Freigabe Sektor-Cap-Deutung
- **Sperren aktiv:** PANW (K5-Fail permanent, FwdPE 42-78 Multi-Source), AMD (K5-Fail permanent)

**Guardrails Check Close (alle 8 GRÜN):**
```
1. Daily Loss Cap:    -0,467 %                                              [GRÜN]
2. Weekly Loss Cap:   KW30 Tag 1 -0,467 %                                   [GRÜN]
3. Drawdown-Alarm:    -2,288 % vs ATH 100.066,47                            [GRÜN]
4. Drawdown-Stopp:    -2,288 %                                              [GRÜN]
5. Crash-Filter:      SPY -0,152 % (nicht Trigger)                          [INAKTIV]
6. VIX-Filter:        18,28 (carry-over Pre)                                [GRÜN]
7. Earnings-Blackout: GOOGL aktiv (Kurs > V1_neu, kein Sofort-Stop-Risiko)  [WARN — Owner-Pending] |
8. Max Käufe KW30:    1/2 (V gefüllt, Slot 2/2 offen bis Fr 24.07.)         [FREI 1]
```

**ClickUp-Task-Erstellung ERR "Team not authorized"** (dieselbe permanent-Fehler-Klasse wie GS 15.07. HTTP 403 OAuth-023 "Team(s) not authorized") — Fallback PushNotification Prio 3 (negative Perf-Regel) an Owner mit Tagesbilanz-Kernpunkten.

**Nächste Routine:** Di 21.07. 08:30 ET Pre-Market Check — **GS V1 1.050,40 kritisch (+0,50 % engste aller Zeiten)**, GOOGL V1 338,65 + Blackout Owner-Freigabe zwingend vor Do 22.07. AMC, LLY RSI 47,72 Momentum-Watch, KO/UPS K5-Multi-Source-Recheck + Earnings-Blackout-Check für Slot 2/2 KW30.

---

## Market Open 09:41 ET — 2026-07-20 (Mo, KW30 Tag 1) — V-Kauf Slot 1/2 gefüllt, PANW K5-Reject, GS/GOOGL Rebound

**Alpaca Clock:** is_open=true, next_close Mo 20.07. 16:00 ET.

**Account 09:41 ET nach V-Fill (Alpaca /v2/account):**
```
Equity:            98.402,10 $   (+0,169 % vs last_equity 98.236,14)         [GRÜN]
Cash:              40.026,28 $   (40,68 % post V-Kauf)
Portfolio_MV:      58.352,91 $   (59,32 %, 7 Positionen)
Buying_power:     323.557,42 $
Käufe KW30:        1/2           (V gefüllt, Slot 2/2 verfügbar bis Fr 24.07.)
Pending Orders:    0
```

**Watchlist-Scan-Ergebnis Mo 20.07. (5 K1-K3 LEADS aus Fr-Carry gescannt):**

| Sym  | Close Fr | Live 09:38 | K1 EMA-Spread | K2 RSI | K3 RS_63d | K4 Vol Extrap | K5 FwdPE MultiSrc | K5 RevGrowth | Entsch. |
|------|----------|------------|---------------|--------|-----------|---------------|-------------------|--------------|---------|
| **V**    | 358,51 | 356,91 (-0,45 %) | +3,61 ✓ | 62,68 ✓ | +7,82 % ✓ | **157 % Avg20** ✓ | **24,4 / 24,8 / 27,0 (Med ~25)** ✓ | **17 % Q2 FY26** ✓ | **KAUF** |
| PANW | 358,62 | 364,20 (+1,56 %) | +65,24 ✓ | 67,33 ✓ | +108,86 % ✓ | 121 % ✓ | **55,17 / 57,89 / 77,66 (>35 alle)** ✗ | 16 % Q2 FY25 ✓ | **REJECT K5** |
| ABBV | 254,52 | 255,02 (+0,20 %) | +8,66 ✓ | 64,43 ✓ | +15,89 % ✓ | (nicht geprüft) | (nicht geprüft) | (nicht geprüft) | **BACKUP** — XLV-Cap-Owner-Pending |
| MRK  | 127,48 | 127,30 (-0,14 %) | +12,55 ✓ | 57,87 ✓ | +4,45 % ✓ | (nicht geprüft) | (nicht geprüft) | (nicht geprüft) | **BACKUP** — XLV-Cap-Owner-Pending |
| JNJ  | 253,01 | 253,09 (+0,03 %) | +22,04 ✓ | 54,42 ✓ | +1,92 % ✓ | (nicht geprüft) | (nicht geprüft) | (nicht geprüft) | **BACKUP** — XLV-Cap-Owner-Pending |

**V-Kauf ausgeführt (Alpaca Order-ID 85d11ad8-fccc-4c6f-a55c-5cc6695999a2):**
- Limit 360,30 (prev_close 358,51 × 1,005) → Fill 09:41:19 ET @ **357,177778 $ × 27 Sh** in 3 sec
- Investiert 9.643,80 $ = 9,80 % Portfolio (Budget 10 % bei VIX < 25)
- Stops: V1 328,60 (-8 %) | V2 314,32 (-12 %) | TP1 428,62 (+20 %) | TP2 482,20 (+35 %)
- Sektor XLF (JPM+GS+V = 3/3 Positionen, 19,63 % Portfolio, unter 30 % Cap)

**PANW K5-Reject-Analyse (permanent K5-blocked wie AMD 14.07.):**
- FwdPE Range **42-78** aus 4 unabhängigen Quellen (GuruFocus current 55,17 / GuruFocus-Snap 57,89 / StockAnalysis 77,66 / GuruFocus älter 42,10)
- Selbst niedrigste Quelle (42,10) verletzt K5-Cap 35 klar
- Cybersecurity-Sektor-Typik: hohe Wachstums-Multiples permanent > 35 → K5-Block bis Multi-Source-Median klar unter 35 fällt

**XLV-Trio (ABBV/MRK/JNJ) nicht aktiviert:**
- Alle 3 K1-K3 3/3 grün (Fr-Screener bestätigt)
- **XLV-Sektor-Cap-Deutungs-Frage Owner-Pending** (UNH 10.127 + LLY 9.362 = 19.489 $ = 33,39 % investiert / 19,80 % Portfolio)
- Bei ABBV-Kauf ~9-10 % Portfolio → 3. XLV-Position wäre ~29-30 % investiert / ~14 % Portfolio → grenzwertig
- **Warten auf Owner-Freigabe zur Sektor-Cap-Deutung** — heute nicht aktiviert (Strategie-Lock Pflichtregel 3)

**Positionen-V1-Check 09:38 ET (alle 6 alte + V = 7 SICHER):**

| Sym    | Live       | Fr-Close | Chg     | P/L %   | V1-Puffer  | Δ vs Fr-Close |
|--------|------------|----------|---------|---------|------------|---------------|
| **GS** | 1.079,81   | 1.065,22 | +1,37 % | -5,43 % | **+2,80 %**| +1,34 pp (Rebound) |
| **GOOGL**|  356,78  | 346,77   | +2,88 % | -3,08 % | **+5,35 %**| +2,95 pp (Rebound) |
| LLY    | 1.174,47   | 1.179,11 | -0,39 % | -1,63 % | +6,93 %    | -0,05 pp |
| V (NEU)|   357,18   | 358,51   | Fill    | +0,00 % | +8,70 %    | Fill-Day+0 |
| JPM    |   343,37   | 341,10   | +0,67 % | +3,18 % | +12,16 %   | +0,75 pp |
| AAPL   |   331,25   | 333,74   | -0,75 % | +4,54 % | +13,64 %   | -0,85 pp |
| UNH    |   421,45   | 426,09   | -1,08 % | +4,95 % | +14,08 %   | -1,24 pp |

**GS/GOOGL Rebound-Kontext (positiv, aber Watch-Fenster nicht abgeschlossen):**
- GS Puffer +2,80 % vs Fr-Close +1,46 % = **+1,34 pp Rebound**, aber weiter unter 3 % → Fill-Day+3-Muster-Watch fortgesetzt
- GOOGL Puffer +5,35 % vs Fr-Close +2,40 % = **+2,95 pp starker Rebound**, **verlässt <3 %-Kritisch-Zone** (Blackout-Konflikt entspannt: V1_neu 349,70 nun +1,99 % positiv vs Fr-Close -0,84 % negativ)

**GOOGL-Blackout-Konflikt-Update (Fortsetzung Option A):**
- V1_neu Blackout 349,70 vs Kurs 356,78 = **+1,99 % positiv** (Fr-Close war -0,84 % negativ)
- **Sofort-Stop-Risiko entfällt** bei aktueller Live-Notierung
- **Option A Strategie-Lock bleibt aktiv** (Standard V1 338,65), Owner-Freigabe weiter pending für Blackout-Aktivierung ab heute Close
- Blackout endet Di 22.07. Close (letzter Blackout-Tag = Mi 22.07. Open-Handel)

**Guardrails Check nach V-Fill (alle 8 GRÜN):**
```
1. Daily Loss Cap:    +0,169 % (positiv)                                    [GRÜN]
2. Weekly Loss Cap:   KW30 Tag 1 +0,169 %                                   [GRÜN]
3. Drawdown-Alarm:    -1,664 % vs ATH 100.066,47                            [GRÜN]
4. Drawdown-Stopp:    -1,664 %                                              [GRÜN]
5. Crash-Filter:      SPY +0,665 % positiv                                  [INAKTIV]
6. VIX-Filter:        18,28                                                 [GRÜN]
7. Earnings-Blackout: GOOGL aktiv (Kurs > V1_neu, kein Sofort-Stop-Risiko) [WARN — Owner-Pending] |
8. Max Käufe KW30:    1/2 (V gefüllt, Slot 2/2 offen)                      [FREI 1]
```

**Watchlist-Rest für Slot 2/2 (bis Fr 24.07.):**
- **Priorität 1:** ABBV/MRK/JNJ (XLV) — nur bei Owner-Freigabe der Sektor-Cap-Deutung
- **Priorität 2:** Neuer Screener-Run (post-V-Kauf) für alternative Sektoren XLK/XLI/XLP
- **Sperren aktiv:** PANW (K5-Fail permanent), AMD (K5-Fail permanent)

**Nächste Routine:** Mo 20.07. 13:00 ET Midday Stop-Check — V Fill-Day+0-Watch (AVGO/MU-Präzedenz für Fill-Day-Drop-Muster), GS/GOOGL Rebound-Fortsetzung prüfen, alle anderen V1 SICHER.

---

## Pre-Market 08:36 ET — 2026-07-20 (Mo, KW30 Tag 1) — Alle 6 V1 SICHER, GS/GOOGL Pre-Market erholt aber Puffer weiter <3%, VIX 18,28 GRÜN, SPY Pre +0,44%, Chip-Selloff-Sorge XLK-Watch, GOOGL-Blackout weiter Owner-Pending, Kaufscan Open FREIGEGEBEN (Slot 2/2 KW30)

**Alpaca Clock:** is_open=false, next_open Mo 20.07. 09:30 ET.

**Account Pre-Market 08:36 ET (Alpaca /v2/account):**
```
Equity:            98.240,91 $   (vs last_equity 98.236,14 → +0,005 % über Nacht flat)   [GRÜN]
Cash:              49.670,08 $   (50,56 %, unverändert seit GS-Fill Mi 15.07.)
Portfolio_MV:      48.572,91 $   (49,44 %, 6 Positionen)
Buying_power:     334.678,64 $
Käufe KW30:        0/2           (LOCK-Ende, KW30-Reset AKTIV — Slot 2/2 verfügbar)
Pending Orders:    0             (V1-V6 alle 6 SICHER am Fr-Close, keine offenen Orders)
Konsistenz vs portfolio.md Fr-Close 98.216,93 → +0,024 % (nachhandel, unkritisch)
```

**Guardrail-Check (alle 8) Pre-Market Snapshot:**
```
1. Daily Loss Cap (-3 %):     -0,005 % (Pre-Market, quasi-flat)                 [GRÜN]
2. Weekly Loss Cap (-5 %):    KW30 Tag 1 Start → 0,000 %                        [GRÜN — RESET]
3. Drawdown-Alarm (-15 %):    -1,828 % vs ATH 100.066,47                        [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,828 %                                          [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Fr -1,011 % (nicht Trigger)                   [INAKTIV]
6. VIX-Filter (>30):          18,28 (Perplexity spot, alt. 20,95)               [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL Q2 22.07. AMC → Blackout aktiv Mo-Mi        [WARN — Owner-Pending]
8. Max Käufe KW30:            0/2 (Slot 2/2 verfügbar)                          [FREI]
```

**Pre-Market Kurse (Alpaca /v2/positions current_price vs lastday_price = Fr-Close 17.07.) — sortiert nach V1-Puffer ENG→WEIT:**

| Sym    | Pre-Market | Fr-Close | Chg PM   | P/L %    | V1-Stop       | V1-Puffer  | Δ vs Fr-Close-Puffer | Status |
|--------|------------|----------|----------|----------|---------------|------------|----------------------|--------|
| **GS** | 1.070,99   | 1.065,22 | +0,54 %  | -6,20 %  | 1.050,40      | **+1,96 %**| +0,50 pp (Erholung)  | SICHER **KRITISCH** (Fill-Day+3, weiter <3 %) |
| **GOOGL**|  348,32  | 346,77   | +0,45 %  | -5,37 %  | 338,65        | **+2,86 %**| +0,46 pp (Erholung)  | SICHER **KRITISCH** (Blackout-Konflikt aktiv, Owner-Pending) |
| LLY    | 1.175,00   | 1.179,11 | -0,35 %  | -1,58 %  | 1.098,38      | +6,98 %    | -0,32 pp             | SICHER |
| JPM    |   341,50   | 341,10   | +0,12 %  | +2,62 %  |  306,16       | +11,54 %   | +0,13 pp             | SICHER |
| AAPL   |   332,07   | 333,74   | -0,50 %  | +4,80 %  |  291,51       | +13,91 %   | -0,58 pp             | SICHER |
| UNH    |   426,25   | 426,09   | +0,04 %  | +6,15 %  |  369,44       | +15,37 %   | +0,05 pp             | SICHER |

→ **Alle 6 V1 Pre-Market SICHER**. GS/GOOGL zeigen leichte Pre-Market-Erholung (~+0,50 pp Puffer), bleiben aber unter 3 %-Schwelle → **kritischer Watch bei Open + Midday zwingend fortgesetzt**.

**GS Fill-Day+3 Kontext:** Fill 15.07. 1.141,74 → PM 20.07. 1.070,99 = **-6,20 % kumuliert**. Präzedenz-Muster AVGO Fill-Day+3 -8,69 % / MU Fill-Day+4 -10,92 % beide V1 Stop-Auslöser → GS heute im **kritischen 3./4. Handelstag-Fenster**. Ohne Trend-Wende Puffer +1,96 % → 1,96/8 = **24,5 % des V1-Weges bereits verbraucht**.

**GOOGL Blackout-Konflikt (Fortsetzung von Fr-Close, Owner-Pending):**
- V1_neu Blackout = 368,10 × 0,95 = **349,70 (-5 %)** vs Standard V1 338,65 (-8 %)
- Pre-Market-Kurs 348,32 < V1_neu 349,70 = **-0,40 % negativ** (Fr-Close war -0,84 %, leicht entspannt)
- **Standard V1 338,65 bleibt aktiv** (Strategie-Lock Option A, Owner-Freigabe pending vor Open zwingend)

**Perplexity Daily Macro Check (08:35 ET, sonar):**
- **VIX:** 18,28 (spot, alternativ 20,95 andere Quelle — beide GRÜN < 30)
- **SPY Pre-Market:** Alpaca IEX Quote 746,49/746,66 vs Fr-Close 743,28 = **+0,44 %** (positive Eröffnungsindikation)
- **10Y Treasury Yield:** ~4,55 % (letzter Wert 17.07., Perplexity refused Zukunftsdatum → carry-over)
- **Fed/CPI/PPI heute:** kein Ereignis vor Open (Perplexity: „not listed")
- **Top News (24h):**
  1. **Global Selloff Chipmakers** (AI-Valuation-Sorgen) → **XLK-Belastung Fortsetzung** — direkter Watchlist-Impact PANW
  2. S&P 500 auf 1-Wo-Tief, Nasdaq 100 auf 5-Wo-Tief (Fr-Close-Momentum negativ)
  3. VIX-Anstieg-Meldung (12,39 %) — konfliktäre Quelle, aber selbst 20,95 = GRÜN

**Earnings-Blackout-Check offene Positionen (Perplexity, 2 Anfragen):**
- **GOOGL Q2 22.07. AMC** — carry-over aus Fr-Close-Doku (Perplexity refused Zukunftsdatum, aber Portfolio.md-Zustand bindend) → **Blackout aktiv Mo-Mi 20.-22.07.**
- **AAPL 30.07. AMC** — außerhalb 3-HT-Fenster [SICHER]
- **GS, JPM, LLY, UNH:** keine Earnings im Fenster 20.-24.07. bestätigt [SICHER]

**Sektor-Kontext für Kauf-Watchlist KW30:**
- **XLK-Chip-Selloff-Fortsetzung** → **PANW (XLK Cybersecurity) VORSICHT** trotz K1-K3 3/3, K5-Multi-Source-FwdPE zwingend + Sektor-Momentum-Recheck bei Open
- **V (XLF)** unbetroffen von Chip-Sektor → **priorisiert** wenn K5 grün
- ABBV/MRK/JNJ (XLV) als Backup, aber XLV-Sektor-Cap-Deutungs-Frage weiter Owner-Pending

**Entscheidung Pre-Market Mo 20.07.:**
- **Kein Sell-Trigger** (alle V1 Pre SICHER, GS/GOOGL bleiben aber im engen Watch-Fenster für Open)
- **Kaufscan Open 09:30 ET FREIGEGEBEN** (alle 8 Guardrails GRÜN, Slot 2/2 KW30 verfügbar)
- **Priorität Watchlist:** V (Q3 ~28.07. → Kauf-Fenster Mo-Mi vor Blackout 23.07. Close) > PANW (XLK-Belastung erhöht Skepsis, K5-Multi-Source zwingend) > XLV-Backup nur bei Sektor-Cap-Freigabe
- **Owner-Frage weiter offen:** GOOGL-Blackout-Tightening Option A/B/C — heute mit Blackout-Aktivierung akut (Fr-Notification unbeantwortet, PM-Puffer -0,40 % vs V1_neu 349,70)

**Nächste Routine:** Mo 20.07. 09:30 ET Market Open + Kauf-Scan KW30 (V/PANW K5-Multi-Source-Recheck, XLV-Backup nur bei Sektor-Cap-Freigabe; GS/GOOGL V1-Watch zwingend engmaschig).

---

## Market Close 16:02 ET — 2026-07-17 (Fr, KW29 Tag 5) — Tagesbilanz, alle 6 V1-V6 SICHER, GS/GOOGL Puffer <3% kritisch, GOOGL-Blackout-Konflikt Owner-Pending, Alpha +0,70% daily / +1,13% weekly POSITIV, Watchlist KW30 5 K1-K3 LEADS

**Alpaca Clock:** is_open=false, next_open Mo 20.07. 09:30 ET, next_close Mo 20.07. 16:00 ET.

**Account Close 16:02 ET (Alpaca /v2/account):**
```
Equity:            98.216,93 $   (vs last_equity 98.524,71 → Daily -0,3124 %)   [GRÜN, Cap -3 %]
Cash:              49.670,08 $   (50,57 %, unverändert seit GS-Fill Mi 15.07.)
Portfolio_MV:      48.546,85 $   (49,43 %, 6 Positionen)
Buying_power:     334.611,50 $
Käufe KW29:        2/2 LOCK      (LOCK endet Mo 20.07. KW30-Reset)
Pending Orders:    0             (V1-V6 alle 6 SICHER — keine Sell/Limit-Order für Mo 20.07.)
```

**SPY-Tagesperformance (Alpaca IEX Close):** SPY 750,87 → 743,28 = **-1,011 %** Tag.
**SPY-Wochenperformance (Fr 10.07. → Fr 17.07.):** 754,94 → 743,28 = **-1,544 %** Woche.
**Portfolio Weekly (Basis Alpaca-History base_value 98.622,21 asof 10.07.):** 98.216,93 → **-0,411 %**.
**Alpha Tag:** -0,3124 % - (-1,011 %) = **+0,699 %** POSITIV.
**Alpha Woche:** -0,411 % - (-1,544 %) = **+1,133 %** POSITIV (Cash-Puffer 50 % dominiert Alpha-Beitrag).

**Positionen Close 16:02 ET (Alpaca /v2/positions + 304d IEX Bars für V5/V6) — sortiert nach V1-Puffer ENG→WEIT:**

| Sym    | Close     | Chg_today | P/L %    | V1-Stop        | V1-Puffer  | V5 Spread | V6 RSI | V6 RS_4w  | Status |
|--------|-----------|-----------|----------|----------------|------------|-----------|--------|-----------|--------|
| **GS** | 1.065,71  | -2,76 %   | -6,66 %  | 1.050,40 (-8 %)| **+1,46 %**| +127,35   | 51,42  | -3,31 %   | SICHER **KRITISCH** (Fill-Day+2 Drop-Muster VOLLBILD, Präzedenz AVGO/MU) |
| **GOOGL**|  346,76 | -2,32 %   | -5,80 %  | 338,65 (-8 %)  | **+2,40 %**| +46,59    | 42,37  | -5,00 %   | SICHER **KRITISCH** (Fill-Day+8 Follow-Through, XLK-Rotation-Verlierer, Blackout-Konflikt) |
| LLY    | 1.178,57  | +0,85 %   | -1,28 %  | 1.098,38 (-8 %)| +7,30 %    | +132,25   | 54,91  | +5,67 %   | SICHER (Reversal-Fortsetzung Tag 3, XLV +2,22 % Rückenwind) |
| JPM    |   341,10  | -0,55 %   | +2,50 %  |  306,16 (-8 %) | +11,41 %   | +16,11    | 60,21  | +1,95 %   | SICHER (Post-Q2-Give-back Tag 4) |
| AAPL   |   333,75  | +0,13 %   | +5,33 %  |  291,51 (-8 %) | +14,49 %   | +29,62    | 72,25  | +12,42 %  | SICHER (XLK-Rebell +2,37 % vs Sektor -2,24 %) |
| UNH    |   426,06  | +0,60 %   | +6,10 %  |  369,44 ✓Reset | +15,32 %   | +48,93    | 57,87  | +6,32 %   | SICHER (Post-Q2-Konsolidierung stabil, XLV-Rückenwind) |

→ **Alle 6 V1-V6 SICHER** (kein Stop getroffen). GS/GOOGL bleiben mit <3 % Puffer im **kritischen Watch-Fenster** für Mo 20.07. Pre-Market.

**GS Fill-Day+2 Kumulierung (Fill 15.07. → Close 17.07.):**
- Fill 09:41 15.07.: 1.141,74 → Fr Close 17.07.: 1.065,71 = **-6,66 % in 3 HT**
- Puffer-Verlauf: Fill +8,57 % → Mi-Close +4,10 % → Do-Open +7,29 % → Do-Close +4,29 % → Fr-Open +1,26 % → Fr-Midday +2,82 % → **Fr-Close +1,46 % ENGSTE**
- Präzedenz-Vergleich: AVGO Fill-Day+3 -8,69 % V1-Stop, MU Fill-Day+4 -10,92 % V1-Stop → GS Fill-Day+2 -6,66 % noch VOR V1-Break
- Mo 20.07. Pre-Market: Break unter 1.050,40 → **V1 Market-Sell sofort** (regelkonform, kein Ermessen)

**GOOGL Nachmittags-Kollaps-Fortsetzung Do → Fr:**
- Do Midday 371,37 → Do Close 354,87 = -4,44 % Nachmittag Do
- Do Close 354,87 → Fr Close 346,76 = -2,32 % Fr (kumuliert Do-Fr -6,63 %)
- Fill-Preis 368,10 → Fr Close 346,76 = **-5,80 % Fill-Day+8**
- V1 338,65 Puffer +2,40 %, Break unter → V1 Market-Sell sofort
- V6 Teil-Bedingung erfüllt: RS_4w -5,00 % negativ (verschärft von Do -5,40 %), aber RSI 42,37 <<80

**GOOGL-Blackout-Konflikt-Regel-Entscheidung (WICHTIG — Owner-Freigabe pending):**
- Q2-Release-Termin: 22.07. AMC (bestätigt aus Do 16.07. Perplexity-Check)
- 3 HT vor Earnings → Blackout-Aktivierung 17.07. Close (heute) — Fr 17. + Mo 20. + Di 21. = 3 HT, Blackout endet Di 21. Close
- V1_neu Blackout = 368,10 × 0,95 = **349,70** (-5 %) vs Standard V1 338,65 (-8 %)
- Kurs Close 346,76 < V1_neu 349,70 = **-0,84 % negativ** → Blackout-Tightening würde Sofort-Stop auslösen bei Aktivierung
- **Optionen:**
  - **Option A (Strategie-Lock, GEWÄHLT):** Standard V1 338,65 BLEIBT AKTIV, Blackout-Tightening NICHT aktiviert (kein Sofort-Stop bei bereits-unterschrittenem V1_neu ohne Owner-Freigabe). Begründung: CLAUDE.md Pflicht-Regel 3 „Strategie-Lock — Niemals von memory/strategy.md abweichen. Bei Konflikt: nicht handeln."
  - **Option B (Rule-strict, VERWORFEN):** V1_neu 349,70 aktivieren + Limit-Sell Mo 20.07. Open bei Market → Sofort-Stop Fill-Preis wahrscheinlich um 344-346 (mid-close-level)
- **Owner-Freigabe erforderlich** vor Mo 20.07. Open — PushNotification Prio 2 mit expliziter Optionsauswahl
- **Fallback Mo Open ohne Owner-Freigabe:** Option A gilt (Standard V1 338,65) — Position bleibt offen sofern V1 nicht getroffen

**Weekly Loss Cap Check KW29 Final:**
- Basis Fr-Close 10.07.: 98.622,21 $ (Alpaca-History base_value asof 2026-07-10)
- Fr-Close 17.07.: 98.216,93 $
- Weekly P/L: **-0,411 %**
- Cap -5 % → Puffer +4,589 % → **KEIN Weekly-Cap-Auslöser** → keine Cancel-Aktion
- Käufe KW29 ohnehin 2/2 LOCK (AAPL Mo + GS Mi) → Reset Mo 20.07. KW30

**Watchlist Mo 20.07. + KW30-Slot 2/2 (LOCK-Ende Mo 20.07., 25 Symbole gescannt):**

**5 K1-K3 LEADS 3/3:**
1. **V (Visa) 358,51** — XLF (Financials/Payment)
   - K1 EMA-Spread +4,13 (marginal ✓)
   - K2 RSI 62,68 ✓
   - K3 RS_63d +7,82 % vs SPY ✓
   - Kauf-Fenster: **Mo-Mi 20.-22.07.** (Q3-Earnings ~28.07. AMC → Blackout ab 23.07. Close aktivierbar)
   - Sektor-Cap: XLF-Position JPM = 1 Position, V wäre 2. → unkritisch (<30 %)
   - K5-Zwingend Mo Pre-Market: Multi-Source-FwdPE-Recheck (Konsens ~25-28 aus Do)
2. **PANW (Palo Alto Networks) 358,62** — XLK (Cybersecurity)
   - K1 EMA-Spread +64,20 ✓
   - K2 RSI 67,33 ✓
   - K3 RS_63d **+108,86 % vs SPY #1** ✓
   - Sektor-Cap: XLK-Position AAPL + GOOGL = 2 Positionen, PANW wäre 3. → Regel-Check (max 3 Positionen/Sektor erfüllt)
   - **K5-Zwingend Mo Pre-Market:** Multi-Source-FwdPE-Recheck (Cybersecurity typisch > 35 wie AMD-Reject-Analogie 14.07.)
3. **ABBV 254,52** — XLV (Health Care)
   - K1 EMA-Spread +14,42 ✓
   - K2 RSI 64,43 ✓
   - K3 RS_63d +15,89 % ✓
   - **Sektor-Cap-Risiko:** UNH (10.222 $) + LLY (9.433 $) = 19.655 $ XLV bereits, ABBV = 3. Position (max 3/Sektor erfüllt), aber Sektor-Gewicht max 30 % → ABBV mit ~9-10 % Kaufwert würde XLV auf ~30 % investiert bringen → **Grenze**
   - Earnings-Blackout Ende Juli — Check zwingend
4. **MRK 127,48** — XLV analog, RSI 57,87, RS +4,45 % — Sektor-Cap-Risiko wie ABBV
5. **JNJ 253,01** — XLV analog, RSI 54,42, RS +1,92 % — Sektor-Cap-Risiko wie ABBV

**Priorisierung Mo:** V (XLF, kein Cap-Risiko) + PANW (XLK, K3 dominant #1) → Slot 1 KW30. XLV-Kandidaten nur wenn V/PANW K5 fail.

**Rejects (K1-K3 <3/3):**
- NVDA/AMZN/META/XOM/CVX: K3-Fail (RS negativ trotz K1/K2 grün)
- AMD: K5-blocked (Multi-Source FwdPE > 35 permanent Di 14.07.)
- CAT/AMAT/MU/BAC/MS: K2-Fail (RSI außerhalb 50-70)
- COST/WMT/PG/ABT/HD/BA: K1-Fail oder Kombination

**Perplexity Sektor-Report Fr 17.07. Close (Sonar-Modell):**
- XLK **-2,24 %** (Semiconductor-Chaos NVDA/AMD/INTC, AI-Überhitzung)
- XLP **+2,80 %** (Defensiv-Rotation)
- XLV **+2,22 %** (UNH-Q2-Beat, MRK-Produkte)
- XLE **+0,92 %** (Iran-Risiken → Öl fest)
- XLI **+0,05 %** (nahezu flach)
- **Interpretation:** Rotation raus aus Growth/Tech → in Defensiv-Sektoren. Bestätigt GOOGL/AAPL Rotation-Verlierer-These und UNH/LLY-Rückenwind.

**Guardrail-Check nach Close (alle 8) — Wochenschluss KW29:**
```
1. Daily Loss Cap (-3 %):     -0,312 %                                    [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,411 % (KW29 Tag 5 Final)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,848 % vs ATH 100.066,47                  [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,848 %                                    [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -1,011 %                                [INAKTIV]
6. VIX-Filter (>30):          ~15-17 (Perplexity Rotation-Bericht)        [GRÜN]
7. Earnings-Blackout (3 HT):  **GOOGL Blackout-Konflikt Owner-Pending**   [WARN]
8. Max Käufe KW29:            2/2 LOCK → Reset Mo 20.07. KW30            [LOCK-ENDE]
```

**Entscheidungs-Matrix Close:**
- Sell-Trigger: **NEIN** (V1-V6 alle 6 SICHER, kein Signal ausgelöst)
- Limit-Order für Mo: **NEIN** (V5/V6 alle SICHER)
- Weekly-Cap-Aktion: **NEIN** (-0,411 % weit von -5 %)
- Blackout-Aktivierung GOOGL: **NEIN** (Option A Strategie-Lock, Owner-Freigabe pending)
- Alert-Prio: **2 (Wichtig)** — GS/GOOGL Puffer <3 % + GOOGL Blackout-Owner-Entscheidung
- Nächster Check: Mo 20.07. 08:30 ET Pre-Market — GS/GOOGL V1-Watch zwingend, K5-Recheck V/PANW

---

## Market Open 09:37 ET — 2026-07-17 (Fr, KW29 Tag 5) — Alle 6 V1 SICHER, GS+GOOGL Puffer <2% KRITISCH, kein Kauf-Scan LOCK

**Alpaca Clock:** is_open=true, next_close 17.07. 16:00 ET, next_open Mo 20.07. 09:30 ET.

**Account Live 09:37 ET (Alpaca /v2/account):**
```
Equity:            98.252,31 $   (vs last_equity 98.524,71 → -0,276 %)   [GRÜN, Cap -3 %]
Cash:              49.670,08 $   (50,55 %, unverändert seit GS-Fill Mi 15.07.)
Portfolio_MV:      48.582,03 $   (49,45 %, 6 Positionen)
Buying_power:     334.710,57 $
Käufe KW29:        2/2 LOCK      (AAPL Mo + GS Mi gefüllt, bis Mo 20.07. KW30) [LOCK]
Pending Orders:    0             (V1 nicht getroffen, kein Sell-Trigger; kein Kauf-Scan LOCK)
```

**Delta zu Pre-Market 08:35 ET:** Equity 98.288,46 → 98.252,31 = **-0,037 % Pre→Open** (weitere Schwäche in ersten 7 Minuten Handel).

**Positionen Live 09:37 ET (Alpaca /v2/positions) — sortiert nach V1-Puffer ENG→WEIT:**

| Sym    | Curr      | Chg_today | P/L %    | V1-Stop        | V1-Puffer  | Status |
|--------|-----------|-----------|----------|----------------|------------|--------|
| **GS** | 1.063,635 | **-2,905%**| **-6,84%**| 1.050,40 (-8 %)| **+1,26 %**| **KRITISCH** (Fill-Day+2 Drop-Muster VOLLBILD, Puffer 2,82% Pre→1,26% Open) |
| **GOOGL**|  344,240| **-2,883%**| **-6,48%**|  338,65 (-8 %) | **+1,65 %**| **KRITISCH** (Follow-Through Do-Nachmittags-Kollaps, Blackout-Konflikt Close) |
| LLY    | 1.177,610 | +0,722 %  | -1,36 %  | 1.098,38 (-8 %)| +7,21 %    | SICHER (Reversal-Fortsetzung Tag 3) |
| JPM    |   336,930 | -1,813 %  | +1,25 %  |  306,16 (-8 %) | +10,05 %   | SICHER (Post-Q2-Give-back Tag 4) |
| AAPL   |   334,085 | +0,248 %  | +5,44 %  |  291,51 (-8 %) | +14,60 %   | SICHER (Fill-Day+4 stabil, XLK-Rebell) |
| UNH    |   430,600 | +1,705 %  | +7,23 %  |  369,44 ✓Reset | +16,56 %   | SICHER (Post-Q2 Konsolidierung stabil) |

→ **Alle 6 V1 SICHER** (V1 nicht getroffen), aber GS/GOOGL Puffer <2 % [WARNUNG DRAMATISCH VERSCHÄRFT vs Pre-Market <5 %].

**GS-Puffer-Verlauf (Fill 15.07. bis Fr 17.07. Open):**
- Fill 09:41:18 ET: 1.141,74 → Live-Hoch 1.151,65 → V1 1.050,40 = +8,57 % Puffer Fill
- Do 09:37 Open: 1.116,84 chg -2,18 % → Puffer +7,29 % (Fill-Day+1 Drop-Start)
- Do 13:07 Midday: 1.102,15 chg -4,34 % → Puffer +4,93 %
- Do 16:02 Close: 1.095,46 chg -4,91 % → Puffer +4,29 %
- Fr 08:35 Pre: 1.079,98 chg -1,41 % (kumuliert -5,41 %) → Puffer +2,82 %
- **Fr 09:37 Open: 1.063,635 chg -2,905 % (kumuliert -6,84 %) → Puffer +1,26 % ENGSTE**
- Muster-Präzedenz: AVGO Fill-Day+3 -8,69 % V1 / MU Fill-Day+4 -10,92 % V1
- **Break unter 1.050,40 → V1 Market-Sell sofort (regelkonform, kein Ermessen).**

**GOOGL-Puffer-Verlauf (Fill 07.07. bis Fr 17.07. Open):**
- Fill 07.07.: 368,10 → V1 338,65 = +8,72 % Puffer Fill
- Fill-Day+7 Mi 15.07.: 366,04 (leicht negativ intraday) → Puffer +8,10 %
- Do 16.07. Close: 354,87 chg -4,33 % **Nachmittags-Kollaps** von Midday 371,37 → Puffer +4,79 %
- Fr 08:35 Pre: 346,76 chg -2,17 % → Puffer +2,39 %
- **Fr 09:37 Open: 344,240 chg -2,883 % (kumuliert -6,48 %) → Puffer +1,65 %**
- Blackout Q2 22.07. AMC = 3 HT → Aktivierung Close heute → V1_neu 349,70

**GOOGL-Blackout-Konflikt Close verschärft:**
- V1_neu 349,70 (-5 % vom Entry 368,10) > Kurs Live 344,24 = **-1,56 % negativ**
- Regel-Entscheidung Close-Routine:
  - **Option A (Strategie-Lock):** Standard-V1 338,65 beibehalten wenn Kurs < V1_neu (keine Regel-Abweichung ohne Owner-Freigabe, aber Blackout-Tightening ausgesetzt)
  - **Option B (Rule-strict):** V1_neu 349,70 aktivieren → Kurs < V1_neu → Sofort-Stop im Close-Bar
- **Entscheidung Open: Dokumentation + Alert Prio 2**, endgültige Auflösung in Close-Routine

**Kandidaten-Scan Schritt 4 — ÜBERSPRUNGEN:** Käufe KW29 2/2 LOCK bis Mo 20.07. KW30. Perplexity Sektor-Check nicht ausgeführt (regelkonform: kein Buying während LOCK). Watchlist V/PANW/ABBV/MRK für KW30-Slot-Vorbereitung bleibt aus Close 16.07. dokumentiert.

**Guardrail-Check nach Open (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,276 %                                    [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,375 % (KW29 Tag 5)                       [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,813 % vs ATH 100.066,47                  [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,813 %                                    [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Pre -0,886 %                            [INAKTIV]
6. VIX-Filter (>30):          ~17 (Pre 17,96, Close Do 16,73)             [GRÜN]
7. Earnings-Blackout (3 HT):  GOOGL ab HEUTE Close aktivierbar            [ÜBERGANG]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30                 [LOCK]
```

**Entscheidungs-Matrix Open:**
- Sell-Trigger: **NEIN** (V1 nicht getroffen bei GS/GOOGL, alle V1-V6 SICHER)
- Kauf-Scan: **NEIN** (LOCK 2/2)
- Alert-Prio: **2 (Wichtig)** — GS/GOOGL Puffer <2 % + GOOGL-Blackout-Konflikt-Vorwarnung
- Nächster Check: Midday 13:00 ET (Fr 17.07. KW29 Tag 5) — GS/GOOGL V1-Watch zwingend

**Datenqualität:**
- Alpaca /v2/account + /v2/positions Live 09:37 ET erfolgreich, alle 6 Positionen mit chg_today/plpc/current_price
- Alpaca /v2/clock is_open=true bestätigt Handelstag aktiv
- SPY Live-Preis nicht separat abgerufen (Pre-Market -0,886 % als Referenz beibehalten)

> **Entscheidung Open 09:37 Fr 17.07.:** **Kein Handel** (V1 alle SICHER, LOCK 2/2). **GS +1,26 % und GOOGL +1,65 % KRITISCH ENG** — Muster-Präzedenz AVGO/MU legt Fill-Day+2/+3 V1-Trigger nahe. **GOOGL-Blackout-Konflikt** bleibt zur Close-Routine offen. Alle 8 Guardrails GRÜN. PushNotification Prio 2 an Owner.
> **Nächste Routine:** Fr 17.07. 13:00 ET Midday Stop-Check (GS/GOOGL V1-Watch, Puffer-Verlauf-Tracking).

---

## Pre-Market 08:35 ET — 2026-07-17 (Fr, KW29 Tag 5) — GS/GOOGL Puffer KRITISCH <5%, GOOGL-Blackout-Konflikt bei Close, alle Guardrails GRÜN, Käufe LOCK

**Alpaca Clock:** is_open=false, next_open Fr 17.07. 09:30 ET, next_close 16:00 ET.

**Account Live 08:35 ET (Alpaca /v2/account):**
```
Equity:            98.288,46 $   (vs last_equity 98.524,71 → -0,240 %)   [GRÜN, Cap -3 %]
Cash:              49.670,08 $   (50,53 %, unverändert seit GS-Fill Mi 15.07.)
Portfolio_MV:      48.618,82 $   (49,47 %, 6 Positionen)
Buying_power:     334.811,79 $
Käufe KW29:        2/2 LOCK      (AAPL Mo + GS Mi gefüllt, bis Mo 20.07. KW30) [LOCK]
Pending Orders:    0             (keine offenen, kein neuer Kauf-Scan)
```

**Konsistenz-Check:** Cash 49.670,08 unverändert seit GS-Fill (Memory ✓). Equity Pre-Market Delta zu Do-Close 98.480,38 → 98.288,46 = **-0,195 %** (leichte Pre-Market-Schwäche, konsistent mit GOOGL/GS Follow-Through).

**Positionen Live 08:35 ET (Alpaca /v2/positions):**
| Sym    | Curr      | Chg_today | P/L %    | V1-Stop        | V1-Puffer  | Status |
|--------|-----------|-----------|----------|----------------|------------|--------|
| AAPL   |   333,08  | -0,05 %   | +5,12 %  | 291,51 (-8 %)  | +14,26 %   | SICHER (stabil nach Do-Rebell) |
| UNH    |   425,79  | +0,57 %   | +6,03 %  | 369,44 (-8 %)  | +15,25 %   | SICHER (Reset stabil, kein Rally-Give-back-2) |
| JPM    |   342,50  | -0,19 %   | +2,92 %  | 306,16 (-8 %)  | +11,87 %   | SICHER (Konsolidierung) |
| LLY    | 1.173,90  | +0,40 %   | -1,67 %  | 1.098,38 (-8 %)| +6,88 %    | SICHER (Reversal-Fortsetzung) |
| **GOOGL**|  346,76 | **-2,17 %**| -5,80 % | 338,65 (-8 %)  | **+2,39 %**| **KRITISCH** (Fill-Day+8 Nachmittags-Kollaps setzt sich fort, Blackout-Konflikt Close!) |
| **GS** | 1.079,98  | **-1,41 %**| -5,41 % | 1.050,40 (-8 %)| **+2,82 %**| **KRITISCH** (Fill-Day+2 Drop-Muster-Fortsetzung wie AVGO/MU) |

→ **Alle 6 V1-V6 SICHER** (V1 nicht getroffen), aber GS und GOOGL Puffer <5 % [WARNUNG].

**SPY-Ground-Truth Pre-Market:** Alpaca IEX SPY Latest-Bar (08:35 ET, 200 Sh) = **744,22** vs Do-Close 750,87 = **-0,886 %**. Alpha Pre-Market = -0,240 % − (-0,886 %) = **+0,646 % POSITIV** (Portfolio läuft besser als SPY dank UNH/LLY-Rebound). Aber: IEX-Pre-Market-Volumen minimal, Bar nur indikativ.

**Perplexity Daily Macro Check — Zukunftsdatum-Refusal (Standard):**
- VIX: Close 16.07. **16,73**, aktuell ~17,96 Pre-Market (im Konfidenz-Range der letzten Tage 15-18) [GRÜN, < 30]
- SPY Premarket: nicht verfügbar → Alpaca-Fallback -0,886 % (siehe oben)
- 10Y Treasury Yield: nicht verfügbar
- Makro-Events heute: nicht verfügbar (Fr 17.07. — potenziell Retail Sales, Consumer Sentiment Uni Michigan Fr-Standard)
- Top News: nicht verfügbar

**Guardrail-Check nach Research (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,240 %                                        [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,338 % (KW29 Tag 5)                           [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,777 % vs ATH 100.066,47                      [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,777 %                                        [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY gestern -0,517 %                            [INAKTIV]
6. VIX-Filter (>30):          16,73 / 17,96 Pre-Market                        [GRÜN]
7. Earnings-Blackout (3 HT):  UNH beendet, GOOGL ab HEUTE Close aktivierbar   [ÜBERGANG]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30                     [LOCK]
```

**Earnings-Blackout-Check (Perplexity vs Memory carry-over):**
- Perplexity behauptet "keine Overlap 17.-24.07." — **falsch für GOOGL** (Q2 22.07.2026 AMC bereits in Memory bestätigt)
- **GOOGL Q2 22.07. AMC** = 3 HT ab heute → **3-HT-Blackout aktivierbar ab HEUTE Close** (Fr 17.07. Close-Routine ZWINGEND)
- AAPL 30.07. AMC (>2 HT weg, kein Blackout), JPM/UNH bereits Q2 released, LLY 05.08. BMO (>2 Wo weg), GS Q3 ~Mitte Oktober (>60 HT weg)
- Nur GOOGL relevant für heutige Blackout-Aktivierung

**GOOGL-Blackout-Konflikt bei Close (kritisch dokumentiert):**
- Standard-V1 338,65 aktiv Pre-Market: Puffer +2,39 % (aktueller Kurs 346,76)
- Blackout-Tightening geplant Close: V1_neu = 368,10 × 0,95 = **349,70**
- Falls Close bei ~346,76 (Pre-Market-Niveau): 346,76 < 349,70 → **V1_neu UNTER Wasser → Sofort-Stop im Moment der Aktivierung**
- Regel-Auslegung: Blackout-Tightening greift nur, wenn Kurs > V1_neu bleibt. Bei Kurs < V1_neu ist Regel-Konflikt: entweder Tightening aussetzen und -8 % beibehalten (338,65) ODER Rule-strict Sofort-Stop im Close-Bar
- **Entscheidung Pre-Market: nur DOKUMENTIEREN + ClickUp-Alert Prio 2 (Wichtig).** Endgültige Regel-Entscheidung in Close-Routine, wenn Kurs bekannt.
- Best-Case: GOOGL bis Close über 349,70 zurück → Blackout-Tightening greift regelkonform
- Worst-Case: GOOGL bleibt < 349,70 → Konflikt-Auflösung durch Strategie-Lock (keine Regel-Abweichung ohne Owner-Freigabe)

**GS Fill-Day+2 Drop-Muster (VOLLBILD-Fortsetzung):**
- Fill-Preis 15.07. 1.141,74 → Do-Close 1.095,46 (-4,05 %) → Fr Pre-Market 1.079,98 (-5,41 % kumuliert)
- V1 1.050,40 bei 1.079,98 = +2,82 % Puffer (Verlauf: Fill Open +7,29 % → Do-Midday +4,93 % → Do-Close +4,29 % → Fr-Pre +2,82 %)
- Muster-Analogie: AVGO Fill-Day+3 -8,69 % V1-Stop, MU Fill-Day+4 -10,92 % V1-Stop → GS Fill-Day+2 aktuell -5,41 %, kritisches Fenster
- **Pre-Market-Alert erforderlich**, aber kein Sofort-Handel (Regel-strict: V1 nicht getroffen)

**Pre-Market-Entscheidungs-Matrix:**
- Kauf-Scan heute: **NEIN** (Slot LOCK 2/2 bis Mo 20.07.)
- Neuer Sell-Trigger: **NEIN** (V1 nicht getroffen, keine V2/V3/V4/V5/V6)
- ClickUp-Alert-Prio: **2 (Wichtig)** wegen 2 Positionen mit Puffer <5 % + GOOGL-Blackout-Konflikt-Vorwarnung
- Nächster Check: Market Open 09:37 ET (Fr 17.07. KW29 Tag 5)

**Datenqualität:**
- Alpaca /v2/account + /v2/positions + /v2/clock Pre-Market Fr erfolgreich
- Alpaca /v2/stocks/bars/latest SPY IEX = nur 200-Sh Pre-Market-Bar (indikativ)
- Perplexity Daily-Macro + Earnings-Query beide "Zukunftsdatum-Refusal" (Standard-Muster seit KW28)
- Memory carry-over als primäre Quelle für Earnings-Daten (bewährt seit LLY/UNH/GS-Blackouts)

> **Entscheidung Pre-Market 17.07.:** **Kein Kauf-Scan** (LOCK), **keine Sofort-Aktion** (alle V1 SICHER). **GS 2,82 % und GOOGL 2,39 % KRITISCH** (Puffer <5 %). **GOOGL-Blackout-Konflikt Close** (V1_neu 349,70 vs Kurs 346,76 = -0,85 % negativ) — Regel-Entscheidung in Close-Routine. Alle 8 Guardrails GRÜN, aber Sub-Status GELB wegen 2 Positionen mit Puffer <5 %. ClickUp-Alert Prio 2.
> **Nächste Routine:** Fr 17.07. 09:30 ET Market Open (Fokus: GS/GOOGL V1-Watch, kein Kauf-Scan wegen LOCK).

---

## Market Close 16:02 ET — 2026-07-16 (Do, KW29 Tag 4) — Tagesbilanz, alle V1-V6 SICHER, GOOGL/GS Nachmittags-Drop, Alpha -0,030 % NEUTRAL

**Alpaca Clock:** is_open=false, next_open Fr 17.07. 09:30 ET, next_close 16:00 ET.

**Account Close 16:02 ET (Alpaca /v2/account):**
```
Equity:            98.480,38 $   (vs last_equity 99.021,31 → -0,546 %)  [GRÜN, Cap -3 %]
Cash:              49.670,08 $   (50,44 %, unverändert seit GS-Fill Mi 15.07.)
Portfolio_MV:      48.810,30 $   (49,56 %, 6 Positionen)
Buying_power:     335.349,16 $
Käufe KW29:        2/2 LOCK      (bis Mo 20.07. KW30) [LOCK]
Pending Orders:    0             (V5/V6 alle 6 SICHER, keine Limit für Fr)
```

**SPY-Ground-Truth:** Alpaca IEX SPY 754,77 → **750,87** = **-0,517 %**. Perplexity Daily-Query "Zukunftsdatum"-Refusal → Alpaca-Ground-Truth als primäre Quelle. Alpha vs SPY = -0,546 % − (-0,517 %) = **-0,030 %** [NEUTRAL — Portfolio-Schwäche lief parallel zu SPY-Schwäche, keine signifikante Alpha-Generierung].

**Positionen Close 16:02 ET (Alpaca IEX 262d Bars, EMA/RSI Wilder):**
| Sym    | Close     | P/L     | Chg_today | V1-Puffer  | EMA-Spread | RSI(14) | RS_4w   | Status |
|--------|-----------|---------|-----------|------------|------------|---------|---------|--------|
| AAPL   |   332,81  | +5,04 % | +1,62 %   | +14,17 %   | +26,20     | 72,02   | +11,05 %| **Tages-Sieger**, RSI 72,02 höchste, V2 auf 294,49 trailt |
| UNH    |   421,14  | +4,87 % | +0,63 %   | +13,99 %   | +49,10     | 56,53   | +3,46 % | Post-Rally-Give-back von TH 460,95 = -8,64 %, V2 auf 405,64 trailt |
| JPM    |   343,15  | +3,12 % | -1,08 %   | +12,08 %   | +13,97     | 63,11   | +3,78 % | Give-back Post-Q2 Tag 3, V2 auf 306,97 trailt |
| LLY    | 1.170,50  | -1,96 % | +1,20 %   | +6,57 %    | +128,69    | 53,18   | +3,94 % | Reversal-Fortsetzung, XLV-Rebound |
| GOOGL  |   354,87  | -3,59 % | -4,33 %   | +4,79 %    | +43,78     | 46,25   | -5,40 % | **Nachmittags-Kollaps** von Midday 371,37, Blackout-Tightening Fr Close |
| **GS** | 1.095,46  | -4,05 % | **-4,91 %**| **+4,29 %**| +121,35   | 56,71   | +0,23 % | **Fill-Day+1 Drop VOLLBILD**, ENGSTE V1 |

→ **Alle 6 V1-V6 SICHER.** GS engste +4,29 %, dann GOOGL +4,79 %.

**GOOGL Nachmittags-Kollaps — dokumentiert:**
- Midday 13:07 ET: 371,37 (chg +0,12 % stabil) → Close 16:02 ET: 354,87 (chg -4,33 %) = **-4,44 % Nachmittag**
- Intraday-Range Alpaca IEX: H 375,18 → L 352,365 → C 354,87 = -6,08 % Intraday-Absturz
- Ursache-Hypothese: Late-Session-Rotation-Aus-XLC oder News-Trigger; Perplexity ohne belastbare Nachrichten
- V1 338,65 bei 354,87 = +4,79 % Puffer (verschlechtert von Midday +9,66 %)
- **Blackout-Vorbereitung Fr Close ZWINGEND:** V1-Tightening auf **349,70** (368,10×0,95 = -5 %) statt 338,65 (Q2 22.07. AMC → 3-HT-Blackout ab Fr 17.07. Close aktivierbar)

**GS Fill-Day+1 Drop-Muster VOLLBILD:**
- Close chg -4,91 % (Open war -2,18 %, Midday war -4,34 %, Close verschärft)
- Muster-Analogie: AVGO Fill-Day+1 -5,77 %, MU Fill-Day+0 -5,26 %, GS Fill-Day+1 -4,91 % = **Muster bestätigt**
- V1 1.050,40 bei 1.095,46 = +4,29 % Puffer (Verlauf: Fill-Preis 1.141,74 → Puffer Open +7,29 % → Midday +4,93 % → Close **+4,29 % ENGSTE**)
- Pre-Market Fr 08:30 ET **kritischer Watch**, Break unter 1.050,40 = Market-Sell sofort
- Muster-Präzedenz zeigt: Fill-Day+2/+3 sind kritisch (AVGO Stop-Loss Fill-Day+3, MU Fill-Day+4)

**UNH Post-Q2-Rally Pump-and-Dump vollständig materialisiert:**
- Pre-Market +6,80 % → Open 452,73 (chg +7,94 %) → Tageshoch 460,95 (chg +10,17 %) → Close 421,14 (chg +0,63 %)
- Gesamter Rally-Give-back innerhalb eines Tages: **-8,64 % vs H, -6,98 % vs Open**
- P/L bleibt aber +4,87 % (fast der gesamte Positions-Beitrag ~+470 $ absorbiert)
- V1-Reset 369,44 (-8 %) unverändert nach Blackout-Ende — komfortabel bei +13,99 % Puffer
- V2-Trail-Update auf **405,64** (460,95×0,88, vorher 381,89 vom alten Hoch 434,19)

**LLY-Reversal-Fortsetzung:**
- Open 1.143,26 (chg -1,12 %) → Close 1.170,50 (chg +1,20 %, Tageshoch 1.188,19)
- P/L Verlauf: Mi Close -3,16 % → Open -4,01 % (Panik-Open) → Midday -1,92 % → Close **-1,96 %**
- XLV-Rebound getragen (UNH-Q2-Effekt zieht Sektor mit)
- V1 1.098,38 +6,57 % Puffer (aus engster Position wechselt zu GS)

**Sektor-Performance Close (Perplexity keine Zahlen, Ableitung aus Positions):**
- XLC: **stark negativ** (GOOGL -4,33 % dominiert, Nachmittags-Rotation raus)
- XLF: **negativ** (JPM -1,08 % + GS -4,91 %, XLF Sektor-Loser)
- XLV: **positiv-stabil** (UNH +0,63 % + LLY +1,20 %, Rebound getragen)
- XLK: **positiv-stabil** (AAPL +1,62 % Rebell)

**V2-Trailing-Stop-Updates:**
| Sym | Tageshoch | Neuer V2  | Alt V2   | Aktion |
|-----|-----------|-----------|----------|--------|
| UNH |  460,95   |   405,64  |  381,89  | **AKTUALISIERT** (neues Posit-Hoch) |
| AAPL|  334,65   |   294,49  |  284,59  | **AKTUALISIERT** (neues Fill-Day-Hoch) |
| JPM |  348,83   |   306,97  |  302,11  | **AKTUALISIERT** (neues Post-Q2-Hoch) |
| GOOGL| 375,18   |   330,16  |  328,36  | **AKTUALISIERT** (marginal höher) |
| LLY | 1.188,19  | 1.045,61  |1.098,70  | unverändert (V2 trailt nur UP, altes 1.248,53 höher) |
| GS  | 1.150,10  | 1.012,09  |1.013,45  | unverändert (V2 trailt nur UP, altes 1.151,65 höher) |

**Alpaca-Screener K1-K3 für Watchlist Fr 17.07. + KW30-Slot-Vorbereitung (19 Symbole gescannt, Slot LOCK KW29):**
```
V     [XLF]   364,78  3/3  K1=✓(+3,16)  K2=✓(RSI 69,93) K3=✓(RS +8,13%)   → grenzwertig oben
PANW  [XLK]   354,11  3/3  K1=✓(+60,49) K2=✓(RSI 66,13) K3=✓(RS +108,23%) → K5-FwdPE-Risk
ABBV  [XLV]   254,38  3/3  K1=✓(+13,40) K2=✓(RSI 65,83) K3=✓(RS +15,35%)  → XLV Sektor-Cap
MRK   [XLV]   127,66  3/3  K1=✓(+13,92) K2=✓(RSI 58,56) K3=✓(RS +1,50%)   → XLV Sektor-Cap
NVDA  [XLK]   207,46  2/3  K3-Fail (-3,13% RS)
AMZN  [XLY]   249,95  2/3  K3-Fail (-6,98% RS)
XOM   [XLE]   145,95  2/3  K3-Fail (-8,96% RS)
CVX   [XLE]   183,85  2/3  K3-Fail (-7,21% RS)
CAT   [XLI]   877,74  2/3  K2-Fail (RSI 39,51)
```

**Watchlist Fr/KW30:** V + PANW + ABBV + MRK (4 LEADS). K5-Multi-Source-Recheck bei Weekly Review Fr 17.07. Close zwingend für alle 4 (FwdPE ≤ 35 + RevGrowth ≥ 10 % + Earnings-Blackout + Sektor-Konzentrations-Check). XLV-Cap: UNH + LLY bereits 2/3, ABBV/MRK würden 30 %-Cap sprengen bei voller Position → nur 1 XLV möglich, bevorzugt K5-grüner. Slot LOCK bis Mo 20.07.

**Guardrail-Status (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,546 %                                    [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,143 % (KW29 Tag 4)                       [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,585 % vs ATH 100.066,47                  [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,585 %                                    [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,517 %                                [INAKTIV]
6. VIX-Filter (>30):          ~15-16 (carry-over)                         [GRÜN]
7. Earnings-Blackout (3 HT):  UNH beendet, GOOGL ab Fr Close aktivierbar  [ÜBERGANG]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30                 [LOCK]
```

**ClickUp:** POST Tagesbericht Prio 3 (negative Perf) — bei ITEM_246 Tier-Limit-Muster Fallback PushNotification an Owner.

**Datenqualität:**
- Alpaca /v2/account + /v2/positions Close 16:02 ET erfolgreich, alle 6 Positionen mit chg_today/plpc
- Alpaca /v2/bars 262d SPY + 6 Positionen für EMA50/EMA200/RSI Wilder erfolgreich (Wilder-Smoothing volle Historie)
- Perplexity SPY-Query "Zukunftsdatum-Refusal" (2026-07-16 als "Future" abgelehnt trotz laufendem Handelstag)
- Perplexity Watchlist-Query gleicher Refusal → Alpaca-Screener-Fallback (Standard-Vorgehen etabliert)
- Alpaca IEX-Daten sind Ground-Truth für Portfolio-Bewegungen; Perplexity nur Cross-Check-Fallback

> **Entscheidung Close 16.07.:** **Alle 6 V1-V6 SICHER**, keine Sell/Limit-Order für Fr platziert. Portfolio -0,546 % Daily / -0,030 % Alpha NEUTRAL. **GS 4,29 % ENGSTE** (Fill-Day+1-Drop-Muster VOLLBILD, kritischer Pre-Market-Watch Fr), **GOOGL 4,79 %** (Nachmittags-Kollaps -4,44 %, Blackout-Tightening Close Fr auf 349,70). UNH Pump-and-Dump vom Tageshoch 460,95 vollständig materialisiert (-8,64 % vs H), aber P/L +4,87 % gehalten. LLY-Reversal-Fortsetzung. Weekly KW29 -0,143 %, DD -1,585 %. Käufe LOCK 2/2 bis Mo 20.07.
> **Nächste Routine:** Fr 17.07. 08:30 ET Pre-Market Check — GS/GOOGL kritisch, GOOGL-Blackout-Aktivierung im Kalender für Close-Routine Fr.

---

## Market Open 09:37 ET — 2026-07-16 (Do, KW29 Tag 4) — UNH Q2-Rally +7,94 %, kein Kauf-Scan (LOCK), V1-Reset UNH 369,44 ausgeführt, Alpha +0,861 % POSITIV

**Alpaca Clock:** is_open=true, next_close 16.07. 16:00 ET.

**Account Live 09:37 ET (Alpaca /v2/account):**
```
Equity:            99.548,85 $   (vs last_equity 99.021,31 → +0,533 %)   [GRÜN, Cap -3 %]
Cash:              49.670,08 $   (49,90 %, unverändert seit GS-Fill Mi 15.07.)
Portfolio_MV:      49.878,77 $   (50,10 %, 6 Positionen)
Buying_power:     338.340,86 $
Käufe KW29:        2/2 LOCK      (AAPL Mo + GS Mi gefüllt, bis Mo 20.07. KW30) [LOCK]
Pending Orders:    0             (keine offenen, kein neuer Kauf-Scan)
```

**Positionen Live 09:37 ET (Alpaca /v2/positions):**
| Sym    | Curr      | Vortag  | Chg %      | P/L %    | V1-Puffer | Bemerkung |
|--------|-----------|---------|------------|----------|-----------|-----------|
| **UNH**|   451,75  | 418,40  | **+7,94 %**| +12,50 % | +22,28 %  | **Q2-BEAT-Rally (Pre-Market +6,80 % → Open +7,94 %)** |
| AAPL   |   328,00  | 327,64  |   +0,15 %  |  +3,52 % | +12,52 %  | Konsolidierung nach Mi-Rebell |
| GOOGL  |   371,17  | 371,11  |   +0,07 %  |  +0,83 % | +9,61 %   | Stabil |
| **GS** | 1.126,96  | 1.151,93|  **-2,18 %**|  -1,29 % | +7,29 %   | **Fill-Day+1 Drop-Muster** ausgelöst |
| JPM    |   342,34  | 346,91  |   -1,32 %  |  +2,87 % | +11,82 %  | Mildes Give-back Post-Q2 Tag 3 |
| **LLY**| 1.145,99  | 1.156,19|   -0,92 %  |  -4,01 % | **+4,33 %**| **Engste V1**, Reversal Mi pausiert |

**SPY-Ground-Truth:** Alpaca IEX SPY 752,295 vs Mi-Close 754,77 → **-0,328 %**. Alpha vs SPY = +0,533 % − (-0,328 %) = **+0,861 % POSITIV** (UNH-Rally dominiert Portfolio-Return).

**UNH V1-Reset AUSGEFÜHRT (Post-Release-Bestätigung erfüllt):**
- Trigger: Q2-Beat-Reaktion chg +7,94 % (Pre-Market +6,80 % → Open Fortsetzung) = positive Post-Release-Reaktion
- Alt: V1 **381,49** (-5 % Blackout-Tight, aktiv Mo 13.07. Close → Mi 15.07. Close)
- Neu: V1 **369,44** (-8 % Standard = 401,57 × 0,92)
- Puffer bei Live 451,75 = **+22,28 %** [KOMFORTABEL, kein V1-Stop-Risiko kurzfristig]

**GS Fill-Day+1 Drop-Muster ausgelöst — Muster-Dokumentation:**
- Chg -2,18 % Fill-Day+1 (vs Mi Close 1.151,93 → 1.126,96)
- Analogie: AVGO -4,36 %/-5,77 % (Fill-Day+0/+1), MU -5,26 %/-5,85 %, LLY +0,79 %/+2,96 % (Ausnahme positiv)
- GS Muster **abgeschwächt** (nur -2,18 % vs -4 bis -6 %), aber Fortsetzung des dokumentierten Musters
- V1 1.050,40 bei 1.126,96 = +7,29 % Puffer (Verengung von Mi Close +9,67 %)
- Keine Aktion nötig (weit vom V1 entfernt)

**Kauf-Scan: NICHT DURCHGEFÜHRT (Slot-LOCK 2/2 KW29 bis Mo 20.07. KW30).**
Watchlist V + PANW carry-over aus Mi Close für Mo 20.07. KW30-Slot-Vorbereitung. Perplexity Watchlist/K5-Multi-Source-Query im Weekly Review Fr 17.07. geplant.

**GOOGL-Blackout-Vorbereitung (nicht heute — Aktion Fr Close):**
- GOOGL Q2 **22.07.2026 AMC** → 3-HT-Blackout ab Fr 17.07. Close aktivierbar
- V1-Tightening morgen 349,70 (-5 %) statt 338,65
- HEUTE NUR im Kalender vermerken

**Guardrail-Status (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,533 %                                 [GRÜN]
2. Weekly Loss Cap (-5 %):    +0,940 % (KW29 Tag 4)                    [GRÜN]
3. Drawdown-Alarm (-15 %):    -0,517 % vs ATH 100.066,47 (verbessert)  [GRÜN]
4. Drawdown-Stopp (-20 %):    -0,517 %                                 [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,328 %                             [INAKTIV]
6. VIX-Filter (>30):          ~15,76-16,40 (Perplexity Do)             [GRÜN]
7. Earnings-Blackout (3 HT):  UNH-Blackout BEENDET → V1 zurück 369,44  [ÜBERGANG COMPLETE]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30              [LOCK]
```

**ClickUp:** Sende-Versuch für UNH-Q2-Rally-Event pending (ITEM_246 Tier-Limit erwartet, Fallback PushNotification an Owner geplant).

> **Entscheidung Market Open 16.07.:** **KEIN Kauf-Scan** (Slot-LOCK 2/2). **UNH V1-Reset AUSGEFÜHRT** 381,49 → **369,44** nach Q2-Beat-Post-Release. Portfolio **+0,533 % Daily / +0,861 % Alpha POSITIV** dominiert von UNH-Q2-Rally (Beitrag ~+1.204 $). Alle 6 V1-V6 SICHER, keine Sell-Order platziert. LLY engste +4,33 % Puffer (Reversal Mi pausiert), GS Fill-Day+1 -2,18 % Drop-Muster abgeschwächt aber ausgelöst. Weekly KW29 Tag 4 +0,940 %, DD -0,52 %. UNH-Positions-Hoch NEU wahrscheinlich → V2-Trail-Update bei Close 397,54 statt 381,89.
> **Nächste Routine:** Do 16.07. 13:00 ET Midday Stop-Check (UNH-Rally-Sustainability, GS Fill-Day+1 Fortsetzung, LLY V1-Watch).

---

## Pre-Market 08:30 ET — 2026-07-16 (Do, KW29 Tag 4) — UNH Q2 BMO POSITIV-Reaktion +6,80 %, alle Guardrails GRÜN, Käufe LOCK, V1-Reset UNH 369,44

**Alpaca Clock:** is_open=false, next_open Do 16.07. 09:30 ET, next_close 16:00 ET.

**Account Pre-Market 08:30 ET (Alpaca /v2/account):**
```
Equity:            99.760,19 $   (vs last_equity 99.021,31 → +0,7462 %) [GRÜN, Cap -3 %]
Cash:              49.670,08 $   (49,79 %, unverändert seit GS-Fill 15.07.)
Portfolio_MV:      50.090,11 $   (50,21 %, 6 Positionen)
Long_MV:           50.090,11 $
Buying_power:     338.932,62 $
Käufe KW29:        2/2 LOCK      (bis Mo 20.07. KW30) [LOCK — kein Scan Market Open]
Pending Orders:    0             (keine offenen aus Mi Close)
```

**Pre-Market Chg_today per Alpaca /v2/positions (offizielle Alpaca-Sicht vor Open):**
| Sym    | Curr      | Vortag Close | Chg %      | P/L     | Bemerkung |
|--------|-----------|--------------|------------|---------|-----------|
| **UNH**|   447,00  |   418,40     | **+6,80 %**| +11,31 %| **Q2-BMO POSITIV-Reaktion — Beat wahrscheinlich** |
| GOOGL  |   372,65  |   371,11     |   +0,47 %  |  +1,24 %| Rebound-Fortsetzung |
| AAPL   |   328,46  |   327,64     |   +0,29 %  |  +3,66 %| stabil |
| LLY    | 1.160,00  | 1.156,19     |   +0,29 %  |  -2,84 %| Reversal-Fortsetzung, V1-Puffer +5,61 % |
| JPM    |   347,30  |   346,91     |   +0,11 %  |  +4,36 %| Post-Q2 stabil |
| GS     | 1.146,25  | 1.151,93     |   -0,51 %  |  +0,40 %| Fill-Day+1 mildes Muster |

→ Portfolio Pre-Market **+738,88 $ (+0,7462 %)** primär durch UNH-Q2-Rally getrieben (Beitrag ~+686 $ = ~+0,69 %).

**Perplexity Daily-Macro-Query:** SPY-Pre-Market, 10Y-Yield, Makro-Events "Datenlücke" — Perplexity gab **VIX 15,76 (Cboe Spot 15.07.) / 16,40 (Finanzen.net 16.07.)** als einzige belastbare Zahl. SPY-Pre-Market und Makro-Events "nicht verfügbar in Search-Results". Fallback: Alpaca-Realdaten dienen als Ground-Truth für Portfolio-Bewegungen.

**UNH-Q2-Release-Verifikation via Perplexity:** Actual-Zahlen "nicht in Search-Results verfügbar". Konsens-Preview (vor Bericht):
- EPS-Konsens: **$4,84-4,85 Adj**
- Revenue-Konsens: **$110,77-110,95 Mrd**
- FY26 Guidance vorher: **> $18,25 Adj EPS**
- Reported: **Alpaca-Reaktion +6,80 % Pre-Market** ist Ersatz-Signal → **Beat/Positive Guidance-Anpassung sehr wahrscheinlich** (bei EPS-Miss wäre Reaktion typisch negativ)

**Earnings-Kalender Do 16.07.-Mo 20.07. (Perplexity + Memory-Cross-Check):**
- **Do 16.07. BMO — UNH Q2** ✓ (heute, positiv reagiert)
- Fr 17.07. — keine relevanten Positions-Earnings
- Mo 20.07. — keine relevanten Positions-Earnings
- **Mi 22.07. AMC — GOOGL Q2** → **3-HT-Blackout ab Fr 17.07. Close aktivierbar** → V1 auf **349,70 (368,10 × 0,95 = -5 %)** statt 338,65 zu tightenen (Aktion Fr Close-Routine, HEUTE noch NICHT)
- Mi 30.07. — AAPL Q3 → Blackout ab Fr 24.07. Close aktivierbar

**UNH V1-Reset — Blackout-Ende:**
- Bisher: V1 **381,49** (-5 % Blackout-Tight, aktiv seit Mo 13.07. Close)
- Neu ab HEUTE Post-Release: V1 **369,44** (-8 % Standard = 401,57 × 0,92) → Puffer bei aktuellem Pre-Market 447,00 = **+20,99 %** [KOMFORTABEL]
- Regel: Nach Post-Release-Bestätigung (positive Reaktion +6,80 % Pre-Market) V1 zurück auf Standard-Level; keine weitere Tightening-Notwendigkeit

**Guardrail-Status Pre-Market (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,7462 % Pre-Market                    [GRÜN]
2. Weekly Loss Cap (-5 %):    +1,156 % (KW29 Tag 4, kum. +0,407 % + 0,746 %) [GRÜN]
3. Drawdown-Alarm (-15 %):    -0,306 % vs ATH 100.066,47 (verbessert)  [GRÜN]
4. Drawdown-Stopp (-20 %):    -0,306 %                                 [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Vortag +0,376 %                      [INAKTIV]
6. VIX-Filter (>30):          ~15,76-16,40 (VIX Do Pre-Market)         [GRÜN]
7. Earnings-Blackout (3 HT):  UNH endet HEUTE Post-Release → V1 369,44 [ÜBERGANG]
8. Max Käufe KW29:            2/2 LOCK bis Mo 20.07. KW30              [LOCK — kein Scan]
```
→ **ALLE GUARDRAILS GRÜN. Kein Kaufscan (Slot-LOCK). Kein STOPP.**

**Entscheidung Pre-Market Do 16.07.:**
- **Market-Open-Scan JA/NEIN → NEIN** (Käufe KW29 2/2 LOCK bis Mo 20.07. KW30)
- **UNH V1-Reset:** 381,49 → 369,44 nach Post-Release-Bestätigung (Pre-Market +6,80 % bestätigt Positiv-Reaktion) — zu setzen bei Market-Open-Routine 09:30 ET
- **Watchlist-Vorbereitung KW30:** V + PANW (K5 Multi-Source zwingend im Weekly-Review Fr 17.07.)
- **GOOGL-Blackout-Vorbereitung:** Fr 17.07. Close V1 auf 349,70 tightenen (HEUTE noch NICHT)

**Zwingende Watch-Punkte Market Open 09:30 ET + Midday 13:00 ET:**
1. UNH V1-Reset auf 369,44 im Positions-Memory tracken
2. UNH Post-Release-Reaction sustained (kein Pump-and-Dump) — Watch für V2-Trail-Update bei neuem Positions-Hoch
3. LLY V1 1.098,38 aktuell +5,61 % Puffer (verbessert von Mi Close +5,26 %) — Reversal-Fortsetzung
4. GS Fill-Day+1 mildes -0,51 % Pre-Market (kein Stop-Risk, V1 1.050,40 +9,15 % Puffer)
5. AAPL/JPM/GOOGL: alle stabil, keine Watch-Trigger

**Datenqualität:**
- Alpaca /v2/account + /v2/positions live Pre-Market 08:37 ET erfolgreich, alle 6 Positionen mit chg_today und plpc
- Alpaca /v2/clock: is_open=false, next_open 09:30 ET
- Perplexity Macro-Query lieferte VIX (15,76-16,40) als einzigen belastbaren Wert; SPY Pre-Market, 10Y Yield, News-Headlines "nicht verfügbar" — "Datenlücke Pre-Market"-Muster fortgesetzt
- Perplexity UNH-Q2-Release-Verifikation: keine Actual-Zahlen → Alpaca-Reaktion +6,80 % als Ersatz-Signal

**ClickUp:** Pending Sende-Versuch (ITEM_246 Tier-Limit weiter erwartet, Fallback PushNotification an Owner geplant)

> **Entscheidung Pre-Market Do 16.07.:** Portfolio +0,7462 % Pre-Market (UNH-Q2-Rally +6,80 % Haupt-Treiber, ~+686 $ Beitrag), alle 8 Guardrails GRÜN, Käufe KW29 LOCK 2/2 → **kein Market-Open-Kaufscan**. UNH V1-Reset 381,49 → **369,44** zwingend bei Market-Open-Routine (Post-Release-Bestätigung durch +6,80 % Pre-Market-Rally erfüllt). Perplexity Macro-Query Datenlücke Pre-Market weiterhin — VIX 15,76-16,40 GRÜN einziger belastbarer Wert. GOOGL-Blackout-Vorbereitung Fr 17.07. Close (V1 auf 349,70 statt 338,65) im Kalender.
> **Nächste Routine:** Do 16.07. 09:30 ET Market Open — UNH V1-Reset ausführen, kein Kaufscan (Slot-LOCK), Position-Update mit UNH Q2-Rally-Details.

---

## Market Close 16:02 ET — 2026-07-15 (Mi, KW29 Tag 3) — Tagesbilanz, alle V1-V6 SICHER, Alpha +0,292 % POSITIV, Watchlist Do V+PANW 3/3-LEADS

**Alpaca Clock:** is_open=false, next_open Do 16.07. 09:30 ET, next_close 16:00 ET.

**Account Close 16:02 ET:**
```
Equity:            99.023,08 $   (vs last_equity 98.365,51 → +0,668 %)                    [GRÜN]
Cash:              49.670,09 $   (50,16 %, unverändert seit GS-Fill Mi 09:41 ET)
Portfolio_MV:      49.352,99 $   (49,84 %, 6 Positionen)
Buying_power:     336.868,73 $
Käufe KW29:        2/2 LOCK      (bis Mo 20.07. KW30)                                     [LOCK]
Pending Orders:    0             (V5/V6 alle 6 SICHER, keine Limit für Do)
```

**SPY-Ground-Truth:** Alpaca IEX SPY 754,77 vs Di-Close 751,94 → **+0,376 %**. Alpha vs SPY = +0,668 % − (+0,376 %) = **+0,292 %** [POSITIV — Umkehr vs Di -0,54 %].

**Positionen Close 16:02 ET (Alpaca IEX 271d Bars, EMA/RSI Wilder):**
| Sym    | Close     | P/L      | Chg_today | V1-Puffer | EMA-Spread | RSI(14) | RS_4w  | Status |
|--------|-----------|----------|-----------|-----------|------------|---------|--------|--------|
| AAPL   |   327,64  | +3,40 %  | **+4,08 %**| +12,39 % | +26,18     | 69,39   | +10,47 %| **Tages-Sieger** (XLK -1,10 % Sektor-Loser, +5,18 % relativ, Fill-Day+2 Rebound) |
| JPM    |   346,91  | +4,25 %  | +1,17 %   | +13,31 %  | +12,29     | 67,34   | +8,56 % | Neues Positions-Hoch (Post-Q2 Tag 3, XLF-Outperform +0,54 %) |
| UNH    |   418,40  | +4,19 %  | -1,60 %   | +9,67 %   | +46,58     | 53,31   | +1,72 % | **Blackout-Cooldown letzter Tag, Q2 morgen BMO → V1-Reset 369,44 zwingend** |
| LLY    | 1.156,19  | -3,16 %  | +0,32 %   | **+5,26 %**| +128,80   | 50,37   | +2,38 % | **Engste**, RSI REKONVERTIERT (49,90 Di → 50,37), XLV neutralisiert |
| GOOGL  |   371,11  | +0,82 %  | +3,23 %   | +9,58 %   | +45,32     | 56,84   | +0,48 % | **P/L erstmals grün seit Fill**, +1,53 % vs XLC (LEAD-Sektor) |
| GS     | 1.151,93  | +0,89 %  | +1,05 %   | +9,67 %   | +117,49    | 68,78   | +6,89 % | **Fill-Day+0 P/L grün** (Fill-Day-Drop-Muster nicht ausgelöst) |

→ **Alle 6 V1-V6 SICHER.** LLY +5,26 % weiter engste, aber Watch-Mode reduziert.

**Sektor-Performance Close (Alpaca IEX ranking):**
```
XLC +1,700 % (LEAD Communication Services)
XLY +0,932 % | XLF +0,632 % | SPY +0,376 %
XLRE +0,135 % | XLP +0,054 % | XLV +0,032 %
XLI -0,200 % | XLB -0,336 % | XLE -0,843 %
XLU -0,997 %
XLK -1,101 % (LOSER Tech-Rücksetzer)
VXX -2,886 % (Vola weiter runter, VIX ~15-16)
```
→ **Rotation raus aus Tech/Utilities/Energy, rein in Communication/Discretionary.** AAPL XLK-Rebell +5,18 % relativ ist Story des Tages.

**Alpaca-Screener 12 Large-Caps K1-K3 für Watchlist Do 16.07. (Slot LOCK KW29, Mo 20.07. KW30 Vorbereitung):**
```
Sym    Close      K1 EMA-Spread    K2 RSI    K3 RS_63d      Verdict
V      355,31     ✓ +1,84 marginal ✓ 64,10   ✓ +4,51 %      3/3 LEAD (K5 Median ~25 grün, Blackout ab 23.07. Close)
PANW   353,99     ✓ +59,19         ✓ 66,09   ✓ +109,47 %    3/3 LEAD (RS #1, K5-FwdPE Cybersecurity zwingend)
NVDA   212,50     ✓ +11,36         ✓ 56,86   ✗ -1,47 %      2/3 K3-FAIL (verschlechtert vs Di +2,30 %)
META   681,24     ✗ -39,02         ✓ 66,79   ✗ -6,76 %      1/3 FAIL
AMZN   254,94     ✓ +8,25          ✓ 60,27   ✗ -7,25 %      2/3 K3-FAIL
TSLA   394,32     ✓ +4,06          ✗ 47,14   ✗ -1,33 %      1/3 FAIL
MA     535,33     ✗                ✓ 63,39   ✗ -5,27 %      1/3 FAIL
MSFT/ORCL/NFLX/COST/WMT: alle ≤1/3 FAIL (RS deutlich negativ)
```

**Watchlist Do 16.07. + Mo 20.07. KW30 Kandidaten (K4/K5 morgen zwingend):**
- **V 355,31** — 3/3 LEAD, K5 FwdPE Median ~25 (Perplexity Multi-Source Di dokumentiert), Q3 FY26 Earnings ~28.07.2026 AMC = **9 HT weg → 3-HT-Blackout ab 23.07. Close aktivierbar**, Kauf-Fenster Mo-Mi 20.-22.07.; K1 EMA-Spread +1,84 marginal (Sensitivität Pre-Market)
- **PANW 353,99** — 3/3 LEAD, RS_63d **+109,47 %** #1 Screener (Chip/Cybersecurity Rally), K5-Multi-Source-FwdPE zwingend prüfen (Cybersecurity typisch > 35 wie AMD-Reject-Analogie 14.07.); nächste Earnings zwingend prüfen (typisch Ende August für PANW Q4 FY26)
- **NVDA 212,50** — 2/3 K3-FAIL (-1,47 %) durch XLK-1,10 % Tag 3 Rücksetzer; Watch für Rebound-Signal (Chip-Sektor-Comeback)

**Perplexity-Refusal-Muster:** Query "SPY 15.07.2026 Tagesperformance" + "Momentum Watchlist 16.07.2026" → **"zukünftiges Datum"-Refusal** (Perplexity hält 15.07.2026 fälschlich für Zukunft trotz laufender Session). Fallback: **Alpaca IEX Ground-Truth** SPY 754,77 (+0,376 %), VXX 20,86 (-2,89 %) für VIX-Proxy, 12-Symbol-Screener für Watchlist. Robuste Fallback-Pipeline etabliert Tag 2 in Folge.

**Guardrail-Status Close (alle 8):**
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

**Earnings-Kalender KW29-30:**
- **Do 16.07. BMO — UNH Q2** → Blackout endet, V1-Reset auf 369,44 nach Release
- Fr 17.07. — keine relevanten Positions-Earnings
- **Mi 22.07. — GOOGL Q2** → 3-HT-Blackout ab Fr 17.07. Close aktivierbar (V1 auf 349,70 = 368,10×0,95)
- Di 28.07. AMC — V Q3 FY26 (nur wenn wir bis dahin V gekauft haben in KW30)
- Mi 30.07. — AAPL Q3 → 3-HT-Blackout ab Fr 24.07. Close aktivierbar

**Sektor-Zusammensetzung Close (6 Positionen, unverändert vs Open):**
```
XLK: AAPL 10.157 = 10,26 %
XLC: GOOGL 9.649 = 9,74 %
XLF: JPM 1.041 + GS 9.215 = 10.257 = 10,36 %  (2/3 Pos, unter 30 % ✓)
XLV: UNH 10.042 + LLY 9.250 = 19.292 = 19,48 %  (2/3 Pos, unter 30 %)
Cash: 49.670 = 50,16 %
Total invested: 49,84 % (unter 80 %-Cap)
```

**LLY-Sonderbeobachtung — Positives Reversal Tag 1:**
- Close 1.156,19 vs V1 1.098,38 = **+5,26 % Puffer** (verbessert von Midday +4,16 %, Open +4,04 %)
- Chg heute +0,32 % (nach 6 Tagen XLV-Schwäche mit -2,33 % Di als Tiefpunkt)
- RSI(14) 50,37 rekonvertiert von Di 49,90 (Momentum-Neutralisierung überwunden)
- XLV +0,03 % Tag 7 stabilisiert (vs Di -1,92 % Tag 6)
- **Watch-Mode reduziert, aber V1 1.098,38 weiter aktiv** (Position bleibt engste in Portfolio)

**ClickUp:** POST /list/{id}/task → HTTP 400 **ITEM_246 Tier-Limit** (Tag 3 in Folge Di/Mi persistent). Fallback: **PushNotification an Owner** (Routine-Regel per notify-skill.md).

> **Entscheidung Market Close 15.07.:** Portfolio +0,668 % positiv, **Alpha +0,292 % POSITIV** (klare Umkehr vs Di -0,54 %). Tages-Story: AAPL Fill-Day+2 XLK-Rebell (+4,08 % chg vs XLK -1,10 % Sektor-Loser = +5,18 % relativer Outperform) trotz Tech-Rücksetzer. JPM neues Positions-Hoch Post-Q2 Tag 3. GOOGL+GS erstmals P/L grün. LLY positives Reversal (RSI 50,37 rekonvertiert, Chg +0,32 %, V1-Puffer +5,26 %). UNH -1,60 % pre-Q2 Blackout-letzter-Tag regelkonform. Alle V1-V6 SICHER → **keine Limit-Order für Do 16.07.** Sektor-Rotation: XLC LEAD +1,70 %, XLK LOSER -1,10 %, XLV neutralisiert (LLY-Positive-Reversal), VXX -2,89 % Vola weiter runter (VIX ~15-16 stabil). Perplexity "Zukunftsdatum"-Refusal Tag 2 → Alpaca-Fallback-Pipeline robust (SPY/VXX/Screener 12 Symbole).
> **Zwingender Watch Do 16.07.:** (1) **UNH Q2 BMO 7:00 AM ET + Call 8:30 AM** — Blackout endet, V1-Reset **von 381,49 → 369,44** (401,57 × 0,92) zwingend nach Release-Bestätigung; (2) LLY V1 1.098,38 +5,26 % Puffer engste (RSI rekonvertiert Watch-Mode reduziert); (3) GS Fill-Day+1 V1 1.050,40 +9,67 %; (4) AAPL XLK-Divergenz-Fortsetzung (+5,18 % relativ nachhaltig?); (5) V/PANW K5-Multi-Source-Vorbereitung für Mo 20.07. KW30-Slot.
> **Lessons-Tag:** (1) AAPL Fill-Day+2 einzelwert-getriebener Sektor-Rebell +5,18 % relativer Outperform gegen XLK -1,10 % — K1-K5-Screen war regel-konform, Momentum kann Sektor dominieren; (2) LLY XLV-Sektor-Neutralisierung nach 6 Tagen Schwäche mit RSI 49,90→50,37 Rekonversion — Bottom-Signal-Kandidat, aber V1-Watch bleibt bei engster Position; (3) Alpaca-Screener als robuster Perplexity-Fallback bei "Zukunftsdatum"-Refusal — V+PANW als 3/3-K1-K3-LEADS identifiziert ohne externen Datenzugriff; (4) GOOGL Fill-Day+7 P/L erstmals grün nach 6 HT Fill-Day-Drop-Muster — bestätigt Muster-Dokumentation ohne Stop-Notwendigkeit.
> **Nächste Routine:** Do 16.07. 08:30 ET Pre-Market Check (KW29 Tag 4, **UNH Q2 BMO — V1-Reset 369,44 zwingend**, LLY V1-Watch reduziert, GS Fill-Day+1, Käufe LOCK bis Mo 20.07.).

---

## Market Open 09:42 ET — 2026-07-15 (Mi, KW29 Tag 3) — GS 8 Sh @ 1.141,74 GEFÜLLT, Slot 2/2 KW29 verbraucht, alle 5 K-Signale grün, Käufe-LOCK

**Alpaca Clock:** is_open=true, next_close 15.07. 16:00 ET.

**Account Post-Fill 09:42 ET:**
```
Equity:            98.376,40 $   (vs Alpaca last_equity 98.365,51 → +0,011 %)              [GRÜN]
Cash:              49.670,09 $   (50,49 %, -9.133,95 vs Open durch GS-Fill)
Portfolio_MV:      48.706,31 $   (49,51 %, 6 Positionen)
Buying_power:     335.058,02 $
Käufe KW29:        **2/2 LOCK** (AAPL Mo + GS Mi)                                          [LOCK]
Pending Orders:    0 (GS-Order vollständig gefüllt)
```

**SPY-Ground-Truth:** Alpaca IEX SPY 754,84 vs Di-Close 751,94 → **+0,386 %**. Alpha vs SPY = +0,011 % − (+0,386 %) = **-0,375 %** [leicht negativ, aber GS Fill-Day-Effekt einbezogen].

**Positionen Post-Fill Live 09:42 ET:**
| Sym    | Live      | P/L      | Chg_today | V1-Stop         | V1-Puffer | Status |
|--------|-----------|----------|-----------|-----------------|-----------|--------|
| AAPL   |   319,15  |  +0,72 % |  +1,363 % | 291,51          | +9,48 %   | SICHER (Fill-Day+2 Rebound, XLK-Recovery) |
| JPM    |   349,38  |  +4,99 % |  +1,893 % | 306,16          | +14,12 %  | SICHER (Post-Q2 Rally Tag 3, +2,11 % vs XLF) |
| UNH    |   418,05  |  +4,10 % |  -1,679 % | 381,49⚠         | +9,58 %   | SICHER (Blackout letzter Tag bis Do 16.07. BMO) |
| LLY    | 1.142,80  |  -4,28 % |  -0,845 % | 1.098,38        | **+4,04 %** | SICHER (**engste**, RSI 49,90 gekippt, XLV-Watch Tag 7) |
| GOOGL  |   364,19  |  -1,06 % |  +1,302 % | 338,65          | +7,54 %   | SICHER (Fill-Day+7 Rebound, XLC-Outperform) |
| **GS** | 1.140,38  |  -0,12 % |  +0,033 % | **1.050,40 NEU**| +8,57 %   | SICHER (**Fill-Day+0**, alle 5 K-Signale grün) |

→ **Alle 6 V1-V6 SICHER.** LLY +4,04 % neu engste (verengt von PM +4,97 %).

**GS KAUF-Details (Slot 2/2 KW29 GEFÜLLT):**
- Limit-Order 1.147,58 $ Day (+0,5 % über Di-Close 1.141,87)
- Submit 09:41:14 ET → Fill **09:41:18 ET** (4 sec, sehr schneller Fill)
- 8/8 Sh @ **1.141,74375 avg** (unter Limit — Post-Submit-Dip auf 1.140,24 hat gefüllt)
- Investiert 9.133,95 $ (9,28 % Portfolio)
- V1 1.050,40 | TP1 1.370,09 | TP2 1.541,35
- Alpaca Order-ID: 495b1c15-9346-4b97-a2f4-7278773753c3

**K1-K5 GS validiert (Alpaca 270d Bars 2025-06-16 → 2026-07-14 + Perplexity K5):**
```
K1 EMA50 1.018,62 > EMA200 903,90 → Spread +114,73     ✓ (Golden Cross sehr breit)
K2 RSI(14) Wilder 67,63                                 ✓ (50-70 Fenster, knapp oben)
K3 RS_63d = GS +28,16 % - SPY +9,61 % = +18,55 %       ✓ (bester Screener-Wert)
K4 Intraday 10min IEX 11.126 Sh, extrap 434k IEX/Tag   ✓ (~606 % Avg20 IEX 71.632)
K5 FwdPE 14,74 / 17,04 / 17,53 / 16,66 → Median ~17    ✓ (klar ≤ 35, 51 % Puffer)
   Rev-Growth Q2 2026 (Umsatz $20,34 Mrd 14.07.)        ✓ (Konsens +11,81 % YoY)
   Q3 Earnings ~Mitte Oktober = >60 HT weg              ✓ (kein Blackout)
```

**Konkurrenz-Kandidaten K5-Recheck:**

**NVDA (Live 211,65 -0,07 % vs Di):**
- Perplexity Multi-Source FwdPE: 34,33 [GuruFocus heute] / 20,40 [StockAnalysis 2026-07-10] / 40,78 [ValueInvesting.io]
- **Range 20,40-40,78 (Median 34,33)** — grenzwertig ≤ 35, aber Multi-Source-Uncertainty ±5-10 um Cap
- Analogie AMD Di 14.07.: FwdPE 35,72-68,65 Multi-Source → K5-Reject
- **NVDA-Verdikt: konservativ REJECT** (Bot-Persona "konservativ bei Unsicherheit" + K5-Cap-Nähe wie AMD-Muster)
- Revenue Growth Q1 FY2026 +122,40 % ✓, aber K5-Bewertung dominiert
- NVDA Q2 FY2026 typisch Ende August — kein Blackout aktuell

**V (Live 353,56 -0,69 % vs Di):**
- Perplexity Multi-Source FwdPE: 24,88 [Yahoo] / 22,78 [StockAnalysis] / 25,33 [ValueInvesting.io] / 21,28 [Intellectia 2026-06-14] / 30,15 [Eulerpool 2026-07-01] / 25,60 [LYNX 2026-07-03]
- **Range 21,28-30,15 (Median ~25)** — klar ≤ 35 ✓ (K5-FwdPE-Puffer 29 % zu Cap)
- Revenue Growth Q letztes gemeldet: +17,10 % YoY ✓
- V Q3 FY26 Earnings: **~28.07.2026 AMC** (historischer Rhythmus letzter Dienstag Juli, Perplexity nicht explizit bestätigt via V IR) = **9 HT ab heute**
- **3-HT-Blackout ab 23.07. Close aktivierbar** → V1-Stop-Tightening auf -5 % ab dann zwingend
- **V-Verdikt: K5-grün, aber Earnings-Blackout-Risiko in 8 HT nach Kauf** vs GS (kein Blackout)

**Warum GS vor V/NVDA gewählt:**
1. **GS RS_63d +18,55 %** deutlich vor V (+5,47 %) und NVDA (+2,30 %) — Bot-Rule "höchste RS + alle Signale grün"
2. **GS K5-FwdPE-Puffer** (Median 17 vs Cap 35 = 51 % Puffer) deutlich robuster als NVDA (34,33 vs 35 = <2 % Puffer) und breiter als V (25 vs 35 = 29 %)
3. **GS Post-Q2-Momentum** (Q2 released 14.07., Umsatz-Beat, chg heute +0,86 % vs SPY +0,39 % Sektor-Outperform)
4. **GS kein Earnings-Blackout in Sicht** (Q3 ~Mitte Oktober) vs V (9 HT weg → Blackout aktivierbar)
5. **XLF-Konzentrations-Check bestanden:** JPM (1.048 = 1,07 %) + GS (9.123 = 9,27 %) = 10,34 % Portfolio, weit unter 30 %-Cap, 2 Positionen ≤ 3-Cap

**Guardrail-Status Post-Fill (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,011 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,249 % (KW29 Tag 3)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,689 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,689 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,386 %                          [INAKTIV]
6. VIX-Filter (>30):          17,16 (Perplexity PM confirmed)        [GRÜN]
7. Earnings-Blackout (3 HT):  UNH V1 381,49 aktiv (letzter Tag)     [GRÜN operativ]
8. Max Käufe KW29:            **2/2 LOCK** (AAPL Mo + GS Mi)         [LOCK]
```

**Sektor-Zusammensetzung Post-Fill (6 Positionen):**
```
XLK: AAPL 9.894 = 10,05 %
XLC: GOOGL 9.469 = 9,62 %
XLF: JPM 1.048 + GS 9.123 = 10.171 = 10,34 %  (2/3 Pos, unter 30 % ✓)
XLV: UNH 10.033 + LLY 9.142 = 19.175 = 19,49 %  (2/3 Pos, unter 30 %)
Cash: 49.670 = 50,49 %  (reichliche Reserve)
Total invested: 49,51 % (unter 80 %-Cap)
```

**Zwingende Watch-Punkte Midday 13:00 ET:**
1. **LLY V1 1.098,38 Puffer +4,04 %** engste Position — RSI 49,90 gekippt, XLV-Tag-7-Trend, Break unter 1.098,38 löst V1-Market-Sell
2. **GS Fill-Day+0 Watch** — V1 1.050,40 +8,57 % noch komfortabel, aber Fill-Day-Drop-Muster (AVGO/MU/GOOGL-Divergenz) beachten
3. **UNH V1 381,49 letzter Tag** — Blackout endet Do 16.07. BMO nach Q2-Release; Puffer +9,58 %
4. **AAPL/JPM Post-Rally-Fortsetzung** — beide V1 komfortabel > +9 % Puffer
5. **GOOGL Fill-Day+7 Rebound-Fortsetzung** — V1 +7,54 % erweitert vs Di +6,15 %

**Datenqualität:**
- Alpaca IEX Live-Trades 09:37-09:42 ET für 5 Positionen + GS + SPY + V + NVDA
- Alpaca 270d Daily-Bars GS (Bar-Count validiert 270) + SPY (270) 2025-06-16 → 2026-07-14 mit adjustment=split — EMA50/EMA200 + Wilder RSI(14) full-history
- Alpaca 1Min Intraday-Bars GS 09:30-09:39 (10 Bars) für K4-Volumen-Extrapolation
- Perplexity K5 GS: 4 unabhängige FwdPE-Quellen + GS-Pressroom Q2-2026-Release Text
- Perplexity K5 NVDA: 3 unabhängige FwdPE-Quellen (Range 20,40-40,78)
- Perplexity K5 V: 6 unabhängige FwdPE-Quellen (Range 21,28-30,15, robust)
- Alpaca account.equity 98.376,40 Post-Fill; last_equity 98.365,51

**ClickUp:** POST /list/{id}/task → HTTP 403 OAuth-023 "Team(s) not authorized" — **neue Fehler-Klasse** vs Di ITEM_246 Tier-Limit HTTP 400. Fallback: **PushNotification an Owner erfolgreich versendet** mit BUY-Details.

**Entscheidung Market Open 15.07.:**
- **KAUF GS 8 Sh @ 1.141,74 GEFÜLLT** (Slot 2/2 KW29 verbraucht, Käufe-LOCK bis Mo 20.07. KW30)
- **NVDA REJECT** (K5-FwdPE Uncertainty 20-41 wie AMD-Muster)
- **V REJECT** (Earnings-Blackout-Risiko in 8 HT nach Kauf, GS besseres Profil)
- **Alle 6 Positionen V1-V6 SICHER**, keine Sell-Order

**Nächste Routine:** Mi 15.07. 13:00 ET Midday Stop-Check (**LLY V1 1.098,38 +4,04 % engste RSI-gekippt-Watch**, GS Fill-Day+0-Muster-Watch, UNH-Blackout letzter Tag, AAPL/JPM/GOOGL Post-Rally-Fortsetzung).

---

## Pre-Market 08:36 ET — 2026-07-15 (Mi, KW29 Tag 3) — Guardrails GRÜN, LLY V1-Puffer +4,97 % engste, UNH-Blackout aktiv bis Do BMO, Slot 2/2 offen für NVDA/V/GS K5-Recheck (GS Q2 Di RELEASED — kein Blackout)

**Alpaca Clock:** is_open=false, next_open Mi 15.07. 09:30 ET (in ~54 Min).

**Account Pre-Market 08:36 ET:**
```
Equity:            98.179,42 $   (Alpaca Live, vs last_equity 98.365,51 → Daily -0,189 %)  [GRÜN]
Cash:              58.804,04 $   (59,89 %, unverändert seit AAPL-Fill Mo)
Portfolio_MV:      39.374,16 $   (40,11 %, AAPL 9.826,07 + JPM 1.035,89 + UNH 9.988,08 + LLY 9.223,92 + GOOGL 9.300,20)
Buying_power:     345.467,23 $
Käufe KW29:        1/2 | Slot 2/2 OFFEN (NVDA/V/GS K5-Recheck aktiv)
Pending Orders:    0 (keine V-Trigger, kein Sell/Limit für heute)
```

**Positionen Live V1-Check (Alpaca 08:36 ET, alle 5 SICHER):**

| Sym    | Curr     | P/L      | vs Close Di | V1-Stop  | V1-Puffer | Status |
|--------|----------|----------|-------------|----------|-----------|--------|
| AAPL   |  316,97  |  +0,04 % |  +0,674 %   | 291,51   | +8,73 %   | SICHER (Fill-Day+2 Rebound) |
| JPM    |  345,30  |  +3,76 % |  +0,871 %   | 306,16   | +12,78 %  | SICHER (Post-Q2-Rally Tag 3) |
| UNH    |  416,17  |  +3,64 % |  -2,251 %   | 381,49⚠  | +9,09 %   | SICHER (Blackout -5 % aktiv, -2,25 % Pre-Market-Drift) |
| LLY    | 1.152,99 |  -3,43 % |  -0,111 %   | 1.098,38 | +4,97 %   | SICHER (**engste**, RSI-Erholung abwarten) |
| GOOGL  |  357,70  |  -2,83 % |  -0,498 %   | 338,65   | +5,63 %   | SICHER (Fill-Day+7) |

**Marktdaten Pre-Market:**
- SPY Live 08:32 ET: **753,46** (vs Di-Close 751,94 = **+0,202 %**)
- VXX letzter Trade Di EOD: 21,48 (Pre-Market thin, keine neue Referenz)
- VIX (Perplexity): **17,16** (weit unter Filter-Schwelle 30) [GRÜN]
- US 10Y Treasury: nicht extrahierbar (Perplexity Date-Bug typisch Pre-Market)
- Makro-Events heute: keine Major-Releases identifiziert (Perplexity leer)
- Top-News heute: keine dominanten Einzel-News Pre-Market

**Guardrail-Status Pre-Market (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,189 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,449 % (KW29 Tag 3, Basis Fr 98.621,81)  [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,886 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,886 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,202 % Pre-Market               [INAKTIV]
6. VIX-Filter (>30):          17,16 (Perplexity confirmed)          [GRÜN]
7. Earnings-Blackout (3 HT):  UNH V1 381,49 aktiv (Q2 Do 16.07. BMO)[GRÜN operativ]
8. Max Käufe KW29:            1/2 → Slot 2/2 OFFEN                   [OFFEN]
```

**Earnings-Blackouts Update (Perplexity + Memory-Cross-Check):**
- **UNH Q2 Do 16.07.2026 BMO CONFIRMED** — Blackout **letzter Tag** heute Mi 15.07., V1 381,49 aktiv (+9,09 % Puffer)
- **JPM Q2 Di 14.07. RELEASED** — kein Blackout mehr, V1 306,16 (-8 %), Puffer +12,78 %
- **GS Q2 Di 14.07. BMO RELEASED** (Perplexity: "14.07.2026 vor Börsenöffnung 7:30 AM ET") — **kein Blackout** für GS-Kauf-Prep, RS_63d +18,55 % ist Post-Q2-Rally-Signal
- LLY Q2 05.08. | GOOGL Q2 22.07. | AAPL Q3 30.07. — alle > 3 HT weg
- NVDA Q2 typisch Aug/Nov — K5-Recheck-Task für Market Open (Blackout-Fenster prüfen)
- V Q3 FY26 typisch Ende Juli — K5-Recheck-Task für Market Open

**Perplexity-Datenqualität-Hinweise:**
- VIX 17,16 einzige verwertbare Live-Zahl (SPY-PM/10Y/Makro/News leer)
- Alpaca IEX SPY 753,46 als Ground-Truth für Pre-Market-Bewegung
- JPM-Earnings-Doppel-Report von Perplexity (JA 16.07.) ist Date-Bug — Memory JPM Q2 Di 14.07. RELEASED (Post-Rally +2,87 %) hat Vorrang
- GS Q2 Datum-Recheck zeigt Di 14.07. BMO → Perplexity-Cross-Bug aufgelöst

**Watchlist Slot 2/2 KW29 (K5-Recheck-Priorität für Market Open 09:30 ET):**
1. **NVDA 211,79** (Close Di) — 3/3 K1-K3 LEAD, K5 zwingend: FwdPE ≤ 35 + RevGrowth ≥ 10 % + Earnings-Blackout-Check
2. **V 356,01** (Close Di) — 3/3 K1-K3 LEAD (K1 +1,41 marginal), K5 zwingend
3. **GS 1141,87** (Close Di) — 3/3 K1-K3 LEAD, K5 zwingend + **Konzentrations-Check vs JPM** (2. XLF-Financial nach LLY+UNH XLV-Cluster-Learning)
4. AMD 548,16 gesperrt (K5 FwdPE > 35 Multi-Source Di-Reject terminal)

**Zwingende Watch-Punkte Market Open 09:30 ET:**
1. **LLY V1 1.098,38 +4,97 % Puffer engste** — Break unter 1.098,38 löst V1-Market-Sell
2. **UNH V1 381,49 Blackout-Puffer +9,09 %** — letzter Tag vor Q2 Do BMO
3. **GOOGL V1 338,65 +5,63 % zweitengste** — Fill-Day+7 Watch
4. **NVDA/V/GS K5-Multi-Source-Recheck** vor Kauf-Order (FwdPE + RevGrowth + Earnings-Blackout + GS-Konzentration)
5. AAPL/JPM Post-Rally-Weiterlauf (V1-Puffer beide > +8 %)

**Entscheidung Pre-Market:**
- **No-Op Positionsseite** (alle 5 V1 SICHER, keine Sell-Order)
- **Kauf-Scan AKTIV bei Market Open 09:30 ET** (Slot 2/2 offen, Guardrails alle GRÜN, keine Crash/VIX-Sperre, kein Weekly-Cap-Trigger)

**ClickUp:** Routine-Log Prio 4 (Low) — fallback PushNotification bei ITEM_246 Tier-Limit.

**Nächste Routine:** Mi 15.07. 09:30 ET Market Open (KW29 Tag 3, NVDA/V/GS K5-Recheck für Slot 2/2, LLY V1-Watch engste, UNH-Blackout-Letzter-Tag).

---

## Market Close 16:02 ET — 2026-07-14 (Di, KW29 Tag 2) — Tagesbilanz, V5/V6 alle SICHER, LLY engste V1 +5,09 % (RSI 49,90 gekippt), Watchlist Mi: NVDA/V/GS 3/3 K1-K3

**Alpaca Clock:** is_open=false, next_open Mi 15.07. 09:30 ET.

**Account Close 16:02 ET:**
```
Equity:            98.399,88 $   (Alpaca Close, vs last_equity 98.562,62 Mo After-Hours-Tick → Daily -0,165 %)  [GRÜN]
Cash:              58.804,04 $   (59,76 %, unverändert seit AAPL-Fill Mo)
Portfolio_MV:      39.595,84 $   (40,24 %, AAPL 9.760,35 + JPM 1.026,96 + UNH 10.218,04 + LLY 9.234,16 + GOOGL 9.346,61)
Buying_power:     346.084,52 $
Käufe KW29:        1/2 (AAPL Mo gefüllt) | Slot 2/2 bleibt OFFEN (AMD K5-Fail dokumentiert, NVDA/V/GS K5-Recheck Mi)
Pending Orders:    0 (alle V5/V6 SICHER, keine Limit-Order für Mi 15.07.)
```

**Positionen Close V1-V6 (Alpaca IEX 280d Bars, EMA/RSI Wilder — 2025-06-01 → 2026-07-14 inkl. Close-Bar):**

| Sym    | Close    | P/L      | Chg_today | V1-Stop  | V1-Puffer | V5 EMA50/200          | V6 RSI  | V6 RS_4w | Status |
|--------|----------|----------|-----------|----------|-----------|-----------------------|---------|----------|--------|
| AAPL   |  314,85  |  -0,63 % |  -0,775 % | 291,51   | +8,01 %   | 296,35/269,80 (+26,54)| 61,97   | +6,81 %  | SICHER |
| JPM    |  342,32  |  +2,87 % |  +2,329 % | 306,16   | +11,81 %  | 320,83/308,07 (+12,75)| 64,76   | +5,56 %  | SICHER (beste, Post-Q2 Tag 2) |
| UNH    |  425,75  |  +6,02 % |  -0,778 % | 381,49⚠  | +11,60 %  | 396,11/348,50 (+47,61)| 58,49   | +2,74 %  | SICHER (Blackout -5 %) |
| LLY    | 1.154,27 |  -3,32 % |  -2,335 % | 1.098,38 | +5,09 %   |1111,06/980,01 (+131,04)| 49,90  | +0,49 %  | SICHER (**engste**, RSI gekippt) |
| GOOGL  |  359,49  |  -2,34 % |  +1,979 % | 338,65   | +6,15 %   | 359,06/312,22 (+46,84)| 49,45   | -1,41 %  | SICHER (Fill-Day+6 Rebound) |

→ **Alle 5 V1-V6 SICHER, keine Sell-Order, keine Limit-Order für Mi. Pending Orders 0.**
→ **LLY neue engste V1-Position +5,09 % Puffer** (RSI(14) auf 49,90 unter 50 gekippt = Momentum-Neutralisierung, XLV -1,92 % Tag 6). Pre-Market-Watch Mi zwingend.
→ **JPM Post-Q2-Rally Tag 2** (chg +2,33 %, P/L jetzt +2,87 % vs Entry, XLF-Outperform +2,11 %) — Blackout-Auslauf-Trade regelkonform alpha-generierend.
→ **GOOGL Fill-Day+6-Rebound** (+1,98 % vs XLC -0,13 % = +2,11 % Outperform) — Muster-Beleg: Fill-Day-Divergenz kann innerhalb 6 HT umkehren.

**Sektor-Performance heute (Alpaca IEX, ranking) — Rotations-Umkehr vs Mo:**
```
XLK +1,274 % (LEAD — Tech-Rebound nach Mo -2,44 % Sell-off)
SPY +0,375 % | XLE +0,370 % | XLF +0,223 % | XLB +0,178 % | XLI +0,044 %
XLU -0,055 % | XLY -0,099 % | XLC -0,125 %
XLRE -0,470 % | XLP -1,389 %
VXX -1,468 % (Vola-Rückgang, VIX ~16 impliziert stabil)
XLV -1,921 %  (Health-Care schwächster Sektor, Tag 6 in Folge)
```
→ **Bot-Impact 5 Positionen aus 4 Sektoren:** JPM XLF-Outperform +2,11 % (Post-Q2), GOOGL XLC-Outperform +2,11 % (Fill-Day+6), AAPL XLK-Underperform -2,05 % (Fill-Day+1 Divergenz trotz Tech-Rally), LLY XLV-Underperform -0,42 % (Sektor + Einzelwert), UNH XLV-Outperform +1,14 % (relative Stärke im schwachen Sektor).
→ **Cluster-Risiko XLV** (LLY + UNH beide im schwächsten Sektor) hat Alpha-Verlust getragen — Konzentrations-Check bei Slot 2/2 Kauf-Entscheidung berücksichtigen.

**Kandidaten-Scan Mi 15.07. Slot 2/2 KW29 (Alpaca 280d, 16 Symbole gescannt):**

| Sym    | Close    | K1 EMA-Spread | K2 RSI  | K3 RS_63d    | K5 Prio     | Verdict |
|--------|----------|---------------|---------|--------------|-------------|---------|
| AMD    |  548,16  | ✓ +155,33     | ✓ 55,22 | ✓ +112,49 %  | ✗ Reject Di | 3/3 K1-K3 aber K5-Fail terminal (FwdPE > 35 Multi-Source Di) |
| NVDA   |  211,79  | ✓ +12,23      | ✓ 56,35 | ✓ +2,30 %    | Recheck     | **3/3 LEAD** (verbessert vs Mo 2/3 durch Chip-Rebound) |
| V      |  356,01  | ✓ +1,41 knapp | ✓ 64,96 | ✓ +5,47 %    | Recheck     | **3/3 LEAD** (K1 marginal, Zahlungssektor-Bewertung K5) |
| GS     | 1141,87  | ✓ +118,64     | ✓ 67,63 | ✓ +18,55 %   | Recheck     | **3/3 LEAD** (Financials-Peer JPM, Konzentrations-Check) |
| CAT    |  933,94  | ✓ +193,66     | ✗ 47,19 | ✓ +8,42 %    | —           | 2/3 K2-Fail (verschlechtert vs Mo 46,87 knapp) |
| TSLA   |  396,17  | ✓ +6,64       | ✗ 47,73 | ✓ +2,79 %    | —           | 2/3 K2-Fail |
| AMZN   |  247,50  | ✓ +8,79       | ✓ 53,23 | ✗ -6,47 %    | —           | 2/3 K3-Fail |
| META   |  661,04  | ✗ -38,91      | ✓ 63,51 | ✗ -5,48 %    | —           | 1/3 FAIL |
| MSFT   |  384,94  | ✗ -40,69      | ✗ 47,54 | ✗ -9,45 %    | —           | 0/3 FAIL |
| MA     |  538,21  | ✗ -19,97      | ✓ 65,59 | ✗ -3,81 %    | —           | 1/3 FAIL |
| AVGO   |  389,09  | ✓ +29,41      | ✗ 49,90 | ✗ -7,13 %    | —           | 1/3 FAIL |
| Rest   | (NFLX, ORCL, COST, CRM, BX) | alle FAIL |

**Zwingende K5-Rechecks Pre-Market Mi 15.07. (3 Kandidaten):**
1. **NVDA 211,79** — Forward P/E ≤ 35 (Perplexity Multi-Source ≥ 3 Quellen), Revenue Growth ≥ 10 % YoY, Earnings-Blackout-Check (NVDA Q2 typisch Aug/Nov — 3-HT-Fenster prüfen)
2. **V 356,01** — Forward P/E (Zahlungssektor typischerweise 25-30, sollte ≤ 35 passieren), Revenue Growth (mittleres +10-12 %), Earnings-Blackout (Q3 FY26 typisch Ende Juli)
3. **GS 1141,87** — Forward P/E (Financials typisch 10-14, sollte weit ≤ 35), Revenue Growth (variabel), Earnings-Blackout **KRITISCH** (GS Q2 hat bereits released?), **JPM-Konzentrations-Check** (2 XLF-Financials nach LLY+UNH XLV-Cluster-Erfahrung)

**Guardrail-Status Market Close (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,165 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,225 % (KW29 Tag 2, Basis Fr 98.621,81) [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,665 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,665 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,375 %                          [INAKTIV]
6. VIX-Filter (>30):          ~16 (VXX 21,48 -1,47 %)               [GRÜN]
7. Earnings-Blackout (3 HT):  UNH V1 381,49 aktiv (Q2 Do 16.07. BMO)[GRÜN operativ, 1 Position -5 % Tightening]
8. Max Käufe KW29:            1/2 → Slot 2/2 bleibt OFFEN            [OFFEN]
```
→ **STATUS: ALLE 8 GRÜN. Weekly Loss Cap -0,225 % weit unter -5 %-Trigger.**

**Entscheidung Market Close:** Regelkonformer **No-Sell** (alle V1-V6 SICHER). **Keine Limit-Order für Mi 15.07.** LLY-Watch-Modus aktiv (engste V1 +5,09 %, RSI gekippt). Slot 2/2 bleibt OFFEN — NVDA/V/GS K5-Multi-Source-Recheck Mi Pre-Market entscheidet.

**Zwingende Watch-Punkte Pre-Market Mi 15.07. 08:30 ET:**
1. **LLY V1-Puffer +5,09 %** engste Position — RSI 49,90 gekippt, XLV-Tag-7-Trend, Break unter 1.098,38 löst V1-Market-Sell
2. **UNH V1 381,49 aktiv** — Blackout bis Do 16.07. BMO, Puffer +11,60 %
3. **NVDA/V/GS K5-Recheck** für Slot 2/2 — Multi-Source-FwdPE + Earnings-Blackout + GS-Konzentrations-Check
4. **AAPL Fill-Day+2** — V1 +8,01 % noch reichlich, XLK-Divergenz-Monitoring
5. **JPM Post-Q2-Momentum Tag 3** — V1 306,16 komfortabel +11,81 %, TP1 399,34 = +16,7 % entfernt

**Datenqualität:**
- Alpaca IEX 280d Bars für 21 Symbole (5 Positionen + SPY + 12 Sektor-ETFs + 16 Screener-Kandidaten, teils überlappend) — EMA50/EMA200 + Wilder RSI(14) full-history
- Latest 1-Min-Bars für alle Positionen ts 2026-07-14T19:59Z = 16:59 UTC / 15:59 ET (letzte reguläre Session-Minute)
- Alpaca Close-Bar-Timestamp 2026-07-14T04:00:00Z (Daily-Bar-Datum-Konvention) — Werte via Close-Feld
- Alpaca account.equity 98.399,88 (Close); last_equity 98.562,62 (Mo After-Hours-Tick)
- SPY IEX Close 751,94 vs Mo-Close 749,13 = +0,375 % (Ground-Truth Alpha-Referenz)
- Perplexity in diesem Close-Run NICHT abgefragt (Alpaca-Daten vollständig für alle Berechnungen, Perplexity Date-Bug-Risiko vermieden — Multi-Source-K5 verschoben auf Pre-Market Mi für die 3 K5-Kandidaten)

**Nächste Routine:** Mi 15.07. 08:30 ET Pre-Market Check — **LLY V1 1.098,38 Watch +5,09 %**, UNH-Blackout weiter aktiv, NVDA/V/GS K5-Recheck für Slot 2/2 KW29.

**ClickUp:** POST /list/{id}/task → HTTP 400 **ITEM_246 Tier-Limit weiter aktiv** (aus Pre-Market/Open carry-over Di). Fallback: **PushNotification an Owner** ausgelöst.

---

## Market Open 09:37 ET — 2026-07-14 (Di, KW29 Tag 2) — Guardrails GRÜN, AMD K5-Reject FwdPE 36-68 > 35, KEIN KAUF, JPM V1-Reset 306,16 post-Q2-Release, LLY/GOOGL neue engste Positionen

**Alpaca Clock:** is_open=true, next_close Di 14.07. 16:00 ET.

**Account Live 09:37 ET:**
```
Equity:            98.281,72 $   (vs Mo-Close 98.587,07 → Daily -0,310 % / vs Alpaca last_eq 98.562,62 → -0,285 %)  [GRÜN]
Cash:              58.804,04 $   (59,83 %, unverändert seit AAPL-Fill Mo 11:31 ET)
Portfolio_MV:      39.477,68 $   (40,17 %, AAPL 9.752,60 + JPM 1.011,36 + UNH 10.335,96 + LLY 9.208,72 + GOOGL 9.172,02)
Buying_power:     345.753,66 $
Käufe KW29:        1/2 (AAPL Mo gefüllt) | Slot 2/2 bleibt OFFEN (AMD K5-Fail)
Pending Orders:    0
```

**Positionen Live V1-Check (Alpaca IEX 09:37 ET):**
| Sym    | Live     | P/L     | Chg_today | V1-Stop        | V1-Puffer | Status |
|--------|----------|---------|-----------|----------------|-----------|--------|
| AAPL   | 314,60   | -0,71 % | -0,904 %  | 291,51         | +7,92 %   | SICHER (Fill-Day+1) |
| JPM    | 337,12   | +1,30 % | **+0,753 %** | **306,16 NEU** (Blackout ENDE) | **+10,11 %** | SICHER (Post-Release-POSITIV, PM-Loss aufgeholt) |
| UNH    | 430,67   | +7,25 % | +0,380 %  | 381,49 (Blackout -5 %) | +12,89 % | SICHER (Blackout bis Do BMO) |
| LLY    | 1.151,09 | -3,58 % | **-2,780 %** | 1.098,38    | **+4,80 %** | SICHER (**neue engste**, XLV Tag 5) |
| GOOGL  | 352,77   | -4,16 % | +0,065 %  | 338,65         | +4,17 %   | SICHER (zweit-engste, Fill-Day+5) |

→ **Alle 5 V1 SICHER, keine Sell-Order, Pending Orders 0.**
→ **JPM Post-Release-Rebound VOLLZOGEN** (PM 326,97 -2,26 % → Live 337,12 +1,30 %). Q2-Release-Reaktion positiv. **V1-Reset 316,14 → 306,16 (-8 %)** durchgeführt nach Call 8:30 AM ET.
→ **LLY / GOOGL neue engste Positionen** (+4,80 % / +4,17 %) — beide V1-Puffer < 5 %, LLY XLV-Verkaufsdruck 5. Tag, GOOGL Fill-Day+5-Divergenz.

**AMD K5 Multi-Source-Recheck (Perplexity 09:38 ET, 5 Datenpunkte):**
- Forward P/E NTM: GuruFocus 35,72 / GuruFocus term-page 36,98 / StockAnalysis 59,82 / MarketBeat 59,82 / ValueInvesting.io 68,65
- Konsens: **~36-68x** — sogar niedrigste Quelle 35,72 > 35 Threshold
- Trailing P/E (12M): 101,79 (GuruFocus) - 173,93 (StockAnalysis) — Hyper-Premium nach +117 % 63d Rally
- Revenue Growth Q4 CY2025: **+34,1 % YoY** (10,27 Mrd $) — K5-Wachstum ✓, aber Bewertung dominiert
- AMD Q2 2026 Earnings: **04.08.2026** (15 HT weg → kein Blackout)
- **Verdikt: K5 FAIL, Kauf regelkonform abgelehnt.**

**Alpaca Bars K1-K4 AMD (259d bis 13.07. Close inkl.):**
- Close Mo 13.07.: 533,69 (Fr 557,85 → -4,33 % Mo, aber heute Live 560,87 = +5,09 % Gap-Up)
- K1 EMA50 474,46 > EMA200 321,46 ✓ (Spread **+153,00**)
- K2 RSI(14) Wilder 52,97 ✓ (50-70 Range)
- K3 RS_63d = AMD +117,81 % - SPY +10,27 % = **+107,54 %** ✓ (dominanter Chip-Rally-Leader)
- K4 Intraday-Vol 09:30-09:37 = 32.126 Sh IEX (extrap. Full-Day ~1,79 M vs Avg20 656.454 = **~2,7× Avg20**) ✓
- **4/5-Signal, K5-FwdPE-Fail regelkonform-terminal**

**Weitere Watchlist-Kandidaten (Rekap):**
- CAT: 2/3 K2-Fail Mo Close (RSI 46,87 knapp unter 50) — kein Rescan im Open (K5-Prio-Reject bei AMD reicht)
- NVDA: 2/3 K3-Fail (RS -2,54 %) — kein Rescan
- TSLA: 2/3 K2-Fail — kein Rescan

**Perplexity Macro Check (09:37 ET Live):**
```
SPY Live:                Alpaca IEX 750,48 → +0,180 % vs Mo-Close 749,13     [POSITIV — Rebound-Tag]
VIX Live:                Perplexity Date-Bug (no Live-Retrieval)
VXX Carry-Over:          Mo-Close 21,79 → VIX ~16-17 impliziert              [GRÜN]
Makro-Events heute:      JPM Q2 2026 Earnings BMO RELEASED (7:00 AM ET Press + 8:30 AM Call)
JPM Result-Detail:       Perplexity Date-Bug — kein indiziertes Transcript/8-K
                         Alpaca Price-Action als Ground-Truth: +0,75 % Post-Release = Positive Reaction
```

**Sonderbeobachtung LLY XLV Tag 5:**
- LLY Live 1.151,09 chg_today -2,780 % → V1-Puffer schmilzt von PM +7,43 % auf +4,80 % (Open)
- XLV-Verkaufsdruck 5. Tag (KW28 Fr XLV -1,77 %, Mo XLV +0,31 % Rebound, aber LLY-eigenwert-schwach)
- Wenn LLY-Trend anhält: V1 1.098,38 könnte innerhalb 1-2 HT gebrochen werden
- Midday-Watch zwingend

**Guardrail-Status Market Open (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,285 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,345 % (KW29 Tag 2, Basis Fr 98.621,81) [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,781 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,781 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY-Live +0,180 %                     [INAKTIV]
6. VIX-Filter (>30):          ~16-17 (VXX 21,79 carry-over)         [GRÜN]
7. Earnings-Blackout (3 HT):  JPM ENDET post-Release, UNH aktiv      [GRÜN operativ, 1 Position -5 %-Tightening]
8. Max Käufe KW29:            1/2 → Slot 2/2 bleibt OFFEN            [OFFEN]
```
→ **STATUS: ALLE 8 GRÜN. Kauf-Fenster war offen, aber AMD K5-Fail → KEIN Kauf.**

**Entscheidung Market Open:** Regelkonformer **No-Buy** (AMD FwdPE > 35 Cap-Verletzung). Alle 5 Positionen SICHER (kein Sell). JPM V1-Reset auf 306,16 durchgeführt. Slot 2/2 KW29 bleibt bis Mi-Fr für neue Signal-Konstellation offen.

**Zwingende Watch-Punkte Midday 13:00 ET:**
1. **LLY V1-Puffer +4,80 %** engste Position — Break unter 1.098,38 löst V1-Market-Sell (XLV-Tag 5 Fortsetzung)
2. **GOOGL V1-Puffer +4,17 %** zweit-engste — Fill-Day+5, Live-Watch
3. **JPM Post-Earnings-Reaction-Fade-Prüfung** (V1 306,16 komfortabel, aber Reaction-Fade nicht ausgeschlossen)
4. **UNH V1 381,49 (Blackout -5 %) SICHER +12,89 %** — Fortsetzung
5. **AAPL Fill-Day+1** — V1 +7,92 % noch reichlich

**Datenqualität:**
- Alpaca IEX Live-Trades 6 Symbole (5 Positionen + AMD + SPY) ts 13:37 UTC = 09:37 ET
- Alpaca Bars AMD 259d 2025-07-01 → 2026-07-13 EMA/RSI/RS (Wilder RSI, adjustment=split) sauber
- Alpaca Bars AMD Intraday 1Min 09:30-09:37 ET für K4 Volume-Extrapolation
- Perplexity K5-AMD 5 Datenpunkte (2 Sources auf GuruFocus divergent 35,72 vs 36,98; StockAnalysis+MarketBeat 59,82; ValueInvesting 68,65 → robuste Reject-Entscheidung)
- Perplexity JPM Q2-Result Date-Bug (Transcript nicht indiziert) → Alpaca-Price-Action-Fallback erfolgreich
- Alpaca account.equity 98.281,72 (Live 09:37); last_equity 98.562,62 (Mo After-Hours-Tick)

**ClickUp:** ITEM_246 Tier-Limit weiter aktiv → Fallback PushNotification an Owner versendet.

**Nächste Routine:** Di 14.07. 13:00 ET Midday Stop-Check (LLY/GOOGL V1-Watch beide < 5 % Puffer, JPM Post-Earnings-Verlauf, UNH-Blackout weiter aktiv).

---

## Pre-Market 08:35 ET — 2026-07-14 (Di, KW29 Tag 2) — Guardrails GRÜN, JPM Q2-Earnings TODAY BMO 7:00 AM ET / 8:30 AM Call, JPM V1-Puffer verengt +3,43 %, UNH-Blackout V1 381,49 aktiv, AMD K5-Recheck für Kauf-Slot 2/2 im Open

**Alpaca Clock:** is_open=false, next_open Di 14.07. 09:30 ET, next_close 16:00 ET. Pre-Market-Session aktiv.

**Account Live 08:35 ET (Pre-Market):**
```
Equity:            98.529,29 $   (vs Mo-Close 98.587,07 → Daily -0,059 %)  [GRÜN]
Cash:              58.804,04 $   (59,68 %, unverändert seit AAPL-Fill Mo 11:31 ET)
Portfolio_MV:      39.725,25 $   (40,32 %, AAPL 9.794,76 + JPM 980,91 + UNH 10.335,36 + LLY 9.440,00 + GOOGL 9.174,88)
Buying_power:     346.446,86 $
Trading_blocked:  false | Status: ACTIVE
Käufe KW29:        1/2 (AAPL Mo gefüllt), Slot 2/2 offen für Kauf-Scan im Open
Pending Orders:    0
last_equity Alpaca: 98.562,62 $  (Mo After-Hours-Tick, +/-25 $ Drift vs Memory Mo-Close, akzeptabel)
```

**Positionen Pre-Market Live (Alpaca 08:35 ET, change_today = vs Mo-Close):**
| Sym    | Live     | P/L     | Chg_today | V1-Stop        | V1-Puffer | Status |
|--------|----------|---------|-----------|----------------|-----------|--------|
| AAPL   | 315,96   | -0,28 % | -0,425 %  | 291,51         | +8,39 %   | SICHER (Fill-Day+1, milder PM-Drift) |
| JPM    | 326,97   | -1,75 % | **-2,260 %** | **316,14** (Blackout) | **+3,43 %** | SICHER (**verengt**, PM-Drift vor Q2 BMO 7:00 AM ET) |
| UNH    | 430,64   | +7,24 % | +0,361 %  | **381,49 NEU** (Blackout -5 %) | +12,88 % | SICHER |
| LLY    | 1.180,00 | -1,16 % | -0,158 %  | 1.098,38       | +7,43 %   | SICHER (XLV-milde) |
| GOOGL  | 352,88   | -4,13 % | +0,105 %  | 338,65         | +4,20 %   | SICHER (**engste** mit JPM verengt, Fill-Day+5) |

→ **Alle 5 V1 SICHER, keine Pre-Market-Trigger, keine Order pending.**
→ **JPM Pre-Market -2,26 % ungewöhnlich (Position-Puffer schmilzt von +5,84 % Mo Close auf +3,43 % PM)** — Pre-Earnings-Positioning-Drift oder Leak. V1 316,14 hält, aber jetzt zweit-engste Position nach GOOGL. **ZWINGENDER Watch bei Market Open + Post-BMO-Release 8:30 AM ET Call.**
→ **UNH V1 381,49 (Blackout -5 %) SICHER +12,88 %** — Aktivierung Mo Close funktioniert wie geplant, Puffer klar reichlich.

**Perplexity Macro Check (Pre-Market Live):**
```
VIX Live 14.07.:         Perplexity Date-in-Future-Bug — kein Live-Wert-Retrieval
                         Suchergebnisse widersprüchlich (15,03-20,95, keine 14.07.-Bestätigung)
SPY Pre-Market Alpaca IEX: mid 752,21 (bid 752,14 / ask 752,27, ts 12:35 UTC)
                          → +0,410 % vs Mo-Close 749,13                             [POSITIV — Rebound-Tag]
VXX Live 08:35 ET:        bid 21,79 (ask 0/leer, thin Pre-Market)                    [~+3,1 % vs Mo, aber unzuverlässig]
                          → VIX ~16-17 impliziert (Mo Close VXX +3,17 % → Vola-Tick blieb)
10Y Treasury:             N/A (Perplexity Date-Bug)
Makro-Events heute:       **JPM Q2 2026 Earnings BMO 7:00 AM ET / Earnings Call 8:30 AM ET CONFIRMED** [JPM IR + Perplexity]
                          Weitere Fed-Speak/CPI/PPI: keine im Perplexity-Retrieval
Top-News:                 Perplexity Date-Bug — keine Live-Bewegungs-News
```

**Sonderfall SPY-PM +0,41 % + JPM Pre-Market -2,26 %:** Marktweiter Rebound, aber JPM-spezifische Schwäche vor eigenem Q2-Release ist auffällig (Pre-Earnings-Skepsis oder De-Risking großer Positionen). Financials-Sektor-Kontext heute wichtig (XLF-Watch im Open).

**Earnings-Blackout-Check (Perplexity Multi-Query 6 Symbole):**
- **JPM Q2 2026: Di 14.07.2026 BMO 7:00 AM ET / Call 8:30 AM ET CONFIRMED** [JPM IR + Perplexity source 1+3]
  - **HEUTE Release-Tag** (0 HT bis Earnings, Mo 13.07. war Vortag)
  - 3-HT-Blackout **AKTIV bis Post-Release 8:30 AM ET Call** → dann Ende
  - V1 316,14 (-5 %) aktiv, PM-Puffer +3,43 % [VERENGT]
  - **Post-Release-Task Di 14.07. Pre-Market: V1 zurück auf -8 % (306,16) nach 8:30 AM Call**
- **UNH Q2 Do 16.07.2026 BMO** — Perplexity nicht bestätigt (Search-Result-Lücke), Memory-Carry-Over Fr 10.07. UNH IR 8 AM ET BMO — **2 HT bis Release** (Di, Mi, Do BMO)
  - 3-HT-Blackout **AKTIV ab Mo 13.07. Close** — V1 381,49 (-5 %) aktiv, Puffer +12,88 %
- **LLY Q2 05.08.2026 BMO** — Perplexity nicht bestätigt (NOT_FOUND), Memory-Carry — 16 HT — weit weg
- **GOOGL Q2 22.07.2026** — Perplexity nicht bestätigt (NOT_FOUND), Memory-Carry — 6 HT — 3-HT-Blackout ab Fr 17.07. Close
- **AAPL Q3 30.07.2026** — Perplexity NOT_FOUND, Memory-Carry — 12 HT — 3-HT-Blackout ab Fr 24.07. Close (fern)
- **AMD Q2 (Kauf-Kandidat):** Perplexity NOT_FOUND → **K5-Multi-Source-Recheck Market Open zwingend** (AMD Q2-Earnings typisch Anfang August, aber Bestätigung via Perplexity + AMD IR im Open ZWINGEND vor Kauf-Order)

→ **JPM = HEUTIGES Release-Ereignis, ansonsten nur UNH-Blackout aktiv.**
→ **Post-JPM-BMO-Update Pre-Market Open ZWINGEND:** V1 316,14 → 306,16 zurücksetzen (nach 8:30 AM Call Release).

**Guardrail-Status Pre-Market (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,059 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,096 % (KW29 Tag 2, Basis Fr 98.621,81) [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,536 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,536 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY-PM +0,410 % (Mo -0,770 %)         [INAKTIV]
6. VIX-Filter (>30):          ~16-17 (VXX 21,79 thin bid)           [GRÜN]
7. Earnings-Blackout (3 HT):  JPM RELEASE TODAY, UNH aktiv           [GRÜN operativ, 2 Positionen -5 %-Tightening]
8. Max Käufe KW29:            1/2 → SLOT 2/2 VERFÜGBAR              [OFFEN]
```
→ **STATUS: ALLE 8 GRÜN, Kauf-Fenster für Market Open 09:30 ET OFFEN.**

**Watchlist KW29 Kauf-Slot 2/2 (Kauf-Fenster ab Market Open 09:30 ET):**
```
Sym    Close Mo    Ranking KW29                                       K5-Recheck Status
AMD    533,69     LEAD-Kandidat 3/3 K1-K3 (RS_63d +107,26 %)          K5 + Earnings-Blackout ZWINGEND im Open
CAT    931,96     Backup 2/3 K2-Fail (RSI 46,87 knapp)                 K2-Recheck im Open
NVDA   203,49     Backup 2/3 K3-Fail (RS -2,54 %)                      RS-Verbesserung watchen
TSLA   394,86     2/3 K2-Fail (RSI 47,30)                              Backup-only
```

→ **Entscheidung Market Open 09:30 ET:** AMD K1-K5-Live-Recheck via Alpaca 259d Bars + Perplexity Multi-Source FwdPE/RevGrowth + AMD-Q2-Earnings-Datum (Blackout-Check zwingend, AMD-Earnings Anfang August typisch). Wenn K5 grün + kein Blackout → Kauf-Order Slot 2/2; sonst kein Kauf.

**Datenqualitäts-Hinweise:**
- Alpaca IEX SPY 752,21 Pre-Market als Ground-Truth
- VXX bid-only 21,79 (ap=0 leer im Pre-Market, thin) → VIX-Referenz aus Mo-Close-Range 16-17 gehalten
- Perplexity Date-in-Future-Bug bei Live-Werten VIX/SPY reproduziert — Alpaca-Fallback erfolgreich
- Perplexity Earnings-Multi-Query: JPM Q2 CONFIRMED BMO 7:00 AM ET / 8:30 AM Call, andere NOT_FOUND (Suchergebnis-Lücke) → Memory-Carry-Over für UNH/LLY/GOOGL/AAPL/AMD genutzt
- Alpaca `equity` 98.529,29 (Live PM); `last_equity` 98.562,62 (Mo After-Hours-Tick -24,45 $ vs Memory Mo-Close 98.587,07)
- Position-Quotes /v2/positions als Pre-Market-Referenz (Alpaca IEX kein STO-PM-Feed)

**ClickUp:** Routine-Log Prio 4 (Low, alle Guardrails GRÜN). Bei Tier-Limit ITEM_246 Fallback auf PushNotification.

**Entscheidung Market Open 09:30 ET:**
- **Kauf-Scan AKTIV** (Slot 2/2 verfügbar, alle Guardrails GRÜN)
- **AMD K1-K5-Live-Recheck** (Alpaca Bars + Perplexity K5 + Earnings-Blackout-Check ZWINGEND)
- **JPM Live-Watch bei < 316,14** → sofort V1-Market-Sell (PM-Puffer nur +3,43 %, zweit-engste)
- **Post-JPM-BMO-Release-Update V1 316,14 → 306,16** nach Earnings-Call 8:30 AM ET (dann Blackout-Ende)
- **GOOGL Live-Watch — engste Position** (V1-Puffer +4,20 %)
- **UNH V1 381,49 hält** (+12,88 % Puffer, Blackout-Aktivierung Mo Close erfolgreich)

**Zwingende Watch-Punkte Market Open:**
1. JPM Q2 Earnings-Release 7:00 AM ET / Call 8:30 AM ET Reaction — Pre-Market-Puffer nur +3,43 %
2. AMD K5 Multi-Source (FwdPE, RevGrowth) + Earnings-Blackout-Check zwingend
3. GOOGL V1 338,65 engste Position (+4,20 % Puffer)
4. Post-JPM-Release V1-Update auf 306,16

**Nächste Routine:** Di 14.07. 09:30 ET Market Open (KW29 Tag 2, **JPM Q2-Earnings-Reaction post-8:30 AM Call**, AMD K5-Scan + Kauf-Entscheidung Slot 2/2, JPM-V1-Post-Release-Update 316,14 → 306,16).

---

## Market Close 16:02 ET — 2026-07-13 (Mo, KW29 Tag 1) — Tagesbilanz, UNH-Blackout AKTIVIERT V1→381,49, Alpha +0,73 % dank AAPL-Outperform vs XLK -2,44 %

**Alpaca Clock:** is_open=false, next_open Di 14.07. 09:30 ET, next_close 16:00 ET.

**Account Close 16:02 ET:**
```
Equity:            98.587,07 $   (Daily -0,036 % vs Alpaca last_equity 98.622,21 Fr-After-Hours)  [GRÜN]
Cash:              58.804,05 $   (59,65 %, unverändert seit AAPL-Fill 11:31 ET)
Portfolio_MV:      39.784,84 $   (40,35 %, AAPL 9.840,74 + JPM 1.003,59 + UNH 10.299,36 + LLY 9.476,72 + GOOGL 9.164,43)
Weekly KW29:       -0,036 %      (Tag 1, Basis Fr-Close 98.621,81)                          [GRÜN]
DD vs ATH:         -1,479 %      (ATH 100.066,47)                                            [GRÜN]
Käufe KW29:        1/2 gefüllt (AAPL 11:31 ET), 1 Slot noch offen bis Fr-Close
Pending Orders:    0             (alle V5/V6 SICHER)
```

**SPY-Ground-Truth:** Alpaca IEX SPY 749,13 vs Fr-Close 754,94 → **-0,770 % Daily**. **Alpha vs SPY = -0,036 % − (-0,770 %) = +0,734 % [DEUTLICH POSITIV]**.

**Positionen Close V1-V6 (Alpaca IEX 259d Bars, EMA/RSI Wilder):**
| Sym    | Close    | P/L      | Chg_today | V1-Stop        | V1-Puffer | V5 EMA-Spread | V6 RSI | V6 RS_4w  | Status |
|--------|----------|----------|-----------|----------------|-----------|---------------|--------|-----------|--------|
| AAPL   |  317,47  |  +0,19 % |  +0,673 % | 291,51 (-8 %)  | +8,90 %   | +24,41        | 64,92  | +5,63 %   | SICHER (Fill-Day+0, V2-Trail 284,58) |
| JPM    |  334,60  |  +0,53 % |  -0,577 % | **316,14 NEU** | +5,84 %   | +12,19        | 59,30  | +5,38 %   | SICHER (Blackout LETZTER Tag) |
| UNH    |  429,04  |  +6,87 % |  +1,064 % | **381,49 NEU** | +12,47 %  | +48,15        | 61,70  | +4,65 %   | SICHER (**Blackout AKTIVIERT**) |
| LLY    | 1.183,95 |  -0,78 % |  -0,336 % | 1.098,38       | +7,79 %   | +128,16       | 56,39  | +0,20 %   | SICHER (XLV +0,31 % Rebound) |
| GOOGL  |  352,54  |  -4,24 % |  -1,316 % | 338,65         | +4,10 %   | +44,89        | 44,02  | -3,31 %   | SICHER (**engste**, Fill-Day+4) |

→ **Alle V1-V6 SICHER.** **KEINE Limit-Order für Di 14.07.**

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLE +3,041 % (LEAD)
XLU +0,683 % | XLF +0,628 % | XLRE +0,574 % | XLP +0,541 % | XLV +0,311 %
XLC -0,022 % | XLB -0,590 % | XLI -0,901 % | XLY -0,986 %
XLK -2,438 %  (Tech-Sell-off)
VXX +3,171 % (Vola-Tick, VIX ~16-17)
```
→ **Klare Defense-Rotation-Tag.** Bot-Positionen: JPM XLF +0,63 % Sektor / -0,58 % Einzelwert (Blackout-Positioning letzter Tag vor Earnings); UNH XLV +0,31 % / UNH +1,06 % Sektor-Winner (Rebound nach 3 Rot-Tagen); LLY XLV / -0,34 % milde Underperformance; **AAPL XLK -2,44 % / +0,67 % = massives +3,11 %-Outperform relativ!** GOOGL XLC -0,02 % / -1,32 % Divergenz.
→ **AAPL 5/5-Kaufsignal validiert** — Fill-Day+0 mit Sektor-Gegenwind ist ein starkes Zeichen; Fill-Day-Drop-Muster (AVGO/MU) durchbrochen.

**⚠ UNH V1-Stop-Tightening AKTIVIERT ab jetzt (Close 16:02 ET):**
- V1 alt (-8 %): 369,44 → V1 **NEU (-5 %): 381,49**
- Gilt bis Q2 Do 16.07.2026 BMO
- Puffer aktuell: 429,04 vs 381,49 = **+12,47 % SICHER**
- Di 14.07. Pre-Market ZWINGEND: UNH < 381,49 → V1-Market-Sell

**⚠ JPM V1-Blackout LETZTER Tag:** V1 316,14 (-5 %), Puffer +5,84 %. Endet Di 14.07. nach Q2-Release (BMO 8:30 AM ET) → V1 zurück auf -8 % (306,16) Mi 15.07. Pre-Market-Update.

**Guardrails Close (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,036 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,036 % (KW29 Tag 1)                 [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,479 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,479 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,770 %                          [INAKTIV]
6. VIX-Filter (>30):          ~16 (VXX +3,17 %)                     [GRÜN]
7. Earnings-Blackout (3 HT):  JPM letzter Tag, UNH AKTIVIERT        [GRÜN operativ, 2 Positionen -5 %-Tightening]
8. Max Käufe KW29:            1/2 (AAPL gefüllt, 1 Slot offen)      [OFFEN]
```

**Weekly Loss Cap Prüfung KW29 Tag 1:**
- Weekly P/L = -0,036 %, weit unter Cap -5 % → **KEIN Trigger**, keine Order-Stornierung, kein ClickUp Critical Alert

**Watchlist Di 14.07. + KW29-Kauf-Prep (Alpaca 259d K1-K3 Screener):**
```
Sym    Close Mo    K1 EMA-Spread    K2 RSI    K3 RS_63d      Verdict
AMD    533,69     ✓ +152,60         ✓ 52,97   ✓ +107,26 %    3/3 LEAD (K5 morgen Pre-Market zwingend)
CAT    931,96     ✓ +196,39         ✗ 46,87   ✓ +7,50 %      2/3 FAIL (K2 knapp)
NVDA   203,49     ✓ +10,56          ✗ 49,93   ✗ -2,54 %      2/3 FAIL
TSLA   394,86     ✓ +1,78           ✗ 47,30   ✓ +2,63 %      2/3 FAIL
META   656,87     ✗                 ✓ 62,83   ✗ -6,17 %      FAIL
AMZN   247,32     ✓ +8,00           ✓ 53,05   ✗ -6,82 %      2/3 FAIL
```

**Watchlist morgen: AMD (3/3 LEAD — Chip-Rally, K5-Recheck), CAT (Backup, K2 knapp Recheck), NVDA (Backup, RS-Watch)**

→ **AMD einziger 3/3-LEAD.** Chip-Rally RS_63d +107 % dominiert. K5-Recheck Multi-Source zwingend:
  - FwdPE ≤ 35 (AMD ist ambitioniert bewertet — Perplexity-Multi-Source oder Fallback ohne Perplexity)
  - RevGrowth ≥ 10 % YoY
  - Earnings-Blackout-Check (AMD Q2 Ende Juli üblich — 3-HT-Blackout-Berechnung)
  - Sektor XLK -2,44 % heute → antizyklischer Entry, aber Kauf-Slot 2/2 verfügbar

**Datenqualitäts-Hinweise:**
- Alpaca IEX 259d Bars vollständig für alle 5 Positionen + 10 Kandidaten (2025-07-01 → 2026-07-13 inkl. heutige Close-Bar)
- EMA50/EMA200 aus vollen 259 Bars (init 50/200), Wilder RSI(14) inkrementell aus 258 Diffs
- 4w-RS: 20-Bar-Return vs SPY analog
- Sektor-ETFs 12/12 erfolgreich Alpaca IEX
- Alpaca `last_equity` 98.622,21 als Fr-Close Ground-Truth (Memory 98.621,81 = -0,40 pre-close-drift, konsistent)
- Perplexity **nicht abgefragt** heute Close (Date-in-Future-Bug carry-over + Alpaca-Bars decken alles Wesentliche)

**Entscheidung Market Close 13.07.:**
- Alle V1-V6 SICHER → keine Sell-Order für Di 14.07.
- **UNH-Blackout-V1-Tightening auf 381,49 (-5 %) AKTIVIERT** — Zwingender Watch-Punkt erfüllt
- **JPM-Blackout-V1 316,14 aktiv letzter Tag** — Endet morgen nach Q2-Release
- **AAPL Fill-Day+0 mit Sektor-Gegenwind erfolgreich** — +0,19 % vs XLK -2,44 %
- **KW29-Kauf-Slot 1/2 verbraucht** (AAPL) — 1 Slot noch offen; AMD als LEAD-Kandidat für Di 14.07.

**Nächste Routine:** Di 14.07. 08:30 ET Pre-Market Check (KW29 Tag 2, **JPM Q2-Earnings-Reaction BMO 8:30 AM ET**, UNH-V1 381,49 aktiv, GOOGL-V1 +4,10 % engste, AMD K5-Recheck für Slot 2/2).

**ClickUp:** [CLOSE] Tagesbilanz Task Prio 4 (Portfolio marginal aber Alpha stark positiv → Priorität Low). Bei Tier-Limit Fallback auf PushNotification.

---

## Market Open 09:37 ET — 2026-07-13 (Mo, KW29 Tag 1) — AAPL 5/5 LEAD, Limit-Buy 316,90 x 31 platziert, NVDA K3-FAIL

**Alpaca Clock:** is_open=true, next_close 13.07. 16:00 ET.

**Account Live 09:37 ET:**
```
Equity:            98.525,80 $   (Daily -0,097 % vs Fr-Close 98.621,81)                 [GRÜN]
Cash:              68.626,60 $   (69,66 %, unverändert)
Portfolio_MV:      29.888,17 $   (30,34 %)
Käufe KW29:        0/2 gefüllt (1 Pending)                                              [OFFEN]
Pending Orders:    1 (AAPL Limit-Buy 316,90 x 31 Day, ID dba7bc05)
Trading_blocked:   false | Status: ACTIVE
```

**SPY-Ground-Truth:** IEX Live 752,99 vs Fr-Close 754,94 → **-0,258 %**. Alpha vs SPY = -0,097 % − (-0,258 %) = **+0,161 %** [leicht positiv].

**Positionen Open (Alpaca 09:37 ET):**
| Sym    | Live     | P/L     | Chg_today | V1-Stop        | V1-Puffer | Status |
|--------|----------|---------|-----------|----------------|-----------|--------|
| JPM    | 334,82   | +0,61%  | -0,49%    | **316,14**     | +5,88 %   | SICHER (Blackout -5 % AKTIV, vorletzter Tag) |
| UNH    | 427,235  | +6,39%  | +0,62%    | 369,44         | +15,65 %  | SICHER (V2 381,89, Blackout-Aktivierung ab Close) |
| LLY    | 1.171,84 | -1,85%  | -1,41%    | 1.098,38       | +6,69 %   | SICHER (XLV-Schwäche 4. Tag intraday verstärkt) |
| GOOGL  | 355,97   | -3,29%  | -0,34%    | 338,65         | +5,12 %   | SICHER (engste, Fill-Day+4) |

→ **Alle 4 V1-V6 SICHER, keine Sell-Order platziert.**

**Kandidaten-Scan Ergebnis (Alpaca 240d Bars + Perplexity K5):**

| Sym  | K1 EMA Spread | K2 RSI  | K3 RS_63d    | K4 Vol*       | K5 FwdPE/RevGrw | Verdict     |
|------|---------------|---------|--------------|---------------|-----------------|-------------|
| **AAPL** | ✓ +21,65  | ✓ 63,57 | ✓ +12,40 %   | ✓ ~172 % pj   | ✓ 31-34 / +17 % | **5/5 LEAD** |
| NVDA | ✓ +10,97      | ✓ 57,00 | ✗ **-0,19 %** | —             | —               | 2/3 FAIL   |
| CAT  | ✓ +180,52     | ✗ **49,65** | ✓ +7,93 %  | —             | —               | 2/3 FAIL   |
| AMZN | ✓ +6,86       | ✓ 51,08 | ✗ **-7,07 %** | —             | —               | 2/3 FAIL   |

*K4 aus 9-min-Extrapolation Vol_ratio 0,04 × (390/9) ≈ 1,72 = 172 % Avg20

**Signal-Nuance:** NVDA-Memory-Erwartung "3/3" widerlegt — Fr-Sprung +4,09 % reichte nicht für 63-Tage-RS-Turnaround. AAPL bleibt einziger 5/5-LEAD, K5 via 3 Perplexity-Quellen konsistent bestätigt.

**K5 AAPL (Perplexity Multi-Source):**
- Forward P/E: 32,45 (GuruFocus) / 34,61 (StockAnalysis) / 31,44 (TIKR) → Konsens ~32,45 → **≤ 35 ✓**
- Umsatzwachstum YoY: +17 % (Q2 FY26 Meldung 30.04.2026, SEC 8-K) → **≥ 10 % ✓**
- Nächstes Earnings: 30.07.2026 17:00 ET → 13 HT weg → 3-HT-Blackout ab Fr 24.07. Close → **HEUTE KEIN Blackout**

**Position-Sizing AAPL (VIX ~15 < 25 → 10 %):**
```
Portfolio-Equity Live 09:37:   98.525,80 $
Budget (10 %):                  9.852,58 $
Prev-Close Fr 10.07. IEX:         315,32 $
Limit (+0,5 %):                   316,90 $
Shares (floor):                       31
Max-Invest:                     9.823,90 $ (9,97 % Portfolio)
```

**Order-Details (Alpaca):**
- Order-ID: **dba7bc05-4c6d-4380-bed8-3e3c4fd842e4**
- Typ: Limit Buy AAPL 31 Sh @ 316,90 $ Day
- Submit: 2026-07-13 09:41:00 ET
- Status: `new` (accepted, working)
- Live-Preis: bid 321,20 / ask 321,48 → gappte +1,93 % über Fr-Close, deutlich über Limit-Cap
- **Kein Sofort-Fill** — regelkonform (Strategie: max +0,5 % über Vortagesschluss = harter Deckel)
- Fill nur bei Intraday-Pullback unter 316,90 möglich; sonst EOD-Expiry

**Guardrail-Status Market Open (alle 8):**
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

**Datenqualitäts-Hinweise:**
- Alpaca IEX 240d Bars für K1-K4 sauber (heutiger Partial-Bar via `end=2026-07-11T00:00:00Z` ausgeschlossen)
- Erste Berechnung inklusive Partial-Bar hatte Signale verzerrt (AAPL prev_close fälschlich 321,12 statt korrekt 315,32) — Fix durch expliziten End-Cutoff
- Perplexity K5 AAPL: 3 unabhängige Quellen für FwdPE, SEC 8-K für RevGrowth — Date-in-Future-Bug diesmal umgangen
- SPY Alpaca IEX 752,99 als Ground-Truth für Alpha

**ClickUp:** Weiter Tier-Limit ITEM_246 → Push-Notification als Fallback.

**Entscheidung Market Open:**
- **AAPL Limit-Buy 31 x 316,90 Day platziert** — regelkonformer max-0,5%-Deckel; kein Sofort-Fill bei Live 321,40; Fill-Wahrscheinlichkeit hängt an Intraday-Pullback
- **Keine Sell-Order** — alle 4 V1-V6 SICHER
- Kauf-Slot KW29 operativ bei 1/2 (Pending zählt bis Fill/Expiry)

**Nächste Routine:** Mo 13.07. 13:00 ET Midday Stop-Check (AAPL-Fill-Check, JPM-Blackout-V1-Watch, GOOGL/LLY-Live-Watch, UNH-Blackout-Vorbereitung).

---

## Pre-Market 08:35 ET — 2026-07-13 (Mo, KW29 Tag 1) — Guardrails GRÜN, JPM V1 316,14 SICHER, Kauf-Slot 2/2 verfügbar, NVDA/AAPL K5-Recheck im Open

**Alpaca Clock:** is_open=false, next_open Mo 13.07. 09:30 ET, next_close 16:00 ET. Pre-Market-Session aktiv.

**Account Live 08:35 ET (Pre-Market):**
```
Equity:            98.587,61 $   (vs last_equity 98.622,21 = Fr After-Hours-Tick → Daily -0,035 %)  [GRÜN]
Cash:              68.626,60 $   (69,61 %, unverändert)
Portfolio_MV:      29.961,01 $   (30,39 %, JPM 1.013,40 + UNH 10.218,96 + LLY 9.480,19 + GOOGL 9.248,46)
Buying_power:     358.397,22 $
Käufe KW29:        0/2 → SLOT VERFÜGBAR (LOCK-KW28 endete Fr Close)
Pending Orders:    0
Trading_blocked:   false | Status: ACTIVE
last_equity Alpaca: 98.622,21 $ (Fr After-Hours-Tick +0,40 $ vs Memory Fr-Close 98.621,81 — akzeptabel)
```

**Positionen Pre-Market Live (Alpaca 08:35 ET, change_today = vs Fr-Close):**
| Sym    | Live     | P/L     | Chg_today | V1-Stop        | V1-Puffer | Status |
|--------|----------|---------|-----------|----------------|-----------|--------|
| JPM    | 337,80   | +1,51%  | +0,40%    | **316,14**     | +6,84 %   | SICHER (Blackout -5 % AKTIV, JPM 337,80 > 316,14) |
| UNH    | 425,79   | +6,03%  | +0,28%    | 369,44         | +15,25 %  | SICHER (V2 381,89, Blackout-Aktivierung ab Close) |
| LLY    | 1.185,02 | -0,74%  | -0,30%    | 1.098,38       | +7,89 %   | SICHER (XLV-Schwäche 4. Tag milder) |
| GOOGL  | 355,71   | -3,37%  | -0,41%    | 338,65         | +5,03 %   | SICHER (engste, Fill-Day+4 Verengung vs Fr +5,19 %) |

→ **Alle 4 V1 SICHER, keine Pre-Market-Trigger, keine Order pending.**
→ **JPM ex-Blackout 316,14 SICHER** (+6,84 % Puffer, kein Break-Under). Zwingender Watch-Punkt erfüllt.
→ **GOOGL-Verengung Fill-Day+4:** V1-Puffer schmilzt weiter von +5,19 % (Fr) auf +5,03 % (Mo PM) — engste Position, aber SICHER; Watch Open + Midday.

**Perplexity Macro Check (Pre-Market Live):**
```
VIX Fr-Close 10.07.:      15,03 (Perplexity-Snippet)                                → GRÜN (< 30)
VIX Live 13.07.:          Perplexity Date-in-Future-Bug, keine Live-Wert-Retrieval
SPY Pre-Market Alpaca IEX: mid 751,62 (bid 751,57 / ask 751,67)
                          → -0,440 % vs Fr-Close 754,94                             [moderat risk-off]
VXX Live 08:35 ET:        mid 21,17 (bid 20,58 / ask 21,75, breite Spread)
                          → -0,014 % vs Fr-Close 21,13 → flat, kein Vola-Spike     [VIX-Proxy GRÜN]
10Y Treasury:             N/A (Perplexity Date-Bug)
Makro-Events heute:       Perplexity keine Live-Retrieval; Reguläres FOMC-Blackout-Fenster (kein Fed-Speak vor 30.07. Meeting laut Memory-Carry-over)
Top-News:                 Perplexity Date-Bug — keine Live-News verfügbar
```

**Sonderfall SPY-PM -0,44 % + VXX flat:** moderat risk-off, aber weit unter Crash-Filter-Schwelle (SPY > -2 %). VXX-Spread breit (20,58/21,75) impliziert Illiquidität Pre-Market — VIX-Referenz stabil aus Fr-Close 15,03.

**Earnings-Blackout-Check (Perplexity 13.07. Multi-Query 8 Symbole):**
- **JPM Q2 2026: Di 14.07.2026 BMO CONFIRMED** [CNBC + Public.com + WallStreetHorizon]
  - 1 HT bis Earnings (Mo 13.07. = Vortag, Di 14.07. = Release-Tag)
  - 3-HT-Blackout **AKTIV weiter** (Do 09.07. Close → Di 14.07. BMO)
  - V1 316,14 (-5 %) SICHER (+6,84 % Puffer)
  - **Auslauf morgen nach Release** → V1 zurück auf -8 % (306,16)
- **UNH Q2 16.07.2026 BMO** — Perplexity-Suchergebnisse liefern für UNH KEIN explizites Datum im Fenster (Suchergebnis-Lücke), Memory-Carry-Over Fr 10.07. bestätigt UNH IR 8 AM ET BMO Do 16.07. → Blackout-Aktivierung **ab Mo 13.07. Close** ZWINGEND.
  - V1-Tightening auf -5 % vom Entry (401,57 × 0,95 = **381,49 $**, statt aktueller 369,44)
  - Mo 13.07. PM 425,79 → geplanter Puffer +11,63 % Close
- **LLY Q2 05.08.2026 BMO** — Perplexity NOT_SOON → 17 HT — weit weg
- **GOOGL Q2 22.07.2026** — Perplexity NOT_SOON → 7 HT → 3-HT-Blackout ab Fr 17.07. Close (nächste Woche) → **HEUTE NICHT AKTIV**
- **NVDA / AAPL / CAT / AMZN** (Watchlist) — Perplexity NOT_SOON → KEIN Blackout im 3-HT-Fenster → K5-Recheck Kauf möglich

→ **Nur JPM-Blackout aktiv heute** (V1 316,14, SICHER, Auslauf Di 14.07. BMO).
→ **Zwingender Watchpunkt Mo 13.07. Close:** UNH-Blackout-Aktivierung → V1 auf -5 % (381,49) ZWINGEND.

**Guardrail-Status Pre-Market (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,035 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,035 % (KW29 Tag 1, Basis Fr 98.621,81) [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,479 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,479 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY-PM -0,44 % (Fr +0,451 %)          [INAKTIV]
6. VIX-Filter (>30):          ~15,03 Fr-Close (VXX flat 21,17)      [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIV (V1 316,14 SICHER)          [GRÜN operativ]
8. Max Käufe KW29:            0/2 → SLOT VERFÜGBAR                  [OFFEN]
```
→ **STATUS: ALLE 8 GRÜN, Kauf-Fenster für Market Open 09:30 ET OFFEN.**

**Watchlist KW29 Kauf-Prep (Kauf-Fenster ab Market Open 09:30 ET):**
```
Sym    Close Fr    Ranking KW29                                       K5-Recheck Status
NVDA   210,99     LEAD-Kandidat +4,09 % Fr-Sprung — 3/3 K1-K3        K5 zwingend im Open
AAPL   315,32     LEAD-Kandidat -0,266 % Fr — 3/3 K1-K3               K5 zwingend im Open
CAT    951,67     Backup — 2/3 K2-Fail RSI 48,93                     K2-Recheck im Open
AMZN   245,35     Backup — 2/3 K2-Fail, K1-Spread eng                Backup-only
```
→ **Entscheidung Market Open 09:30 ET:** NVDA/AAPL K1-K5-Live-Recheck via Alpaca-Bars + Perplexity Multi-Source FwdPE/RevGrowth → besten LEAD kaufen (max. 1 aus XLK, keine Doppel-Position), 2. Slot für spätere Woche behalten.

**Datenqualitäts-Hinweise:**
- Alpaca IEX SPY 751,62 Pre-Market als Ground-Truth (Perplexity Date-in-Future-Bug bei Live-Werten reproduziert)
- Alpaca Position-Quotes /v2/positions als beste Pre-Market-Referenz (IEX-STO führt kein volles Pre-Market)
- VXX 21,17 mit breiter Spread (20,58/21,75) impliziert Pre-Market-Illiquidität — VIX-Referenz Fr-Close 15,03
- Perplexity Earnings-Multi-Query: JPM CONFIRMED, UNH-Suchergebnis-Lücke (Memory-Carry-Over Fr genutzt), alle anderen NOT_SOON
- Alpaca last_equity 98.622,21 vs Memory Fr-Close 98.621,81 (+0,40 After-Hours-Tick, akzeptabel)

**ClickUp:** Task-Anlage versucht (ITEM_246 Tier-Limit-Fallback auf Push-Notification möglich, siehe Routine-Reply).

**Entscheidung Market Open 09:30 ET:**
- **Kauf-Scan AKTIV** (Slot 2/2 verfügbar, alle Guardrails GRÜN)
- **NVDA + AAPL K1-K5-Live-Recheck** (Alpaca 63d-RS, Wilder-RSI, EMA50/200; Perplexity K5 FwdPE ≤ 35 + RevGrowth ≥ 10 %)
- **JPM Live-Watch** bei < 316,14 → sofort V1-Market-Sell (Puffer PM +6,84 %)
- **GOOGL Live-Watch** — Fill-Day+4 Verengung (V1-Puffer +5,03 %, weiter engste)
- **LLY Live-Watch** — 4. XLV-Schwäche-Tag; V1 +7,89 % Puffer noch reichlich

**Nächste Routine:** Mo 13.07. 09:30 ET Market Open (KW29 Tag 1, NVDA/AAPL K5-Scan + Kauf-Entscheidung, JPM V1-Watch 316,14).

---

## Market Close 16:02 ET — 2026-07-10 (Fr, KW28 Tag 5) — Tagesbilanz, alle V1-V6 SICHER, KEINE Pending-Order für Mo, KW28 abgeschlossen

**Alpaca Clock:** is_open=false, next_open Mo 13.07. 09:30 ET, next_close 16:00 ET.

**Account Close 16:02 ET:**
```
Equity:            98.621,81 $   (Daily -0,374 % vs Memory Do-Close 98.992,13)   [GRÜN]
Cash:              68.626,60 $   (69,59 %, unverändert)
Portfolio_MV:      29.993,80 $   (30,41 %)
Weekly KW28:       -0,803 %      (Mo-Basis 99.420,34)                            [GRÜN]
DD vs ATH:         -1,444 %      (ATH 100.066,47)                                [GRÜN]
Käufe KW28:        2/2 → LOCK-Ende Fr Close, Kauf-Slot ab Mo 13.07. neu
Pending Orders:    0             (V5/V6 alle SICHER)
last_equity Alpaca: 99.060,07 $ (Do After-Hours-Tick — Memory Do-Close Ground-Truth)
```

**SPY-Ground-Truth:** Alpaca IEX SPY 754,94 vs Do-Close 751,55 → **+0,451 % Daily**. Alpha vs SPY = -0,374 % − 0,451 % = **-0,825 %** [NEGATIV].

**Positionen Close V1-V6 (Alpaca IEX 210d Bars, EMA/RSI Wilder inkrementell):**
| Sym    | Close    | P/L     | Chg_today | V1-Stop        | V1-Puffer | V5 Spread | V6 RSI  | Status |
|--------|----------|---------|-----------|----------------|-----------|-----------|---------|--------|
| JPM    | 336,38   | +1,08%  | +0,29%    | **316,14 NEU** | +6,02 %   | +11,05    | ~62     | SICHER (Blackout -5 % AKTIV) |
| UNH    | 424,57   | +5,73%  | -1,64%    | 369,44         | +12,98 %  | +54,07    | ~64     | SICHER (V2 381,89 hält) |
| LLY    | 1188,57  | -0,45%  | -2,23%    | 1.098,38       | +7,59 %   | +112,16   | ~60     | SICHER (schwächste Tages-Bewegung, XLV-Verlierer) |
| GOOGL  | 357,17   | -2,97%  | -0,48%    | 338,65         | +5,19 %   | +41,27    | ~47     | SICHER (engste, Fill-Day+3 Divergenz zu XLC) |

→ **Alle V1-V6 SICHER.** **KEINE Limit-Order für Mo 13.07.** Pending Orders bleiben 0.

**Sektor-Performance heute (Alpaca IEX, ranking):**
```
XLB +1,193 % | XLP +1,100 % | XLC +0,968 % | XLU +0,632 % | XLE +0,502 % | XLRE +0,498 %
XLI +0,472 % | XLF +0,306 % | XLY +0,278 % | XLK +0,267 %
XLV -0,780 %  (einziger roter Sektor — Rotations-Verlierer 3. Tag)
VXX -2,221 % (Vola-Entspannung fortgesetzt, VIX ~15-16 GRÜN)
```
→ **XLV-Rotation-raus 3. Tag in Folge (Fr -0,78 %, Do -0,10 %, Mi -1,34 %)** — Bot-Portfolio strukturell benachteiligt durch 2×XLV-Overweight.
→ Bot-Sektor-Beteiligung: JPM XLF konsistent (+0,29 % vs Sektor +0,31 %), UNH+LLY XLV Rotation-Verlierer, GOOGL divergiert zu XLC (-0,48 % vs +0,97 %) → Fill-Day+3.
→ **XLK +0,27 % mild — aber NVDA +4,09 % Sprung! AAPL -0,27 % underperformt.** KW29-Watchlist-Momentum-Shift.

**Watchlist-Kandidaten Close-Bewegung Fr:**
```
Sym    Close Fr    Chg Fr        Ranking KW29 (Mo 13.07. Kauf-Slot)
NVDA   210,99     +4,092 %      LEAD-Kandidat — 3/3 K1-K3 grenzwertig RS, aber massiver Tages-Sprung, K5-Recheck Mo Pre-Market
AAPL   315,32     -0,266 %      LEAD-Kandidat — 3/3 K1-K3 (RS +10,33 % carry-Mi), aber underperformt heute
CAT    951,67     +1,461 %      Backup — 2/3 K2-Fail RSI 48,93; XLI-Rebound heute
AMZN   245,35     -0,652 %      Backup — 2/3 K2-Fail, K1-Spread eng
```
→ **KW29-LEAD-Ranking neu geordnet:** NVDA und AAPL auf Augenhöhe — K5-Multi-Source-Recheck beider Mo 13.07. Pre-Market entscheidet.

**Watchlist morgen (= Mo 13.07. KW29 Tag 1):** NVDA (LEAD-Kandidat +4,09 % Sprung), AAPL (LEAD-Kandidat, underperformt heute), CAT (Backup, K2 Recheck), AMZN (Backup)

**Guardrails Close (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,374 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,803 %                              [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,444 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,444 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,451 %                          [INAKTIV]
6. VIX-Filter (>30):          ~15-16 (VXX -2,221 %)                 [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIV (V1 316,14 SICHER)          [GRÜN operativ]
8. Max Käufe KW28:            2/2 → LOCK-Ende Fr, KW29 neu 2/2      [KW29 Slot verfügbar]
```

**⚠ Earnings-Blackout-Vorbereitung Mo 13.07. Close ZWINGEND:**
- **JPM Q2 14.07.2026 BMO** — Blackout weiter aktiv (V1 316,14, +6,02 % Puffer, 2 HT bis Earnings)
- **UNH Q2 16.07.2026 BMO** — 3-HT-Blackout aktivierbar **ab Mo 13.07. Close** → V1-Stop-Tightening auf -5 % vom Entry (401,57 × 0,95 = **381,49 $**, statt heutiger 369,44). Fr 10.07. Close 424,57 → geplanter Puffer +11,29 %. **Close-Routine Mo 13.07. Aktivierungs-Task**.
- **LLY Q2 05.08.2026 BMO** — 17 HT — weit weg
- **GOOGL Q2 22.07.2026** — 7 HT — 3-HT-Blackout ab Fr 17.07. Close (nächste Woche)

**Weekly Loss Cap Prüfung KW28 abgeschlossen:**
- Weekly P/L Fr Close = -0,803 % (Mo-Basis 99.420,34 → Fr-Close 98.621,81 = -798,53 $)
- Cap-Trigger -5 %: **NEIN**, weit unter Schwelle
- KEINE Pending-Order zu stornieren (bereits 0)
- KEIN WEEKLY_CAP-Alert ClickUp

**KW28-Wochenperformance-Zusammenfassung (für lessons-learned):**
- Depot Start 99.420,34 $ (Mo 06.07.) → Ende 98.621,81 $ (Fr 10.07.)
- Wochenergebnis: **-0,803 %** (-798,53 $)
- SPY-Vergleich: 744,86 (Do 02.07. carry-over Mo-Basis KW28) → 754,94 (Fr 10.07.) = **+1,353 %**
- Alpha KW28: **-2,156 %** [DEUTLICH NEGATIV]
- Käufe KW28: 2 (LLY Mo, GOOGL Di) — beide gerade so über Wasser (LLY -0,45 %, GOOGL -2,97 %)
- Verkäufe: 1 (MU V1 Di 07.07., -1.019,43 $ realisiert)
- Sektor-Kontext: XLV 3-Tages-Rotation-raus (Mi-Fr) + XLK-Aufholrally ohne Bot-Exposure = Alpha-Miss strukturell
- **Weekly Review Fr 17:00 ET fällig** (routines/weekly-review-routine.md)

**Entscheidung Market Close 10.07.:**
- Alle V1-V6 SICHER → keine Sell-Order für Mo 13.07.
- KEIN Kauf-Slot verwendet (Slot LOCK 2/2 KW28 abgeschlossen)
- **UNH-Blackout-V1-Tightening auf 381,49 ZWINGEND vorzubereiten für Close-Routine Mo 13.07.**
- **NVDA/AAPL K5-Recheck Mo Pre-Market ZWINGEND** für Kauf-Entscheidung
- Watchlist-Momentum-Shift: NVDA sprang, AAPL underperformt → K5-Recheck entscheidend

**Nächste Routine:** Fr 10.07. 17:00 ET Weekly Review (KW28 Bilanz + lessons-learned Update).
**Danach:** Mo 13.07. 08:30 ET Pre-Market Check (KW29 Tag 1).

**ClickUp:** [CLOSE] Tagesbilanz Task Prio 3 (Portfolio -0,374 % + Alpha -0,825 % → Priorität Normal).

---

## Market Open 09:37 ET — 2026-07-10 (Fr, KW28 Tag 5) — No-Op, alle V1 SICHER, Kauf-Scan SKIPPED (Slot LOCK 2/2)

**Alpaca Clock:** is_open=true, next_close 10.07. 16:00 ET.

**Account Live 09:37 ET:**
```
Equity:            98.675,68 $   (Daily -0,320 % vs Memory Do-Close 98.992,13)   [GRÜN]
Cash:              68.626,60 $   (69,55 %, unverändert)
Portfolio_MV:      30.058,10 $   (30,46 %)
Buying_power:     358.643,82 $
Weekly KW28:       -0,749 %       (Mo-Basis 99.420,34)                            [GRÜN]
DD vs ATH:         -1,390 %       (ATH 100.066,47)                                [GRÜN]
Käufe KW28:        2/2 → LOCK bis Mo 13.07.                                       [GESPERRT]
Pending Orders:    0
Trading_blocked:   false | Status: ACTIVE
last_equity Alpaca: 99.060,07 $ (After-Hours-Tick — Memory Do-Close als Ground-Truth)
```

**SPY-Ground-Truth:** Alpaca IEX SPY 752,955 vs Do-Close 751,55 → **+0,187 % Live**. Alpha = -0,320 % − 0,187 % = **-0,507 %** [NEGATIV].

**Positionen Live V1-Check (Alpaca /v2/positions):**
| Sym    | Live      | P/L     | Chg_today | V1-Stop         | V1-Puffer | Status |
|--------|-----------|---------|-----------|-----------------|-----------|--------|
| JPM    | 337,75    | +1,49%  | +0,68%    | **316,14 NEU** | +6,84 %   | SICHER (Blackout -5 % AKTIV) |
| UNH    | 427,58    | +6,48%  | -0,95%    | 369,44          | +15,74 %  | SICHER (V2 381,89 hält) |
| LLY    | 1188,25   | -0,47%  | -2,36%    | 1.098,38        | +8,18 %   | SICHER (schwächste Tages-Bewegung) |
| GOOGL  | 356,805   | -3,07%  | -0,58%    | 338,65          | +5,08 %   | SICHER (engste, Fill-Day+3 Verengung) |

→ **Alle 4 V1 SICHER, keine Sell-Order platziert.** V2-V6 carry-over von Do-Close, keine Neuberechnung nötig (kein neues Posit-Hoch heute, kein V5-Break, V6 alle mit RSI << 80).

**Kauf-Scan SCHRITT 3–5 SKIPPED wegen Käufe-Slot LOCK 2/2:**
- Guardrail-Prüfung Schritt 2 hat 2/2-Käufe-Cap als NEIN identifiziert → Routine schreibt gemäß Regel nur Log, Rest fertig.
- Regelkonform: kein Perplexity-Sektor-Query, kein K1-K5-Recheck der Watchlist, keine Position-Sizing-Berechnung, keine Limit-Order.

**Guardrails Open (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,320 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,749 %                              [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,390 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,390 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,187 % Live                     [INAKTIV]
6. VIX-Filter (>30):          ~16 (VXX 21,43, -2,72 % vs Do)        [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIV (V1 316,14 SICHER)          [GRÜN operativ]
8. Max Käufe KW28:            2/2 → LOCK bis Mo 13.07.              [GESPERRT]
```
→ **STATUS: 7/8 GRÜN + 1 SLOT-LOCK.** Guardrails erlauben Handel, aber Käufe-Slot blockiert.

**Watchlist KW29-Prep (carry-over Do-Close, unverändert):**
```
AAPL  LEAD — 3/3 K1-K3 (RS +10,33 %, RSI 62,81)      XLK Do +2,16 % validiert Sektor-Timing
NVDA  NEU 2. XLK-Kandidat — 3/3 grenzwertig RS       XLK-Rebound-Bestätigung
CAT   Backup — 2/3 K2-Fail RSI 48,93                 K3 stärkstes RS +17,69 %
AMZN  Backup — 2/3 K2-Fail, K1-Spread eng            XLY Do +1,35 % positiv
```
→ Ranking KW29: **AAPL LEAD** / **NVDA 2. XLK** / **CAT/AMZN Backup**. K5-Recheck AAPL/NVDA zwingend am Mo 13.07. Pre-Market.

**Datenqualität:**
- Alpaca `equity` 98.675,68 = Live 09:37. `last_equity` 99.060,07 ist Overnight-After-Hours-Tick — Memory Do-Close 98.992,13 als Ground-Truth (Konvention).
- SPY Alpaca IEX 752,955 Live vs 751,55 Do-Close (Ground-Truth).
- Alle 4 Position-Quotes /v2/positions Cross-Check mit /v2/stocks/trades/latest — konsistent.
- Keine Perplexity-Queries (Slot-LOCK → kein Sektor/K5-Scan nötig).

**Entscheidung Market Open 09:37 ET:**
- **No-Op** — alle V1-V6 SICHER, keine Sell-Order platziert.
- **Kauf-Scan SKIPPED** wegen Käufe-Slot LOCK 2/2 bis Mo 13.07.
- **JPM V1-Blackout 316,14 SICHER** (+6,84 % Puffer).
- **GOOGL Fill-Day+3-Verengung fortgesetzt** (+5,08 % Puffer, weiter engste Position) — Watch Midday.
- **LLY -2,36 % Tages-Schwäche** — XLV-Rotation raus setzt sich fort, V1 +8,18 % noch reichlich.
- **Alpha -0,507 %** durch LLY/GOOGL-Schwäche.

**Nächste Routine:** Fr 10.07. 13:00 ET Midday Stop-Check.

**ClickUp:** ITEM_246 Tier-Limit carry-over aus Pre-Market → Push-Notification als Fallback.

---

## Pre-Market 08:35 ET — 2026-07-10 (Fr, KW28 Tag 5) — Guardrails GRÜN, JPM V1 316,14 SICHER, KEIN Kauf-Scan (Slot LOCK 2/2)

**Alpaca Clock:** is_open=false, next_open Fr 10.07. 09:30 ET, next_close 16:00 ET. Pre-Market-Session aktiv.

**Account Live 08:35 ET (Pre-Market):**
```
Equity:            99.047,72 $   (vs Do-Close 98.992,13 → Daily +0,056 %) [GRÜN]
Cash:              68.626,60 $   (69,29 %, unverändert)
Portfolio_MV:      30.421,12 $   (30,71 %, JPM 1.012,50 + UNH 10.389,12 + LLY 9.757,52 + GOOGL 9.261,98)
Buying_power:     359.685,54 $
Trading_blocked:  false | Status: ACTIVE
Käufe KW28:        2/2 → LOCK bis Mo 13.07.
Pending Orders:    0
last_equity Alpaca: 99.060,07 $ (After-Hours-Tick +67,94 vs Memory Do-Close 98.992,13 — akzeptabel)
```

**Positionen Pre-Market Live (Alpaca 08:35 ET, change_today = vs Do-Close):**
| Sym    | Live     | P/L     | Chg_today | V1-Stop        | V1-Puffer | Status |
|--------|----------|---------|-----------|----------------|-----------|--------|
| JPM    | 337,50   | +1,42%  | +0,61%    | **316,14 NEU** | +6,76 %   | SICHER (Blackout -5 % AKTIV, kein Break) |
| UNH    | 432,88   | +7,80%  | +0,28%    | 369,44         | +17,17 %  | SICHER (Posit-Hoch 434,19 nicht erreicht) |
| LLY    | 1.219,69 | +2,16%  | +0,23%    | 1.098,38       | +11,05 %  | SICHER |
| GOOGL  | 356,23   | -3,22%  | -0,74%    | 338,65         | +5,19 %   | SICHER (engste, Fill-Day+3 Verengung von +5,97 %) |

→ **Alle 4 V1 SICHER, keine Pre-Market-Trigger, keine Order pending.**
→ **JPM ex-Blackout 316,14 SICHER** (+6,76 % Puffer, kein Break-Under). Zwingender Watch-Punkt erfüllt.
→ **GOOGL-Verengung Fill-Day+3:** V1-Puffer schmilzt weiter von +5,97 % (Do) auf +5,19 % (Fr Pre-Market) — engste Position, aber SICHER; Watch für Open + Midday.

**Perplexity Macro Check (Pre-Market Live):**
```
VIX Live 10.07. (Snippet): 16,79 (-0,65 %) [tradingeconomics]                    → GRÜN (< 30)
VIX Prior Close 09.07.:    16,90 [wsj/cnbc]
SPY Pre-Market Alpaca IEX: mid 751,39 (bid 751,30 / ask 751,48)
                          → -0,021 % vs Do-Close 751,55                          → nahe flat
VXX Live 08:35 ET:         mid 22,54 (bid 21,59 / ask 23,49, wide spread)
                          → +2,32 % vs Do-Close 22,03 impliziert leichten Vola-Tick
10Y Treasury:              N/A (Perplexity keine Live-Yield)
Makro-Events heute:        Perplexity meldet KEINE Mega-Daten (kein Fed-Speak, kein CPI/PPI/NFP)
Top-News:                  keine spezifischen Marktbewegungs-Headlines (Perplexity search-result-lite)
```

**Sonderfall SPY vs VIX:** SPY-Premarket flat -0,02 % + VIX ~16,79 stabil → neutral pre-open. BEIDES weit von Guardrail-Schwellen (SPY > -2 %, VIX < 30).

**Earnings-Blackout-Check (Perplexity 10.07. Multi-Query):**
- **JPM Q2 2026: Di 14.07.2026 BMO 8:30 AM ET CONFIRMED** [Yahoo Finance + MarketBeat + WallStreetHorizon + JPM IR]
  - 3 HT bis Earnings (Fr 10.07., Mo 13.07., Di 14.07.)
  - 3-HT-Blackout **AKTIV** ab Do 09.07. Close → V1 auf -5 % (316,14) → **BLEIBT AKTIV** bis Q2-Release
  - Pre-Market 337,50 > 316,14 → +6,76 % Puffer SICHER
- **UNH Q2 2026: Do 16.07.2026 BMO 8:00 AM ET CONFIRMED** [UNH IR + Perplexity Multi-Source; Perplexity-Label „AMC" ist Fehler — 8 AM ET ist BMO]
  - 4 HT bis Earnings (Fr 10.07., Mo 13.07., Di 14.07., Mi 15.07., Do 16.07.)
  - 3-HT-Blackout aktivierbar ab **Mo 13.07. Close** → **HEUTE NICHT AKTIV**
  - Zwingender Watch: UNH-Stop-Tightening V1 → -5 % ab Mo 13.07. Close (Berechnung 401,57 × 0,95 = 381,49 $ — statt heutiger 369,44)
- **LLY Q2 2026: 05.08.2026 BMO** carry-over → 18 HT → weit weg [NOT_SOON confirmed]
- **GOOGL Q2 2026: 22.07.2026** carry-over → 8 HT → 3-HT-Blackout ab 17.07. Close → **HEUTE NICHT AKTIV** [NOT_SOON confirmed]

→ **Nur JPM-Blackout aktiv heute** (V1 316,14, SICHER).
→ **Nächster Watchpunkt:** Mo 13.07. Close → UNH-Blackout-Aktivierung → V1 auf -5 % (381,49) VORBEREITEN.

**Guardrail-Status Pre-Market (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,056 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,375 % (KW28 Mo-Basis 99.420,34)    [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,018 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,018 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY Do +0,841 % / PM -0,02 %          [INAKTIV]
6. VIX-Filter (>30):          ~16,79 (VXX ~22,54)                   [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIV (V1 316,14 SICHER)          [GRÜN operativ]
8. Max Käufe KW28:            2/2 → LOCK bis Mo 13.07.              [GESPERRT]
```
→ **STATUS: ALLE 8 GRÜN, aber Käufe-Slot LOCK aktiv.**

**Entscheidung Market Open 09:30 ET:**
- **KEIN Kauf-Scan** (Käufe-Slot 2/2 voll, LOCK bis Mo 13.07.)
- **Nur Guardrail-Monitoring + V1-Watch** aller 4 Positionen
- **JPM Live-Watch** bei < 316,14 → sofort V1-Market-Sell (Puffer heute +6,76 % SICHER)
- **GOOGL Live-Watch** — Fill-Day+3 Verengung (V1-Puffer nur +5,19 %) → Midday-Recheck zwingend
- **Keine Order-Aktivität** — keine Sell-Signale, keine Buy-Slots

**Watchlist KW29-Prep (Kauf-Fenster ab Mo 13.07.):**
```
Sym    Ranking Mi 08.07. Close (carry) Status KW29                              Kommentar
AAPL   3/3 K1-K3 (RS +10,33 %)         LEAD — K5-Recheck zwingend Mo 13.07.     XLK +2,16 % Do bestätigt Sektor-Timing
NVDA   3/3 K1-K3 (RS +1,37 %)          NEU 2. XLK-Kandidat, K5 offen            Grenzwertig RS
CAT    2/3 K2-Fail (RSI 48,93)         Backup — K3 stärkstes RS +17,69 %        KW29-Recheck
AMZN   2/3 K2-Fail                     Backup — K1-Spread eng                   K5 offen
```
→ Ranking KW29: **AAPL LEAD** / **NVDA 2. XLK-Kandidat** / **CAT/AMZN Backup**.

**Datenqualitäts-Hinweise:**
- Alpaca IEX SPY-Quote 08:36 ET Live als Ground-Truth (Perplexity lieferte keine SPY-Pre-Market-Daten)
- Alpaca Position-Quotes für JPM/UNH/LLY/GOOGL zeigen Do-Close ts=20:00 UTC = 16:00 ET (Alpaca IEX führt kein STO-Pre-Market-Feed) — `current_price` aus /v2/positions als beste verfügbare Pre-Market-Referenz genutzt
- Perplexity VIX-Snippet vom 10.07. (16,79/-0,65 %) einzige Live-Referenz — plausibel gegen 09.07.-Close 16,90 (VXX-Widening +2,32 % impliziert leichten Vola-Tick, Datenkonsistenz akzeptabel)
- Perplexity Earnings-Multi-Query: JPM 14.07. BMO + UNH 16.07. BMO beide multi-source konsolidiert; LLY/GOOGL NOT_SOON bestätigt (Perplexity-Label bei UNH „AMC" mit 8 AM ET Call ist offensichtlicher Bug — 8 AM ET = BMO)
- Alpaca last_equity 99.060,07 weicht +67,94 $ vs Memory Do-Close 98.992,13 (After-Hours-Tick, akzeptabel; Daily-P/L auf Memory-Close-Ground-Truth 98.992,13 gerechnet)

**ClickUp:** Task-Anlage fehlgeschlagen (ITEM_246 „Max usage for custom task types reached" Tier-Limit carry-over aus KW26/27) → Push-Notification an Owner als Fallback (siehe Routine-Reply).

**Nächste Routine:** Fr 10.07. 09:30 ET Market Open (KW28 Tag 5, KEIN Kauf-Scan, JPM-Live-Watch bei 316,14, GOOGL-Fill-Day+3-Watch).

---

## Market Close 16:02 ET — 2026-07-09 (Do, KW28 Tag 4) — Tagesbilanz, JPM V1-Tightening AKTIVIERT, XLK-Rally ohne Bot-Exposure

**Alpaca Clock:** is_open=false, next_open Fr 10.07. 09:30 ET, next_close 16:00 ET.

**Account Close 16:02 ET:**
```
Equity:            98.992,13 $   (Daily +0,023 % vs Mi-EOD 98.969,42)      [GRÜN]
Cash:              68.626,60 $   (69,33 %, unverändert)
Portfolio_MV:      30.365,53 $   (30,67 %)
Weekly KW28:       -0,431 %      (Mo-Basis 99.420,34)                       [GRÜN]
DD vs ATH:         -1,074 %      (ATH 100.066,47)                           [GRÜN]
Käufe KW28:        2/2 → LOCK bis Mo 13.07.
Pending Orders:    0
```

**SPY-Ground-Truth:** Alpaca IEX SPY 751,55 (Mi 745,28) → **+0,841 % Daily**. Perplexity nannte 749,74/+0,54 % — moderate Diskrepanz, Alpaca als Ground-Truth. **Alpha vs SPY = +0,023 % − 0,841 % = -0,818 %** [NEGATIV].

**Positionen Close V1-V6 (Alpaca IEX 205d Bars, EMA/RSI inkrementell aus Vortag):**
| Sym    | Close    | P/L     | Chg_today | V1-Stop        | V1-Puffer | Status |
|--------|----------|---------|-----------|----------------|-----------|--------|
| JPM    | 335,415  | +0,79%  | +1,36%    | **316,14 NEU** | +6,10 %   | SICHER (Blackout -5 % AKTIV) |
| UNH    | 431,655  | +7,49%  | +1,42%    | 369,44         | +16,84 %  | SICHER (V2 NEU 381,89, Posit-Hoch 434,19) |
| LLY    | 1215,62  | +1,82%  | +0,09%    | 1.098,38       | +10,67 %  | SICHER |
| GOOGL  | 358,88   | -2,51%  | -0,86%    | 338,65         | +5,97 %   | SICHER (engste, Fill-Day+2 Divergenz zu XLC) |

→ **Alle V1-V6 SICHER.** **Keine Limit-Order für Fr 10.07.**

**Sektor-Performance heute (Alpaca IEX):**
```
XLK +2,16 % | XLY +1,35 % | XLF +1,03 % | XLC +0,97 % | XLI +0,39 % | XLB +0,20 % | XLRE +0,17 %
XLV -0,10 % | XLU -0,55 % | XLP -1,42 % | XLE -1,44 %
VXX -1,82 % (Vola-Entspannung post-FOMC, VIX ~17)
```
→ **Klare Rotation ZURÜCK in Tech/Growth.** Bot-Positionen: JPM XLF +1,03 % Rebound (change_today +1,36 %); UNH+LLY XLV -0,10 % ohne Sektor-Support (UNH +1,42 % einzelwert-stark); GOOGL XLC +0,97 % Sektor grün ABER GOOGL -0,86 % Divergenz.
→ **XLK +2,16 % ohne Bot-Exposure → Alpha-Miss -0,818 % strukturell.** AAPL/NVDA-KW29-Prep validiert.

**Guardrails Close (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,023 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,431 %                              [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,074 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,074 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY +0,841 %                          [INAKTIV]
6. VIX-Filter (>30):          ~17 (VXX -1,82 %)                     [GRÜN]
7. Earnings-Blackout (3 HT):  JPM AKTIVIERT ab HEUTE CLOSE           [GRÜN operativ, V1 auf -5 %]
8. Max Käufe KW28:            2/2 → LOCK bis Mo 13.07.              [GESPERRT]
```

**⚠ JPM V1-Stop-Tightening AKTIVIERT AB JETZT:**
- V1 alt (–8 %): 306,16 → V1 NEU (–5 %): **316,14** (aktueller Kurs 335,415 → Puffer +6,10 %)
- Gilt bis Q2 14.07.2026 BMO (Blackout-Ende = Earnings-Tag)
- Fr 10.07. Pre-Market ZWINGEND: JPM < 316,14 → sofort V1-Market-Sell

**Watchlist Fr 10.07. + KW29-Prep (Ranking bleibt aus Mi 08.07. Close-Screener):**
```
Sym   Ranking                                                Kommentar
AAPL  LEAD — 3/3 K1-K3 (RS +10,33 %, RSI 62,81)              XLK +2,16 % heute massiv → Momentum-Restore validiert
NVDA  NEU 2. XLK-Kandidat — 3/3 grenzwertig RS +1,37 %        XLK-Rebound bestätigt Sektor-Timing
CAT   Backup — 2/3 K2-Fail RSI 48,93                          K3 stärkstes RS +17,69 %; KW29-Recheck
AMZN  Backup — 2/3 K2-Fail, K1-Spread eng                     XLY +1,35 % heute positiv
```
→ **AAPL LEAD gestärkt** durch XLK-Rally +2,16 % — Sektor-Timing für Mo 13.07. Kauf perfekt.

**Perplexity-Query:** SPY-Daten leicht verzerrt (749,74/+0,54 % vs Alpaca 751,55/+0,841 %) — Alpaca als Ground-Truth. VIX/Sektor-Details fehlten, Alpaca-ETF-Fallback erfolgreich.

**Entscheidung Market Close 09.07.:**
- Alle V1-V6 SICHER → keine Sell-Order für Fr 10.07.
- KEIN Kauf-Scan (Slot LOCK 2/2 bis Mo 13.07.)
- **JPM V1-Tightening auf 316,14 (-5 %) AKTIVIERT** — Fr Pre-Market-Watch zwingend
- UNH V2-Trail auf 381,89 angehoben (NEUES Posit-Hoch 434,19)
- Watchlist AAPL/NVDA-Sektor-Support durch XLK +2,16 % validiert

**Nächste Routine:** Fr 10.07. 08:30 ET Pre-Market Check.

**ClickUp:** [CLOSE] Tagesbilanz Task Prio 3 (Portfolio-Performance leicht positiv ABER Alpha stark negativ -0,818 % → Priorität Normal).

---

## Market Open 09:37 ET — 2026-07-09 (Do, KW28 Tag 4) — No-Op (Slot LOCK 2/2), alle V1 SICHER, leichter Rebound post-FOMC

**Alpaca Clock:** is_open=true, next_close 09.07. 16:00 ET.

**Account Live 09:37 ET:**
```
Equity:            98.999,05 $   (vs last_equity 98.969,42 = Mi EOD-Mark → Daily +0,030 %) [GRÜN]
Cash:              68.626,60 $   (69,32 %, unverändert)
Portfolio_MV:      30.372,45 $   (30,68 %)
Buying_power:     359.549,25 $
Käufe KW28:        2/2 → LOCK bis Mo 13.07.
Pending Orders:    0
Trading_blocked:   false | Status: ACTIVE
```

**Positionen Live V1 (Alpaca 09:37 ET, change_today = vs Mi-Close):**
| Sym    | Live      | P/L     | Chg_today | V1-Stop    | V1-Puffer  | Status |
|--------|-----------|---------|-----------|------------|------------|--------|
| JPM    | 331,935   | -0,25 % | +0,40 %   | 306,16     | +8,42 %    | SICHER |
| UNH    | 426,27    | +6,15 % | +0,16 %   | 369,44     | +15,35 %   | SICHER |
| LLY    | 1.228,405 | +2,89 % | +1,03 %   | 1.098,38   | +11,83 %   | SICHER |
| GOOGL  | 358,4775  | -2,61 % | -0,95 %   | 338,65     | +5,85 %    | SICHER (engste, Fill-Day+2 Verengung) |

→ **Alle 4 V1 SICHER, keine Order pending, keine Verkaufsentscheidung.** Leichter Rebound-Tag (Daily +0,030 %) nach Mi post-FOMC-Rutsch.

**LLY-Rebound-Signal:** +1,03 % change_today = XLV-Rotation-Comeback (Mi -1,60 %); Position P/L +2,89 % nach Mi +1,84 %. → Watchlist-Watch für Midday.

**GOOGL-Verengung:** Fill-Day+2 Konsolidierung fortgesetzt (change_today -0,95 %, P/L -2,61 %). V1-Puffer schmilzt +6,45 % → +5,85 % (Mi-Close vs jetzt). Weiter engste Position aber SICHER (V1 338,65 $, aktuell 358,48 $ = +5,85 % Puffer).

**Guardrail-Status Market Open (alle 8):**
```
1. Daily Loss Cap (-3 %):     +0,030 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,423 % (KW28 Mo-Basis 99.420,34)    [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,067 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,067 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   INAKTIV                                [GRÜN]
6. VIX-Filter (>30):          ~18-19 carry-over                     [GRÜN]
7. Earnings-Blackout (3 HT):  KEINER heute (JPM ab Close aktiv)     [GRÜN heute]
8. Max Käufe KW28:            2/2 → LOCK bis Mo 13.07.              [GESPERRT]
```
→ **STATUS: ALLE 8 GRÜN, aber Käufe-Slot LOCK aktiv.**

**Perplexity-Query ENTFÄLLT:** Keine Kauf-Entscheidung (Slot LOCK) → kein Sektor-Scan erforderlich. Guardrail-Monitoring + V1-V6-Watch reicht.

**Earnings-Blackout-Preview (aktueller Stand):**
- **JPM Q2 14.07.2026 BMO CONFIRMED** → 3-HT-Blackout aktiviert ab **HEUTE CLOSE (09.07. 16:00 ET)** → **V1-Tightening auf -5 % (316,14) ZWINGEND zur Close-Routine**
- UNH ~16.07. carry-unbestätigt / LLY 05.08. (19 HT) / GOOGL 22.07. (9 HT) — alle sicher

**Sektor-Update:** JPM XLF 1,01 % + UNH XLV 10,33 % + LLY XLV 9,93 % + GOOGL XLC 9,41 % = **30,68 %** investiert. XLV Total 20,26 % (unter 30 %-Cap ✓). 4/8 Positions-Slots belegt.

**Entscheidung Market Open:**
- **KEIN Kauf-Scan** (Käufe-Slot 2/2 voll, LOCK bis Mo 13.07.)
- **Nur Guardrail-Monitoring + V1-Watch** aller 4 Positionen
- **Keine Order-Aktivität** — keine Sell-Signale, keine Buy-Slots
- **Vorbereitung Close-Routine:** JPM-V1-Tightening auf -5 % (316,14) ZWINGEND ab 16:00 ET Close

**Watchlist KW29-Prep (Kauf-Fenster ab Mo 13.07., aus Mi-Close-Screener):**
```
Sym    Ranking Mi 08.07. Close      Status KW29                                    Kommentar
AAPL   3/3 K1-K3 (RS +10,33 %)     LEAD — K5-Recheck zwingend                     XLK-Sektor-Support (+1,22 % Mi)
NVDA   3/3 K1-K3 (RS +1,37 %)      NEU 2. XLK-Kandidat, K5 offen                  Grenzwertig RS
CAT    2/3 K2-Fail (RSI 48,93)     Backup — K3 stärkstes RS +17,69 %              KW29-Recheck
AMZN   2/3 K2-Fail                  Backup — K1-Spread eng                         K5 offen
```
→ Ranking KW29: **AAPL LEAD** / **NVDA/CAT/AMZN Backup**.

**Datenqualitäts-Hinweise:**
- Alpaca last_equity 98.969,42 weicht -1,57 $ vs Memory Mi-Close 98.970,99 (After-Hours-Tick, akzeptabel)
- Live-Marks als Ground-Truth für V1-Puffer-Rechnung (change_today vs Mi-Close verwendet)
- Perplexity-Query aus Effizienzgründen übersprungen (No-Op-Routine, Slot LOCK)
- VIX carry-over aus Mi (~18-19); explizite Live-Query nicht erforderlich für No-Op

**ClickUp:** [ROUTINE] Market Open Log-Task Prio 4 (Low, No-Op, Slot LOCK, kein Alert-Kontext).

**Nächste Routine:** Do 09.07. 13:00 ET Midday Stop-Check (KW28 Tag 4, V1-V4-Watch aller 4 Positionen; keine Kauf-Aktivität möglich).

---

## Market Close 16:02 ET — 2026-07-08 (Mi, KW28 Tag 3) — Tagesbilanz post-FOMC, alle V5/V6 SICHER, KEINE Pending-Order für Do

**Alpaca Clock:** is_open=false, next_open Do 09.07. 09:30 ET, next_close 16:00 ET.

**Account Close 16:02 ET:**
```
Equity:            98.970,99 $   (Daily -0,380 % vs Di-EOD 99.348,08) [GRÜN]
Cash:              68.626,60 $   (69,34 %, unverändert)
Portfolio_MV:      30.344,39 $   (30,66 %)
Weekly KW28:       -0,452 %      (Mo-Basis 99.420,34)                  [GRÜN]
DD vs ATH:         -1,095 %      (ATH 100.066,47)                      [GRÜN]
Käufe KW28:        2/2 → LOCK bis Mo 13.07.
Pending Orders:    0
```

**SPY-Ground-Truth:** Alpaca IEX SPY 745,28 (Di 747,77) → **-0,333 % Daily**. Alpha vs SPY = -0,380 % - (-0,333 %) = **-0,047 %** (~flat).

**Positionen Close V1-V6 (Alpaca IEX 204d Bars, EMA/RSI Wilder live):**
| Sym    | Close  | P/L    | Chg_today | V5 EMA50/200         | V6 RSI/RS_4w   | Status |
|--------|--------|--------|-----------|----------------------|----------------|--------|
| JPM    | 330,45 | -0,70% | -2,59%    | 316,57>306,41 ✓      | 56,99 / +5,64% | SICHER |
| UNH    | 425,60 | +5,98% | -0,61%    | 389,48>336,55 ✓      | 62,23 / +4,18% | SICHER |
| LLY    | 1215,83| +1,84% | -1,60%    | 1097,80>989,44 ✓     | 64,28 / +4,70% | SICHER |
| GOOGL  | 362,00 | -1,66% | -1,37%    | 359,31>317,16 ✓      | 50,29 / -1,54% | SICHER |

→ **Alle V5/V6 SICHER (GOOGL RS_4w negativ, aber RSI 50,29 <80 → V6 verlangt BEIDES).** **Keine Limit-Order für Do 09.07.**

**Sektor-Performance heute (post-FOMC-Minutes 14:00 ET):**
```
XLE +1,70 % | XLK +1,22 %     ← nur diese 2 grün
XLP -0,51 % | XLU -0,74 % | XLI -1,09 % | XLV -1,34 % | XLC -1,41 %
XLRE -1,68 % | XLY -1,77 % | XLF -1,91 % | XLB -2,58 %
VXX +1,57 % (Vola-Tick, VIX ~18-19)
```
→ Bot-Verlierer: JPM XLF -1,91 % (change_today -2,59 %). UNH+LLY XLV -1,34 % moderat. GOOGL XLC -1,41 %.
→ **KW29-Rotation-Watch: XLK-Rebound signalisiert AAPL/NVDA-Momentum-Restore.**

**Guardrails Close (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,380 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,452 %                              [GRÜN]
3. Drawdown-Alarm (-15 %):    -1,095 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -1,095 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   SPY -0,333 %                          [INAKTIV]
6. VIX-Filter (>30):          ~18-19 (VXX +1,57 %)                  [GRÜN]
7. Earnings-Blackout (3 HT):  KEINER heute, JPM ab 09.07. Close     [GRÜN heute]
8. Max Käufe KW28:            2/2 → LOCK bis Mo 13.07.              [GESPERRT]
```

**Watchlist Do 09.07. + KW29-Prep (Alpaca K1-K3 Live 08.07. Close, SPY_RS_63d +13,34 %):**
```
Sym    Last      K1 EMA50>200          K2 RSI (50-70) K3 RS_63d      Rank/Status
AAPL   313,33   ✓ 292,89>271,56       ✓ 62,81         ✓ +10,33 %    LEAD KW29 — XLK-Support heute
NVDA   204,07   ✓ 203,47>191,00       ✓ 51,02         ✓ +1,37 %     NEU — 3/3 grenzwertig RS, XLK-Support
CAT    947,62   ✓ 916,49>702,87       ✗ 48,93         ✓ +17,69 %    2/3 — K2-Fail RSI cool-off, K3 stärkstes
AMZN   243,60   ✓ 245,37>233,35       ✗ 49,50         ✓ +0,59 %     2/3 — K2-Fail, K1-Spread eng, Backup
```
**Watchlist morgen: AAPL (LEAD, K5-Recheck erforderlich), NVDA (2. XLK-Kandidat, K5 offen), CAT (K2-Recheck bei Rebound), AMZN (Backup)**

**Perplexity Watchlist-Query:** lieferte keinen Value (Date-in-Future-Bug carry-over). Alpaca-K1-K3-Screener als Fallback erfolgreich für Kandidatenrunde.

**Earnings-Blackout-Preview (Do 09.07.):**
- JPM Q2 14.07.2026 BMO CONFIRMED → 3-HT-Blackout aktiviert **ab Close 09.07.** → **V1-Tightening auf -5 % (316,14 statt 306,16) ab MORGEN CLOSE** zwingend
- UNH ~16.07. carry-unbestätigt (Perplexity-Recheck morgen)
- LLY 05.08. (20 HT) / GOOGL 22.07. (10 HT) — beide sicher

**Entscheidung Market Close 08.07.:**
- Alle V1-V6 SICHER → keine Sell-Order
- KEIN Kauf-Scan (Slot LOCK 2/2 bis Mo 13.07.)
- Watchlist erweitert um NVDA (XLK-Rebound), AAPL bleibt LEAD, CAT rutscht auf K2-Fail
- JPM-Stop-Tightening auf V1=-5 % ab Do 09.07. Close vorbereiten

**Nächste Routine:** Do 09.07. 08:30 ET Pre-Market Check.

**ClickUp:** [CLOSE] Tagesbilanz Task Prio 3 (leicht negative Performance UND leicht negatives Alpha → Priorität Normal).

---

## Pre-Market 08:35 ET — 2026-07-08 (Mi, KW28 Tag 3) — Guardrails GRÜN, KEIN Kauf-Scan (Slot LOCK 2/2), V1-V6-Watch

**Alpaca Clock:** is_open=false, next_open Mi 08.07. 09:30 ET, next_close 16:00 ET. Pre-Market-Session aktiv.

**Account Live 08:35 ET (Pre-Market):**
```
Equity:           99.236,19 $   (vs last_equity 99.348,08 → Daily -0,113 %) [GRÜN]
Cash:             68.626,60 $   (69,15 %, unverändert)
Portfolio_MV:     30.609,59 $   (30,85 %)
Buying_power:    360.213,25 $
Käufe KW28:       2/2 (LLY+GOOGL FILLED — LOCK bis Mo 13.07.)
Pending Orders:   0
Trading_blocked:  false | Status: ACTIVE
```

**Positionen Pre-Market Live (Alpaca Quotes 08:35 ET, change_today = vs 07.07. Close):**
- **JPM**   336,73 $ (Entry 332,78, P/L +1,19 %, change_today -0,73 %) — XLF-Cool-off nach flat-Di
  - V1 306,16 SICHER +9,98 % Puffer
  - lastday 339,22 (After-Hours-Tick +0,23 % vs Memory Close 338,45)
- **UNH**   427,85 $ (Entry 401,57, P/L +6,54 %, change_today -0,08 %) — XLV stabil nach Rebound-Di
  - V1 369,44 SICHER +15,81 %
- **LLY**  1.235,00 $ (Entry 1.193,89, P/L +3,44 %, change_today -0,05 %) — Konsolidierung nach Posit-Hoch 1.248,53
  - V1 1.098,38 SICHER +12,44 %
  - V2 Trail 1.098,70 (carry-over vom 07.07. Posit-Hoch)
- **GOOGL** 363,50 $ (Entry 368,10, P/L -1,25 %, change_today -0,96 %) — Fill-Day+1 leichte Verengung
  - V1 338,65 SICHER +7,33 % Puffer [engste Position, ABER weit über V1]
  - V2 Trail 328,36 (carry-over Posit-Hoch 373,14)
  - lastday 367,03 (After-Hours-Tick +0,12 %)

→ **Alle 4 V1-V6 SICHER, keine Order pending, keine Verkaufsentscheidung.**

**Perplexity Macro Check (Pre-Market Live):**
```
VIX Spot Di 07.07. Close: 16,13 (CBOE, +3,60 % vs 15,57 Mo)
VIX Live 08.07. 08:30 ET (CBOE-Snippet): ~18,82 (+16,68 %, Vola-Tick)  → GRÜN (< 30)
SPY Pre-Market Alpaca IEX: mid ~743,83 (-0,527 % vs Di-Close 747,77)  [Ground-Truth]
                          (Perplexity nannte "+0,75 %" — Datenfehler carry-over Juni-Artikel)
10Y Treasury:             N/A explizit (Perplexity indirekt via „Fed Rate Hike Fears Ease")
FOMC-Minutes:             heute PLANMÄSSIG (Perplexity MarketWatch-Snippet 07.07. 18:24 ET)
Geopolitik:               Middle-East-Spannungen im Fokus
Top-News:                 (1) Chip-Recovery: MRVL +9 % (S&P 500-Inclusion) (2) BofA SNDK Target $2100 (Buy) (3) Citi Year-End SPX Target 8100 (AI-Tailwind)
```

**Sonderfall SPY vs VIX:** Alpaca IEX SPY-Premarket -0,53 % + VIX-Tick +16,68 % konsistent (moderat risk-off). BEIDES noch weit von Guardrail-Schwellen (SPY > -2 %, VIX < 30).

**Earnings-Blackout-Check (Perplexity 08.07.):**
- **JPM Q2 2026: 14.07.2026 BMO CONFIRMED** (WallStreetHorizon + MarketBeat + JPM IR) → 4 HT ab heute (Mi 08, Do 09, Fr 10, Mo 13, Di 14 = 4 HT bis Earnings)
  - 3-HT-Blackout aktiv ab **09.07. Close (Do)** → **JETZT NOCH NICHT AKTIV** — Watch morgen zwingend
  - Stop-Tightening JPM V1 → -5 % erforderlich ab Do 09.07. Close (Regel: Earnings-Blackout → V1 auf -5 %)
- **UNH Q2 2026:** unbestätigt via Perplexity → carry-over 16.07.2026 (unverifiziert) → Blackout ab 13.07. Close → **JETZT NICHT AKTIV**
- **LLY Q2 2026:** 05.08.2026 BMO carry-over (Multi-Source 06.07.) → 20 HT ab heute → weit weg
- **GOOGL Q2 2026:** 22.07.2026 carry-over → 10 HT ab heute → 3-HT-Blackout ab 17.07. Close → NICHT AKTIV

→ **Kein Blackout heute aktiv.** Standard V1-Stops für alle 4 Positionen bleiben.
→ **Zwingender Watch morgen:** JPM Blackout-Aktivierung + Stop-Tightening -5 % ab Do 09.07. Close.

**Guardrail-Status Pre-Market (alle 8):**
```
1. Daily Loss Cap (-3 %):     -0,113 %                              [GRÜN]
2. Weekly Loss Cap (-5 %):    -0,185 % (KW28 Mo-Basis 99.420,34)    [GRÜN]
3. Drawdown-Alarm (-15 %):    -0,835 % vs ATH 100.066,47            [GRÜN]
4. Drawdown-Stopp (-20 %):    -0,835 %                              [GRÜN]
5. Crash-Filter (SPY -5 %):   Di +/-747,77 → SPY-PM -0,53 %         [INAKTIV]
6. VIX-Filter (>30):          ~16-19 Live                            [GRÜN]
7. Earnings-Blackout (3 HT):  KEINER heute                          [GRÜN]
8. Max Käufe KW28:            2/2 → LOCK bis Mo 13.07.              [GESPERRT]
```
→ **STATUS: ALLE 8 GRÜN, aber Käufe-Slot LOCK aktiv.**

**Entscheidung Market Open 09:30 ET:**
- **KEIN Kauf-Scan** (Käufe-Slot 2/2 voll, LOCK bis Mo 13.07.)
- **Nur Guardrail-Monitoring + V1-V6-Watch** aller 4 Positionen
- FOMC-Minutes 14:00 ET → möglicher intraday-Vola-Spike; Midday-Routine 13:00 ET vor Release, Close-Routine nach Release
- Middle-East-News-Watch bei Sektor-Rotation (XLE ggf. Gewinner wie 07.07. +2,84 %)

**Watchlist KW29-Prep (Kauf-Fenster ab Mo 13.07.):**
```
Sym   Ranking Mo 06.07. Close        Status Recheck                                       Kommentar
CAT   RS +20,55 % / RSI 51,65       K5 RevGrowth Q1 -1 % Recheck zwingend KW29           XLI-Sektor -1,68 % 07.07. (Rotation weg) — Watch bleibt
AAPL  RS +7,47 % / RSI 63,16        K5 Multi-Source-Recheck                              XLK-Konflikt obsolet nach MU-Sell; XLK -2,38 % 07.07. — Sektor-Timing schwierig
MS    AUSGESCHIEDEN                 Earnings 15.07. → Blackout ab Fr 10.07. Close        Kauf Mo 13.07. NICHT möglich
```
→ Ranking KW29: **CAT LEAD** / **AAPL Backup** / MS AUS.

**Datenqualitäts-Hinweise:**
- Perplexity SPY-Premarket-Query gab veraltete Juni-Daten (+0,75 %) — Alpaca IEX SPY-Quote 743,83 als Ground-Truth
- VIX-CBOE-Snippet "as of July 8, 2026 $18.82" ist einzige 08.07.-Datum-Referenz → Sprung von 16,13 auf ~18,82 plausibel bei Middle-East-Tensionen
- Perplexity Earnings-Query nur JPM bestätigt (WallStreetHorizon), UNH/LLY/GOOGL unbestätigt — carry-over aus vorherigen Rechercheeinträgen verwendet
- Alpaca `current_price` in Pre-Market = letzter Trade/Quote, kein offizieller Open-Preis; V1-Trigger erst bei Regulär-Session-Preis
- Alpaca last_equity 99.348,08 weicht +13,47 $ vs Memory Close 99.334,61 ab (After-Hours-Tick, kleinere Abweichung als Vortage — akzeptabel)

**ClickUp:** [PRE-MARKET] Check Task angelegt Prio 4 (Low, No-Op-Routine → keine besondere Aktion, nur Log).

**Nächste Routine:** Mi 08.07. 13:00 ET Midday Stop-Check (V1-V4-Watch aller 4 Positionen VOR FOMC-Minutes 14:00 ET; keine Kauf-Aktivität möglich).

---

## Market Close 16:02 ET — 2026-07-07 (Di, KW28) — Tagesbilanz + Watchlist Mi 08.07. (Kauf-Slots LOCK)

**Tagesbilanz:** Portfolio 99.334,61 $ (-50,68 $ / -0,051 %) | SPY IEX -0,466 % (751,27 → 747,77) | **Alpha +0,415 %** [POSITIV] | Positionen 4/8 (JPM +1,70 % / UNH +6,63 % / LLY +3,49 % / GOOGL -0,41 %) | Käufe KW28 **2/2 VOLL** (LLY 06.07. + GOOGL 07.07. — Lock bis Mo 13.07.) | Guardrails alle GRÜN | Weekly KW28 -0,086 %.

**Sektor-Performance heute (Alpaca IEX):**
```
XLE +2,84 % | XLV +1,51 % | XLRE +1,40 % | XLU +0,92 % | XLP +0,89 % | XLC +0,73 %
XLF -0,20 % | XLY -0,49 % | XLB -0,87 % | XLI -1,68 % | XLK -2,38 %
VXX +0,84 % (Vola-Tick, weiter GRÜN <25)
```
→ **Rotation ins Defensives — XLV/XLU/XLP/XLE alle grün, XLK/XLI unter Druck.** Bot-Portfolio: UNH+LLY XLV +1,51 % (Sektor-Winner), GOOGL XLC +0,73 % (Support), JPM XLF -0,20 % (flat). Alpha +0,415 % erklärbar durch XLV-Overweight bei defensivem Rotations-Tag. **MU-V1-Sell gestern zum optimalen Zeitpunkt** — XLK -2,38 % heute hätte auf 9 Sh MU zusätzlichen Verlust ~-215 $ verursacht.

**V1–V6-Check ALLE 4 POSITIONEN SICHER (nach Close-Recalc EMA/RSI aus Alpaca IEX 203d):**
- JPM V1 +10,55 % / V5 EMA-Spread +9,01 ✓ / V6 RSI 67,16 & RS +7,33 % → SICHER
- UNH V1 +15,90 % / V5 EMA-Spread +41,81 ✓ / V6 RSI 64,18 & RS +6,07 % → SICHER
- LLY V1 +12,49 % / V5 EMA-Spread +109,68 ✓ / V6 RSI 69,15 & RS +7,38 % → SICHER (neues Posit-Hoch 1.248,53 → V2-Trail 1.098,70)
- GOOGL V1 +8,25 % / V5 EMA-Spread +35,28 ✓ / V6 RSI 53,98 & RS -2,14 % → SICHER (V6 verlangt BEIDES; RSI weit unter 80)

→ **Keine Verkaufsorder für Mi 08.07. vorbereitet.** Pending Orders bleiben 0.

**Watchlist Mi 08.07. — KEIN AKTIVER KAUF-SCAN:**
Käufe KW28 2/2 voll → Watchlist ist Prep für KW29 Mo 13.07., nicht handelbar Mi.
```
Sym   Ranking Mo 06.07. Close       Status Recheck                                       Kommentar
CAT   RS +20,55 % / RSI 51,65      K5 RevGrowth Q1 -1 % Recheck zwingend KW29           XLI-Sektor -1,68 % heute (Rotation weg) — Watch bleibt
MS    RS +19,81 % / RSI 60,39      Earnings 15.07. → 3-HT-Blackout ab Fr 10.07. Close   Kauf Mo 13.07. NICHT möglich (Blackout aktiv) — SCHEIDET AUS
AAPL  RS +7,47 % / RSI 63,16       K5 Multi-Source-Recheck                              XLK-Konflikt jetzt obsolet nach MU-Sell; XLK -2,38 % heute — Sektor-Timing schwierig
```

**Ranking KW29 Prep:**
1. **CAT** LEAD — K5 RevGrowth-Recheck (Q1 -1 % carry-over aus Multi-Source-Erhebung); XLI leer trotz Sektor-Rutsch heute; Earnings ~05.08. sicher
2. **AAPL** Backup — K5-Recheck; XLK-Konflikt obsolet; Sektor XLK -2,38 % heute problematisch als Timing-Signal (AAPL relative Stärke vs. Sektor prüfen KW29)
3. MS AUSGESCHIEDEN (Blackout)

**Perplexity Status:** Datum-in-Zukunft-Bug carry-over für SPY-Query und Sektor-Query (wiederholt geliefert "SPY SPY SPY..."). Fallback auf Alpaca IEX für alle Preis-/Sektor-Daten funktionierte einwandfrei. K5-Multi-Source-Rechecks für CAT/AAPL erst am KW29-Anfang (Perplexity-Bug-Persistenz Watch).

**Guardrail-Status Close:**
```
1. Daily Loss Cap (-3 %):    -0,051 %  → GRÜN
2. Weekly Loss Cap (-5 %):   -0,086 %  → GRÜN
3. Drawdown-Alarm (-15 %):   -0,732 %  → GRÜN
4. Käufe KW28:                2/2      → LOCK (nächster Kauf frühestens Mo 13.07.)
5. Crash-Filter SPY -5 %:     -0,466 %  → INAKTIV
6. VIX-Filter > 30:           ~16      → GRÜN
7. Earnings-Blackout:         KEINER   → GRÜN
```

**Datenqualitäts-Hinweise:**
- Perplexity SPY-Tages-Query gab "SPY SPY SPY..." Token-Repetition (Datum-in-Zukunft-Bug) — Alpaca IEX SPY-Bar als Ground-Truth 751,27 → 747,77 = -0,466 %
- Sektor-ETF-Marks alle über Alpaca IEX Fallback (12/12 Sektoren erfolgreich, inkl. VXX)
- 203d Daily-Bars für JPM/UNH/LLY/GOOGL/SPY geladen — EMA50/200 + RSI(14) + 4w/63d-Returns live berechnet
- Alpaca last_equity 99.385,29 (Mo EOD-Mark After-Hours) weicht +137 $ vs Memory Mo Close 99.248,28 ab — Alpaca als Ground-Truth für Daily-P/L (Standard-Vorgehen bei EOD-Recalc-Ticks)

**ClickUp:** [CLOSE] Tagesbilanz Task angelegt Prio 4 (P/L leicht negativ, ABER Alpha positiv → Prio abgestuft). Push-Notification an Owner (ITEM_246 Tier-Limit carry-over, `custom_item_id: null`).

**Nächste Routine:** Mi 08.07. 08:30 ET Pre-Market Check (KW28 Tag 3, KEIN Kauf-Scan mangels Käufe-Slot, nur Guardrail-Monitoring + V1-V6-Watch aller 4 Positionen).

---

## Market Open 09:40 ET — 2026-07-07 (Di, KW28) — MU V1-Sell exec + GOOGL Buy pending

**Alpaca Clock:** is_open=true, next_close 16:00 ET. Regulär-Session seit 09:30 ET.

**Account nach MU-Sell (09:40 ET):**
```
Equity:          99.266,85 $   (vs last_equity 99.420,34 → Daily -0,154 %) [GRÜN]
Cash:            78.197,20 $   (78,78 %, +8.320,05 $ aus MU-Sell)
Portfolio_MV:    21.069,65 $   (21,22 %)
Buying_power:   361.664,03 $
Käufe KW28:      1/2 (LLY 06.07. filled; GOOGL-Buy pending zählt nach Fill als 2/2)
Pending Orders:  1 (GOOGL Limit-Buy)
```

**⚠️ SCHRITT 1 — MU V1 Stop-Loss AUSGELÖST bei Market Open:**
- Live 09:37 ET: MU 925,86 $ → -3,01 % unter V1-Stop 954,71 $
- Market Sell 9 Sh submit 09:37:39 ET → Fill 09:37:42 ET (3 sec, exzellent)
- Fill-Preis 924,45 $ avg → Erlös 8.320,05 $
- **Realisierter Verlust -1.019,43 $ (-10,92 %)** vs Entry 1.037,72 $
- Alpaca Order-ID: 12e7fa06-2702-4a47-ab32-c2f66edfd8d5
- ClickUp Critical Task 869e1fgp5 angelegt + Owner-Push Notification

**SCHRITT 2 — Guardrail-Status nach MU-Sell:**
```
1. Daily Loss Cap (-3 %):    -0,154 %   → GRÜN (Puffer -2,85 %)
2. Weekly Loss Cap (-5 %):   -0,154 %   → GRÜN
3. Drawdown-Alarm (-15 %):   -0,799 %   → GRÜN
4. Drawdown-Stopp (-20 %):   -0,799 %   → GRÜN
5. Crash-Filter SPY -5 %:    SPY -0,20 %→ INAKTIV
6. VIX-Filter > 30:          ~16        → GRÜN
7. Earnings-Blackout:        keine      → GRÜN (GOOGL 22.07. = 11 HT sicher)
8. Käufe/Woche max 2:        1/2        → 1 Slot frei
```
**Alle Guardrails GRÜN → Kauf-Scan erlaubt.**

**SCHRITT 3 — V1-V6 Live-Check verbliebene Positionen (09:40 ET):**
- **JPM** 340,81 $ (P/L +2,41 %) — V1 306,16 SICHER +11,32 % — Keine Action
- **UNH** 424,69 $ (P/L +5,76 %) — V1 369,44 SICHER +14,94 % — Keine Action
- **LLY** 1.232,28 $ (P/L +3,22 %) — V1 1.098,38 SICHER +12,20 % — Keine Action
→ Alle 3 verbliebenen Positionen V1-V6 SICHER, keine Verkaufsorder.

**SCHRITT 4 — Kauf-Scan GOOGL K1-K5 Live (Alpaca IEX 211d Bars):**
```
Sym    Live      K1 EMA50>EMA200      K2 RSI    K3 RS_63d vs SPY   K4 Vol-Projektion   K5 Multi-Source
GOOGL  369,57   ✓ 358,91>323,23     ✓ 53,59   ✓ +9,11 %          ✓ ~176 % Avg20      ✓ FwdPE 21,87/28,65 ≤35, Rev +11,33 % (carry 06.07.)
SPY    749,76   ✓ 731,53>696,51     ✓ 58,44   —                  —                    —
```
→ **GOOGL 5/5 grün → BUY-Entscheidung**

**SCHRITT 5 — GOOGL Position-Sizing + Limit-Order:**
- Equity nach MU-Sell: 99.266,85 $
- VIX ~16 (<25) → 10 % Sizing: Budget 9.926,69 $
- Shares = floor(9.926,69 / 369,57) = **26 Sh**
- Limit = round(366,34 × 1,005, 2) = **368,17 $** (+0,5 % über Mo-Close)
- Max Kosten: 26 × 368,17 = 9.572,42 $ (9,64 % Portfolio)
- Order-Submit: 09:40:46 ET, TIF=day
- Status 09:41 ET: **new pending** (Live 369,42 $ > Limit → wartet auf Pullback)
- Alpaca Order-ID: 69106496-90d4-46dc-a370-cafb7eb816ac

**Sektor-Post-Buy (bei Fill):** JPM XLF 1,03 % + UNH+LLY XLV 20,20 % + GOOGL XLC 9,64 % = 30,9 % investiert, 4/8 Slots → Diversifikation stark verbessert (XLC neu, XLK/MU-Slot freigegeben)

**Perplexity Sektor-Check heute:** ENTFÄLLT (Watchlist-Carry-over vom Pre-Market/Mo-Close ausreichend; alle 5 Signale via Alpaca Bars ohne Perplexity-K5-Recheck bestätigt — K5 carry-over-Median FwdPE 21,87/28,65 aus multi-source Erhebung 06.07.).

**Datenqualitäts-Hinweise:**
- Alpaca IEX-Bars 211d verfügbar für GOOGL — EMA50/200 + RSI(14) live berechnet
- SPY IEX 749,76 als Ground-Truth für RS_63d-Rechnung (Mo Close 751,27 = -0,20 %)
- Volume-Projektion 8-min-Fenster → linear extrapoliert auf 390 min (konservativ da Open-Vol typisch überproportional)

**ClickUp:** [CRITICAL] MU V1 Task 869e1fgp5 Prio 1 angelegt. Kein [OPEN] Alert für GOOGL-Order-Submit (nur bei Fill Prio 3 senden).

**Nächste Routine:** Di 07.07. 13:00 ET Midday — GOOGL-Fill-Status prüfen, V1-V4 aller 3 verbliebenen Positionen live.

---

## Pre-Market 08:35 ET — 2026-07-07 (Di, KW28) — **MU-V1-ALARM Pre-Market: 936,39 $ < Stop 954,71 $**

**Alpaca Clock:** is_open=false, next_open Di 07.07. 09:30 ET, next_close 16:00 ET. Pre-Market-Session aktiv.

**Account Live 08:35 ET (Pre-Market):**
```
Equity:           99.215,80 $   (vs last_equity 99.420,34 → Daily -0,206 %) [GRÜN]
Cash:             69.877,15 $   (70,43 %, unverändert)
Portfolio_value:  99.215,80 $
Positions MV:     29.338,65 $   (29,57 %)
Buying_power:    361.656,81 $
Trading_blocked:  false | Account_blocked: false | Status: ACTIVE
```

**Positionen Pre-Market (Alpaca Quotes 08:35 ET, change_today = vs Vortagesschluss):**
- **JPM**  341,57 $ (Entry 332,78, P/L +2,64 %, change_today +1,14 %) — XLF Pre-Market-Erholung fortgesetzt
- **UNH**  420,75 $ (Entry 401,57, P/L +4,78 %, change_today +0,66 %) — XLV Pre-Market-Stabilisierung
- **MU**   936,39 $ (Entry 1037,72, P/L **-9,77 %**, change_today **-4,91 %**) — **KRITISCH: LIEGT UNTER V1-STOP 954,71 $** ← Pre-Market-Tick
- **LLY**  1.223,99 $ (Entry 1193,89, P/L +2,52 %, change_today +1,99 %) — XLV-Rebound, Fill-Vorteil verstärkt

**⚠️ MU-V1-ALARM (Pre-Market):**
- Pre-Market-Tick 936,39 $ → -9,77 % vs Fill (Entry 1037,72)
- V1-Stop (Kaufkurs × 0,92) = 954,71 $ → **Pre-Market UNTER Stop**
- Pre-Market-Ticks lösen V1 NICHT direkt aus (Strategy V1 = Kurs während Regulär-Session)
- **Aktion 09:30 ET Market Open:** Falls MU im Open unter 954,71 $ → **V1 Market Sell SOFORT** (siehe market-open-routine.md)
- Portfolio-Effekt bei V1-Auslösung: Verlust ~-6,7 % × 9.339,48 Investiert ≈ -625 $ realisiert, Cash ~78,3 % danach

**Perplexity Macro Check (Pre-Market Live):**
```
VIX:              ~15,9-16,0        (+2-3 % vs Vortag) → GRÜN (< 30)
SPY Pre-Market:   ±0,3-0,6 %        (Futures moderat, keine starken Bewegungen)
10Y Treasury:     ~4,2-4,3 %        (stabile Zinsen)
Fed-Speak heute:  Regional-Fed möglich (Inflation & Arbeitsmarkt)
Makro-Events:     keine Mega-Daten heute (kein FOMC/CPI/NFP)
Top-News:         (1) Zinssenkungs-Timing-Debatte (2) weichere Arbeitsmarktdaten Nachwirkung (3) Tech/Semis Rotation Growth/Value
MU-News:          Keine spezifische Einzel-News, wahrscheinlich Branchenthemen (Speicherpreise/KI-Sentiment/Zyklizität)
```

**Earnings-Blackout-Check (Perplexity Di-Do 07.-09.07.):**
- JPM, UNH, MU, LLY: **keine Earnings** in nächsten 3 Handelstagen (S&P 500 Earnings-Welle startet erst Mitte Juli — JPM/Banken KW29-30)
- Watchlist GOOGL, CAT, MS, AAPL: keine Earnings vor Mitte Juli (GOOGL 22.07. carry-over ✓)
- **Kein Blackout aktiv** → keine Stop-Loss-Verengung auf -5 %

**Guardrail-Status Pre-Market:**
```
1. Daily Loss Cap (-3 %):    -0,206 %   → GRÜN (Puffer -2,79 %)
2. Weekly Loss Cap (-5 %):   -0,206 %   → GRÜN
3. Drawdown-Alarm (-15 %):   -0,856 %   → GRÜN (ATH 100.066,47)
4. Drawdown-Stopp (-20 %):   -0,856 %   → GRÜN
5. Crash-Filter SPY -5 %:    Mo +0,86 % → INAKTIV
6. VIX-Filter > 30:          ~16        → GRÜN
7. Earnings-Blackout:        keine      → GRÜN
8. Käufe/Woche max 2:        1/2        → 1 Slot frei
```
**Alle Guardrails GRÜN — aber MU-V1-Pre-Market-Alarm überlagert Kauf-Entscheidung.**

**Entscheidung Market-Open-Scan (09:30 ET):**
- **Priorität 1:** MU-V1-Überwachung — bei Open unter 954,71 $ → sofort Market Sell 9 Shares (siehe market-open-routine.md V1-Handling)
- **Priorität 2:** Falls MU-V1 auslöst → Kauf-Scan zurückstellen (Cash-Erholung + Portfolio-Reset zuerst)
- **Priorität 3:** Falls MU-V1 NICHT auslöst (Open ≥ 954,71 $ oder Rebound) → GOOGL K1-K5 Live-Recheck möglich, 1 Kauf-Slot frei
- Watchlist unverändert: GOOGL (Lead), CAT (Backup K5-Recheck), MS (Timing-Vorbehalt), AAPL (Fallback)

**Datenqualitäts-Hinweise:**
- Alpaca `current_price` in Pre-Market = letzter Trade/Quote, kein offizieller Open-Preis → V1-Trigger erst bei Regulär-Session-Preis
- Perplexity SPY-Premarket-Range 0,3-0,6 % unspezifisch (Inference-Marker) — Ground-Truth aus Alpaca-SPY-Quote bei Market Open zwingend
- Perplexity 10Y-Yield als Inference (kein direkter Live-Feed im Search) — bestätigt aus News nur Größenordnung

**ClickUp:** [PRE-MARKET] Check Task angelegt Prio 3 (statt 4 wegen MU-V1-Alarm-Kontext).

**Nächste Routine:** Di 07.07. 09:30 ET Market Open — **MU-V1-Handling zwingend als erster Schritt**, dann Kauf-Scan bei sicherem Portfolio.

---

## Market Close 16:00 ET — 2026-07-06 (Mo, KW28) — Tagesbilanz + Watchlist Di 07.07.

**Tagesbilanz:** Portfolio -0,173 % (-172,06 $) | SPY IEX +0,861 % (Do 02.07. 744,86 → Mo 06.07. 751,27; Fr Feiertag) | **Alpha -1,034 %** | Positionen 4/8 (JPM +1,76 % / UNH +3,94 % / MU -6,69 % / LLY +0,79 %) | Käufe KW28 1/2 nach LLY-Fill | Guardrails alle GRÜN | Weekly KW28 -0,173 % (kein Cap-Trigger).

**Sektor-Performance heute (Alpaca IEX):**
```
XLK +1,70 % | XLF +0,96 % | XLI +0,88 % | XLY +0,74 % | XLC +0,57 %
XLB -0,08 % | XLE -0,15 % | XLRE -0,92 % | XLU -1,02 % | XLV -1,04 % | XLP -1,07 %
VXX -2,63 % (Vola-Entspannung fortgesetzt, VIX ~15-16)
```
→ **Rotation weg von Defensives (XLV/XLU/XLP -1 %) hin zu Tech/Financials (XLK +1,70 %/XLF +0,96 %)**. Bot-XLV-Overweight (UNH+LLY 19,79 %) erklärt Alpha-Miss -1,03 % strukturell.

**V1–V6-Check ALLE 4 POSITIONEN SICHER (nach Close-Recalc EMA/RSI aus Alpaca IEX 211d):**
- JPM V1 +10,61 % / V5 EMA-Spread +8,59 ✓ / V6 RSI 66 & RS +9,65 % → SICHER
- UNH V1 +12,97 % / V5 EMA-Spread +48,53 ✓ / V6 RSI 59 & RS +6,55 % → SICHER
- **MU V1 nur +1,42 %** [KRITISCH — verengt von Midday +4,89 %] / V5 EMA-Spread +416,54 ✓ / V6 RSI 49 & RS -1,10 % → SICHER (V6 verlangt BEIDES RSI>80 UND RS<0)
- LLY V1 +9,55 % / V5 EMA-Spread +104,46 ✓ / V6 RSI 65 & RS +7,23 % → SICHER

→ **Keine Verkaufsorder für Di 07.07. vorbereitet.** Pending Orders bleiben 0.

**Watchlist-Screen K1-K3 (Alpaca 06.07.-Close, SPY_RS_63d = +14,86 %):**
```
Sym    Live       K1 EMA50>200      K2 RSI      K3 RS_63d vs SPY   Sektor
GOOGL  366,34    ✓ 358,90>314,48   ✓ 53,59     ✓ RS +9,11 %       XLC (leer)
CAT    969,52    ✓ 914,19>701,19   ✓ 51,65     ✓ RS +20,55 %      XLI (leer)
MS     222,07    ✓ 205,22>178,34   ✓ 60,39     ✓ RS +19,81 %      XLF (JPM 1 %)
AAPL   312,73    ✓ 291,29>270,14   ✓ 63,16     ✓ RS +7,47 %       XLK (Konflikt MU)
BAC     59,90    ✓ 54,48>52,31     ✗ 74,52 (>70) ✓ RS +7,14 %     XLF (K2 ✗)
NVDA   195,59    ✓ 203,70>190,45   ✓ 42,24     ✗ RS -4,42 %       XLK (K3 ✗)
DE     635,40    ✓ 586,12>533,08   ✓ 64,97     ✗ RS -4,14 %       XLI (K3 ✗)
```

**Watchlist morgen (Ranking):**
1. **GOOGL** LEAD — 5/5-Bild stabil vom Mo Open (K5 carry ✓ FwdPE 21,87/28,65 ≤35, Rev +11,33 % ≥10 %); XLC leer → keine Sektor-Konflikte; Earnings 22.07. (11 HT sicher)
2. **CAT** Backup — RS 2. höchste (+20,55 %), XLI-Sektor leer; K5 RevGrowth Q1 -1 % **Recheck Multi-Source zwingend** vor Buy; Earnings ~05.08.
3. **MS** Timing-Vorbehalt — 5/5 aber Earnings 15.07. → 3-HT-Blackout ab Fr 10.07. Close = Kauf Di gäbe **nur 3 HT Puffer** (Di/Mi/Do), sehr eng
4. **AAPL** Only-If — XLK-Konflikt MU + K5 offen

**Watchlist morgen: GOOGL (Lead), CAT (Backup, K5-Recheck), MS (Timing-Vorbehalt), AAPL (Fallback).**

**Datenqualitäts-Hinweise:**
- Perplexity Sektor-Query heute leer (Datum-in-Zukunft-Bug carry-over) → Alpaca ETF-Marks als Fallback
- Alpaca IEX 211d-Bars verfügbar für alle Positionen + Watchlist → EMA50/200/RSI(14) live berechnet
- SPY IEX +0,861 % als Ground-Truth (Perplexity nannte +0,78 % — moderate Diskrepanz)
- LLY Alpaca lastday_price 1213,91 (vs Memory Do 02.07. Close 1210,79 — After-Hours-Tick)

**ClickUp:** [CLOSE] Tagesbilanz Task angelegt Prio 3 (leicht negative Performance, Alpha negativ). Push-Notification Fallback bei ITEM_246 Tier-Limit.

**Nächste Routine:** Di 07.07. 08:30 ET Pre-Market Check (KW28 Tag 2, MU-V1-Puffer +1,42 % kritisch, GOOGL/CAT/MS Watchlist-Recheck).

---

## Market Open 09:41 ET — 2026-07-06 (Mo, KW28) — **LLY LIMIT-ORDER PLACED (5/5, K5 Multi-Source ✓)**

**Alpaca Clock:** is_open=true (09:37 ET), next_close 06.07. 16:00 ET. **NYSE offen KW28 Mo.**

**Account Live 09:41 ET:**
```
Equity:            99.541,20 $   (vs last_equity 99.420,34 → +0,121 % Daily) [GRÜN]
Cash:              79.428,25 $   (79,79 %)
Long MV:           20.112,95 $   (20,21 %; JPM 1.014,15 + UNH 10.090,32 + MU 9.008,48)
SPY Live:            748,11 $    (+0,55 % vs Do 02.07. 744,86 → moderate risk-on)
VIX:                ~16          (Multi-Source ~16 carry-over Pre-Market)
Crash-Filter:       INAKTIV       (SPY +0,55 %)
Guardrails 8/8:     ALLE GRÜN     (Daily +0,12 % | Weekly +0,12 % | DD -0,53 % | VIX ~16 | Käufe 1/2)
```

**Positionen V1–V6 Live:**
- JPM 338,05 $ (+1,58 %, V1-Puffer +9,54 %) → alle SICHER
- UNH 420,43 $ (+4,69 %, V1 +13,80 %, V2 378,48 getrailt) → alle SICHER
- MU  1.001,12 $ (-3,53 %, V1-Puffer +4,86 % **ENTSPANNT** vs Fr-Close +2,19 %) → alle SICHER
→ **Keine Verkaufsorder.**

**Kandidaten-Scan (Alpaca 200d IEX Bars + Perplexity K5 06.07.):**
| Sym | Live | K1 | K2 RSI | K3 RS vs SPY (+14,07 % 63d) | K4 Proj | K5 | Score |
|-----|------|-----|--------|-----------------------------|---------|-----|-------|
| GOOGL | 361,72 | ✓ EMA50 358,17>316,50 | ✓ 50,73 | ✓ +8,24 % | ✓ 220 % | ✓ FwdPE 21,87/28,65 ≤35, Rev +11,33 % | 5/5 Backup |
| **LLY** | 1199,90 | ✓ 1089,02>987,10 | ✓ 64,34 | ✓ **+14,16 %** | ✓ 242 % | ✓ FwdPE 34,51/32,69/32,53 ≤35, Rev +47,43 % | **5/5 LEAD** |
| MS | 219,62 | ✓ 204,77>178,92 | ✓ 58,26 | ✓ +18,40 % | ✓ 150 % | ✓ carry-over aber Earnings 15.07. Blackout ab 10.07. | 5/5 Timing-Vorbehalt |
| CAT | 984,00 | ✓ | ✓ 53,30 | ✓ +23,10 % | ✓ 371 % | ✗ RevGrowth Q1 -1 % | 4/5 K5 ✗ |
| AMD | 540,73 | ✓ | ✓ 55,73 | ✓ +134,27 % | ✓ 533 % | ✗ FwdPE 35-95x + XLK-Konflikt | 4/5 K5 ✗ |
| AAPL | 309,28 | ✓ | ✓ 61,25 | ✓ +6,80 % | ✓ 168 % | ? Recheck + XLK-Konflikt | 4/5 K5 offen |

**Perplexity K5 Multi-Source LLY (06.07.):**
- FwdPE: **34,51** [intellectia.ai 04.07.] / **32,69** [valueinvesting.io] / **32,53** [finbox] → **Median ~32,7 ≤35** ✓
- RevGrowth Q1 2026 YoY: **+47,43 %** [Perplexity Source 8] → ≥10 % ✓
- Sektor: XLV Healthcare (Pharma) bestätigt
- Earnings Q2 2026: **05.08.2026 BMO** — 4-Source-Konsens (MarketBeat + LLY IR Webcast 05.08. 10:00 EDT + MarketChameleon + Nasdaq/Zacks 06.08. algo) → 22 HT ab heute → 3-HT-Blackout ab 31.07. Close → JETZT NICHT AKTIV

**Perplexity K5 GOOGL (06.07.):**
- FwdPE: 21,87 [GuruFocus] / 28,65 [Chartloom] → ≤35 ✓
- RevGrowth: 11,33 % Q1 2026 estimate → ≥10 % ✓
- Sektor XLC bestätigt; Earnings unbestätigt, "late July or early August" — Weekly-Review 22.07. → 12+ HT Puffer

**Ranking (Strategie: höchste RS + alle 5 grün):**
1. AMD +134 % → K5 ✗ OUT
2. CAT +23 % → K5 ✗ OUT
3. MS +18 % → 5/5 aber Earnings 15.07. → 4 HT Puffer bis Blackout → **Downgrade Backup**
4. **LLY +14,16 % → 5/5 grün, Earnings safe (22 HT) → LEAD**
5. GOOGL +8,24 % → 5/5 grün, XLC-Diversifikation → Backup
6. AAPL +6,80 % → K5 offen → OUT

**LLY-Order (Alpaca):**
```
Order-ID:   f6364db0-8a8f-4a11-b305-26a4874f1f6d
Symbol:     LLY | BUY LIMIT | 8 Sh | 1.216,84 $ | Day | Status NEW/pending
Berechnung: prev_close 1.210,79 (Do 02.07.) * 1,005 = 1.216,84 ; sizing floor(99541,20*0,10/1199,90) = 8
Max-Cost:   9.734,72 $ (9,78 % Portfolio)
```

**Sektor-Check bei Fill:** XLF 1,02 % + XLV 19,92 % (UNH+LLY) + XLK 9,05 % = 29,99 % investiert; XLV Total unter 30 %-Cap ✓, 2/3 XLV-Positionen ✓; Positionen 4/8.

**Bei Fill:** V1 = fill*0,92; V2 = Posit-Hoch*0,88; V3 = fill*1,20; V4 = fill*1,35. ClickUp TRADE_BUY Prio 3 (Fallback Push).
**Bei kein Fill bis 16:00 ET:** Day-Order verfällt, KW28 zurück 0/2.

**Zusammenfassung (routine-schema):**
```
Scans:               6 Kandidaten (GOOGL, LLY, MS, CAT, AMD, AAPL)
Kaufsignal:          LLY (5/5, höchste RS unter K5-grünen + Earnings-safe)
Trade platziert:     JA — LLY BUY LIMIT 8 Sh @ 1.216,84 Day (pending)
Käufe KW28:          1/2
Portfolio nach Scan: 99.541 $ Gesamt, 20,21 % investiert (Fill hebt auf ~30 %)
```

**Datenqualität:**
- Perplexity Multi-Symbol lieferte nur LLY, GOOGL separate Query nötig → Prompt-Split-Strategie
- LLY-FwdPE 34,51 knapp unter 35 → K5 grün, grenzwertig, Weekly-Review-Recheck
- Alpaca IEX-Live-Ask sprang auf 1.270,50 (dünne IEX-Liquidität, letzter Trade 1.192,75 gültig)

**ClickUp:** TRADE_BUY Alert Prio 3 (Push-Notification Fallback wegen ITEM_246 Tier-Limit carry-over).

**Nächste Routine:** Mo 06.07. 13:00 ET Midday Stop-Check (LLY-Fill-Status + V1–V4).

---

## Pre-Market 08:35 ET — 2026-07-06 (Mo, KW28 Start) — Guardrails GRÜN, MU-Gap-Up entspannt V1-Puffer, Buy-Scan JA

**Makro-Lage (Pre-Market 08:35 ET, Alpaca IEX + Perplexity):**
```
VIX Spot Live:      15,81 (CBOE Futures) / 16,32 (Yahoo)     [GRÜN — <25 → 10 % Sizing erlaubt]
VIX Close 02.07.:   16,15 (letzter offizieller Print, Fr 03.07. Feiertag)
SPY Premarket:      N/A via Alpaca IEX (letzter Quote t=2026-07-02T20:00Z = After-Hours Do 02.07. Close)
                    ap 762,42 / bp 724,91 → sehr weite Spread (dünne PM-Liquidität), nicht verwertbar
                    Perplexity SPY-PM: N/A (Datum-in-Zukunft-Bug carry-over)
SPY Do 02.07. Close: 744,86 (Alpaca IEX 1Day-Bar)
VIXY Quote:         ap 21,95 / bp 20,55 (t 2026-07-02T20:00Z = After-Hours) → Spot ~16 konsistent
10Y Treasury Yield: N/A (Perplexity leer, carry-over Bug)
Crash-Filter:       INAKTIV (SPY Do -0,108 % → weit von -5 %)
Markt-Status:       CLOSED (Alpaca is_open=false, next_open 06.07. 09:30 ET, next_close 06.07. 16:00 ET)
```

**Alpaca Account-Status (Konsistenz-Check):**
```
Equity:             99.682,06 $    (vs last_equity 99.420,34 → +261,72 $ / +0,263 % Pre-Market-Tick, hauptsächlich MU-Gap-Up)
Cash:               79.428,25 $    (identisch zu Memory Fr-Close, 79,68 %)
Last_Equity:        99.420,34 $    (identisch zu Memory Fr-Close ✓)
Long Market Value:  20.253,81 $    (JPM 999,36 + UNH 10.180,56 + MU 9.073,89)
Status:             ACTIVE         (trading_blocked=false, PDT=false, DayTrade=0)
Buying Power:       374.423,67 $
Open Orders:        0
Positions Live (Pre-Market Marks):
- JPM 333,12 $ (change_today -0,404 %, P/L +0,102 % vs Entry 332,78)
- UNH 424,19 $ (change_today -0,275 %, P/L +5,63 % vs Entry 401,57)
- MU  1.008,21 $ (change_today +3,347 %, P/L -2,844 % vs Entry 1.037,72) — GAP UP!
```

**Reconciliation Memory ↔ Alpaca:**
- portfolio.md Fr-Close 99.420,34 ↔ Alpaca last_equity 99.420,34 → **exakt konsistent ✓**
- cash 79.428,25 identisch ✓
- lastday_price = Fr-Close Marks (JPM 334,47 / UNH 425,36 / MU 975,56) ↔ Memory identisch ✓
- Positionen-Anzahl & avg_entry konsistent (JPM 3@332,78 / UNH 24@401,57 / MU 9@1037,72)

**Guardrails-Check (alle 8 Hierarchien, KW28 Reset):**
```
1. Daily Loss Cap (-3 %/Tag):     +0,263 % (99.682,06 vs last_equity 99.420,34)    [GRÜN]
2. Weekly Loss Cap (-5 %/Woche):   0,000 % (KW28 Mo-Basis = Fr-Close 99.420,34)    [GRÜN — Reset]
3. Drawdown vom ATH (-15 %):      -0,384 % (99.682,06 vs ATH 100.066,47)           [GRÜN — 14,6 %-Puffer]
4. Drawdown-Stopp (-20 %):        INAKTIV
5. Crash-Filter (SPY -5 %/Tag):   INAKTIV (Do 02.07. -0,108 %; Fr 03.07. Feiertag)
6. VIX-Filter (>30):              INAKTIV (Spot ~16 → sehr klar GRÜN → 10 % Sizing)
7. Earnings-Blackout (3 HT):      KEINER — JPM 14.07. BMO CONFIRMED (7 HT ab heute, Blackout ab 09.07. Close);
                                  UNH 16.07. carry-over unbestätigt (Blackout ab 13.07.); MU Q4 typisch Ende Sept
8. Max neue Käufe KW28:           0/2 genutzt → 2 frei (Reset Mo)
```
→ **STATUS: ALLE 8 GRÜN.**

**Positionen Signal-Recheck (Pre-Market V1–V6, Live-Marks):**
```
JPM  333,12 $ — V1 306,16 SICHER +8,81 % Puffer | V2 ~302,11 SICHER +10,26 % (Posit-Hoch 343,31 carry-over 25.06.)
              | V5 EMA50 315,32 > EMA200 306,00 ✓ carry-over | V6 RSI 62,83 / RS +12,30 % → KEIN Trigger
UNH  424,19 $ — V1 369,44 SICHER +14,81 % Puffer | V2 378,48 (getrailt 02.07. auf Hoch 430,095) SICHER +12,08 %
              | V5 EMA50 385,12 > EMA200 342,87 ✓ carry-over | V6 RSI 64,76 / RS +13,97 % → KEIN Trigger
MU  1.008,21 $ — V1 954,71 SICHER **+5,60 % Puffer** [ENTSPANNT vs Fr-Close +2,19 %, Gap-Down-Risiko abgewendet]
              | V2 913,39 (Posit-Hoch 1.037,94 = Fill-Preis carry-over) SICHER +9,40 %
              | V3 1.245,26 / V4 1.400,92 — nicht erreicht
              | V5 EMA50 882,15 > EMA200 507,23 ✓ (Spread +374 sehr breit) carry-over
              | V6 RSI 48,57 / RS -8,42 % → NICHT ausgelöst (V6 verlangt RSI>80 UND RS<0)
```
→ **Keine Verkaufsorder pending, alle V1–V6 SICHER.** MU-V1-Puffer weitet sich auf +5,60 % (vs Fr-Close +2,19 %) durch Pre-Market Gap-Up +3,35 % — kritischer Gap-Down-Fall vom Weekend abgewendet.

**Earnings-Verifikation (Perplexity 06.07.):**
- **JPM Q2 2026: 2026-07-14 BMO CONFIRMED** — Multi-Source: Business-Wire, MarketBeat, WallStreetHorizon, Public, MarketChameleon, JPM IR. Konsens EPS 5,59, Q2-Call 8:30 ET, Report ~7:00 ET. **7 HT ab heute** (Mo 06, Di 07, Mi 08, Do 09, Fr 10, Mo 13, Di 14). 3-HT-Blackout aktiv ab **09.07. Close (Do)** → JETZT NICHT AKTIV.
- **UNH Q2 2026:** Perplexity UNCONFIRMED heute → carry-over 2026-07-16 → ~8 HT → Blackout aktiv ab **13.07. Close (Mo)** → JETZT NICHT AKTIV.
- **MU Q4 FY2026:** Perplexity nennt "23.07.2026 BMO" (nicht bestätigt, MarketBeat/WSH nicht in Quellen); Memory-carry-over sagt "typisch Ende September". → Widerspruch. Aktuell weit außerhalb 3-HT-Blackout. Recheck erforderlich bei nächster Routine wenn <10T entfernt.
- Andere S&P 500/MidCap-Earnings 06.-08.07.: **KEINE bestätigt** (Perplexity leer).
- → Standard V1-Stops bleiben für alle 3 Positionen (kein Stop-Tightening auf -5 %).

**News overnight/weekend (Perplexity + carry-over aus Fr-Pre-Market):**
- Chipmakers-Selloff-Debatte (AI-Buildout-Nachhaltigkeit) carry-over — **MU-relevanter Kontext**, RS +191 % 63d bleibt sensibel; MU-Pre-Market +3,35 % zeigt aber Rebound-Beginn
- S&P 500 2-Wochen-Hoch, DJIA neues ATH per Do 02.07. Close (kein Handel Fr)
- Fed-Rate-Hike-Sorgen abgeflaut nach schwachem Jobs-Bericht (carry-over)
- **Keine großen Makro-Releases heute** (Perplexity: kein FOMC/CPI/NFP/ISM heute)

**Watchlist Mo 06.07. Market Open (carry-over Fr-Weekly-Review + Fr-Pre-Market):**
```
Symbol | Sektor | Score | K1-K3 (carry) | K4 (Open-Check) | K5 (Recheck)                  | Earnings
GOOGL  | XLC    | LEAD  | ✓✓✓ carry     | Live-Vol         | FwdPE 27,45 ✓ / Rev +22 % ✓ | 22.07. (>10 HT, sicher)
MS     | XLF    | 3/5   | ✓✓✓ carry     | Live-Vol         | FwdPE 21,58 ✓ / Rev +16,4 % ✓ | 15.07. → BLOCK 10T-Blackout ab 10.07. Close (heute noch OK, aber Buy heute + Blackout ab Fr → Timing prüfen)
LLY    | XLV    | 4/5   | ✓✓✓ carry     | Live-Vol         | FwdPE 32-33 ✓ / Rev +26 %    | ~25.07. (>10 HT)
CAT    | XLI    | 3/5   | ✓✓✓ carry     | Live-Vol         | Rev -1 % ✗ Recheck            | ~05.08. (>10 HT)
AMD    | XLK*   | 3/5   | ✓✓✓ carry     | Live-Vol         | FwdPE ✗ Recheck               | ~05.08. (>10 HT); *Konflikt MU
AAPL   | XLK*   | ?     | ✓✓✓ carry     | Live-Vol         | ? Recheck                     | ~30.07. (>10 HT); *Konflikt MU
```

**Sektor-Belegung Pre-Market 06.07.:** JPM XLF 1,00 % + UNH XLV 10,21 % + MU XLK 9,10 % = 20,31 % investiert. 3/8 Slots. XLC/XLI/XLE/XLU/XLB/XLY/XLP leer → viel Diversifikations-Raum. **GOOGL XLC füllt Lücke ohne Konflikt.**

**Entscheidung 09:30 ET Market Open:**
- **Buy-Scan JA** — alle 8 Guardrails GRÜN, VIX sehr entspannt (~16), MU-Gap-Up entlastet V1-Watch
- **Lead-Kandidat: GOOGL** (XLC-Diversifikation, K5 sauber laut Weekly-Review-Prep, Earnings 22.07. sicher außerhalb 10T-Blackout)
- **Backup: LLY** (XLV zusammen mit UNH aber unter 30 %-Cap, K5 ✓, K4 abhängig von Live-Vol)
- **MS Timing-Vorbehalt:** Earnings 15.07. → 10T-Blackout ab 10.07. Close. Bei Kauf heute Mo 06.07. verbleiben nur 4 HT ohne Blackout — wenn V-Trigger vor 10.07. nicht feuert, kommt Blackout während Position-Hold. Regel bezieht sich auf **3-HT-Blackout vor Earnings** (nicht 10T), also Kauf Mo möglich, aber Stop-Tightening auf -5 % ab Fr 10.07. Close nötig. → **MS bleibt Backup, aber vorsichtiger.**
- **AMD/AAPL/CAT:** Recheck-Bedarf, kein Lead-Status
- Fallback: kein Trigger → 0/2 KW28-Slots bleiben frei

**Datenqualitäts-Hinweise:**
- SPY-Premarket via Alpaca IEX nicht verwertbar (After-Hours-Quote Fr-Feiertag), Perplexity ebenfalls leer
- Perplexity Datum-in-Zukunft-Bug carry-over für SPY-PM, 10Y, US-Kalender
- VIX ~16 verifiziert Multi-Source (CBOE, Yahoo, CNBC)
- Alpaca Broker-Marks für alle 3 Positionen konsistent mit Fr-Close-Memory

**ClickUp:** ROUTINE Log-Notification Prio 4 (Push-Notification-Fallback via ITEM_246 Tier-Limit carry-over, Payload mit `custom_item_id: null`).

**Nächste Routine:** Mo 06.07. 09:30 ET Market Open — Buy-Scan GOOGL Lead, Backup LLY/MS.

---

## Market Open 09:37 ET — 2026-07-03 (Fr, KW27) — **NO-OP, NYSE geschlossen (Independence Day observed)**

**Cron-Trigger:** Routine feuerte planmäßig 13:30 UTC (09:30 ET). Wie im Pre-Market 08:35 ET bereits festgestellt und dokumentiert: NYSE ist heute geschlossen (04.07. Samstag → Feiertag auf Fr 03.07. verschoben).

**Alpaca Clock Re-Verifikation (09:37 ET Live):**
```
is_open:      false
next_open:    2026-07-06T09:30:00-04:00
next_close:   2026-07-06T16:00:00-04:00
timestamp:    2026-07-03T09:37:07-04:00
```
**Alpaca Calendar 03.07.–07.07.:** Nur Einträge für 06.07. (Mo) und 07.07. (Di). **03.07. fehlt vollständig → kein Handelstag.**

**Ausgeführte Schritte gemäß market-open-routine.md:**
- Schritt 1 (Memory laden): ✓ strategy/portfolio/trade-log/research-log gelesen
- Schritt 2 (Guardrails-Check): entfällt — kein Handel möglich (alle 8 Levels GRÜN carry-over aus Pre-Market)
- Schritt 3 (Stop-Loss-Check offene Positionen): entfällt — keine Orders platzierbar (Alpaca akzeptiert keine Orders für Feiertagsdatum). V1–V6 alle SICHER (JPM/UNH/MU) carry-over aus 02.07. Close bzw. Pre-Market After-Hours-Marks
- Schritt 4 (Kandidaten-Scan): entfällt — kein Live-Marktdaten-Handel, keine Kauforder möglich
- Schritt 5 (Kauf ausführen): entfällt
- Schritt 6 (Memory + Log): dieser Eintrag

**Zusammenfassung:**
```
Scans durchgeführt:      0 (Markt geschlossen)
Kaufsignal:              KEINER (nicht anwendbar)
Trade ausgeführt:        NEIN (nicht möglich)
Käufe diese Woche:       1/2 (KW27 unverändert nach MU-Fill 02.07.)
Portfolio nach Scan:     99.420 $ Gesamt, ~20 % investiert (After-Hours-Marks unverändert)
Positions Live V1-V6:    JPM/UNH/MU alle SICHER; MU-V1-Puffer +2,14 % (After-Hours) bleibt engste Watch-Position, aber keine Order platzierbar bis Mo 06.07. Pre-Market
```

**Nächste Routine:** Fr 2026-07-03 17:00 ET Weekly Review (KW27-Bilanz, MU-Fill-Analyse). Dann Mo 2026-07-06 08:30 ET Pre-Market Check (KW28-Start).

**ClickUp:** ROUTINE Log-Notification Prio 4 (Push-Notification-Fallback wegen ITEM_246 Tier-Limit carry-over).

---

## Pre-Market 08:35 ET — 2026-07-03 (Fr, KW27) — **NYSE GESCHLOSSEN** (Independence Day observed), Guardrails GRÜN, kein Scan

**KORREKTUR zur Memory-Annahme:** Alpaca `/v2/clock` liefert `is_open:false`, `next_open:2026-07-06T09:30-04:00`. NYSE-Kalender-Query 03.07.→06.07. liefert NUR den Eintrag 2026-07-06 (Mo). → **Heute ist KEIN Handelstag, auch kein verkürzter HT.** Die Notiz vom Close 02.07. "verkürzter HT bis 13:00 ET" war falsch — NYSE-Regel: fällt 04.07. auf Samstag, wird der Feiertag auf Freitag 03.07. verschoben (nicht verkürzt). Perplexity bestätigt: "US stock market **CLOSED** today (Friday, July 3, 2026) — Independence Day observed."

**Makro-Lage (08:35 ET, Perplexity):**
```
VIX Spot:            16,15         [GRÜN — sehr entspannt, 02.07. Close via Perplexity; kein Live-Update mangels Handel]
SPY Premarket:       N/A            (Markt geschlossen, kein Premarket-Handel)
10Y Treasury Yield:  N/A            (Perplexity leer)
Crash-Filter:        INAKTIV        (SPY 02.07. -0,108 % → weit von -5 %)
NYSE-Status:         GESCHLOSSEN    (next_open 2026-07-06 09:30 ET)
```

**Alpaca Account (Konsistenz-Check):**
```
Equity:              99.420,34 $    (= last_equity, kein Handel → 0 % day-change)
Cash:                79.428,25 $    (identisch zu Memory 79.428,26; -0,01 $ Rundung)
Long Market Value:   19.992,09 $    (After-Hours-Marks: JPM 1.003,41 / UNH 10.208,64 / MU 8.780,04)
Portfolio-Value:     99.420,34 $    (vs Memory Close 02.07. 99.413,51 → +6,83 $ After-Hours-Tick, akzeptabel)
Status:              ACTIVE / trading_blocked=false / PDT=false / daytrade_count=0
Buying Power:        373.690,85 $
Open Orders:         0
```

**Positionen (After-Hours-Marks, KEIN Handel möglich heute):**
- **JPM** 334,47 $ (P/L +0,51 %, ct 0) — carry-over vom 02.07. Close, keine Änderung
- **UNH** 425,36 $ (P/L +5,92 %, ct 0) — +0,25 % After-Hours-Tick vs Close 424,28 (kein neuer Trigger)
- **MU**  975,56 $ (P/L -5,99 %, ct 0) — **-0,25 % After-Hours-Tick vs Close 978,00**; V1 954,71 → Puffer **+2,14 %** (Close war +2,38 %) → weiter eng, aber KEIN Trigger möglich mangels Handel

**Guardrails-Check (8 Hierarchien):**
```
1. Daily Loss Cap (-3 %/Tag):     0,000 % (kein Handel)                 [GRÜN]
2. Weekly Loss Cap (-5 %/Woche): -0,604 % (99.420,34 vs KW27-Basis 100.024,25) [GRÜN]
3. Drawdown vom ATH:             -0,650 % (vs ATH 100.066,47)           [GRÜN — Alarm bei -15 %]
4. Drawdown-Stopp -20 %:          INAKTIV
5. Crash-Filter (SPY -5 %):       INAKTIV (02.07. -0,108 %)
6. VIX-Filter (>30):              INAKTIV (16,15)                       [GRÜN → 10 % Sizing]
7. Earnings-Blackout (3 HT):      KEINER — JPM 14.07. BMO (Perplexity heute CONFIRMED); UNH 16.07. carry-over; MU Q4 ~Ende Sept
8. Max neue Käufe KW27:           1/2 (MU 02.07.) → 1 Slot theoretisch frei, aber KW27 endet heute → praktisch nicht mehr nutzbar
```
→ **STATUS: GRÜN auf allen 8 Levels.**

**V1–V6-Recheck (After-Hours, keine Order möglich):**
- JPM/UNH: alle V1–V6 SICHER wie Close 02.07. (V-Trigger-Levels unverändert)
- **MU: V1-Puffer After-Hours +2,14 %** (975,56 vs V1 954,71). V5 EMA-Spread +374 sehr breit, V6 RSI 48 unter 80 → keine Trigger, aber V1 kritisch eng.
- **Kein Order-Placement möglich (Alpaca akzeptiert Orders nur außerhalb Feiertag → Mo 06.07. Pre-Market).**

**Earnings-Verifikation (Perplexity 03.07.):**
- JPM Q2 2026: **2026-07-14 BMO (CONFIRMED)** — vorher Pre-Market 02.07. hatte "07-15 AMC". Diskrepanz erneut, aber weiter 6 HT entfernt (ab Mo 06.07. gezählt: Mo 06, Di 07, Mi 08, Do 09, Fr 10, Mo 13, Di 14 = 7 HT). 3-HT-Blackout aktiv ab **09.07. Close** (Do). → JETZT NICHT AKTIV.
- UNH Q2 2026: Perplexity UNCONFIRMED → carry-over 2026-07-16 (7 HT ab Mo) → 3-HT-Blackout aktiv ab **13.07.** → JETZT NICHT AKTIV.
- MU Q4 FY2026: Perplexity UNCONFIRMED → typisch Ende September → weit weg.

**News overnight (Perplexity):**
- Chipmakers-Selloff wegen AI-Buildout-Nachhaltigkeitsdebatte (MU-relevanter Kontext, RS +191 % 63d — Sektor-Sensitivität hoch)
- S&P 500 2-Wochen-Hoch, DJIA neues ATH (02.07. Close, kein Handel heute)
- Fed-Rate-Hike-Sorgen abgeflaut nach schwachem Jobs-Bericht (10Y-Signal indirekt)

**Watchlist (carry-over für Mo 06.07.):**
- MS 213,89 | XLF-Diversifikation, K1-K3 ✓, K4/K5 Open-Check
- CAT 963,60 | XLI-Slot leer, K1-K3 ✓, K5 RevGrowth-Recheck
- LLY 1210,79 | XLV, K5 ✓, K4 wartet
- AMD 518,25 | XLK (Sektor-Konflikt MU), K5 FwdPE-Recheck; **AI-Chip-Selloff-Kontext beachten**
- AAPL 308,24 | XLK (Sektor-Konflikt MU), K4/K5 Open-Check

**Datenqualität:** Alpaca Clock+Calendar sind Ground-Truth für Marktstatus. Perplexity bestätigt NYSE-Closure. Perplexity SPY-Premarket + 10Y = N/A (durch geschlossenen Markt bedingt, kein Bug).

**Entscheidung Fr 03.07.:**
- **Kein Market-Open-Scan** (Markt geschlossen)
- **Keine Midday-Routine** (Markt geschlossen)
- **Keine Market-Close-Routine** (Markt geschlossen, keine Bewegung → Portfolio bleibt auf 02.07.-Close-Basis)
- Käufe KW27 abgeschlossen bei 1/2 (nur MU gefillt)
- MU-V1-Puffer bleibt kritische Watch-Position → **Pre-Market Mo 06.07. 08:30 ET zwingend**, danach Market Sell sofort möglich falls Gap-Down MU <954,71
- Weekly Review Fr 03.07. 17:00 ET (per Zeitplan) — heute noch fällig, aber ohne Intraday-Bewegung reduziert sich der Umfang auf KW27-Bilanz (MU-Fill-Analyse zentral)

**Nächste Routine:** Mo 06.07. 08:30 ET Pre-Market Check (KW28 startet, Käufe-Zähler reset 0/2, MU-V1-Puffer weiter überwachen); dazwischen Fr 03.07. 17:00 ET Weekly Review.

**ClickUp:** ROUTINE Log-Notification (Prio 4) siehe unten.

---

## Market Close 16:02 ET — 2026-07-02 (Do, KW27) — Watchlist für Fr 03.07. (verkürzter HT bis 13:00 ET)

**Tagesbilanz:** Portfolio -0,593 % (-593,40 $) | SPY -0,108 % | Alpha -0,485 % | Positionen 3/8 (JPM +0,51 % / UNH +5,66 % / MU -5,75 % Fill-Day) | Käufe KW27 1/2 nach MU-Fill | Guardrails alle GRÜN.

**Perplexity-Sektor-Query 02.07. (Watchlist-Support):** Query lieferte KEINE spezifischen Kandidaten (allgemeine SPX-Daten ohne Titel-Detail) — Datum-in-Zukunft-Bug carry-over aus Pre-Market/Midday. SPY-Tagesperformance Perplexity leer (Alpaca IEX bestätigt -0,108 %). **Fallback: Alpaca-basiertes RS-63d-Screening auf 31-Titel-Universe.**

**Watchlist-Screen K1-K3 (Alpaca 02.07. Close, SPY_RS_63d = +13,69 %):**
```
Sym  Last     EMA50   EMA200  RSI     RS_63d vs SPY  K1 K2 K3  Score  Sektor
AMD  518,25   455,87  306,29  52,49   +132,84 %      ✓  ✓  ✓   3/3   XLK (MU!)
ELV  417,45   383,06  352,13  62,38   +26,12 %       ✓  ✓  ✓   3/3   XLV (UNH!)
CAT  963,60   913,55  710,44  50,92   +18,28 %       ✓  ✓  ✓   3/3   XLI leer
MS   213,89   204,26  179,26  52,51   +15,03 %       ✓  ✓  ✓   3/3   XLF (JPM!)
LLY 1210,79  1084,58  964,14  67,06   +13,13 %       ✓  ✓  ✓   3/3   XLV (UNH!)
AAPL 308,24   290,47  266,57  60,74    +6,99 %       ✓  ✓  ✓   3/3   XLK (MU!)
BAC   58,69    54,31   51,95  69,67    +5,43 %       ✓  ✓  ✓   3/3   XLF (JPM!)
CSCO 112,69   110,91   89,36  43,44   +30,86 %       ✓  ✗  ✓   2/3   XLK
GE   377,49   332,46  304,49  75,42   +15,33 %       ✓  ✗  ✓   2/3   XLI (RSI überkauft, Watch)
```

**Watchlist für morgen (Fr 03.07.):** MS, CAT, LLY, AMD, AAPL

- **MS**  213,89 $ | XLF — Grund: NEU im Screening, K1-K3 alle ✓, RSI 52,51 mittig, RS +15 % solid; Sektor XLF nur JPM 1,01 % belegt → Diversifikations-Potential
- **CAT** 963,60 $ | XLI — Grund: XLI-Sektor bisher leer, K1-K3 ✓; K5 carry-over ✗ (RevGrowth Q1 -1 %) → K5-Recheck morgen zwingend, evtl. Q2-Update
- **LLY** 1210,79 $ | XLV — Grund: K5 carry-over ✓ (FwdPE 32-33, Rev +26 %), K4 wartet auf Volume-Spike; RSI 67 nahe 70-Limit — Kauf-Fenster eng
- **AMD** 518,25 $ | XLK — Grund: höchste RS +132,84 % Semi-Rally-Rekord; ABER XLK bereits MU 8,85 % → 2. XLK-Position würde Sektor auf ~19 % heben (unter 30 % Limit, aber Konzentrations-Risiko); K5 struktr. ✗ FwdPE 35-95x → K5 Multi-Source-Recheck morgen (wie bei MU 02.07. gemacht)
- **AAPL** 308,24 $ | XLK — Grund: solide RS +6,99 %, moderate RSI 60,74; wie AMD Sektor-Konflikt XLK; K4/K5 Open-Check morgen

**Sektor-Belegung Post-Close 02.07.:** JPM XLF 1,01 % | UNH XLV 10,24 % | MU XLK 8,85 % = 20,10 % investiert. 3/8 Positions-Slots. XLI/XLE/XLU leer.

**Positionen-Check zusammen mit Watchlist:** V1-V6 alle SICHER (JPM/UNH/MU), keine V5/V6-Limit-Order für morgen (MU-V5 EMA-Spread +374 sehr breit, MU-V6 RSI 48 unter 80). MU-V1-Puffer nur +2,38 % → Pre-Market Fr zwingend, weiterer Verlust >-2,4 % triggert Market Sell sofort.

**Fr 03.07. Marktbedingungen:**
- **Verkürzter HT bis 13:00 ET** wegen Independence Day Sa 04.07.
- Volumina typisch dünn (60-70 % vs. voller HT) → K4-Hürde 120 % Avg20 schwerer erreichbar
- Keine 13:00 ET Midday-Routine (Close ist 13:00)
- Käufe KW27 nur noch 1 Slot frei (nach MU-Fill)
- Guardrails-Erwartung: keine Änderung (VIXY 21,47, DD -0,65 %)

**ClickUp:** [CLOSE] Tagesbilanz Task angelegt Prio 3, Push-Notification an Owner gesendet.

---

## Pre-Market 08:35 ET — 2026-07-02 (Do, KW27) — Guardrails GRÜN, Buy-Scan JA, Lead ELV (K5 strukturell blockt)

**Makro-Lage (Pre-Market 08:35 ET, Alpaca IEX + Perplexity):**
```
VIX (Spot):         16,70          [GRÜN — sehr entspannt, <25 → 10 % Sizing erlaubt; Perplexity/Investing.com Live]
SPY Quote 08:35 ET: bid 748,95 / ask 749,15 → Mid 749,05 $ (+0,454 % vs Mi-Close 745,665)
SPY 1m-Bar 08:34:   748,97 $ (n=1 Trade, v=100 — dünn Premarket)
VIXY Close 01.07.:  21,47 $         (+0,77 % vs Di 21,305)
VIXY Bid 20:00 UTC: 20,86            → Spot ~17 konsistent
10Y Treasury Yield: n/v (Perplexity leer — nicht handlungsblockierend)
Crash-Filter:       NEIN (SPY Mi -0,13 % → weit von -5 %)
Markt-Status:       CLOSED (next_open 09:30 ET)
```

**Alpaca Account-Status (Konsistenz-Check):**
```
Equity:             100.019,54 $    (Pre-Market Mark, vs Mi-Close 100.006,91 → +12,63 $ / +0,013 % Settlement-Tick)
Cash:                88.767,74 $    (identisch zu Memory)
Last_Equity:        100.006,91 $    (Mi-EOD-Mark; Memory notierte 100.006,57 → +0,34 $ After-Hours-Tick akzeptabel)
Long Market Value:   11.251,80 $    (JPM 1.011,00 + UNH 10.240,80)
Status:              ACTIVE         (trading_blocked=false, account_blocked=false)
DayTrade Count:      0 / PDT False
Buying Power:       386.576,00 $
Open Orders:         0
Positions Live:      JPM 337,00 $ (P/L +1,27 %, change_today +0,88 %)
                     UNH 426,70 $ (P/L +6,26 %, change_today +0,04 %)
```

**Guardrails-Check (alle 8 Hierarchien):**
```
1. Daily Loss Cap (-3 %/Tag):    +0,013 % (100.019,54 / 100.006,91) [GRÜN]
2. Weekly Loss Cap (-5 %/Woche): -0,005 % (vs KW27 Mo-Basis 100.024,25 = Fr-Close) [GRÜN]
3. Drawdown vom ATH:             -0,047 % (vs ATH 100.066,47) [GRÜN — Alarm bei -15 %]
4. Drawdown-Stopp -20 %:         INAKTIV
5. Crash-Filter (SPY -5 %):      INAKTIV (Mi -0,13 %)
6. VIX-Filter (>30):             INAKTIV (16,70 → sehr klar GRÜN → 10 % Sizing)
7. Earnings-Blackout (3 HT):     KEINER — JPM 15.07. (13d, Perplexity heute) | UNH 16.07. (14d carry-over — Perplexity heute N/A)
8. Max neue Käufe KW27:          0/2 genutzt → 2 frei (Do 02.07. ist ggf. letzter regulärer HT KW27, Fr 03.07. NYSE-Closure für Independence Day Sa 04.07.)
```
→ **STATUS: GRÜN auf allen 8 Levels.**

**Positionen Signal-Recheck (Pre-Market, V1–V6 carry-over Close 01.07. + Live-Adjustment):**
```
JPM    337,00 $ — V1 306,16 SICHER (+10,08 %) | V2 ~302,11 SICHER (+11,55 %) | V5 EMA50 316,48>EMA200 308,96 ✓ | V6 RSI 65,18 / RS_4w +12,80 % → KEIN Trigger
UNH    426,70 $ — V1 369,44 SICHER (+15,50 %) | V2 376,65 (NEU vom 01.07.) SICHER (+13,29 %) | V5 EMA50 391,55>EMA200 347,22 ✓ | V6 RSI 63,46 / RS_4w +14,68 % → KEIN Trigger
```
→ Keine Verkaufsorder pending. EMA50>EMA200 für beide sehr komfortabel. RSI weit unter 80, RS positiv. UNH-V2 auf 376,65 (getrailt nach Posit-Hoch 428,01 vom 01.07.).

**Earnings-Verifikation (Perplexity 02.07.):**
- **JPM Q2 2026: 2026-07-15 AMC (Perplexity heute)** — 13 Tage entfernt → KEIN Blackout
  - **Diskrepanz-Note:** Pre-Market 01.07. hatte "07-14 CONFIRMED via Business-Wire"; heute Perplexity 07-15. Beide >3 HT, nicht handlungskritisch. Verifikation Pre-Market 14.07. zwingend.
- UNH Q2 2026: Perplexity heute N/A → carry-over 2026-07-16 (14 Tage) → KEIN Blackout
- Weitere KW28-Earnings (nicht in Positionen): Citigroup 14.07., Wells Fargo 14.07., Goldman Sachs 14.07., Morgan Stanley 14.07. — Banken-Cluster
- → Standard V1 -8 % bleibt für JPM + UNH, kein Stop-Tightening.

**Top-News / Makro heute (Perplexity 02.07.):**
- Perplexity Datum-in-Zukunft-Bug carry-over: SPY-Premarket-%, Top-3-News, US-Kalender alle **N/A**
- **Keine großen Makro-Releases** dokumentiert (CPI/PCE/NFP/ISM/FOMC nicht auf Kalender via Perplexity)
- VIX-Spot 16,70 via Investing.com/Yahoo-Live-Zitation — Vola-Entspannung setzt sich fort (vs 01.07. 16,3–16,4)
- 10Y Treasury tagesgenauer Tick fehlt (Perplexity leer — nicht handlungsblockierend)

**Watchlist-Status (Carry-over Close 01.07., Alpaca IEX):**
```
Symbol | Close   | K1     | K2 RSI | K3 RS_63d | K4 Vol% | K5                                    | Score
ELV    |  415,95 | ✓      | ✓ 59,2 | ✓ +27,3 % | ✓ 175 % | ✗ RevGrowth Q1 +1,5 % (Perplexity heute) | 4/5 LEAD — K5 strukturell BLOCKS
CAT    |  991,98 | ✓      | ✓ 55,4 | ✓ +25,3 % | ✓ 144 % | ✗ RevGrowth Q1 -1 %                     | 4/5 BLOCKS (K5)
AMD    |  540,89 | ✓      | ✓ 58,1 | ✓ +151,4%| ✓ 128 % | ✗ FwdPE 35–95x                          | 4/5 BLOCKS (K5)
MU     | 1032,64 | ✓      | ✓ 53,8 | ✓ +191,2%| ✗ 108 % | unklar (Perplexity leer)                | 3/5 K4+K5 warten
LLY    | 1192,14 | ✓      | ✓ 66,1 | ✓ +14,9 % | ✗  72 % | ✓ FwdPE 32,4–33 / Rev +26 %             | 4/5 K4 warten
INTC   |  127,08 | ✓      | ✓ 52,7 | ✓ +173,3%| ✗  73 % | ✗ FwdPE >120 (Multi-Src)                | 3/5 BLOCKS strukturell
```

**Perplexity K5-Recheck ELV (02.07.):**
- FwdPE ~10,1 (Q1-2026-Prognose $18,99 EPS bei Preisniveau $192 laut Perplexity — Achtung! Perplexity zitiert offenbar veralteten Preis $192 statt Live 415,95; TTM/FY-EPS-Schätzung ungenau). MarketBeat/Yahoo 30.06. hatten FwdPE 13,9–14,6 → K5 FwdPE-Sub-Kriterium ✓ (klar ≤35)
- **Q1 2026 Umsatzwachstum YoY: +1,5 % operativ / +2,64 % gesamt** — Perplexity heute bestätigt Mi-Wert. K5 RevGrowth-Hürde ≥10 % strukturell nicht erfüllt.
- 2026 EPS-Guidance angehoben auf $26,75 (Anhebung am 22.04.2026, carry-over) — Guidance hilft **nicht** für K5, weil Strategie hart Umsatzwachstum YoY prüft, nicht Guidance-EPS.
- Q2 Earnings-Datum: **Mitte August 2026** (Perplexity heute, vs. Mi-Schätzung "~16.07."). → Bei Kauf morgen kein 3-HT-Blackout aktiv.

**Entscheidung 09:30 ET Market Open:**
- **Buy-Scan JA** — alle 8 Guardrails GRÜN, Pre-Market moderate risk-on (+0,45 %), VIX sehr entspannt (16,70), keine Makro-Release-Störung heute
- **Lead-Kandidat: ELV (4/5 ✓, K5 RevGrowth strukturell blockt)**
  - K5-Override wäre Strategie-Bruch → **KEIN Kauf ELV** (Strategie-Lock)
  - K1 ✓ EMA50 384,33>EMA200 348,01 | K2 ✓ RSI 59,2 | K3 ✓ RS_63d +27,3 % | K4 ✓ Vol 175 % Avg20 | K5 ✗ RevGrowth 1,5 % <10 %
- **Backup-Kandidaten (bei Live-Vol-Push mit K5 ✓):**
  - LLY 1.192,14 (K4 warten — Vortag 72 % Vol; heute Live-Vol-Trigger bei ≥120 % Avg20 aktivierbar; K5 ✓)
  - MU 1.032,64 (K5-Recheck Perplexity Live zwingend, K4 Vol-Trigger 108 % → knapp)
- Fallback: falls kein Kandidat alle K5-Kriterien trifft → 0/2 Slots bleiben frei (Bot bleibt Long JPM+UNH, Cash 88,76 %)
- Sektor-Check ELV: XLV (mit UNH → 2 Positionen XLV, ~22 % Gesamt bei Kauf → OK <30 %-Limit), Earnings Mid-August (>3 HT)
- Max 2 Käufe KW27 — 2 Slots verbleiben

**Reconciliation Memory ↔ Alpaca:**
- portfolio.md Mi-Close 100.006,57 vs Alpaca last_equity 100.006,91 = +0,34 $ After-Hours-Tick (akzeptabel)
- cash 88.767,74 identisch
- Positionen-Anzahl & avg_entry konsistent (JPM 3 Sh @ 332,78 / UNH 24 Sh @ 401,57)

**Datenqualitäts-Hinweis:**
Perplexity Datum-in-Zukunft-Bug bleibt: SPY-Premarket, US-Kalender, News-Top-3, 10Y Treasury alle N/A. VIX 16,70 verifizierbar via Investing.com. Perplexity ELV FwdPE-Preisniveau ($192) veraltet; Live-Preis (415,95) korrekt via Alpaca IEX — für K5-Filter zählt RevGrowth (unabhängig davon nicht erfüllt).

**ClickUp:** ROUTINE Normal-Alert Versuch (Prio 4) → ITEM_246 "Max usage for custom task types reached" (Tier-Limit-Issue carry-over seit 26.06.). Fallback: Push-Notification an Owner + Memory-Log primär.

**Nächste Routine:** 09:30 ET Market Open — Buy-Scan ELV (K5-Blocker akzeptieren), Backup LLY (K4-Live-Vol), Backup MU (K5-Recheck).

---

## Market Close 16:04 ET — 2026-07-01 (Mi, KW27) — Tagesbilanz + Watchlist Do 02.07.

**Tages-Performance (Alpaca + IEX-Bars Close 16:00 ET):**
```
Bull-Depot:   100.006,57 $  (vs last_equity 99.724,85)  Daily P/L +281,72 $  +0,283 %  [GRÜN]
SPY:              745,665 $ (vs Di-Close 746,65)         Daily -0,132 % (IEX 1Day-Bar 01.07.)
Alpha:             +0,414 % [POSITIV — UNH +2,63 % + JPM +2,08 % Doppel-Rally trotz Cash-Heavy]
ATH:            100.066,47 $ Drawdown -0,060 %  [GRÜN]
Weekly P/L:        -0,018 % (KW27 Mo-Basis = Fr-Close 100.024,25)  [GRÜN >-5 %]
VIXY Close:         21,47 $ (+0,77 % vs Di 21,305) → Spot ~17 [GRÜN]
Crash-Filter:    INAKTIV (SPY -0,13 %)
```

**SPY-Quelle:** Alpaca IEX 1Day-Bar 01.07. (Close 745,665 vs Di-Close 746,65 = -0,132 %). Perplexity halluzinierte fälschlich, ELV +7,6 % gäbe es nicht („keine bestätigten News") — Alpaca IEX Close bestätigt tatsächliche Werte (ELV 415,95, +7,59 % IEX). Perplexity Datum-Bug carry-over.

**Markt-News (Perplexity 01.07.):**
- JPMorgan Chase +3,30 % (Perplexity nannte JPM als Top-Financials-Mover) → Financials-Rebound-Tag nach Di-Lag; Bot-JPM +2,08 %/IEX konsistent
- Elevance Health (ELV) EPS-Beat: 12,58 $ vs 10,74 $ Konsens (+1,84 $ Beat); Revenue Q1 2026 49,49 Mrd $ (+1,5 % YoY, ✓ über Erwartung 48,21 Mrd)
- ELV Guidance-Anhebung 2026 EPS ≥26,75 $; Carelon-Wachstumstreiber (Care-Bridge)
- Sektor-Divergenz: XLV allgemein „downturn" — ELV als Relative-Strength-Ausreißer
- DXC Technology +4,54 % / Bath & Body Works +7,45 % (Perplexity, nicht S&P-Top-5-Cap)

**Verkaufssignal-Check JPM + UNH (V1–V6 Close 16:00 ET, Alpaca IEX + Live-berechnete Indikatoren):**
```
Symbol | Close   | V1 Stop | V2 Trail | V5 EMA50/EMA200       | V6 RSI / RS_4w
JPM    | 334,06  | 306,16 ✓ +9,11 %  | 302,11 ✓ +10,51 % | 316,48 > 308,96 ✓  | 65,18 / +12,80 % ✓
UNH    | 426,52  | 369,44 ✓ +15,45 % | 376,65 (NEU) ✓ +13,24 % | 391,55 > 347,22 ✓  | 63,46 / +14,68 % ✓
```
→ **Keine pending Verkaufsorder für Do.** Trail-Stop UNH **hochgesetzt auf 376,65** (neues Posit-Hoch 428,01 heute vs. bisher 427,81).

**Watchlist-Scan Do 02.07. (Alpaca IEX 200d-Window Close 01.07.):**
```
Symbol | Close    | Chg%   | EMA50/EMA200         | K1 | RSI  | K2 | RS_63d | K3 | Vol%  | K4 | K5                        | Score
ELV    |  415,95  | +7,59% | 384,33 > 348,01      | ✓  | 59,2 | ✓  | +27,3% | ✓  | 175%  | ✓  | ✗ FwdPE 13,9-14,6 ✓ / Rev +1,5% | 4/5 LEAD K5-Recheck
CAT    |  991,98  | -6,82% | 920,39 > 730,94      | ✓  | 55,4 | ✓  | +25,3% | ✓  | 144%  | ✓  | ✗ RevGrowth Q1 -1 %       | 4/5 BLOCKS (K5)
AMD    |  540,89  | -6,83% | 463,08 > 307,95      | ✓  | 58,1 | ✓  | +151,4%| ✓  | 128%  | ✓  | ✗ FwdPE 35–95x            | 4/5 BLOCKS (K5)
MU     | 1032,64  |-10,37% | 884,06 > 526,00      | ✓  | 53,8 | ✓  | +191,2%| ✓  | 108%  | ✗  | unklar (Perplexity leer)  | 3/5 + K4+K5-Recheck
LLY    | 1192,14  | -0,60% | 1070,24 > 978,25     | ✓  | 66,1 | ✓  | +14,9% | ✓  |  72%  | ✗  | ✓ FwdPE 32,4-33 / Rev +26%| 4/5 K4 warten
INTC   |  127,08  | -8,94% | 112,08 > 69,57       | ✓  | 52,7 | ✓  | +173,3%| ✓  |  73%  | ✗  | ✗ FwdPE >120 (Multi-Src)  | 3/5 BLOCKS strukturell
PLTR   |  125,75  | +7,81% | 132,66 < 151,00      | ✗  | 50,0 | ✓  | -28,7% | ✗  | 203%  | ✓  | n/a                       | 2/5 BLOCKS
NVDA   |  197,54  | -1,20% | 206,60 > 193,38 knapp| ✓  | 41,0 | ✓  | -1,4%  | ✗  | 126%  | ✓  | n/a                       | 3/5 K3 BLOCKS
GEV    | 1134,39  | -3,40% | 1029,93 > 851,56     | ✓  | 59,5 | ✓  | +15,3% | ✓  |  70%  | ✗  | n/a Perplexity            | 3/5 K4 warten
```

**Perplexity K5 Verifikation 01.07.:**
- **ELV**: FwdPE 14,41 (MarketBeat) / 14,60 (Yahoo) / 13,9 (Finbox) → alle ✓ ≤35 | Q1 2026 Rev YoY +1,5 % → ✗ <10 % Hürde | EPS-Beat 12,58 vs. 10,74 + Guidance-Anhebung → aber K5-Rev-Kriterium hart, kein Override
- **MU**: Perplexity-Quelle leer für Micron. Grobe Marktvermutung FwdPE 15–20 (nicht verifiziert). Morgen Perplexity-Recheck falls K4 anspringt.

**Watchlist Do 02.07.:** ELV (LEAD 4/5, K5 RevGrowth strukturell — Perplexity-Recheck ob Q2-Erwartung >10 %), CAT (K5 blockt), MU (K5 unklar + K4 warten), LLY (K4 warten), GEV (K4 warten).

**Sektor-Check kompakt:** Health Care (XLV: UNH +2,63 %/ELV +7,59 % — Sektor-Rebound-Tag!). Financials (XLF: JPM +2,08 %/„JPM +3,30 %"-Konsens — Rebound nach Di-Lag). Tech (XLK: NVDA -1,2 %/AMD -6,83 %/INTC -8,94 % — schwach; MU -10,37 % Selloff). Industrials (XLI: CAT -6,82 % + GEV -3,40 % — schwach). Bot-Long-Positionen im Sektor-Rebound-Duo XLV+XLF perfekt positioniert.

**Entscheidung Market Close:**
- KEINE Verkaufsorders (V1–V6 ALLE SICHER für JPM + UNH, UNH V2 auf 376,65 hochgetrailt).
- KEINE Pending Buys (Routine kauft erst bei Market Open mit K4-Live-Volumen + K5-Perplexity-Live).
- Bot bleibt Long JPM + UNH, 88,76 % Cash für ELV-Kauf-Setup morgen reserviert (falls K5-Recheck stützt).
- **Nächste Routine:** Do 2026-07-02 08:30 ET Pre-Market Check.

**Lessons:**
1. UNH-Trail-Stop auf 376,65 hochgetrailt (Posit-Hoch 428,01 → -12 % = 376,65) — Trail funktioniert diszipliniert, sichert Gewinn +13,24 % Puffer nach neuem Hoch.
2. Financials-Rebound + Health-Insurer-EPS-Move gleichzeitig = **Bot-Alpha +0,41 % trotz Cash-Heavy** durch beide Longs im richtigen Sektor.
3. ELV EPS-Beat + Guidance-Anhebung stark, aber **K5 RevGrowth-Hürde (10 %)** blockt Insurer-Momentum-Trades. Strukturelle Filter-Grenze — kein Override.
4. Perplexity halluzinierte („ELV +7,6 % nicht bestätigt") — Alpaca IEX bleibt Source of Truth für Kurse.
5. Perplexity Sektor-Rotation-Query bleibt leer (Datum-in-Zukunft-Bug carry-over) — Alpaca IEX-Bars als Sektor-Vergleichs-Primärquelle.
6. ClickUp Tier-Limit ITEM_246 open seit 26.06. → Push-Notification + Memory primärer Notification-Kanal.

---

## Market Open 09:37 ET — 2026-07-01 (Mi, KW27) — KEIN TRADE (LLY K4 FAIL, INTC K5 FAIL)

**Live-Snapshot Market Open (Alpaca 09:37 ET):**
```
Equity:             99.745,58 $   (vs last_equity 99.724,85 → +0,021 % GRÜN)
Cash:               88.767,74 $   (88,99 %)
Long MV:            10.977,84 $   (JPM 978,87 + UNH 9.998,64)
SPY Live:              743,08 $   (-0,48 % vs Di-Close 746,65 → moderate risk-off)
VIXY Live:              21,62 $   (vs Di-Close 21,305 → Spot ~17,3, weiter GRÜN)
DayTrade Count:     0 / PDT False | Buying Power: 385.808,91 $
Open Orders:        0
```

**Positionen Live V1–V6 (Alpaca 09:37 ET):**
- JPM  326,29 $ — V1 306,16 SICHER +6,58 % | V2 ~302,11 SICHER +8,00 % | V5 EMA50 314,15>EMA200 308,78 ✓ | V6 RSI 57,6 / RS_4w +11,86 % → KEIN Trigger
- UNH  416,36 $ — V1 369,44 SICHER +12,71 % | V2 ~376,47 SICHER +10,71 % | V5 EMA50 383,13>EMA200 339,23 ✓ | V6 RSI 60,6 / RS_4w +10,94 % → KEIN Trigger

→ Keine Verkaufsorder pending. Beide Positionen vollständig SICHER auf allen 4 aktiven Verkaufssignalen.

**Kandidaten-Scan K1–K5:**

- **LLY** Live 1.188,95 $ (Open 1.211,52 → -1,87 % intraday, vs Di-Close 1.199,38 → -0,87 %)
  - K1 ✓ EMA50 1073,1 > EMA200 978,5 (carry-over Close 30.06.)
  - K2 ✓ RSI(14) 66,5 (Cooldown-Trend intakt)
  - K3 ✓ RS_63d +17,1 %
  - **K4 ✗ FAIL — LIVE-VOL BLOCKS**
    - IEX-Cumvol nach 9 min (13:30–13:39 UTC): **2.197 Sh**
    - Avg20 Daily IEX Vol: **147.363 Sh** (Fenster 01.–30.06.2026, 21 Sessions)
    - Aktuelle Lauf-Ratio: 2.197 / 147.363 = **1,49 % gelaufen** nach 9/390 min = 2,3 % Zeit → **Volumen unter linearer Extrapolation**
    - Tages-Projektion (390-min-Extrapolation): ~95k Sh = **65 % Avg20** << 120 %-Hürde
    - Kontext: Vortag K4 nur 99 % (Grenze knapp verfehlt); heute noch schwächer + Kursverfall → Momentum-Absence
  - K5 ✓ FwdPE 32,4–33,0 + Rev YoY +26 % (carry-over Perplexity 30.06.)
  - **Verdict: 4/5 — K4 hart BLOCKS. Kein Kauf.**

- **INTC** Live 132,86 $ (Open 135,03 → -1,61 % intraday, vs Di-Close 139,55 → -4,80 % — deutlicher Selloff)
  - K1 ✓ EMA50 109,4 > EMA200 61,0
  - K2 ✓ RSI(14) 63,0
  - K3 ✓ RS_63d +220,7 %
  - K4 ✓ IEX-Cumvol nach 9 min = 165.223 Sh vs Avg20 IEX 4.026.506 Sh = 4,10 % gelaufen → Projektion ~7,2M = **179 % Avg20**
  - **K5 ✗ FAIL — LIVE-PERPLEXITY BLOCKS HART**
    - FwdPE Multi-Source Perplexity 01.07.:
      - Seeking Alpha: **120,24**
      - Yahoo Finance: **158,73**
      - MarketBeat: **221,63**
      - → Konsens FwdPE >>35 (mindestens 120)
    - RevGrowth Q1 2026 YoY: **+7,4 %** (unter 10 %-Hürde)
    - BEIDE K5-Sub-Kriterien (FwdPE ≤35 UND RevGrowth ≥10 %) fallen
  - **Verdict: 3/5 — K5 hart BLOCKS.** INTC strukturell in K5-Sperrliste (Turnaround-Story mit stretched Bewertung wie CRWD/AMD).

- **Andere Watchlist-Kandidaten (carry-over Close 30.06., alle blockiert):**
  - CAT 1.063,33 — K5 ✗ RevGrowth Q1 -1 %
  - AMD 580,52 — K5 ✗ FwdPE 35–95x Konsens
  - CRWD 763,12 — K2 ✗ RSI 70,3 + K5 ✗ FwdPE ~69x
  - ELV 386,98 — K2 ✗ RSI 46,9 + K5 ✗ RevGrowth +7 %

→ **KEIN Kandidat erfüllt alle 5 Kaufsignale. KEIN Trade.**

**Guardrails (alle 8 GRÜN):**
- Daily P/L +0,021 % | Weekly KW27 -0,279 % | DD -0,321 % | VIX-Spot ~17 | Käufe 0/2 | Crash-Filter NEIN | Earnings-Blackout NEIN | Cash 88,99 % > 20 %

**Sektor-Rotation (Perplexity 01.07.):**
- 1-Jahres-Performance (nur diese Quelle abrufbar): XLK +50,13 % / XLE +34,32 % / XLV +4,36 %
- Datenqualität: 5-Tage-Rotation Perplexity nicht verfügbar (Datum-in-Zukunft-Bug carry-over)
- Konsistenz: XLK weiter Top-Sektor 1Y, aber Bot 0 % XLK exponiert wegen K5-Filter (AMD/CRWD/INTC alle strukturell blockiert)

**ClickUp:** ROUTINE Normal-Alert (Prio 3, KEIN Trade) → ITEM_246 Tier-Limit-Issue carry-over seit 26.06. Fallback: Push-Notification + Memory-Log primär.

**Lessons:**
1. K4 Live-Vol-Trigger bei Open-Selloff funktioniert sauber als Blocker — LLY-Kurs-Verfall (-1,87 %) parallel zu Vol-Absence (Projektion 65 %) bestätigt fehlendes Buying-Momentum.
2. INTC K5-Multi-Source-Verifikation (Perplexity 3 Quellen) macht Live-Blockierung eindeutig — Turnaround-Story braucht weiterhin >35 FwdPE-Filter-Respekt.
3. K5 FwdPE-Filter erweist sich als robustester Blocker gegen Retail-getriebene Momentum-Namen (INTC, CRWD, AMD alle >120 FwdPE trotz Kurs-Momentum).
4. Perplexity Sektor-5-Tage-Rotation-Query erneut leer — konsistente Einschränkung, Alpaca IEX-Bars als Primärquelle für Sektor-Vergleich.

**Entscheidung:** KEIN Trade. Beide KW27-Slots (0/2) bleiben ungenutzt bei 2 verbleibenden Handelstagen (Do 02.07., Fr 03.07. verkürzt für Independence Day).

**Nächste Routine:** Mi 2026-07-01 13:00 ET Midday Stop-Check.

---

## Pre-Market 08:35 ET — 2026-07-01 (Mi, KW27) — Guardrails GRÜN, Buy-Scan JA, Lead LLY

**Makro-Lage (Pre-Market 08:35 ET, Alpaca IEX + Perplexity):**
```
VIX (Spot):         16,3–16,4       [GRÜN — sehr entspannt, <25 → 10 % Sizing erlaubt; Perplexity/CBOE]
SPY Last Trade:     745,23 $        (08:34 ET, vs Di-Close 746,65 → -0,19 % flach Premarket)
SPY Quote 08:35:    bid 744,53 / ask 744,73 → Mid 744,63 $ (-0,27 %)
VIXY Close 30.06.:  21,305 $        (-2,16 % vs Mo → Vola weiter niedrig)
10Y Treasury Yield: ~4,3–4,4 %      (Perplexity Fed/TradingEconomics, tagesgenau intraday n/v)
Crash-Filter:       NEIN            (SPY Di +0,78 % → weit von -5 %)
Markt-Status:       CLOSED          (next_open 09:30 ET)
```

**Alpaca Account-Status (Konsistenz-Check):**
```
Equity:             99.717,38 $     (Pre-Market Mark, vs Di-Close 99.722,36 → -4,98 $ / -0,005 % Drift)
Cash:               88.767,74 $     (identisch zu Memory)
Last_Equity:        99.724,85 $     (Di-EOD-Mark)
Long Market Value:  10.949,64 $     (JPM 980,76 + UNH 9.968,88)
Status:             ACTIVE          (trading_blocked=false, account_blocked=false)
DayTrade Count:     0 / PDT False
Buying Power:       385.729,95 $
Open Orders:        0
Positions Live:     JPM 326,92 $ (P/L -1,76 %, change_today -0,125 %)
                    UNH 415,37 $ (P/L +3,44 %, change_today -0,063 %)
```

**Guardrails-Check (alle 8 Hierarchien):**
```
1. Daily Loss Cap (-3 %/Tag):    -0,008 % (99.717,38 / 99.724,85) [GRÜN]
2. Weekly Loss Cap (-5 %/Woche): -0,307 % (vs KW27 Mo-Basis 100.024,25) [GRÜN]
3. Drawdown vom ATH:             -0,349 % (vs ATH 100.066,47) [GRÜN — Alarm bei -15 %]
4. Drawdown-Stopp -20 %:         INAKTIV
5. Crash-Filter (SPY -5 %):      INAKTIV (Di +0,78 %)
6. VIX-Filter (>30):             INAKTIV (16,3 → sogar klar <25 → 10 % Sizing)
7. Earnings-Blackout (3 HT):     KEINER — JPM 14.07. (13d, CONFIRMED Business-Wire) | UNH 16.07. (15d carry-over)
8. Max neue Käufe KW27:          0/2 genutzt → 2 frei
```
→ **STATUS: GRÜN auf allen 8 Levels.**

**Positionen Signal-Recheck (Pre-Market, V1–V6 carry-over Close 30.06. + Live-Adjustment):**
```
JPM    326,92 $ — V1 306,16 SICHER (+6,78 %) | V2 ~302,11 SICHER (+8,21 %) | V5 EMA50 314,15>EMA200 308,78 ✓ | V6 RSI 57,6 / RS_4w +11,86 % → KEIN Trigger
UNH    415,37 $ — V1 369,44 SICHER (+12,42 %) | V2 ~376,47 SICHER (+10,33 %) | V5 EMA50 383,13>EMA200 339,23 ✓ | V6 RSI 60,6 / RS_4w +10,94 % → KEIN Trigger
```
→ Keine Verkaufsorder pending. EMA50>EMA200 für beide intakt. RSI weit unter 80, RS positiv.

**Earnings-Verifikation (Perplexity 01.07.):**
- **JPM Q2 2026: 2026-07-14 (13 Tage) — CONFIRMED via Business-Wire Q2-Call + Wall Street Horizon** → KEIN Blackout
- UNH Q2 2026: 2026-07-16 (15 Tage, carry-over — Perplexity heute keine offizielle Quelle, plausibel) → KEIN Blackout
- KEIN S&P-500-Earnings >50 Mrd Market Cap zwischen 01.–03.07. (Perplexity verifiziert)
- → Standard V1 -8 % bleibt für beide, kein Stop-Tightening.

**Top-News / Makro heute (Perplexity 01.07.):**
- **Keine großen Makro-Releases heute** (CPI/PCE/NFP/ISM/FOMC nicht auf Tages-Kalender)
- Perplexity liefert nur routinemäßige Reden/Daten; keine belastbaren tagesgenauen Top-3-Headlines
- 10Y Treasury ~4,3–4,4 % (stabil, keine dramatischen Bewegungen)
- VIX 16,3 (Vola-Entspannung setzt sich fort)

**Watchlist-Status (Carry-over Close 30.06., Alpaca IEX):**
```
Symbol | Close   | K1     | K2 RSI | K3 RS_63d | K4 Vol% | K5                     | Score
LLY    | 1199,36 | ✓      | ✓ 66,5 | ✓ +17,1 % | ✗ 99 %  | ✓ FwdPE 32–33/Rev +26% | 4/5 LEAD — K4 Vol-Trigger heute entscheidend
INTC   |  139,55 | ✓      | ✓ 63,0 | ✓ +220,7%| ✗ 49 %  | unklar (Perplexity leer)| 3/4 + K5 Recheck Live am Open zwingend
CAT    | 1063,33 | ✓      | ✓ 65,3 | ✓ +41,2 % | ✗ 83 %  | ✗ RevGrowth Q1 -1 %    | 3/5 BLOCKS strukturell
AMD    |  580,52 | ✓      | ✓ 64,8 | ✓ +178,0%| ✓ 121 % | ✗ FwdPE 35–95x Konsens | 4/5 K5 BLOCKS strukturell
CRWD   |  763,12 | ✓      | ✗ 70,3 | ✓ +82,7 % | ✗ 85 %  | ✗ FwdPE ~69x           | 2/5 BLOCKS
ELV    |  386,98 | ✓      | ✗ 46,9 | ✓ +17,8 % | ✗ 69 %  | ✗ RevGrowth +7 %       | 2/5 BLOCKS
```

**Entscheidung 09:30 ET Market Open:**
- **Buy-Scan JA** — Guardrails GRÜN, Pre-Market flach (-0,19 %), VIX sehr entspannt (16,3), keine Makro-Release-Störung heute
- **Lead-Kandidat: LLY (4/5 ✓, K4 Vol-Trigger heute entscheidend)**
  - K1–K3 + K5 alle ✓ (FwdPE 32–33, Rev YoY +26 %)
  - K4 muss Live-Volumen bei Open ≥120 % Avg20 zeigen → K4 Live-Check am Open zwingend
  - Falls K4 kippt: kein Pflicht-Kauf, Slot bleibt frei
  - Limit-Order: max +0,5 % über Vortagesschluss = max 1.205,36 $ Limit
  - Sizing: ~10 % Portfolio = ~9.972 $ → 8 Shares bei ~1.199 $ (~9.594 $)
  - Sektor: LLY = XLV (mit UNH → 2 Positionen XLV, ~20 % Gesamt → OK unter 30 %-Limit)
  - Earnings: LLY 2026-07-31 (30 Tage) → KEIN Blackout
- **Backup: INTC (3/4 + K5 Recheck)** — K5 Perplexity-Recheck am Open zwingend (FwdPE, RevGrowth verifizieren); K4 Vol-Trigger am Open erforderlich
- Fallback: kein Kandidat trifft alle 5 → 0/2 Slots bleiben frei (2 Slots + 3 Handelstage KW27)

**Reconciliation Memory ↔ Alpaca:**
- portfolio.md Di-Close 99.722,36 vs Alpaca last_equity 99.724,85 = +2,49 $ After-Hours-Tick (akzeptabel)
- cash 88.767,74 identisch
- Positionen-Anzahl & avg_entry konsistent (JPM 3 Sh @ 332,78 / UNH 24 Sh @ 401,57)

**Datenqualitäts-Hinweis:**
Perplexity SPY-Premarket-Bewegung nicht quantifizierbar (Datum-in-Zukunft-Bug carry-over). Alpaca IEX SPY-Last-Trade + Quote als Source of Truth (-0,19 % / -0,27 %). VIX 16,3 via CBOE/Perplexity plausibel. 10Y Treasury tagesgenauer Intraday-Tick fehlt aber Range 4,3–4,4 % konsistent.

**Nächste Routine:** 09:30 ET Market Open — Buy-Scan LLY (K4 Live-Vol entscheidend), Backup INTC (K5 Recheck).

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
