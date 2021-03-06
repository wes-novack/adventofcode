def read_file():
    with open("input.txt") as input:
        intcodes = input.readline().split(",")
        intcodes = [int(x) for x in intcodes]
    return intcodes


def calculate_intcode(intcodes):
    position = 0
    length = len(intcodes)
    while position < (length-1):
        opcode = intcodes[position]
        if opcode == 1:
            newlist = intcodes[position:position + 4]
            print([intcodes[position:(position + 4)]])
            sum = intcodes[newlist[1]] + intcodes[newlist[2]]
            intcodes[newlist[3]] = sum
        elif opcode == 2:
            newlist = intcodes[position:position+4]
            multiplier = intcodes[newlist[1]] * intcodes[newlist[2]]
            intcodes[newlist[3]] = multiplier
        elif opcode == 99:
            break
        else:
            print("Unknown opcode, something went wrong")
        position = position + 4
    return intcodes


if __name__ == "__main__":
    intcodes = read_file()
    intcodes[1] = 12
    intcodes[2] = 2
    result = calculate_intcode(intcodes)
    print(result[0])