# Count the Number of Characters, Words, and Lines in a File

def count_file_details(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_characters = sum(len(line) for line in lines)
            
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_characters}")
    except FileNotFoundError:
        print("File not found!")

# Example usage:
filename = input("Enter the filename: ")
count_file_details(filename)
