from __future__ import annotations
from typing import TypeVar, Generic

from common import Vector, VectorSizeError

K = TypeVar("K", int, float)


class Matrix(Generic[K]):
    def __init__(self, rows: list[Vector[K]]):
        if not rows:
            raise ValueError("Matrix cannot be empty")

        width = len(rows[0].n)

        if width == 0:
            raise ValueError("Matrix rows cannot be empty")

        for row in rows:
            if len(row.n) != width:
                raise VectorSizeError(row, rows[0])

        self._rows: list[Vector[K]] = rows

        self._shape = (len(self._rows), len(self._rows[0].n))

    def __str__(self) -> str:
        return str(self.rows)

    def __repr__(self) -> str:
        return str(self.rows)

    @property
    def n_rows(self) -> int:
        return self._shape[0]

    @property
    def n_cols(self) -> int:
        return self._shape[1]

    @property
    def rows(self) -> list[Vector[K]]:
        return self._rows

    @rows.setter
    def rows(self, rows: list[Vector[K]]) -> None:
        self._rows = rows

    def mul_vec(self, vec: Vector[K]) -> Vector[K]:
        if self.n_cols != len(vec.n):
            raise ValueError("Column - Lines not equal")
        result: list[K] = []
        for row in self.rows:
            result.append(vec.dot(row))

        return Vector(result)

    def mul_mat(self, mat: Matrix[K]) -> Matrix[K]:
        if self.n_rows != len(mat.rows[0].n):
            raise ValueError("Column - Lines not equal")

        # TODO: finish mul_mat
        return Matrix([])
