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
import heapq

def get_min_max(filename: str) -> Tuple[int, int]:
    with open(filename, "r") as f:
        nums_lst=f.read().splitlines()
        heapq.heapify(nums_lst)
        sorted_nums_lst = [int(heapq.heappop(nums_lst)) for _ in range(len(nums_lst))]
    return (sorted_nums_lst[0], sorted_nums_lst[-1])