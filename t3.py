'''3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.'''

import random
a = [int(random.random()*16) for k in range(10)] #делаю массив из 10 элементов
print('Cлучайный список:\n',a)
minim = min(a)
maxim = max(a)

for num,each in enumerate(a):
    if each == minim:
        a[num] = maxim
    elif each == maxim:
        a[num] = minim
print('Поменяли местами мин и макс:\n',a)