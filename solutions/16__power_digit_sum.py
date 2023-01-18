"""
Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solution():
    # INFO: the "pythonic" solution
    # ans = sum(int(digit) for digit in str(2**1000))
    # print(ans)

    # INFO: now with fast exponentiation
    # The approach is to use the method of splitting the exponent into powers of 2
    # as we know the power, we can pick any combination, but I picked the following
    # 2^8, 2^32, 2^64, 2^128, (2^256 * 3)
    ans = 1
    for power in [8, 32, 64, 128, *([256] * 3)]:
        ans *= 2**power

    print(sum(int(n) for n in str(ans)))


if __name__ == "__main__":
    solution()
