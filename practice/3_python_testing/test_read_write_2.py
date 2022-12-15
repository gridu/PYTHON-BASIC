"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import pytest

@pytest.fixture
def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

def text(list,caracter):
    data=''
    for x in list:
        data=data+x+caracter
    return data 

def test_create_line_breaks_file(generate_words,tmpdir):
    p = tmpdir.mkdir("sub").join("file1.txt")
    p.write(text(generate_words,'\n'))
    assert p.read() == (text(generate_words,'\n'))
    assert len(tmpdir.listdir()) == 1

def test_create_commas_file(generate_words,tmpdir):
    p = tmpdir.mkdir("sub").join("file2.txt")
    p.write(text(generate_words,','))
    assert p.read() == (text(generate_words,','))
    assert len(tmpdir.listdir()) == 1


