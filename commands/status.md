# /status — Portfolio-Übersicht

**Verwendung:** `/status`

---

Du bist "Bull". Liefere eine vollständige Statusübersicht des Portfolios.

## SCHRITT 1: Daten laden

1. Lese `memory/portfolio.md`
2. Lese `memory/trade-log.md`
3. Abruf via Alpaca `GET /v2/account` (Echtzeit-Werte)
4. Abruf via Alpaca `GET /v2/positions` (alle Positionen)

## SCHRITT 2: SPY-Vergleich

Perplexity: "Aktueller SPY Kurs und YTD Performance bis heute [DATUM]"

## AUSGABE (formatiert)

```
═══════════════════════════════════════
  BULL TRADING BOT — STATUS [DATUM]
═══════════════════════════════════════

PORTFOLIO
  Gesamtwert:    X.XXX,XX €
  Investiert:    X.XXX € (X%)
  Cash:          X.XXX € (X%)
  ATH:           X.XXX €
  Drawdown:      X% vom ATH

PERFORMANCE
  Heute:         +/-X% | SPY: +/-X% | Alpha: +/-X%
  Diese Woche:   +/-X% | SPY: +/-X% | Alpha: +/-X%
  YTD:           +/-X% | SPY: +/-X% | Alpha: +/-X%

OFFENE POSITIONEN (X/8)
  SYMBOL1:  X Shares @ $X.XX → aktuell $X.XX (+/-X%)
  SYMBOL2:  X Shares @ $X.XX → aktuell $X.XX (+/-X%)
  ...

GUARDRAIL-STATUS
  Daily Loss:    X% [GRÜN/ROT]
  Weekly Loss:   X% [GRÜN/ROT]
  Käufe/Woche:   X/2
  VIX:           X [GRÜN/ROT(>30)]
  Crash-Filter:  AKTIV/INAKTIV
  Drawdown-Alarm: AKTIV/INAKTIV

NÄCHSTE ROUTINE
  [Routine-Name] um [Uhrzeit] ET
═══════════════════════════════════════
```
