from typing import Sequence, TypeAlias

from common.Vector import Vector

Number: TypeAlias = int | float


def linear_combination(
        vectors: Sequence[Vector],
        coefs: Sequence[Number],
) -> Vector:
    if len(vectors) != len(coefs):
        raise ValueError("There must be as many vectors as coefs")

    for vector, scalar in zip(vectors, coefs):
        vector.scl(scalar)

    result = vectors[0]

    for vector in vectors[1:]:
        result.add(vector)

    return result
