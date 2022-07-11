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
    
    lines=list(lines)
   
    lines2=[]
    for i in lines:
        element=list(i.split(" "))
        element2=sorted(set(element))
        lines2.append(element2)

    res=[]  
    for l in lines2:
        if len(l)<word_number:
            continue
        else:
           for n in l:
            ind=l.index(n)
            if ind==word_number:
                res.append(n)

    return " ".join(res)

