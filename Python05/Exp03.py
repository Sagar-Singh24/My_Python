# Count Positive, Negative, and Zero Numbers in a List

# Input: Enter a list of numbers
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
positive_count = sum(1 for num in numbers if num > 0)
negative_count = sum(1 for num in numbers if num < 0)
zero_count = numbers.count(0)

print("Positive Numbers Count:", positive_count)
print("Negative Numbers Count:", negative_count)
print("Zeros Count:", zero_count)
