import math
def binary_exp(value = None, exponent = None):
    result = 1
    factor = value
    while exponent >= 1:
        if (exponent%2 == 1):
            result *= factor
        factor *= factor
        exponent /= 2
        print(f'result:{result}, factor:{factor}, exponent:{exponent}, '
               f'floor:{math.floor(exponent)}, result:{result}')
        exponent = math.floor(exponent)
    return result

binary_exp(value = 3, exponent = 5)