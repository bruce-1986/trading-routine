# Research Log

**Bot:** Bull | **Aktualisiert:** täglich

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
