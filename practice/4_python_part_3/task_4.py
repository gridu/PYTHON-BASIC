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
import pytest
import sys
from unittest.mock import patch


fake = Faker()


class FakerProviderNotFoundException(Exception):
    pass


def print_fake_data(namespace: argparse.Namespace) -> None:
    result = {}
    for field in namespace.fields:
        [key, provider] = field.split('=')
        try: 
            result[key] = fake.format(provider)
        except AttributeError:
            raise FakerProviderNotFoundException(provider)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='number', type=int)
    parser.add_argument(dest='fields', nargs='+')
    args = [arg.replace('--', '') for arg in sys.argv[1:]]
    namespace = parser.parse_args(args)
    for _ in range(namespace.number):
        print_fake_data(namespace)


if __name__ == '__main__':
    main()


"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""


@pytest.mark.parametrize('test_input,is_valid', [
    (['', '2', '--fake-address=address', '--some_name=name'], True),
    (['', '1000', '--my_name=name'], True),
    (['', '7', '--test=this_provider_does_not_exist'], False),
    ([''], False)
])
def test_main(capfd, test_input, is_valid):
    with patch('sys.argv', test_input):
        if is_valid:
            main()
            out, err = capfd.readouterr()
            assert len(out[:-1].split('\n')) == int(test_input[1])
            assert err == ''
        else:
            with pytest.raises((FakerProviderNotFoundException, SystemExit)):
                main()
