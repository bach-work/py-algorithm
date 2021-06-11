# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».

def get_simple_erat(n):
    simple_list = []
    sieve = [0, 0]  # Решето
    delta = n  # Окно, на которое будем расширять решето
    while len(simple_list) < n:  # Пока не найдем нужное количество простыъ чисел
        sieve.extend(list(range(len(sieve), len(sieve) + delta)))  # Расширяем решето
        for sieve_value in sieve:
            if sieve_value > 1:
                if sieve_value not in simple_list:
                    simple_list.append(sieve_value)  # Записываем в список пустых чисел
                for j in range(sieve_value + sieve_value, len(sieve), sieve_value):
                    sieve[j] = 0  # Обнуляем не простые

    return simple_list.pop()

# print(get_simple_erat(5))


# python -m timeit -n 100 -s "import less4_task2_1" "less4_task2_1.get_simple_erat(10)"
# 100 loops, best of 3: 13.8 usec per loop
# python -m timeit -n 100 -s "import less4_task2_1" "less4_task2_1.get_simple_erat(50)"
# 100 loops, best of 3: 156 usec per loop
# python -m timeit -n 100 -s "import less4_task2_1" "less4_task2_1.get_simple_erat(100)"
# 100 loops, best of 3: 514 usec per loop
# python -m timeit -n 100 -s "import less4_task2_1" "less4_task2_1.get_simple_erat(500)"
# 100 loops, best of 3: 7.67 msec per loop
# python -m timeit -n 100 -s "import less4_task2_1" "less4_task2_1.get_simple_erat(1000)"
# 100 loops, best of 3: 21.8 msec per loop
