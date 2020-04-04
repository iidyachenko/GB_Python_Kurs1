class Car:
    def __init__(self, color, name, speed=0, is_police=False):
        self.color = color
        self.name = name
        self.speed = int(speed)
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"Машина {self.name} поехала, скорость: {self.speed}км\ч")

    def stop(self):
        self.speed = 0
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Машина {self.name} едет, со скоростью: {self.speed}км\ч")


class TownCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, speed=0, is_police=False)

    def show_speed(self):
        print(f"Машина {self.name} едет, со скоростью: {self.speed}км\ч")
        if self.speed >= 60:
            print("Машина едет с превышением скорости")


class WorkCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, speed=0, is_police=False)

    def show_speed(self):
        print(f"Машина {self.name} едет, со скоростью: {self.speed}км\ч")
        if self.speed >= 40:
            print("Машина едет с превышением скорости")


class SportCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, speed=0, is_police=False)

    def show_speed(self):
        print(f"Машина {self.name} едет, со скоростью: {self.speed}км\ч")
        if self.speed >= 140:
            print("Машина едет с превышением скорости")


class PoliceCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(color, name, speed=0, is_police=True)


townCar = TownCar("red", "Lada")
townCar.go(70)
townCar.show_speed()
townCar.turn("Направо")

workCar = WorkCar("green", "Bus")
workCar.go(30)
workCar.show_speed()
workCar.turn("Налево")

sportCar = SportCar("red", "Ferrari")
sportCar.go(100)
sportCar.show_speed()
sportCar.turn("Налево")

policeCar = PoliceCar("blue", "UAZ")
policeCar.go(150)
policeCar.show_speed()
policeCar.turn("Направо")
print(policeCar.is_police)