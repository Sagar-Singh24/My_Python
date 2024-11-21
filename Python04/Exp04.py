# Find All Prime Numbers Between 11 and 100 and Their Sum

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_and_sum(start, end):
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    print(f"Prime numbers: {primes}")
    print(f"Sum of primes: {sum(primes)}")

# Find primes between 11 and 100
find_primes_and_sum(11, 100)
