class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        return Complex(self.left - other.left, self.right - other.right)

    def __gt__(self, other):
        return Complex(self.left > other.left, self.right > other.right)

    def __radd__(self, other):
        return Complex(self.left + other.left, self.right)

    def __mul__(self, other):
        return Complex(self.left * other.left, self.right * other.right)

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __iadd__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'


c = Complex(2, 5)
d = Complex(5, 5)
f = Complex(2, 3)
d += Complex(2, 5)

print(d)
