from math import ceil


class Ceil:

    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return Ceil(self.count + other.count)

    def __sub__(self, other):
        if self.count < other.count:
            print("Во втором объекте клеток больше, вычитание невозможно!")
        else:
            return Ceil(self.count - other.count)

    def __mul__(self, other):
        return Ceil(self.count + other.count)

    def __truediv__(self, other):
        return Ceil(self.count // other.count)

    def make_order(self, n):
        n = int(n)
        print_ceils = self.count
        for _ in range(0, ceil(self.count / n)):
            if print_ceils / n >= 1:
                print('*' * (int(n)))
            else:
                print('*' * (print_ceils % n))
            print_ceils -= n


ceil_1 = Ceil(12)
ceil_1.make_order('5')
