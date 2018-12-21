from day2.puzzle1 import *
import pytest

check_duplicate_chars_testdata = [
    ("abcddefghijklmooo", {2,3}),
    ("abcdeee", {3}),
    ("aaabbbccc", {3}),
    ("abcdefgg", {2})
]

@pytest.mark.parametrize("id,output_set", check_duplicate_chars_testdata)
def test_check_duplicate_chars(id, output_set):
    assert check_duplicate_chars(id) == output_set

