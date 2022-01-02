"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно, сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

import random
from timeit import timeit


q = [random.randint(-100, 100) for i in range(10)]


def srt1(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return array


def srt2(array):
    for i in range(len(array) - 1):
        ans = True
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
                ans = False
        if ans is True:
            break
    return array


# print(srt1(q))
# print(srt2(q))

print(timeit('srt1(q)', setup='from __main__ import srt1, q', number=1000), '- srt1')
print(timeit('srt2(q)', setup='from __main__ import srt2, q', number=1000), '- srt2')

# 0.0072318 - srt1
# 0.001200099999999999 - srt2
# в 7 раз быстрее с доработкой
