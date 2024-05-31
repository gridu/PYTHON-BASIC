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
    words = []
    for word in line.split():
        if word not in words:
            words.append(word)
    return ' '.join(words)


if __name__ == '__main__':
    assert remove_duplicated_words('cat cat dog 1 dog 2') == 'cat dog 1 2'
    assert remove_duplicated_words('cat cat cat') == 'cat'
    assert remove_duplicated_words('1 2 3') == '1 2 3'
    