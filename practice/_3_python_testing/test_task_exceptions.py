"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import pytest


import sys
sys.path[0] = '' # necessary to import from a sibling folder
from practice._2_python_part_2.task_exceptions import division, DivisionByOneException


def test_division_ok(capfd):
    assert division(10, 2) == 5
    assert division(4, 4) == 1
    assert division(-20, 5) == -4
    out, err = capfd.readouterr()
    assert out == 'Division finished\n' * 3
    assert err == ''


def test_division_by_zero(capfd):
    result = division(1, 0)
    assert result is None
    out, err = capfd.readouterr()
    assert 'Division by 0' in out
    assert 'Division finished' in out
    assert err == ''


def test_division_by_one(capfd):
    with pytest.raises(DivisionByOneException):
        division(1, 1)
    out, _ = capfd.readouterr()
    assert 'Division finished' in out


if __name__ == '__main__':
    pytest.main([__file__])
