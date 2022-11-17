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
    with open('./files/file1.txt', 'w', encoding='utf-8') as f:
        for number, w in enumerate(words):
            if number != n - 1:
                f.write(w + '\n')
            else:
                f.write(w)
    with open('./files/file2.txt', 'w', encoding='cp1252') as g:
        for number, w in enumerate(words[::-1]):
            if number != n - 1:
                g.write(w + ',')
            else:
                g.write(w)
    return words


if __name__ == '__main__':
    generate_words()
