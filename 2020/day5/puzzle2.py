from puzzle1 import *


def find_empty_seat():
    seat_ids = sorted(main())
    length = len(seat_ids)
    for i, seat_id in enumerate(seat_ids):
        if i == 0:
            continue
        if seat_id - 1 == seat_ids[i - 1]:
            continue
        else:
            candidate_id = seat_id - 1
            if candidate_id - 1 == seat_ids[i - 1]: 
                return candidate_id
            else:
                continue


if __name__ == '__main__':
    print(find_empty_seat())