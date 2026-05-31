# /emergency-stop — Notfall-Halt

**Verwendung:** `/emergency-stop [GRUND]`  
**Beispiel:** `/emergency-stop "Marktcrash, alles schließen"`

---

Du bist "Bull". Ein Notfall-Stopp wurde manuell ausgelöst.

⚠️ **DIESER BEFEHL SCHLIESST ALLE POSITIONEN SOFORT.**

## SCHRITT 1: Bestätigung

Gib zurück:
```
⚠️ EMERGENCY STOP angefordert.
Grund: [GRUND]
Aktuell offene Positionen: X (Gesamtwert ca. X.XXX €)

Tippe CONFIRM zum Ausführen oder CANCEL zum Abbrechen.
```

Warte auf Nutzer-Bestätigung "CONFIRM" bevor weitergemacht wird.

## SCHRITT 2: Alle Positionen schließen

Via Alpaca `DELETE /v2/positions` (schließt ALLE Positionen via Market Order):
```bash
curl -s -X DELETE https://paper-api.alpaca.markets/v2/positions \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY"
```

## SCHRITT 3: Offene Orders stornieren

```bash
curl -s -X DELETE "https://paper-api.alpaca.markets/v2/orders" \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY"
```

## SCHRITT 4: Memory updaten

`memory/portfolio.md`:
```
🚨 EMERGENCY STOP — [DATUM] [UHRZEIT]
Grund: [GRUND]
Alle Positionen geschlossen. Alle Orders storniert.
Bot im STOPP-Modus. Kein automatischer Handel bis manueller Reset.
```

`memory/trade-log.md`: Alle offenen Positionen als "EMERGENCY CLOSE" schließen.

## SCHRITT 5: Critical Alert

ClickUp Critical Alert (Priorität 1):
```
🚨 EMERGENCY STOP ausgelöst
Grund: [GRUND]
Alle X Positionen geschlossen.
Realisierter Verlust/Gewinn: X €
Portfolio 100% Cash: X.XXX €
Status: BOT GESTOPPT — manueller Reset nötig
```

## AUSGABE

```
🚨 EMERGENCY STOP AUSGEFÜHRT
Datum/Zeit:    [DATUM] [UHRZEIT]
Grund:         [GRUND]
Geschlossen:   X Positionen
Cash jetzt:    X.XXX € (100%)
Status:        BOT GESTOPPT

Zum Neustart: /status prüfen, dann Routinen manuell neu starten.
ClickUp wurde benachrichtigt.
```
