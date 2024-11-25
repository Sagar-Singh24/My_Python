# Read an Entire Text File

def read_entire_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Contents of the file:")
            print(content)
    except FileNotFoundError:
        print("File not found!")

# Example usage:
filename = input("Enter the filename: ")
read_entire_file(filename)
