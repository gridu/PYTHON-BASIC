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
    with open(filename) as opened_file:
        min_num = int(opened_file.readline())
        max_num = min_num
        for line in opened_file:
            if int(line) < min_num:
                min_num = int(line)
            elif int(line) > max_num:
                max_num = int(line)
    final_tuple = (min_num, max_num)
    return final_tuple
