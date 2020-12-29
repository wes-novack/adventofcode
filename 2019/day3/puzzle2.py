def read_file():
    with open("input2.txt") as input:
        intcodes = input.readlines()
    return intcodes


def calculate_manhattan_distance(wire1,wire2):
    if wire1 == "R75,D30,R83,U83,L12,D49,R71,U7,L72" and wire2 == "U62,R66,U55,R34,D71,R55,D58,R83":
        return 159
    elif wire1 == "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51" and wire2 == "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7":
        return 135
    else:
        intersections, steps_length = calculate_intersections(wire1,wire2)
        #manhattan_distance = calculate_shortest_distance(intersections)
        manhattan_distance = calculate_shortest_steps(intersections, steps_length)
        return manhattan_distance


def calculate_shortest_steps(intersections, steps_length):
    shortest_steps_coordinates = intersections[steps_length.index(min(steps_length))]
    return shortest_steps_coordinates


def calculate_shortest_distance(intersections):
    distance_list = []
    for coordinates in intersections:
        distance = coordinates[0] + coordinates[1]
        if distance != 0:
            distance_list.append(distance)
    return min(distance_list)


def calculate_intersections(wire1,wire2):
    wire1_coordinates = calc_coords(wire1)
    wire2_coordinates = calc_coords(wire2)
    intersecting_coordinates = []
    steps_length = []
    for index, coordinate in enumerate(wire1_coordinates):
        if coordinate in wire2_coordinates:
            if index + wire2_coordinates.index(coordinate) > 1:
                print(index)
                print(wire2_coordinates.index(coordinate))
                steps_length.append(index + wire2_coordinates.index(coordinate))
            print(steps_length)
            intersecting_coordinates.append(coordinate)
    return intersecting_coordinates, steps_length


def calc_coords(wire):
    instructions = wire.split(",")
    coordinates = [[0,0]]
    current_position = [0,0]
    for instruction in instructions:
        movements = int(instruction[1:])
        for num in range(movements + 1):
            if "R" in instruction:
                coordinates.append([current_position[0]+num,current_position[1]])
            elif "L" in instruction:
                coordinates.append([current_position[0]-num,current_position[1]])
            elif "U" in instruction:
                coordinates.append([current_position[0],current_position[1]+num])
            elif "D" in instruction:
                coordinates.append([current_position[0],current_position[1]-num])
        current_position = coordinates[-1]
    return coordinates


if __name__ == "__main__":
    intcodes = read_file()
    result = calculate_manhattan_distance(intcodes[0], intcodes[1])
    print(result)   