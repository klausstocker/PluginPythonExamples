# Variablen

## Lernziele

Nach diesem Kapitel kannst du:

- erklären, was eine Variable ist und warum Programme Variablen verwenden,
- Variablen Werte zuweisen und diese später verändern,
- gültige und aussagekräftige Variablennamen wählen,
- die grundlegenden Datentypen `int`, `float`, `str` und `bool` unterscheiden,
- mit `type()` den Datentyp eines Wertes bestimmen,
- Mehrfachzuweisungen verwenden und Werte vertauschen,
- Variablen und Konstanten anhand der Namenskonvention unterscheiden.

## Was ist eine Variable?

Programme arbeiten mit Daten: einer Temperatur, einer Spannung, einem Namen, einem Zähler oder dem Zustand einer Maschine. Eine **Variable** gibt einem solchen Wert einen Namen, damit wir ihn später im Programm verwenden können.

In Python entsteht eine Variable, wenn einem Namen ein Wert zugewiesen wird:

```python
temperature = 21.5
```

Dabei ist `temperature` der Variablenname und `21.5` der aktuelle Wert. Der Zuweisungsoperator `=` verbindet den Namen mit dem Wert.

> **Wichtig:** Beim Programmieren bedeutet `=` **Zuweisung**. Es bedeutet nicht „ist gleich“ im mathematischen Sinn.

Python ist **dynamisch typisiert**. Der Datentyp einer Variable muss vor ihrer Verwendung nicht deklariert werden. Python bestimmt den Typ anhand des zugewiesenen Wertes.

```python
name = "Alice"
age = 16
temperature = 21.5
motor_running = True
```

Diese Variablen enthalten unterschiedliche Arten von Daten, ohne dass vorher ein Datentyp angegeben werden musste.

## Grundlegende Datentypen

Vorerst verwenden wir vier wichtige eingebaute Datentypen:

| Typ | Bedeutung | Beispiel |
| --- | --- | --- |
| `int` | ganze Zahl | `17`, `-5`, `1000` |
| `float` | Gleitkommazahl | `3.14`, `-0.5`, `230.0` |
| `str` | Text (String) | `"Python"`, `"HTL"` |
| `bool` | logischer Wert | `True`, `False` |

Beispiel:

```python
student_count = 28
voltage = 12.5
school = "HTL Hollabrunn"
switch_on = True
```

Mit der Funktion `type()` kann der Datentyp überprüft werden:

```python
print(type(student_count))
print(type(voltage))
print(type(school))
print(type(switch_on))
```

Ausgabe:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Komplexere Typen wie Listen und Dictionaries werden später in eigenen Kapiteln behandelt.

## Variablennamen

Ein Variablenname sollte erkennen lassen, welche Bedeutung der gespeicherte Wert hat. Vergleiche:

```python
x = 23.4
```

mit:

```python
room_temperature = 23.4
```

Beide Varianten sind gültig, die zweite ist jedoch wesentlich leichter zu verstehen.

Für Variablennamen gelten in Python folgende Regeln:

- Sie dürfen Buchstaben, Ziffern und Unterstriche (`_`) enthalten.
- Sie dürfen nicht mit einer Ziffer beginnen.
- Groß- und Kleinschreibung wird unterschieden.
- Python-Schlüsselwörter wie `for`, `if` oder `while` dürfen nicht verwendet werden.

Gültige Namen:

```python
student_count = 25
room_temperature = 21.5
sensor1 = 3.3
_internal_value = 10
```

Ungültige Namen:

```python
# 2nd_sensor = 5       # beginnt mit einer Ziffer
# room-temperature = 21.5  # '-' ist im Namen nicht erlaubt
# for = 10             # 'for' ist ein Python-Schlüsselwort
```

Für Variablennamen aus mehreren Wörtern wird in Python üblicherweise **snake_case** verwendet:

```python
maximum_temperature = 80
motor_speed = 1500
student_first_name = "Anna"
```

> **Hinweis:** Verwende möglichst aussagekräftige Namen. Sehr kurze Namen wie `x`, `y` und `i` sind in bestimmten mathematischen Zusammenhängen oder bei Schleifen sinnvoll, sollten aber nicht ohne Grund aussagekräftige Namen ersetzen.

## Zuweisung und Neuzuweisung

Eine Variable kann später im Programm einen neuen Wert erhalten. Dies wird als **Neuzuweisung** bezeichnet.

