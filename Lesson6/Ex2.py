# Задание два. Создание класса дорога и расчет массы асфальта


class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, depth):
        return self._length * self._width * depth * 25


length = int(input("Введите длину дороги: "))
width = int(input("Введите ширину дороги: "))
depth = int(input("Введите толщину асфальта: "))
road = Road(length=length, width=width)
print("Масса асфальта: ", road.mass(5)/1000,"тонн")
