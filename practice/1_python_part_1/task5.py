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
    # Split the line into words using space as the delimiter
    words = line.split()
    
    # Create a set to store unique words
    unique_words = set()
    
    # Initialize an empty list to store the non-duplicated words
    result = []
    
    for word in words:
        if word not in unique_words:
            # If the word is not in the set of unique words, add it to the result list
            result.append(word)
            unique_words.add(word)  # Add the word to the set to mark it as seen
    
    # Join the non-duplicated words back into a space-separated line
    result_line = ' '.join(result)
    
    return result_line