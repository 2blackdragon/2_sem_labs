def f1(x):
    return x


def f2(x):
    return x ** 2 - (x + 5) ** 0.5


def find_coords(matrix, n, m, func):
    x, y = 0, 0
    minn = matrix[0][0]
    for i in range(n):
        for j in range(m):
            if func(matrix[i][j]) < minn:
                minn = func(matrix[i][j])
                x, y = i, j
    return x, y


def find_max(matrix, n, m, coords):
    imin, jmin = coords
    maxx = matrix[imin + 1][jmin + 1]
    for i in range(imin + 1, n):
        for j in range(jmin + 1, m):
            if abs(matrix[i][j]) > maxx:
                maxx = abs(matrix[i][j])
    return maxx


'''def find_coords(matrix, n, m, func):
    x, y = 0, 0
    maxx = matrix[0][0]
    for i in range(n):
        for j in range(m):
            if func(matrix[i][j]) > maxx:
                maxx = func(matrix[i][j])
                x, y = i, j
    return x, y


def calculate_product(matrix, n, m, coords):
    im, jm = coords
    res = 1
    for i in range(im + 1, n):
        for j in range(jm + 1, m):
            res = res * matrix[i][j]
    return res


def calculate_product_in_vector(vector, m):
    res = 1
    for i in range(m):
        res *= vector[i]
    return res


def bubble_sort(matrix, n, m):
    flag = True
    i = 0
    while (i < n) and flag:
        j = 0
        flag = False
        while j < n - i - 1:
            if calculate_product_in_vector(matrix[j], m) > calculate_product_in_vector(matrix[j + 1], m):
                flag = True
                a = matrix[j]
                matrix[j] = matrix[j + 1]
                matrix[j + 1] = a
            j += 1
        i += 1'''
