"""Spannung im erlaubten Bereich: Variablen und Ausdrücke ohne eigene Funktionen."""

spannung = 230.0

# Auswertung
spannung_erlaubt = spannung >= 210.0 and spannung <= 250.0
print(spannung_erlaubt)
