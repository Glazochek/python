"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from timeit import timeit


def median(d):
    for i in range(len(d) // 2):
        d.remove(max(d))
        d.remove(min(d))
    return d[0]


print(timeit('median([i for i in range(2*10+1)])', setup='from __main__ import median', number=100))
print(timeit('median([i for i in range(2*100+1)])', setup='from __main__ import median', number=100))
print(timeit('median([i for i in range(2*1000+1)])', setup='from __main__ import median', number=100))

# 0.0008923999999999981
# 0.0363822
# 3.257903
