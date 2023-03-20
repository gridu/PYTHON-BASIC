"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

# To allow importing modules from other directories
import sys
import tempfile
import pytest
import os

# Allowing file to search for modules in parent directory. Need to cd into 3_python_testing folder
sys.path.append("..")

from python_part_2 import task_read_write as task

# Need to cd into 3_python_testing
def test_read_write_output():
    temp_path = tempfile.mkstemp()[1]
    task.read_files("file_1.txt", "file_2.txt", res_file_path=temp_path)
    with open(temp_path, "r", encoding="utf-8") as temp_file:
        contents = temp_file.read()
    os.remove(temp_path)
    assert contents == "80, 37"

def test_invalid_filename():    
    temp_path = tempfile.mkstemp()[1]
    with pytest.raises(FileNotFoundError):
        task.read_files("file_1.txt", "files_2.txt", res_file_path=temp_path)
    os.remove(temp_path)