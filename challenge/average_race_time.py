# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    races = races.splitlines()
    list_of_race_times = []
    name = "Rhines"
    for line in races:
        if name in line:
            elements = line.split()
            list_of_race_times.append(elements[0])
    return list_of_race_times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    number_of_races = len(racetimes)
    total_time = datetime.timedelta()
    for time in racetimes:
        try:
            mins, secs, ms = re.split(r'[:.]', time)
            total_time += datetime.timedelta(minutes=int(mins),
                                             seconds=int(secs), milliseconds=int(ms))
        except ValueError:
            mins, secs = re.split(r'[:.]', time)
            total_time += datetime.timedelta(minutes=int(mins),
                                             seconds=int(secs), milliseconds=int(ms))

    return f'{total_time / number_of_races}'[2:-5]


print(get_average())
