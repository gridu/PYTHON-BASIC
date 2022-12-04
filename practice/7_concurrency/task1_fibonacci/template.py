import os
import queue
import threading
from random import randint
import multiprocessing as mp
from queue import Queue

OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def create_queue(array: list) -> Queue:
    q = Queue()
    for item in array:
        q.put(item)
    return q


def func1(array: list):
    def write_to_files():
        while True:
            try:
                number, result = q.get(block=False)
            except queue.Empty:
                return
            with open(OUTPUT_DIR + '/' + str(number) + '.txt', 'w') as f:
                f.write(str(result))
            q.task_done()

    with mp.Pool() as pool:
        results = pool.map(fib, array)
    pairs = [(array[i], results[i]) for i in range(len(array))]
    q = create_queue(pairs)
    threads = [threading.Thread(target=write_to_files) for _ in range(min(os.cpu_count() + 4, 32))]
    [t.start() for t in threads]
    q.join()


def func2(result_file: str):
    q = create_queue(os.listdir(OUTPUT_DIR))
    results = []

    def read_from_files():
        while True:
            try:
                path = q.get(block=False)
            except queue.Empty:
                return
            with open(OUTPUT_DIR + '/' + path, 'r') as f:
                results.append((path.split('.')[0], f.read()))
            q.task_done()

    def write_to_csv():
        with open(result_file, 'w') as f:
            for data in results:
                number, result = data
                f.write(number + ', ' + result)
                f.write('\n')
    # How to write it using csv module?
    threads = [threading.Thread(target=read_from_files) for _ in range(min(os.cpu_count() + 4, 32))]
    [t.start() for t in threads]
    q.join()
    write_to_csv()


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
