class MyComplex:

    def __init__(self, x, y):
        self.real = x
        self.image = y

    def __str__(self):
        return f"{self.real} + {self.image}j"

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.image + other.image)

    def __mul__(self, other):
        return MyComplex(self.real * other.real - self.image * other.image, self.real * other.image + other.real * self.image)


cnum_1 = MyComplex(1, 5)
print(cnum_1)
cnum_2 = MyComplex(2, 10)
print(cnum_1)
print(cnum_1 + cnum_2)
print(cnum_1 * cnum_2)