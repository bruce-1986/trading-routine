# Research Log

**Bot:** Bull | **Aktualisiert:** täglich

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
