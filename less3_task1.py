# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.


num_dict = {x: 0 for x in range(2, 10)}
for i in range(2, 100):
    for key in num_dict.keys():
        if i % key == 0:
            num_dict[key] += 1

# key - число
# value - количество кратных
print(num_dict)
