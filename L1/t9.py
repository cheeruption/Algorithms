lst = input('Введите три разных числа через запятую: ').split(',')

a = float(lst[0])
b = float(lst[1])
c = float(lst[2])

if a>b:
    if a<c:
        print('Среднее число -',a)
    elif b>c:
        print('Среднее число -',c)
    else:
        print('Среднее число -',b)
else:
    if b<c:
        print('Среднее число -',b)
    elif a>c:
        print('Среднее число -',a)
    else:
        print('Среднее число -',c)

