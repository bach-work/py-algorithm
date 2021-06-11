# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import cProfile


# ---- Через цикл ----
def find_loop(num: int) -> dict:
    res_dict = {"even": 0, "odd": 0}
    while num > 0:
        if (num % 10) % 2 == 0:
            res_dict["even"] += 1
        else:
            res_dict["odd"] += 1
        num = num // 10
    return res_dict


# python -m timeit -n 1000 -s "import less4_task1_1" "less4_task1_1.find_loop(34560)
# 1000 loops, best of 5: 1.17 usec per loop
# python -m timeit -n 1000 -s "import less4_task1_1" "less4_task1_1.find_loop(345603456034560)
# 1000 loops, best of 5: 3.38 usec per loop
# python -m timeit -n 1000 -s "import less4_task1_1" "less4_task1_1.find_loop(345603456034560345603456034560345603456034560345603456034560345603456034560)
# 1000 loops, best of 5: 18.7 usec per loop

# cProfile.run('find_loop(34560)') :
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 less4_task1_1.py:7(find_loop)

# cProfile.run('find_loop(345603456034560)') :
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 less4_task1_1.py:7(find_loop)


#cProfile.run('find_loop(345603456034560345603456034560345603456034560345603456034560345603456034560)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 less4_task1_1.py:7(find_loop)

