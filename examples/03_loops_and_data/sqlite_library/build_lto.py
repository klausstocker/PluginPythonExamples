"""Build a Letto import using the supplied truth-table export as a template."""

import ast
import json
from pathlib import Path
from xml.dom import minidom


EXAMPLE_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY_ROOT = EXAMPLE_DIRECTORY.parents[2]


def set_text(document, element, value, cdata=False):
    for child in list(element.childNodes):
        element.removeChild(child)
    node = document.createCDATASection(value) if cdata else document.createTextNode(value)
    element.appendChild(node)


def build_export():
    document = minidom.parse(str(REPOSITORY_ROOT / "Frage_Funktion_aus_Wahrheitstabelle.lto"))
    question = document.getElementsByTagName("question")[0]
    for dataset in list(question.getElementsByTagName("dataset")):
        question.removeChild(dataset)
    # New content must not retain the source question's database identities.
    for element in document.getElementsByTagName("id"):
        set_text(document, element, "0")
    set_text(document, question.getElementsByTagName("idUser")[0], "0")
    for element in question.getElementsByTagName("text"):
        if element.hasAttribute("id"):
            element.setAttribute("id", "0")
    set_text(document, question.getElementsByTagName("name")[0],
             "SQLite: Bibliotheksverwaltung (n:m)", cdata=True)
    for tag in ("maxima", "maximaAngabe"):
        set_text(document, question.getElementsByTagName(tag)[0], "")
    set_text(document, question.getElementsByTagName("responseFieldLines")[0], "25")

    source = (EXAMPLE_DIRECTORY / "answer.py").read_text(encoding="utf-8")
    function = next(node for node in ast.parse(source).body
                    if isinstance(node, ast.FunctionDef) and node.name == "get_lends")
    lines = source.splitlines(keepends=True)
    starter = "".join(lines[:function.body[0].lineno - 1])
    starter += '    """Ergaenze hier deine SQL-Abfrage."""\n    pass\n'
    starter += "".join(lines[function.end_lineno:])

    # Validation owns the schema so students only have to implement the query.
    schema_function = next(node for node in ast.parse(source).body
                           if isinstance(node, ast.FunctionDef) and node.name == "create_database")
    schema_source = "".join(lines[schema_function.lineno - 1:schema_function.end_lineno])
    validation = (EXAMPLE_DIRECTORY / "test_answer.py").read_text(encoding="utf-8")
    validation = validation.replace("import answer\n", "import answer\n\n\n" + schema_source + "\n")
    validation = validation.replace("answer.create_database()", "create_database()")
    validation = validation.split('if __name__ == "__main__":')[0]

    plugin_element = question.getElementsByTagName("plugins")[0]
    template_plugin = plugin_element.firstChild.data
    prefix = '[PI Plugin1 Python "'
    suffix = '"]'
    config = json.loads(template_plugin[len(prefix):-len(suffix)])
    config.update(datasetVariables=[], validation=validation, indication=starter,
                  files={}, linterWeight=0.0)
    set_text(document, plugin_element,
             prefix + json.dumps(config, ensure_ascii=False) + suffix, cdata=True)

    html = """<h3>Bibliotheksverwaltung mit SQLite</h3>
<p>Die vorgegebene Datenbank enthaelt drei Tabellen:</p>
<ul><li><code>books(id, title)</code>: Buecher</li>
<li><code>customers(id, name)</code>: Kunden</li>
<li><code>lends(id, book_id, customer_id, lend_date)</code>: Ausleihen</li></ul>
<p>Ein Kunde kann mehrere Buecher ausleihen; ein Buch kann im Laufe der Zeit
von mehreren Kunden ausgeliehen werden. <code>lends</code> bildet diese
n:m-Beziehung ab. Die beiden Fremdschluessel verweisen auf die jeweiligen IDs.</p>
<p>Implementiere <code>get_lends(connection, book_id)</code> mit einer SQL-Abfrage:
Wer hat das Buch mit dieser ID wann ausgeliehen?</p>
<ul><li>Gib eine Liste von Tupeln <code>(kundenname, ausleihdatum)</code> zurueck.</li>
<li>Verbinde die Tabellen mit JOIN und filtere nach der Buch-ID.</li>
<li>Verwende einen <code>?</code>-Platzhalter und <code>(book_id,)</code> als Parameter.</li>
<li>Sortiere nach Ausleihdatum aufsteigend, bei gleichem Datum nach Ausleih-ID.</li>
<li>Behalte wiederholte Ausleihen bei; ohne Treffer ist das Ergebnis <code>[]</code>.</li></ul>
<p>Die Daten im Startercode liefern fuer Buch 1:</p>
<pre>[("Anna", "2026-09-01"), ("Ben", "2026-09-15"), ("Anna", "2026-10-01")]</pre>
<p>Die Datumswerte sind Text im Format YYYY-MM-DD. Ergaenze nur
<code>get_lends</code>. Die Datenbank wird im Arbeitsspeicher erstellt.
Die Funktion gibt die Liste zurueck; das Demonstrationsprogramm gibt sie aus.</p>
<p>[Q0]</p>
"""
    question_text = next(element for element in question.getElementsByTagName("text")
                         if element.getAttribute("art") == "Questiontext")
    set_text(document, question_text.getElementsByTagName("inhalt")[0], html, cdata=True)
    output_path = EXAMPLE_DIRECTORY / "Frage_SQLite_Bibliotheksverwaltung.lto"
    output_path.write_bytes(document.toxml(encoding="UTF-8"))
    return output_path


if __name__ == "__main__":
    print(build_export())
