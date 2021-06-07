# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

rows = 10
columns = 6
rand_max = 100

table = [[randint(0, rand_max + 1) for _ in range(columns+1)] for _ in range(rows+1)]
print('\n'.join(list(map(str, table))))

max_el = 0
for column in range(columns):
    min_el = rand_max
    for row in range(rows):
        if table[row][column] < min_el:
            min_el = table[row][column]
    if max_el < min_el:
        max_el = min_el

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_el}')
