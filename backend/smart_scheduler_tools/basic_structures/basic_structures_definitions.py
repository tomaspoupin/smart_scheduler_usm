#   Module name: basic_structures_definitions
#   from package: basic_structures
#   Used Modules: vector sum, empty_schedule_dict_generator
#   Description: The goal of this file is to define the fundamental
#   classes that lay the foundation of the application
#   Last Modified: 04/10/2019
#   by: LFC & TAM

import copy
from smart_scheduler_tools.basic_structures.subroutines.vector_sum import vector_sum
from smart_scheduler_tools.basic_structures.subroutines.empty_schedule_dict_generator import generate_empty_schedule_dict

class Schedule:
    'Actual representation of a schedule. formatted as a dictionary'

    def __init__(self, data=generate_empty_schedule_dict()):
        self.data = copy.deepcopy(data)   # a dictionary with the schedule data formatted as "...data[day] = block list"
        self.overlaps = 0
        self.compute_overlaps()

    # In: the schedule object
    # Out: the amount of overlaps in the schedule
    # by: TAM & LFC
    def compute_overlaps(self):
        self.overlaps = 0 # overlaps is reset to calculate new value
        for day in self.data:
            for block in range(7):
                if self.data[day][block] > 1:
                    self.overlaps += (self.data[day][block] - 1)

    # In: the schedule object and another schedule object to add its data
    # Out: the first schedule object with .data the sum of both datas
    # by: LFC 
    def add_schedule(self, added_schedule):
        if self.data.keys() == added_schedule.data.keys():
            for day in self.data:
                if len(self.data[day]) == len(added_schedule.data[day]):
                    self.data[day] = vector_sum(self.data[day], added_schedule.data[day])

    # In: the schedule object and dictionary with the schedule data to add
    # Out: the schedule with its data updated
    # by: TAM
    def load_from_dict(self, schedule_dict):
        if self.data.keys() == schedule_dict.keys():
            self.data = copy.deepcopy(schedule_dict)
            self.compute_overlaps()

    # In: the schedule object
    # Out: resets the data of the schedule object
    # by: TAM & LFC
    def clear(self):
        del self.data
        self.data = {
        'Mon': [0,0,0,0,0,0,0],
        'Tue': [0,0,0,0,0,0,0],
        'Wen': [0,0,0,0,0,0,0],
        'Thu': [0,0,0,0,0,0,0],
        'Fri': [0,0,0,0,0,0,0],
        'Sat': [0,0,0,0,0,0,0]}

    def get_dict(self):
        return copy.deepcopy(self.data)

class Subject:
    'Actual representation of a subject.'
    def __init__(self, code, schedule_options):
        self.code = code # Ex: DEF101
        self.schedule_options = copy.deepcopy(schedule_options) # dictionary of Schedule objects with sections as keys