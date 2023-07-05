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
    temp_line = []
    for i in line.split(" "):
        if i not in temp_line:
            temp_line.append(i)
    return (" ".join([i for i in temp_line]))


# print (remove_duplicated_words('cat cat dog 1 dog 2'))