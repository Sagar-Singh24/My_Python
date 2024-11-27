# Replace "donkey" with "$$$$$" in a File

# Create a file with the word "donkey" multiple times
with open("donkey.txt", "w") as file:
    file.write("The donkey is a domestic animal. The donkey is hardworking. Everyone respects the donkey.")

# Replace "donkey" with "$$$$$" in the file
def replace_word_in_file(filename, target_word, replacement):
    try:
        with open(filename, "r") as file:
            content = file.read()

        content = content.replace(target_word, replacement)

        with open(filename, "w") as file:
            file.write(content)
        print(f'All occurrences of "{target_word}" have been replaced with "{replacement}".')
    except FileNotFoundError:
        print("File not found!")

# Example usage
replace_word_in_file("donkey.txt", "donkey", "$$$$$")
