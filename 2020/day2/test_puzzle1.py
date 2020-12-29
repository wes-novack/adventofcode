from puzzle1 import *

test_data = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]


def test_password_validity():
    actual = password_validity("1-3","a","abcde")
    expected = True
    assert actual == expected


def test_number_of_valid_passwords():
    actual = number_of_valid_passwords(test_data)
    expected = 2
    assert actual == expected
