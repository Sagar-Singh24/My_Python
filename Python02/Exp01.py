# Write a Python program to perform addition and subtraction of two complex number to be inputted from standard keyboard. 


def add_complex_numbers(num1, num2):
    """Adds two complex numbers."""
    real_sum = num1.real + num2.real
    imag_sum = num1.imag + num2.imag
    return complex(real_sum, imag_sum)

def subtract_complex_numbers(num1, num2):
    """Subtracts two complex numbers."""
    real_diff = num1.real - num2.real
    imag_diff = num1.imag - num2.imag
    return complex(real_diff, imag_diff)

def main():
    """Main function to get input and perform operations."""
    num1_str = input("Enter the first complex number (in the form a+bj): ")
    num2_str = input("Enter the second complex number (in the form a+bj): ")

    try:
        num1 = complex(num1_str)
        num2 = complex(num2_str)

        sum_result = add_complex_numbers(num1, num2)
        diff_result = subtract_complex_numbers(num1, num2)

        print("Sum:", sum_result)
        print("Difference:", diff_result)

    except ValueError:
        print("Invalid input format. Please enter complex numbers in the form a+bj.")

if __name__ == "__main__":
    main()