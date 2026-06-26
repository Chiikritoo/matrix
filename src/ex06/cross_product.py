from math import fma

from common import Vector


def cross_product(u: Vector, v: Vector) -> Vector:
    # x = u.n[1] * v.n[2] - u.n[2] * v.n[1]
    # y = u.n[2] * v.n[0] - u.n[0] * v.n[2]
    # z = u.n[0] * v.n[1] - u.n[1] * v.n[0]
    x = fma(u.n[1], v.n[2], -u.n[2] * v.n[1])
    y = fma(u.n[2], v.n[0], -u.n[0] * v.n[2])
    z = fma(u.n[0], v.n[1], -u.n[1] * v.n[0])
    return Vector([x, y, z])
