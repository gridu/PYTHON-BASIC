"""
Write tests for python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import os.path
import unittest
import tempfile
import filecmp


class TestFileContent(unittest.TestCase):

    def test_content(self):
        final_str = ""
        for i in range(1, 21):
            file = open(os.path.relpath("../python_part_2/files/file_" + str(i) + ".txt"), 'r')
            content = file.readline()
            final_str += ", " + content
            file.close()
        temp_file = tempfile.NamedTemporaryFile('r+', delete=False)
        temp_file.write(final_str[2:])
        temp_file.seek(0)
        # print(temp_file.read())
        # file = open(os.path.relpath("../python_part_2/files/result.txt"), 'r')
        # print(file.read())
        self.assertTrue(
            filecmp.cmp(os.path.relpath("../python_part_2/files/result.txt"), temp_file.name, shallow=False),
            msg='The content of the file is other than expected')
