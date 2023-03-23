import os
from random import randint
import sys

OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'

# Overwrite the maximum limit for integer string conversion 
sys.set_int_max_str_digits(9999999)

def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def func1(array: list):
    for el in array:
        with open(f"file {el}", "w", encoding="utf-8") as el_file:
            el_file.write(str(fib(el)))

def func2(result_file: str):
    pass


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
