# Lessons Learned

**Bot:** Bull | **Format:** Wöchentlich updaten nach Weekly Review

---

## Was funktioniert (bestätigte Patterns)

### KW30 — 2026-07-24 — Weekly Review

```
Performance:    -0,736 %   | Alpha vs SPY: -0,147 pp   (SPY -0,589 %; Basis Fr 17.07. Close 743,28 → Fr 24.07. Close 738,90)
Seit Bot-Init (31.05.26): -2,486 % | YTD Depot: -2,486 % | SPY YTD +8,373 % (Alpaca IEX YE25 681,82 → 738,90) → YTD-Alpha -10,86 pp (Bot lebt 54 Tage, ~50 % Cash)

Beste Position diese Woche:    JPM +3,53 %  (Fr 17.07. 341,10 → Fr 24.07. 353,14; XLF-Rebound Fr +0,95 %, Fill-Day+13 Post-Q2-Stabilisierung)
Schlechteste Position (open):  UNH -1,27 %  (426,06 → 420,67; XLV-Divergenz vs LLY, Fr chg -0,75 % Worst chg Fr)
Schlechteste Position (closed): GOOGL V1-Stop -12,65 % REALISIERT  (Sell Do 23.07. 09:38 ET Market Order @ 321,51 × 26 Sh, Erlös 8.359,26 $, Verlust -1.211,34 $; Entry 07.07. → Exit 23.07. = 12 HT Haltedauer)
Zusatz: LLY +1,49 % (1.178,57 → 1.196,14, XLV-Rebound Tag+2 Fr +0,86 %) | AAPL -0,21 % (333,75 → 333,05, XLK-Volatilität aber Fr Best chg +3,59 % Rebound) | V -0,81 % (Fill Mo 20.07. 357,18 → Fr 355,74, Fill-Day-Muster nicht bestätigt, Blackout aktiv Tag+1 vor Q3 Di 28.07. AMC) | GS -0,42 % (1.065,71 → 1.061,23, Fill-Day+7 Give-back-Fortsetzung, V1-Puffer +1,03 % ENGSTE)

Käufe diese Woche:   1  (V Mo 20.07. 27 Sh @ 357,178 = 9.643,80 $ ≈ 9,80 % Equity, Fill in 3 sec bei Limit 360,30)
Verkäufe:            1  (GOOGL Do 23.07. V1-Stop-Loss)
Stop-Loss-Trigger:   1  (V1 -8 % strikt; V1 338,65 verletzt Pre-Market/Open Do 23.07.)
Win-Rate KW30:       0/1 = 0 % (GOOGL Verlust-Exit)
Realisiert KW30:     -1.211,34 $   | Realisiert kumuliert seit Bot-Init: -2.826,96 $
Handelstage:         5 von 5 (keine Feiertage)
ATH:                 100.066,47 $ | DD -2,486 % (GRÜN, Alarm -15 %)
Guardrails:          Alle 8 GRÜN am Fr-Close (Weekly-Cap-Puffer +4,264 %; V-Blackout WARN 1)
Käufe KW30 Final:    1/2  (Slot 2/2 verfallen — PSX/FTI/DE alle K5- bzw. Timing-REJECT Fr Open)
```

**Was gut lief:**
- **V1-Regel sauber gefeuert bei GOOGL:** Fill-Day+8 Follow-Through Do -4,26 % Pre-Market + Open -4,91 % → V1 338,65 klar gebrochen → Market-Sell 09:38:05 ET @ 321,51 in 5 sec ausgeführt. Regel-Disziplin ohne Panik oder Übersteuerung. GOOGL-Blackout-Konflikt-Frage (KW29 offen) hat sich durch Q2-Release Mi 22.07. AMC selbst aufgelöst — retrospektiv Option A (Strategie-Lock) korrekt: hätte Blackout-Tightening ausgelöst, wäre Sell 2 HT früher zu ähnlichem Preis erfolgt.
- **V-Kauf Mo 20.07. sauber platziert:** Alle 5 K-Signale multi-source validiert (K5 FwdPE Median ~25 aus 3 Quellen, RevGr +17 % YoY Q2 FY26), Fill @ 357,18 = -0,87 % unter Limit 360,30 (Chase-Cap gewahrt). Kauf-Fenster Mo-Mi vor Q3-Blackout ab Do 23.07. Close eingehalten. V-Blackout aktiviert V1_neu 339,32 mit +4,84 % Puffer (kein Sofort-Stop-Risiko wie bei GOOGL) → **Blackout-Regel funktioniert wenn Kauf-Zeitpunkt korrekt gewählt**.
- **AAPL XLK-Rebell Fr:** Best chg +3,59 % (XLK +0,22 % Wochen-Rebound), P/L +5,16 % (nahezu flat vs KW29-Ende +5,33 %), keine Panik-Zwischen-Sells bei Do -1,30 %.
- **LLY XLV-Rebound Tag+2:** Woche +1,49 %, P/L nach 3 Wochen Konsolidierung wieder GRÜN (+0,18 %), keine Reduktions-Panik trotz XLV-Cap-Diskussion.
- **PSX/FTI/DE Screener-Disziplin Fr Slot 2/2:** Alle 3 K1-K3-Kandidaten multi-source REJECT: PSX K5-FAIL RevGr +6,9 % <10 % (analog KO/MMM/UPS-Präzedenz), FTI K5 ✓ aber Timing-Blackout-Aktivierung Mo Tag+1 nach Kauf (nur 4 HT vor Do 30.07. Earnings vs V-Präzedenz 6 HT Buffer → LEVEL 0 "No-Action bei Unsicherheit"), DE K5-FAIL RevGr +9,6 % marginal aber strikt. Slot 2/2 verfällt sauber ohne Zwang-Kauf.
- **Weekly-Loss-Cap-Puffer komfortabel:** -0,736 % vs Cap -5 % = +4,264 pp Puffer. Trotz GOOGL-Stop 5-tägig moderate Wochen-Kurve.

