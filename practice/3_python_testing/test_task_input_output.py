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
import sys
from unittest.mock import patch


def read_numbers(n: int) -> str:
    values = []
    for i in range(n):
        aux = input('Enter value: ')
        if aux.isdigit():
            values.append(int(aux))

    if len(values) == 0:
        return ('No numbers entered')

    else:
        return 'Avg: '+str(round(sum(values)/len(values), 2))

@patch('builtins.input', side_effect=['1', '2', '3','4'])
def test_read_numbers_without_text_input(self):
    assert read_numbers(4) == 'Avg: 2.5'

@patch('builtins.input', side_effect=['text', 'hello', 'bye','cat'])
def test_read_numbers_with_text_input(self):
    assert read_numbers(4) == 'No numbers entered'
