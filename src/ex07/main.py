from common import Vector, Matrix
import sympy as sp


def test_matrix():
    print("Test mul vec")

    m1 = Matrix([[1, 4, 7],
                [2, 5, 8],
                [3, 6, 9]])

    v = Vector([5, 1, 2])

    try:
        vec = m1.mul_vec(v)
        print(f"{vec}")

    except ValueError as error:
        print("Error:", error)
    print()

    print("Test mul mat")

    m2 = Matrix([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

    try:
        mat = m1.mul_mat(m2)
        sp.pprint(sp.Matrix(mat.rows))

    except ValueError as error:
        print("Error:", error)

    print()


def main():
    test_matrix()


if __name__ == "__main__":
    main()
