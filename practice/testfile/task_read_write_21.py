"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""

class RandomWordsGenerator:
    def __init__(self, somename):
        self.somename = somename

    def generate_words(n=20):
        import string
        import random

        words = list()
        for _ in range(n):
            word = ''.join(random.choices(
                string.ascii_lowercase, k=random.randint(3, 10)))
            words.append(word)

        return words


    fileList = generate_words()
    file1 = "\n".join(i for i in fileList)
    file2 = ",".join(i for i in fileList[::-1])


    f = open("file1.txt", "w", encoding='utf-8')
    f.seek(0)
    f.truncate()
    f.write(file1)
    f.close()

    f = open("file2.txt", "w",  encoding='CP1252')
    f.seek(0)
    f.truncate()
    f.write(file2)
    f.close()
