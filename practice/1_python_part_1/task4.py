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
    if not ints:
        return []

    result = [ints[0]]  # Initialize the result list with the first element

    for i in range(1, len(ints)):
        original_value = ints[i]
        previous_result = result[i - 1]
        power = original_value ** 2
        difference = previous_result - power
        result.append(difference)

    return result