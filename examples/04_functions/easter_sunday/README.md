# Datum des Ostersonntags berechnen

## Lernziel

Eine Funktion mit Parameter und Rückgabewert schreiben, eine vorgegebene
Rechenvorschrift mit `//` und `%` umsetzen und Datumswerte mit `unittest` prüfen.
Sonderfälle und Grenzen des gültigen Eingabebereichs berücksichtigen.

## Aufgabe

Schreibe die Funktion:

```python
from datetime import date

def ostersonntag(jahr: int) -> date:
    ...
```

1. Berechne den Ostersonntag des westlichen Osterfestes im gregorianischen Kalender.
2. Gib das Ergebnis als `datetime.date` zurück.
3. Unterstütze ganze Jahre von **1583 bis 4099 einschließlich**. Für Jahre
   außerhalb dieses Bereichs löse einen `ValueError` aus.
4. Gib das Datum außerhalb der Funktion mit `print()` aus.

Beispiel:

```python
ostersonntag(2026)
# Rückgabewert: date(2026, 4, 5)
```

Verwende die gregorianische Osterformel von Gauß wie in `answer.py`:
Berechne zuerst die Reste des Jahres bei Division durch 19, 4 und 7.
Bestimme anschließend die Jahrhundertkorrekturen, den Vollmondrest und den
Abstand zum Sonntag. Addiere beide letzten Werte zum 22. März mit `timedelta`.
Berücksichtige davor die beiden Sonderfälle, die den Termin um sieben Tage
zurücksetzen. `//` bedeutet ganzzahlige Division, `%` liefert den Rest.

## Dateien

- `answer.py` enthält die Musterlösung mit erklärenden Variablennamen und einen Beispielaufruf.
- `test_answer.py` prüft feste Ostertermine, beide Korrekturfälle, Jahrhundertwechsel,
  die früheste und späteste mögliche Lage sowie ungültige Jahre.
  Die unabhängige Referenzfunktion `correct(jahr)` verwendet die
  Meeus/Jones/Butcher-Osterformel und liefert das erwartete Datum.
  Zusätzlich vergleicht es für alle unterstützten Jahre das Ergebnis mit `correct(jahr)`
  und prüft, dass es ein Sonntag
  zwischen dem 22. März und dem 25. April desselben Jahres ist.

## Import in LETTO

Importiere `Frage_Ostersonntag.lto` in LETTO. Die Datei enthält die Aufgabenstellung
mit vorgegebener Osterformel, Startercode ohne fertige Lösung und die Tests samt
Referenzfunktion `correct(jahr)`. Die Aufgabe benötigt das Python-Plugin;
zusätzliche Dateien oder Pakete sind nicht erforderlich.

`build_lto.py` erzeugt den Export erneut aus den aktuellen Tests und der vorhandenen
SQLite-Exportvorlage. Starte es vom Repository-Hauptordner:

```bash
python examples/04_functions/easter_sunday/build_lto.py
```

Die IDs der Vorlage werden auf `0` gesetzt. XML, Plugin-Konfiguration und
eingebettete Tests wurden lokal geprüft. Ein Import in eine laufende
LETTO-Instanz wurde nicht durchgeführt.

## Voraussetzungen

Python 3.9 oder neuer, nur Standardbibliothek. Kenntnisse zu Funktionen,
Ganzzahlarithmetik, Bedingungen und Ausnahmen. Die Eingabe ist eine ganze Zahl;
eine Prüfung des Datentyps ist nicht Teil der Aufgabe.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/04_functions/easter_sunday/answer.py
python -m unittest discover -s examples/04_functions/easter_sunday -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Die Osterformel sollte vorgegeben werden; das Lernziel ist ihre Umsetzung und
Prüfung, nicht die Herleitung der Kalenderrechnung. Die Jahre 1954 und 1981
prüfen die beiden unterschiedlichen Sonderfälle. Die Referenzfunktion verwendet
eine andere Osterformel als die Musterlösung; feste Erwartungswerte prüfen
zusätzlich die Referenzfunktion. Die allgemeinen
Kalenderprüfungen ergänzen diese Werte, ersetzen sie aber nicht.

Die Aufgabe behandelt das westliche Osterfest. Für das orthodoxe Osterfest gelten
andere Berechnungsregeln. Eine Übersicht der Varianten und des hier gewählten
Jahresbereichs bietet die [dateutil-Dokumentation](https://dateutil.readthedocs.io/en/stable/easter.html).
Die Bibliothek wird für dieses Beispiel nicht benötigt.
