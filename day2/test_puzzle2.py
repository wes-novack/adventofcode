from day2.puzzle2 import *
import pytest

calculate_common_letters_testdata = [
    ("abcdeefgh","abcdfefgh","abcdefgh"),
    ("fghij","fguij","fgij")
]


@pytest.mark.parametrize("string1,string2,common_letters", calculate_common_letters_testdata)
def test_calculate_common_letters(string1, string2, common_letters):
    assert calculate_common_letters(string1, string2) == common_letters


find_similar_testdata = [
    (["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"], ["fghij","fguij"]),
]


@pytest.mark.parametrize("in_list,out_list", find_similar_testdata)
def test_find_similar(in_list, out_list):
    assert find_similar(in_list) == out_list


compare_two_testdata = [
    ("fghij","fguij", ["fghij", "fguij"]),
    ("abcde","fghij", None),
    ('abcde', 'axcye', None)
]


@pytest.mark.parametrize("string1,string2,answer", compare_two_testdata)
def test_compare_two(string1, string2, answer):
    assert compare_two(string1, string2) == answer
