"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import pytest


import sys
sys.path[0] = '' # necessary to import from a sibling folder
from practice._2_python_part_2.task_read_write_2 import main as read_write


def test_read_write(tmpdir):
    read_write(tmpdir)
    file1_contents = tmpdir.join('file1.txt').read().split('\n')
    file2_contents = tmpdir.join('file2.txt').read().split(',')[::-1]
    assert file1_contents == file2_contents
    assert len(file1_contents) == 20


if __name__ == '__main__':
    pytest.main([__file__])
