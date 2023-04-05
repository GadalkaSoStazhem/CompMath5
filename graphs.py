import numpy as np
import matplotlib.pyplot as plt
from least_square import *


def get_graphs(result, a, b):
    ids, xs, ys, fs = zip(*result)
    fig, axes = plt.subplots(nrows=2, ncols=1)
    x = np.arange(a, b + 1, 1)
    xy = formater(result, 1, 2)
    approx = get_linear_function(xy, len(xy))
    axes[0].scatter(xs, ys, color='black', label = 'найденные решения')
    axes[0].scatter(xs[0], ys[0], color='red', label='начальное условие')
    axes[0].plot(x, approx(x), color='blue', label = 'линейная аппроксимация')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    axes[0].legend()
    y = np.arange(min(ys), max(ys) + 1, 1)
    yy = formater(result, 3, 2)
    approx = get_linear_function(yy, len(yy))
    axes[1].scatter(ys, fs, color='orange', label='найденные решения')
    axes[1].scatter(ys[0], fs[0], color='red', label='начальное условие')
    axes[1].plot(y, approx(y), color='blue', label='линейная аппроксимация')
    axes[1].set_xlabel('y')
    axes[1].set_ylabel('y\'')
    axes[1].legend()

    plt.show()


def formater (result, col1, col2):
    formated = []
    for i in range(len(result)):
        row = [result[i][col1], result[i][col2]]
        formated.append(row)
    return formated