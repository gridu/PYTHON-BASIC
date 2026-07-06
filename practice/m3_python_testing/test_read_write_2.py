"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import pytest

from practice.m2_python_part_2 import task_read_write_2


def test_task_read_write_2(tmp_path):
    words = task_read_write_2.generate_words()
    file1 = tmp_path / "f1.txt"
    file2 = tmp_path / "f2.txt"

    task_read_write_2.write_files(words, file1, file2)

    try:
        with open(file1, "r", encoding="utf-8") as f:
            assert f.read() == "\n".join(words)
    except UnicodeDecodeError:
        pytest.fail("Encoding is not utf-8")

    try:
        with open(file2, "r", encoding="cp1252") as f:
            assert f.read() == ",".join(reversed(words))
    except UnicodeDecodeError:
        # XXX: This wont triger for files wich do not contain any bad characters like ą, ę even if
        # encoding is wrong (for example set to utf-8) it should be check assuring correct open() function call
        # argument not the file itself
        pytest.fail("Encoding is not cp1252")
