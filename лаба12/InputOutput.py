def get_matrix(file, n):
    matrix = [0.0] * n  # [0.0, 0.0, 0,0]
    # [[0.0, 0.0, 0.0], 0.0, 0.0]
    for i in range(n):
        matrix[i] = [0.0] * n  # [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        tmp = file.readline().split()  # '1 2 3 4 5' -> [1, 2, 3, 4, 5]
        for j in range(n):
            matrix[i][j] = int(tmp[j])
    return matrix


def put_matrix(file, matrix, n):
    for i in range(n):
        for j in range(n):
            file.write("{} ".format(matrix[i][j]))
        file.write('\n')
