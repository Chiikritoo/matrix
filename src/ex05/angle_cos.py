from common import Vector


def angle_cos(u: Vector, v: Vector) -> float:
    u_norm = u.norm()
    v_norm = v.norm()

    if u_norm == 0 or v_norm == 0:
        raise ValueError("Cosine is undefined for zero vectors")

    return u.dot(v) / (u_norm * v_norm)
