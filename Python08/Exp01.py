# Count Frequency of Characters in a File

from collections import Counter

def count_character_frequency(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            frequency = Counter(content)
            print("Character frequencies:")
            for char, count in frequency.items():
                print(f"'{char}': {count}")
    except FileNotFoundError:
        print("File not found!")

# Example usage:
filename = input("Enter the filename: ")
count_character_frequency(filename)
