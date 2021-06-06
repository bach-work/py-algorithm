# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# ---- Через цикл ----
num = abs(int(input('Введите натуральное число: ')))
even = 0  # четный
odd = 0  # нечетный
while num > 0:
    if (num % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f'Четных {even}, нечетных {odd}')


# ---- Через рекурсию ----
def calc(n: int, res: dict):
    if n == 0:
        return res
    res['even' if (n % 10) % 2 else 'odd'] += 1
    return calc(n // 10, res)


res_dict = calc(34560, {'even': 0, 'odd': 0})
print(res_dict.get('even'), dict.get('odd'))
