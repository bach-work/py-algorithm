# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import cProfile


# ---- Через преобразование к строке  ----
def find_str(num: int) -> dict:
    res_dict = {"even": 0, "odd": 0}
    for n in list(str(num)):
        res_dict["even" if int(n) & 1 == 0 else "odd"] += 1
    return res_dict

# python -m timeit -n 1000 -s "import less4_task1_3" "less4_task1_3.find_str(34560)
# 1000 loops, best of 5: 1.93 usec per loop
# python -m timeit -n 1000 -s "import less4_task1_3" "less4_task1_3.find_str(345603456034560)
# 1000 loops, best of 5: 4.45 usec per loop
# python -m timeit -n 1000 -s "import less4_task1_3" "less4_task1_3.find_str(345603456034560345603456034560345603456034560345603456034560345603456034560)
# 1000 loops, best of 5: 20 usec per loop

# cProfile.run('find_str(34560)')
# 1    0.000    0.000    0.000    0.000 less4_task1_3.py:7(find_str)
# cProfile.run('find_str(345603456034560)')
# 1    0.000    0.000    0.000    0.000 less4_task1_3.py:7(find_str)
# cProfile.run('find_str(345603456034560345603456034560345603456034560345603456034560345603456034560)')
# 1    0.000    0.000    0.000    0.000 less4_task1_3.py:7(find_str)
