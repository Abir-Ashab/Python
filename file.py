# Create a sample text file
file_name = "sample.txt"
with open(file_name, "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("It contains some text.\n")
    file.write("Python is awesome!\n")

# Opening and reading a file
with open(file_name, "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Reading lines from a file
with open(file_name, "r") as file:
    lines = file.readlines()
    print("Lines in the file:")
    for line in lines:
        print(line.strip())  # strip() removes newline characters

# Appending to a file
with open(file_name, "a") as file:
    file.write("Appending new content.\n")

# Checking if a file exists
import os
if os.path.exists(file_name):
    print(f"{file_name} exists.")

# Renaming a file
new_file_name = "renamed_sample.txt"
os.rename(file_name, new_file_name)

# Checking if a file exists (after renaming)
if os.path.exists(new_file_name):
    print(f"{new_file_name} exists.")

# Deleting a file
os.remove(new_file_name)
print(f"{new_file_name} has been deleted.")

# Error handling for file operations
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# Creating directories
os.mkdir("sample_directory")

# Renaming directories
os.rename("sample_directory", "renamed_directory")

# Removing directories
os.rmdir("renamed_directory")
print("Directory removed.")

# Handling exceptions when removing directories
try:
    os.rmdir("non_existent_directory")
except FileNotFoundError:
    print("Directory not found!")

# Getting the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Listing files and directories in a directory
files_and_dirs = os.listdir(current_directory)
print("Files and directories in the current directory:")
for item in files_and_dirs:
    print(item)
