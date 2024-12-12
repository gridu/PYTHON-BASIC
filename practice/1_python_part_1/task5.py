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
    if line != '':
        words = line.split(' ')
    else:
        words = []
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return ' '.join(unique_words)
