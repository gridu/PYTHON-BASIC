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

from pathlib import Path

CURR_DIR = Path(__file__).parent
DATA_DIR = CURR_DIR / "files"
RES_FILE = CURR_DIR / "result.txt"


def concat_files(data_dir, res_file):
    tab = []
    for file in sorted(data_dir.iterdir()):
        with open(file) as f:
            pom = f.readline().strip()
            tab.append(pom)
    result_string = ", ".join(str(el) for el in tab)
    print(result_string)

    with open(res_file, "w") as f:
        f.write(result_string)


if __name__ == "__main__":
    concat_files(DATA_DIR, RES_FILE)
