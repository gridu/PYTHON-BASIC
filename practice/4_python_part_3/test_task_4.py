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
import os
import subprocess

from task_4_exceptions import InvalidFakerProviderException, InvalidKeyValuePairException

print(subprocess.run(["python3", "task_4.py", "2", "--name=s", "--address=address=addr"]))
class TestPrintName:
    def test_with_valid_args(self, capfd):
        os.system("python3 'task_4.py' 2 --name=name --address=address")
        captured = capfd.readouterr()
        out_dict = {'name': 'Amanda Tracy', 'address': '944 Priscilla Junctions Suite 591\nEast Davidberg, NV 13114'}
        assert captured.out == f"{out_dict}\n"*2
    
    def test_with_invalid_dict_pair(self):
        with pytest.raises(InvalidKeyValuePairException):
            subprocess.run(["python3", "task_4.py", "2", "--name=s", "--address=address=addr"])
        # assert os.system("python3 'task_4.py' 2 --name=s --address=address=addr") == "n"

        # with pytest.raises(InvalidKeyValuePairException):

