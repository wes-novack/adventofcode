from puzzle2 import *


byr_passport1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
byr_passport2 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:193 iyr:2017 cid:147 hgt:183cm"
byr_passport3 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1919 iyr:2017 cid:147 hgt:183cm"
byr_passport4 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2003 iyr:2017 cid:147 hgt:183cm"
iyr_passport1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2021 cid:147 hgt:183cm"
eyr_passport1 = "ecl:gry pid:860033327 eyr:2019 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"


def test_valid_fields_byr_valid():
    actual = valid_fields(byr_passport1)
    expected = True
    assert actual == expected


def test_valid_fields_byr_invalid_3_digits():
    actual = valid_fields(byr_passport2)
    expected = False
    assert actual == expected


def test_valid_fields_byr_invalid_early_year():
    actual = valid_fields(byr_passport3)
    expected = False
    assert actual == expected


def test_valid_fields_byr_invalid_late_year():
    actual = valid_fields(byr_passport4)
    expected = False
    assert actual == expected


def test_valid_fields_iyr_invalid():
    actual = valid_fields(iyr_passport1)
    expected = False
    assert actual == expected


def test_valid_fields_eyr_invalid():
    actual = valid_fields(eyr_passport1)
    expected = False
    assert actual == expected