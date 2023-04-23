import numpy as np


def example_ones():
    print("\nOnes:")
    print(np.ones(3))
    print()


def example_mask():
    print("\nMask:")
    mask = np.array([True, True, False, False], dtype=bool)
    print(mask)

    array = np.ones(4)
    print(array)
    print(array[mask])
    print()


def example_multiplication():
    print("\nMultiplication:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(a * b)
    print()


def example_sum():
    print("\nSum:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(a + b)
    print()


def example_division():
    print("\nDivision:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(a / b)
    print()


def example_subtraction():
    print("\nSubtraction:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(a - b)
    print()


example_ones()
example_mask()
example_multiplication()
example_sum()
example_division()
example_subtraction()
