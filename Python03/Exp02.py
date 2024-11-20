# Write a Python code to design an arithmetic calculator(+,-,*,/,%,<<,>>) with inputting 2 numbers.

def arithmetic_calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Modulo by zero is not allowed."
    elif operation == '<<':
        return num1 << num2
    elif operation == '>>':
        return num1 >> num2
    else:
        return "Invalid operation."

# Input: Enter two numbers and the operation
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, %, <<, >>): ")

    # Calculate the result
    result = arithmetic_calculator(num1, num2, operation)
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
