print('Введите координаты двух точек')
print('Введите х1: ')
x1 = float(input())
print('Введите y1: ')
y1 = float(input())
print('Введите x2: ')
x2 = float(input())
print('Введите y2: ')
y2 = float(input())

if x1 != x2:
    k = (y1-y2)/(x1-x2)
    b = y1 - k * x1
    print('Уравнение прямой, проходящей через Ваши точки: y = {:.2f}x + {:.2f}'.format(k, b))
else:
    print(('Уравнение прямой, проходящей через Ваши точки: x = {:.2f}'.format(x1)))