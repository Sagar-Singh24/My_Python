# Display Common Elements of Two Lists

# Input: Two lists from the user
list1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]
common_elements = list(set(list1) & set(list2))  # Find common elements using set intersection

print("Common Elements:", common_elements)
