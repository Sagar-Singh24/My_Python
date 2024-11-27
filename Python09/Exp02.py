# Open Three Files and Handle Missing Files

def open_files(files):
    for file in files:
        try:
            with open(file, "r") as f:
                print(f"Contents of {file}:\n{f.read()}\n")
        except FileNotFoundError:
            print(f"File {file} is not present!")

# Example usage
files = ["planets1.txt", "planets2.txt", "planets3.txt"]
open_files(files)
