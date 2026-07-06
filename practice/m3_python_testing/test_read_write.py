"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

from practice.m2_python_part_2 import task_read_write


def test_task_read_write(tmp_path):
    data_dir = tmp_path / "files"
    data_dir.mkdir()
    tab = []
    for i in range(10):
        tf = data_dir / f"data{i}.txt"
        tf.write_text(f"{i}")
        tab.append(i)

    res_file = tmp_path / "result.txt"

    task_read_write.concat_files(data_dir=data_dir, res_file=res_file)

    assert res_file.read_text() == ", ".join(str(el) for el in tab)
