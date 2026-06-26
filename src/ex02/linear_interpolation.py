from math import fma
from typing import TypeAlias

Number: TypeAlias = int | float


def lerp(v0: Number, v1: Number, t: Number) -> float:
    return fma(t, v1 - v0, v0)  # v0 + t * (v1 - v0)
