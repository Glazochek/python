"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

import collections

ask = int(input('Введите количество предприятий для расчета прибыли:'))
n = ask
asm = 0
sm = 0
d = collections.defaultdict(int)
while n != 0:
    ask2 = input('Введите название предприятия:')
    ask3 = input('через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала):')
    for r in ask3.split():
        sm += int(r)
    d[ask2] = sm
    asm += sm
    sm = 0
    n -= 1

sr = asm / ask
print(f'Средняя годовая прибыль всех предприятий: {sr}')
for dck in d.keys():
    if d[dck] > sr:
        print(f'Предприятия, с прибылью выше среднего значения: {dck}')
    elif d[dck] < sr:
        print(f'Предприятия, с прибылью ниже среднего значения: {dck}')
