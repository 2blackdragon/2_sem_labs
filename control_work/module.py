def find_sred(matrix, n, m):
    summ = 0
    for i in range(n):
        for j in range(m):
            summ += matrix[i][j]
    return summ / (n * m)


def find_min_column(matrix, n, m):
    # Проверка на существование положительного элемента
    flag = False
    min_pol = 0
    column = -1
    i = 0
    while (i < n) and not flag:
        j = 0
        while (j < m) and not flag:
            if matrix[i][j] > 0:
                min_pol = matrix[i][j]
                column = j
                flag = True
            j += 1
        i += 1
    if flag:
        # Поиск координат минимального положительного элемента
        for i in range(n):
            for j in range(n):
                if (matrix[i][j] > 0) and (matrix[i][j] < min_pol):
                    min_pol = matrix[i][j]
                    column = j
    return column
