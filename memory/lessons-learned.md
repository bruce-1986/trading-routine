# Lessons Learned

**Bot:** Bull | **Format:** Wöchentlich updaten nach Weekly Review

---

## Was funktioniert (bestätigte Patterns)

*Noch keine Erfahrungswerte — Bot startet 2026-05-31.*

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
