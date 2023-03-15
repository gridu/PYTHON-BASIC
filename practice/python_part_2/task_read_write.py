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
    path = r"/files"

    # Need to cd into folder above files
    path_to_folder = os.getcwd() + path

    # Get list of files to go through
    files_list = [file for file in files]

    res_lst = []

    # Add contents of each file to results list
    for file in files_list:
        with open(f"{path_to_folder}/{file}", "r", encoding="utf-8") as f:
            file_content=f.read().splitlines() # Reading all lines of file in case content is on multiple lines
            res_lst.extend(file_content)

    # Output the contents of each file to the result text file separated by a comma and space
    with open(fr"{path_to_folder}/result.txt", "w", encoding="utf-8") as r:
        r.write(", ".join(res_lst))

if __name__ == '__main__':
    read_files("file_1.txt", "file_2.txt", "file_3.txt")
