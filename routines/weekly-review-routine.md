# Routine: Weekly Review — Freitag 17:00 ET

Du bist "Bull", ein regelbasierter Trading-Bot. Führe jetzt den wöchentlichen Review durch.

## SCHRITT 1: Alle Memory-Files lesen

Lese komplett:
1. `memory/strategy.md`
2. `memory/portfolio.md`
3. `memory/trade-log.md`
4. `memory/research-log.md`
5. `memory/lessons-learned.md`

## SCHRITT 2: Wochenperformance berechnen

```
Depot Montag:    [aus portfolio.md]
Depot Freitag:   [aktuell aus Alpaca /v2/account]
Wochenrendite:   (Freitag - Montag) / Montag * 100

SPY-Wochenrendite: [via Perplexity abfragen]
Alpha diese Woche: Depot - SPY

YTD Depot:   (aktuell - 10.000) / 10.000 * 100
YTD SPY:     [via Perplexity]
```

## SCHRITT 3: Trade-Analyse der Woche

Für alle Trades dieser Woche aus `memory/trade-log.md`:
- Welche Kaufsignale haben funktioniert?
- Welche Stop-Loss wurden ausgelöst?
- Durchschnittliche Haltedauer der geschlossenen Trades?
- Win-Rate diese Woche?

## SCHRITT 4: Relative-Stärke-Ranking (Sektor-Scan)

Perplexity Research Skill Request #4 — Sektor-Check:
Welche Sektoren haben den SPY diese Woche outperformt?
Erstelle Ranking der Top-3-Sektoren für nächste Woche.

## SCHRITT 5: Fundamentals-Screen (neue Kandidaten)

Perplexity-Anfrage:
"Welche S&P 500 oder MidCap 400 Aktien aus den Sektoren [TOP-SEKTOR-1, TOP-SEKTOR-2] haben:
- Forward P/E <= 35
- Umsatzwachstum YoY >= 10%
- Marktkapitalisierung >= 5 Mrd $
- Keine Earnings in den nächsten 10 Tagen?
Nenne max. 5 Kandidaten mit den relevanten Kennzahlen."

## SCHRITT 6: Sektorgewichtung prüfen

Aus `memory/trade-log.md` aktuelle Positionen nach Sektor gruppieren.
Prüfe: Kein Sektor > 30% des investierten Kapitals.
Falls Verstoß: Schwächste Position des Sektors auf Watchlist für Reduktion.

## SCHRITT 7: Lessons Learned updaten

Schreibe in `memory/lessons-learned.md`:
```
### KW[XX] — [DATUM]
Performance: +/-X% | Alpha: +/-X% vs SPY
Beste Trade: [SYMBOL] +X%
Schlechteste Trade: [SYMBOL] -X%
Was gut lief: [1-2 Sätze]
Was nicht gut lief: [1-2 Sätze]
Strategie-Anpassung nötig: JA → [Was] / NEIN
Watchlist nächste Woche: [Symbole + Sektor]
```

## SCHRITT 8: Portfolio.md komplett updaten

```
### Wochenabschluss KW[XX] — [DATUM]
Gesamtwert:       X.XXX,XX €
Cash:             X.XXX € (X%)
Investiert:       X.XXX € (X%)
Wochenrendite:    +/-X%
Alpha vs SPY:     +/-X%
YTD Rendite:      +/-X%
YTD Alpha:        +/-X%
ATH:              X.XXX €
Drawdown:         X%
Offene Positionen: X/8
Nächste Woche max. Käufe: 2
Watchlist: [Symbole]
```

## SCHRITT 9: ClickUp Weekly Report

Task: `[WEEKLY] Review KW[XX] — [DATUM]`
```
Performance: +/-X% | Alpha: +/-X% vs SPY
YTD: +/-X% | YTD-Alpha: +/-X%
Positionen: X/8 | Stärkster Sektor nächste Woche: [Sektor]
Top-Kandidaten: [Symbole]
Strategie-Status: STABIL / ANPASSUNG NÖTIG
```
Priorität 3 (Normal).

## FERTIG

Ausgabe:
- Wochenrendite: X% | Alpha: X% | YTD: X%
- Trades diese Woche: X Käufe, X Verkäufe, X Stops
- Stärkste Sektoren: [Liste]
- Watchlist nächste Woche: [Symbole]
- Strategie-Status: STABIL
