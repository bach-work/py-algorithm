# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
import random
from random import shuffle

array = [i for i in range(2 * 25 + 1)]
shuffle(array)
print(array)


def find_med(array: list, med_index=None) -> int:
    if med_index is None:  # Если не указан индекс медианы, значит его надо проинициализировать
        return find_med(array, len(array) / 2 + 1)  # Вызываем себя и берем середину массива

    pivot = random.choice(array)  # Берем случайное опорное значение
    left_list = [el for el in array if el < pivot]  # список тех, кто меньше
    right_list = [el for el in array if el > pivot]  # список тех, кто больше
    pivot_count = array.count(pivot)  # количество опорных значений

    if med_index < len(left_list):  # если медиана находится в левом списке
        # там и ищем
        return find_med(left_list, med_index)
    elif med_index >= len(left_list) + pivot_count:  # если медиана в правом списке
        # ищем в правом, сдвигая медиану на размер левого списка и количество опорных элементов
        return find_med(right_list, med_index - len(left_list) - pivot_count)
    else:  # если ее нет ни там, ни там, значит нашли ее в pivot
        return pivot  # Алилуйя! Вот медиана!


print(find_med(array))
