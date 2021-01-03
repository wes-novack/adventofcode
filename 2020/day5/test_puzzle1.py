from puzzle1 import *


def test_f_and_0_127_returns_lower_half():
    actual = get_new_range('F', (0, 127))
    expected = (0, 63)
    assert actual == expected


def test_b_and_0_127_returns_upper_half():
    actual = get_new_range('B', (0, 127))
    expected = (64, 127)
    assert actual == expected


def test_b_and_0_63_returns_upper_half():
    actual = get_new_range('B', (0, 63))
    expected = (32, 63)
    assert actual == expected


def test_f_and_32_63_returns_lower_half():
    actual = get_new_range('F', (32, 63))
    expected = (32, 47)
    assert actual == expected


def test_b_and_32_47_returns_lower_half():
    actual = get_new_range('B', (32, 47))
    expected = (40, 47)
    assert actual == expected


def test_b_and_40_47_returns_lower_half():
    actual = get_new_range('B', (40, 47))
    expected = (44, 47)
    assert actual == expected


def test_f_and_44_47_returns_lower_half():
    actual = get_new_range('F', (44, 47))
    expected = (44, 45)
    assert actual == expected


def test_f_and_44_45_returns_row():
    actual = get_new_range('F', (44, 45))
    expected = 44
    assert actual == expected


def test_f_and_44_44_returns_none():
    actual = get_new_range('F', (44, 44))
    expected = None
    assert actual == expected


def test_r_and_0_7_returns_upper_half():
    actual = get_new_range('R', (0,7))
    expected = (4, 7)
    assert actual == expected


def test_l_and_4_7_returns_lower_half():
    actual = get_new_range('L', (4, 7))
    expected = (4, 5)
    assert actual == expected


def test_r_and_4_5_returns_seat():
    actual = get_new_range('R', (4,5))
    expected = 5
    assert actual == expected


def test_full_seat_code_returns_row_and_seat():
    actual = get_row_and_seat_number('FBFBBFFRLR')
    expected = 44, 5
    assert actual == expected


def test_get_seat_id():
    actual = get_seat_id('FBFBBFFRLR')
    expected = 357
    assert actual == expected


def test_get_seat_id_v2():
    actual = get_seat_id('BFFFBBFRRR')
    expected = 567
    assert actual == expected


def test_get_seat_id_v3():
    actual = get_seat_id('FFFBBBFRRR')
    expected = 119
    assert actual == expected