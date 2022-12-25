"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def solution() -> None:
    sieve = sieve_of_eratosthenes(2000000)
    print(sum(sieve))


def sieve_of_eratosthenes(n: int) -> list:
    """Return all primes up to and including n."""
    primes = []

    # INFO: all integers are initially considered prime

    is_prime = [True for _ in range(n + 1)]

    # INFO: 0 and 1 are not prime

    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, n + 1):
        if is_prime[p]:
            # INFO: p is a prime, so add it to the list
            primes.append(p)
            # INFO: mark all multiples of p as nonprime
            for i in range(p, n + 1, p):
                is_prime[i] = False

    return primes


if __name__ == "__main__":
    solution()
