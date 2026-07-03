# Lessons Learned

**Bot:** Bull | **Format:** Wöchentlich updaten nach Weekly Review

---

## Was funktioniert (bestätigte Patterns)

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
