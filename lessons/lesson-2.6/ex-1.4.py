from pympler import asizeof
# Основы языка Python: урок 11 задание 7


class OperationsWithComplexNumbersOne:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return complex(self.num + other.num)

    def __mul__(self, other):
        return complex(self.num * other.num)


num_1 = OperationsWithComplexNumbersOne(65)
num_2 = OperationsWithComplexNumbersOne(78)
print(asizeof.asizeof(num_1))  # 240
print(asizeof.asizeof(num_2))  # 240


class OperationsWithComplexNumbersTwo:

    __slots__ = ['num']

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return complex(self.num + other.num)

    def __mul__(self, other):
        return complex(self.num * other.num)


num_1 = OperationsWithComplexNumbersTwo(65)
num_2 = OperationsWithComplexNumbersTwo(78)
print(asizeof.asizeof(num_1))  # 72
print(asizeof.asizeof(num_2))  # 72
# результат на лицо - было 240 стало 72
# использовал __slots__
