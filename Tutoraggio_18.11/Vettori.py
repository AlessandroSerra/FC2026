from numpy import sqrt as np_sqrt
from numpy import acos as np_acos

class Vec2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_somma = self.x + other.x
        y_somma = self.y + other.y
        risultato = Vec2D(x_somma, y_somma)
        return risultato

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __str__(self):
        return f"Vec2D({self.x}, {self.y})"

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, scalare):
        return Vec2D(scalare * self.x, scalare * self.y)

    def __rmul__(self, scalare):
        return self * scalare

    def __truediv__(self, scalare):
        return self * (1 / scalare)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return np_sqrt(self @ self)

    def angolo_tra(self, other):
        # theta = acos(v @ w / (|v| * |w|))
        norm_prod = abs(self) * abs(other)
        costheta = self @ other / norm_prod
        return np_acos(costheta)

