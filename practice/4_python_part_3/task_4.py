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
from faker  import Faker
from unittest.mock import patch
import pytest


def test_print_name_adress(capsys):
    with patch("sys.argv", ['task_4.py', '-r', '10', '-f', 'address', 'name']):
        print_name_address()
    captured = capsys.readouterr()
    with pytest.raises(AssertionError):
        assert captured.out == 'something'


def print_name_address():
    parser = argparse.ArgumentParser(description='Create dictionaries with names and other data')
    parser.add_argument('-r', '--rows', type=int, required=True, help='Number of dictionaries to create')
    parser.add_argument('-f', '--fakers', type=str, required=True, help='Set types of faker', nargs='+')
    args = parser.parse_args()
    fake = Faker()
    fake_name = getattr(fake, args.fakers[1])
    fake_adress = getattr(fake, args.fakers[0])
    for i in range(args.rows):
        dictionary = dict(some_name=fake_name(), some_adress=fake_adress())
        print(dictionary)

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
