from typing import Iterable


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

def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    final_str = ''
    for line in lines:
        line = ' '.join(dict.fromkeys(line.split())).split()
        if word_number > len(line)-1:
            continue
        final_str += f"{line[word_number]} " 
    return final_str