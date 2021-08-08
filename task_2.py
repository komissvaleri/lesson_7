
from abc import ABC

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumtion(self):
        return f'Сумма затраченной ткани = {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

class Coat(Clothes):
    def consumtion(self):
        return f'Для пошива пальто нужно {self.param / 6.5 + 0.5 :.2f} ткани'

class Costume(Clothes):
    def consumtion(self):
        return f'Для пошива костюма нужно {2 * self.param + 0.3 :.2f} ткани'

coat = Coat(1)
costume = Costume(1)
print(coat.consumtion())
print(costume.consumtion())

