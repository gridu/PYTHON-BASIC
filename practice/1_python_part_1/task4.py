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
    #out = [ints[0]**2]
    #for i, x in enumerate(ints[1:]):
    #    prev = ints[i]
    #    out.append(x**2 - (prev**2 - prev))
    # return out

    power = [x ** 2 for x in ints]
    difference = [x - (power[i] - ints[i]) for i, x in enumerate(power[1:])]
    return [power[0]] + difference
