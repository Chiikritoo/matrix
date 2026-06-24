from common import Vector


def main():
    print("Test norm")
    v1 = Vector([1, 2, 3])

    print(f"{v1.norm_1()}, {v1.norm():.8f}, {v1.norm_inf()}")
