"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""



# To allow importing modules from other directories
import sys
import unittest
import tempfile
import os

# Allowing file to search for modules in parent directory. Need to cd into 3_python_testing folder
sys.path.append("..")

from python_part_2 import task_read_write_2 as task

class Read_Write_Tests_2(unittest.TestCase):
    def test_read_write_2_output(self):
        temp_path = tempfile.mkstemp()[1]
        task.read_files("file_1.txt", "file_2.txt", res_file_path=temp_path)

