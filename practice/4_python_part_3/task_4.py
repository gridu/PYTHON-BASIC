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
from faker import Faker
from unittest.mock import patch

def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()

    for _ in range(args.number):
        data = {}
        for field, provider in args.fields.items():
            data[field] = getattr(fake, provider)()

        print(data)

@patch('builtins.print')
def test_print_name_address(mock_print):
    fake_args = argparse.Namespace(number=2, fields={'fake_address': 'address', 'some_name': 'name'})

    print_name_address(fake_args)

    assert mock_print.call_count == 2

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
