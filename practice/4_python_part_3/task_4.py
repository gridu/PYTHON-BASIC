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


fake = Faker()

parser = argparse.ArgumentParser(prog="TaskFourCLI")
parser.add_argument('NUMBER', type=int)
parser.add_argument('add_args', nargs=argparse.REMAINDER)
args = parser.parse_args()

class InvalidKeyValuePair(Exception):
    pass

class InvalidFakerProvider(Exception):
    pass

def print_name_address(args: argparse.Namespace) -> None:
    for _ in range(args.NUMBER):
        new_dict = {}
        for arg in args.add_args:
            arg_lst = arg.split("=")

            # Check if after split of add_args it's equal to 2
            if len(arg_lst) != 2:
                raise InvalidKeyValuePair("A dictionary requires a key-value pair.")
        
            dict_key = arg_lst[0].strip('--')
            arg_val = arg_lst[1]

            try:
                f = getattr(fake, arg_val)
            except AttributeError:
                print(arg_val)
                raise InvalidFakerProvider('Faker Provider not found. Please enter a valid value.')
            
            new_dict[dict_key] = f()
        print(f"{new_dict}")
print_name_address(args)
