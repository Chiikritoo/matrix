from __future__ import annotations
from typing import TypeVar, Generic

K = TypeVar("K", int, float)


class VectorSizeError(ValueError):
    def __init__(self, v1: Vector, v2: Vector) -> None:
        super().__init__(
            f"Vectors have not the same length ({len(v1.n)} != {len(v2.n)})"
        )


class Vector(Generic[K]):
    def __init__(self, numbers: list[K]) -> None:
        if not numbers:
            raise ValueError("Vector cannot be empty")
        self._n: list[K] = numbers

    def __str__(self) -> str:
        strs = [str(x) for x in self._n]
        width = max(len(s) for s in strs)
        n = len(strs)
        lines = []

        for i, s in enumerate(strs):
            padded = s.center(width)

            if n == 1:
                left, right = "[", "]"
            elif i == 0:
                left, right = "⎡", "⎤"
            elif i == n - 1:
                left, right = "⎣", "⎦"
            else:
                left, right = "⎢", "⎥"

            lines.append(f"{left}{padded}{right}")

            if i < n - 1:
                lines.append(f"⎢{' ' * width}⎥")

        return "\n".join(lines)

    def __repr__(self) -> str:
        return str(self._n)

    @property
    def n(self) -> list[K]:
        return self._n

    @n.setter
    def n(self, numbers: list[K]) -> None:
        self._n = numbers

    def add(self, other: Vector) -> None:
        if len(self.n) != len(other.n):
            raise VectorSizeError(self, other)

        self.n = [n1 + n2 for n1, n2 in zip(self.n, other.n)]

    def sub(self, other: Vector) -> None:
        if len(self.n) != len(other.n):
            raise VectorSizeError(self, other)

        self.n = [n1 - n2 for n1, n2 in zip(self.n, other.n)]

    def scl(self, scalar: K) -> None:
        self.n = [scalar * component for component in self.n]
