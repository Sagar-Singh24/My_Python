# Add Two Numbers Using a Module

import operator

def add_numbers(num1, num2):
    """Adds two numbers using the operator module.

    Args:
        num1: The first number.
        num2: The second number.

    Returns:
        The sum of the two numbers.
    """

    result = operator.add(num1, num2)
    return result

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum = add_numbers(num1, num2)
    print("The sum of", num1, "and", num2, "is", sum)