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
    words = line.split()
    list_of_words = []
    final_line = ""
    if words:
        for word in words:
            if word not in list_of_words:
                list_of_words.append(word)
                final_line += " " + word

    return final_line[1:]


