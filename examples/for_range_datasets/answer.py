"""Reference solution for the for_range_datasets example."""


DATASETS = [
    (1, 5),
    (3, 7),
    (0, 4),
]


def collect_numbers_from_ranges(datasets):
    """Return all numbers produced by range(start, stop) for each dataset.

    Each dataset contains a start value and a stop value. The for loop visits
    every number from start up to, but not including, stop.
    """
    all_numbers = []

    for start, stop in datasets:
        for number in range(start, stop):
            all_numbers.append(number)

    return all_numbers


if __name__ == "__main__":
    print(collect_numbers_from_ranges(DATASETS))
