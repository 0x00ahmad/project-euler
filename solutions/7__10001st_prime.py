"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""


def is_prime(n: int) -> bool:
    if n == 2:
        return True

    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def solution() -> None:
    """Main function"""
    nth_prime_to_find = 10001
    current_nth_prime = 0
    number_to_check = 1
    while current_nth_prime < nth_prime_to_find:
        number_to_check += 1
        if is_prime(number_to_check):
            current_nth_prime += 1

    print(number_to_check)


if __name__ == "__main__":
    solution()
