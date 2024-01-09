"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import os
import tempfile
import pytest

from your_module import read_files_and_write_result  # Replace 'your_module' with the actual name of your module

@pytest.fixture
def setup_files():

    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, "file1.txt")
        file2_path = os.path.join(temp_dir, "file2.txt")


        with open(file1_path, "w") as file1:
            file1.write("10\n20\n30")

        with open(file2_path, "w") as file2:
            file2.write("40\n50\n60")

        yield temp_dir, file1_path, file2_path

def test_read_files_and_write_result(setup_files):
    temp_dir, file1_path, file2_path = setup_files

    read_files_and_write_result(temp_dir, "output.txt")

    with open(os.path.join(temp_dir, "output.txt"), "r") as output_file:
        result = output_file.read()
        assert result == "10, 20, 30, 40, 50, 60"