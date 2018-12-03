from day2.puzzle2 import *
import pytest

calculate_common_letters_testdata = [
    ("abcde","abcdf","abcd"),
    ("fghij","fguij","fgij")
#    (["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"], "fgij"),
]

@pytest.mark.parametrize("string1,string2,common_letters", calculate_common_letters_testdata)
def test_calculate_common_letters(string1, string2, common_letters):
    assert calculate_common_letters(string1, string2) == common_letters

