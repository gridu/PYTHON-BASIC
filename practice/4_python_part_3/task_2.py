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

class InvalidNumberOfArguments(Exception):
    pass

def math_calculate(function: str, *args):
    try:
        math_func = getattr(math, function)
        return math_func(*args)
    except AttributeError:
        raise OperationNotFoundException('Invalid function for math module.')
    except TypeError:
        raise InvalidNumberOfArguments('Recheck the number of arguments.')

"""
Write tests for math_calculate function
"""

class TestMathCalculate:
    def test_valid_func_and_num_params(self):
        assert math_calculate('ceil', 10.7) == 11

    def test_valid_func_invalid_params(self):
        with pytest.raises(InvalidNumberOfArguments):
            math_calculate('ceil', 10.7, 4)
    
    def test_invalid_func(self):
        with pytest.raises(OperationNotFoundException):
            math_calculate('ceils', 10.7)

    

