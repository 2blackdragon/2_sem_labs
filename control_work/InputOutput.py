def get_matrix(file, n, m):
    matrix = [0.0] * n
    for i in range(n):
        matrix[i] = [0.0] * m
        tmp = file.readline().split()
        for j in range(m):
            matrix[i][j] = float(tmp[j])
    return matrix


def put_matrix(file, matrix, n, m):
    for i in range(n):
        for j in range(m):
            file.write("{} ".format(matrix[i][j]))
        file.write('\n')