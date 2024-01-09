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
    min_value = float('inf')  # Initialize min_value to positive infinity
    max_value = float('-inf')  # Initialize max_value to negative infinity
    
    with open(filename) as opened_file:
        for line in opened_file:
            value = int(line.strip())
            min_value = min(min_value, value)
            max_value = max(max_value, value)
    
    return min_value, max_value

