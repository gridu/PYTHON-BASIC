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
integers = [ 1,5,3,2,6,7,10,333]
with open("file", "a") as file:
    for i in integers:
        file.write(str(i))
        file.write("\n")



def get_min_max(filename: str) -> Tuple[int, int]:
    with open(filename, "r") as f:
        min_value = int(f.readline())
        max_value = int(f.readline())
        for i in f:
            i = int(i)
            if int(i) > max_value:
                max_value = i 
            if int(i) < min_value:
                min_value = i
    return min_value, max_value
min,max = get_min_max("file")    
print("min: ",min," max: ", max)