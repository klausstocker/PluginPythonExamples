# Bestellung mit Dataclasses prüfen

## Lernziel

Artikel- und Bestelldaten mit Dataclasses modellieren.
Datenfelder mit `str`, `int` und `bool` beschreiben, Objekte erzeugen und über
Attribute auf Werte zugreifen. Ein neues Ergebnisobjekt zurückgeben.

## Aufgabe

Definiere mit `@dataclass` drei Klassen mit genau diesen Feldern:

| Klasse | Felder |
| --- | --- |
| `Artikel` | `name: str`, `bestand: int`, `aktiv: bool` |
| `Bestellung` | `kunde: str`, `menge: int` |
| `Bestellergebnis` | `kunde: str`, `artikel: str`, `menge: int`, `lieferbar: bool` |

Importiere dafür `dataclass` aus dem Modul `dataclasses`.
Schreibe anschließend die Funktion:

```python
def bestellung_pruefen(
    artikel: Artikel, bestellung: Bestellung
) -> Bestellergebnis:
    ...
```

Die Funktion erhält ein Artikelobjekt und ein Bestellobjekt. Erzeuge ein
**neues `Bestellergebnis`** mit Kundenname, Artikelname und Bestellmenge.
Setze `lieferbar` auf `True`, wenn der Artikel aktiv ist und sein Bestand
mindestens der Bestellmenge entspricht; andernfalls auf `False`.
Gib das Ergebnisobjekt zurück. Verändere die Eingabeobjekte nicht.

Beispiel:

```python
artikel = Artikel("Bleistift", 20, True)
bestellung = Bestellung("Mia", 5)
ergebnis = bestellung_pruefen(artikel, bestellung)
print(ergebnis)
```

Erwartete Ausgabe:

```text
Bestellergebnis(kunde='Mia', artikel='Bleistift', menge=5, lieferbar=True)
```

## Dateien

- `answer.py` enthält die Dataclasses, die Musterlösung und eine Demonstration.
- `test_answer.py` vergleicht die Rückgabewerte mit `correct()`.

## Voraussetzungen

Python 3.7 oder neuer, nur Standardbibliothek. Kenntnisse zu Funktionen,
Type Hints und booleschen Ausdrücken. Der Bestand ist eine
nichtnegative ganze Zahl, die Bestellmenge eine positive ganze Zahl.
Gültige Eingaben werden vorausgesetzt; Eingabeprüfungen sind nicht Teil der Aufgabe.

## Ausführen und testen

Vom Repository-Hauptordner:

```bash
python examples/05_dataclasses/order_dataclasses/answer.py
python -m unittest discover -s examples/05_dataclasses/order_dataclasses -p "test_*.py"
```

Alternativ im Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

## Hinweise für Lehrkräfte

Mit `artikel.bestand` wird auf das Feld `bestand` des Artikelobjekts zugegriffen.
Die Dataclass benennt die Felder an einer zentralen Stelle. Beim Erzeugen eines
Objekts werden die Werte diesen Feldern zugeordnet.

`@dataclass` erzeugt automatisch den Konstruktor, eine lesbare Darstellung und
einen Vergleich anhand der Felder. Deshalb können die Tests Ergebnisobjekte
direkt mit `assertEqual()` vergleichen. Die Typangaben dokumentieren die Felder;
sie erzwingen keine Typprüfung zur Laufzeit.
Siehe auch die [Python-Dokumentation zu Dataclasses](https://docs.python.org/3/library/dataclasses.html).

Die Tests prüfen ausschließlich Rückgabewerte mit anderen Daten als in der
Demonstration. Ob die Eingaben unverändert bleiben, kann beim Besprechen des
Codes geprüft werden. Eigene Methoden, Vererbung und verschachtelte Daten
sind für diese Aufgabe nicht erforderlich.
