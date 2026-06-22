import sympy as sp
from Vector import Vector
from linear_combination import linear_combination

def test_addition():
    print('Test addition (v+v)')
    v1 = Vector([5, 10, 15])
    v2 = Vector([15, 10, 5])
    try:
        v1.add(v2)
        print(v1)
    except ValueError as error:
        print('Error:', error)

    print()


def test_substract():
    print('Test substract (v-v)')
    v1 = Vector([5, 10, 15])
    v2 = Vector([15, 10, 5])
    try:
        v1.sub(v2)
        print(v1)
    except ValueError as error:
        print('Error:', error)

    print()

def test_mult_by_scalar():
    print('Test mult by scalar (n*v)')
    v1 = Vector([5, 10, 15])
    try:
        v1.scl(2)
        print(v1)
    except ValueError as error:
        print('Error:', error)

    print()

def test_linear_combination():
    print('Test linear combination')
    v1 = Vector([1, 2, 3])
    v2 = Vector([0, 10, -100])

    vectors = [v1, v2]
    scalars = [10, -2]
    r = linear_combination(vectors, scalars)
    print(r)


def main():
    test_addition()
    test_substract()
    test_mult_by_scalar()
    test_linear_combination()


if __name__ == "__main__":
    main()