```python
counter = 1
print(counter)

counter = 2
print(counter)
```

Ausgabe:

```text
1
2
```

Durch die neue Zuweisung wird der bisher mit dem Namen verbundene Wert ersetzt.

Eine Variable kann sogar einen Wert eines anderen Datentyps erhalten:

```python
value = 10
value = "ten"
```

Python erlaubt dies aufgrund der dynamischen Typisierung. Ohne guten Grund den Typ und die Bedeutung einer Variable zu verändern, kann ein Programm jedoch schwer verständlich machen.

## Mehrfachzuweisung

Python kann mehreren Variablen in einer Anweisung Werte zuweisen:

```python
x, y, z = 1, 2, 3
```

Dies entspricht drei einzelnen Zuweisungen.

Damit lassen sich auch zwei Werte besonders einfach vertauschen:

```python
a = 5
b = 10

a, b = b, a

print(a, b)
```

Ausgabe:

```text
10 5
```

Eine zusätzliche Hilfsvariable ist nicht notwendig.

Derselbe Wert kann auch mehreren Variablen zugewiesen werden:

```python
red = green = blue = 0
```

## Variablen in Berechnungen

Besonders nützlich werden Variablen, wenn sie in Ausdrücken und Berechnungen verwendet werden.

```python
voltage = 12.0
current = 2.5
power = voltage * current

print(power)
```

Ausgabe:

```text
30.0
```

Diese Schreibweise ist leichter verständlich als:

```python
print(12.0 * 2.5)
```

Aussagekräftige Variablennamen dokumentieren gleichzeitig, welche Bedeutung eine Berechnung hat.

## Konstanten als Konvention

Python verhindert nicht, dass eine Variable verändert wird. Soll ein Wert während des Programms konstant bleiben, wird sein Name in Python üblicherweise mit Großbuchstaben geschrieben:

```python
MAX_SPEED = 100
SUPPLY_VOLTAGE = 24.0
PI = 3.14159
```

Dadurch wird eine erneute Zuweisung technisch nicht verhindert. Der großgeschriebene Name signalisiert anderen Programmierenden: **Dieser Wert sollte normalerweise nicht verändert werden.**

## Häufige Fehler

### Variable vor der Zuweisung verwenden

```python
print(temperature)
```

Wurde `temperature` vorher noch kein Wert zugewiesen, erzeugt Python einen `NameError`.

### Variablennamen falsch schreiben

```python
temperature = 22.5
print(temprature)
```

`temperature` und `temprature` sind zwei unterschiedliche Namen.

### Groß- und Kleinschreibung

```python
speed = 100
Speed = 200
```

Da Python zwischen Groß- und Kleinschreibung unterscheidet, sind dies zwei verschiedene Variablen.

### Zuweisung und Vergleich verwechseln

```python
x = 5
```

weist `x` den Wert `5` zu. Der Vergleichsoperator `==` wird später gemeinsam mit Bedingungen behandelt.

## Durchgerechnetes Beispiel — Elektrische Leistung

Wir wollen die elektrische Leistung aus Spannung und Strom berechnen.

```python
voltage = 24.0
current = 1.5
power = voltage * current

print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Power:", power, "W")
```

Ausgabe:

```text
Voltage: 24.0 V
Current: 1.5 A
Power: 36.0 W
```

Drei Variablen repräsentieren drei physikalische Größen. Ändert sich die Spannung oder der Strom, muss nur die entsprechende Zuweisung geändert werden; die Formel bleibt unverändert.

## Zusammenfassung

Nach diesem Kapitel solltest du wissen:

- Eine Variable ist ein Name, der auf einen Wert verweist.
- Mit `=` wird einer Variable ein Wert zugewiesen.
- Python bestimmt Datentypen dynamisch.
- Wichtige grundlegende Datentypen sind `int`, `float`, `str` und `bool`.
- Mit `type()` kann der Datentyp eines Wertes bestimmt werden.
- Variablennamen sollten gültig und aussagekräftig sein und üblicherweise `snake_case` verwenden.
- Variablen können neue Werte erhalten.
- Python unterstützt Mehrfachzuweisungen und das direkte Vertauschen von Werten.
- Großgeschriebene Namen werden üblicherweise für Konstanten verwendet.

## Zugehörige Beispiele

Praktische Übungen zu diesem Kapitel werden im Verzeichnis `examples/` des Repositorys abgelegt und hier verlinkt, sobald sie hinzugefügt wurden.
