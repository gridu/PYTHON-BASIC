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
    final_str = ""
    for line in lines:
        if line:
            words = str(line).split()
            word_count = 0
            if word_number == 0:
                final_str = final_str + " " + words[0]
            else:
                for word in range(1, len(words)):
                    if words[word] != words[word-1]:
                        word_count += 1
                        if word_count == word_number:
                            final_str = final_str + " " + words[word]
    if final_str:
        return final_str[1:]
    else:
        return ""
