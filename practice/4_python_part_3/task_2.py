"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math
import pytest
import sys


class OperationNotFoundException(Exception):
    pass


def math_calculate(function: str, *args):
    if len(args) in [1, 2]:
        try:
            return getattr(math, function)(*args)
        except AttributeError:
            raise OperationNotFoundException
    print('Number of arguments is not correct!')


"""
Write tests for math_calculate function
"""


def tests():
    assert math_calculate('comb', 4, 2) == 6
    assert math_calculate('fabs', -5) == 5
    assert math_calculate('factorial', 5) == 120
    assert math_calculate('gcd', 32, 16) == 16
    assert math_calculate('gcd', 129, 7) == 1
    with pytest.raises(OperationNotFoundException):
        math_calculate('aaa', 5)
        math_calculate('bbb', 333)

if __name__ == '__main__':
    tests()
