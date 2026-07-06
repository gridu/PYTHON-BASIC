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


class OperationNotFoundException(Exception):
    pass


def math_calculate(function: str, *args):
    math_dict = vars(math)
    if function in math_dict:
        desired_function = math_dict[function]
        result = desired_function(*args)
        return result
    else:
        raise OperationNotFoundException


print(math_calculate("ceil", 10.7))
"""
Write tests for math_calculate function
"""


def test_math_calculate_good_call():
    assert math_calculate("log", 1024, 2) == 10.0


def test_math_calculate_wrong_func_name():
    with pytest.raises(OperationNotFoundException):
        math_calculate("loga", 1024, 2)


def test_math_calculate_wrong_arguments():
    with pytest.raises(Exception):
        math_calculate("ceil", 1024, 3, 4, 14.4)
