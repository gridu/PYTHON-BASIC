"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     #>>> math_calculate('log', 1024, 2)
     10.0
     #>>> math_calculate('ceil', 10.7)
     11
"""
import math
import pytest


def math_calculate(function: str, *args):
    if len(args) > 2:
        return print('too many arguments - unconsistent with restriction')
    try:
        function_to_use = getattr(math, function)
    except AttributeError:
        return print('OperationNotFoundException')
    if len(args) == 2:
        result = function_to_use(args[0], args[1])
    else:
        result = function_to_use(args[0])
    return result
#type error gdy sie spierdoli ilosc arg do dobrej funkcji


"""
Write tests for math_calculate function
"""

def test_math_calculate_correct():
    assert math_calculate('log', 1024, 2) == 10.0

def test_math_calculate_incorrect():
    with pytest.raises(AssertionError):
        assert math_calculate('log', 1024, 2) == 15.0

def test_math_calculate_bad_function(capfd):
    math_calculate('dummy', 1024, 2)
    out, err = capfd.readouterr()
    assert out == 'OperationNotFoundException\n'

def test_math_calculate_bad_number_of_args():
    with pytest.raises(TypeError):
        math_calculate('ceil', 1024, 2)
