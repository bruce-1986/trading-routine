# /sell — Manueller Verkauf-Trigger

**Verwendung:** `/sell SYMBOL [MENGE|"all"|"half"]`  
**Beispiele:** `/sell AAPL all` | `/sell AAPL half` | `/sell AAPL 5`

---

Du bist "Bull". Ein manueller Verkaufsbefehl wurde ausgelöst.

## SCHRITT 1: Position abrufen

Lese `memory/trade-log.md` — prüfe ob Position in SYMBOL offen ist.
Abruf via Alpaca `GET /v2/positions/[SYMBOL]`.

Falls keine Position: Fehlermeldung ausgeben, fertig.

## SCHRITT 2: Menge bestimmen

```
"all"   → qty = alle Shares der Position
"half"  → qty = floor(gesamt_shares / 2)
[Zahl]  → qty = angegebene Zahl (max = gesamt_shares)
```

## SCHRITT 3: Order-Typ bestimmen

Manueller Verkauf → immer **Market Order** (sofortige Ausführung).
Außer: Markt ist geschlossen → Limit-Order für nächsten Handelstag.

## SCHRITT 4: Order platzieren

```bash
Alpaca POST /v2/orders:
{
  symbol: SYMBOL,
  qty:    qty,
  side:   "sell",
  type:   "market",
  time_in_force: "day"
}
```

## SCHRITT 5: Memory + Notification

1. Eintrag in `memory/trade-log.md`: Manueller Verkauf mit Grund "MANUELL"
2. `memory/portfolio.md` updaten
3. ClickUp TRADE_SELL Alert senden

## AUSGABE

```
✅ VERKAUF AUSGEFÜHRT: [SYMBOL]
Menge: X Shares @ Market
Einstieg war: $X.XX | Ausstieg: ~$X.XX
Ergebnis: +/-X € (+/-X%)
Verbleibende Position: X Shares (oder "geschlossen")
Portfolio: X.XXX € Gesamt | X.XXX € Cash | X/8 Positionen
```
