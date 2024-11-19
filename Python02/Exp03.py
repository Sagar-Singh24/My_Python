# Write a Python program to input your name and reverse it. Print last 5 character of reversed name.


def reverse_and_extract(name):
    # Reverse the name
    reversed_name = name[::-1]

    # Extract the last 5 characters of the reversed name
    last_five = reversed_name[:5]

    print(f"Reversed Name: {reversed_name}")
    print(f"Last 5 Characters of Reversed Name: {last_five}")

# Input: Enter your name
name = input("Enter your name: ")

# Call the function
reverse_and_extract(name)
