from common import Vector
from ex05.angle_cos import angle_cos


def test_angle_cos():
    print("Test angle cos")
    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])
    print(f"{angle_cos(u, v):.9f}")
    print()


def main():
    test_angle_cos()


if __name__ == "__main__":
    main()
