# Rename a File

import os

# Create a dummy file
with open("rename_me.txt", "w") as file:
    file.write("This is a file to be renamed.")

# Rename the file
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except FileNotFoundError:
        print(f"File {old_name} not found!")
    except Exception as e:
        print(f"Error renaming file: {e}")

# Example usage
rename_file("rename_me.txt", "renamed_by_python.txt")
