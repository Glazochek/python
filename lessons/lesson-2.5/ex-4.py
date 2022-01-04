"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

ordd = OrderedDict()
d = dict()


# использовать OrderedDict в Python 3.6 не имеет смысла, в более поздних версиях обычный словарь
# не поддерживал порядок вставки элементов, для этого и создали OrderedDict и тогда он имел смысл
# сейчас, уже обычный словарь потдерживает порядок


# -----------------------------------------{ ordd[i] = 0 vs  d[i] = i }-------------------------------------------------

print(timeit("""
for i in range(1000):
    ordd[i] = i""", setup='from __main__ import ordd', number=10000), 'ordd[i] = 0')

print(timeit("""
for i in range(1000):
    d[i] = i""", setup='from __main__ import d', number=10000), 'd[i] = 0')

# 0.6324601270000001 ordd[i] = 0
# 0.41975592399999995 d[i] = 0
# Dict быстрее

# ------------------------------------{ ordd.move_to_end vs d.pop(i), d[i] = i }----------------------------------------

print(timeit("""
for i in range(1000):
    ordd.move_to_end(i)""", setup='from __main__ import ordd', number=100), 'ordd.move_to_end(i)')

print(timeit("""
for i in range(1000):
    d.pop(i)
    d[i] = i""", setup='from __main__ import d', number=100), 'd.pop(i), d[i] = i')

# 0.006353922000000178 ordd.move_to_end(i)
# 0.009797692000000024 d.pop(i), d[i] = i
# OrderedDict быстрее

# ------------------------------------------------{ popitem }-----------------------------------------------------------


def f1():
    for i in range(10):
        ordd.popitem(True)


def f2():
    for i in range(10):
        d.popitem()


print(timeit("""f1
""", setup='from __main__ import ordd, f1', number=100), 'ordd.popitem()')

print(timeit("""f2
""", setup='from __main__ import d, f2', number=100), 'd.popitem()')

# 1.4230000000559073e-06 ordd.popitem()
# 1.1380000000116297e-06 d.popitem()
# обычный словарь быстрее

# вывод:
# OrderedDict абсолютный победитель в удаление пар, быстро перемещает эелементы в начало словаря
# так же OrderedDict дает четко понять, что нам важен порядок
# есть свои собственные методы, к примеру - move_to_end()
# подходит для того чтобы что-то быстренько удалить или переместить
