class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} и {self.b + other.b}'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} и {self.b * other.a}'


c_1 = ComplexNumber(3, 23)
c_2 = ComplexNumber(9, 12)
print(c_1 + c_2)
print(c_1 * c_2)
