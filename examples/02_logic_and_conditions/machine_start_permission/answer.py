"""Startfreigabe einer simulierten Anlage: Variablen und Ausdrücke ohne eigene Funktionen."""

tuer_geschlossen = True
stoppsignal_aktiv = False
taster_links = True
taster_rechts = False

# Auswertung
startwunsch = taster_links or taster_rechts
startfreigabe = tuer_geschlossen and (not stoppsignal_aktiv) and startwunsch
print(startfreigabe)
