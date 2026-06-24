from common import Vector


def test_addition():
    print("Test addition (v+v)")
    v1 = Vector([5, 10, 15])
    v2 = Vector([15, 10, 5])
    try:
        v1.add(v2)
        print(v1)
    except ValueError as error:
        print("Error:", error)

    print()


def test_substract():
    print(
        "Test substract (v-v)"
    )
    v1 = Vector([4, 10, 15])
    v2 = Vector([15, 10, 5])
    try:
        v1.sub(v2)
        print(v1)
    except ValueError as error:
        print("Error:", error)

    print()


def test_mult_by_scalar():
    print("Test mult by scalar (n*v)")
    v1 = Vector([5, 10, 15])
    try:
        v1.scl(2)
        print(v1)
    except ValueError as error:
        print("Error:", error)

    print()


def main():
    test_addition()
    test_substract()
    test_mult_by_scalar()


if __name__ == "__main__":
    main()
