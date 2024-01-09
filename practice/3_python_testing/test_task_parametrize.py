"""
Write a parametrized test for two functions.
The functions are used to find a number by ordinal in the Fibonacci sequence.
One of them has a bug.

Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Task:
 1. Write a test with @pytest.mark.parametrize decorator.
 2. Find the buggy function and fix it.
"""


import pytest

def test_fibonacci_functions(fibonacci_function):
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21)
    ]

    for n, expected_result in test_cases:
        result = fibonacci_function(n)
        assert result == expected_result

@pytest.mark.parametrize("fibonacci_function", [fibonacci_1, fibonacci_2])
def test_fibonacci_1(n):

    result = fibonacci_1(n)
    assert result == fibonacci_2(n)

