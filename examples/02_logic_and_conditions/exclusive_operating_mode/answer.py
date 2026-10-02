"""Genau eine Betriebsart gewählt: Variablen und Ausdrücke ohne eigene Funktionen."""

handbetrieb = True
automatikbetrieb = False

# Auswertung
mindestens_eine_betriebsart = handbetrieb or automatikbetrieb
genau_eine_betriebsart = handbetrieb != automatikbetrieb
print(mindestens_eine_betriebsart)
print(genau_eine_betriebsart)
