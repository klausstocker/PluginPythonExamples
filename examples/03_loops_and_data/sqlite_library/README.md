# Bibliotheksverwaltung mit SQLite

## Lernziel

Die Lernenden verstehen eine n:m-Beziehung, verbinden Tabellen mit `JOIN`
und führen eine parametrisierte SQL-Abfrage in Python aus. Mit `fetchall()`
übernehmen sie das Ergebnis als Liste von Tupeln.

## Datenmodell

| Tabelle | Spalten | Bedeutung |
| --- | --- | --- |
| `books` | `id`, `title` | Bücher |
| `customers` | `id`, `name` | Kunden |
| `lends` | `id`, `book_id`, `customer_id`, `lend_date` | Ausleihvorgänge |

Ein Kunde kann mehrere Bücher ausleihen. Ein Buch kann im Laufe der Zeit von
mehreren Kunden ausgeliehen werden. Die Tabelle `lends` verbindet deshalb
`books` und `customers` zu einer **n:m-Beziehung**. Jede Ausleihe hat eine eigene
ID; auch wiederholte Ausleihen desselben Buchs durch denselben Kunden sind möglich.
`book_id` und `customer_id` sind Fremdschlüssel auf die jeweiligen IDs.

## Aufgabe

Implementiere `get_lends(connection, book_id)`. Schreibe eine SQL-Abfrage, die
ermittelt, **wer ein bestimmtes Buch wann ausgeliehen hat**.

- Wähle das Buch anhand seiner ID aus, nicht anhand seines Titels.
- Verbinde die Tabellen über ihre IDs.
- Gib eine Liste von Tupeln `(kundenname, ausleihdatum)` zurück.
- Sortiere nach Ausleihdatum aufsteigend, bei gleichem Datum nach Ausleih-ID.
- Behalte jede Ausleihe bei, auch wenn Name und Datum mehrfach vorkommen.
- Wenn keine Ausleihen vorliegen, gib `[]` zurück.
- Verwende für die Buch-ID einen `?`-Platzhalter und übergib `(book_id,)`
  als Parameter an `connection.execute`.

Für die Beispieldaten in `answer.py` ergibt `get_lends(connection, 1)`:

```python
[("Anna", "2026-09-01"), ("Ben", "2026-09-15"), ("Anna", "2026-10-01")]
```

Die Funktion gibt das Ergebnis zurück. Das Demonstrationsprogramm zeigt es mit
`print` an. Für eine reine Datumsliste kann anschließend verwendet werden:

```python
dates = [lend_date for name, lend_date in get_lends(connection, 1)]
```

## Dateien

- `answer.py`: Datenbankschema, Referenzabfrage und kleine Demonstration.
- `test_answer.py`: Tests mit anderen Daten, wiederholten Ausleihen,
  gleichen Namen und Titeln sowie Büchern ohne Ausleihe.
- `Frage_SQLite_Bibliotheksverwaltung.lto`: Letto-Import mit Aufgabenstellung,
  Startercode (ohne fertige Abfrage) und eingebetteten Validierungstests.
- `build_lto.py`: Erstellt den Import erneut aus Referenzlösung und Tests;
  verwendet `Frage_Funktion_aus_Wahrheitstabelle.lto` im Repository als Vorlage.

## Import in Letto

Importiere `Frage_SQLite_Bibliotheksverwaltung.lto` in Letto. Die Aufgabe verwendet
das Python-Plugin wie die mitgelieferten Exportvorlagen. Datenbank und Daten werden
im Startercode erstellt; zusätzliche Dateien sind nicht erforderlich. Die Tests
erstellen ihr eigenes Schema und prüfen die Funktion `get_lends`.

Die IDs der Vorlage sind auf `0` gesetzt, damit die neue Aufgabe keine bestehenden
Datenbank-IDs übernimmt. XML, Plugin-JSON und die eingebetteten Tests wurden lokal
geprüft; der tatsächliche Import in Letto wurde nicht durchgeführt.

Nach Änderungen an der Referenzlösung oder den Tests aus dem Repository-Stamm:

```bash
python examples/03_loops_and_data/sqlite_library/build_lto.py
```

## Ausführen und testen

Voraussetzung: Python 3.9 oder neuer mit dem Standardbibliotheksmodul `sqlite3`.
Keine zusätzlichen Pakete und kein Datenbankserver erforderlich. Die Datenbank
liegt im Arbeitsspeicher und wird beim Beenden verworfen.

Aus dem Beispielordner:

```bash
python answer.py
python -m unittest test_answer.py
```

Aus dem Repository-Stammverzeichnis:

```bash
python -m unittest discover -s examples/03_loops_and_data/sqlite_library -p "test_*.py"
```

## Hinweise für Lehrkräfte

Gib das Schema und die Beispieldaten vor und ersetze für die Lernenden den
Funktionsrumpf von `get_lends` durch `pass`. Die Aufgabe konzentriert sich auf
`SELECT`, `JOIN`, `WHERE` und `ORDER BY`.

Datumswerte werden als Text im Format `YYYY-MM-DD` gespeichert; dadurch liefert
die Textsortierung eine chronologische Reihenfolge. Das Modell zeigt eine
Ausleihhistorie und verwaltet weder Rückgaben noch einzelne Buchexemplare.
