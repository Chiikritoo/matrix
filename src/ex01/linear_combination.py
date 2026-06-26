from math import fma
from typing import Sequence, TypeAlias

from common import Vector

Number: TypeAlias = int | float


def linear_combination(
        vectors: Sequence[Vector],
        coefs: Sequence[Number],
) -> Vector:
    if len(vectors) != len(coefs):
        raise ValueError("There must be as many vectors as coefs")

    if not vectors:
        raise ValueError("Vectors cannot be empty")

    size = len(vectors[0].n)
    if any(len(vector.n) != size for vector in vectors):
        raise ValueError("Vectors must have the same size")

    result = [0.0] * size
    for vector, coef in zip(vectors, coefs, strict=True):
        for i, component in enumerate(vector.n):
            result[i] = fma(coef, component, result[i])

    return Vector(result)
