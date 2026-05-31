# Research Skill — Perplexity API

**Zweck:** Markt-Research, Makro-News, Earnings-Check, Sektor-Analyse

---

## API-Konfiguration

```
Base URL:  https://api.perplexity.ai/chat/completions
Auth:      Bearer $env:PERPLEXITY_API_KEY
Model:     sonar-pro   (für aktuellste Daten mit Web-Search)
```

---

## Standard-Anfragen

### 1. Daily Macro Check (Pre-Market)

```bash
curl -s https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $env:PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "messages": [{
      "role": "user",
      "content": "Gib mir einen kompakten Markt-Überblick für heute: VIX Stand, SPY Premarket, 10Y Treasury Yield, wichtige Makro-Ereignisse heute (Fed, CPI, Jobs), und Top 3 marktbewegende News. Antworte in maximal 200 Wörtern, strukturiert."
    }]
  }'
```

### 2. Earnings-Kalender (nächste 5 Tage)

```bash
curl -s https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $env:PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "messages": [{
      "role": "user",
      "content": "Welche S&P 500 Unternehmen berichten Earnings in den nächsten 5 Handelstagen? Liste: Datum, Symbol, EPS-Konsenserwartung, Marktkapitalisierung. Nur Unternehmen mit Marktkapitalisierung > 5 Mrd. $."
    }]
  }'
```

### 3. Symbol-Research (vor Kauf)

```bash
# Ersetze SYMBOL mit z.B. AAPL, MSFT etc.
curl -s https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $env:PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "messages": [{
      "role": "user",
      "content": "Analysiere [SYMBOL] für einen mittel- bis langfristigen Kauf (6 Monate). Liefere: Forward P/E, Umsatzwachstum YoY, nächste Earnings-Date, wichtige Risiken, Analysten-Konsens (Buy/Hold/Sell Ratio). Kompakt, maximal 150 Wörter."
    }]
  }'
```

### 4. Sektor-Check (wöchentlich)

```bash
curl -s https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $env:PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "messages": [{
      "role": "user",
      "content": "Welche S&P 500 Sektoren haben in den letzten 5 Handelstagen den SPY outperformt? Ranking nach Relative Stärke, mit kurzer Begründung. Format: Tabelle mit Sektor, ETF-Symbol, 5-Tage-Performance, Begründung."
    }]
  }'
```

---

## Ausgabe-Verarbeitung

Perplexity-Antworten **immer komprimieren** bevor sie in Memory geschrieben werden:
- Zahlen extrahieren (VIX, Preise, P/E)
- Nur handlungsrelevante Fakten behalten
- Quellen-Links weglassen
- Maximal 5 Zeilen pro Research-Eintrag in `memory/research-log.md`

---

## Fehler-Handling

| Fehler | Aktion |
|---|---|
| API nicht erreichbar | Routine mit "Research nicht verfügbar" weiterführen, kein Kauf |
| Rate-Limit (429) | 60 Sekunden warten, einmal retry, dann weiterführen |
| Leere Antwort | Als "Keine Daten" loggen, keinen Trade basierend darauf ausführen |
