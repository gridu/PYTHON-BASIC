"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

def write_to_file(file_path, content, encoding, separator='\n'):
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(separator.join(content))

def reverse_order(words):
    return list(reversed(words))


word_list = generate_words()

write_to_file('file1.txt', word_list, 'utf-8')

reversed_word_list = reverse_order(word_list)

write_to_file('file2.txt', reversed_word_list, 'cp1252', separator=',')

print("Original words:", word_list)
print("Reversed order:", reversed_word_list)

