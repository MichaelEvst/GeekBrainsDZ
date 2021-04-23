class Stationary:
    def __init__(self, title):
        self.title = tittle

    @staticmethod
    def draw():
        print("Запуск отрисовки")


class Pen(Stationary):
    @staticmethod
    def draw():
        print('pen')


class Pencil(Stationary):
    @staticmethod
    def draw():
        print('pencil')


class Handle(Stationary):
    @staticmethod
    def draw():
        print('handle')
