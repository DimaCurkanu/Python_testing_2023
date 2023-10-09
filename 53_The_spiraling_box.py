def create_box(m, n):
    matrix = [[0] * m for _ in range(n)]

    for el_n in range(n):
        for el_m in range(m):
            min_distance = min(el_n, el_m, n - el_n - 1, m - el_m - 1)
            matrix[el_n][el_m] = min_distance + 1

    return matrix