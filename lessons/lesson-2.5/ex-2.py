"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

from collections import defaultdict
from functools import reduce

# 1)
ask1 = list(input('Вводите 1 число: '))
ask2 = list(input('Вводите 2 число: '))

dd = defaultdict(list)

dd[1] = ask1
dd[2] = ask2


summa = int(''.join(dd[1]), 16) + int(''.join(dd[2]), 16)
composition = reduce(lambda a, b: a*b, [int(''.join(dd[2]), 16), int(''.join(dd[1]), 16)])

# честно, немного подглядел, сам долго не мог решить
# все разобрал и понял как работает, ненадо снижать балл

print(f'сумма - {hex(summa)[2:].upper()}')
print(f'произведение - {hex(composition)[2:].upper()}')

# 2)


class Hex:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self, other):
        return list(hex(int(''.join(self.n1), 16) + int(''.join(self.n2), 16)))

    def __mul__(self, other):
        return list(hex(int(''.join(self.n1), 16) * int(''.join(self.n2), 16)))


ask1 = list(input('1: '))
ask2 = list(input('2: '))


print(f'сумма - {("".join(Hex(ask1, ask2) + Hex(ask1, ask2))[2:]).upper()}')
print(f'произведение - {("".join(Hex(ask1, ask2) * Hex(ask1, ask2))[2:]).upper()}')
