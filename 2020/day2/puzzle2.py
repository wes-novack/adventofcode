from puzzle1 import read_data

def password_validity(policy_range, policy_char, password):
    policy_range_list = policy_range.split('-')
    first_index = int(policy_range_list[0]) - 1
    second_index = int(policy_range_list[1]) - 1

    if policy_char == password[first_index] and policy_char != password[second_index]:
        return True
    elif policy_char != password[first_index] and policy_char == password[second_index]:
        return True
    else:
        return False


def number_of_valid_passwords(password_data):
    valid_passwords = 0
    for line in password_data:
        password_data_item_list = line.split(' ')
        policy_range = password_data_item_list[0]
        policy_char = password_data_item_list[1].strip(':')
        password = password_data_item_list[2]
        if password_validity(policy_range, policy_char, password):
            valid_passwords += 1
    return valid_passwords


if __name__ == '__main__':
    input = read_data()
    print(number_of_valid_passwords(input))