from concurrent.futures import ProcessPoolExecutor
import os
from random import randint
import sys


OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'
sys.set_int_max_str_digits(0) # the default limit of 4300 is too small for ~fib(100_000)


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def func1(array: list):
    array = list(set(array))
    def func(number) -> None:
        result = fib(number)
        with open(f'{OUTPUT_DIR}/{number}.txt', 'w') as file:
            file.write(str(result))
    with ProcessPoolExecutor() as executor:
        executor.map(func, array)


def func2(result_file: str = RESULT_FILE):
    filenames = os.listdir(OUTPUT_DIR)
    def func(filename: str) -> tuple[str, str]:
        with open(f'{OUTPUT_DIR}/{filename}') as file:
            value = file.read()
            return (filename[:-4], value)
    with ProcessPoolExecutor() as executor:
        data = executor.map(func, filenames)
        with open(result_file, 'x') as file:
            file.write('\n'.join([f'{d[0]},{d[1]}' for d in data]))


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
