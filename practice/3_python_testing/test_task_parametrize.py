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


def fibonacci_1(n):
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def fibonacci_2(n):
    fibo = [0, 1]
    for i in range(1, n + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo[n]


values = list(range(20))


@pytest.fixture
def correct():
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]


@pytest.mark.parametrize('n', values)
def test_fibbonaci_1(n, correct):
    assert correct[n] == fibonacci_1(n)


@pytest.mark.parametrize('n', values)
def test_fibbonaci_2(n, correct):
    assert correct[n] == fibonacci_1(2)
