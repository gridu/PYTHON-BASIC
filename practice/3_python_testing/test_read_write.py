"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
from task_read_write import unpack_data, load_data
import tempfile, unittest


class Test(unittest.TestCase):
    def SetUp(self):
        self.data = unpack_data()

    def test_unpack_data(self):
        for i in range(1, 21):
            with open(f'./files/file_{i}.txt', 'r') as f:
                self.assertEqual(self.data[i - 1], f.readline().rstrip('\n'))

    def test_load_data(self):
        check = tempfile.NamedTemporaryFile()
        load_data(self.data, check.name)
        data_to_check = []
        with open(check.name, 'r') as g:
            data_to_check.append(g.read().split(','))
        self.assertEqual(self.data, data_to_check)



