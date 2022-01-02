from abc import ABC, abstractmethod

class Clothes(ABC):
    V = None
    H = None

    @abstractmethod
    def cloth(self):
        pass

class Coat(Clothes):
    def cloth(self, V):
        self.V = V
        cloths = V // 6.5 + 0.5
        print(cloths)
class Costume(Clothes):
    def cloth(self, H):
        self.H = H
        cloths = 2 * H + 0.3
        print(cloths)

Coat().cloth(10)
Costume().cloth(10)
