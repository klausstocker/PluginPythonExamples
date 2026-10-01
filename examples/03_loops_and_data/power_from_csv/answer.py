"""Read the twelfth measurement and print its instantaneous power in watts."""


def main() -> None:
    with open("measurements.csv", "r", encoding="utf-8") as measurement_file:
        rows = measurement_file.readlines()

    # File rows count from 1; Python list indices count from 0.
    voltage_text, current_text = rows[11].strip().split(";")
    voltage = float(voltage_text)
    current = float(current_text)
    power = voltage * current
    print(power)


if __name__ == "__main__":
    main()
