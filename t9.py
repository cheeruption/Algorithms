''''9. Найти максимальный элемент среди минимальных
элементов столбцов матрицы.'''

import random
a = []
min_arr=[]

size = int(input('Введите количество столбцов матрицы '))

for i in range(size):
    a.append([])
    for k in range(size):
        a[i].append(random.randint(-100,100))

def print_matrix(lst):
    for i in range(len(lst)):
        for each in lst[i]:
            print('%5d'% each,end=' ')
        print()

print_matrix(a)

for each in a:
    min_arr.append(min(each))
print('Максимальный элемент среди минимальных элемнтов в столбцах:',max(min_arr))
