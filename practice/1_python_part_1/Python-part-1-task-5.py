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


from pdb import line_prefix


def remove_duplicated_words(line: str) -> str:
   line = line.split(" ")
   without_duplicates = list(dict.fromkeys(line))
   without_duplicates_str = ' '.join(map(str, without_duplicates))
   print(without_duplicates_str)

remove_duplicated_words('cat cat dog 1 dog 2')