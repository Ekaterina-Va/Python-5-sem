class Complex():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y,
                       self.x * other.y + self.y * other.x)

    def __truediv__(self, other):
        return Complex((self.x * other.x + self.y * other.y) / (other.x ** 2 + other.y ** 2),
                       (-self.x * other.y + self.y * other.x) / (other.x ** 2 + other.y ** 2))

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)


A = Complex(1, 1)
B = Complex(2, 2)
C = Complex()
D = A * B

print(abs(C))
print(D.x, '+', D.y, 'i')
abs(D)