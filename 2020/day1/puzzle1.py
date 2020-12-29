
def read_file():
    with open("input.txt") as input_list:
        input_lines = []
        for line in input_list:
            input_lines.append(int(line))
    return input_lines


def find_numbers_that_sum_to_2020(numbers_list):
    for i, number in enumerate(numbers_list):
        if i < (len(numbers_list) - 1):
            for other_num in numbers_list:
                if number + other_num == 2020:
                    return number, other_num


def multiply_nums(num1, num2):
    return num1 * num2


if __name__ == '__main__':
    input = read_file()
    num1, num2 = find_numbers_that_sum_to_2020(input)
    answer = multiply_nums(num1, num2)
    print(answer)