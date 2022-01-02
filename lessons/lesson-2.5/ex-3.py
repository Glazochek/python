"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""

from collections import deque
from timeit import timeit

dq = deque()
ls = list()

# 1) -------------------------------------------------{ append }--------------------------------------------------------

print(timeit("""
for i in range(100):
    dq.append(i)""", setup='from __main__ import dq', number=10000), 'dq.append(i)')

print(timeit("""
for i in range(100):
    ls.append(i)""", setup='from __main__ import ls', number=10000), 'ls.append(i)')

# 0.00528441 dq.append(i)
# 0.005370311999999995 ls.append(i)
# здесь по времении все одинаково

print('\nравны\n')

# --------------------------------------------------{ pop }-------------------------------------------------------------

print(timeit("""
for i in range(100):
    dq.pop()""", setup='from __main__ import dq', number=10000), 'dq.pop()')

print(timeit("""
for i in range(100):
    ls.pop()""", setup='from __main__ import ls', number=10000), 'ls.pop()')

# 0.032367512000000015 dq.pop()
# 0.033634143000000005 ls.pop()
# оба равны по времяни

print('\nравны\n')

# ----------------------------------------------------{ extend }--------------------------------------------------------

print(timeit("""
for i in range(1):
    dq.extend([3, 5 ,6])""", setup='from __main__ import dq', number=10000), 'dq.extend([3, 5 ,6])')

print(timeit("""
for i in range(1):
    ls.extend([3, 5 ,6])""", setup='from __main__ import ls', number=10000), 'ls.extend([3, 5 ,6])')

# 0.002706774000000023 dq.extend([3, 5 ,6])
# 0.002302293000000011 ls.extend([3, 5 ,6])
# примерно равны
print('\nравны\n')

# 2) ---------------------------------------{ append vs insert }--------------------------------------------------------

# здесь лист настолько проигрывает, что мне пришлось снизить колличество повторений в цикле

print(timeit("""
for i in range(1):
    dq.appendleft(i)""", setup='from __main__ import dq', number=10000), 'dq.appendleft(i)')

print(timeit("""
for i in range(1):
    ls.insert(0, i)""", setup='from __main__ import ls', number=10000), 'ls.insert(0, i)')

# 0.0017385249999999908 dq.appendleft(i)
# 20.19975515 ls.insert(0, i)
# deque быстрее
print('\ndeque быстрее\n')

# ----------------------------------------------{ popleft vs remove }---------------------------------------------------

print(timeit("""
for i in range(1):
    dq.popleft()""", setup='from __main__ import dq', number=10000), 'dq.popleft()')

print(timeit("""
for i in range(1):
    ls.pop(0)""", setup='from __main__ import ls', number=10000), 'ls.pop(0)')

# 0.0016833429999998373 dq.popleft()
# 20.519805019 ls.pop(0)
# deque быстрее
print('\ndeque быстрее\n')

# ------------------------------------------{ extendleft vs insert  }---------------------------------------------------

print(timeit("""
for i in range(1):
    dq.extendleft([3, 5 ,6])""", setup='from __main__ import dq', number=10000), 'dq.extendleft([3, 5 ,6])')

print(timeit("""
for i in range(1):
    ls.insert(0, [3, 5 ,6])""", setup='from __main__ import ls', number=10000), 'ls.insert(0, [3, 5 ,6])')

# 0.0024931559999998854 dq.extendleft([3, 5 ,6])
# 19.901009607 ls.insert(0, [3, 5 ,6])
# deque быстрее
print('\ndeque быстрее\n')

# 3) ------------------------------------------{ получение елемента }---------------------------------------------------

print(timeit("""
for i in range(100):
    dq[i]""", setup='from __main__ import dq', number=10000), 'dq[i]')

print(timeit("""
for i in range(100):
    ls[i]""", setup='from __main__ import ls', number=10000), 'ls[i]')

# 0.02620416800000669 dq[i]
# 0.020079793000000734 ls[i]
# list быстрее
print("\nlist быстрее\n")

# deque показал себя очень хорошо, в любой операции, кроме получения елемента выигрывает список
# действительно deque подойдет "что-то быстро дописать или вытащить"
# "быстрый случайный доступ" тоже сказано верно, здесь лист победил
