#objectives
#1) sort log entries by date/minute
#2) find the Guard# with the most minutes of sleep
#3) for the Guard# with the most minutes of sleep, what minute does that guard spend asleep the most?
#4) What is the ID of the guard you chose multiplied by the minute you chose?
import re


def read_file(filename):
    with open(filename) as file:
        log_lines = []
        for line in file:
            log_lines.append(line)
        log_lines.sort()
        return log_lines


def find_guard_that_sleeps_most(lines):
    guards_total_sleep = {}
    for line in lines:
        if 'begins shift' in line:
            guard_id = line.split()[3]
        elif 'falls asleep' in line:
            time = re.search('\d{2}:\d{2}(?=] )',line)
            start_time = time.group(0).replace("00:", "")
        elif 'wakes up' in line:
            time = re.search('\d{2}:\d{2}(?=] )',line)
            end_time = time.group(0).replace("00:", "")
            sleep_time = int(end_time) - int(start_time)
            if guard_id in guards_total_sleep:
                guards_total_sleep[guard_id] += sleep_time
            else:
                guards_total_sleep[guard_id] = sleep_time
        else:
            print("No if blocks matched for line")
    guard_with_most_sleep = ""
    otherkey, othervalue = next(iter(guards_total_sleep.items()))
    for k, v in guards_total_sleep.items():
        if v > othervalue:
            guard_with_most_sleep = k
            otherkey, othervalue = k, v
        else:
            guard_with_most_sleep = otherkey
    return guard_with_most_sleep


def most_popular_min_of_sleep_for_guard(guard_id, lines):
    minute_dict = {}
    guard_id_found = False
    for line in lines:
        if guard_id in line:
            guard_id_found = True
        elif 'falls asleep' in line and guard_id_found == True:
            time = re.search('\d{2}:\d{2}(?=] )',line)
            start_time = time.group(0).replace("00:", "")
        elif 'wakes up' in line and guard_id_found == True:
            time = re.search('\d{2}:\d{2}(?=] )',line)
            end_time = time.group(0).replace("00:", "")
            for min in range(int(start_time), int(end_time)):
                if min in minute_dict:
                    minute_dict[min] += 1
                else:
                    minute_dict[min] = 1
        else:
            guard_id_found = False

    most_popular_minute = ""
    otherkey, othervalue = next(iter(minute_dict.items()))
    for k, v in minute_dict.items():
        if int(v) > int(othervalue):
            most_popular_minute = k
            otherkey, othervalue = k, v
        else:
            most_popular_minute = otherkey
    return most_popular_minute


if __name__ == '__main__':
    lines = read_file("input.txt")
    guard_with_most_sleep = find_guard_that_sleeps_most(lines)
    minute = most_popular_min_of_sleep_for_guard(guard_with_most_sleep, lines)
    print("minute: {}".format(minute))
    guard = guard_with_most_sleep.replace("#", "")
    print("guard: {}".format(guard))
    puzzle_answer = int(guard) * minute
    print(puzzle_answer)