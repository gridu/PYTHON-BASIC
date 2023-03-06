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


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words
words_n_separator = '\n'.join(map(str, generate_words(n=20)))
words_comma_separator = ', '.join(map(str, generate_words(n=20)))
with open("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/UTF-8_file.txt", "w", encoding="utf-8") as a_file:
    a_file.write(words_n_separator)

with open("/Users/wlitwin/Desktop/Python-Basics/Python-part-2-tasks/files/CP1252_file.txt","w", encoding = "CP1252") as f:
    f.write(words_comma_separator)
print(words_comma_separator)