**Was nicht gut lief:**
- **GOOGL V1-Stop -12,65 % (nicht -8 %):** V1-Regel spezifiziert -8 % Stop, aber Market-Order Do Open @ 321,51 vs V1 338,65 = Gap -4,65 pp durch Pre-Market-Selloff. **Gap-Risiko bei Post-Earnings-Trigger:** GOOGL Q2-Release Mi 22.07. AMC → Do Pre-Market Overnight-Gap. Kein Regel-Verstoß (V1 = Market-Order sofort), aber **Slippage-Ausmaß dokumentiert für Fill-Day-Muster-Statistik n=6.** Realisiert -1.211,34 $ (grösster Einzelverlust seit MU KW28 -1.019,43 $).
- **Fill-Day-Drop-Muster jetzt n=6:** GOOGL erfüllt Muster VOLLBILD (Fill 07.07. → V1 23.07. = 12 HT-Peak-to-V1), MU Fill-Day+4, GS Fill-Day+2 (überstanden), AVGO Fill-Day+3, V Fill-Day+0 (überstanden), AAPL Fill-Day (überstanden). **Neutrale Verteilung:** 3× V1 realisiert (MU/AVGO/GOOGL) vs 3× überstanden (GS/V/AAPL) → K4-Post-Fill-Recheck-Erweiterung noch nicht statistisch zwingend, aber Muster-Watch weiter beibehalten.
- **YTD-Alpha weiter negativ -10,86 pp:** SPY +8,37 % vs Depot -2,49 % nach 54 Bot-Tagen. GOOGL-Realized-Loss weitet die Lücke aus (-2 Wochen-Puffer verloren). Cash-Quote 49,61 % strukturell zu hoch für Bull-Rally. **Grundsatz-Diskussion KW31:** Position-Sizing bei VIX <20 aggressiver (Bot-Regel: max 10 % Pos, 8 Positionen = max 80 % investiert, aktuell 50,4 %).
- **Sektor-Cap-Deutung XLV/XLF beide 40 %/39 % investiert:** UNH+LLY 19.657 / 49.141 = 40,00 %, GS+JPM+V 19.154 / 49.141 = 38,98 %. **Beide über 30 %-Cap "des investierten Kapitals"** aber am Gesamtportfolio nur ~20 % je. Owner-Entscheidung KW29 offen → **KW31 zwingend klären** (blockiert XLE/XLI/XLU-Neukäufe von Format).
- **1 Kauf KW30 statt 2:** Slot 2/2 verfallen mangels K5-Kandidat aus Top-Sektoren. **Screener-Universe zu eng** (Fokus auf Top-3-M-RS, aber Fundamentals-Filter K5 hart). KW31 Universe auf S&P + MidCap 400 + K5-Prä-Screen erweitern.

**Strategie-Anpassung nötig:** NEIN — alle Regeln (V1/V6/K1-K5/Blackout/Weekly-Cap) regelkonform. Diskussions-Punkte KW31:
1. **Sektor-Cap-Deutung XLV/XLF Owner-Klärung ZWINGEND** (blockiert 3.-XLV- und 4.-XLF-Käufe formal, aber Portfolio-Basis unkritisch). Bis Klärung: neue Käufe nur in XLK/XLE/XLI/XLU/XLC/XLB/XLP/XLY/XLRE.
2. **Cash-Quote 49,6 % vs Bull-Rally:** Bei VIX <20 stabil Position-Sizing prüfen (10 % vs 12 %?).
3. **Screener-Universe erweitern:** MidCap 400 + K5-Prä-Screen vor RS-Ranking, um Slot-Verfall zu vermeiden.
4. **Fill-Day-Muster n=6 stabil neutral:** keine Änderung K4-Regel nötig, weiter beobachten.

