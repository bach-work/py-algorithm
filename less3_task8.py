# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
from functools import reduce

my_matrix = list()

while len(my_matrix) < 4:
    row_list = list(map(int, input(str('Строка {} (Введите 4 числа):'.format(len(my_matrix) + 1))).split()))
    row_list.append(reduce(lambda a, b: a + b, row_list))
    my_matrix.append(row_list)

for row in my_matrix:
    print(row)
