from tabulate import tabulate


def get_number():
    number = int(input("Введите номер примера от 1 до 8: "))
    if number < 1 or number > 8:
        print("Неверно введен номер примера")
        exit()
    return number


def get_interval():
    print("Введите интервал для поиска решений: ")
    a, b = [float(x) for x in input().split()]
    if not a < b:
        print("Неверно введен интервал")
        exit()
    return a, b


def get_nodes(a, b):
    n = int(input("Введите количество точек: "))
    h = abs(b - a) / (n - 1)
    print("Полученный шаг: h = ", h)
    return n, h


def get_condition(a):
    x_0 = a
    y_0 = float(input("Введите y_0: "))
    print(f"Начальное условие: y({x_0}) = {y_0}")
    return y_0


def print_equation(number):
    print("Выбранное уравнение:")
    if number == 1:
        print('y\' = 1 - sin(1.25x + y) + 0.5y/(x + 2)')
    elif number == 2:
        print('y\' = x + cos(y/sqrt(5))')
    elif number == 3:
        print('y\' = 2xy^2')
    elif number == 4:
        print('y\' = 1 / sqrt(x^2 - 1)')
    elif number == 5:
        print('y\' = e^(-sin(x)) - y * cos(x)')
    elif number == 6:
        print('y\' = e^(-3x)')
    elif number == 7:
        print('y\' = e^x / ((1 + e^(2x)) * y^2)')
    elif number == 8:
        print('y\' = 4xy - 4y^3')


def print_table(result):
    table = [['№', 'x', 'y', 'f(x,y)']]
    table += result
    print(tabulate(table, headers='firstrow'))

