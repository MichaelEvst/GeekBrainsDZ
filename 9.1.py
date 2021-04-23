from time import sleep


class TrafficLight:
    def __init__(self):
        self._color - None

    def running(self):
        self._color = 'Красный'
        yield self._color
        sleep(7)
        self._color = 'Желтый'
        yield self._color
        sleep(2)
        self._color = 'Зелёный'
        yield self._color
        sleep(5)


if __name__ == '__main__':
    traffic_light = TrafficLight()

    lighst_order = []

    for light in traffic_light.running():
        lighst_order.append(light)
    assert (lights_order == ['Красный', 'Жёлтый', 'Зелёный']), "Светофор неисправен"


