from puzzle1 import *


def valid_fields(passport):
    if not valid_year(passport, 'byr:', 4, 1920, 2002):
        return False
    if not valid_year(passport, 'iyr:', 4, 2010, 2020):
        return False
    if not valid_year(passport, 'eyr:', 4, 2020, 2030):
        return False
    return True


def valid_year(passport, field_code, digits, min_year, max_year):
    passport_fields = passport.split()
    for field in passport_fields:
        if field_code in field:
            field_code_list = field.split(':')
            year = int(field_code_list[1])
            if len(str(year)) == digits and year >= min_year and year <= max_year:
                return True
            else:
                return False
    return False