import numpy as np


def get_equation(number):
    if number == 1:
        return lambda x, y: 1 - np.sin(1.25 * x + y) + (0.5 * y)/(x + 2)
    elif number == 2:
        return lambda x, y: x + np.cos(y / np.sqrt(5))
    elif number == 3:
        return lambda x, y: 2 * x * y * y
    elif number == 4:
        return lambda x, y: 1 / np.sqrt(x**2 - 1)
    elif number == 5:
        return lambda x, y: np.power(np.e, -np.sin(x)) - y * np.cos(x)
    elif number == 6:
        return lambda x, y: np.power(np.e, -3 * x)
    elif number == 7:
        return lambda x, y: np.power(np.e, x) / ((1 + np.power(np.e, 2 * x)) * np.power(y, 2))
    elif number == 8:
        return lambda x, y: 4 * x * y - 4 * np.power(x, 3)


def solution(number, x_0, y_0):
    if number == 1:
        print('Невозможно решить аналитически')
        return None
    elif number == 2:
        print('Невозможно решить аналитически')
        return None
    elif number == 3:
        c = (y_0 * x_0 ** 2 + 1) / y_0
        return lambda x:  1 / (c - x ** 2)
    elif number == 4:
        c = y_0 - np.log(np.abs(x_0 + np.sqrt(x_0 ** 2 - 1)))
        return lambda x: np.log(np.abs(x + np.sqrt(x ** 2 - 1))) + c
    elif number == 5:
        c = (y_0 / np.power(np.e, -np.sin(x_0))) - x_0
        return lambda x: (x + c) * np.power(np.e, -np.sin(x))
    elif number == 6:
        c = y_0 + 0.33333333333 * np.power(np.e, -3 * x_0)
        return lambda x: -0.33333333333 * np.power(np.e, -3 * x) + c
    elif number == 7:
        c = (np.power(y_0, 3) - 3 * np.arctan(np.power(np.e, x_0))) / 3
        return lambda x: np.power(3, 1/3) * np.power(c + np.arctan(np.power(np.e, x)), 1/3)
    elif number == 8:
        c = (y_0 - x_0 ** 2 - 0.5) / np.power(np.e, 2 * (x_0 ** 2))
        return lambda x: x ** 2 + 0.5 + c * np.power(np.e, 2 * (x ** 2))
