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

from unittest.mock import patch

from practice.m2_python_part_2 import task_input_output


@patch("practice.m2_python_part_2.task_input_output.input")
def test_read_numbers_without_text_input(mock_input):
    mock_input.side_effect = ["1", "2", "3", "4"]
    result = task_input_output.read_numbers(4)
    assert result == "Avg: 2.5"


@patch("practice.m2_python_part_2.task_input_output.input")
def test_read_numbers_with_text_input(mock_input):
    mock_input.side_effect = ["1", "2", "Text"]
    result = task_input_output.read_numbers(3)
    assert result == "Avg: 1.5"


@patch("practice.m2_python_part_2.task_input_output.input")
def test_read_numbers_with_only_text_input(mock_input):
    mock_input.side_effect = ["ABC", "BCA", "Text"]
    result = task_input_output.read_numbers(3)
    assert result == "no numbers entered"
