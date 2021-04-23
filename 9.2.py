class Road:
    THINKLESS_CM = 5
    SQUARE_METER_MASS = 25


    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculator(self):
        return self._width * self._length * self.SQUARE_METER_MASS * self.THINKLESS_CM


if __name__ == '__main__':
    road = Road(250,10)
    print(f'{road.mass_calculator() / 1000} тонн')
