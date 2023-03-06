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



contents = []
def read_file(file_path):
 with open(file_path, 'r') as file:
      a = file.read()
      contents.append(a)
      contents.append(", ")

read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_1.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_2.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_3.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_4.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_5.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_6.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_7.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_8.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_9.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_10.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_11.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_12.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_13.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_14.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_15.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_16.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_17.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_18.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_19.txt")
read_file("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/file_20.txt")

contents_str = ''.join(map(str, contents))
with open("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/new_file", "a") as f:
    f.write(contents_str)

with open("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/new_file", "r") as f:     
    print(f.read())