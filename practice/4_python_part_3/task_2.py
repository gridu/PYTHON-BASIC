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
    if function not in math.__dict__:
        raise OperationNotFoundException
    if not callable(math.__dict__[function]):
        raise OperationNotFoundException
    function = math.__dict__[function]
    return function(*args)


"""
Write tests for math_calculate function
"""


@pytest.mark.parametrize('test_input,test_output', [
    (['ceil', 10.5], 11),
    (['floor', 10.5], 10),
    (['sin', 0], 0),
    (['cos', 0], 1)
])
def test_good_operations(test_input, test_output):
    assert math_calculate(*test_input) == test_output


@pytest.mark.parametrize('test_input', [
    ['this operation does not exist', 1, 2],
    ['__name__', 1, 2],
    ['inf', 1, 2],
    ['e', 1, 2],
    ['exp3', 1, 2]
])
def test_bad_operations(test_input):
    with pytest.raises(OperationNotFoundException):
        math_calculate(*test_input)
