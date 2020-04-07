from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, title, v):
        super().__init__(title)
        self.V = float(v)

    @property
    def consumption(self):
        return self.V/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, title, h):
        super().__init__(title)
        self.H = float(h)

    @property
    def consumption(self):
        return 2 * self.H + 0.3


coat = Coat("Пальто", 20)
print(f"Расход ткани на {coat.title} = {coat.consumption:0.2f}")

suit = Suit("Костюм", 1.8)
print(f"Расход ткани на {suit.title} = {suit.consumption:0.2f}")