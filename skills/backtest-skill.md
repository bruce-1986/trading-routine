# Backtest Skill — Alpaca Trading API

**Zweck:** Historische Backtests der Bull-Bot-Strategie ausführen, bevor ein Symbol in die Watchlist aufgenommen wird.

---

## Wann nutzen

- Neues Symbol wird als Kaufkandidat identifiziert → Strategie historisch validieren
- Strategie-Parameter sollen angepasst werden → Auswirkung testen
- Weekly Review → Top-Performer aus dem Backtest in `memory/research-log.md` eintragen

**NIEMALS** einen Backtest als Grundlage für einen Live-Trade verwenden ohne manuellen Review.

---

## Pflicht-Disclosure

Jeder Report, jede `notes.md`, jede `report.md` muss diesen Block enthalten:

> **Wichtiger Hinweis**
> Dieser Backtest ist eine hypothetische historische Simulation und stellt keine echte Trading-Performance dar. Historische Ergebnisse garantieren keine zukünftigen Ergebnisse. Ergebnisse hängen von Datenqualität, Corporate-Action-Behandlung, Gebühren, Slippage, Liquidität und Ausführungsannahmen ab. Dieses Material dient ausschließlich Research- und Bildungszwecken und ist keine Anlageberatung. Alle Investitionen beinhalten Risiken. Offizielle Hinweise: [alpaca.markets/disclosures](https://alpaca.markets/disclosures)

---

## CLI-Voraussetzungen

### Installation prüfen

```bash
alpaca version
```

Falls nicht installiert:

```bash
# Go
go install github.com/alpacahq/cli/cmd/alpaca@latest

# macOS/Linux mit Homebrew
brew install alpacahq/tap/cli
```

### Auth-Check (immer zuerst)

```bash
alpaca doctor
```

### API-Keys (ausschließlich aus Environment Variables)

```bash
export ALPACA_API_KEY=$env:ALPACA_API_KEY
export ALPACA_SECRET_KEY=$env:ALPACA_SECRET_KEY
export ALPACA_QUIET=1
```

**NIEMALS** Keys in Dateien schreiben, in Reports ausgeben oder in Shell-History exponieren.

---

## Workflow (12 Schritte)

```
Strategie-Idee → Formalisierung → Bestätigung → CLI-Daten → Script → Artefakte → Report
```

1. **Eingaben sammeln:** Symbol, Startdatum, Enddatum
2. **Defaults inferieren:** Asset-Class (Aktie), Timeframe (1Day), Feed (sip), Adjustment (split), Benchmark (SPY buy-and-hold), Initial Cash (Paper-Portfolio-Wert aus `memory/portfolio.md`)
3. **Bull-Strategie formalisieren** (Regeln aus `memory/strategy.md`):
   - Kaufsignal: K1 EMA50>EMA200, K2 RSI(14) 50–70, K3 RS>SPY 63 Tage, K4 Vol>=120% Avg20, K5 FwdPE<=35 & Wachstum>=10%
   - Verkaufssignal: V1 -8% Stop, V2 -12% Trailing, V3 +20% Teilverkauf, V4 +35% Restverkauf, V5 Death Cross, V6 RSI>80 & RS<0
   - Sizing: 10% Portfolio (7% wenn VIX>25), max. 8 Positionen, min. 20% Cash
4. **Interpretation bestätigen** — vor Code-Generierung kurz zeigen was angenommen wird
5. **Workspace prüfen** — gibt es bereits Rohdaten für dieses Symbol/Zeitraum?
6. **Run-Folder anlegen** (siehe unten)
7. **`notes.md` und `strategy_spec.json` schreiben**
8. **Daten via Alpaca CLI fetchen**
9. **Simulation lokal ausführen**
10. **Artefakte schreiben**
11. **Teaching Five ausgeben** (siehe Report-Standard)
12. **Ergebnis in `memory/research-log.md` eintragen** (komprimiert, max. 5 Zeilen)

---

## Run-Folder-Struktur

```
runs/YYYY-MM-DD_SYMBOL_bull-momentum_1Day/
  notes.md
  strategy_spec.json
  config.json
  run.py
  requirements.txt
  raw/
    bars_SYMBOL.json
    calendar.json
  normalized/
    bars_SYMBOL.csv
  summary.json
  report.md
  trades.csv
  round_trips.csv
  equity.csv
  benchmark_equity.csv
  data_fingerprint.json
  warnings.json
```

---

## Daten fetchen (Alpaca CLI)

```bash
# Tages-Bars (split-adjustiert)
alpaca data bars \
  --symbol AAPL \
  --start 2022-01-01 \
  --end 2024-12-31 \
  --timeframe 1Day \
  --feed sip \
  --adjustment split \
  --quiet

# Handelskalender
alpaca calendar --start 2022-01-01 --end 2024-12-31 --quiet
```

---

## Code-Regeln für `run.py`

- Einzelne lesbare Datei (kein Framework)
- Rohdaten aus Run-Folder lesen, kein Netzwerkaufruf nach Data-Fetch
- Signal-Timing von Fill-Timing trennen
- **Fill-Modell:** `next_open` — Signal auf Bar-T-Close, Fill auf Bar-T+1-Open + 0,5% Slippage (wie in Strategie)
- Exakte Indikator-Definitionen implementieren:
  - EMA: exponentieller gleitender Durchschnitt, `span=50` bzw. `span=200`, `adjust=False`
  - RSI(14): Wilder's Smoothing (EWM mit `alpha=1/14`)
  - Relative Stärke: `(Aktie-Return 63T) - (SPY-Return 63T)`
  - Volumen-Ratio: `Volume / Volume.rolling(20).mean()`
- Stop-Loss V1 und V2 täglich neu berechnen
- Gebühren: 0 $ (Alpaca equity-Gebühren, kein Spread-Modell)
- Deterministisches Sorting, UTC-Timestamps

```python
# Lesbares Beispiel für Fill
fill_price = bar_open * 1.005  # +0.5% Slippage wie Limit-Regel
```

---

## Report-Standard

`report.md` beginnt mit **Performance vs. Benchmark**:

```markdown
| | Gesamt-Return | Ann. Return | Max. Drawdown | Sharpe | End-Kapital |
|---|---:|---:|---:|---:|---:|
| **Bull-Strategie** | ...% | ...% | ...% | ... | $... |
| SPY Buy-and-Hold | ...% | ...% | ...% | ... | $... |
```

Danach: Strategie-Konfiguration, Fill-Modell, erster/letzter Trade, Annahmen, Data-Fingerprint, Caveats, Disclosure-Block.

---

## Teaching Five (In-Chat-Antwort)

Immer zuerst ausgeben:

1. Gesamt-Return vs. SPY
2. Max. Drawdown
3. Anzahl Trades
4. Win Rate
5. Sharpe Ratio vs. SPY

Dann: Annualisierter Return, Profit Factor, erste/letzte Trade, wichtigste Caveats, Artefakt-Pfade.

---

## Memory-Integration

Nach dem Backtest in `memory/research-log.md` eintragen:

```
[DATUM] Backtest [SYMBOL] [ZEITRAUM]: Return X% vs. SPY Y%, Sharpe Z, N Trades, Win-Rate W%.
Fazit: [Kaufkandidat / Abgelehnt / Bedingt (Begründung)]
```

Maximal 3–5 Zeilen. Kein Raw-Output.

---

## Sicherheits-Guardrails

Der Skill darf NIEMALS:
- Zukunftsdaten im Signal verwenden (Look-ahead Bias)
- `same_bar`-Fill ohne explizite Dokumentation nutzen
- Live-Orders als Teil des Backtests senden
- Direkte HTTP-Calls statt Alpaca CLI verwenden
- Adjusted und unadjusted Bars mischen
- Vage Signale als "vollständig spezifiziert" behandeln

---

## Troubleshooting

```
alpaca: command not found
  → PATH prüfen, Go-Install unter ~/go/bin

alpaca doctor: Auth-Fehler
  → ALPACA_API_KEY und ALPACA_SECRET_KEY neu setzen

CLI-Output enthält Nicht-Daten-Text
  → --quiet oder ALPACA_QUIET=1 verwenden

Rate Limit
  → Retry-After abwarten, gecachte Daten nutzen wenn Fingerprint passt

Pagination / fehlende Daten
  → next_page_token prüfen, alle Seiten fetchen
```

---

## Nützliche CLI-Befehle

```bash
alpaca version
alpaca doctor
alpaca --help-all
alpaca data bars --help
alpaca data bars --schema
alpaca calendar --help
```
