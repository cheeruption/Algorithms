'''4. Определить, какое число в массиве встречается чаще всего.'''

import random
#создаем массив
M=[]
#заполняем массив
for i in range(50):
    M.append(random.randint(0, 25))
print('Сгенерированный массив:', M)
#записываем какие цифры вообще есть в массиве
values = list(set(M))
print('В массив входят следующие числа:', values)


max_q = 0 #количество вхождений элемента в массив
#считаем количество вхождении для каждого числа
for each in values:
    n = M.count(each)
    if n>max_q: #
        maxim=each
        max_q = n

print('Чаще всего в массиве встречается число',maxim)