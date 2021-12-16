"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

d = OrderedDict()
b = dict()


# использовать OrderedDict в Python 3.6 имеет смысл, в более поздних версиях обычный словарь
# не поддерживал порядок вставки элементов, для этого и создали OrderedDict


# -----------------------------------------{ d[i] = 0 vs  b[i] = i }----------------------------------------------------

print(timeit("""
for i in range(1000):
    d[i] = i""", setup='from __main__ import d', number=10000), 'd[i] = 0')

print(timeit("""
for i in range(1000):
    b[i] = i""", setup='from __main__ import b', number=10000), 'b[i] = 0')

# 0.6324601270000001 d[i] = 0
# 0.41975592399999995 b[i] = 0
# Dict быстрее

# ------------------------------------{ move_to_end vs b.pop(i), b[i] = i }---------------------------------------------

print(timeit("""
for i in range(1000):
    d.move_to_end(i)""", setup='from __main__ import d', number=100), 'd.move_to_end(i)')

print(timeit("""
for i in range(1000):
    b.pop(i)
    b[i] = i""", setup='from __main__ import b', number=100), 'b.pop(i), b[i] = i')

# 0.006353922000000178 d.move_to_end(i)
# 0.009797692000000024 b.pop(i), b[i] = i
# OrderedDict быстрее

# ------------------------------------------------{ popitem }-----------------------------------------------------------

print(timeit("""
for i in range(10):
    d.popitem(True)""", setup='from __main__ import d', number=100), 'd.popitem()')

print(timeit("""
for i in range(10):
    b.popitem()""", setup='from __main__ import b', number=100), 'b.popitem()')

# 0.00012942199999987913 d.popitem()
# 7.367099999999738e-05 b.popitem()
# OrderedDict быстрее

# вывод:
# OrderedDict абсолютный победитель в удаление пар, быстро перемещает эелементы в начало словаря
# так же OrderedDict дает четко понять, что нам важен порядок
# есть свои собственные методы, к примеру - move_to_end()
# подходит для того чтобы что-то быстренько удалить или переместить
