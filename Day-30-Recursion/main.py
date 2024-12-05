# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)
def factorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))
print(factorial(4))
print(factorial(5))
print("This is factor of 7 is:",factorial(7))

# 5 * factorial(4)
# 5 * 4 * fatorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Fibonacci Series: https://en.wikipedia.org/wiki/Fibonacci_sequence
# f(0) = 0
# f(1) = 1
# f(2) = f1 + f0
# # fn = f(n-1) + f(n-2)
