required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def passport_valid(passport):
    for field in required_fields:
        if field in passport:
            continue
        else:
            return False
    return True


def extract_passports(passports_file):
    passports_list = []
    with open(passports_file) as file:
        passport = ""
        for line in file:
            if line.strip() != "":
                if passport != "":
                    passport += " "
                passport += line.strip()
            else:
                passports_list.append(passport)
                passport = ""
    return passports_list


def calculate_number_of_valid_passports(passport_file):
    passports_list = extract_passports(passport_file)
    valid_passports = 0
    for passport in passports_list:
        if passport_valid(passport):
            valid_passports += 1
    return valid_passports


if __name__ == '__main__':
    print(calculate_number_of_valid_passports("input.txt"))