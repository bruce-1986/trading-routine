# Trade Skill — Alpaca API

**Zweck:** Orders platzieren, Positionen abrufen, Portfolio-Status prüfen

---

## API-Konfiguration

```
Paper URL:  https://paper-api.alpaca.markets   (Standard, solange ALPACA_LIVE=false)
Live URL:   https://api.alpaca.markets          (NUR wenn ALPACA_LIVE=true explizit gesetzt)
Data URL:   https://data.alpaca.markets

Auth-Header:
  APCA-API-KEY-ID:     $env:ALPACA_API_KEY
  APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY
```

**WICHTIG:** Vor jedem API-Call prüfen: `$env:ALPACA_LIVE` == "true"?  
→ NEIN (Default): Paper-URL verwenden.  
→ JA: Live-URL verwenden + extra ClickUp-Alert senden.

---

## Häufige API-Calls

### 1. Account-Status abrufen

```bash
curl -s https://paper-api.alpaca.markets/v2/account \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY"
```

Relevante Felder: `portfolio_value`, `cash`, `buying_power`, `equity`

### 2. Alle offenen Positionen

```bash
curl -s https://paper-api.alpaca.markets/v2/positions \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY"
```

Relevante Felder: `symbol`, `qty`, `avg_entry_price`, `current_price`, `unrealized_pl`, `unrealized_plpc`

### 3. Limit-Order KAUFEN

```bash
curl -s -X POST https://paper-api.alpaca.markets/v2/orders \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol":        "AAPL",
    "qty":           "10",
    "side":          "buy",
    "type":          "limit",
    "time_in_force": "day",
    "limit_price":   "185.50"
  }'
```

**Limit-Preis-Regel:** max. +0,5% über Vortagesschluss.  
`limit_price = round(prev_close * 1.005, 2)`

### 4. Limit-Order VERKAUFEN (Teilposition)

```bash
curl -s -X POST https://paper-api.alpaca.markets/v2/orders \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol":        "AAPL",
    "qty":           "5",
    "side":          "sell",
    "type":          "limit",
    "time_in_force": "day",
    "limit_price":   "220.00"
  }'
```

### 5. Market-Order VERKAUFEN (Stop-Loss — sofort)

```bash
curl -s -X POST https://paper-api.alpaca.markets/v2/orders \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol":        "AAPL",
    "qty":           "10",
    "side":          "sell",
    "type":          "market",
    "time_in_force": "day"
  }'
```

**Nur für V1 (Stop-Loss) und V2 (Trailing Stop) verwenden.**

### 6. Offene Orders abrufen

```bash
curl -s "https://paper-api.alpaca.markets/v2/orders?status=open" \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY"
```

### 7. Marktdaten — Letzter Kurs

```bash
curl -s "https://data.alpaca.markets/v2/stocks/AAPL/trades/latest" \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY"
```

### 8. Marktdaten — Bars (für EMA/RSI Berechnung)

```bash
curl -s "https://data.alpaca.markets/v2/stocks/AAPL/bars?timeframe=1Day&limit=200" \
  -H "APCA-API-KEY-ID: $env:ALPACA_API_KEY" \
  -H "APCA-API-SECRET-KEY: $env:ALPACA_SECRET_KEY"
```

---

## Position-Sizing Berechnung

```
portfolio_value = [aus /v2/account]
position_budget = portfolio_value * 0.10          # 10% Standard
                = portfolio_value * 0.07          # wenn VIX > 25
shares          = floor(position_budget / price)
```

**Vorher prüfen:**
- Cash >= position_budget (sonst nicht kaufen)
- Anzahl offener Positionen < 8
- Käufe diese Woche < 2
- Sektor-Gewichtung nach Kauf <= 30%

---

## Post-Trade Pflicht

Nach JEDEM Order-Call:
1. Order-ID aus Response extrahieren
2. Eintrag in `memory/trade-log.md` schreiben
3. `memory/portfolio.md` updaten
4. ClickUp-Notification senden (via `skills/notify-skill.md`)

---

## Fehler-Handling

| HTTP-Status | Bedeutung | Aktion |
|---|---|---|
| 403 | Kein Guthaben / Konto gesperrt | Sofort stoppen, Critical Alert |
| 422 | Ungültige Order (z.B. Markt geschlossen) | Loggen, Order für nächsten Tag queuen |
| 429 | Rate Limit | 5 Sekunden warten, einmal retry |
| 5xx | Alpaca-Server-Fehler | 60 Sekunden warten, einmal retry, dann Alert |
