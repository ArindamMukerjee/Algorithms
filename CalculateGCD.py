import math
# Calculate GCD of two numbers
def gcd(a, b):
    while b!=0:
        remainder = a%b
        a = b
        b = remainder
    return a
gcd(20, 16)
gcd(4851, 3003)

# GCD with bezout's identity and calculating the values of multipliers
a, b = 210, 154
def bezout_gcd(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b != 0:
        remainder = a%b
        quotient = math.floor(a/b)
        a = b
        b = remainder
        x = x0 - quotient*x1
        y = y0 - quotient*y1
        x1, x0 = x, x1
        y1, y0 = y, y1
    return a, x0, y0
bezout_gcd(a, b)
