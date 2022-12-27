"""
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time
from functools import cache


@cache
def collatz_sequence(number: int) -> int:
    """Return the length of the Collatz sequence for a given number."""
    if number == 1:
        return 1
    elif number % 2 == 0:
        return 1 + collatz_sequence(number // 2)
    else:
        return 1 + collatz_sequence(3 * number + 1)


def solution() -> None:
    s = time.time()
    longest_sequence = 0
    longest_sequence_number = 0
    for number in range(1, 1_000_000):
        sequence = collatz_sequence(number)
        if sequence > longest_sequence:
            longest_sequence = sequence
            longest_sequence_number = number

    print(longest_sequence_number)
    print(f"Time taken: {time.time() - s}")


if __name__ == "__main__":
    solution()
