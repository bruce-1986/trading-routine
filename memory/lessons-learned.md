# Lessons Learned

**Bot:** Bull | **Format:** Wöchentlich updaten nach Weekly Review

---

## Was funktioniert (bestätigte Patterns)

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
