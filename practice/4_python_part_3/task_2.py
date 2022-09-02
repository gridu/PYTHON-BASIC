"""
Write function which executes custom operation from math module
for given arguments.
Restriction: math function could take 1 or 2 arguments
If given operation does not exist, raise OperationNotFoundException
Examples:
     >> math_calculate('log', 1024, 2)
     10.0
     >> math_calculate('ceil', 10.7)
     11
"""
import math
import pytest


class OperationNotFoundException(Exception):
    pass


def math_calculate(function: str, *args):
    try:
        func_call = getattr(math, function)
        try:
            a, b = args
            return func_call(a, b)
        except ValueError:
            a = float(args[0])
            return func_call(a)
    except AttributeError:
        raise OperationNotFoundException


"""
Write tests for math_calculate function
"""


def test_functions_one_arg():
    math_ceil = math_calculate('ceil', 8.000001)
    assert math_ceil == 9
    math_fabs = math_calculate('fabs', -23.45)
    assert math_fabs == 23.45
    math_frexp_mantissa, math_frexp_exponent = math_calculate('frexp', 0.125)
    assert (math_frexp_mantissa == 0.5 and math_frexp_exponent == -2)


def test_functions_two_args():
    math_log = math_calculate('log', 1024, 2)
    assert math_log == 10
    math_copy_sign = math_calculate('copysign', 11.1, -23456789)
    assert math_copy_sign == -11.1


def test_nonexistent_function():
    with pytest.raises(OperationNotFoundException):
        math_calculate('celi', 22.2)
    with pytest.raises(OperationNotFoundException):
        math_calculate('pepeLaugh', 1337, 6.9)
