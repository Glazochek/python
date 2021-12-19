class OperationsWithComplexNumbers:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return complex(self.num + other.num)

    def __mul__(self, other):
        return complex(self.num * other.num)


num_1 = OperationsWithComplexNumbers(65)
num_2 = OperationsWithComplexNumbers(78)

print(num_1 * num_2)
print(num_1 + num_2)
