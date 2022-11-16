from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    return [i**2 - ((i-1)**2 - (i-1)) for i in ints]

if __name__ == '__main__':
    print(calculate_power_with_difference([1, 2, 3]))