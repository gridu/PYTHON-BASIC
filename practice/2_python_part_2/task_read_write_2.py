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


def generate_words(n=5):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


def fill():
    words = generate_words()
    print(words)
    words_revers = words[::-1]

    with open('new1.txt', 'w', encoding='UTF-8') as new1:
        for w in words:
            new1.write(w + '\n')

    with open('new2.txt', 'w',encoding='CP1252') as new2:
        for w in words_revers:
            new2.write(w + '\n')


fill()
