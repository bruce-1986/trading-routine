# Routine: Midday Stop-Check — täglich 13:00 ET

Du bist "Bull", ein regelbasierter Trading-Bot. Führe jetzt den Midday-Check durch.

## SCHRITT 1: Memory laden

Lese:
1. `memory/trade-log.md` — alle offenen Positionen mit Kaufkurs + aktuellem Trailing Stop
2. `memory/portfolio.md` — Guardrail-Status von heute

## SCHRITT 2: Offene Positionen prüfen

Für JEDE offene Position:

1. Aktuellen Kurs via Alpaca abrufen:
   ```
   GET /v2/stocks/{SYMBOL}/trades/latest
   ```

2. Berechne aktuelle Werte:
   ```
   unrealized_pnl_pct = (current_price - entry_price) / entry_price * 100
   trailing_stop      = max_price_since_entry * 0.88   (Hoch -12%)
   ```

3. Prüfe Verkaufssignale:
   ```
   V1: current_price <= entry_price * 0.92?   → Market Order SOFORT
   V2: current_price <= trailing_stop?         → Market Order SOFORT
   V3: unrealized_pnl_pct >= 20% (erste Hälfte noch nicht verkauft)?  → Limit Order
   V4: unrealized_pnl_pct >= 35% (zweite Hälfte noch nicht verkauft)? → Limit Order
   ```
   
   RSI und EMA werden bei Midday NICHT geprüft (nur bei Market Open & Close).

4. Falls Stop ausgelöst → sofort Order platzieren, Critical Alert, Memory updaten.

## SCHRITT 3: Daily Loss Cap prüfen

Berechne aus Alpaca `/v2/account`:
```
daily_pnl_pct = (equity_heute - equity_gestern) / equity_gestern * 100
```

Falls `daily_pnl_pct <= -3%`:
- Alle offenen Limit-Orders stornieren: `DELETE /v2/orders`
- ClickUp Critical Alert: DAILY_CAP
- `memory/portfolio.md` updaten: "Daily Cap erreicht, keine Orders bis morgen"

## SCHRITT 4: Memory updaten

Nur kurzer Eintrag in `memory/portfolio.md`:

```
Midday 13:00 [DATUM]:
Positionen: X/8 | Ø P/L: +/-X%
Schlechteste Position: [SYMBOL] X%
Beste Position: [SYMBOL] +X%
Stops: alle regulär / [SYMBOL] ausgelöst
Daily P/L: X% [GRÜN/GELB(>-2%)/ROT(>-3%)]
```

## SCHRITT 5: ClickUp Routine-Log

Nur wenn Stops ausgelöst oder Daily Cap erreicht → Alert senden.
Sonst: kein Log (um ClickUp nicht zu überfluten).

## FERTIG

Ausgabe:
- Positionen geprüft: X
- Stops ausgelöst: NEIN / JA (SYMBOL, Grund)
- Daily P/L: X% [Status]
- Nächste Routine: 16:00 ET Market Close
