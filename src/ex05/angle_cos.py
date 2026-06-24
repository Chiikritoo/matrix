from common import Vector


def angle_cos(u: Vector, v: Vector) -> float:
    return u.dot(v) / (u.norm() * v.norm())
