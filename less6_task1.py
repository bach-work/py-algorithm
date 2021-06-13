# 2. Во втором массиве сохранить индексы четных элементов первого массива.

# 6-1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


import sys
from random import randint


def show_size(x, level=0):
    """ Выводит общий размер объекта """
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, objects= {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


input_list = [randint(0, 100) for _ in range(100)]

output = [i for i, el in enumerate(input_list) if el % 2 == 0]  # list 472B
show_size(output)
print('-' * 30)

output = (i for i, el in enumerate(input_list) if el % 2 == 0)  # generator 112B
show_size(output)
print('-' * 30)

output = tuple(i for i, el in enumerate(input_list) if el % 2 == 0)  # tuple 432B
show_size(output)
print('-' * 30)

output = {i: el for i, el in enumerate(input_list) if el % 2 == 0}  # dict 2272B
show_size(output)
print('-' * 30)

# Сводная таблица занимаемой памяти разных итерируемых объектов
# list | generator | tuple | dict |
# --------------------------------|
#  472 |    112    |  432  | 2272 |
# ---------------------------------

# Как мы видим, при хренении одних и тех же итерируемых данных,
# генеротор занимает менльше всего памяти.
# Кортеж хранит данные чуть лучше списка
# Словарю тяжелее всего, но у него другие задачи
