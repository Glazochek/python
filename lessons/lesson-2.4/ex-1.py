"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit

num = [1, 3, 2, 4, 5, 6, 7, 8]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [e for e in nums if e % 2 == 0]

# я убрал range и len, чтобы сократить время
# так же, использую cписковое включение

# результат давольно неплох - на 0.00225 секунд быстрее:
# 0.006895788999999999 - func_1
# 0.004649245999999999 - func_2


print(timeit('func_1(num)', setup='from __main__ import func_1, num', number=10000), '- func_1')
print(timeit('func_2(num)', setup='from __main__ import func_2, num', number=10000), '- func_2')
