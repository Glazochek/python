"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

import math
import random
from timeit import timeit


def shell_sort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return array[len(array)//2]


# print(shell_sort([i for i in range(2*10+1)]), [i for i in range(2*10+1)])

print(timeit('shell_sort([random.randint(-100, 100) for i in range(2*10+1)])',
             setup='from __main__ import shell_sort, random', number=100))
print(timeit('shell_sort([random.randint(-100, 100) for i in range(2*100+1)])',
             setup='from __main__ import shell_sort, random', number=100))
print(timeit('shell_sort([random.randint(-100, 100) for i in range(2*1000+1)])',
             setup='from __main__ import shell_sort, random', number=100))

# 0.0043505
# 0.0335097
# 0.4678087
