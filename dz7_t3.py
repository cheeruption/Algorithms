'''

3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше 
медианы, в другой – не больше ее.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, 
который не рассматривался на уроках.
'''


import random

m = int(input('Введите натуральное число (m) '))
array_new = [random.randint(-100,100) for _ in range(2*m+1)]
print('Заданный массив',array_new)
for i in range(len(array_new)):
    bol = 0
    men = 0
    rav = 0
    for j in range(len(array_new)):
        if j!=i:
            if array_new[j]> array_new[i]:
                bol+=1
            elif array_new[j]< array_new[i]:
                men+=1
            else:
                rav+=1
    if bol+men+rav+1 == 2*m+1:
        if bol == men or bol+rav == men or men+rav == bol:
            print('Медиана данного массива - число', array_new[i])
            break
print('*'*50+'\n'+'Проверка {}\nОтсортированный массив{}'.format(sorted(array_new)[m],sorted(array_new)))