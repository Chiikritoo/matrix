import sympy as sp
from Vector import Vector

def main():
    v1 = Vector([14, 57, 77])
    v2 = Vector([14, 57])
    try:
        v1.add(v2)
        print(v1)
    except ValueError as error:
        print('Error:', error)


if __name__ == "__main__":
    main()
