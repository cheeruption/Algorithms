'''3. ������������ �� ���������� ����� �������� �� ������� �������� � ���� ���� � ������� �� �����.
 ��������, ���� ������� ����� 3486, �� ���� ������� ����� 6843.'''

import sys

lst = []
print(sys.getsizeof(lst)) #64 ����� ��� ������ ������ ������� 64 ����

lst = list('3486')
print(sys.getsizeof(lst)) #120 ������ + ������ �� 4 �������� ����������� 120 ���

lst = lst[::-1]
print(sys.getsizeof(lst)) #96 ����� ������ ���������� 96 ��� (������ � 4 ������)

lst = '3486'
print(sys.getsizeof(lst)) #53 ���� "�����" ������ � 4 �������

print(''.join(lst))


#64-��������� �������, Windows, python 3.6.5