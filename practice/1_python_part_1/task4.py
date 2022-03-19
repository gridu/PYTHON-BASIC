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
    previous = 0
    first = True
    result = []
    for i in ints:
        if first:
            a = i ** 2
            first = False
        else:
            a = i ** 2 - (previous - previous_i)
        previous = a
        previous_i = i
        result.append(a)

    return result

print(calculate_power_with_difference([1, 2, 3,4]))
