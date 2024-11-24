# Recursive Function with Foo(n, p)

def foo(n, p):
    if n == 0:
        return 0
    else:
        k = n % 10
        n = n // 10
        p += k + n
        print(f"K: {k}, N: {n}, P: {p}")
        return foo(n, p)

# Initial call to the function
foo(3042, 0)
