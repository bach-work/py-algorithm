# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random
import timeit
from functools import partial


def bubble_sort(array: list):
    """Сортировка из урока"""
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


def bubble_sort2(array: list):
    """Улучшили, заменив while на for"""
    for n in range(1, len(array)):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


def gen_and_sort(sort_func, size: int) -> None:
    """Генерирует массив и сортирует его функцией sort_func"""
    array = [random.randint(-100, 100) for i in range(size)]
    print(f'Исходный массив: {array}')
    sort_func(array)
    print(f'После сортировки: {array}')


gen_and_sort(bubble_sort, 10)
gen_and_sort(bubble_sort2, 10)

# print(timeit.Timer(partial(bubble_sort, [random.randint(-100, 100) for i in range(1000)])).repeat(5, 100))
# print(timeit.Timer(partial(bubble_sort2, [random.randint(-100, 100) for i in range(1000)])).repeat(5, 100))
# [3.85, 3.71, 3.66, 3.65, 3.68]  <- Обычная
# [3.69, 3.65, 3.80, 3.66, 3.64]  <- через for
# Не скажу, что сильно улучшили. Ну прям такое...
