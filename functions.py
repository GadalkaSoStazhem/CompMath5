import math


def get_equation(number):
    if number == 1:
        return lambda x, y: 1 - math.sin(1.25 * x + y) + (0.5 * y)/(x + 2)
    elif number == 2:
        return lambda x, y: x + math.cos(y / math.sqrt(5))
    else:
        return 0