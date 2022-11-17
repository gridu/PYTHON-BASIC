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
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            numbers.append(int(line))
    return min(numbers), max(numbers)


if __name__ == '__main__':
    print(get_min_max('test.txt'))

