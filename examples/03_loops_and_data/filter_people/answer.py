"""Zwei Filter fuer eine Liste von (Name, Alter)-Tupeln."""


def print_names_under_ten(people: list[tuple[str, int]]) -> None:
    """Gib die Namen aller Personen unter zehn Jahren aus."""
    for name, age in people:
        if age < 10:
            print(name)


def print_names_long_or_even_age(people: list[tuple[str, int]]) -> None:
    """Gib Namen mit mehr als fuenf Buchstaben oder geradem Alter aus."""
    for name, age in people:
        if len(name) > 5 or age % 2 == 0:
            print(name)


if __name__ == "__main__":
    people = [("Anna", 8), ("Benjamin", 11), ("Clara", 10), ("David", 9)]
    print_names_under_ten(people)
    print_names_long_or_even_age(people)
