#5. ������������ ������ ��� �����. ����������, �� ����� ������ �������� ��� ����� � ������� ����� ���� ��������� ����.
import sys
from re import findall


summ=0
a = input('������� ��� ��������� ����� ����� �������:') #����� "d,g"

summ+=sys.getsizeof(a)

pos1 =ord(findall('^\w',a)[0])-96
summ+=sys.getsizeof(pos1)

pos2 =ord(findall('\w$',a)[0])-96
summ+=sys.getsizeof(pos2)

dist = abs(pos2-pos1-1)
summ+=sys.getsizeof(dist)


print('������ ����� �����',pos1,'������ ����� �����',pos2,'����� ����',dist,'������(-��)')

print(summ) #136

#64-��������� �������, Windows,python 3.6.5