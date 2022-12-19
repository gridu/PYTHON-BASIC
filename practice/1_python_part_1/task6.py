"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    num_list = []
    with open(filename) as opened_file:
        for num in opened_file.read().split():
            num_list.append(float(num))
            mn = min(num_list)
            mx = max(num_list)
        print(mn, mx)
