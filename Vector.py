from __future__ import annotations

class Vector:
    def __init__(self, numbers: list) -> None:
        self._n: list = numbers

    def __str__(self) -> str:
        return str(self._n)

    def __repr__(self) -> str:
        return str(self._n)

    @property
    def n(self) -> list:
        return self._n

    @n.setter
    def n(self, numbers: list) -> None:
        self._n: list = numbers

    def add(self, other: Vector) -> None:
        if len(self.n) != len(other.n):
            raise ValueError(f"Vectors have not the same length ({self.n} - {other.n})")
        self.n = [n1 + n2 for n1, n2 in zip(self.n, other.n)]

    def sub(self, other: Vector) -> None:
        if len(self.n) != len(other.n):
            raise ValueError(f"Vectors have not the same length ({self.n} - {other.n})")
        self.n = [n1 - n2 for n1, n2 in zip(self.n, other.n)]

    def scl(self, scalar: int) -> None:
        self.n = [scalar * component for component in self.n]
