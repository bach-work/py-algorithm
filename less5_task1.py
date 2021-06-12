# 1. Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
import copy
from collections import namedtuple
from functools import reduce
from random import randint

# Описание компании. p1, p2, p3, p4 - прибыль в соответсвующий квартал
Company = namedtuple('Company', ['name', 'p1', 'p2', 'p3', 'p4'])

company_list = []
count = int(input('Введите количество компаний: '))
while len(company_list) < count:
    c = Company
    c.name = input('Введите название компании: ')
    c.p1 = int(input('Введите доход в первый квартал: '))
    c.p2 = int(input('Введите доход во второй квартал: '))
    c.p3 = int(input('Введите доход в третий квартал: '))
    c.p4 = int(input('Введите доход в четвертый квартал: '))
    company_list.append(copy.deepcopy(c))

# company_list.append(Company)
# c = company_list[len(company_list) - 1]

# company_list = [Company(name='Иллюзион',
#                         p1=randint(3000, 6000), p2=randint(3000, 6000),
#                         p3=randint(3000, 6000), p4=randint(3000, 6000)),
#                 Company(name='Киномакс',
#                         p1=randint(3000, 6000), p2=randint(3000, 6000),
#                         p3=randint(3000, 6000), p4=randint(3000, 6000)),
#                 Company(name='Юность',
#                         p1=randint(3000, 6000), p2=randint(3000, 6000),
#                         p3=randint(3000, 6000), p4=randint(3000, 6000)),
#                 Company(name='Пролетарий',
#                         p1=randint(3000, 6000), p2=randint(3000, 6000),
#                         p3=randint(3000, 6000), p4=randint(3000, 6000))
#                 ]

for c in company_list:
    print(c.name, c.p1, c.p2, c.p3, c.p4)

average = reduce(lambda prev, curr: prev + curr, [sum([c.p1, c.p2, c.p3, c.p4]) for c in company_list]) \
          / len(company_list)

print(f'Средняя прибыль: {average}')
print(f'Прибыль выше среднего: {", ".join([c.name for c in company_list if sum([c.p1, c.p2, c.p3, c.p4]) > average])}')
print(f'Прибыль ниже среднего: {", ".join([c.name for c in company_list if sum([c.p1, c.p2, c.p3, c.p4]) < average])}')
