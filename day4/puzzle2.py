#objectives
#1) sort log entries by date/minute
#2) Of all guards, which guard is most frequently asleep on the same minute?
#3) What is the ID of the guard you chose multiplied by the minute you chose?
import re

guards_sleep = {}


def read_file(filename):
    with open(filename) as file:
        log_lines = []
        for line in file:
            log_lines.append(line)
        log_lines.sort()
        return log_lines


def add_guards_to_dict(lines):
    for line in lines:
       if 'begins shift' in line:
            guard_id = line.split()[3].replace("#", "")
            guards_sleep[guard_id] = []


def get_most_popular_min_for_each_guard(lines):
    for key in guards_sleep.keys():
        most_popular_minute, mins_asleep = most_popular_min_of_sleep_for_guard(key, lines)
        guards_sleep[key] = [most_popular_minute, mins_asleep]
    for k,v in guards_sleep.items():
        print(k, v)


def get_most_sleep_on_unique_min(guards_sleep):
    guard_id = 0
    minute = 0
    minute_id = 0
    for k,v in guards_sleep.items():
        print("for k,v - v[1]: {}".format(v[1]))
        if v[1] == '':
            continue
        mins_asleep = int(v[1])
        if mins_asleep > minute:
            guard_id = k
            minute = v[1]
            minute_id = int(v[0])
        else:
            continue
    print(guard_id, minute_id)
    return guard_id, minute_id


def most_popular_min_of_sleep_for_guard(guard_id, lines):
    minute_dict = {}
    guard_id_found = False
    for line in lines:
        if guard_id in line:
            guard_id_found = True
            continue
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


    most_popular_minute, mins_asleep = "", ""
    otherkey, othervalue = "", 0
    for k, v in minute_dict.items():
        if int(v) > int(othervalue):
            most_popular_minute = k
            mins_asleep = v
            otherkey, othervalue = k, v
        else:
            most_popular_minute = otherkey
            mins_asleep = othervalue
    return most_popular_minute, mins_asleep


if __name__ == '__main__':
    lines = read_file("input_partial.txt")
    add_guards_to_dict(lines)
    get_most_popular_min_for_each_guard(lines)
    guard_id, minute = get_most_sleep_on_unique_min(guards_sleep)
    print("Puzzle answer:",int(guard_id)* minute)