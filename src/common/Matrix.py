from __future__ import annotations
from typing import TypeVar, Generic
from xmlrpc.client import Boolean

from .Vector import Vector

K = TypeVar("K", int, float)


class Matrix(Generic[K]):
    def __init__(self, rows: list[list[K]]):
        if not rows:
            raise ValueError("Matrix cannot be empty")

        width = len(rows[0])

        if width == 0:
            raise ValueError("Matrix rows cannot be empty")

        for row in rows:
            if len(row) != width:
                # raise MatrixSizeError(row, rows[0])
                raise ValueError(row, rows[0])

        self._rows: list[list[K]] = rows

        self._shape = (len(self._rows), len(self._rows[0]))

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
    def rows(self) -> list[list[K]]:
        return self._rows

    @rows.setter
    def rows(self, rows: list[list[K]]) -> None:
        self._rows = rows

    def is_square(self) -> Boolean:
        return self.n_rows == self.n_cols

    def mul_vec(self, vec: Vector[K]) -> Vector[K]:
        if self.n_cols != vec.length:
            raise ValueError("Column - Lines not equal")
        result: list[K] = []
        for row in self.rows:
            result.append(Vector(row).dot(vec))

        return Vector(result)

    def mul_mat(self, mat: Matrix[K]) -> Matrix[K]:
        if self.n_cols != mat.n_rows:
            raise ValueError("Matrix columns and rows are not compatible")

        columns = list(zip(*mat.rows))
        result: list[list[K]] = []

        for row in self.rows:
            result_row: list[K] = []

            for column in columns:
                value = Vector(row).dot(Vector(list(column)))
                result_row.append(value)

            result.append(result_row)

        return Matrix(result)

    def trace(self) -> K:
        if not self.is_square():
            raise ValueError("Trace is only defined for square matrices")

        result: K = self.rows[0][0]

        for index in range(1, self.n_rows):
            result += self.rows[index][index]

        return result

    def transpose(self) -> Matrix[K]:
        columns = [list(column) for column in zip(*self.rows)]
        return Matrix(columns)
