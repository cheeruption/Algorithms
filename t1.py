while True:
    n1 = float(input('Введите первое число '))
    n2 = float(input('Введите второе число '))
    znak = input('Введите знак операции ')

    if znak in '0/*+-':
        if znak == '0':
            break
        else:
            print('Результат:')
            if znak == '*':
                print(n1*n2)
            elif znak == '/':
                if not n2:
                    print('Ошибка деления на ноль\n')
                else:
                    print(n1/n2)
            elif znak == '-':
                print(n1-n2)
            else:
                print(n1+n2)
    else:
        znak = input('Некорректный ввод, введите знак операции повторно ')
