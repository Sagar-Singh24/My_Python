# Check if a String is a Palindrome

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage:
string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
