class Worker:
    def __init__(self, name, surname, income, position):
        self.name = name
        self.surname = surname
        self._income = income
        self.position = position


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    income_dict = {'wage': 50, 'bonus': 35}
    pos = Position('Quentin', 'Tarantino', income_dict, 'Filmmaker')
    print(pos.get_total_income())
    print(pos.get_full_name())
