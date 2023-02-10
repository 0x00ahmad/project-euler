"""
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

ONE_DIGIT_MAP = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

TWO_DIGIT_MAP_BEFORE_20 = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
}

TWO_DIGIT_FIRST_DIGIT_MAP = {
    "0": "",
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}


def get_one_digit_count_word(number: str) -> str:
    assert len(number) == 1
    return ONE_DIGIT_MAP[str(number)]


def get_two_digit_count_word(number: str):
    """return the word representation of a two digit number"""
    assert len(number) == 2
    if number[0] == "1":
        return TWO_DIGIT_MAP_BEFORE_20[number]

    if number[1] == "0":
        return TWO_DIGIT_FIRST_DIGIT_MAP[number[0]]

    return TWO_DIGIT_FIRST_DIGIT_MAP[number[0]] + ONE_DIGIT_MAP[number[1]]


def get_three_digit_count_word(number: str):
    if number[1:] == "00":
        return ONE_DIGIT_MAP[number[0]] + "hundred"
    return (
        ONE_DIGIT_MAP[number[0]] + "hundredand" + get_two_digit_count_word(number[1:])
    )


def solution():
    number_letter_counts = 0
    len_map = {
        "1": get_one_digit_count_word,
        "2": get_two_digit_count_word,
        "3": get_three_digit_count_word,
    }
    for num in (str(i) for i in range(1, 1001)):
        if num == "1000":
            number_letter_counts += len("onethousand")
            continue
        out = len_map[str(len(num))](num)
        number_letter_counts += len(out)

    print(f"{number_letter_counts=}")


if __name__ == "__main__":
    solution()
