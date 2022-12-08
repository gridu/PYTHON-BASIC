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

import os

if __name__ == '__main__':
    result = []

    for filename in os.listdir("./files"):
        with open(os.path.join("./files", filename), 'rt') as f:
            result.append(int(f.read()))
            f.close()

    result_file=open('result.txt', 'w')
    result_file.write(str(result)[1:-1])
