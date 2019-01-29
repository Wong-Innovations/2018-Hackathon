'''
Class for various types of shifts.
Expects positions(A dictionary of positions with each position having a numeric value for 'max_rev' and 'min_num',
    revenue goal for the shift, hour of start time, minutes of start time, hours of end time, minutes of end time,
    and either 'half' or 'hour' which shows whether the revenue handled is per half-hour or hour
Times should be given in military time
'''

from math import ceil
import json




class Shift:
    def __init__(self, username, shift_name, positions, shift, unit):
        self.username = username
        self.shift_name = shift_name
        self.positions = positions
        self.shift = shift
        self.unit = unit

        self.numbers = {}

        self.length_hr = self.shift['end_time_hr'] - self.shift['start_time_hr']
        self.length_min = self.shift['end_time_min'] - self.shift['start_time_min']

        if self.length_min < 0:
            self.length_min += 60
            self.length_hr -= 1

        if self.length_hr < 0:
            self.length_hr += 24

        self.length = self.length_hr + (self.length_min / 60)

        if unit == 'hour':
            self.unit_rev_goal = self.shift['rev_goal'] / self.length
        else:
            self.unit_rev_goal = self.shift['rev_goal'] / (2 * self.length)

        for position in self.positions:
            self.numbers[position] = ceil(self.unit_rev_goal/self.positions[position]['max_rev'])
            if self.numbers[position] < self.positions[position]['min_num']:
                self.numbers[position] = self.positions[position]['min_num']

    def set_position_attr(self, position, attr, value):
        self.positions[position][attr] = value

    def get_position_attr(self, position, attr):
        return self.positions[position][attr]

    def set_shift_attr(self, attr, value):
        self.shift[attr] = value

    def get_shift_attr(self, attr):
        return self.shift[attr]

    def set_unit(self, unit):
        self.unit = unit

    def get_unit(self):
        return self.unit

    def set_numbers(self):
        for position in self.positions:
            self.numbers[position] = ceil(self.unit_rev_goal/self.positions[position]['max_rev'])
            if self.numbers[position] < self.positions[position]['min_num']:
                self.numbers[position] = self.positions[position]['min_num']

    def print_numbers(self):
        print(self.numbers)

    def store(self):
        with open('data/shifts.json') as file:
            shifts = json.load(file)

        shifts[self.username][self.shift_name]['start_time_hr'] = self.shift['start_time_hr']
        shifts[self.username][self.shift_name]['start_time_min'] = self.shift['start_time_min']
        shifts[self.username][self.shift_name]['end_time_hr'] = self.shift['end_time_hr']
        shifts[self.username][self.shift_name]['end_time_min'] = self.shift['end_time_min']
        shifts[self.username][self.shift_name]['rev_goal'] = self.shift['rev_goal']

        with open('data/shifts.json') as file:
            json.dump(shifts, file, indent=2)
