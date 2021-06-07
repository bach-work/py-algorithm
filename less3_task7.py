# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

input_list = [5, 8, 2, 1, 1, 5]  # Для теста

min1 = input_list[0]
min2 = input_list[1]
for el in input_list[2:]:
    if el < min1:
        min1 = el
    elif el < min2:
        min2 = el

print('Два наименьших часла: {}, {}'.format(min1, min2))
