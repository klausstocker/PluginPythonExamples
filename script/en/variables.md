# Variables

## Learning objectives

After completing this chapter, you should be able to:

- explain what a variable is and why programs use variables,
- assign and reassign values to variables,
- choose valid and meaningful variable names,
- identify the basic data types `int`, `float`, `str`, and `bool`,
- inspect the type of a value with `type()`,
- use multiple assignment and swap values,
- distinguish variables from constants by naming convention.

## What is a variable?

Programs work with data: a temperature, a voltage, a name, a counter, or the state of a machine. A **variable** gives such a value a name so that we can use it later in the program.

In Python, a variable is created when a value is assigned to a name:

```python
temperature = 21.5
```

Here, `temperature` is the variable name and `21.5` is its current value. The assignment operator `=` connects the name with the value.

> **Important:** In programming, `=` means **assignment**. It does not mean "is equal to" in the mathematical sense.

Python is **dynamically typed**. You do not have to declare the type of a variable before using it. Python determines the type from the assigned value.

```python
name = "Alice"
age = 16
temperature = 21.5
motor_running = True
```

These variables contain different kinds of data, but no type declaration was necessary.

## Basic data types

For now, we will use four important built-in data types:

| Type | Meaning | Example |
| --- | --- | --- |
| `int` | integer number | `17`, `-5`, `1000` |
| `float` | floating-point number | `3.14`, `-0.5`, `230.0` |
| `str` | text (string) | `"Python"`, `"HTL"` |
| `bool` | logical value | `True`, `False` |

Example:

```python
student_count = 28
voltage = 12.5
school = "HTL Hollabrunn"
switch_on = True
```

The function `type()` can be used to inspect a value's type:

```python
print(type(student_count))
print(type(voltage))
print(type(school))
print(type(switch_on))
```

The output is:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

More complex types such as lists and dictionaries will be introduced separately later.

## Variable names

A variable name should tell the reader what the stored value means. Compare:

```python
x = 23.4
```

with:

```python
room_temperature = 23.4
```

Both programs are valid, but the second version is much easier to understand.

Python variable names:

- may contain letters, digits, and underscores (`_`),
- must not start with a digit,
- are case-sensitive,
- must not be Python keywords such as `for`, `if`, or `while`.

Valid names:

```python
student_count = 25
room_temperature = 21.5
sensor1 = 3.3
_internal_value = 10
```

Invalid names:

```python
# 2nd_sensor = 5       # starts with a digit
# room-temperature = 21.5  # '-' is not allowed in a name
# for = 10             # 'for' is a Python keyword
```

Python commonly uses **snake_case** for variable names consisting of several words:

```python
maximum_temperature = 80
motor_speed = 1500
student_first_name = "Anna"
```

> **Tip:** Prefer descriptive names. Very short names such as `x`, `y`, and `i` are useful in some mathematical or loop contexts, but should not replace meaningful names without a reason.

## Assignment and reassignment

A variable can receive a new value later in the program. This is called **reassignment**.

```python
counter = 1
print(counter)

counter = 2
print(counter)
```

Output:

```text
1
2
```

The new assignment replaces the previous value associated with the name.

A variable may even be reassigned to a value of another type:

```python
value = 10
value = "ten"
```

Python allows this because it is dynamically typed. However, changing the meaning and type of a variable without a good reason can make programs difficult to understand.

## Multiple assignment

Python can assign several variables in one statement:

```python
x, y, z = 1, 2, 3
```

This is equivalent to assigning the three values individually.

The same feature makes it easy to swap two values:

```python
a = 5
b = 10

a, b = b, a

print(a, b)
```

Output:

```text
10 5
```

No temporary variable is required.

The same value can also be assigned to several variables:

```python
red = green = blue = 0
```

## Variables in calculations

Variables become useful when they are combined in expressions.

```python
voltage = 12.0
current = 2.5
power = voltage * current

print(power)
```

Output:

```text
30.0
```

This is easier to understand than writing only:

```python
print(12.0 * 2.5)
```

Meaningful variable names document what the calculation represents.

## Constants by convention

Python does not prevent a variable from being changed. If a value is intended to remain constant, Python programmers conventionally write its name in uppercase letters:

```python
MAX_SPEED = 100
SUPPLY_VOLTAGE = 24.0
PI = 3.14159
```

This does not technically prevent reassignment. The uppercase name tells other programmers: **this value should normally not be changed**.

## Common mistakes

### Using a variable before assigning it

```python
print(temperature)
```

If `temperature` has not been assigned before this line, Python raises a `NameError`.

### Misspelling a variable name

```python
temperature = 22.5
print(temprature)
```

`temperature` and `temprature` are different names.

### Uppercase and lowercase letters

```python
speed = 100
Speed = 200
```

These are two different variables because Python names are case-sensitive.

### Confusing assignment and comparison

```python
x = 5
```

assigns the value `5` to `x`. The comparison operator `==` will be introduced with conditions.

## Worked example — Electrical power

We want to calculate electrical power from voltage and current.

```python
voltage = 24.0
current = 1.5
power = voltage * current

print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Power:", power, "W")
```

Output:

```text
Voltage: 24.0 V
Current: 1.5 A
Power: 36.0 W
```

Three variables represent three physical quantities. If the voltage or current changes, only the corresponding assignment has to be changed; the formula remains the same.

## Summary

At this point, you should know that:

- a variable is a name used to refer to a value,
- `=` assigns a value to a variable,
- Python determines data types dynamically,
- common basic types are `int`, `float`, `str`, and `bool`,
- `type()` reports the type of a value,
- variable names should be valid, descriptive, and normally use `snake_case`,
- variables can be reassigned,
- Python supports multiple assignment and direct swapping of values,
- uppercase names are conventionally used for constants.

## Related examples

Practical exercises for this chapter are stored in the repository's `examples/` directory and will be linked here as they are added.
