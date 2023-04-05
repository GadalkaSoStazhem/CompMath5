from my_io import *
from functions import *
from adams_method import *

number = get_number()
print("inter")
a, b = [float(x) for x in input().split()]
y_0 = get_condition(a)
n = get_nodes()
eps = get_accuracy()
f = get_equation(number)

print_table(adams3(f, a, b, n, y_0, eps))