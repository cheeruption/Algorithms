a = input('Введите две латинские буквы через запятую:')

from re import findall

pos1 =ord(findall('^\w',a)[0])-96
pos2 =ord(findall('\w$',a)[0])-96
dist = abs(pos2-pos1-1)

print('Первая буква номер',pos1,'Вторая буква номер',pos2,'Между ними',dist,'символ(-ов)')