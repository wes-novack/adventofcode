from puzzle1 import *


def valid_fields(passport):
    if not valid_field(passport, 'byr:', 4, 4, 1920, 2002):
        return False
    if not valid_field(passport, 'iyr:', 4, 4, 2010, 2020):
        return False
    if not valid_field(passport, 'eyr:', 4, 4, 2020, 2030):
        return False
    if not valid_field(passport, 'hgt:', 2, 3, 59, 193):
        return False
    return True


def valid_field(passport, field_code, min_chars, max_chars, min_val, max_val):
    passport_fields = passport.split()
    for field in passport_fields:
        if field_code in field:
            field_code_list = field.split(':')
            if is_int_string(field_code_list[1]):
                field_value = int(field_code_list[1])
            else:
                if field_code == 'hgt:':
                    min_val, max_val, field_value = hgt_validity(field_code_list)
                    if not min_val or not max_val or not field_value:
                        return False
            field_value_length = len(str(field_value))
            if field_value_length >= min_chars and field_value_length <= max_chars and field_value >= min_val and field_value <= max_val:
                return True
            else:
                return False
    return False


def hgt_validity(field_code_list):
    if "cm" in field_code_list[1]:
        min_val = 150
        max_val = 193
        field_value = int(field_code_list[1].split('cm')[0])
    elif "in" in field_code_list[1]:
        min_val = 59
        max_val = 76
        field_value = int(field_code_list[1].split('in')[0])
    else:
        min_val = None
        max_val = None
        field_value = None
    return min_val, max_val, field_value


def is_int_string(text):
    try: 
        int(text)
        return True
    except ValueError:
        return False