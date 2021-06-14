# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
from random import shuffle, randint


def merge(left_arr: list, right_arr: list) -> list:
    """Сортируем и объединяем"""
    sorted_arr = []
    idx_left = idx_right = 0
    while idx_left < len(left_arr) and idx_right < len(right_arr):  # Пока указатели не достигли конца любого списка
        if left_arr[idx_left] <= right_arr[idx_right]:  # Если слева меньше, чем справа
            sorted_arr.append(left_arr[idx_left])  # Кидаем левый элемент в отсортированный список
            idx_left += 1
        else:
            sorted_arr.append(right_arr[idx_right])  # Кидаем правый элемент в отсортированный список
            idx_right += 1  #

    if idx_left == len(left_arr):  # Если достигли конца левого массива
        sorted_arr.extend(right_arr[idx_right:])  # Докинули что осталось из правого
    elif idx_right == len(right_arr):  # и наоборот
        sorted_arr.extend(left_arr[idx_left:])  # докинули что осталось из левого

    return sorted_arr


def merge_sort(array: list) -> list:
    """Разбиваем и сортируем"""
    if len(array) < 2:
        return array

    mid = int(len(array) / 2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


array = [randint(0, 50) for _ in range(100)]
print(array)
print(merge_sort(array))
