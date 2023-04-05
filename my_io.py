from tabulate import tabulate


def get_number():
    number = int(input("Введите номер примера от 1 до 5 "))
    if number < 1 or number > 5:
        return None
    return number


def get_nodes():
    n = int(input("Введите количество узлов: "))
    return n


def get_accuracy():
    eps = float(input("Введите точность: "))
    return eps


def get_condition(a):
    x_0 = a
    y_0 = float(input("Введите y_0: "))
    print("Начальное условие: y(", x_0, ") = ", y_0)
    return y_0


def print_table(result):
    table = [['№', 'x', 'y', 'f(x,y)']]
    table += result
    print(tabulate(table, headers='firstrow'))

