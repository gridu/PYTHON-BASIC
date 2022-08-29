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
import unittest
from unittest.mock import patch

from python_part_2 import task_input_output as ti


class TestReadNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=[1, 2, 3, 4])
    def test_read_numbers_without_text_input(self, mock_input):
        res = ti.read_numbers(4)
        self.assertEqual(res, "Avg: 2.50")

    @patch('builtins.input', side_effect=[1, 2, 'Text'])
    def test_read_numbers_with_text_input(self, mock_input):
        res = ti.read_numbers(3)
        self.assertTrue(res, "Avg: 1.50")

    @patch('builtins.input', side_effect=['Text'])
    def test_read_numbers_with_only_text_input(self, mock_input):
        res = ti.read_numbers(1)
        self.assertTrue(res == "No numbers entered")