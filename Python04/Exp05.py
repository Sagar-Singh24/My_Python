# Convert Lowercase to Uppercase Without upper()

def to_uppercase(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

# Input
lowercase_string = input("Enter a lowercase string: ")
uppercase_string = to_uppercase(lowercase_string)
print(f"Uppercase: {uppercase_string}")
