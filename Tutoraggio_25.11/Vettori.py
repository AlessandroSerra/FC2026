from __future__ import annotations

import numpy as np


class Vec2D:
    """Represent a two-dimensional vector."""

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vec2D(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return self.__repr__()

    def __add__(self, other: Vec2D) -> Vec2D:
        """Return the sum of two vectors."""
        return Vec2D(self.x + other.x, self.y + other.y)

    def __neg__(self) -> Vec2D:
        """Return the opposite vector."""
        return Vec2D(-self.x, -self.y)

    def __sub__(self, other: Vec2D) -> Vec2D:
        """Return the difference between two vectors."""
        return self + (-other)

    def __mul__(self, scalar: float) -> Vec2D:
        """Multiply the vector by a scalar."""
        return Vec2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> Vec2D:
        """Support scalar multiplication from the left."""
        return self * scalar

    def __truediv__(self, scalar: float) -> Vec2D:
        return self * (1 / scalar)

    def __matmul__(self, other: Vec2D) -> float:
        result = self.x * other.x + self.y * other.y
        return result

    def __abs__(self) -> float:
        """Return the Euclidean norm."""
        return np.sqrt(self @ self)

    def unit(self) -> Vec2D:
        return self / abs(self)

    def angle_to(self, other: Vec2D) -> float:
        norm_prod = abs(self) * abs(other)
        cos = self @ other / norm_prod
        return np.acos(cos)


if __name__ == "__main__":
    v = Vec2D()

    print(v)
    print(v.unit()) # 2.236 * 
