"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import pytest


import sys
sys.path[0] = '' # necessary to import from a sibling folder
from practice._2_python_part_2.task_read_write import main as read_write


def test_read_write(tmpdir):
    folder = tmpdir.mkdir('files')
    for i in range(10):
        file = folder.join(f'file_{i}.txt')
        file.write(i)
    read_write(folder)
    expected_output = ', '.join([str(i) for i in range(10)])
    actual_output = folder.join('result.txt').read()
    assert expected_output == actual_output


if __name__ == '__main__':
    pytest.main([__file__])
