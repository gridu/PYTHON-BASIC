"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""

from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    powered_ints = [el**2 for el in ints]
    for i in range(len(powered_ints) - 1, 0, -1):
        powered_ints[i] = powered_ints[i] - (powered_ints[i - 1] - ints[i - 1])
    return powered_ints


if __name__ == "__main__":
    print(calculate_power_with_difference([1, 2, 3]))
