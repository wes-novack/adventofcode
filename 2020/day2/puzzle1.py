def read_data():
    input_list = []
    with open('input.txt') as file:
        for line in file:
            input_list.append(line.strip('\n'))
    return input_list


def password_validity(policy_range, policy_char, password):
    policy_range_list = policy_range.split('-')
    print(policy_range_list)
    policy_char_count = 0
    for char in password:
        if char == policy_char:
            policy_char_count+=1
    start = int(policy_range_list[0])
    end = int(policy_range_list[1]) + 1
    if policy_char_count in range(start, end):
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