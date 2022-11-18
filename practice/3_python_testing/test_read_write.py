"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
from tasks.task_read_write import unpack_data, load_data
import tempfile, pytest


@pytest.fixture
def data():
    return unpack_data()


def test_unpack_data(data):
    for i in range(1, 21):
        with open(f'./files/file_{i}.txt', 'r') as f:
            assert f.readline() == data[i - 1]


def test_load_data(data):
    file = tempfile.NamedTemporaryFile()
    load_data(data, file.name)
    with open(file.name) as f:
        assert data == f.readline().split(',')
