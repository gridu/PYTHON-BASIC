"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

import pytest

from practice.m2_python_part_2 import task_exceptions


def test_division_ok(capfd):
    assert task_exceptions.division(2, 2) == 1
    out, err = capfd.readouterr()
    assert "Division finished" in out


def test_division_by_zero(capfd):
    res = task_exceptions.division(2, 0)
    assert res is None
    out, err = capfd.readouterr()
    assert "Division by 0" in out
    assert "Division finished" in out


def test_division_by_one(capfd):
    with pytest.raises(task_exceptions.DivisionByOneException):
        task_exceptions.division(2, 1)
    out, err = capfd.readouterr()
    assert "Division finished" in out
