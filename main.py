from my_io import *
from functions import *
from adams_method import *
from graphs import *

number = get_number()
print("Введите интервал для поиска решений: ")
a, b = [float(x) for x in input().split()]
y_0 = get_condition(a)
n = get_nodes()
eps = get_accuracy()
f = get_equation(number)
result = adams3(f, a, b, n, y_0, eps)
print_table(result)
get_graphs(result, a, b)
