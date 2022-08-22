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
final_str = ""
for i in range(1, 21):
    file = open("files/file_"+str(i)+".txt", 'r')
    content = file.readline()
    final_str += ", " + content
file = open("files/result.txt", 'w')
file.write(final_str[2:])
