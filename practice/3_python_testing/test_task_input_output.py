"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from your_module import read_numbers  # Replace 'your_module' with the actual name of your module
from unittest.mock import patch
import io
import sys
import pytest

def mock_input(prompt):
    return next(input_values)

def test_read_numbers_without_text_input():
    global input_values
    input_values = iter(["1", "2", "3", "4"])

    with patch('builtins.input', side_effect=mock_input):
        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            result = read_numbers(4)
            sys.stdout = sys.__stdout__

    assert result == "Avg: 2.50\n------------"
    assert captured_output.getvalue().strip() == ""


def test_read_numbers_with_text_input():
    global input_values
    input_values = iter(["1", "2", "Text"])

    with patch('builtins.input', side_effect=mock_input):
        with io.StringIO() as captured_output:
            sys.stdout = captured_output
            result = read_numbers(3)
            sys.stdout = sys.__stdout__

    assert result == "No numbers entered"
    assert captured_output.getvalue().strip() == ""