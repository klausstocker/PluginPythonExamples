"""Reference solution for counting dial rotations that end at zero."""


def countPointingAt0(start: int, rotations: list[str]) -> int:
    """Count stops at zero on a dial numbered from 0 through 99."""
    if not 0 <= start <= 99:
        raise ValueError("start must be between 0 and 99")

    position = start
    zero_stops = 0

    for rotation in rotations:
        if not rotation:
            raise ValueError("rotation entries must be non-empty strings")

        direction = rotation[0]
        if direction not in {"L", "R"}:
            raise ValueError(f"invalid direction in rotation: {rotation}")

        distance_str = rotation[1:]
        if not distance_str.isdigit():
            raise ValueError(f"invalid distance in rotation: {rotation}")

        distance = int(distance_str)
        # Modulo keeps the position on the dial, even after several full turns.
        if direction == "L":
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100

        if position == 0:
            zero_stops += 1

    return zero_stops


if __name__ == "__main__":
    print(countPointingAt0(20, ["L20", "R15", "L15"]))  # 2
