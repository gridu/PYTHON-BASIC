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
import pytest
from unittest.mock import patch


import sys
sys.path[0] = '' # necessary to import from a sibling folder
from practice._2_python_part_2.task_input_output import read_numbers


@pytest.fixture
def user_input_with_text():
    return ['1', '2', '3', 'Text']


@pytest.fixture
def user_input_without_text():
    return ['1', '2', '3', '4']


@pytest.fixture
def user_input_with_only_text():
    return ['hello', 'world', 'hello', 'world']


def test_read_numbers_without_text_input(capfd, user_input_without_text):
    with patch('builtins.input') as mocked_input:
        mocked_input.return_value = user_input_without_text[0]
        mocked_input.side_effect = lambda: user_input_without_text.pop(0)

        read_numbers(4)
        out, _ = capfd.readouterr()
        assert out == f'Avg: {10/4:.2f}\n'


def test_read_numbers_with_text_input(capfd, user_input_with_text):
    with patch('builtins.input') as mocked_input:
        mocked_input.return_value = user_input_with_text[0]
        mocked_input.side_effect = lambda: user_input_with_text.pop(0)

        read_numbers(4)
        out, _ = capfd.readouterr()
        assert out == f'Avg: {6/3:.2f}\n'


def test_read_numbers_with_only_text_input(capfd, user_input_with_only_text):
    with patch('builtins.input') as mocked_input:
        mocked_input.return_value = user_input_with_only_text[0]
        mocked_input.side_effect = lambda: user_input_with_only_text.pop(0)

        read_numbers(4)
        out, _ = capfd.readouterr()
        assert out == f'No numbers entered\n'


if __name__ == '__main__':
    pytest.main([__file__])
