sum = 0
a = 1
n1 = int(input('Введите количество элементов '))
for i in range(n1):
    sum+=a
    a = a/(-2)
print('Сумма равна',sum)