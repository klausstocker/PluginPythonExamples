"""Erstelle den LETTO-Import mit Startercode und eingebetteten Tests."""

import json
from pathlib import Path
from xml.dom import minidom


EXAMPLE_DIRECTORY = Path(__file__).resolve().parent
TEMPLATE = (
    EXAMPLE_DIRECTORY.parents[1]
    / "03_loops_and_data/sqlite_library/Frage_SQLite_Bibliotheksverwaltung.lto"
)


def set_text(document, element, value, cdata=False):
    for child in list(element.childNodes):
        element.removeChild(child)
    node = document.createCDATASection(value) if cdata else document.createTextNode(value)
    element.appendChild(node)


def build_export():
    document = minidom.parse(str(TEMPLATE))
    question = document.getElementsByTagName("question")[0]
    for dataset in list(question.getElementsByTagName("dataset")):
        question.removeChild(dataset)
    for element in document.getElementsByTagName("id"):
        set_text(document, element, "0")
    set_text(document, question.getElementsByTagName("idUser")[0], "0")
    for element in question.getElementsByTagName("text"):
        if element.hasAttribute("id"):
            element.setAttribute("id", "0")
    set_text(document, question.getElementsByTagName("name")[0],
             "Datum des Ostersonntags berechnen", cdata=True)
    for tag in ("maxima", "maximaAngabe"):
        set_text(document, question.getElementsByTagName(tag)[0], "")

    starter = '''from datetime import date, timedelta


def ostersonntag(jahr: int) -> date:
    """Gib den westlichen Ostersonntag für das angegebene Jahr zurück."""
    pass
'''
    validation = (EXAMPLE_DIRECTORY / "test_answer.py").read_text(encoding="utf-8")
    validation = validation.split('if __name__ == "__main__":')[0]
    plugin = question.getElementsByTagName("plugins")[0]
    prefix, suffix = '[PI Plugin1 Python "', '"]'
    config = json.loads(plugin.firstChild.data[len(prefix):-len(suffix)])
    config.update(datasetVariables=[], validation=validation, indication=starter,
                  files={}, linterWeight=0.0)
    set_text(document, plugin,
             prefix + json.dumps(config, ensure_ascii=False) + suffix, cdata=True)

    html = '''<h3>Datum des Ostersonntags berechnen</h3>
<p>Implementiere <code>ostersonntag(jahr: int) -&gt; date</code>.
Die Funktion gibt das Datum des westlichen Ostersonntags im gregorianischen
Kalender als <code>datetime.date</code> zurück.</p>
<ul><li>Unterstütze ganze Jahre von 1583 bis 4099 einschließlich.</li>
<li>Löse für Jahre außerhalb dieses Bereichs einen <code>ValueError</code> aus.</li>
<li>Eine Prüfung des Datentyps ist nicht erforderlich.</li></ul>
<p>Beispiel: <code>ostersonntag(2026)</code> liefert <code>date(2026, 4, 5)</code>.</p>
<p>Verwende folgende gregorianische Osterformel von Gauß.
<code>//</code> ist ganzzahlige Division, <code>%</code> liefert den Rest:</p>
<pre>a = jahr % 19
b = jahr % 4
c = jahr % 7
k = jahr // 100
p = (13 + 8 * k) // 25
q = k // 4
M = (15 - p + k - q) % 30
N = (4 + k - q) % 7
d = (19 * a + M) % 30
e = (2 * b + 4 * c + 6 * d + N) % 7</pre>
<p>Korrigiere anschließend die Sonderfälle: Falls <code>d == 29</code> und
<code>e == 6</code>, ziehe 7 von <code>e</code> ab. Dasselbe gilt, falls
<code>d == 28</code>, <code>e == 6</code> und <code>a &gt; 10</code>.</p>
<p>Addiere dann <code>d + e</code> Tage zum 22. März des angegebenen Jahres.
Verwende dazu <code>date</code> und <code>timedelta</code> aus der Standardbibliothek.
Wähle für deine Umsetzung erklärende Variablennamen.</p>
<p>Die Tests prüfen den Rückgabewert deiner Funktion; eine Bildschirmausgabe ist
nicht erforderlich. Zusätzliche Dateien oder Pakete werden nicht benötigt.</p>
<p>[Q0]</p>
'''
    question_text = next(element for element in question.getElementsByTagName("text")
                         if element.getAttribute("art") == "Questiontext")
    set_text(document, question_text.getElementsByTagName("inhalt")[0], html, cdata=True)
    output = EXAMPLE_DIRECTORY / "Frage_Ostersonntag.lto"
    output.write_bytes(document.toxml(encoding="UTF-8"))
    return output


if __name__ == "__main__":
    print(build_export())
