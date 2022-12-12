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
    end_list=[(ints[0]**2)]
    for i in range(1,len(ints)):
        end_list.append((ints[i]**2 - ((ints[i-1])**2 -ints[i-1])))
    return(end_list)

print(calculate_power_with_difference([1, 2, 4]))