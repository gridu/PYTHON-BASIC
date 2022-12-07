"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    result=""
    list=line.split(' ')
    unique_words=dict.fromkeys(list)

    for x in unique_words:
        result+= (x+' ')

    return result.strip()