# 2. Logic and conditions

Practice comparing values, combining Boolean expressions, and choosing which
instructions to execute. Learners should already understand variables and
simple calculations.

## Recommended order

1. [Logical and](logical_and/README.md): require both conditions to be true.
2. [Logical or](logical_or/README.md): require at least one condition to be true.
3. [Logical not](logical_not/README.md): negate a Boolean expression.
4. [Temperature warning](if_temperature_warning/README.md): use a single `if` to change a default value.
5. [Fan control](if_else_fan_control/README.md): choose between two branches with `if/else`.
6. [Battery status](if_elif_battery_status/README.md): classify three ranges with `if/elif/else`.
7. [Radians to degrees](radians_to_degrees/README.md): combine angle conversion with quadrant assignment as an extension.

Discuss exact threshold values and predict which branch runs before testing.
The example READMEs describe the required function interfaces and prerequisites.

## Run tests

From the repository root, for example:

```bash
python -m unittest discover -s examples/02_logic_and_conditions/if_temperature_warning -p "test_*.py"
```

Each example README gives its task and test command. Run all chapters with
`python -m unittest test_all_examples.py`.

Previous: [Variables and calculations](../01_variables_and_calculations/README.md).
Next: [Loops and data](../03_loops_and_data/README.md).

## Boolean expressions before functions

These three examples use only variables and expressions in `answer.py`; learners
do not need to define functions or use branches or loops. Start here when following
the script, which introduces Boolean operators before functions.

- [Spannung im erlaubten Bereich](voltage_range/README.md): Vergleiche und `and` ohne eigene Funktionen verwenden.
- [Genau eine Betriebsart gewählt](exclusive_operating_mode/README.md): Bei booleschen Werten XOR mit `!=` ausdrücken und mit `or` vergleichen.
- [Startfreigabe einer simulierten Anlage](machine_start_permission/README.md): `and`, `or` und `not` mit klaren Klammern kombinieren.
