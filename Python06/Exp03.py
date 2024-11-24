# Tuple-Based Addition and Multiplication

def process_tuple(numbers):
    addition = sum(numbers)
    multiplication = 1
    for num in numbers:
        multiplication *= num
    return addition, multiplication

# Example usage:
numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
addition, multiplication = process_tuple(numbers)
print(f"Addition: {addition}, Multiplication: {multiplication}")
