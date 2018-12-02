calculated_frequencies = []


def read_file():
    try:
        with open("input.txt") as change_list:
            input_lines = []
            for line in change_list:
                input_lines.append(line)
            return input_lines
    except Exception:
        print("Exception: {}".format(Exception))


def calibrate(base_frequency, change_list):
    base = base_frequency
    calibrated = False
    while not calibrated:
        calibrated, new_frequency = process_change_list(calibrated, change_list, base)
        base = new_frequency
    return new_frequency


def process_change_list(calibrated, change_list, new_frequency):
    for line in change_list:
        if line[0] == "+":
            line_split = line.split("+")
            new_frequency += int(line_split[1])
            if new_frequency in calculated_frequencies:
                print("new_frequency: {}".format(new_frequency))
                calibrated = True
                break
            else:
                calculated_frequencies.append(new_frequency)
                print(calculated_frequencies)
                calibrated = False
        elif line[0] == "-":
            line_split = line.split("-")
            new_frequency -= int(line_split[1])
            if new_frequency in calculated_frequencies:
                print("new_frequency: {}".format(new_frequency))
                calibrated = True
                break
            else:
                calculated_frequencies.append(new_frequency)
                print(calculated_frequencies)
                calibrated = False
        else:
            print("No + or - character detected at start of line")
    return calibrated, new_frequency


if __name__ == "__main__":
    change_list = read_file()
    result = calibrate(0, change_list)
    print(result)