class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(self.title, "Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, '\033[94m' + "Отрисовка ручкой" + '\033[0m')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, '\033[92m' + '\033[91m' + "Отрисовка карандашом" + '\033[0m')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(self.title, '\033[1m' + "Отрисовка маркером")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()