"""
Lattice Paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

"""

WIDTH = 20
HEIGHT = 20


def solution() -> None:
    """
    the approach is to use the binomial coefficient formula
    """

    # the number of paths is the binomial coefficient
    # (WIDTH + HEIGHT)! / (WIDTH! * HEIGHT!)
    # this can be simplified to (WIDTH + HEIGHT)! / (WIDTH!)^2
    # this can be simplified to (WIDTH + HEIGHT)(WIDTH + HEIGHT - 1)...(WIDTH + 1) / (WIDTH!)^2
    # this can be simplified to (WIDTH + HEIGHT)(WIDTH + HEIGHT - 1)...(WIDTH + 1) / (WIDTH)(WIDTH - 1)...(1)
    # this can be simplified to (WIDTH + HEIGHT)(WIDTH + HEIGHT - 1)...(WIDTH + 1) / (WIDTH)(WIDTH - 1)...(1)
    # this can be simplified to (WIDTH + 1)(WIDTH + 2)...(WIDTH + HEIGHT) / (1)(2)...(WIDTH)

    numerator = 1
    for i in range(WIDTH + 1, WIDTH + HEIGHT + 1):
        numerator *= i

    denominator = 1
    for i in range(1, WIDTH + 1):
        denominator *= i

    print(numerator // denominator)


if __name__ == "__main__":
    solution()
