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

result = ''
for i in range(1, 21):
    with open(f'files/file_{i}.txt', 'r') as f:
        result += f.read() + ', '
result = result[:-2]
with open(f'files/result.txt', 'w') as f:
    f.write(result)