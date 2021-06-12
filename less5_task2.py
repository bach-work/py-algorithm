# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import defaultdict, Counter, deque

c = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
     '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def get_key(d: dict, value: int):
    for k, v in d.items():
        if v == value:
            return k
    return 0


def sum_hex(first_str: str, second_str: str) -> str:
    """ Принимает 2 числа в виде строки на вход и складывает их """
    a = deque(first_str)
    b = deque(second_str)

    def _sum_hex_(frst: int, scnd: int) -> list:
        """ Складывает 2 числа и возвращает признак переноса 1 на след разряд """
        res_list = []
        res = frst + scnd
        res_list.append(res > 15)
        if res > 15:
            res = res - 16
        res_list.append(res)
        return res_list

    flag = False
    res_lst = []
    while len(a) > 0 or len(b) > 0:
        first = a.pop() if len(a) else '0'
        second = b.pop() if len(b) else '0'
        f_value = c[first]
        s_value = c[second]
        if flag:
            flag, f_value = _sum_hex_(f_value, 1)  # Добавили 1 к первому числу
        f, sum_value = _sum_hex_(f_value, s_value)  # Сложили 2 числа
        if not flag:
            flag = f
        res_lst.insert(0, get_key(c, sum_value))

    if flag:
        res_lst.insert(0, '1')
    return ''.join(res_lst)


print(sum_hex('A2', 'C4F'))


def mult_hex(first_str: str, second_str: str):
    mult_index = '0'
    res = '0'
    while mult_index != second_str:
        res = sum_hex(res, first_str)
        mult_index = sum_hex(mult_index, '1')
    return res


print(mult_hex('A2', 'C4F'))
