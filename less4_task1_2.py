# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import cProfile


def find_rec(n: int, res_dict: dict = None):
    if res_dict is None:
        res_dict = {"even": 0, "odd": 0}
    if n == 0:
        return res_dict
    res_dict['even' if (n % 10) % 2 else 'odd'] += 1
    return find_rec(n // 10, res_dict)

# python -m timeit -n 1000 -s "import less4_task1_2" "less4_task1_2.find_rec(34560)
# 1000 loops, best of 5: 1.6 usec per loop
# python -m timeit -n 1000 -s "import less4_task1_2" "less4_task1_2.find_rec(345603456034560)"
# 1000 loops, best of 5: 4.92 usec per loop
# python -m timeit -n 1000 -s "import less4_task1_2" "less4_task1_2.find_rec(345603456034560345603456034560345603456034560345603456034560345603456034560)"
# 1000 loops, best of 5: 25.5 usec per loop

# cProfile.run('find_rec(34560)'):
# 6/1    0.001    0.000    0.001    0.001 less4_task1_2.py:6(find_rec)
# cProfile.run('find_rec(345603456034560)')
# 16/1    0.000    0.000    0.000    0.000 less4_task1_2.py:6(find_rec)
# cProfile.run('find_rec(345603456034560345603456034560345603456034560345603456034560345603456034560)')
# 76/1    0.000    0.000    0.000    0.000 less4_task1_2.py:6(find_rec)
