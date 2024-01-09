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



import os

def read_files_and_write_result(directory_path="./files", output_file="result.txt"):

    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    values = []

    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "r") as file:
            try:
                value = int(file.read().strip())
                values.append(str(value))
            except ValueError:
                print(f"Ignoring non-numeric content in {file_name}")

    result_path = os.path.join(directory_path, output_file)
    with open(result_path, "w") as result_file:
        result_file.write(", ".join(values))

# Call the function
read_files_and_write_result()