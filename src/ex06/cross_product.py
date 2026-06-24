from common import Vector


def cross_product(u: Vector, v: Vector) -> Vector:
    x = u.n[1] * v.n[2] - u.n[2] * v.n[1]
    y = u.n[0] * v.n[2] - u.n[2] * v.n[0]
    z = u.n[0] * v.n[1] - u.n[1] * v.n[0]
    return Vector([x, y, z])
