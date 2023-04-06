import numpy as np
import matplotlib.pyplot as plt
from least_square import *
from functions import solution


def get_graphs(result, a, b, y_0, number):
    ids, xs, ys, fs = zip(*result)
    fig, axes = plt.subplots(nrows=2, ncols=1)
    x = np.linspace(a, b, 100)
    xy = formater(result, 1, 2)
    approx = get_linear_function(xy, len(xy))
    axes[0].scatter(xs, ys, color='black', label = 'найденные решения')
    axes[0].scatter(xs[0], ys[0], color='red', label='начальное условие')
    axes[0].plot(x, approx(x), color='blue', label = 'линейная аппроксимация')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    axes[0].legend()

    axes[1].scatter(xs, ys, color='orange', label='найденные решения')
    axes[1].scatter(xs[0], ys[0], color='red', label='начальное условие')
    if solution(number, a, y_0) != None:
        an_solution = solution(number, a, y_0)
        axes[1].plot(x, an_solution(x), color='green', label='аналитическое решение')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')
    axes[1].legend()

    plt.show()


def formater (result, col1, col2):
    formated = []
    for i in range(len(result)):
        row = [result[i][col1], result[i][col2]]
        formated.append(row)
    return formated