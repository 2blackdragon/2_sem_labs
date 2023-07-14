def if_elements(data, n, k):
    res = False
    i = 1
    while (i < n) and not res:
        j = 0
        while (j < i - 1) and not res:
            if data[i][j] < k:
                res = True
            j += 1
        i += 1
    return res


def sred_znach(data, n, k):
    summ = 0
    count = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] < k:
                summ += data[i][j]
                count += 1
    if count == 0:
        res = None
    else:
        res = summ / count
    return res
