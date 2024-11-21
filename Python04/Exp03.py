# Find LCM and HCF of Two Numbers

import math

def find_hcf_lcm(num1, num2):
    hcf = math.gcd(num1, num2)
    lcm = (num1 * num2) // hcf
    print(f"HCF: {hcf}, LCM: {lcm}")

# Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
find_hcf_lcm(num1, num2)
