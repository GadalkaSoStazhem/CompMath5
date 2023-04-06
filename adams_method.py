def adams3(f, a, n, h, y_0):

    print('h', h)
    result = []
    y = y_0
    for i in range(3):
        x = a + i * h
        row = [i, x, round(y, 4), round(f(x, y), 4)]
        result.append(row)
        y = runge_kutt(f, x, y, h)

    for i in range(3, n):
        x = result[i - 1][1]
        y = result[i - 1][2]
        y_next = y + (h/12) * (23 * f(x, y)
                               - 16 * f(result[i - 2][1], result[i - 2][2])
                               + 5 * f(result[i - 3][1], result[i - 3][2]))
        y_next = y + (h / 12) * (5 * f(x + h, y_next)
                                 + 8 * f(x, y)
                                 - f(result[i - 2][1], result[i - 2][2]))
        row = [i, x + h, round(y_next, 4), round(f(x + h, y_next), 4)]
        result.append(row)

    return result


def runge_kutt(f, x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    y_next = y + 0.1666667 * (k1 + 2 * k2 + 2 * k3 + k4)

    return y_next
