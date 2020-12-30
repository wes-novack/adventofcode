from puzzle1 import *

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
single_line_passport = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
multi_line_passport = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\
byr:1937 iyr:2017 cid:147 hgt:183cm"


def test_single_line_passport_is_valid():
    actual = passport_valid(single_line_passport)
    expected = True
    assert actual == expected


def test_multi_line_passport_is_valid():
    actual = passport_valid(single_line_passport)
    expected = True
    assert actual == expected


def test_extract_multi_line_passport_from_file():
    passports = extract_passports("test_input.txt")
    actual = passports[2]
    expected = "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm" 
    print(f"actual: {actual}")
    print(f"expected: {expected}")
    assert actual == expected


def test_calculate_number_of_valid_passports():
    actual = calculate_number_of_valid_passports("test_input.txt")
    expected = 2
    assert actual == expected