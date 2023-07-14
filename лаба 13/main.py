from module import *
from InputOutput import *
import sys

params = sys.argv


fin = params[1]
file = open(fin, 'r')
na, ma = file.readline().split()
na, ma = int(na), int(ma)
a = get_matrix(file, na, ma)

nb, mb = file.readline().split()
nb, mb = int(nb), int(mb)
b = get_matrix(file, nb, mb)
file.close()

fout = params[2]
file = open(fout, 'w')
file.write('Матрица А: \n')
put_matrix(file, a, na, ma)
file.write('Матрица B: \n')
put_matrix(file, b, nb, mb)
file.write('\n')

data = {'1': f1, '2': f2}
f = data[params[3]]

coords = find_coords(a, na, ma, f)
if coords[0] == na - 1 or coords[1] == ma - 1:
    file.write('Ниже и правее элементов нет\n')
else:
    file.write('Результат для матрицы А: \n')
    file.write("{}\n".format(find_max(a, na, ma, coords)))

coords = find_coords(b, nb, mb, f)
if coords[0] == nb - 1 or coords[1] == mb - 1:
    file.write('Ниже и правее элементов нет\n')
else:
    file.write('Результат для матрицы А: \n')
    file.write("{}\n".format(find_max(b, nb, mb, coords)))

'''coords = find_coords(a, na, ma, f)
if coords[0] == na or coords[1] == ma:
    file.write('Координаты не найдены')
else:
    file.write('Результат для матрицы А: \n')
    file.write("{}\n".format(calculate_product(a, na, ma, coords)))

coords = find_coords(b, nb, mb, f)
if coords[0] == nb or coords[1] == mb:
    file.write('Координаты не найдены')
else:
    file.write('Результат для матрицы В: \n')
    file.write("{}\n".format(calculate_product(a, nb, mb, coords)))

bubble_sort(a, na, ma)
print(a)'''

# отсортировать строки в порядке возрастания значения
