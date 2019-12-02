from puzzle1 import *

OUTPUT=19690720
INPUT_RANGE=range(0,100)


def find_inputs(output, input_range, intcodes):
    for noun in input_range:
        working_intcodes = intcodes.copy()
        working_intcodes[1] = noun
        for verb in input_range:
            verb_intcodes = working_intcodes.copy()
            verb_intcodes[2] = verb
            result = calculate_intcode(verb_intcodes)
            if result[0] == output:
                return noun, verb


if __name__ == "__main__":
    intcodes = read_file()
    noun, verb = find_inputs(OUTPUT, INPUT_RANGE, intcodes)
    print(100 * noun + verb)