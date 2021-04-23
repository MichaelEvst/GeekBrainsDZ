class Car:
    def __init__(self, speed, color, name, is_police):
        self.is_police - is_police
        self.name = name
        self.color = color
        self.speed = speed

    @staticmethod
    def drive():
        print('Car started to move')

    @staticmethod
    def stop():
        print('Car stopped')

    @staticmethod
    def turn(to):
        print(f'Car turned {to}')

    def show_speed(self):
        print(f'Current speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if 60 < self.speed:
            print('Speed limit')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if 40 < self.speed:
            print('Speed limit warning')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    work_car = WorkCar(50, 'green', 'Delivery', False)
    work_car.show_speed()
