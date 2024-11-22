# Separate Odd and Even Numbers into Two Lists

# Input: Enter a list of numbers
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
