"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import pytest
from tasks.task_exceptions import *


def test_division_ok(capfd):
    assert division(15, 5) == 3
    assert division(10, 2) == 5
    division(20, 10)
    out, err = capfd.readouterr()
    assert out == 'Division finished'


def test_division_by_zero(capfd):
    assert division(5, 0) is None
    division(3, 0)
    out, err = capfd.readouterr()
    assert out == 'Division by zero'

def test_division_by_one(capfd):
    with pytest.raises(DivisionByOneException) as e:
        division(5, 1)
    out, err = capfd.readouterr()
    assert out.strip() == 'Division finished'