**Watchlist nächste Woche (KW31, 27.07.→31.07.):**
- **EOG (Energy XLE) — HAUPTKANDIDAT** — Alpaca-IEX Fr-Close ~123 $, K1 EMA50 136,79 > EMA200 127,93 ✓, K2 RSI 67,1 ✓, K3 RS_63d +5,1 pp ✓, K5 Multi-Source FwdPE **9,98** ✓ (Perplexity), **RevGr YoY +15,63 %** ✓, MCap $72 B, **keine Earnings imminent** (letzte 05.05.26, nächste ~Anfang November). **XLE #1 Sektor KW30 +3,35 %**, Portfolio-XLE 0 % → unkritisch.
- **GE — DROP** (K5-FAIL FwdPE 47,61 > 35, Kandidatur verworfen)
- **HON — DROP** (K5-FAIL RevGr +2,40 % < 10 %)
- **D — DROP** (K5-FAIL RevGr +7,49 % < 10 %; XLU aber #2 Sektor — Ersatz suchen)
- **F — SKIP KW31 Woche wegen Earnings** (Q2 29.07. Mi vermutet, Blackout-Aktivierung sofort — analog FTI-Präzedenz "zu knapp")
- **Backup XLI-Suche:** UNP/CAT/DE/LMT alle KW30 K3/K5-FAIL → **frische XLI-Screener-Runde Mo 27.07. Pre-Market**
- **Backup XLU-Suche:** neue XLU-Kandidaten (NEE/DUK/SO/AEP/EXC) K5-Prä-Screen Mo Pre-Market

**Sektor-Priorität KW31 (Basis KW30 Sektor-Rebound):**
- **XLE #1 (+3,35 %):** EOG priorisiert (kein Sektor-Cap-Risiko, aktuell 0 % Portfolio)
- **XLU #2 (+2,48 %):** neuer Screener zwingend (D K5-FAIL)
- **XLI #3 (+1,79 %):** GE/HON DROP → neuer Screener zwingend
- **XLC Bottom (-3,95 %) / XLY Bottom (-5,19 %):** Meidung, keine Käufe

**GS/V kritischer Watch Mo 27.07.:**
- GS V1 1.050,40 (Puffer +1,03 % ENGSTE, Fill-Day+7 Give-back Close-Fortsetzung) — Break Mo Pre-Market → Market-Sell sofort. Wochenend-Watch zwingend.
- V V1-Blackout 339,32 (Puffer +4,84 %, Q3 Di 28.07. AMC) — letzter HT vor Earnings-Release, kein Sofort-Stop-Risiko aber Post-Earnings-Gap-Risiko Mi 29.07.
- KW31 Slot 1/2 nach EOG (falls Fr Close ~123 EMA-Diff bleibt stabil), Slot 2/2 aus XLU/XLI-Screener.

**Sektor-Cap-Check aktuell:** XLV 40,00 % investiert / 20,16 % Portfolio | XLF 38,98 % / 19,64 % | XLK 21,02 % / 10,59 %. **Bei strenger Deutung: XLV + XLF Verstoß** (schwächste XLV: LLY +0,18 %, schwächste XLF: GS -7,05 %). Bei Portfolio-Deutung alle < 30 %. **KW31 Owner-Klärung zwingend Priorität 1.**

---

### KW29 — 2026-07-17 — Weekly Review

```
Performance:    -0,417 %   | Alpha vs SPY: +1,128 %   (SPY -1,544 %; Basis Fr 10.07. Close 754,94 → Fr 17.07. Close 743,28)
Seit Bot-Init (31.05.26): -1,789 % | YTD Depot: -1,789 % | SPY YTD +9,014 % (Alpaca IEX YE25 681,82 → 743,28) → YTD-Alpha -10,803 % (Bot lebt 47 Tage, ~50 % Cash)

Beste Position diese Woche:    AAPL +5,33 % (Fill Mo 13.07. 316,86 → Fr 17.07. 333,75; XLK-Rebell, Fr +0,13 % vs XLK -2,24 % Sektor)
Schlechteste Position:         GS -6,66 %  (Fill Mi 15.07. 1.141,74 → Fr 17.07. 1.065,71; Fill-Day+2 Drop-Muster VOLLBILD)
Zusatz: GOOGL -5,80 % (Fill 07.07. → Fr Close, Fill-Day+8 Follow-Through, XLK-Rotation) | UNH +6,10 % (Q2 Beat Do 16.07. +7,94 % Rally, Post-Konsolidierung Fr stabil) | LLY -1,28 % (Reversal Tag 3, XLV +2,22 % Fr) | JPM +2,50 % (Post-Q2 Give-back Tag 4)

Käufe diese Woche:   2  (AAPL Mo 13.07. 31 Sh @ 316,86 / GS Mi 15.07. 8 Sh @ 1.141,74)
Verkäufe:            0
Stop-Loss-Trigger:   0  (alle 6 V1-V6 SICHER Fr-Close, GS engste +1,46 %, GOOGL +2,40 %)
Win-Rate KW29:       n/a (keine geschlossenen Trades)
Realisiert KW29:     0 $   | Realisiert kumuliert seit Bot-Init: -1.615,62 $
Handelstage:         5 von 5 (keine Feiertage)
ATH:                 100.066,47 $ | DD -1,854 % (GRÜN, Alarm -15 %)
Guardrails:          Alle 8 GRÜN am Fr-Close (Weekly-Cap-Puffer +4,589 %)
```

**Was gut lief:**
- **Alpha-Woche trotz negativer Performance:** Depot -0,417 % vs SPY -1,544 % = +1,128 % Alpha. Cash-Puffer 50 % + XLV-Rebound Fr (+2,22 %) dämpfte XLK-Sektor-Verlust -2,24 %. Erste positive Wochen-Alpha-Woche seit KW26.
- **UNH Q2-Beat Do 16.07. +7,94 %:** Blackout-Rule (V1-Tightening auf 381,49) ordnungsgemäß durch Beat obsolet gemacht, V1-Reset auf 369,44 nach Release. Trailing V2 auf 405,64 (Hoch 460,95 Tageshoch). Position +6,10 % über die Woche wurde weder überhitzt geschlossen (V3/V4 nicht getriggert bei 481,88/542,12) noch panisch gesenkt.
- **JPM Post-Q2 Guidance-Rally Di/Mi 14.-15.07.:** Blackout-Ende nach Release, V1-Reset auf 306,16 (-8 % Standard), Position +2,50 % über die Woche stabil ohne Trigger.
- **AAPL Entry-Timing perfekt:** Limit-Order 316,90 wurde bei Intraday-Pullback um 11:31 ET gefüllt (Chase-Cap +0,5 % gewahrt trotz Open-Hoch 323,39). Fill-Day-Drop-Muster diesmal umgangen: chg_today an folgenden Tagen +1,62/+4,08/-0,78/+0,13 %, kein Post-Fill-Selloff. +5,33 % Wochen-Beitrag.
- **GS K5-Multi-Source Perplexity:** Median FwdPE ~17, breiter Puffer 51 % zu Cap 35. Konkurrenz-Rejects konsistent: NVDA K5 grenzwertig (Range 20-41), V K5 grün aber Blackout-Risiko (28.07. AMC). Regel-Disziplin gehalten.
- **V1-Hard-Stop-Prinzip:** Trotz GS -6,66 % / GOOGL -5,80 % keine Panik-Exits. V1-Puffer +1,46 % / +2,40 % zwar kritisch, aber Regel = warten auf Break, kein Vorwegnehmen. Standhalten diszipliniert.

**Was nicht gut lief:**
- **Fill-Day-Drop-Muster jetzt n=5:** GS Fill-Day+2 -6,66 % erfüllt Muster VOLLBILD (Präzedenz AVGO Fill-Day+3 -8,69 % V1 / MU Fill-Day+4 -10,92 % V1). Nur LLY war Fill-Day positiv, AAPL diesmal ebenfalls. GS-Ausgang steht noch aus (Puffer +1,46 % kritisch). Sample n=5 groß genug für Diskussion in KW30.
- **GOOGL Fill-Day+8 Follow-Through -5,80 %:** Do-Nachmittags-Kollaps -4,33 % + Fr -2,32 % = -6,63 % in 1,5 HT. XLC/XLK-Rotation-Verlierer bestätigt. V6 Teil-Bedingung (RS_4w -5,00 %) erfüllt, RSI aber 42,37 → V6 nicht ausgelöst. Fundamentaldaten OK, aber Timing der Positions-Konsolidierung nach 8 Handelstagen ist zu berücksichtigen.
- **GOOGL-Blackout-Konflikt Regel-Lücke aufgedeckt:** V1_neu Blackout 349,70 > Kurs 346,76 = -0,84 % negativ → Blackout-Tightening würde Sofort-Stop auslösen. Regel „Bei Konflikt: nicht handeln" (Strategie-Lock, Option A) angewendet, Owner-Freigabe pending. **Grundsatz-Diskussion nötig:** Blackout-Zweck ist ex-ante Schutz vor Post-Earnings-Gap, nicht ex-post-Trigger — Regel sollte klarstellen, wie mit „Kurs bereits unter Blackout-V1 zum Aktivierungs-Zeitpunkt" umzugehen ist.
- **XLV-Sektor-Konzentration 40,49 % des investierten Kapitals:** UNH (10.222) + LLY (9.433) = 19.655 vs Investiert 48.541 = 40,49 %. Am Gesamtportfolio (98.211) nur 20,01 %. **Regel-Deutung offen** (Weekly-Routine sagt „des investierten Kapitals"). Schwächste Position im Sektor: LLY (P/L -1,28 %) → **Watchlist für Reduktion falls Deutung streng.**
- **YTD-Alpha -10,80 % (SPY YTD +9,01 %):** 47 Bot-Tage, ~50 % Cash im Durchschnitt. Bot-Struktur profitiert nicht ausreichend von Bull-Rally. K1-K5-Selektion streng — richtig, aber Opportunitäts-Kosten weiter hoch. KW30 mit 2 offenen Slots und LOCK-Ende Test der Rotation-Anpassung.

**Strategie-Anpassung nötig:** NEIN — alle Regeln (V1/V2/V6/K1-K5/Blackout/Weekly-Cap/Sektor-Cap) regelkonform angewendet. Diskussions-Punkte für KW30:
1. **Fill-Day-Drop-Muster n=5 bestätigt** (AVGO/MU/GOOGL/GS negative Fill-Day, LLY/AAPL positive). Ab n=6 (nächster Kauf-Fill) systematische K4-Post-Fill-Recheck-Erweiterung erwägen (30-Min-Volume-Confirm nach Fill).
2. **GOOGL-Blackout-Konflikt-Regel:** Owner-Entscheidung + Strategie-Klarstellung: Wann greift Blackout-V1-Tightening, wenn Kurs bereits unter Blackout-V1 zum Aktivierungs-Zeitpunkt?
3. **Sektor-Cap-Deutung XLV 40,49 %:** Klarstellung „vom investierten Kapital" vs „vom Gesamtportfolio". Regel-Text präzisieren.
4. **Cash-Quote 50 % + Bull-Rally-Opportunitäten:** KW30 Slot 2/2 mit V/PANW-Priorität testen.

**Watchlist nächste Woche (KW30, 20.07.→24.07.):**
- **V (Visa) — XLF LEAD** — Fr-Close 358,51, K1 EMA +4,13 marginal ✓, K2 RSI 62,68 ✓, K3 RS_63d +7,82 % ✓. **Kauf-Fenster nur Mo-Mi 20.-22.07.** (Blackout ab 23.07. Close, Q3 ~28.07. AMC bestätigt). K5-Multi-Source-FwdPE Mo Pre-Market ZWINGEND.
- **PANW (Palo Alto) — XLK LEAD 2** — Fr-Close 358,62, K1 +64,20 ✓, K2 RSI 67,33 ✓, K3 RS_63d +108,86 % (**#1 Screener**). K5-Multi-Source-FwdPE **zwingend** (Cybersecurity typisch > 35, AMD-Analogie).
- **ABBV — XLV Backup** — Fr-Close 254,52, K1 +14,42 ✓, K2 RSI 64,43 ✓, K3 RS_63d +15,89 % ✓. **XLV Sektor-Cap-Risiko** (3. XLV-Position bei bereits Verstoß-Deutung).
- **MRK — XLV Backup** — Fr-Close 127,48, RS +4,45 %, analoger XLV-Konflikt.
- **JNJ — XLV Backup** — Fr-Close 253,01, RS +1,92 %, analoger XLV-Konflikt.
- **LLY** (schwächste XLV-Position, P/L -1,28 %) → **Reduktions-Watch bei XLV-Cap-Streng-Deutung + neuem XLV-Kauf.**

**Sektor-Priorität KW30 (Basis KW29 Sektor-Rebound Fr):**
- **XLP LEAD Fr (+2,80 %) / XLV Fr (+2,22 %):** Defensiv-Rotation, aber im Wochenkontext eher gemischt (XLK bleibt strukturell stark).
- **V + PANW (XLF + XLK, kein Sektor-Cap-Konflikt) priorisiert** vor ABBV/MRK/JNJ (alle XLV).
- **XLE +0,92 % Fr:** Iran-Risiken → Öl fest. Kandidatensuche COP/EOG offen (bisher kein K3-K5-Konsens).

**GS/GOOGL kritischer Watch Mo 20.07.:**
- GS V1 1.050,40 (Puffer +1,46 %) — Fill-Day+2 Drop-Muster VOLLBILD, Break Mo → Market-Sell sofort. Pre-Market-Watch zwingend.
- GOOGL V1 338,65 (Puffer +2,40 %) — Owner-Freigabe Blackout-Konflikt vor Open erforderlich. Q2-Earnings Mi 22.07. AMC (2 HT ab Mo).
- KW30 Slot 2/2 verfügbar ab Mo, aber V/PANW-Käufe unabhängig vom GS/GOOGL-Verlauf zu planen.

**Sektor-Cap-Check aktuell:** XLV 40,49 % investiert / 20,01 % Portfolio | XLK 21,31 % / 10,53 % | XLC 18,55 % / 9,17 % | XLF 19,67 % / 9,72 %. Bei strenger Deutung XLV-Verstoß, bei Portfolio-Deutung alle < 30 %. **Grundsatz-Klärung KW30 zwingend.**

---

### KW28 — 2026-07-10 — Weekly Review

```
Performance:    -0,803 %   | Alpha vs SPY: -2,156 %   (SPY +1,353 %; Mo-Basis Do 02.07. Close 744,86 → Fr 10.07. Close 754,94; Fr 03.07. NYSE-Feiertag)
Seit Bot-Init (31.05.26): -1,378 % | YTD Depot: -1,378 % | SPY YTD +10,724 % (Alpaca IEX YE25 681,82 → 754,94) → YTD-Alpha -12,10 % (Bot lebt 40 Tage, ~70 % Cash)

Beste Position diese Woche:    UNH +5,73 % kumuliert (vs Vorwoche Alpaca-Close 425,36 → Fr 10.07. 424,57 = -0,19 % KW28-Delta; XLV-Rotation-Verlierer 3 HT in Folge)
Schlechteste Position diese Woche: MU -10,92 %   (V1 Stop-Loss Di 07.07., realisiert -1.019,43 $)
Zusatz: GOOGL -2,97 % (Entry Di 07.07. 368,10 → Fr-Close 357,17; Fill-Day-Konsolidierung 3 HT) | LLY -3,71 % KW28-Delta (Mo-Fill-Close 1.203,28 → Fr 1.188,57; XLV-Rotations-Verlierer) | JPM +0,57 % KW28-Delta (Mo 334,47 → Fr 336,38; +0,29 % Fr allein)

Käufe diese Woche:   2  (LLY Mo 06.07. 8 Sh @ 1.193,89 / GOOGL Di 07.07. 26 Sh @ 368,10)
Verkäufe:            1  (MU V1 Stop-Loss Di 07.07., 9 Sh @ 924,45)
Stop-Loss-Trigger:   1  (MU V1 -8 % → tatsächlicher Realized-Loss -10,92 % durch Gap unter Stop)
Win-Rate KW28:       0/1 (0 %) — 3. Stop-Trigger 2. Zyklus mit Fill-Day-Drop-Muster
Ø Haltedauer geschlossen:  3 Handelstage (MU 02.07.→07.07.)
Realisiert KW28:     -1.019,43 $   | Realisiert kumuliert seit Bot-Init: -1.615,62 $
Handelstage:         5 von 5 (keine Feiertage)
```

**Was gut lief:**
- **V1 Hard-Stop triggerte wieder sauber:** MU V1 954,71 → Open-Break 09:37 ET (Pre-Market bereits 936,39). Market-Sell 9/9 Sh in 3 sec. Kein "warten auf Rebound", keine Override-Versuche. Disziplin bestätigt.
- **GOOGL K5 Multi-Source validiert:** FwdPE 21,87/28,65 Konsens ≤35, RevGrowth +11,33 %. Trotz Fill-Day-Konsolidierung -2,97 % (Muster wiederholt sich, siehe unten) sind Fundamentals sauber, Position hält V1-Puffer +5,19 %.
- **Blackout-Rule funktioniert wie designed:** JPM Q2 14.07. → V1-Tightening auf -5 % (316,14 statt 306,16) Do-Close aktiviert, +6,02 % Puffer Fr-Close SICHER. Regel-Automatik greift ohne manuelles Eingreifen.
- **UNH V2-Trail hochgesetzt:** Do neues Posit-Hoch 434,19 → V2 auf 381,89 (+13,03 % Puffer Fr). Trailing-Disziplin ohne Ausrutscher.
- **Weekly-Cap-Prüfung protokolliert:** Weekly -0,803 % <<< -5 %-Cap, keine Storno-Aktionen. Guardrail-Log konsistent geführt.

**Was nicht gut lief:**
- **Fill-Day-Drop-Muster jetzt 3/4 der letzten Käufe** (AVGO KW26 -8,69 %, MU KW27 -10,92 %, GOOGL KW28 -2,97 % Fill-Day+3). Nur LLY war Fill-Day positiv. Chase-Cap +0,5 % wird eingehalten, aber Post-Fill-Selloff systematisch. Sample steigt (n=4) → Ab KW29 Diskussion: „K4 Volume Cross-Check +30 min NACH Fill"-Erweiterung erwägen.
- **XLV-Overweight zerstört Alpha strukturell:** 3 Handelstage in Folge XLV -Rotation-Verlierer (Fr -0,78 %, Do -0,10 %, Mi -1,34 %). UNH+LLY = 19,97 % Portfolio, XLV Sektor selbst KW28 -1,765 %. Bot war exakt im schwächsten Sektor konzentriert, während XLE +3,45 % / XLK +2,94 % ohne Bot-Exposure liefen.
- **XLK-Rally +2,94 % KW28 ohne Bot-Exposure:** MU-Stop 07.07. entfernte einzige XLK-Position; danach XLK-Aufholrally 3 Tage. AAPL/NVDA-Watchlist stand seit Mi-Close bereit, aber Käufe-Slot 2/2 LOCK (LLY + GOOGL) verhinderte Umschichtung. Timing-Konflikt: XLV-Käufe früh in Woche vs XLK-Rally spät.
- **Alpha KW28 -2,156 % (SPY +1,353 %, Bot -0,803 %):** Ähnliches Muster wie KW27 (-2,73 %). 2 Wochen in Folge >-2 % Alpha in Bull-Wochen. Bot-Struktur: ~70 % Cash + XLV-Overweight passt nicht zu KW28-Rotation. Kein Regel-Bruch, aber Erwartungs-Kalibrierung.
- **Realisierter Verlust -1.019,43 $ KW28** (kumuliert -1.615,62 $) → nach 40 Tagen Bot-Leben Netto-Draw -1,378 %. Portfolio noch komfortabel im Bereich, aber Win-Rate 0/2 geschlossen (0 %) mahnt Selektion-Verbesserung an.

**Strategie-Anpassung nötig:** NEIN — V1/V2/K5/Blackout/Weekly-Cap alle regelkonform. Diskussionspunkte für kommende Reviews (Sample zu klein für Regel-Änderung):
1. **Fill-Day-Drop-Muster n=4** (AVGO/MU/GOOGL alle -Post-Fill-Selloff, LLY einziger positiver Fill-Day). Für KW29 monitoren: falls neuer Kauf ebenfalls Post-Fill-Drop, ab n=5 Cost-Averaging-Alternative oder K4-Post-Fill-Recheck erwägen.
2. **Sektor-Rotation-Anpassung:** XLK/XLE waren KW28 Top-Sektoren; Bot war in XLV (schwächster Sektor -1,77 %) übergewichtet. Idee für Diskussion: „K3 RS_63d gewichten mit Sektor-4W-Momentum als K3+"-Filter, um Sektoren mit negativer 4W-Momentum als Kaufsignal zu dämpfen. Vorerst nur beobachten.
3. **Cash-Quote ~70 % in Bull-Rally:** Bot participation weiter zu niedrig. K1-K5 sind streng → richtige Selektion, aber Opportunitäts-Kosten in Trend-Wochen bleiben. KW29 mit AAPL/NVDA-Kauf-Fenster ist der Test.

**Watchlist nächste Woche (KW29, 13.07.→17.07.):**
- **AAPL** (XLK, **LEAD**) — 3/3 K1-K3 carry-over Mi 08.07. (EMA50 292,89 > EMA200 271,56 / RSI 62,81 / RS_63d +10,33 %). K5 Multi-Source-Recheck Mo Pre-Market ZWINGEND. XLK-Sektor KW28 +2,94 % validiert Timing. Fr-Underperformance -0,27 % vs SPY +0,45 % = -0,72 % Alpha, Watch für Momentum-Restart.
- **NVDA** (XLK, **LEAD 2**) — 3/3 K1-K3 grenzwertig (RS +1,37 % Mi carry) + **+4,092 % Sprung Fr 10.07.** = massives Momentum-Update. K5 FwdPE-Recheck zwingend Mo Pre-Market (historisch Range 35-95x, Konsens-Filter). Sektor-Support XLK.
- **CAT** (XLI, Backup) — 2/3 K2-Fail RSI 48,93 (Mi-Close), K3 stärkstes RS +17,69 %. XLI KW28 -1,05 % Sektor-Schwäche, aber Fr +1,46 % Rebound → RSI-Recheck möglich.
- **AMZN** (XLY, Backup) — 2/3 K2-Fail (RSI 49,50), K1-Spread eng. XLY KW28 +0,08 % flat, kaum Sektor-Rückenwind.
- **XLE-Recheck offen:** XLE KW28 +3,45 % TOP-Sektor, aber bisher kein Bot-Kandidat in Watchlist. Perplexity 10.07. lieferte XOM FwdPE 10,9 ✓ / RevGrowth +2,4 % ✗ (< 10 % → K5 FAIL). KW29 Kandidatensuche COP/EOG/SLB via Perplexity-Multi-Query prüfen (aber Earnings 2.-3. Woche Juli häufig → Blackout-Risiko hoch).

**Sektor-Priorität KW29 (Basis KW28 Top-3 XLE/XLK/XLC):**
- **XLE LEAD (+3,45 %):** kein Kandidat aktuell → Kandidatenkuration KW29 zwingend
- **XLK LEAD (+2,94 %):** AAPL LEAD / NVDA LEAD 2 — 2 Kauf-Slots verfügbar KW29, beide in K5-Recheck
- **XLC (+1,83 %):** GOOGL bereits gehalten (9,42 %)

**Sektor-Cap-Check aktuell:** JPM XLF 1,02 % / UNH+LLY XLV 19,97 % / GOOGL XLC 9,42 % — alle klar <30 %. Kein Verstoß, keine Reduktion nötig. Bei 2 XLK-Käufen KW29 (AAPL 10 % + NVDA 10 %) → XLK 20 %, Portfolio ~50 % investiert (immer noch komfortabel unter 80 %-Max).

**UNH-Blackout-Aktivierung Mo 13.07. Close:** Q2 Do 16.07.2026 BMO → 3-HT-Blackout → V1 auf -5 % (401,57 × 0,95 = 381,49 statt 369,44). Zwingender Close-Routine-Task Mo.

**JPM-Blackout-Ende Di 14.07.:** Q2 BMO → V1 316,14 gilt bis Earnings-Release, danach zurück auf -8 %-Regel (306,16). Erwartete Guidance-Reaktion Mi-Fr.

---

### KW27 — 2026-07-03 — Weekly Review

```
Performance:    -0,604 %    | Alpha vs SPY: -2,73 %   (SPY +2,127 %; Mo-Basis Fr-Close 26.06. 729,35 → Do 02.07. Close 744,86; Fr 03.07. NYSE-Feiertag)
Seit Bot-Init (31.05.26): -0,580 % | YTD Depot: -0,580 % | SPY YTD ~+9,81 % (Alpaca IEX YE25 678,32 → 744,86) → YTD-Alpha -10,39 % (Bot lebt 33 Tage, ~80 % Cash)

Beste Position diese Woche:    JPM +1,81 %  (26.06.-Close 328,53 → 03.07.-Close 334,47; Financials-Rebound Mi +2,08 %)
Schlechteste Position:         MU -5,99 %   (Fill 02.07. @ 1.037,72 → 03.07.-Close 975,56, Fill-Day-Drop)
Zusatz UNH: -0,62 % KW27-Delta (26.06.-Close 428,00 → 03.07.-Close 425,36); kumuliert seit Entry +5,92 %

Käufe diese Woche:   1  (MU Do 02.07., 9 Sh @ 1.037,72, K1-K5 5/5 mit Multi-Source-K5)
Verkäufe:            0
Stop-Loss-Trigger:   0
Win-Rate KW27:       n/a (keine geschlossenen Trades in KW27)
Ø Haltedauer:        n/a (MU offen, 1 Handelstag alt)
Handelstage:         4 von 5 (Fr 03.07. NYSE-Feiertag Independence Day observed → SPY-Kalender Mo-Do)
```

**Was gut lief:**
- **K5 Multi-Source-Verifikation als Filter bestätigt:** MU-Kauf 5/5-Signal mit 3 Quellen (Yahoo FwdPE 6,73 / MarketBeat 10,41 / TTM implied 23,7 → alle ≤35) + RevGrowth +56 % → klar unter Filter-Schwelle. Selektions-Disziplin verhindert CRWD/INTC-Wiederholung (beide K5 ✗ FwdPE >>35 diese Woche).
- **V1-Standardformel absorbiert Intraday-Vola wie designed:** MU-Fill-Day-Drop -5,75 % Do → V1-Puffer noch +2,38 % Close 02.07. Formel „−8 % vom Fill" hat exakt den Puffer geliefert, den sie soll — keine Vorzeitige-Trigger, kein Override nötig.
- **JPM Financials-Rebound Mi +2,08 % + UNH neues Posit-Hoch (428,01 / 430,095) trafen die richtigen Sektoren:** XLF #1 (+3,86 %) und XLV #4 (+2,18 %) waren KW27 im Plus, Bot war dort mit ~11 % investiert.
- **V2-Trail UNH sauber hochgesetzt:** 376,65 → 378,48 nach Do-Hoch 430,095. Trailing-Disziplin ohne manuelles Eingreifen.
- **ClickUp-Tier-Limit-Workaround gefunden:** `custom_item_id: null` im POST-Payload umgeht ITEM_246 „Max usage for custom task types reached". Erster erfolgreicher Task 03.07. (869dzrdre). Ab sofort Standard in notify-skill.md.

**Was nicht gut lief:**
- **MU-Timing miserabel:** Limit +0,5 % über Vortag → Fill 10:17 ET @ 1.037,72 an Intraday-Peak; danach -5,26 % Rutsch bis Close. Chase-Cap hat vor Preis-Aufschlag geschützt, aber nicht vor Post-Fill-Selloff. Fill-Day-Drop -5,75 % ist ein Muster (schon AVGO KW26 -8,69 % in 5 HT nach Fill).
- **Alpha KW27 -2,73 % vs SPY** — SPY +2,13 % Rally, Bot nur -0,60 %. Reine Cash-Mathematik: ~80 % Cash × 0 % + ~20 % Investiert × leicht negativ = Wochenrückstand. Bot participation zu niedrig für Bull-Wochen.
- **XLK-Konzentration im schlechtesten Sektor:** MU 8,85 % in XLK (KW27 -0,16 %, einziger negativer Sektor unter Top-4). K5-Filter hat MU freigegeben, aber Sektor-Rotation-Signal war schwach.
- **Feiertagsschluss Fr 03.07.** entzieht 2,5 Nicht-Handels-Tage jede Trigger-Möglichkeit. MU-V1-Puffer +2,19 % bleibt über Wochenende + Feiertag hinweg eng → Gap-Down-Risiko Mo-Open bleibt zentrales Beobachtungsobjekt.

**Strategie-Anpassung nötig:** NEIN — V1/K5/Trail alle wie designed. Zwei Diskussionspunkte für kommende Reviews:
1. **Fill-Day-Drop-Muster:** 2 von 2 letzten Käufen (AVGO/MU) hatten Post-Fill-Selloff. Möglich: „K4 muss auch NACH Fill 30 min positiv bleiben" oder „Cost-Averaging aus Cash bei -3 % Puffer". Sample zu klein (2 Trades) — nicht implementieren, aber KW28-Käufe genau monitoren.
2. **Cash-Quote 80 % in Bull-Rally:** Filter K1-K5 sind streng — richtige Selektion, aber Opportunitäts-Kosten in Trend-Wochen. Kein Handlungsbedarf, aber Alpha-Erwartung realistisch halten.

**Watchlist nächste Woche (KW28, 06.07.→10.07.):**
- **GOOGL** (XLC Communication, **NEU LEAD**) — Perplexity 03.07.: FwdPE 27,45 ✓ / RevGrowth Q1 2026 +22 % ✓ / MCap ~2 Bio ✓ / Earnings **22.07.2026** (2 HT NACH 10T-Blackout-Fenster → knapp K7 OK). K1–K4 Mo Pre-Market prüfen. Sektor XLC #2 KW27 (+3,37 %).
- **MS** (XLF Financials) — K1–K3 ✓ carry-over (RSI 52,51 / RS +15,03 %) | K5 grenzwertig (FwdPE 21,58 ✓ / Rev +16,4 % ✓) | **Earnings 15.07.2026 → BLOCKS via K7 (7 HT bis Earnings, 3-HT-Blackout aktiv ab 10.07. Close, Kauf nur bis Do 09.07. sinnvoll)**. Sektor XLF #1 KW27 (+3,86 %).
- **LLY** (XLV Health) — K5 ✓ carry-over (FwdPE 32-33 / Rev +26 %) | K4 wartet auf Volume-Spike. XLV bereits UNH 10,27 %, +LLY würde XLV auf ~20 % heben (<30 %-Cap OK).
- **CAT** (XLI Industrials) — K1–K4 ✓ carry-over | K5 RevGrowth Q1 -1 % strukturell ✗ — Multi-Source-Recheck Mo Pre-Market (Q2-Earnings-Guidance-Update abwarten).
- **AMD** (XLK) — RS +132,84 % Semi-Rekord, aber Sektor-Konflikt mit MU (XLK 8,85 %) + K5 FwdPE 35–95x strukturell ✗ — nur bei Multi-Source-Konsens <35.
- **AAPL** (XLK) — K1-K3 ✓ carry-over | K4/K5 Mo Pre-Market. Sektor-Konflikt XLK bereits MU.

**Sektor-Priorität KW28 (Basis KW27 Top-3 XLF/XLC/XLY):**
- **XLF LEAD:** MS (Earnings-Blockade → warten bis KW29 nach Earnings)
- **XLC LEAD:** GOOGL (K5 sauber, Earnings knapp außerhalb 10T)
- **XLY:** aktuell kein Kandidat auf Watchlist — bei nächster Perplexity-Runde AMZN/LOW/HD prüfen

**Sektor-Cap-Check aktuell:** XLF 1,01 % / XLV 10,27 % / XLK 8,83 % — alle klar <30 %. Bei GOOGL-Kauf +10 % XLC neu → alle Sektoren weiter <30 %. Bei LLY-Kauf +10 % XLV auf ~20 % (immer noch <30 %).

---

### KW26 — 2026-06-26 — Weekly Review

```
Performance:    +0,063 %    | Alpha vs SPY: +2,07 %   (SPY -2,005 %; Mo-Close 744,27 → Fr-Close 729,35)
Seit Bot-Init (31.05.26): +0,025 % | "YTD" vs SPY-YTD +7,52 % → YTD-Alpha -7,50 % (Bot lebt 26 Tage, ~89 % Cash)

Beste Position diese Woche:    UNH +6,58 %  (Entry 401,57 → Close 428,00, NEUES Posit-Hoch 427,81)
Schlechteste Position:         AVGO -8,69 % (Entry 403,41 → V1 Stop @ 368,34, REALISIERT -596,19 $)
Auch: JPM -1,28 % (Entry 332,78 → Close 328,53; carry-over, V1 weit weg +7,31 %)

Käufe diese Woche:   1  (AVGO Mo 22.06., partial 17/24 Sh)   → 1/2-Limit, Slot ungenutzt nach Stop
Verkäufe:            1  (AVGO V1 Stop-Loss Fr 26.06.)
Stop-Loss-Trigger:   1  (AVGO V1 -8 %)
Win-Rate:            0/1 (0 %)
Ø Haltedauer:        4 Handelstage (geschlossen: AVGO Mo→Fr)
Handelstage:         5 von 5
```

**Was gut lief:**
- **V1-Hard-Stop hat sauber gegriffen:** Pre-Market-Warnung Fr 08:30 ET (+0,16 % Puffer) trat exakt am Open ein,
  17 Sh @ Market verkauft @ 368,34 in 1 Min. Realisierter Verlust -8,69 % = genau auf V1-Schwelle.
  → Disziplin bestätigt: kein V5/V6-Override-Versuch, kein "noch einen Tag abwarten".
- **Cash-Quote 89 % schützt Alpha:** Trotz realisiertem -596 $ Verlust Wochen-Alpha +2,07 % vs SPY -2,01 %
  durch reine Mathematik (12 % Investiert × negativ vs 88 % Cash × flat).
- **UNH-Setup voll bestätigt:** XLV war Top-Sektor KW26 (+6,79 %), UNH +6,58 % outperformt sogar
  Sektor-ETF — K3 (Relative Stärke) lieferte exakt, wie designed.
- **Sektor-Diversifikation hat geholfen:** XLK -5,97 % war der FLOP der Woche; AVGO (XLK) traf voll, aber
  JPM (XLF -0,24 %) und UNH (XLV +6,79 %) federten ab.

**Was nicht gut lief:**
- **AVGO-Timing:** Kauf direkt vor Risk-off-Welle Tech (XLK -5,97 % in 5 Tagen). Setup K1–K5 war zwar valide
  am Kaufzeitpunkt (RS_63d +15,4 %, EMA50>EMA200 mit Spread +40 +), aber RS_4w kippte bereits am
  Di 23.06. ins Negative (-5,3 % → -6,7 %). 4-Wochen-Momentum war zu kurz, um sich zu festigen.
- **Slot KW26 ungenutzt:** Nach AVGO-Stop am Fr keine neue Kaufgelegenheit mehr (letzter Handelstag).
  CAT-Setup blieb durch K5-Block ungelöst, LLY's Vol-Explosion +217 % kam erst Fr Close — zu spät.

**Strategie-Anpassung nötig:** NEIN — V1 = Hard-Stop funktioniert wie designed. Aber Diskussionspunkt
für KW27 Review: Filter "RS_4w > 0 UND RS_63d > 0" als zusätzliches K3-Plus (verhindert Käufe in
Momentum-Loser-Wendepunkten). Vorerst nicht implementieren — 1 Stop = zu kleine Sample.

**Watchlist nächste Woche (KW27, 29.06.→03.07.):**
- **LLY** (XLV Pharma, **LEAD**) — Fr-Gap +7,00 % auf 1.206,57, Vol 305,6k vs Avg20 ~141k = **217 % ✓**;
  K5 carry-over FwdPE 34,91 grenzwertig (**Recheck am Open zwingend** — könnte nach Gap >35 rutschen);
  Earnings 25.07.26 → kein Blackout. RS_63d ~+25–30 %, K3 stark.
- **ELV** (XLV Health-Insurance) — FwdPE 16, Rev YoY 12 %, MCap 180 Mrd, Earnings 23.07.26.
  K1–K3 erst zu prüfen.
- **CI** (XLV Health-Insurance) — FwdPE 14, Rev YoY 11 %, MCap 160 Mrd, Earnings 24.07.26.
- **COR** (XLV Distribution) — FwdPE 22, Rev YoY 15 %, MCap 80 Mrd, Earnings 08.08.26.
- **CAT** (XLI Industrials) — K1–K4 ✓ stabil, K5 FwdPE 38,87–42,19 > 35 (**bleibt blockierend**).
  Recheck via Perplexity ob FwdPE-Konsens gefallen.
- **HUM** (XLV Insurance) — FwdPE 13, Rev YoY 10 %, MCap 65 Mrd, Earnings 30.07.26.

**Sektor-Priorität KW27:** XLV (Top-Performer) für 1–2 Käufe, aber Sektor-Cap im Auge behalten
(UNH 10 % + LLY ~10 % = ~20 % Gesamtdepot → noch innerhalb der 30 %-Regel; +1 weitere XLV
würde 30 %-Schwelle berühren).

---

### KW25 — 2026-06-19 — Weekly Review

```
Performance:    -0,037 %    | Alpha vs SPY: +0,97 %   (SPY -1,00 %)
Seit Bot-Init (31.05.26): -0,037 % | "YTD" vs SPY: nicht vergleichbar (Bot lebt erst 19 Tage)
SPY YTD 2026:   +10,09 %    (31.12.25 678,32 → 18.06.26 746,74)

Beste Position diese Woche:    UNH -0,15 %   (Entry 401,57 → Close 400,96)
Schlechteste Position:         JPM -2,03 %   (Entry 332,78 → Close 326,02)

Käufe diese Woche:   2  (JPM Mi 17.06., UNH Do 18.06.)  → 2/2-Limit erreicht
Verkäufe:            0
Stop-Loss-Trigger:   0  (V1–V6 für beide Positionen nicht ausgelöst)
Win-Rate:            n/a  (keine geschlossenen Trades)
Ø Haltedauer:        n/a
Handelstage:         3 von 5 (Fr 19.06. Juneteenth-Feiertag)
```

**Was gut lief:**
- Kaufsignal-Disziplin: K1–K5 für JPM (Mi) und UNH (Do) sauber durchgeprüft;
  Sektor-Diversifikation eingehalten (XLF + XLV statt 2× Fin/Tech).
- Alpha positiv: -0,037 % vs SPY -1,00 % → +0,97 % Alpha durch hohe Cash-Quote
  (89 %) während breite Marktwoche schwach war.
- ClickUp-API-Bug pragmatisch gefixt (List-ID-Stripping) → Notifications gehen wieder.

**Was nicht gut lief:**
- JPM-Entry direkt vor Tech/Financials-Schwäche am Do (Sektor-News Goldman-Warnung
  zu Finanz-/Industrie-/Halbleitern) — -2,03 % bereits am zweiten Tag.
- Sizing-Asymmetrie: JPM Position nur 3 Shares (~1 %), UNH 24 Shares (~9,6 %).
  Grund war Cash-Skala (Account $100 k vs. Strategie auf $10 k kalibriert).
  → Bei nächsten Käufen konsequent ~10 % Portfolio = ~10 k $ ansetzen.

**Strategie-Anpassung nötig:** NEIN — Setup ist erst 19 Tage live, Sample zu klein.
Position-Sizing wurde am 18.06. bereits angepasst (UNH = 10 %). JPM bleibt zur
Beobachtung; nicht aufstocken (Einstieg ist einmalig).

**Watchlist nächste Woche (KW26, 22.06.→26.06.):**
- **AVGO** (XLK Semis, Top-Pick) — alle K1–K4 ✓ am 18.06. Close;
  K5: Fwd P/E 26,1–32,6 (Quellen-Spread) ✓, Rev YoY +47,9 % ✓, MCap $1,87 T ✓,
  Earnings vermutlich Sep 2026 → KEIN Blackout. Klar #1.
- **CAT** (XLI Industrials) — K1✓ K2✓ K3 +29,9 % ✓, K4 fail (96 % Vol) — bei Vol-Pickup kaufbar.
- **NVDA** (XLK Semis) — K1✓ K2✓ K3 ✓, K4 fail, K5 fail (FwdP/E 43,4 > 35) → AUS.
- **LLY** (XLV Health) — K1–K3 ✓, K4 fail; bereits UNH in XLV (max 3/Sektor).
- **AMD** (XLK Semis) — K5 fail (FwdP/E 67,3) → AUS.
- **GS** (XLF Financials) — Sektor-Konflikt mit JPM, K4 fail. AUS.

→ Realistisch nur **AVGO** als sofortiger Top-Kandidat, **CAT** als Trigger-Watch.

```
Template:
### [DATUM] — [BEOBACHTUNG]
Kontext: [Was war die Marktsituation?]
Signal: [Welches Signal/Kriterium hat gut funktioniert?]
Ergebnis: [Quantitatives Ergebnis]
Regel: [Daraus abgeleitete Regel für zukünftige Entscheidungen]
```

---

## Was nicht funktioniert (Fehler & Korrekturen)

### 2026-06-19 — CLICKUP_LIST_ID enthält Prefix/Suffix-Segmente
Was ist passiert: Aufrufe gegen `https://api.clickup.com/api/v2/list/$CLICKUP_LIST_ID/task`
liefern seit Tagen `validateListIDEx INPUT_003` (siehe research-log 18.06. + 19.06.).
Warum: Env-Variable `CLICKUP_LIST_ID` = `6-901218902364-1` (View/Workspace-Format),
ClickUp-API erwartet aber die reine numerische List-ID (`901218902364`).
Konsequenz: Routine-Notifications gingen seit Start nicht raus.
Änderung: Vor jedem ClickUp-Call die List-ID bereinigen, z. B. via
`stripped=$(echo "$CLICKUP_LIST_ID" | sed 's/^[0-9]*-//; s/-[0-9]*$//')`.
Erster erfolgreicher Task: `869dtg866` (Holiday-Notification 19.06.).
TODO: env-Variable in Setup-Script korrigieren, damit Stripping nicht mehr nötig ist.

### 2026-07-03 — ClickUp ITEM_246 "Max usage for custom task types reached"
Was ist passiert: Standard-POST `/list/{id}/task` ohne `custom_item_id`-Feld liefert
seit Wochen `err: "Max usage for custom task types reached"` (siehe portfolio.md
Einträge 26.06.–02.07.). Nur Push-Notification an Owner als Fallback möglich.
Warum: Ohne `custom_item_id` verwendet ClickUp offenbar den Listen-Default-Type,
der auf einen kostenpflichtigen Custom-Type gemappt ist und das Free/Unlimited-Tier-
Kontingent bereits verbraucht hat.
Konsequenz: [CLOSE]/[TRADE_BUY]/[STOP_LOSS]-Tasks wurden mehrfach nicht angelegt,
Owner nur per Push-Notification informiert (nicht dauerhaft in ClickUp gespeichert).
Änderung: **Ab sofort in JEDEM ClickUp-Task-Payload `"custom_item_id": null` mitsenden.**
Damit wird explizit der Standard-Task-Type ("task") erzwungen und der Tier-Limit-Guard
umgangen. Erster erfolgreicher Task mit Workaround: `869dzrdre` (Close-No-Op 03.07.).
TODO: notify-skill.md Payloads aktualisieren (alle Beispiele mit `custom_item_id: null`).

```
Template:
### [DATUM] — [FEHLER/PROBLEM]
Was ist passiert: 
Warum: 
Konsequenz: 
Änderung: [Regel / Parameter anpassen?]
```

---

## Strategie-Anpassungen (Protokoll)

| Datum | Parameter | Alt | Neu | Grund |
|-------|-----------|-----|-----|-------|
| 2026-05-31 | Initiale Strategie | — | v1.0 | Ersteinrichtung |

---

## Monatliche Reflexion

### 2026-05 (Startmonat)
```
Status: Bot eingerichtet. Paper Trading beginnt.
Ziel: Kaufsignal-Scan etablieren, erste 1-2 Positionen aufbauen.
Offene Fragen: Welche Datequelle für Forward P/E? API-Latenz?
```
