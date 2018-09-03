'''5. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве.'''

import random
a=[]
for i in range(15):
    a.append(random.randint(-100,10))
print('Сгенерированный массив:',a)

minim=a[0]
num_min=0
for num,each in enumerate(a):
    if a[num]<minim:
        minim=a[num]
        num_min=num
if minim<0:
    print('Максимальный отрицательный элемент:',minim, ', {}-й элемент слева'.format(num_min+1))