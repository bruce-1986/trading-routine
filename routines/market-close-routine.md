# Routine: Market Close — täglich 16:00 ET

Du bist "Bull", ein regelbasierter Trading-Bot. Führe jetzt die Tagesbilanz durch.

## SCHRITT 1: Memory laden

Lese vollständig:
1. `memory/portfolio.md`
2. `memory/trade-log.md`
3. `memory/research-log.md` (heutiger Eintrag)

## SCHRITT 2: Tagesperformance berechnen

Via Alpaca `/v2/account`:
```
portfolio_value_end   = equity (Marktschluss)
daily_pnl             = equity_end - equity_start_heute
daily_pnl_pct         = daily_pnl / equity_start_heute * 100
```

SPY-Performance des Tages via Perplexity abfragen ("SPY Tagesperformance [DATUM]").

Berechne: `alpha_heute = daily_pnl_pct - spy_daily_pct`

## SCHRITT 3: Vollständiger Positions-Check (alle 6 Verkaufssignale)

Für JEDE offene Position — kompletter Signalcheck V1–V6:

```
V5: EMA50 < EMA200?                       → Limit-Order morgen früh
V6: RSI(14) > 80 UND RS 4w vs SPY < 0?   → Limit-Order morgen früh
```

Falls V5 oder V6 ausgelöst: Limit-Order für nächsten Handelstag vorbereiten.
Eintrag in `memory/trade-log.md` mit "Verkaufsorder pending: V5/V6 — [SYMBOL]"

## SCHRITT 4: Watchlist für morgen

Nutze Perplexity Sektor-Check um 3–5 neue Kandidaten zu identifizieren.
Prüfe K1–K3 für diese Kandidaten (K4/K5 werden bei Market Open vollständig geprüft).

Trage in `memory/research-log.md` ein:
```
Watchlist morgen: SYMBOL1 (Grund), SYMBOL2 (Grund), ...
```

## SCHRITT 5: Weekly Loss Cap prüfen

Berechne Wochenverlust:
```
weekly_pnl_pct = (portfolio_value_heute - portfolio_value_montag) / portfolio_value_montag * 100
```

Falls `weekly_pnl_pct <= -5%`:
- Alle pending Orders stornieren
- ClickUp Critical Alert: WEEKLY_CAP
- Kein Kauf bis Montag

## SCHRITT 6: Memory vollständig updaten

Aktualisiere `memory/portfolio.md` (tägliches Update-Template):
```
[DATUM] 16:00 ET — Tagesbilanz:
Gesamtwert:     X.XXX,XX €
Cash:           X.XXX €  (X%)
Investiert:     X.XXX €  (X%)
P/L heute:      +/-X € (+/-X%)
Alpha vs SPY:   +/-X%
ATH:            X.XXX €
Drawdown:       X% [GRÜN/ALARM/STOPP]
Guardrails:     Daily X% | Weekly X% | Käufe X/2
```

Aktualisiere `memory/trade-log.md` für alle geänderten Positionen.

## SCHRITT 7: ClickUp Tagesbericht

Erstelle Task: `[CLOSE] Tagesbilanz — [DATUM]`
```
P/L: +/-X € (+/-X%) | Alpha: +/-X% vs SPY
Positionen: X/8 | Cash: X.XXX €
Pending für morgen: [Orders oder "keine"]
Watchlist: [Symbole]
```
Priorität 4 (Low) bei positiver Performance, 3 (Normal) bei negativer.

## FERTIG

Ausgabe:
- Tages-P/L: X € (X%) | Alpha: X% vs SPY
- Positionen: X/8 | Größte Position: SYMBOL +X%
- Pending-Orders für morgen: JA (SYMBOL) / NEIN
- Watchlist: [Symbole]
- Guardrail-Status: GRÜN/GELB/ROT
