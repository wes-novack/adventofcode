def create_bag_definition(rule):
    bag_definition = {}
    if not "no other bags" in rule:
        rule_list = rule.split(" bags contain ")
        top_level_bag = rule_list[0]
        bag_definition[top_level_bag] = {}
        bags_contained = rule_list[1].split(", ")
        for bag in bags_contained:
            count = int(bag[0])
            bag_words = bag.split()
            bag_identifier = bag_words[1] + " " + bag_words[2]
            bag_definition[top_level_bag][bag_identifier] = count
    else:
        rule_words = rule.split()
        top_level_bag = rule_words[0] + " " + rule_words[1]
        bag_definition[top_level_bag] = {}
    return bag_definition


def read_file(filename):
    with open(filename) as file:
        rules = file.readlines()
    return rules


def process_rules(filename):
    rules = read_file(filename)
    rule_list = []
    for rule in rules:
        rule_list.append(create_bag_definition(rule))
    return rule_list


def calculate_valid_bag_colors(rule_list, color, valid_bag_colors):
    valid_bag_start_count = len(valid_bag_colors)
    for bag in rule_list:
        for k, v in bag.items():
            if color in v and k != color:
                valid_bag_colors.add(k)
    set_copy = valid_bag_colors.copy()
    if len(valid_bag_colors) != valid_bag_start_count:
        for bag in set_copy:
            calculate_valid_bag_colors(rule_list, bag, valid_bag_colors)
    return len(valid_bag_colors)


def main(filename):
    rule_list = process_rules(filename)
    valid_bag_colors = set()
    return calculate_valid_bag_colors(rule_list, "shiny gold", valid_bag_colors)


if __name__ == '__main__':
    print(main("input.txt"))