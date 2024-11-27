# Check for Words in a Poem

# Create the "poems.txt" file containing the poem
with open("poems.txt", "w") as file:
    file.write("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.")

# Check if the words "twinkle" and "star" are present
def check_words_in_file(filename, words):
    try:
        with open(filename, "r") as file:
            content = file.read().lower()
            for word in words:
                if word.lower() in content:
                    print(f'The word "{word}" is found in the file.')
                else:
                    print(f'The word "{word}" is not found in the file.')
    except FileNotFoundError:
        print("File not found!")

# Example usage
check_words_in_file("poems.txt", ["twinkle", "star"])
