import os
import shutil
import string

#1
def list_contents(path):
    if not os.path.exists(path):
        return "Path does not exist."
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files, os.listdir(path)

#2
def check_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

#3
def path_info(path):
    if os.path.exists(path):
        return os.path.basename(path), os.path.dirname(path)
    return "Path does not exist."

#4
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for _ in file)

#5
def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        file.writelines(f"{line}\n" for line in data)

#6
def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is {letter}.txt\n")

#7
def copy_file(source, destination):
    shutil.copyfile(source, destination)

#8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return "File deleted."
    return "File cannot be deleted."

#примеры принтов
print(list_contents(".")) 
print(check_access("example.txt"))
print(path_info("example.txt"))
write_list_to_file("test.txt", ["Hello", "World"])
generate_alphabet_files()
copy_file("test.txt", "copy_test.txt")
print(delete_file("test.txt"))
