"""
Write tests for python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import unittest
import tempfile
import re
from python_part_2 import task_read_write_2 as t2


class TestFileContent(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_file1 = tempfile.NamedTemporaryFile('r+', delete=False)
        self.tmp_file2 = tempfile.NamedTemporaryFile('r+', delete=False)
        t2.write_files(self.tmp_file1, self.tmp_file2, t2.generate_words())
        self.tmp_file1.seek(0)
        self.tmp_file2.seek(0)

    def test_separators(self):
        file1_content = self.tmp_file1.read()
        file2_content = self.tmp_file2.read()

        self.assertTrue(re.search(r"[a-zA-Z]\\n[a-zA-Z]", file1_content) and
                        re.search(r"[a-zA-Z],[a-zA-Z]", file2_content),
                        msg='Wrong separator used')

    def test_both_files_same_words(self):

        file1_content = self.tmp_file1.read()
        file2_content = self.tmp_file2.read()

        """

        special_chars = " !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        counter_of_non_letters = 0
        separator_file1 = ""
        for i in file1_content:
            if not i.isalpha():
                counter_of_non_letters += 1
                if i in special_chars:
                    separator_file1 += '\\'
                separator_file1 += i
            elif counter_of_non_letters > 0:
                break

        counter_of_non_letters = 0
        separator_file2 = ""
        for i in file2_content:
            if not i.isalpha():
                counter_of_non_letters += 1
                if i in special_chars:
                    separator_file2 += '\\'
                separator_file2 += i
            elif counter_of_non_letters > 0:
                break
                
        """

        file1_content = file1_content.split("\\n")
        file2_content = file2_content.split(",")
        self.assertTrue(file1_content == file2_content[::-1], msg='Words in both files differ')



