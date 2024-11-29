"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""

import os.path


def read_file(path):
    index = 1
    number_table = []
    while True:
        filepath = os.path.join(path, f"file_{index}.txt")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                for x in f:
                    x = x.strip()
                    number_table.append(x)
            index += 1
        else:
            break
    return number_table


def write_file(number_table, path):
    while True:
        result_filepath = os.path.join(path, f"result_1.txt")
        with open(result_filepath, "w") as w:
            w.write(", ".join(number_table))
        break


filepath = "/Users/broczniok/Desktop/PYTHON-BASIC/practice/2_python_part_2/files/"
write_file(read_file(filepath), filepath)
