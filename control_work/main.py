'''
Если две матрицы имеют равное среднее арифметическое,
определить в какой из них меньше номер столбца, содержащего минимальный положительный элемент'''

'''
УПЗ 
Заданы 2 матрицы вещественного типа a и b с размерами na, ma и nb, mb соответственно 
(1 <= na, ma, nb, mb <= 10). Проверить, что среднее арифметическое двух матриц sr_a = sr_b.
Результат проверки fl (лог.) истина, если sr_a = sr_b иначе, fl ложь. Если fl истина, определить 
в какой из двух матриц меньше номер столбца, содержащий минимальный положительный элемент. Иначе
вывести: "Средние арифметические матриц не равны"
'''
from InputOutput import *
from module import *


file = open('input.txt')

size = file.readline().split()
na, ma = int(size[0]), int(size[1])
a = get_matrix(file, na, ma)

size = file.readline().split()
nb, mb = int(size[0]), int(size[1])
b = get_matrix(file, nb, mb)

sr_a = find_sred(a, na, ma)
sr_b = find_sred(b, nb, mb)
if sr_a == sr_b:
    j1 = find_min_column(a, na, ma)
    j2 = find_min_column(b, nb, mb)
    if j1 != -1 and j2 != -1:
        if j1 < j2:
            print('Матрица А')
        elif j1 > j2:
            print('Матрица B')
        else:
            print('В матрице А и B одинаковые столбцы')
    elif j1 == -1:
        print('В матрице А нет положительных элементов')
    elif j2 == -1:
        print('В матрице B нет положительных элементов')
    else:
        print('В двух матрицах нет положительных элементов')
else:
    print('Средние арифметические матриц не равны')

