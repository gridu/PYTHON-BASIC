"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""

import pytest
from unittest.mock import Mock
import os

fake = Mock()
faker_attrs = {'name.return_value': 'Amanda Tracy', 'address.return_value':'944 Priscilla Junctions Suite 591\nEast Davidberg, NV 13114', 'color.return_value': '#e57293'}
fake.configure_mock(**faker_attrs)

print(os.system("python3 'task_4.py' 5 --name=name --address=address"))

class TestPrintName:
    pass
    def test_with_valid_args(self):
        pass
        # test = os.system('task_4 5 --name=name --address=address')
        # print(test)