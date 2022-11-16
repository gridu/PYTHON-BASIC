from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            numbers.append(int(line))
    return min(numbers), max(numbers)


if __name__ == '__main__':
    print(get_min_max('test.txt'))