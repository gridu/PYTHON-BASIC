"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]

"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    return [i**2 - ((i-1)**2 - (i-1)) for i in ints]