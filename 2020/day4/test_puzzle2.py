import pytest

from puzzle2 import *

byr_passport1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
byr_passport2 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:193 iyr:2017 cid:147 hgt:183cm"
byr_passport3 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1919 iyr:2017 cid:147 hgt:183cm"
byr_passport4 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2003 iyr:2017 cid:147 hgt:183cm"
iyr_passport1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2021 cid:147 hgt:183cm"
eyr_passport1 = "ecl:gry pid:860033327 eyr:2019 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
hgt_passport1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183mm"
hgt_passport2 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:194cm"
hgt_passport3 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:58in"
hcl_passport1 = "ecl:gry pid:860033327 eyr:2020 hcl:fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
hcl_passport2 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffff byr:1937 iyr:2017 cid:147 hgt:183cm"
ecl_passport1 = "ecl:red pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
pid_passport1 = "ecl:gry pid:8600333d eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"

valid1 = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f"
valid2 = "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"
valid3 = "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022"
valid4 = "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"


invalid_passports = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2003 iyr:2017 cid:147 hgt:183cm",
"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:190in",
"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:190",
"ecl:gry pid:860033327 eyr:2020 hcl:#123abz byr:1937 iyr:2017 cid:147 hgt:183cm",
"ecl:gry pid:860033327 eyr:2020 hcl:123abc byr:1937 iyr:2017 cid:147 hgt:183cm",
"ecl:wat pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
"ecl:gry pid:0123456789 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"]


@pytest.mark.parametrize("passport", invalid_passports)
def test_invalid_passports(passport):
    actual = valid_fields(passport)
    expected = False
    assert actual == expected


def test_valid_fields_valid1():
    actual = valid_fields(valid1)
    expected = True
    assert actual == expected


def test_valid_fields_valid2():
    actual = valid_fields(valid2)
    expected = True
    assert actual == expected


def test_valid_fields_valid3():
    actual = valid_fields(valid3)
    expected = True
    assert actual == expected


def test_valid_fields_valid4():
    actual = valid_fields(valid4)
    expected = True
    assert actual == expected


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


def test_valid_fields_hgt_invalid():
    actual = valid_fields(hgt_passport1)
    expected = False
    assert actual == expected


def test_valid_fields_hgt_invalid_v2():
    actual = valid_fields(hgt_passport2)
    expected = False
    assert actual == expected


def test_valid_fields_hgt_invalid_v3():
    actual = valid_fields(hgt_passport3)
    expected = False
    assert actual == expected


def test_valid_fields_hcl_invalid():
    actual = valid_fields(hcl_passport1)
    expected = False
    assert actual == expected


def test_valid_fields_hcl_invalid2():
    actual = valid_fields(hcl_passport2)
    expected = False
    assert actual == expected


def test_valid_fields_ecl_invalid():
    actual = valid_fields(ecl_passport1)
    expected = False
    assert actual == expected


def test_valid_fields_pid_invalid():
    actual = valid_fields(pid_passport1)
    expected = False
    assert actual == expected