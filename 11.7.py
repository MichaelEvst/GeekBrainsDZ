class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма n1 и n2 равна')
        return f'n = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение n1 и n2 равно')
        return f'n = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'n = {self.a} + {self.b} * i'


n_1 = ComplexNumber(3, -7)
n_2 = ComplexNumber(5, 4)
print(n_1)
print(n_1 + n_2)
print(n_1 * n_2)
