"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

import pytest
import typing
from unittest.mock import patch
from your_module import division, DivisionByOneException  # Replace 'your_module' with the actual name of your module


def test_division_ok(capfd):
    # Test division with valid values
    with patch('builtins.print') as mock_print:
        result = division(6, 2)
        captured = capfd.readouterr()

    assert result == 3
    assert captured.out.strip() == "Division finished"
    assert mock_print.call_count == 0  # Ensure no "Division by 0" or "Deletion on 1 get the same result" is printed


def test_division_by_zero(capfd):
    # Test division by zero
    with patch('builtins.print') as mock_print:
        result = division(1, 0)
        captured = capfd.readouterr()

    assert result is None
    assert "Division by 0" in captured.out
    assert "Division finished" in captured.out


def test_division_by_one(capfd):
    # Test division by one
    with patch('builtins.print') as mock_print:
        with pytest.raises(DivisionByOneException, match="Deletion on 1 get the same result"):
            result = division(1, 1)
        captured = capfd.readouterr()

    assert result is None
    assert "Division finished" in captured.out

