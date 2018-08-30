import random

n1 = random.randint(0,100)
i = 0

while i < 10:
    n2 = int(input('Введите целое число от 0 до 100: '))
    if n2 == n1:
        print('Вы угадали!')
        break
    else:
        if n2>n1:
            print('Загаданное число меньше',n2)
        else:
            print('Загаданное число больше',n2)
    i+=1
else:
    print('Вы проиграли - загаданное число:', n1)