'''8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних
элементов строк. Программа должна вычислять сумму введенных элементов
каждой строки и записывать ее в ее последнюю ячейку. В конце следует
вывести полученную матрицу.'''
a=[]
for i in range(4):
    a.append([])
    print('Вводим {}-ю строку'.format(i+1))
    for k in range(5):
        if k!=4:
            a[i].append(int(input('Введите число ')))
        else:
            a[i].append(sum(a[i]))
def print_matrix(lst):
    for i in range(len(lst)):
        for each in lst[i]:
            print('%5d'% each,end=' ')
        print()

print_matrix(a)
