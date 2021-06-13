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


def gen_company(n: str) -> Company:
    return Company(name=n, p1=randint(3000, 6000), p2=randint(3000, 6000),
                   p3=randint(3000, 6000), p4=randint(3000, 6000))


company_list = []
count = int(input('Введите количество компаний: '))
print('-' * 30)
while len(company_list) < count:
    name = input('Введите название компании: ')
    p1 = int(input('Введите доход в первый квартал: '))
    p2 = int(input('Введите доход во второй квартал: '))
    p3 = int(input('Введите доход в третий квартал: '))
    p4 = int(input('Введите доход в четвертый квартал: '))
    company_list.append(Company(name, p1, p2, p3, p4))
    print('-' * 30)

# --------- Если лень вводить руками, закомменть строки 21 - 30, а нижнее открой ------------------------
# company_list = [gen_company('Иллюзион'), gen_company('Киномакс'),
#                 gen_company('Юность'), gen_company('Пролетарий')]

average = reduce(lambda prev, curr: prev + curr, [sum([c.p1, c.p2, c.p3, c.p4]) for c in company_list]) \
          / len(company_list)

print(f'Средняя прибыль: {average}')
print(f'Прибыль выше среднего: {", ".join([c.name for c in company_list if sum([c.p1, c.p2, c.p3, c.p4]) > average])}')
print(f'Прибыль ниже среднего: {", ".join([c.name for c in company_list if sum([c.p1, c.p2, c.p3, c.p4]) < average])}')
