"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


def solution() -> None:
    """
    We can find the largest palindrome by starting at the largest possible
    product of two 3-digit numbers and working our way down. If we find a
    palindrome, we can stop. We can also stop if the product is less than the
    largest palindrome we have found so far.
    """
    largest_palindrome = 0

    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if product < largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product

    print(f"The largest palindrome is {largest_palindrome}")


def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


if __name__ == "__main__":
    solution()
