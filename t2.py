chet = 0
nechet = 0
n1 = list(input('Введите натуральное число: '))

for each in n1:
    if int(each)%2:
        nechet+=1
    else:
        chet+=1

print('Кол-во четных =',chet)
print('Кол-во нечетных =',nechet)