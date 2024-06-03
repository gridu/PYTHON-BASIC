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


GROUND_TRUTH = [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (11, 89),
    (12, 144)
]


def fibonacci_1(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b


def fibonacci_2(n):
    fibo = [0, 1]
    for _ in range(1, n+1):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[n]


@pytest.mark.parametrize('test_input,test_output', GROUND_TRUTH)
def test_fibonacci_1(test_input, test_output):
    assert fibonacci_1(test_input) == test_output


@pytest.mark.parametrize('test_input,test_output', GROUND_TRUTH)
def test_fibonacci_2(test_input, test_output):
    assert fibonacci_2(test_input) == test_output


if __name__ == '__main__':
    pytest.main([__file__])
