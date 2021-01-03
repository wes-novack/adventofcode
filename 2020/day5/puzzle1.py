import math


def get_new_range(letter_code, start_range):
    if not (start_range[1] + 1) % 2:
        start_range_begin = start_range[0]
        start_range_end = start_range[1]
        start_range_diff = start_range[1] - start_range[0]

        lower_half_end = math.floor(start_range_diff/2) + start_range_begin
        upper_half_begin = lower_half_end + 1
        lower_half = (start_range_begin, lower_half_end)
        upper_half = (upper_half_begin, start_range_end)
        
        if letter_code.upper() in ['F', 'L']:
            if lower_half[0] == lower_half[1]:
                return lower_half[0]
            else:
                return lower_half
        elif letter_code.upper() in ['B', 'R']:
            if upper_half[0] == upper_half[1]:
                return upper_half[0]
            return upper_half
        else:
            print("unrecognized letter code")
    else:
        print("start_range not divisible by 2")


def get_row_and_seat_number(seat_hash):
    row_code = seat_hash[0:7]
    row_number = 0
    seat_number = 0

    start_range = (0, 127)
    for letter in row_code:
        start_range = get_new_range(letter, start_range)
    row_number = start_range

    seat_start_range = (0, 7)
    seat_code = seat_hash[7:]
    for letter in seat_code:
        seat_start_range = get_new_range(letter, seat_start_range)
    seat_number = seat_start_range
    return row_number, seat_number


def get_seat_id(seat_hash):
    row, seat = get_row_and_seat_number(seat_hash)
    return row * 8 + seat


def read_file(filename):
    seat_hashes = []
    with open(filename) as file:
        for line in file:
            seat_hashes.append(line.strip())
    return seat_hashes


def main():
    seat_hashes = read_file('input.txt')
    seat_ids = []
    for hash in seat_hashes:
        seat_ids.append(get_seat_id(hash))
    print(max(seat_ids))
    return seat_ids


if __name__ == '__main__':
    main()