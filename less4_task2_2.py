# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Второй — без использования «Решета Эратосфена».

def get_simple(index):
    def _is_prime_(num: int) -> bool:
        """Проверка числа на простоту"""
        if num % 2 == 0:
            return num == 2
        j = 3
        while j * j <= num and num % j != 0:
            j += 2
        return j * j > num

    counter = 0
    num = 1
    while counter < index:  # Пока недосчитались простых чисел
        num += 1  # Берем следующее
        if _is_prime_(num):  # Проверяем его на простоту
            counter += 1
    return num

# print(get_simple(5))

# python -m timeit -n 100 -s "import less4_task2_2" "less4_task2_2.get_simple(10)"
# 100 loops, best of 3: 6.52 usec per loop
# python -m timeit -n 100 -s "import less4_task2_2" "less4_task2_2.get_simple(50)"
# 100 loops, best of 3: 70.4 usec per loop
# python -m timeit -n 100 -s "import less4_task2_2" "less4_task2_2.get_simple(100)"
# 100 loops, best of 3: 206 usec per loop
# python -m timeit -n 100 -s "import less4_task2_2" "less4_task2_2.get_simple(500)"
# 100 loops, best of 3: 1.91 msec per loop
# python -m timeit -n 100 -s "import less4_task2_2" "less4_task2_2.get_simple(1000)"
# 100 loops, best of 3: 5.58 msec per loop
