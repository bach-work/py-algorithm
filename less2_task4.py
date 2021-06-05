# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


size = int(input('Введите размер последовательности'))
element = 1
my_summ = 0
for i in range(size):
    summ += element
    element /= -2
print(my_summ)