'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''

from collections import namedtuple
Company = namedtuple('Сompany', 'name quarter1 quarter2 quarter3 quarter4 average')
n = int(input('Введите количество компаний '))
all_companies = []
lower = []
higher = []

for i in range(n):
    name = input('Введите название фирмы: ')
    quarter1 = int(input('Прибыль за 1ый квартал: '))
    quarter2 = int(input('Прибыль за 2ый квартал: '))
    quarter3 = int(input('Прибыль за 3ий квартал: '))
    quarter4 = int(input('Прибыль за 4ый квартал: '))
    average = (quarter1 + quarter2 + quarter3 + quarter4) / 4
    this_company = Company(name, quarter1, quarter2, quarter3, quarter4, average)
    all_companies.append(this_company)

summa = 0

for i in range(n):
    summa += (all_companies[i].quarter1 + all_companies[i].quarter2 +
                    all_companies[i].quarter3 + all_companies[i].quarter4)

total_average = summa / (4 * n)
print('Средняя прибыль равна: {}'.format(total_average))

for i in range(n):
    if all_companies[i].average < total_average:
        lower.append(all_companies[i].name)
    else:
        higher.append(all_companies[i].name)

print(f'Прибыль меньше среднего у компаний: - {lower}, Прибыль больше среднего у компаний - {higher}')