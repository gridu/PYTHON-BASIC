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

def read_files(*files):
    path = r"\files"

    print(files)
    # Need to cd into folder above files
    path_to_folder = os.getcwd() + path
    # files_list = [file for sub_dir, dirs, files in os.walk(path_to_folder) for file in files]
    files_list = [file for file in files]
    print(files_list)
    res_lst = []

    for file in files_list:
        with open(f"{path_to_folder}\{file}", "r") as f:
            file_content=f.read()
            res_lst.append(file_content)

    with open(fr"{path_to_folder}\result.txt", "w") as r:
        r.write(",".join(res_lst))
