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
import faker


def print_name_address(args: argparse.ArgumentParser) -> None:
    fake = faker.Faker()
    args.add_argument('number', type=int, help='number of records to display')
    args.add_argument('--address')
    args.add_argument('--name')
    par_args = args.parse_args()
    if not par_args.name:
        par_args.name = 'some_name'
    if not par_args.address:
        par_args.address = 'some_address'
    for _ in range(par_args.number):
        print({par_args.name: fake.name(), par_args.address: fake.address()})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    print_name_address(parser)
"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
