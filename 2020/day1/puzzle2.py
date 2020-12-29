from puzzle1 import *


def three_nums_sum_to_2020(numbers_list):
    for i, number in enumerate(numbers_list):
        if i < (len(numbers_list) - 1):
            for second_num in numbers_list:
                for third_num in numbers_list:
                    if number + second_num + third_num == 2020:
                        return number, second_num, third_num


if __name__ == '__main__':
    input = read_file()
    num1, num2, num3 = three_nums_sum_to_2020(input)
    print(num1 * num2 * num3)