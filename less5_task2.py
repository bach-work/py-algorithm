# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def get_key(d: dict, value: int) -> int:
    """ Возвращает ключ по значению из d """
    for k, v in d.items():
        if v == value:
            return k
    return 0


def sum_hex(first_str: str, second_str: str) -> str:
    """ Принимает 2 числа в виде строки на вход и складывает их """

    def _sum_hex_(frst: str, scnd: str, fl: bool = False) -> list:
        """
        Складывает 2 цифры(принмает как текст),
        возвращает признак переноса 1 на след разряд
        и результат сложения.
        fl - признак того, что есть пенесенная 1
        из предыдущего действия
        """
        res = hex_dict[frst] + hex_dict[scnd] + (1 if fl else 0)
        res_list = [res > 15]
        if res > 15:
            res = res - 16
        res_list.append(get_key(hex_dict, res))
        return res_list

    first_deq = deque(first_str)  # Очередь первого числа
    second_deq = deque(second_str)  # Очередь второго числа
    flag = False  # Флаг переноса единицы
    res_lst = []  # Сюда складывается результат сложения
    while len(first_deq) > 0 or len(second_deq) > 0:
        f_value = first_deq.pop() if len(first_deq) else '0'  # взяли цифру из первого числа
        s_value = second_deq.pop() if len(second_deq) else '0'  # взяли цифру из второго числа
        flag, sum_value = _sum_hex_(f_value, s_value, flag)  # Сложили 2 числа
        res_lst.insert(0, sum_value)

    if flag:  # Если цифры кончились, а перенос стоит
        res_lst.insert(0, '1')  # Добавили 1 в начало числа
    return ''.join(res_lst)


def mult_hex(first_str: str, second_str: str) -> str:
    """
    Принимает 2 числа в виде строки на вход и умножает их.
    Фактически second_str раз складывает их
    """
    mult_index = '0'  # Счетчик сложения
    res = '0'  # Результат сложения
    while mult_index != second_str:
        res = sum_hex(res, first_str) # Прибавили к сумме число
        mult_index = sum_hex(mult_index, '1')  # Увеличили счетчик
    return res


print(sum_hex('A2', 'C4F'))
print(sum_hex('FF', 'FF'))

print(mult_hex('A2', 'C4F'))
print(mult_hex('FF', 'FF'))
