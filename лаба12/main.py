from module import *
from InputOutput import *

print('Введите заданное значение')
k = float(input())

fin = 'input.txt'
file = open(fin, 'r')
na = int(file.readline())
a = get_matrix(file, na)

nb = int(file.readline())
b = get_matrix(file, nb)

nc = int(file.readline())
c = get_matrix(file, nc)
file.close()

fout = 'output.txt'
file = open(fout, 'w')
file.write('Матрица А: \n')
put_matrix(file, a, na)
file.write('Матрица B: \n')
put_matrix(file, b, nb)
file.write('Матрица C: \n')
put_matrix(file, c, nc)
file.close()

if if_elements(a, na, k):
    print("Среднее арифметическое значений, меньших {} в матрице А = {}".format(k, sred_znach(a, na, k)))
else:
    print(f"'В матрице A ниже главной диагонали нет элементов меньше ', {k}")

if if_elements(b, nb, k):
    print(f"Среднее арифметическое значений, меньших {k} в матрице А = {sred_znach(b, nb, k)}")
else:
    print(f"'В матрице B ниже главной диагонали нет элементов меньше ', {k}")

if if_elements(c, nc, k):
    print(f"Среднее арифметическое значений, меньших {k} в матрице А = {sred_znach(c, nc, k)}")
else:
    print(f"'В матрице C ниже главной диагонали нет элементов меньше ', {k}")


