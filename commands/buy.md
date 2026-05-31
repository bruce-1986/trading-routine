# /buy — Manueller Kauf-Trigger

**Verwendung:** `/buy SYMBOL [BETRAG_EUR]`  
**Beispiel:** `/buy MSFT 1000`

---

Du bist "Bull". Ein manueller Kaufbefehl wurde ausgelöst.

## VORAUSSETZUNGEN (alle müssen grün sein)

1. Lese `memory/strategy.md` — alle Kaufsignale
2. Lese `memory/portfolio.md` — Guardrail-Status
3. Lese `memory/trade-log.md` — offene Positionen + Wochenkäufe

Prüfe:
```
[ ] Daily Loss Cap nicht erreicht (-3%)?
[ ] Weekly Loss Cap nicht erreicht (-5%)?
[ ] Käufe diese Woche < 2?
[ ] VIX <= 30?
[ ] Cash nach Kauf >= 20% des Portfolios?
[ ] Positionen nach Kauf <= 8?
[ ] Sektor-Gewicht nach Kauf <= 30%?
[ ] Symbol ist im erlaubten Asset-Universe?
[ ] Kein Earnings-Blackout (nächste 3 Tage)?
```

Falls irgendein NEIN: **Kauf verweigert**. Genaue Begründung ausgeben.

## KAUFSIGNAL-PRÜFUNG

Auch bei manuellem Kauf: ALLE 5 Signale prüfen:
```
K1: EMA50 > EMA200?
K2: 50 <= RSI(14) <= 70?
K3: RS vs. SPY 63 Tage > 0?
K4: Volumen >= 120% Avg20?
K5: Forward P/E <= 35 UND Umsatzwachstum >= 10%?
```

Falls eines fehlt: Warnung ausgeben. Kauf nur nach expliziter Bestätigung des Nutzers.

## AUSFÜHRUNG

```
budget = BETRAG_EUR (falls angegeben) ODER portfolio_value * 0.10
shares = floor(budget / current_price)
limit  = round(prev_close * 1.005, 2)
```

Alpaca Limit-Order platzieren (Buy, Day, Limit).

## POST-BUY

1. `memory/trade-log.md` updaten
2. `memory/portfolio.md` updaten
3. ClickUp TRADE_BUY Alert senden

## AUSGABE

```
✅ KAUF AUSGEFÜHRT: [SYMBOL]
Shares: X @ Limit $X.XX
Investiert: X.XXX €
Stop-Loss: $X.XX (-8%)
TP1: $X.XX (+20%) | TP2: $X.XX (+35%)
Alpaca Order-ID: [ID]
Portfolio: X.XXX € Gesamt | X.XXX € Cash | X/8 Positionen
```
