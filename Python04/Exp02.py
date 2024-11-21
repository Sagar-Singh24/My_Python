# Check Number for Armstrong, Perfect, Adam, or Palindrome

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)

def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_adam(num):
    squared = num ** 2
    reversed_num = int(str(num)[::-1])
    reversed_squared = int(str(reversed_num ** 2)[::-1])
    return squared == reversed_squared

# Input
number = int(input("Enter a number: "))

print(f"Armstrong: {is_armstrong(number)}")
print(f"Perfect: {is_perfect(number)}")
print(f"Palindrome: {is_palindrome(number)}")
print(f"Adam: {is_adam(number)}")
