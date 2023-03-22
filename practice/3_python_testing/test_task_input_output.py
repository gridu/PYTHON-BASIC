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
from read_numbers import read_numbers
import pytest 

class TestInputOutput:
    @patch('builtins.input', lambda x: x)
    def test_return_input(self, num):
        assert input(num) == num
    
    @pytest.mark.parametrize("nums_no_text", [1,2,3,4])
    def test_read_numbers_without_text_input(self, nums_no_text):
        assert read_numbers() == [1,2,3,4]



    def test_read_numbers_with_text_input(self):
        ...
