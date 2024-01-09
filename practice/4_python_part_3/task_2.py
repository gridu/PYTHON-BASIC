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
import pytest
from task import math_calculate, OperationNotFoundException

def test_math_calculate_log():
    result = math_calculate('log', 1024, 2)
    assert result == 10.0

def test_math_calculate_ceil():
    result = math_calculate('ceil', 10.7)
    assert result == 11

def test_math_calculate_invalid_operation():
    with pytest.raises(OperationNotFoundException, match="Invalid operation: 'invalid'"):
        math_calculate('invalid', 10)

def test_math_calculate_invalid_arguments():
    with pytest.raises(OperationNotFoundException, match="Invalid operation arguments"):
        math_calculate('log', 'invalid_argument')


"""
Write tests for math_calculate function
"""
