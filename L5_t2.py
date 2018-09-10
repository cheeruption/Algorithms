from collections import deque
from functools import reduce

dict_1 = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
dict_2 = dict((y, x) for x, y in dict_1.items())

number1 = deque(input('Первое число: '))
number2 = deque(input('Второе число: '))
# number1 = deque('a2')
# number2 = deque('c4f')

def suma_hex(this,that):
    '''
    :param this: число с основанием 16
    :param that: число с основанием 16
    :return: РЕЗУЛЬТАТ В ВИДЕ ШЕСТНАДЦАТЕРИЧНОГО ЧИСЛА
    '''

    dict_1 = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    dict_2 = dict((y, x) for x, y in dict_1.items())

    #развернем числа для прохода по рязрядом начиная с 0-ой степени числа 16
    this.reverse()
    that.reverse()
    power = max(len(this),len(that))
    a = [[] for j in range(power)] #в этот список кладем слагаемые соответсвующего разряда
    i = 0
    while i<len(this):
        a[i].append(this[i])
        i+=1
    i = 0
    while i<len(that):
        a[i].append(that[i])
        i+=1
# после заполнения слагаемых - переведем буквы в цифры
    for k in range(len(a)):
        for x in range(len(a[k])):
            if not a[k][x].isdigit():
                a[k][x] = dict_1[a[k][x]]
            else:
                a[k][x] = int(a[k][x])
    a.append([])

    for num,el in enumerate(a):
        a[num] = sum(el) # считаем сумму каждго разряда
        if a[num] >= 16:#если нужно - переносим в след. разряд число
            a[num+1].append(a[num]//16)
            a[num] = a[num]%16
# подставим буквы где число в разряде больше 9
    for num,each in enumerate(a):
        if a[num] > 9:
            a[num] = dict_2[a[num]]
        else:
            a[num] = str(a[num])
#удалим ненужные разряды
    if a[len(a)-1] == '0':
        a.pop()
    a = a[::-1]
    return ''.join(a)


print('Результат сложения двух чисел =',suma_hex(number1,number2))


elements = len(number1)*len(number2)

mult = [[] for i in range(elements-2)] # вот тут большой вопрос - по сути в массиве будут почленно
# перемноженные элементы
i = 0
#методом конкатенации прописываем слагаемые по правилу умножения
for q,m1 in enumerate(number1):
    for num,m2 in enumerate(number2):
        mult[q+num].append(m1+m2)
mult.append([])#добавим еще один разряд


for num,el in enumerate(mult):
    for i in range(len(el)):
        mult[num][i] = list(el[i])
        for k in range(len(list(el[i]))):
            if not el[i][k].isdigit():
                mult[num][i][k] = dict_1[el[i][k]]
            else:
                mult[num][i][k] = int(el[i][k])                            # в каждом слагаемом
    mult[num] = sum([reduce(lambda x, y: x*y, each) for each in mult[num]])# перемножим слагаемые
                                                                           # и просуммируем одинаковые разряды
for i in range(len(mult)):
    if mult[i] > 15:
        mult[i+1] = mult[i+1]+mult[i]//16
        mult[i] = mult[i]%16
    if mult[i] > 9:
            mult[i] = dict_2[mult[i]]
    else:
            mult[i] = str(mult[i])
for i in range(len(mult)):
    if mult[-1] == '0':
        mult.pop()
print('Результат умножения двух чисел =',''.join(mult[::-1]))


