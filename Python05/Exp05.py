# Find the Average of Maximum and Minimum Elements of a List

# Input: A list of numbers
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
max_value = max(numbers)
min_value = min(numbers)
average = (max_value + min_value) / 2

print(f"Maximum: {max_value}, Minimum: {min_value}, Average: {average}")
