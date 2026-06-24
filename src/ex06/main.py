from common import Vector
from ex06.cross_product import cross_product


def test_cross_product():
    print("Test cross product")
    u = Vector([2, 3, 1])
    v = Vector([4, 1, 5])
    print(f"{cross_product(u, v)}")
    print()

    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])
    print(f"{cross_product(u, v)}")
    print()


def main():
    test_cross_product()


if __name__ == "__main__":
    main()
