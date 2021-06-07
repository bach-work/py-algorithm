# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

# Массив случайных числе размера 10
input_list = [randint(1, 100) for _ in range(11)]
print(input_list)

i_min = 0  # Положение минимального
i_max = 0  # Положение максимального элемента
for pos, value in enumerate(input_list):
    if value < input_list[i_min]:
        i_min = pos
    elif value > input_list[i_max]:
        i_max = pos

# Меняем местами
input_list[i_min], input_list[i_max] = input_list[i_max], input_list[i_min]
print(input_list)


