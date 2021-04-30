class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return divider / denominator
        except:
            return f'Деление на ноль недопустимо'


div = DivisionByNull(10, 100)

print(DivisionByZero.divide_by_null(10, 0))
print(DivisionByZero.divide_by_null(10, 0.1))
print(div.divide_by_zero(100, 0))
