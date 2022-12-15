"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import pytest
import os
data_test_files=[23,78,3]


#We create temp files with data_test_files
@pytest.fixture
def files(tmp_path):

    d = tmp_path / "sub"
    d.mkdir()

    i=1
    for n in data_test_files:
        p = d / ("file_"+str(i)+".txt")
        p.write_text(str(n))
        i=i+1

    return d

#We read the temp files and the content of each for create result.txt
def test_result_file(files):
    result = []

    for filename in os.listdir(files):
        with open(os.path.join(files, filename), 'rt') as f:
            result.append(int(f.read()))
            f.close()
    
    p=files/'result.txt'
    p.write_text(str(result)[1:-1])

    assert p.read_text() == '23, 78, 3'