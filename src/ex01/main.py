from common.Vector import Vector
from ex01.linear_combination import linear_combination


def test_linear_combination():
    print("Test linear combination")
    v1 = Vector[int]([1, 2, 3])
    v2 = Vector[int]([0, 10, -100])

    vectors = [v1, v2]
    scalars = [10, -2]
    r = linear_combination(vectors, scalars)
    print(r)
    print()


def main():
    test_linear_combination()


if __name__ == "__main__":
    main()
