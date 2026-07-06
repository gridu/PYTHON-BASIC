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
from unittest.mock import patch

from faker import Faker


class WrongFakerProviderException(Exception):
    pass


def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()
    arg_list = args._get_kwargs()
    num = arg_list[0][1]
    rest = arg_list[1:]
    for _ in range(num):
        res = "{"
        for el in rest:
            key = el[0]
            method_name = el[1]
            if hasattr(fake, method_name):
                method = getattr(fake, method_name)
            else:
                raise WrongFakerProviderException
            val = method()
            res += f'"{key}": "{val}", '
        res = res[:-2] + "}"
        print(res)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number_of_flags", type=int)
    args, rest = parser.parse_known_args()

    for item in rest:
        tab = item[2:].strip().split("=")
        i_key = tab[0]
        i_val = tab[1]
        setattr(args, i_key, i_val)
    print_name_address(args)

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""


@patch(f"{__name__}.Faker")
def test_print_name_adress(mock, capfd):
    mock_faker = mock.return_value

    mock_faker.name.return_value = "Chad Baird"
    mock_faker.adress.return_value = "62323 Hobbs Green\nMaryshire, WY 48636"
    mock_args = argparse.Namespace(
        number_of_flags=2,
        some_name="name",
    )
    setattr(mock_args, "fake-address", "adress")
    print_name_address(mock_args)
    out, err = capfd.readouterr()
    assert (
        '{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}'
        in out
    )
    assert mock_faker.name.call_count == 2
