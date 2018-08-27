
a_range = input('Введите числовой диапазон (целые числа) в формате n1 n2 через пробел, где n2>n1\n')

from re import findall
n1 = int(a_range.split(' ')[0])
n2 = int(a_range.split(' ')[0])

from random import randint
print(randint(n1,n2))


a_range = input('Введите числовой диапазон (любые числа) в формате n1 n2 (через пробел), где n2>n1\n')

from re import findall
n1 = float(a_range.split(' ')[0])
n2 = float(a_range.split(' ')[0])

from random import uniform
print(uniform(n1,n2))


a_range = input('Введите символьный диапазон в формате a-z\n')

n1 = ord(str(a_range.split('-')[0]))
n2 = ord(str(a_range.split('-')[1]))

print(chr(randint(n1,n2)))
