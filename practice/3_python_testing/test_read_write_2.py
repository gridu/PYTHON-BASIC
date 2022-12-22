"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

from tasks.task_read_write_2 import generate_words
import tempfile


def test_generate_words():
    normal = tempfile.NamedTemporaryFile()
    reverse = tempfile.NamedTemporaryFile()
    words = generate_words(20, normal.name, reverse.name)
    with open(normal.name, 'r') as f, open(reverse.name, 'r') as g:
        assert words == f.read().split('\n') and words[::-1] == g.read().split(',')
