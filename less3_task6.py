# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Массив случайных чисел от 1 до 10 размера 10
from random import randint

input_list = [randint(1, 10) for _ in range(11)]
print(input_list)

# input_list = [5, 8, 2, 2, 1, 5] # Для теста

i_min = 0  # Положение минимального
i_max = 0  # Положение максимального элемента
for pos, value in enumerate(input_list):
    if value < input_list[i_min]:
        i_min = pos
    elif value > input_list[i_max]:
        i_max = pos

# выбираем какой из индексов меньше
left = i_min if i_min <= i_max else i_max
right = i_max if i_max >= i_min else i_min

interval_sum = 0
for el in input_list[left + 1:right]:
    interval_sum += el

print('Сумма элементов, находящихся между минимальным и максимальным элементами: {}'.format(interval_sum))
