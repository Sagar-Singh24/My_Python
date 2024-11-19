# Write a Python program to enter a 6-digit number (for example 786531) 
# find the sum of their increasing order powers (sum1=71+82+63+54+35+16). 
# reverse the summation of digits (sum2=11+32+53+64+85+76).
# find subtraction of sum2 from sum1 and print the result.

def compute_sum_difference(number):
    # Convert the number to a string for easier manipulation
    num_str = str(number)

    # Ensure the number is a 6-digit number
    if len(num_str) != 6:
        print("Please enter a valid 6-digit number.")
        return

    # Calculate sum1
    sum1 = 0
    for i in range(6):
        sum1 += int(num_str[i]) ** (i + 1)

    # Calculate sum2
    reversed_num_str = num_str[::-1]
    sum2 = 0
    for i in range(6):
        sum2 += int(reversed_num_str[i]) ** (i + 1)

    # Calculate the difference
    result = sum1 - sum2

    # Print the result
    print(f"Sum1: {sum1}")
    print(f"Sum2: {sum2}")
    print(f"Difference (Sum1 - Sum2): {result}")

# Input: Enter a 6-digit number
try:
    six_digit_number = int(input("Enter a 6-digit number: "))
    compute_sum_difference(six_digit_number)
except ValueError:
    print("Invalid input. Please enter a numeric 6-digit number.")
