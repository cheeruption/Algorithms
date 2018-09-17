'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

'''


import random


array_new = [round(random.random()*50,2) for _ in range(10)]
print(array_new)

def selection_sort(array):
    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] <= array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]
        print(array)


selection_sort(array_new)
print(array_new)
