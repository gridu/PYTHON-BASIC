import os
from random import randint
import csv
import time
import concurrent.futures
import multiprocessing as mp


OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def func1(array: list):
    with concurrent.futures.ProcessPoolExecutor(
            max_workers=10, mp_context=mp.get_context('fork')) as ex:
        ex.map(calculate_and_write_number, array)


def calculate_and_write_number(number: int):
    f_value = fib(number)
    filepath = os.path.join(OUTPUT_DIR, f'{number}.txt')
    with open(filepath, 'w') as f:
        f.write(str(f_value))


def func2(result_file: str):
    filenames = os.listdir(OUTPUT_DIR)
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        output_data = executor.map(read_file, filenames)

    with open(result_file, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(output_data)


def read_file(filename: str):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'r') as f:
        value = int(f.readline().strip())
    ordinal_number = int(filename.strip('.txt'))
    return [ordinal_number, value]


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
