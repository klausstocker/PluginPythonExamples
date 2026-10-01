# 1. Variables and calculations

Practice storing values, using meaningful variable names, and translating
technical formulas into Python expressions.

## Recommended order

1. [Calculate a sum](calculate_sum/README.md): add values and print a result.
2. [Electrical power](electrical_power/README.md): calculate power from voltage and current.
3. [Temperature conversion](temperature_conversion/README.md): apply a conversion formula.
4. [Motor energy](motor_energy/README.md): combine several calculation steps.

## Extension exercises

- [Robot movement in 2D](robot_movement_2d/README.md): calculate positions using vectors; the route task also uses loops.
- [Vector angle in 3D](vector_angle_3d/README.md): use dot products and vector lengths.

These extensions require NumPy and additional mathematical background. See each
example's prerequisites before assigning it.

## Run tests

From the repository root, for example:

```bash
python -m unittest discover -s examples/01_variables_and_calculations/electrical_power -p "test_*.py"
```

Each example README gives its task and test command. Run all chapters with
`python -m unittest test_all_examples.py`.

Next: [Logic and conditions](../02_logic_and_conditions/README.md).
