# Write a Python program to input 2 strings and insert side-by-side one character from string 2 in string1. 
# (For Ex: String1="Amar", String1="Peter", result= "APmeatrr")

def merge_strings(string1, string2):
    result = ""
    
    # Get the length of the longer string
    max_length = max(len(string1), len(string2))
    
    # Iterate through both strings and merge them character by character
    for i in range(max_length):
        if i < len(string1):
            result += string1[i]
        if i < len(string2):
            result += string2[i]

    return result

# Input: Enter two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Get the merged result
merged_result = merge_strings(string1, string2)

# Print the result
print(f"Merged Result: {merged_result}")
