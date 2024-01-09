import os
import csv
import concurrent.futures

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def generate_and_write_files(ordinal_numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(fibonacci, n): n for n in ordinal_numbers}
        for future in concurrent.futures.as_completed(futures):
            n = futures[future]
            filename = f"file_{n}.txt"
            result = future.result()
            with open(filename, 'w') as file:
                file.write(str(result))

def read_files_and_create_csv(folder_path):
    fibonacci_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            ordinal_number = int(filename.split("_")[1].split(".")[0])
            with open(os.path.join(folder_path, filename), 'r') as file:
                value = int(file.read())
                fibonacci_data.append((ordinal_number, value))

    with open('output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Ordinal Number', 'Fibonacci Value'])
        csv_writer.writerows(fibonacci_data)


ordinal_numbers = [5, 1, 8, 10]
generate_and_write_files(ordinal_numbers)
read_files_and_create_csv('folder_path')