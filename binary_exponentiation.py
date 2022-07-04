def binary_exp(value = None, exponent = None):
    result = 1
    factor = value
    while exponent != 0:
        print(f'result:{result}, factor:{factor}, exponent:{exponent}')
        if (exponent%2 == 1):
            result *= factor
        factor *= factor
        exponent //= 2
    return result

binary_exp(value = 2, exponent = 5)

b = 21
while b != 0:
    print(b%2, b)
    b //= 2
