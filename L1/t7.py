lens = input('Введите длины трех отрезков через запятую: ').split(',')

if float(lens[0])+float(lens[1])>float(lens[2]) \
        and float(lens[1])+float(lens[2])>float(lens[0]) and float(lens[0])+int(lens[2])>int(lens[1]):
    print('Треугольник существует')
    if float(lens[0]) == float(lens[1]) == float(lens[2]):
        print('Треугольник равносторонний')
    elif float(lens[0]) == float(lens[1]) or float(lens[1]) == float(lens[2]) or float(lens[2]) == float(lens[0]):
            print('Треугольник равнобедренный')
    else:
            print('Треугольник разносторонний')

else:
        print('Треугольник не существует')
