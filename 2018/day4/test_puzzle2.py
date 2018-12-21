from day4.puzzle2 import *
import pytest


lines = read_file("input_partial.txt")

'''
#137:   16
#3251:  29 + 26 = 55
#479:   13 + 17 = 30
'''


def test_most_popular_min_of_sleep_for_guard():
    most_popular_minute, mins_asleep = most_popular_min_of_sleep_for_guard("#3251", lines)
    assert most_popular_minute == 33
    assert mins_asleep == 2
    most_popular_minute, mins_asleep = most_popular_min_of_sleep_for_guard("#137", lines)
    assert most_popular_minute == 39
    assert mins_asleep == 3


def test_most_popular_min_of_sleep_for_guard():
    add_guards_to_dict(lines)
    get_most_popular_min_for_each_guard(lines)
    guard_id, minute = get_most_sleep_on_unique_min(guards_sleep)
    print(int(guard_id)* minute)
    assert int(guard_id) == 137
    assert minute == 39
