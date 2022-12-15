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
    my_list = []
    for i in ints:
        if i == ints[0]:
            my_list.append(i ** 2)
            print("i0", i ** 2)
        elif i in ints[1:]:
            my_list.append(i ** 2 - (((i-1) ** 2)- (i -1)))
            print("i-1) ** 2", ((i-1) **2))
    print(my_list)
