"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math


def solution() -> None:
    """
    We only need to check up to the square root of the target
    the reason for this is that if a number is not prime, it can be
    factored into two numbers. If one of those numbers is greater than
    the square root of the target, the other number must be less than
    the square root of the target.
    """
    target = 600_851_475_143
    largest_prime_factor = 0

    for i in range(2, int(math.sqrt(target))):
        if target % i == 0:
            if is_prime(i):
                largest_prime_factor = i

    print(f"The largest prime factor of {target} is {largest_prime_factor}")


def is_prime(number: int) -> bool:
    """
    we can find this by checking if the number is divisible by any number
    between 2 and the square root of the number. If it is divisible by any
    number, it is not prime.
    """
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    solution()
