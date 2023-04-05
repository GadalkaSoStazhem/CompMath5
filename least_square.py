def get_linear_function(points, n):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_kv_x = 0
    for row in points:
        sum_xy += row[0] * row[1]
        sum_x += row[0]
        sum_y += row[1]
        sum_kv_x += row[0] ** 2
    a = (n * sum_xy - sum_x * sum_y) / (n*sum_kv_x - sum_x ** 2)
    b = (sum_y - a * sum_x) / n

    return lambda x: a * x + b