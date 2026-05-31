# Notify Skill — ClickUp API

**Zweck:** Trading-Alerts, Trade-Logs und Critical Events in ClickUp melden

---

## API-Konfiguration

```
Base URL:  https://api.clickup.com/api/v2
Auth:      Authorization: Bearer $env:CLICKUP_API_KEY
List-ID:   $env:CLICKUP_LIST_ID           (normale Trade-Tasks)
Critical:  $env:CLICKUP_CRITICAL_LIST_ID  (Stop-Loss, Drawdown-Stopp, Fehler)
```

---

## Alert-Typen und wann sie ausgelöst werden

| Typ | Priorität | Auslöser | List |
|---|---|---|---|
| TRADE_BUY | Normal | Kauf ausgeführt | CLICKUP_LIST_ID |
| TRADE_SELL | Normal | Verkauf ausgeführt | CLICKUP_LIST_ID |
| STOP_LOSS | Urgent | V1 oder V2 ausgelöst | CLICKUP_CRITICAL_LIST_ID |
| DAILY_CAP | Urgent | -3% Daily Loss erreicht | CLICKUP_CRITICAL_LIST_ID |
| DRAWDOWN_ALARM | Urgent | -15% vom ATH | CLICKUP_CRITICAL_LIST_ID |
| DRAWDOWN_STOP | Critical | -20% vom ATH | CLICKUP_CRITICAL_LIST_ID |
| CRASH_FILTER | Urgent | SPY -5% an einem Tag | CLICKUP_CRITICAL_LIST_ID |
| VIX_FILTER | Normal | VIX > 30 | CLICKUP_LIST_ID |
| ROUTINE_DONE | Normal | Routine erfolgreich beendet | CLICKUP_LIST_ID |
| API_ERROR | Urgent | API nicht erreichbar | CLICKUP_CRITICAL_LIST_ID |

---

## Task erstellen (Standard-Trade)

```bash
curl -s -X POST "https://api.clickup.com/api/v2/list/$env:CLICKUP_LIST_ID/task" \
  -H "Authorization: Bearer $env:CLICKUP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "[TRADE_BUY] AAPL — 10 Shares @ $185.50",
    "description": "Kaufsignale: K1✓ K2✓ K3✓ K4✓ K5✓\nInvestiert: 1.855,00 €\nStop-Loss: $170.66 (-8%)\nTP1: $222.60 (+20%)\nTP2: $250.43 (+35%)\nAlpaca Order-ID: abc123",
    "priority": 3,
    "tags": ["buy", "AAPL", "momentum"]
  }'
```

**Prioritäten:** 1=Urgent (rot), 2=High (orange), 3=Normal (gelb), 4=Low (blau)

---

## Critical Alert (Stop-Loss / Drawdown)

```bash
curl -s -X POST "https://api.clickup.com/api/v2/list/$env:CLICKUP_CRITICAL_LIST_ID/task" \
  -H "Authorization: Bearer $env:CLICKUP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "🚨 [STOP_LOSS] AAPL — Stop ausgelöst",
    "description": "STOP-LOSS V1 ausgelöst!\nPosition: 10 Shares AAPL\nKaufkurs: $185.50\nAusstieg: $170.66 (-8%)\nVerlust: -148,40 €\nAlpaca Market Order platziert.\n\nPortfolio nach Trade:\nGesamt: 9.851,60 € | Cash: 7.996,60 € | Positionen: X/8",
    "priority": 1,
    "tags": ["critical", "stop-loss", "AAPL"]
  }'
```

---

## Routine-Abschluss-Log

```bash
curl -s -X POST "https://api.clickup.com/api/v2/list/$env:CLICKUP_LIST_ID/task" \
  -H "Authorization: Bearer $env:CLICKUP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "[ROUTINE] Pre-Market Check — 2026-05-31 08:30 ET",
    "description": "Routine abgeschlossen.\nVIX: 18.5 | SPY Premarket: +0.3%\nGuardrails: GRÜN\nWatchlist: MSFT, NVDA (Kandidaten)\nKauf heute: NEIN (warten auf Market Open Scan)\nNächste Routine: 09:30 ET Market Open",
    "priority": 4,
    "tags": ["routine", "premarket"]
  }'
```

---

## Kommentar zu bestehendem Task hinzufügen

```bash
curl -s -X POST "https://api.clickup.com/api/v2/task/{TASK_ID}/comment" \
  -H "Authorization: Bearer $env:CLICKUP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "comment_text": "Update 13:00 Midday: Position +8.3%. Trailing Stop angepasst auf $175.50 (aktuelles Hoch $202.30 -12%)."
  }'
```

---

## Fehler-Handling

| Fehler | Aktion |
|---|---|
| ClickUp API down | Direkt in `memory/trade-log.md` schreiben, weiterarbeiten |
| 401 Unauthorized | CLICKUP_API_KEY prüfen, Routine stoppen |
| 429 Rate Limit | 30 Sekunden warten, einmal retry |

**Fallback:** Bei ClickUp-Ausfall immer in Memory-Files schreiben. Notifications sind sekundär, Memory ist primär.
