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
    final_lst = [num**2 - (ints[ind-1]**2 - ints[ind-1]) if ind != 0 else num**2 for ind, num in enumerate(ints)]
    return final_lst