import re


def create_bag_definition(rule):
    rule_list = rule.split(" bags contain ")
    top_level_bag = rule_list[0]
    bag_definition = {}
    bag_definition[top_level_bag] = {}
    bags_contained = rule_list[1].split(", ")
    for bag in bags_contained:
        count = int(bag[0])
        bag_words = bag.split()
        bag_identifier = bag_words[1] + " " + bag_words[2]
        bag_definition[top_level_bag][bag_identifier] = count
    return bag_definition
