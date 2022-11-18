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


def unpack_data():
    data_from_files = []
    for i in range(1, 21):
        with open(f'./files/file_{i}.txt', 'r') as f:
            data_from_files.append(f.readline().rstrip('\n'))
    return data_from_files


def load_data(data_from_files, path='./files/result.txt'):
    with open(path, 'w') as g:
        for number, word in enumerate(data_from_files):
            if number != 19:
                g.write(word + ', ')
            else:
                g.write(word)
