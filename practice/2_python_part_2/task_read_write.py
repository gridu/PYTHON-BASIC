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
path=r"/Users/nrandjelovic/Desktop/PYTHON-BASIC/practice/2_python_part_2/files/"
os.chdir(path)

def read_files(file_path):
    with open(file_path,'r') as f:
        txt=f.read()
    return txt

def read_write():
    res=[]
    for file in os.listdir():
         if file.endswith('.txt'):
            file_path=f"{path}{file}"
            txt=read_files(file_path)
            res.append(txt)
         
    text=", ".join(res)
    
    with open("new_file.txt",'w') as f:
        f.write(text)
    

read_write()