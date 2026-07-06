"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""

from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    res = ""
    for line in lines:
        tab = line.split()
        unique_words = []
        for word in tab:
            if word not in unique_words:
                unique_words.append(word)
        if len(unique_words) > word_number:
            res += unique_words[word_number] + " "
    return res[:-1] if len(res) > 0 else res


def main():
    print(build_from_unique_words("a b c", "1 1 1 2 3", "cat dog milk", word_number=1))
    print(build_from_unique_words("a b c", "", "cat dog milk", word_number=0))
    print(build_from_unique_words("1 2", "1 2 3", word_number=10))
    print(build_from_unique_words(word_number=10))


if __name__ == "__main__":
    main()
