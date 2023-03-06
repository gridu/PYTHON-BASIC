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
    output_string = ""
    for line in lines:
        splitted = line.split(" ")
        i =0
        while i < (len(splitted)-1):
            if splitted[i] == splitted[i+1]:
                splitted.pop(i)
            else:
                i+=1
        output = splitted[word_number] + " "
        output_string += output
    print(output_string)
build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)