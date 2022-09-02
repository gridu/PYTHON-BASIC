"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
import builtins
import unittest
import pytest
import re
from unittest import mock

from faker import Faker
from unittest.mock import Mock


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    parser.add_argument("--fake-address", const=None)
    parser.add_argument("--some-name", const=None)
    return parser.parse_args()


def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()
    for _ in range(args.number):
        score = {}
        for key in args.__dict__:
            if key != 'number' and key is not None:
                provider = getattr(fake, args.__dict__[key])
                score[key] = provider()
        print(score)


"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""


class TestPrintNameAddress(unittest.TestCase):
    def setUp(self):
        self.mck = Mock()
        self.mck.args_both = argparse.Namespace(**{"fake_address": "address", "number": 4, "some_name": "name"})
        self.mck.args_name = argparse.Namespace(**{"number": 6, "some_name": "name"})
        self.mck.args_addr = argparse.Namespace(**{"number": 5, "fake_address": "address"})

    @mock.patch('builtins.print')
    def test_print_both_arguments(self, mock_print):
        print_name_address(self.mck.args_both)
        self.assertTrue(len(mock_print.mock_calls) == 4)
        for call in mock_print.call_args_list:
            check_address = re.search("\'fake_address\':", str(call))
            check_name = re.search("\'some_name\':", str(call))
            self.assertTrue(check_name and check_address)

    @mock.patch('builtins.print')
    def test_print_name(self, mock_print):
        print_name_address(self.mck.args_name)
        self.assertTrue(len(mock_print.mock_calls) == 6)
        for call in mock_print.call_args_list:
            check_address = re.search("\'fake_address\':", str(call))
            check_name = re.search("\'some_name\':", str(call))
            self.assertTrue(check_name and not check_address)

    @mock.patch('builtins.print')
    def test_print_address(self, mock_print):
        print_name_address(self.mck.args_addr)
        self.assertTrue(len(mock_print.mock_calls) == 5)
        for call in mock_print.call_args_list:
            check_address = re.search("\'fake_address\':", str(call))
            check_name = re.search("\'some_name\':", str(call))
            self.assertTrue(not check_name and check_address)

