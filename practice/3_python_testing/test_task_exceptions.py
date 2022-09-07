"""
Write tests for division() function in python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import pytest
from python_part_2 import task_exceptions as te


def test_division_ok(capfd):
    res = te.division(44, 11)
    out, err = capfd.readouterr()
    assert out == "Division finished\n"
    assert res == 4


def test_division_by_zero(capfd):
    res = te.division(1, 0)
    out, err = capfd.readouterr()
    assert out == "Division by 0\nDivision finished\n"
    assert res is None


def test_division_by_one(capfd):
    with pytest.raises(te.DivisionByOneException):
        x = te.division(1, 1)

