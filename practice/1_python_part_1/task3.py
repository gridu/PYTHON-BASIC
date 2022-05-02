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
    unique_list = []
    result =""
    for x in lines:
        x = x.split()
        local_list = []
        for y in x:
            if y not in local_list:
                local_list.append(y)
        unique_list.append(local_list)
    for z in unique_list:
        if word_number < len(z):
            result += z[word_number] + ' '
    return result

print(build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1))