# Robot movement in 2D

## Learning goal

Use NumPy vectors to calculate a position from velocity and elapsed time.
Then combine a loop over movement instructions with angle conversion and
trigonometry to calculate the final position of a route.

This exercise builds on **Position from velocity**, **Velocity vectors**, and
**Length and unit vectors** in the robotics script. The second part combines
these ideas with the sine, cosine, and degree conversion used in its 2D rotation
section.

## Task 1: One movement

Implement `end_position(start_point, velocity, delta_t)`.

- `start_point`: a NumPy array `[x, y]` with shape `(2,)`, in metres.
- `velocity`: a NumPy array `[vx, vy]` with shape `(2,)`, in metres per second.
- `delta_t`: the duration of the movement in seconds (delta T).

Return the end position as a NumPy array with shape `(2,)`. Use:

```text
end position = start point + velocity * delta_t
```

The velocity remains constant throughout this movement. Its components may be
negative. For example, starting at `[1, 2]` with velocity `[0.5, -1]` for
4 seconds gives the end position `[3, -2]`.

## Task 2: A sequence of movements

Implement `end_position_after_movements(start_point, movements)`.

`start_point` has the same meaning as in Task 1. `movements` is a list of tuples:

```python
(angle_degrees, speed, delta_t)
```

Here `speed` is a scalar in metres per second, rather than a velocity vector.
Each tuple describes one movement with constant speed and direction.

Angles describe **absolute directions in the same fixed coordinate system**,
not turns relative to the previous movement:

| Angle | Direction |
| --- | --- |
| 0 degrees | Positive x |
| 90 degrees | Positive y |
| 180 degrees | Negative x |
| 270 degrees or -90 degrees | Negative y |

Positive angles run counterclockwise. Convert each angle to radians using
`np.deg2rad`, then calculate the velocity components:

```text
vx = speed * cos(angle_radians)
vy = speed * sin(angle_radians)
```

Create the velocity vector with `np.array`. Use your function from Task 1 to
update the position for each movement. Return only the final position as a
NumPy array with shape `(2,)`.

For example:

```python
start_point = np.array([1.0, 2.0])
movements = [(0.0, 2.0, 3.0), (90.0, 1.0, 2.0)]
```

The first movement ends at `[7, 2]`; the second ends at `[7, 4]`.
An empty movement list returns a copy of the start point.

## Assumptions and requirements

- Inputs contain finite numbers. Points and velocity vectors are NumPy arrays
  with shape `(2,)`; speeds and durations are nonnegative.
- Zero speed or zero duration produces no displacement. Negative angles and
  angles larger than 360 degrees are allowed.
- Neither function changes its input arrays or the movement list. Return a new
  array, including when there are no movements.
- Direction and speed may change instantly between movements. Acceleration,
  obstacles, and input validation are outside the scope of this exercise.

Python 3 and NumPy are required. NumPy is already included in the repository's
`requirements.txt`. Students should know functions, `return`, lists, tuples,
and `for` loops before starting Task 2.

## Files

- `answer.py`: reference solutions and demonstrations for both tasks.
- `test_answer.py`: `unittest` checks using data different from the demonstrations.

## Run and test

From the repository root:

```bash
python -m pip install -r requirements.txt
python examples/robot_movement_2d/answer.py
python -m unittest discover -s examples/robot_movement_2d -p "test_*.py"
```

Alternatively, from this example folder:

```bash
python -m unittest test_answer.py
```

## Notes for teachers

Start with Task 1, then ask students to sketch a route before implementing
Task 2. Include a route whose second angle is also nonzero to distinguish
absolute directions from relative turns.

The tests cover fractional durations, diagonal and axis-aligned movements,
closed routes, stationary movements, empty routes, and unchanged inputs.
They compare coordinates with a tolerance because trigonometric calculations
can produce tiny rounding errors instead of exact zeros. The reuse of Task 1
in Task 2 can be checked by reading the solution.
