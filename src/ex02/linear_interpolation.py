from typing import TypeAlias

Number: TypeAlias = int | float


def lerp(v0: Number, v1: Number, t: Number) -> float:
    return v0 + t * (v1 - v0)
