# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

# Массив случайных чисел от 1 до 10 размера 100
input_list = [randint(1, 10) for _ in range(101)]
print(input_list)

# Посчитали в словарь
counter_dict = {}
for x in input_list:
    counter_dict[x] = counter_dict.get(x, 0) + 1
print(counter_dict)

# Ищем максимальное вхождение
max_count = 0
num = 0
for n, count in counter_dict.items():
    if count > max_count:
        max_count = count
        num = n
print('Чаще всего встречается число {} ({} раз)'.format(num, max_count))
