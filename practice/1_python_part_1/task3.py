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
    if word_number < 0:
        return "Invalid word number"

    unique_words = set()
    
    for line in lines:
        words = line.split()
        unique_words.update(words)

    unique_words = list(unique_words)
    
    if word_number >= len(unique_words):
        return "Word number exceeds the unique word count"

    return unique_words[word_number]
