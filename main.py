from my_io import *
from functions import *
from adams_method import adams3
from graphs import *

number = get_number()
print_equation(number)
a, b = get_interval()
y_0 = get_condition(a)
n, h = get_nodes(a, b)
f = get_equation(number)
an_solution = solution(number, a, y_0)
result = adams3(f, a, n, h, y_0, an_solution)
print_table(result)
get_graphs(result, a, b, y_0, an_solution)
