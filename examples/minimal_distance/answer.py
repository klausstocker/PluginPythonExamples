"""Find the shortest Euclidean distance between two point entries."""

import math
from typing import Optional


def minimalDistance(points: list[tuple[float, float]]) -> Optional[float]:
    """Return the smallest pairwise distance, or None if no pair exists."""
    if len(points) < 2:
        return None

    min_dist = math.inf
    for first_index in range(len(points) - 1):
        first_point = points[first_index]
        # Later indices avoid self-comparisons and checking each pair twice.
        for second_index in range(first_index + 1, len(points)):
            second_point = points[second_index]
            distance = math.hypot(
                second_point[0] - first_point[0],
                second_point[1] - first_point[1],
            )
            min_dist = min(min_dist, distance)

    return min_dist


if __name__ == "__main__":
    print(minimalDistance([(1.0, 2.0), (4.0, 6.0), (10.0, 2.0)]))  # 5.0
