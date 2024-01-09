"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import os
import tempfile
import pytest

from your_module import generate_words, write_to_file, reverse_order  # Replace 'your_module' with the actual name of your module

@pytest.fixture
def setup_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, "file1.txt")
        file2_path = os.path.join(temp_dir, "file2.txt")

        word_list = generate_words()

        write_to_file(file1_path, word_list, 'utf-8')

        reversed_word_list = reverse_order(word_list)

        write_to_file(file2_path, reversed_word_list, 'cp1252', separator=',')

        yield temp_dir, file1_path, file2_path

def test_generate_words():
    words = generate_words(10)
    assert len(words) == 10

    for word in words:
        assert 3 <= len(word) <= 10

def test_write_to_file(setup_files):
    temp_dir, file1_path, file2_path = setup_files

    with open(file1_path, 'r') as file1:
        content1 = file1.read()
    with open(file2_path, 'r') as file2:
        content2 = file2.read()

    assert content1 == '\n'.join(generate_words())
    assert content2 == ','.join(reverse_order(generate_words()))
