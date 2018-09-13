#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
import sys
from re import findall


summ=0
a = input('Введите две латинские буквы через запятую:') #ввожу "d,g"

summ+=sys.getsizeof(a)

pos1 =ord(findall('^\w',a)[0])-96
summ+=sys.getsizeof(pos1)

pos2 =ord(findall('\w$',a)[0])-96
summ+=sys.getsizeof(pos2)

dist = abs(pos2-pos1-1)
summ+=sys.getsizeof(dist)


print('Первая буква номер',pos1,'Вторая буква номер',pos2,'Между ними',dist,'символ(-ов)')

print(summ) #136

#64-разрядная система, Windows,python 3.6.5