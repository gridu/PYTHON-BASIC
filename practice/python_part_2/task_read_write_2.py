"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""
import typing


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


def write_files(file1: typing.TextIO, file2: typing.TextIO, words: list):
    first = True
    for word in words:
        if first:
            file1.write(word)
            first = False
        else:
            file1.write("\\n" + word)

    first = True
    for word in words[::-1]:
        if first:
            file2.write(word)
            first = False
        else:
            file2.write("," + word)


if __name__ == '__main__':
    words = generate_words()
    file_1 = open("file1.txt", 'w', encoding='utf-8')
    file_2 = open("file2.txt", 'w', encoding='cp1252')
    write_files(file_1, file_2, words)
