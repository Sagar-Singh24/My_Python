# Print Each Line of a File in Reverse Order

def print_lines_in_reverse(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print("Lines in reverse order:")
            for line in lines:
                print(line.strip()[::-1])
    except FileNotFoundError:
        print("File not found!")

# Example usage:
filename = input("Enter the filename: ")
print_lines_in_reverse(filename)
