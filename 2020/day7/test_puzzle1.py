import pytest

from puzzle1 import *

@pymark
def test_light_red():
    actual = create_bag_definition("light red bags contain 1 bright white bag, 2 muted yellow bags.")
    expected = {"light red": {"bright white": 1, "muted yellow": 2}}
    assert actual == expected


def test_dark_orange():
    actual = create_bag_definition("dark orange bags contain 3 bright white bags, 4 muted yellow bags.")
    expected = {"dark orange": {"bright white": 3, "muted yellow": 4}}
    assert actual == expected