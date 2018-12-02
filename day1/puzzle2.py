def read_file():
    try:
        with open("input.txt") as change_list:
            input_lines = []
            for line in change_list:
                input_lines.append(line)
            return input_lines
    except Exception:
        print("Exception: {}".format(Exception))


def calibrate(base, mylist, frequencies_visited):
    calibration = None
    for frequency in mylist:
        if base in frequencies_visited:
            calibration = base
            break
        else:
            frequencies_visited.append(base)
        base = base + int(frequency)
    return base, calibration, frequencies_visited


def check_calibration(mylist):
    no_visits = []
    current, calibration, frequencies_visited = calibrate(0, mylist, no_visits)
    while calibration is None:
        current, calibration, frequencies_visited = calibrate(current, mylist, frequencies_visited)
    return calibration


if __name__ == "__main__":
    change_list = read_file()
    result = check_calibration(change_list)
    print(result)
