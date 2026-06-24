from common import Vector


def main():
    print("Test dot product")
    v1 = Vector([-1, 6])
    v2 = Vector([3, 2])

    scalar = v1.dot(v2)

    print(v1)
    print(v2)
    print("Dot product:", scalar)
    print()


if __name__ == "__main__":
    main()
