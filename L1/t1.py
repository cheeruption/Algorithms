print('Введите трехзначное число')
num = input('Ваше число: ')

num = num[-3:] #если число отрицательное
a = int(num[0])
b = int(num[1])
c = int(num[2])

sum = a + b + c
mult = a*b*c

print('Cумма цифр равна {}, произведение цифр равно {}'.format(sum,mult))
