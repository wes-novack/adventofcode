def read_file(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line.replace("\n",""))
    return lines


def solve_puzzle(lines):
    return 17


def determine_outer_coords(lines):
    outer_coords = { "nw": [1000, 0], "ne": [0, 0], "se": [0, 0], "sw": [1000, 1000] }
    coordinate_pairs = []
    for line in lines:
        coordinate_pair = line.split(",")
        coordinate_pairs.append(coordinate_pair)
    print(coordinate_pairs)
    for (element, coordinate_pair) in enumerate(coordinate_pairs):
        x = int(coordinate_pair[0])
        y = int(coordinate_pair[1])
        if x < outer_coords["nw"][0] and y > outer_coords["nw"][1]:
            outer_coords["nw"] = [int(coordinate_pair[0]),int(coordinate_pair[1])]
        if x > outer_coords["ne"][0] and y > outer_coords["ne"][1]:
            outer_coords["ne"] = [int(coordinate_pair[0]),int(coordinate_pair[1])]
        if x < outer_coords["sw"][0] and y < outer_coords["sw"][1]:
            outer_coords["sw"] = [int(coordinate_pair[0]),int(coordinate_pair[1])]
    print(outer_coords)



if __name__ == '__main__':
    coordinates = read_file("input2.txt")
    determine_outer_coords(coordinates)
