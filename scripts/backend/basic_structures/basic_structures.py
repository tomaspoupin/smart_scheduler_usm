from basic_structures.subroutines.sort_subjects import sort_schedule_options

class Schedule:
    'Actual representation of a schedule. formatted as a dictionary'
    days_of_week = ("Mon", "Tue", "Wen", "Thu", "Fri", "Sat")

    def __init__(self):
        self.overlaps = 0
        self.data = {
        'Mon': [0,0,0,0,0,0,0],
        'Tue': [0,0,0,0,0,0,0],
        'Wen': [0,0,0,0,0,0,0],
        'Thu': [0,0,0,0,0,0,0],
        'Fri': [0,0,0,0,0,0,0],
        'Sat': [0,0,0,0,0,0,0]}

    def change_data(self, day, block, new_state):
        if day in Schedule.days_of_week:
            if new_state == 0:
                self.data[day][block] = new_state
            elif new_state == 1:
                self.data[day][block] += new_state

    def compute_overlaps(self):
        self.overlaps = 0 # overlaps is reset to calculate new value
        for day in self.data:
            for block in range(7):
                if self.data[day][block] > 1:
                    self.overlaps += (self.data[day][block] - 1)

class Subject:
    'Actual representation of a subject.'
    SECTION = 0
    SCHEDULE = 1
    def __init__(self, code, schedule_options):
        self.code = code # Ex: DEF101
        self.schedule_options = schedule_options #tuples list, with each tuple (section, schedule)
        sort_schedule_options(self.schedule_options)
    
    def change_schedule_option(self, option, new_state): # new_state: 1 add option, 0 remove it
        option_counter = 0
        for iterable_option in self.schedule_options:
            if iterable_option[Subject.SECTION] == option[Subject.SECTION]: # index 0 is section
                if new_state == 1:
                    self.schedule_options[option_counter] = option
                elif new_state == 0:
                    self.schedule_options.pop(option_counter)
                return
            option_counter += 1
        if new_state == 1:
            self.schedule_options.append(option) # option is a tuple with (section, schedule)
            sort_schedule_options(self.schedule_options)
