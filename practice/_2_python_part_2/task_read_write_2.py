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
from pathlib import Path


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


def main(path: Path) -> None:
    words = generate_words()
    with open(path / 'file1.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(words))
    with open(path / 'file2.txt', 'w', encoding='cp1252') as file:
        words.reverse()
        file.write(','.join(words))


if __name__ == '__main__':
    main(Path('practice/_2_python_part_2'))
