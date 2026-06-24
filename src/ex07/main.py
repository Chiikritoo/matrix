from common import Vector, Matrix


def test_matrix():
    print("Test cross product")
    v1 = Vector([1, 4, 7])
    v2 = Vector([2, 5, 8])
    v3 = Vector([3, 6, 9])

    m = Matrix([v1, v2, v3])

    v = Vector([5, 1, 2])

    try:
        vec = m.mul_vec(v)
        print(f"{vec}")

    except ValueError as error:
        print("Error:", error)

    print()


def main():
    test_matrix()


if __name__ == "__main__":
    main()
