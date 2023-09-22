import math


def two_decimal_places(number):
    # new_num = float(f'{number:.2f}')
    # return new_num
    return math.trunc(number * 100) / 100