"""
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


def solution() -> None:
    """
    we do know that the smallest number that is divisible by 1 to 10 is 2520
    so we can start from there and increment by 2520
    """
    number = 2520
    while True:
        if all(number % i == 0 for i in range(1, 21)):
            print(f"the smallest number that is divisible by 1 to 20 is {number}")
            break
        number += 2520


if __name__ == "__main__":
    solution()
