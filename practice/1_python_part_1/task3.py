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


def nth_unique_word(line: str, word_number: int) -> str:
    words = []
    for word in line.split():
        if word not in words:
            words.append(word)
    return words[word_number] if word_number < len(words) else None


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    words = [nth_unique_word(line, word_number) for line in lines]
    words = filter(lambda x: x is not None, words)
    return ' '.join(words)


if __name__ == '__main__':
    assert build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1) == 'b 2 dog'
    assert build_from_unique_words('a b c', '', 'cat dog milk', word_number=0) == 'a cat'
    assert build_from_unique_words('1 2', '1 2 3', word_number=10) == ''
    assert build_from_unique_words(word_number=10) == ''
    