"""
Create virtual environment and install Faker package only for this venv.
Using Faker, generate mock Name and address.
Then create functions which read current name and address(optional) as external arguments(args/argparse module)
And print as output like “Name is {Name}”
If address was entered, also print “Address is {Address}}”
example of running script
$python task_4.py Fake Name --address="Fake Address"
Name is Fake Name
Address is Fake Address
"""

import argparse


def print_name_address(args: argparse.Namespace) -> None:
    ...


