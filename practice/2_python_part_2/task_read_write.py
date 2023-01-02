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

# Import Module
import os
dir_path = "files"

f1 = open("resultfile.txt", "w")
f1.seek(0)
f1.truncate()

for dirpath, dir, files in os.walk(dir_path):
    f2_data = []
    for i in files:
        f2 = open((str(dirpath) + '/' + str(i)), "r")
        f2_data.append(f2.read())
        f2.close()

    result_data = ", ".join(i for i in f2_data)
f1.write(result_data)
f1.close()
