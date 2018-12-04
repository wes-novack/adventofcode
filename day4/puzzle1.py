#objectives
#1) sort log entries by date/minute
#2) find the Guard# with the most minutes of sleep
#3) for the Guard# with the most minutes of sleep, what minute does that guard spend asleep the most?
#4) What is the ID of the guard you chose multiplied by the minute you chose?

def read_file():
    with open("input.txt") as file:
        log_lines = []
        for line in file:
            log_lines.append(line)
        log_lines.sort()
        print(log_lines)
        return log_lines


if __name__ == '__main__':
    read_file()

